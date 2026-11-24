"""Study-materials library: ingestion, auto-tagging and FTS5 search over materials/.

Tables (data/library.db):
  documents(id, path UNIQUE, code, title, pages, hash, added)
  pages(doc_id, page_no, text, ocr)            -- page_no is 1-based
  pages_fts(text, doc_id UNINDEXED, page_no UNINDEXED)   -- FTS5 index
  page_tags(path, page_no, topic_id, source, confidence)
       source: 'auto' | 'add' (manual add) | 'remove' (manual removal of an auto tag)
Manual tags are keyed by path so they survive re-ingestion of a changed file.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import sqlite3
from contextlib import closing
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import config
from utils.syllabus import subject_map, topic_map

SUPPORTED = {".pdf", ".docx", ".pptx", ".md", ".txt", ".png", ".jpg", ".jpeg"}
TEXT_CHUNK = 3000            # chars per pseudo-page for docx/md/txt
AUTO_MIN_SCORE = 2           # keyword hits needed for an auto tag
PREFIX_RE = re.compile(r"^(CE\d{3})-(\d{2})", re.I)
CODE_RE = re.compile(r"^CE\d{3}$", re.I)

SCHEMA = """
CREATE TABLE IF NOT EXISTS documents(
  id INTEGER PRIMARY KEY, path TEXT UNIQUE, code TEXT, title TEXT, pages INTEGER,
  hash TEXT, added TEXT);
CREATE TABLE IF NOT EXISTS pages(
  doc_id INTEGER, page_no INTEGER, text TEXT, ocr INTEGER DEFAULT 0,
  PRIMARY KEY(doc_id, page_no));
CREATE VIRTUAL TABLE IF NOT EXISTS pages_fts USING fts5(
  text, doc_id UNINDEXED, page_no UNINDEXED, tokenize='porter unicode61');
CREATE TABLE IF NOT EXISTS page_tags(
  path TEXT, page_no INTEGER, topic_id TEXT, source TEXT, confidence REAL,
  PRIMARY KEY(path, page_no, topic_id, source));
