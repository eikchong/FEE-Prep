"""Formula-sheet export: Markdown and printable PDF (A4) with binder index."""
from __future__ import annotations

import io
from collections import defaultdict
from contextlib import closing
from datetime import date
from functools import lru_cache
from pathlib import Path

import config
from utils.formulas import LEGACY_NOTE, codes as formula_codes, sections
from utils.syllabus import subject_map, topic_map

VERIFY = "⚠ verify against Singapore NA"


def page_ranges(pages: list[int]) -> str:
    pages = sorted(set(pages))
    out, start, prev = [], None, None
    for p in pages:
        if start is None:
            start = prev = p
        elif p == prev + 1:
            prev = p
        else:
            out.append(f"{start}" if start == prev else f"{start}–{prev}")
            start = prev = p
    if start is not None:
        out.append(f"{start}" if start == prev else f"{start}–{prev}")
    return ", ".join(out)


def binder_index(min_conf: float = 0.0) -> dict[str, dict[str, dict[str, list[int]]]]:
    """code -> topic_id -> path -> [pages] from the library's effective tags."""
    from utils import library
    idx: dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    if not library.db_path().exists():
        return {}
    with closing(library.connect()) as con:
        rows = con.execute(f"SELECT e.* FROM ({library.EFFECTIVE_TAGS}) e JOIN documents d ON d.path=e.path").fetchall()
    for r in rows:
        if r["confidence"] >= min_conf or r["manual"]:
            t = topic_map().get(r["topic_id"])
            if t:
                idx[t["code"]][r["topic_id"]][r["path"]].append(r["page_no"])
    return idx


def _codes(codes):
    return codes or formula_codes()


def cite(src: dict | None) -> str:
    """'(CE101_Mechanics_of_Materials.pdf, p. 12)' — the binder-tab reference."""
    if not src:
        return ""
    return f"({Path(src['doc']).name}, p. {src['page']})"


def to_markdown(codes: list[str] | None = None, notes: dict | None = None, pins: list | None = None,
                index: dict | None = None) -> str:
    notes, pins = notes or {}, pins or []
    index = binder_index() if index is None else index
    L = [f"# FEE 2027 (Civil) — Formula & Code Sheet", "",
         f"_Exam {config.EXAM_DATE:%a %d %b %Y} · generated {date.today():%d %b %Y}_", "",
         f"> {config.CODES_RULE}  ", f"> {LEGACY_NOTE}", ""]
    for code in _codes(codes):
        s = subject_map()[code]
        L += [f"## {code} {s['name']}", ""]
        for sec in sections(code):
            if sec["title"]:
                L += [f"### {sec['title']}" + (f" _{cite(sec.get('src'))}_" if sec.get("src") else ""), ""]
            for f in sec["items"]:
                meta = " · ".join(x for x in [f["clause"], f["note"], VERIFY if f["verify"] else "",
                                              cite(f.get("src"))] if x)
                if f["latex"]:
                    L += [f"**{f['title']}**" + (f" — {meta}" if meta else ""), "", f"$$ {f['latex']} $$", ""]
                else:
                    L += [f"- **{f['title']}** — {meta}"]
            L.append("")
        sp = [p for p in pins if p.get("code") == code]
        if sp:
            L += ["### Pinned excerpts", ""]
            for p in sp:
                ex = p.get("excerpt", "").strip().replace("\n", " ")
                L += [f"- {ex} _({p['doc']}, p. {p['page']})_"]
            L.append("")
        if notes.get(code, "").strip():
            L += ["### My notes", "", notes[code].strip(), ""]
    if index:
        L += ["## Binder index", "", "_Subject → sub-topic → file & pages (tab your printed notes)_", ""]
        for code in _codes(codes):
            if code not in index:
                continue
            L += [f"### {code} {subject_map()[code]['name']}", ""]
            for tid in sorted(index[code]):
                L.append(f"- **{tid} {topic_map()[tid]['name']}**")
                for path, pgs in sorted(index[code][tid].items()):
                    L.append(f"    - {path} — p. {page_ranges(pgs)}")
            L.append("")
    return "\n".join(L)


# ------------------------------------------------------------------ PDF
@lru_cache(maxsize=512)
def latex_png(latex: str, fontsize: int = 14) -> bytes:
    """Render a mathtext expression to PNG bytes (raises on unsupported syntax)."""
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib import mathtext
    from matplotlib.font_manager import FontProperties
    buf = io.BytesIO()
    mathtext.math_to_image(f"${latex}$", buf, prop=FontProperties(size=fontsize), dpi=220, format="png")
    return buf.getvalue()


def _font_paths() -> tuple[str, str]:
    import matplotlib
    d = Path(matplotlib.get_data_path()) / "fonts" / "ttf"
    return str(d / "DejaVuSans.ttf"), str(d / "DejaVuSans-Bold.ttf")


