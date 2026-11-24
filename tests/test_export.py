import pymupdf

from utils import export
from utils.formulas import FORMULAS


def test_all_formulas_render():
    for code, fs in FORMULAS.items():
        for f in fs:
            assert export.latex_png(f["latex"])[:4] == b"\x89PNG", (code, f["title"])


def test_markdown_and_pdf():
    idx = {"CE202": {"CE202-06": {"CE202/steel.pdf": [2, 3, 4, 9]}}}
    pins = [{"code": "CE202", "topic_id": "CE202-06", "doc": "CE202/steel.pdf", "page": 3, "excerpt": "C1 = 1.127"}]
    md = export.to_markdown(None, {"CE202": "my note"}, pins, idx)
    assert "## Binder index" in md and "CE202/steel.pdf — p. 2–4, 9" in md
    assert "(CE202/steel.pdf, p. 3)" in md and "my note" in md
    assert "verify against Singapore NA" in md
    pdf = export.to_pdf(["CE201", "CE202"], {"CE202": "my note"}, pins, idx)
    doc = pymupdf.open(stream=pdf)
    text = "".join(p.get_text() for p in doc)
    assert "Binder index" in text and "Formula & Code Sheet" in text
    assert f"1/{doc.page_count}" in text


def test_page_ranges():
    assert export.page_ranges([5, 1, 2, 3, 7]) == "1–3, 5, 7"
