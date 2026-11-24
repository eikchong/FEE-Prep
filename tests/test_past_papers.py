"""Past-paper index: schema, page pointers, and every computed answer re-derived."""
import math

import pytest

from utils import calcs as c
from utils import pastpapers as pp
from utils.library import unshift_if_garbled
from utils.syllabus import topic_map

ITEMS = pp.items()
BY = {q["id"]: q for q in ITEMS}


def test_schema():
    ids = [q["id"] for q in ITEMS]
    assert len(ids) == len(set(ids))
    for q in ITEMS:
        assert q["topics"] and all(t in topic_map() for t in q["topics"]), q["id"]
        assert q["appearances"]
        for a in q["appearances"]:
            assert a["doc"] in pp.docs() and a["page"] >= 1
        if q["part"] == 1:
            assert q["answer"] is None or 0 <= q["answer"] < 4
            assert q["answer_source"] in ("computed", "reasoned", "candidate")
            assert q["explain"].strip()
        else:
            assert q["approach"]


def test_frequency_counts_repeats():
    f = pp.frequency(2)
    assert f["CE204"] >= 4          # vertical curves 2017/2020/2026 + 2019 recollection
    assert pp.topic_frequency()["CE202-05"] == 3


# ---- options (numbers only) as printed in the papers, used to check the keyed letter
P1_CHECKS = {
    "PP1-truss-elongation": ((0.76, 0.95, 1.43, 1.91),
                             lambda: (75 * 1.5 / 0.9) * 1.2 / 1.5 * 1e3 * 1200 / (math.pi * 100 * 200e3)),
    "PP1-composite-column": ((168, 88, 44, 11), lambda: 200e3 * 1e6 / (25e9 * 0.067 + 200e9 * 0.003)),
    "PP1-soil-sample": ((18.5, 16.7, 15.4, 11.5), lambda: 333 / 196 * 9.81 / 1.45),
    "PP1-bernoulli-reducer": ((98500, 92500, 68500, None), lambda: 100000 - 1000 * (4 ** 2 - 1) / 2),
    "PP1-inclined-circular-gate": ((6576, 3582, 2724, None),
                                   lambda: 1000 * 9.81 * math.pi / 4 * (0.5 + 0.5 * math.sin(math.pi / 4))),
    "PP1-stepped-bar-ratio": ((1.96, 2.33, 5.44, 2.77), lambda: (35 / 15) ** 2),
    "PP1-column-steel-force": ((1.96, 2.74, 2.96, 1.74), lambda: 10 * 200 * 210 / (200 * 210 + 1e4 * 20)),
    "PP1-overhang-upward-deflection": ((0.25, 1 / math.sqrt(3), 0.5, 2 / math.sqrt(3)), lambda: math.sqrt(1 / 3)),
    "PP1-riverbed-effective-stress": ((30, 60, 90, 120), lambda: (20 - 10) * 3),
    "PP1-inclined-manometer": ((19620, 13873, 16991, None), lambda: 9810 * 2 * math.cos(math.pi / 4)),
    "PP1-froude-model-velocity": ((10, 158.1, 2.24, None), lambda: 0.5 * math.sqrt(20)),
    "PP1-19-friction-blocks": ((None, 736, 1030, None), lambda: 0.3 * 9.81 * (100 + 250)),
    "PP1-19-overhang-n": ((1.0, 1.5, 2.0, 3.0), lambda: 18 * (1 / 2 - 1 / 3)),
    "PP1-19-pitot": ((0, 4.43, None, None), lambda: math.sqrt(2 * 9.81 * 1)),
}


@pytest.mark.parametrize("qid", sorted(P1_CHECKS))
def test_part1_numeric_keys(qid):
    opts, f = P1_CHECKS[qid]
    v = f()
    q = BY[qid]
    keyed = opts[q["answer"]]
    assert keyed is not None and abs(keyed - v) / abs(v) < 0.01, f"{qid}: computed {v:.4g}, keyed {keyed}"


def test_soil_sample_saturation():
    gd = 333 / 196 * 9.81 / 1.45
    e = 2.65 * 9.81 / gd - 1
    assert 0.45 * 2.65 / e == pytest.approx(0.945, abs=0.002)


def test_compound_beam_bm():
    RA = (4 + 4 + 4 + 5) - (4 * 0.5 + 4 * 2 + 4 * 4 + 5 * 6) / 4
    assert RA == pytest.approx(3.0)
    xs = [i / 1000 for i in range(0, 2001)]
    M = [RA * x - 4 * min(x, 1) * (x - min(x, 1) / 2) for x in xs]
    assert max(M) == pytest.approx(1.125) and BY["PP1-compound-beam-bm"]["answer"] == 3


def test_portal_collapse_minimum():
    beam, sway, comb = 3.0, 2.0, 4 / 2.5
    assert min(beam, sway, comb) == pytest.approx(1.6) and BY["PP1-portal-plastic"]["answer"] == 1


def test_determinacy_counts():
    trusses = [(5, 3, 4), (9, 4, 6), (9, 3, 6)]
    assert [m + r - 2 * j for m, r, j in trusses] == [0, 1, 0]           # det, indet, det → (c)
    beams = [4 - 3, 7 - 3, 9 - 3 - 1, 4 - 3]
    assert beams == [1, 4, 5, 1]                                          # → (a)