def to_pdf(codes: list[str] | None = None, notes: dict | None = None, pins: list | None = None,
           index: dict | None = None) -> bytes:
    from fpdf import FPDF
    from PIL import Image

    notes, pins = notes or {}, pins or []
    index = binder_index() if index is None else index
    reg, bold = _font_paths()

    class SheetPDF(FPDF):
        def footer(self):
            self.set_y(-10)
            self.set_font("DejaVu", "", 7)
            self.set_text_color(120, 120, 120)
            self.cell(0, 4, f"FEE 2027 Civil · formula & code sheet · {date.today():%d %b %Y} · "
                            f"{self.page_no()}/{{nb}}", align="C")
            self.set_text_color(0, 0, 0)

    pdf = SheetPDF(format="A4")
    pdf.set_auto_page_break(True, margin=14)
    pdf.add_font("DejaVu", "", reg)
    pdf.add_font("DejaVu", "B", bold)
    pdf.set_margins(14, 14, 14)

    pdf.add_page()
    pdf.set_font("DejaVu", "B", 18)
    pdf.cell(0, 10, "FEE 2027 (Civil) — Formula & Code Sheet", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 9)
    pdf.multi_cell(0, 5, f"Exam {config.EXAM_DATE:%a %d %b %Y}. {config.CODES_RULE}\n{LEGACY_NOTE}\n"
                         "Items marked ⚠ depend on Nationally Determined Parameters — verify against the Singapore NA.")
    W = pdf.w - pdf.l_margin - pdf.r_margin

    for code in _codes(codes):
        s = subject_map()[code]
        color = config.COLOR_P1 if s["part"] == 1 else config.COLOR_P2
        r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
        if pdf.get_y() > pdf.h - 60:
            pdf.add_page()
        pdf.ln(3)
        pdf.set_fill_color(r, g, b)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 8, f"  {code} {s['name']}", fill=True, new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(1)
        for sec in sections(code):
            if sec["title"]:
                if pdf.get_y() > pdf.h - 40:
                    pdf.add_page()
                pdf.ln(1)
                pdf.set_font("DejaVu", "B", 10.5)
                pdf.set_text_color(r, g, b)
                pdf.multi_cell(0, 5.5, sec["title"] + (f"   {cite(sec.get('src'))}" if sec.get("src") else ""),
                               new_x="LMARGIN", new_y="NEXT")
                pdf.set_text_color(0, 0, 0)
            for f in sec["items"]:
                meta = " · ".join(x for x in [f["clause"], f["note"], cite(f.get("src"))] if x)
                title = f["title"] + ("  ⚠ verify NA" if f["verify"] else "")
                if not f["latex"]:   # text-only key point
                    if pdf.get_y() + 10 > pdf.h - 14:
                        pdf.add_page()
                    pdf.set_font("DejaVu", "B", 9)
                    pdf.multi_cell(0, 4.4, "• " + title, new_x="LMARGIN", new_y="NEXT")
                    if meta:
                        pdf.set_x(pdf.l_margin + 3)
                        pdf.set_font("DejaVu", "", 8)
                        pdf.set_text_color(70, 70, 70)
                        pdf.multi_cell(W - 3, 4, meta, new_x="LMARGIN", new_y="NEXT")
                        pdf.set_text_color(0, 0, 0)
                    pdf.ln(0.8)
                    continue
                png = latex_png(f["latex"])
                im = Image.open(io.BytesIO(png))
                w_mm, h_mm = im.width / 220 * 25.4, im.height / 220 * 25.4
                if w_mm > W:
                    h_mm, w_mm = h_mm * W / w_mm, W
                need = 6 + h_mm + (4 if meta else 0)
                if pdf.get_y() + need > pdf.h - 14:
                    pdf.add_page()
                pdf.set_font("DejaVu", "B", 9.5)
                pdf.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
                pdf.image(io.BytesIO(png), x=pdf.l_margin + 3, w=w_mm, h=h_mm)
                if meta:
                    pdf.set_font("DejaVu", "", 8)
                    pdf.set_text_color(90, 90, 90)
                    pdf.multi_cell(0, 4, meta, new_x="LMARGIN", new_y="NEXT")
                    pdf.set_text_color(0, 0, 0)
                pdf.ln(1.5)
        sp = [p for p in pins if p.get("code") == code]
        if sp:
            pdf.set_font("DejaVu", "B", 10)
            pdf.cell(0, 6, "Pinned excerpts", new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("DejaVu", "", 8.5)
            for p in sp:
                ex = p.get("excerpt", "").strip().replace("\n", " ")
                pdf.multi_cell(0, 4.2, f"• {ex}  ({p['doc']}, p. {p['page']})", new_x="LMARGIN", new_y="NEXT")
        if notes.get(code, "").strip():
            pdf.set_font("DejaVu", "B", 10)
            pdf.cell(0, 6, "My notes", new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("DejaVu", "", 8.5)
            pdf.multi_cell(0, 4.2, notes[code].strip(), new_x="LMARGIN", new_y="NEXT")

    if index:
        pdf.add_page()
        pdf.set_font("DejaVu", "B", 14)
        pdf.cell(0, 8, "Binder index", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("DejaVu", "", 8.5)
        pdf.cell(0, 5, "Subject → sub-topic → file & pages", new_x="LMARGIN", new_y="NEXT")
        for code in _codes(codes):
            if code not in index:
                continue
            pdf.ln(2)
            pdf.set_font("DejaVu", "B", 10.5)
            pdf.cell(0, 6, f"{code} {subject_map()[code]['name']}", new_x="LMARGIN", new_y="NEXT")
            for tid in sorted(index[code]):
                pdf.set_font("DejaVu", "B", 8.5)
                pdf.multi_cell(0, 4.4, f"{tid}  {topic_map()[tid]['name']}", new_x="LMARGIN", new_y="NEXT")
                pdf.set_font("DejaVu", "", 8)
                for path, pgs in sorted(index[code][tid].items()):
                    pdf.set_x(pdf.l_margin + 5)
                    pdf.multi_cell(W - 5, 4, f"{path} — p. {page_ranges(pgs)}", new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())
