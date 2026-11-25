import json
from pathlib import Path

from utils.notes_index import PRACTICE_RE
from utils.study_notes import STUDY

OL = json.loads((Path(__file__).resolve().parents[1] / "data" / "lecture_outlines.json").read_text(encoding="utf-8"))
KINDS = {"md", "eq", "steps", "ex", "tip", "q"}


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


def test_practice_pages_use_question_blocks():
    """Tutorial / exam / quiz pages show questions with hidden answers, not open worked examples."""
    for doc, d in STUDY.items():
        if not PRACTICE_RE.search(d["title"]):
            continue
        kinds = [bl[0] for s in d["sections"] for bl in s["blocks"]]
        assert "q" in kinds and "ex" not in kinds, (doc, d["title"])


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


def test_ce2155_buckling_failure_numbers():
    import math
    c = (2 * 400 / (math.pi * 150e6)) ** (1 / 3)          # cast-iron shaft radius
    assert abs(c * 1000 - 11.93) < 0.01
    assert abs(0.7 * 4.0 - 2.8) < 1e-9                    # Example 2 y-y effective length


def test_materials_worked_numbers():
    # moisture adjustment
    ca, fa = 1050 * (1 - 0.005), 710 * (1 + 0.045 - 0.013)
    water = 200 + 1050 * 0.005 - 710 * (0.045 - 0.013)
    assert abs(ca - 1044.75) < 0.01 and abs(fa - 732.72) < 0.01 and abs(water - 182.53) < 0.01
    # thermal shrinkage
    assert abs(10e-6 * 15 * 20000 - 3.0) < 1e-9
    # lever rules
    assert abs((58 - 50) / (50 - 46) - 2) < 1e-9
    r = (6.7 - 0.8) / (0.8 - 0.025)
    assert abs(r - 7.61) < 0.01 and abs(r / (1 + r) - 0.884) < 0.001
    # packing factors
    import math
    assert round(math.pi / 6, 2) == 0.52 and round(math.sqrt(3) * math.pi / 8, 2) == 0.68 and round(math.sqrt(2) * math.pi / 6, 2) == 0.74


def test_consolidation_example():
    import math
    T = 1.781 - 0.933 * math.log10(100 * (1 - 1.5 / 1.61))
    assert abs(T - 1.0) < 0.02 and abs(T * 2.5 ** 2 / 0.5 - 12.5) < 0.3
    T2 = 0.5 * 2 / 2.5 ** 2
    assert abs(T2 - 0.16) < 1e-9 and abs(math.sqrt(4 * T2 / math.pi) * 1.61 - 0.72) < 0.01


def test_slope_mass_procedure_examples():
    import math
    MR = 60 * 16.5 ** 2 * math.pi / 2
    assert abs(MR - 25659) < 5
    assert abs(MR / (1.35 * 18163) - 1.05) < 0.005 and abs(MR / 1.4 / 18163 - 1.01) < 0.005
    dc = 2 * 20 / 19
    assert abs(dc - 2.1) < 0.01 and abs(0.5 * 10 * 2.1 ** 2 - 22.1) < 0.1
    c1 = 1.35 * (2777 + 64) + 1.5 * 438 - 116
    c2 = 2777 + 64 + 1.3 * 438 - 116
    assert abs(c1 - 4376) < 2 and abs(c2 - 3294) < 1
    assert abs(4518 / c1 - 1.03) < 0.005 and abs(4518 / 1.4 / c2 - 0.98) < 0.005
