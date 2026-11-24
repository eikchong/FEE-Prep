"""Study-notes reader helpers: documents and sections per subject in lecture order, plus
clean-up of extracted / OCR text for on-screen reading. Content is read at runtime from
materials/ and data/library.db — nothing from the notes is stored in the repo."""
from __future__ import annotations

import re

from utils import library

BOILERPLATE = [
    r"^CE ?11\d\d\s+(Civil Engineering Principles and Practice|Statics and Mechanics of Materials)\s*$",
    r"^PE FUNDAMENTALS\s*[–-]\s*CE ?\d{3}.*$",
    r"^\d{1,2}/\d{1,2}/20\d\d$",                         # slide date stamps
    r"^CE ?1[0O]3\s+Str?uc\w*\s+An\w*.*$",                # "CE 103 Structural Analysis" footers
    r"^Source\s*:.*$",
    r"^Slide \d+$", r"^Lesson \d+-\d+\w*$",
    r"^Page \d+$", r"^\d{1,3}$",
]
_BP = [re.compile(p, re.I) for p in BOILERPLATE]


def _collapse_doubled(line: str) -> str:
    """'Sign Convention Sign Convention' → 'Sign Convention' (shadow text in some PDFs)."""
    words = line.split()
    n = len(words)
    if n >= 2 and n % 2 == 0 and words[: n // 2] == words[n // 2:]:
        return " ".join(words[: n // 2])
    return line


_PUA = re.compile(r"[\ue000-\uf8ff\u200b\ufeff\x00-\x08\x0b-\x1f]")


def _dedupe_words(line: str) -> str:
    """'then then dV dV/dx' → 'then dV/dx' (doubled shadow glyphs)."""
    words, out = line.split(" "), []
    for w in words:
        if out and (w == out[-1] or (len(out[-1]) > 1 and w.startswith(out[-1]) and len(w) > len(out[-1]))
                    and out[-1] == w[:len(out[-1])] and len(out) and w not in ("=",)):
            if w != out[-1]:
                out[-1] = w   # keep the longer token
            continue
        out.append(w)
    return " ".join(out)


def clean_text(text: str) -> str:
    text = _PUA.sub("", text)
    out, recent = [], []
    for raw in text.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if len(line) <= 1 or any(p.match(line) for p in _BP):
            continue
        line = _dedupe_words(_collapse_doubled(line))
        if line in recent:   # shadow copy of a recent line
            continue
        out.append(line)
        recent = (recent + [line])[-3:]
    # re-flow: join wrapped lines that do not end a sentence/heading
    para, buf = [], ""
    for line in out:
        if buf and (buf.endswith(("-",)) and not buf.endswith(" -")):
            buf = buf[:-1] + line
        elif buf and not re.search(r"[.:;?!)]$", buf) and line[:1].islower():
            buf += " " + line
        else:
            if buf:
                para.append(buf)
            buf = line
    if buf:
        para.append(buf)
    return "\n".join(para)


def documents_for(code: str, docs_in_db: list[dict]) -> list[dict]:
    """[{path, title, pages, sections:[{title, pages:[a,b]}], ocr}] in study order for a subject."""
    ol = library.outlines()
    have = {d["path"]: d for d in docs_in_db}
    out = []
    for path, o in ol.items():
        if path not in have:
            continue
        if o.get("code") == code:   # the subject's own file: every section, incl. untagged intro pages
            secs = list(o["sections"])
        else:                       # other files (e.g. the fluids compilation): sections tagged to this subject
            secs = [s for s in o["sections"] if any(t.startswith(code + "-") for t in s["topics"])]
        if secs:
            out.append({"path": path, "title": o.get("title", path), "seq": o.get("seq", 99),
                        "pages": have[path]["pages"], "sections": secs})
    # documents in the subject folder without an outline: one section per 10 pages
    for d in docs_in_db:
        if d["code"] == code and d["path"] not in ol and not d["path"].startswith("_past_papers/"):
            n = d["pages"]
            secs = [{"title": f"Pages {a}–{min(a + 9, n)}", "pages": [a, min(a + 9, n)], "topics": []}
                    for a in range(1, n + 1, 10)]
            out.append({"path": d["path"], "title": d["title"], "seq": 50, "pages": n, "sections": secs})
    return sorted(out, key=lambda x: (x["seq"], x["path"]))
