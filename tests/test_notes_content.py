"""Lecture-note content: outlines, formula-sheet citations, legacy separation, rendering."""
import json
from pathlib import Path

import pytest

from utils import export
from utils.formulas import LEGACY, all_items, legacy_items, sections
from utils.syllabus import topic_map

DATA = Path(__file__).resolve().parents[1] / "data"
OL = json.loads((DATA / "lecture_outlines.json").read_text(encoding="utf-8"))
NOTE_CODES = ["CE101", "CE102", "CE103", "CE105", "CE205"]


def test_outlines_valid_and_in_order():
    for doc, o in OL.items():
        prev = 0
        for s in o["sections"]:
            a, b = s["pages"]
            assert 1 <= a <= b <= o["page_count"], (doc, s["title"])
            assert a >= prev - 1, f"{doc}: '{s['title']}' out of lecture order"
            prev = a
            assert all(t in topic_map() for t in s["topics"]), s["title"]


@pytest.mark.parametrize("code", NOTE_CODES)
def test_sheet_entries_cite_real_pages_in_lecture_order(code):
    secs = [s for s in sections(code) if s.get("src")]
    assert secs, code
    pages = [s["src"]["page"] for s in secs]
    assert pages == sorted(pages), f"{code} sections not in lecture order: {pages}"
    for s in secs:
        for f in s["items"]:
            assert f["src"], (code, f["title"])
            assert f["src"]["doc"] in OL
            assert 1 <= f["src"]["page"] <= OL[f["src"]["doc"]]["page_count"]


@pytest.mark.parametrize("code", NOTE_CODES)
def test_sheet_latex_renders(code):
    for f in all_items(code):
        if f["latex"]:
            assert export.latex_png(f["latex"])[:4] == b"\x89PNG", f["title"]


def test_legacy_kept_off_the_sheet():
    assert LEGACY["CE201"] and all(f["legacy"] for f in LEGACY["CE201"])
    for code in ("CE201", "CE202"):
        assert legacy_items(code)
        assert not any(f.get("legacy") for f in all_items(code))
        md = export.to_markdown([code], index={})
        assert "0.156" not in md and "BS 8110 singly" not in md


def test_markdown_export_has_sections_and_citations():
    md = export.to_markdown(["CE205"], index={})
    assert "### 5 · Weirs & gates" in md
    assert "(CE105_Pressure_and_Fluid_Statics.pdf, p. 92)" in md
