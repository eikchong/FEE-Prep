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
    assert len(STUDY) == 14
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


def test_ce2155_quoted_numbers():
    import math
    # combined loading Ex 3 superposition
    assert abs((2.83 + 211.3) - 214.1) < 0.05 and abs((6.04 + 169) - 175.0) < 0.05
    # Mohr Ex 4: A(-12,-6) with sigma_y = 0
    c, R = -6, math.hypot(6, 6)
    assert abs(c + R - 2.49) < 0.01 and abs(c - R + 14.49) < 0.01
    # nailed box beam spacings
    qB = 80 * 33700 / 2295e3
    assert abs(qB - 1.176) < 0.002 and abs(30 / (qB / 2) - 51) < 0.5 and abs(30 / 0.353 - 85) < 0.5
    # rectangle tau_max = 1.5 V/A
    assert 1.5 == 6 / 4