def test_recollection_worked_numbers():
    # rigid bar on Al/steel posts
    kA, kS = 70000 * 1250 / 250 / 1e3, 210000 * 1250 / 249.9 / 1e3
    d = (500 + kS * 0.1) / (2 * kA + kS)
    assert 210000 * (d - 0.1) / 249.9 == pytest.approx(206, abs=1)
    # pretension elastic-shortening loss
    eps = 120e3 / (20000 * (40000 - 20) + 210000 * 20)
    assert 210000 * eps == pytest.approx(31.3, abs=0.1)


# ---- Part 2 key results
def test_vertical_curves():
    v = 70 / 3.6
    crest = v * 2.5 + v ** 2 / (2 * 9.81 * (0.30 - 0.03))
    sag = v * 2.5 + v ** 2 / (2 * 9.81 * (0.30 - 0.04))
    kr = BY["PP2-vertical-curves-pavement"]["key_results"]
    assert crest == pytest.approx(kr["SSD_crest_m"], abs=0.1)
    assert sag == pytest.approx(kr["SSD_sag_m"], abs=0.1)
    Lc = 5 * 120 ** 2 / (200 * (math.sqrt(1.05) + math.sqrt(0.15)) ** 2)
    Ls = 7 * 122.7 ** 2 / (120 + 3.5 * 122.7)
    assert Lc == pytest.approx(kr["L_crest_m"], abs=0.1) and Ls == pytest.approx(kr["L_sag_m"], abs=0.1)
    assert Lc / 2 + Ls / 2 > 150
    D1 = 2.3 / 0.45
    assert D1 == pytest.approx(kr["D1_in"], abs=0.01)
    assert (3.3 - 0.45 * D1) / (0.20 * 1.20) == pytest.approx(kr["D2_in"], abs=0.01)
    assert (4.3 - 3.3) / (0.12 * 1.10) == pytest.approx(kr["D3_in"], abs=0.01)


def test_sluice_jump():
    kr = BY["PP2-sluice-jump"]["key_results"]
    Q, y1, V1 = 4 * 2 * 0.5, 0.5, 4
    yc = c.critical_depth_trapezoid(Q, 2, 0)
    Fr = V1 / math.sqrt(9.81 * y1)
    y2 = y1 / 2 * (math.sqrt(1 + 8 * Fr ** 2) - 1)
    m = c.manning_trapezoid(2, 0, y2, 0.02, 1.0)            # V at S=1 → scale
    S0 = (Q / m["Q"]) ** 2
    vals = {"Q": Q, "E1": y1 + V1 ** 2 / 19.62, "yc": yc, "Ec": 1.5 * yc, "Fr1": Fr, "y2": y2, "S0": S0}
    for k, v in vals.items():
        assert v == pytest.approx(kr[k], rel=5e-3), k


def test_clarifier_activated_sludge():
    kr = BY["PP2-clarifier-as"]["key_results"]
    cl = c.clarifier(45000 * 0.55, 55, 2)
    Q, S = 520, (200 * 550 + 320 * 650) / 520
    V = Q * S / 1000 / 4
    X = Q * S / (V * 0.6)                                  # g/m3 = mg/L
    theta = V * X / ((Q - 95) * 20 + 95 * 10000)
    vals = {"A": cl["A"], "D": cl["D"], "depth": cl["depth"],
            "sludge_m3d": 0.75 * 45000 * 32 / 1000 / 0.015 / 1005, "V": V, "HRT_h": V / Q * 24,
            "MLVSS": X, "theta_c_d": theta}
    for k, v in vals.items():
        assert v == pytest.approx(kr[k], rel=5e-3), k


def test_bored_pile_alpha():
    kr = BY["PP2-bored-pile-clay"]["key_results"]
    per = math.pi * 0.8
    Qs = 0.5 * 30 * per * 5 + 0.5 * (40 + 3 * 7.5) * per * 15
    Qb = 9 * (40 + 3 * 15) * math.pi * 0.4 ** 2
    assert Qs == pytest.approx(kr["Qs_kN"], abs=0.5)
    assert Qb == pytest.approx(kr["Qb_kN"], abs=0.5)
    assert Qs + Qb == pytest.approx(kr["Qult_kN"], abs=0.5)


def test_greenshields_2019():
    g = c.greenshields(60, 120)
    kr = BY["PP2-19-greenshields-curve-pavement"]["key_results"]
    assert (g["q_max"], g["k_c"], g["v_c"]) == (kr["q_max"], kr["k_c"], kr["v_c"])


def test_unshift_garbled_font():
    shifted = "".join(chr(ord(ch) - 29) if ch not in "\n " else ch for ch in "Page 11\nFEE 2020 Q3. (a) 350 mm")
    shifted = shifted.replace(" ", "\x03")
    assert unshift_if_garbled(shifted) == "Page 11\nFEE 2020 Q3. (a) 350 mm"
    assert unshift_if_garbled("Normal text, no shift.") == "Normal text, no shift."