"""


def db_path() -> Path:
    return config.DATA_DIR / "library.db"


def connect(path: Path | None = None) -> sqlite3.Connection:
    p = Path(path or db_path())
    p.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(p)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


# ------------------------------------------------------------------ extraction
def _ocr_image(img_bytes: bytes) -> str | None:
    try:
        import pytesseract
        from PIL import Image
        return pytesseract.image_to_string(Image.open(io.BytesIO(img_bytes)))
    except Exception:  # tesseract binary missing or failed
        return None


def _chunks(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return [""]
    out, buf = [], ""
    for para in re.split(r"\n\s*\n", text):
        if len(buf) + len(para) > TEXT_CHUNK and buf:
            out.append(buf)
            buf = ""
        buf += para + "\n\n"
    if buf:
        out.append(buf)
    return out


def extract_pages(path: Path) -> list[tuple[str, bool]]:
    """Return [(text, ocr_flag)] per page/slide/chunk (1 entry = 1 'page')."""
    ext = path.suffix.lower()
    if ext == ".pdf":
        import pymupdf as fitz
        pages = []
        with fitz.open(path) as doc:
            for pg in doc:
                txt = pg.get_text("text") or ""
                if len(txt.strip()) < 20:  # scanned / image page → OCR
                    ocr = _ocr_image(pg.get_pixmap(dpi=200).tobytes("png"))
                    pages.append(((ocr or txt), True))
                else:
                    pages.append((txt, False))
        return pages
    if ext == ".docx":
        import docx
        d = docx.Document(str(path))
        parts = [p.text for p in d.paragraphs]
        for t in d.tables:
            for row in t.rows:
                parts.append(" | ".join(c.text for c in row.cells))
        return [(c, False) for c in _chunks("\n".join(parts))]
    if ext == ".pptx":
        from pptx import Presentation
        prs = Presentation(str(path))
        out = []
        for slide in prs.slides:
            txt = []
            for shp in slide.shapes:
                if shp.has_text_frame:
                    txt.append(shp.text_frame.text)
            if slide.has_notes_slide:
                txt.append(slide.notes_slide.notes_text_frame.text)
            out.append(("\n".join(txt), False))
        return out or [("", False)]
    if ext in (".md", ".txt"):
        return [(c, False) for c in _chunks(path.read_text(encoding="utf-8", errors="ignore"))]
    if ext in (".png", ".jpg", ".jpeg"):
        return [((_ocr_image(path.read_bytes()) or ""), True)]
    raise ValueError(f"unsupported file type: {ext}")


# ------------------------------------------------------------------ tagging
def _keywords() -> dict[str, list[str]]:
    syn = json.loads((config.STATIC_DATA_DIR / "topic_keywords.json").read_text(encoding="utf-8"))
    out = {}
    for tid, t in topic_map().items():
        name = t["name"].lower()
        # the full sub-topic name, plus distinctive pieces split on punctuation
        # (multi-word only: single generic words like "buckling" over-tag; put those in synonyms)
        pieces = [p.strip() for p in re.split(r"[,&()/;]| and ", name) if len(p.strip().split()) >= 2]
        out[tid] = sorted({name, *pieces, *[s.lower() for s in syn.get(tid, [])]})
    return out


def _count(text: str, kw: str) -> int:
    """Occurrences of kw starting at a word boundary (so 'restrained beam' does not match
    'unrestrained beams'); short tokens (e.g. 'ssd', 'cv') must also end at a boundary."""
    tail = r"(?![\w])" if len(kw) <= 4 else ""
    return len(re.findall(rf"(?<![\w]){re.escape(kw)}{tail}", text))


def auto_tags(text: str, code: str | None, keywords: dict[str, list[str]] | None = None,
              forced: str | None = None) -> dict[str, float]:
    """Return {topic_id: confidence 0..1}. Folder code restricts candidates."""
    keywords = keywords or _keywords()
    low = text.lower()
    cands = [t for t in keywords if not code or t.startswith(code + "-")]
    tags: dict[str, float] = {}
    for tid in cands:
        score = sum(_count(low, kw) * (2 if " " in kw else 1) for kw in keywords[tid])
        if score >= AUTO_MIN_SCORE:
            conf = min(1.0, score / 8)
            tags[tid] = round(conf if code else conf * 0.7, 2)  # less sure without folder code
    if forced:
        tags[forced] = 1.0
    return tags


# ------------------------------------------------------------------ ingestion
@dataclass
class IngestReport:
    added: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    failed: list[tuple[str, str]] = field(default_factory=list)
    ocr_pages: int = 0
    ocr_missing: int = 0
    gaps: list[str] = field(default_factory=list)

    def summary(self) -> str:
        return (f"{len(self.added)} added · {len(self.updated)} updated · {len(self.skipped)} unchanged · "
                f"{len(self.removed)} removed · {len(self.failed)} failed · {self.ocr_pages} OCR pages")


def _hash(p: Path) -> str:
    h = hashlib.sha1()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(rel: Path) -> tuple[str | None, str | None]:
    """(subject code or None, forced topic id or None) from folder + filename prefix."""
    folder = rel.parts[0] if len(rel.parts) > 1 else ""
    code = folder.upper() if CODE_RE.match(folder) and folder.upper() in subject_map() else None
    forced = None
    m = PREFIX_RE.match(rel.name)
    if m:
        tid = f"{m.group(1).upper()}-{m.group(2)}"
        if tid in topic_map():
            forced = tid
            code = code or m.group(1).upper()
    return code, forced


def ingest(materials: Path | None = None, con: sqlite3.Connection | None = None,
           progress_cb=None) -> IngestReport:
    root = Path(materials or config.MATERIALS_DIR)
    own = con is None
    con = con or connect()
    rep = IngestReport()
    kw = _keywords()
    files = sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED
                   and not any(part.startswith(".") for part in p.relative_to(root).parts))
    seen = set()
    for i, f in enumerate(files):
        rel = f.relative_to(root)
        key = rel.as_posix()
        seen.add(key)
        if progress_cb:
            progress_cb(i / max(1, len(files)), key)
        h = _hash(f)
        row = con.execute("SELECT id, hash FROM documents WHERE path=?", (key,)).fetchone()
        if row and row["hash"] == h:
            rep.skipped.append(key)
            continue
        try:
            pages = extract_pages(f)
        except Exception as e:  # keep going on a bad file
            rep.failed.append((key, str(e)))
            continue
        code, forced = classify(rel)
        if row:
            _delete_doc(con, row["id"], key, keep_manual=True)
            rep.updated.append(key)
        else:
            rep.added.append(key)
        cur = con.execute("INSERT INTO documents(path, code, title, pages, hash, added) VALUES(?,?,?,?,?,?)",
                          (key, code, f.stem, len(pages), h, datetime.now().isoformat(timespec="seconds")))
        doc_id = cur.lastrowid
        for n, (text, ocr) in enumerate(pages, start=1):
            if ocr:
                rep.ocr_pages += 1
                if not text.strip():
                    rep.ocr_missing += 1
            con.execute("INSERT INTO pages VALUES(?,?,?,?)", (doc_id, n, text, int(ocr)))
            con.execute("INSERT INTO pages_fts(text, doc_id, page_no) VALUES(?,?,?)", (text, doc_id, n))
            for tid, conf in auto_tags(text, code, kw, forced).items():
                con.execute("INSERT OR REPLACE INTO page_tags VALUES(?,?,?,?,?)", (key, n, tid, "auto", conf))
        con.commit()
    # remove deleted files
    for row in con.execute("SELECT id, path FROM documents").fetchall():
        if row["path"] not in seen:
            _delete_doc(con, row["id"], row["path"], keep_manual=False)
            rep.removed.append(row["path"])
    con.commit()
    rep.gaps = coverage_gaps(con)
    if own:
        con.close()
    return rep


def _delete_doc(con, doc_id: int, path: str, keep_manual: bool):
    con.execute("DELETE FROM pages WHERE doc_id=?", (doc_id,))
    con.execute("DELETE FROM pages_fts WHERE doc_id=?", (doc_id,))
    con.execute("DELETE FROM documents WHERE id=?", (doc_id,))
    if keep_manual:
        con.execute("DELETE FROM page_tags WHERE path=? AND source='auto'", (path,))
    else:
        con.execute("DELETE FROM page_tags WHERE path=?", (path,))


# ------------------------------------------------------------------ queries
EFFECTIVE_TAGS = """
SELECT path, page_no, topic_id, MAX(confidence) AS confidence, MAX(source='add') AS manual
FROM page_tags t
WHERE source IN ('auto','add')
  AND NOT EXISTS (SELECT 1 FROM page_tags r WHERE r.source='remove' AND r.path=t.path
                  AND r.page_no=t.page_no AND r.topic_id=t.topic_id)
