import json
from pathlib import Path

from utils.study_notes import STUDY, TUTORIALS

OL = json.loads((Path(__file__).resolve().parents[1] / "data" / "lecture_outlines.json").read_text(encoding="utf-8"))
KINDS = {"md", "eq", "steps", "ex", "tip", "tut"}


def test_study_notes_follow_the_source_order_and_pages():
    for doc, d in STUDY.items():
        assert doc in OL, doc
        n = OL[doc]["page_count"]
        starts = [s["pages"][0] for s in d["sections"]]
        assert starts == sorted(starts), f"{doc} not in note order"
        for s in d["sections"]:
            a, b = s["pages"]
            assert 1 <= a <= b <= n, (doc, s["title"])
            assert s["blocks"] and all(bl[0] in KINDS for bl in s["blocks"]), s["title"]


def test_every_module_covered_and_tutorials_mapped():
    assert len(STUDY) == 9
    for tdoc, page, title, target in TUTORIALS:
        assert tdoc in OL and 1 <= page <= OL[tdoc]["page_count"] and target in STUDY, title
    assert len(TUTORIALS) == 12


def test_quoted_example_numbers_consistent():
    # Example 2.1: tau_max = T c / J with T = 80 Nm, c = 17.5 mm, J for 35 mm
    import math
    J = math.pi * 35 ** 4 / 32
    assert abs(J - 147323.5) < 1 and abs(80e3 * 17.5 / J - 9.5) < 0.05
    # Example 1.10: shortest rope 3.08 m
    th = math.asin(3000 / 13000)
    assert abs(2 * 1.5 / math.cos(th) - 3.08) < 0.01
    # Example 1.11 C–D: theta 72.54°, T 514 N
    th = math.acos(0.3)
    assert abs(math.degrees(th) - 72.54) < 0.01 and abs(981 / (2 * math.sin(th)) - 514.2) < 0.5
    # Diving board: sigma = M c / I with I = 5.1e5
    assert abs(1962e3 * 11.4 / 5.1e5 - 43.9) < 0.1
    # Pier cap midspan: -136 + (42.5 + 22.5)/2 * 2.5
    assert -136 + (42.5 + 22.5) / 2 * 2.5 == -54.75