GROUP BY path, page_no, topic_id
"""


def topic_page_counts(con) -> dict[str, int]:
    rows = con.execute(f"""SELECT e.topic_id, COUNT(*) n FROM ({EFFECTIVE_TAGS}) e
                           JOIN documents d ON d.path=e.path GROUP BY e.topic_id""").fetchall()
    return {r["topic_id"]: r["n"] for r in rows}


def coverage_gaps(con) -> list[str]:
    counts = topic_page_counts(con)
    return [tid for tid in topic_map() if counts.get(tid, 0) == 0]


def page_tags(con, path: str, page_no: int) -> list[dict]:
    rows = con.execute(f"SELECT * FROM ({EFFECTIVE_TAGS}) WHERE path=? AND page_no=? ORDER BY topic_id",
                       (path, page_no)).fetchall()
    return [dict(r) for r in rows]


def set_page_tags(con, path: str, page_no: int, topic_ids: list[str]) -> None:
    """Manual override: the effective tag set for this page becomes exactly `topic_ids`.

    Every saved decision is recorded as manual ('add' / 'remove') so it survives re-scans,
    including auto tags the user chose to keep."""
    wanted = set(topic_ids)
    known = {r["topic_id"] for r in con.execute(
        "SELECT topic_id FROM page_tags WHERE path=? AND page_no=?", (path, page_no))}
    for tid in wanted:
        con.execute("DELETE FROM page_tags WHERE path=? AND page_no=? AND topic_id=? AND source='remove'",
                    (path, page_no, tid))
        con.execute("INSERT OR REPLACE INTO page_tags VALUES(?,?,?,?,?)", (path, page_no, tid, "add", 1.0))
    for tid in known - wanted:
        con.execute("DELETE FROM page_tags WHERE path=? AND page_no=? AND topic_id=? AND source='add'",
                    (path, page_no, tid))
        con.execute("INSERT OR REPLACE INTO page_tags VALUES(?,?,?,?,?)", (path, page_no, tid, "remove", 1.0))
    con.commit()


def _fts_query(q: str) -> str:
    q = q.strip()
    if any(op in q for op in ('"', " OR ", " NOT ", " NEAR(")):
        return q  # user wrote an FTS expression
    toks = re.findall(r"[\w′'.,-]+", q)
    return " ".join('"' + t.replace('"', "") + '"' for t in toks)


def search(con, query: str = "", code: str | None = None, topic_id: str | None = None,
           path: str | None = None, limit: int = 50) -> list[dict]:
    where, args = [], []
    if code and not topic_id:
        where.append(f"(d.code = ? OR EXISTS (SELECT 1 FROM ({EFFECTIVE_TAGS}) e WHERE e.path=d.path "
                     "AND e.page_no=p.page_no AND e.topic_id LIKE ?))")
        args += [code, code + "-%"]
    if path:
        where.append("d.path = ?")
        args.append(path)
    if topic_id:
        where.append(f"EXISTS (SELECT 1 FROM ({EFFECTIVE_TAGS}) e WHERE e.path=d.path "
                     "AND e.page_no=p.page_no AND e.topic_id=?)")
        args.append(topic_id)
    if query.strip():
        sql = f"""SELECT d.path, d.title, d.code, p.page_no, p.ocr,
                    snippet(pages_fts, 0, '**', '**', ' … ', 14) AS snippet, bm25(pages_fts) AS rank
                  FROM pages_fts f JOIN documents d ON d.id = f.doc_id
                  JOIN pages p ON p.doc_id = f.doc_id AND p.page_no = f.page_no
                  WHERE pages_fts MATCH ? {''.join(' AND ' + w for w in where)}
                  ORDER BY rank LIMIT ?"""
        try:
            rows = con.execute(sql, [_fts_query(query), *args, limit]).fetchall()
        except sqlite3.OperationalError:
            rows = con.execute(sql, [_fts_query(re.sub(r"[^\w\s]", " ", query)), *args, limit]).fetchall()
    else:
        sql = f"""SELECT d.path, d.title, d.code, p.page_no, p.ocr,
                    substr(replace(p.text, char(10), ' '), 1, 220) AS snippet, 0 AS rank
                  FROM pages p JOIN documents d ON d.id = p.doc_id
                  {'WHERE ' + ' AND '.join(where) if where else ''}
                  ORDER BY d.path, p.page_no LIMIT ?"""
        rows = con.execute(sql, [*args, limit]).fetchall()
    return [dict(r) for r in rows]


def documents(con) -> list[dict]:
    return [dict(r) for r in con.execute("SELECT * FROM documents ORDER BY path")]


def page_text(con, path: str, page_no: int) -> str:
    r = con.execute("""SELECT p.text FROM pages p JOIN documents d ON d.id=p.doc_id
                       WHERE d.path=? AND p.page_no=?""", (path, page_no)).fetchone()
    return r["text"] if r else ""


def abs_path(rel: str) -> Path:
    return config.MATERIALS_DIR / rel


def safe_counts() -> dict[str, int]:
    """Topic page counts, or {} if the library has never been built."""
    if not db_path().exists():
        return {}
    with closing(connect()) as con:
        return topic_page_counts(con)
