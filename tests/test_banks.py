"""Question-bank integrity + every numeric answer recomputed in code."""
import json
import math
import re
from pathlib import Path

import pytest

from utils import calcs as c
from utils.syllabus import topic_map

DATA = Path(__file__).resolve().parents[1] / "data"
MCQ = json.loads((DATA / "mcq_bank.json").read_text(encoding="utf-8"))
P2 = json.loads((DATA / "part2_bank.json").read_text(encoding="utf-8"))


def num(s):
    return float(re.search(r"-?\d+(?:\.\d+)?", s.replace(",", "")).group())


def test_mcq_schema():
    ids = [q["id"] for q in MCQ]
    assert len(ids) == len(set(ids))
    for q in MCQ:
        assert len(q["options"]) == 4 and 0 <= q["answer"] < 4
        assert q["topic"] in topic_map() and q["topic"].startswith(q["code"])
        assert q["explain"].strip()
    per = {code: sum(q["code"] == code for q in MCQ) for code in ["CE101", "CE102", "CE103", "CE104", "CE105"]}
    assert all(n >= 3 for n in per.values()), per


def test_part2_schema():
    assert len(P2) >= 9
    slots = {"CE201": 2, "CE202": 2, "CE203": 2, "CE204": 1, "CE205": 1, "CE206": 1}
    for code, n in slots.items():
        assert sum(q["code"] == code for q in P2) >= n
    for q in P2:
        assert q["approach"] and q["prompt"]
        assert all(t in topic_map() for t in q["topics"])


# --- MCQ numeric answers: computed value must match the keyed option (and only it)
MCQ_CHECKS = {
    "M-CE101-001": lambda: 50e3 / (math.pi * 20 ** 2 / 4) * 2000 / 200e3,
    "M-CE102-001": lambda: 10 * 6 ** 2 / 8,
    "M-CE102-002": lambda: 20 * 3 + 4 * 3 ** 2 / 2,
    "M-CE102-003": lambda: 16 * 1.5e6 / (math.pi * 50 ** 3),
    "M-CE103-001": lambda: 12 * 5 ** 2 / 12,
    "M-CE103-002": lambda: (4 / 4) / (4 / 4 + 3 / 6),
    "M-CE103-003": lambda: 8 * 120 / 6,
    "M-CE103-004": lambda: c.euler_Ncr(210000, 25e6, 2 * 5000),
    "M-CE104-001": lambda: c.soil_phase(2.70, 0.65, 0.18)["gamma"],
    "M-CE104-002": lambda: c.effective_stress([(2, 18), (10, 20)], 6, 2)["sigma_v_eff"],
    "M-CE104-003": lambda: 0.197 * 3 ** 2 / 2,
    "M-CE105-001": lambda: 1000 * 9.81 * 1.5 * 6 / 1000,
    "M-CE105-002": lambda: 1000 * ((0.1 / (math.pi * 0.15 ** 2 / 4)) ** 2 - (0.1 / (math.pi * 0.3 ** 2 / 4)) ** 2) / 2 / 1000,
    "M-CE105-003": lambda: 0.02 * 25 ** 2.5,
    # ---- from lecture notes
    "M-CE101-007": lambda: (150 - (-50)) / 2,
    "M-CE101-008": lambda: 0.18 + 1.20 / 6 + (0.10 + 0.05 + 0.02) / 5 + (0.15 + 0.10) / 15,
    "M-CE101-009": lambda: math.sqrt(4 * (4.62 / (0.00785 * 1.20)) / math.pi),
    "M-CE101-011": lambda: 160 / (450 + 3 * 35),
    "M-CE101-012": lambda: (1 - 0.02 - 350 / 3150 - 175 / 1000 - 750 / 2600) * 2650,
    "M-CE101-013": lambda: 15 / math.sqrt(9),
    "M-CE101-014": lambda: 12000 * 300 / (100 * 100 ** 2),
    "M-CE102-005": lambda: math.hypot(20 + 30 * math.cos(math.radians(60)) + 25 * math.cos(math.radians(150)),
                                      30 * math.sin(math.radians(60)) + 25 * math.sin(math.radians(150))),
    "M-CE102-006": lambda: math.sqrt(sum(x * x for x in _cross((4, 1, 0), (2, -3, 6)))),
    "M-CE102-007": lambda: 400 * (1 / 300) / (1 / 300 + 1 / 500),
    "M-CE102-008": lambda: 10e6 * 50 / (math.pi * (100 ** 4 - 60 ** 4) / 32),
    "M-CE102-009": lambda: math.degrees(1e6 * 2000 / (80000 * math.pi * 50 ** 4 / 32)),
    "M-CE102-010": lambda: 1.5 * 60000 / (100 * 300),
    "M-CE102-011": lambda: 40 * 6 ** 2 / (16 * 20000),
    "M-CE103-006": lambda: (0.8 * 50 * 4 + (-0.6) * (-30) * 3) / 200000 * 1000,
    "M-CE103-007": lambda: 1.25 * 12e-6 * 30 * 5000,
    "M-CE103-008": lambda: 5 * 0.5 * 10 * (4 * 6 / 10),
    "M-CE103-009": lambda: 3 * 12 * 8 / 8,
    "M-CE103-010": lambda: 2 * 40000 / 5 * (2 * 0.002),
    "M-CE103-011": lambda: 50 * math.cos(math.radians(30)) ** 2,
    "M-CE102-012": lambda: 10000 / (math.pi * 16 ** 2 / 4),
    "M-CE102-013": lambda: 50000 / (2 * math.pi * 300 / 60),
    "M-CE102-014": lambda: 200 / 10 * 100,
    "M-CE102-015": lambda: 10 * 4 ** 4 / (8 * 20000) * 1000,
    "M-CE105-004": lambda: (13.6 - 1) * 9810 * 0.2 / 1000,
    "M-CE105-005": lambda: 2.5 + (2 * 3 ** 3 / 12) / (2.5 * 6),
    "M-CE105-006": lambda: 9.81 * math.pi * 2 ** 2 / 4 * 3,
    "M-CE105-007": lambda: 650 / 1025 * 0.5,
    "M-CE105-008": lambda: 0.75 + 6 ** 2 / (12 * 1.5) - 2.0,
    "M-CE105-009": lambda: math.degrees(math.atan(2 / 9.81)),
    "M-CE105-010": lambda: 10 ** 2 * 0.3 ** 2 / (2 * 9.81),
    "M-CE105-011": lambda: math.sqrt(2) * 1000 * 0.2 * (0.2 / (math.pi * 0.3 ** 2 / 4)),
}


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


@pytest.mark.parametrize("qid", sorted(MCQ_CHECKS))
def test_mcq_numeric(qid):
    q = next(x for x in MCQ if x["id"] == qid)
    v = MCQ_CHECKS[qid]()
    vals = [num(o) for o in q["options"]]
    best = min(range(4), key=lambda i: abs(vals[i] - v) / max(abs(v), 1e-9))
    assert best == q["answer"], f"{qid}: computed {v:.4g}, keyed {q['options'][q['answer']]}"
    assert abs(vals[best] - v) / abs(v) < 0.01, f"{qid}: computed {v:.4g} vs option {vals[best]}"


def test_mcq_text_answers_from_notes():
    by = {q["id"]: q for q in MCQ}
    assert 0.001 * (1 - 2 * 0.3) == pytest.approx(4e-4) and by["M-CE101-006"]["answer"] == 1   # volume increases
    assert 0.25 + 0.658 * 0.60 == pytest.approx(0.645, abs=1e-3) and by["M-CE101-015"]["answer"] == 1
    assert 4 * 3 + 4 == 5 * 3 + 1 and by["M-CE103-005"]["answer"] == 0                        # 3m+r = 3j+c
    assert by["M-CE101-010"]["answer"] == 2                                                    # w/c ≈ 0.38
    assert 1 / math.sqrt(4) == 0.5 and by["M-CE101-005"]["options"][by["M-CE101-005"]["answer"]] == "one half"


def test_every_new_mcq_cites_a_lecture_page():
    ol = json.loads((DATA / "lecture_outlines.json").read_text(encoding="utf-8"))
    cited = [q for q in MCQ if q.get("source")]
    assert len(cited) >= 37
    for q in cited:
        doc, page = q["source"]["doc"], q["source"]["page"]
        assert doc in ol, q["id"]
        assert 1 <= page <= ol[doc]["page_count"], q["id"]


def test_part1_subjects_have_ten_plus_where_notes_exist():
    for code in ("CE101", "CE102", "CE103", "CE105"):
        assert sum(q["code"] == code for q in MCQ) >= 10, code


def test_mcq_determinacy():
    q = next(x for x in MCQ if x["id"] == "M-CE102-004")
    assert 11 + 3 == 2 * 7 and q["answer"] == 1


# --- Part 2 key results recomputed
def p2_values():
    v = {}
    w = 1.35 * 18 + 1.5 * 12
    M = w * 7.5 ** 2 / 8
    b = c.ec2_rect_beam(M, 300, 540, 30)
    wc = 1.35 * (0.3 * 0.6 * 25 + 2.5 * 0.1 * 25) + 1.5 * 0.75 * 2.5
    v["P2-CE201-001"] = {"w_Ed": w, "M_Ed": M, "K": b["K"], "z": b["z"], "As": b["As"], "As_min": b["As_min"],
                         "M_Ed_construction": wc * 7.5 ** 2 / 8}
    col = c.ec2_short_column_axial(3800, 400, 400, 35)
    v["P2-CE201-002"] = {"N_conc": col["N_conc_kN"], "As_axial": col["As"], "M_min": 3800 * c.ec2_min_eccentricity(400) / 1000,
                         "n_ratio": 3.8e6 / (400 * 400 * 35), "m_ratio": 120e6 / (400 * 400 ** 2 * 35)}
    w = 1.35 * 12 + 1.5 * 10
    Mcr = c.ec3_Mcr(8000, 1452e4, 37.1e4, 0.705e12, C1=1.127)
    lt = c.ec3_ltb_rolled(1471e3, 355, Mcr, 453.4 / 189.9)
    lt2 = c.ec3_ltb_rolled(1471e3, 355, c.ec3_Mcr(4000, 1452e4, 37.1e4, 0.705e12, C1=1.0), 453.4 / 189.9)
    Av = c.ec3_Av_rolled_I(8550, 189.9, 12.7, 8.5, 10.2, 453.4 - 2 * 12.7)
    v["P2-CE202-001"] = {"w_Ed": w, "M_Ed": w * 64 / 8, "V_Ed": w * 4, "Mc_Rd": c.ec3_Mc_Rd(1471e3, 355),
                         "Vpl_Rd": c.ec3_Vpl_Rd(Av, 355), "Mcr": Mcr, "lambda_LT": lt["lambda_LT"],
                         "chi_LT": lt["chi_LT"], "Mb_Rd": lt["Mb_Rd"], "Mb_Rd_restrained": lt2["Mb_Rd"]}
    fy = c.ec3_flexural_buckling(9310, 355, 5000, 110, 0.34)
    fz = c.ec3_flexural_buckling(9310, 355, 5000, 64.6, 0.49)
    v["P2-CE202-002"] = {"lambda1": fy["lambda1"], "lambda_y": fy["lambda_bar"], "chi_y": fy["chi"], "Nb_y_Rd": fy["Nb_Rd"],
                         "lambda_z": fz["lambda_bar"], "chi_z": fz["chi"], "Nb_z_Rd": fz["Nb_Rd"],
                         "Fv_Rd": c.ec3_bolt_shear(800, 245)}
    pd2 = c.phi_design(32, 1.25)
    sch = c.schmertmann_strip(156, 19, 57, 2, [(0, 2, 21000), (2, 4, 28000), (4, 6, 35000), (6, 8, 42000)])
    v["P2-CE203-001"] = {"Vd_C1": 1.35 * 250 + 1.5 * 100, "Rd_C1": c.strip_bearing_drained(2, 1, 19, 32) * 2,
                         "phi_d_C2": pd2, "Vd_C2": 250 + 1.3 * 100, "Rd_C2": c.strip_bearing_drained(2, 1, 19, pd2) * 2,
                         "dp": 350 / 2 - 19, "Iz_p": sch["Iz_p"], "C1": sch["C1"], "s_mm": sch["s_mm"]}
    pd3 = c.phi_design(30, 1.25)
    Ka1, Ka2 = c.rankine_Ka(30), c.rankine_Ka(pd3)
    v["P2-CE203-002"] = {"Ka_C1": Ka1, "Hd_C1": 1.35 * 0.5 * Ka1 * 18 * 25 + 1.5 * Ka1 * 10 * 5,
                         "Rd_C1": 220 * math.tan(math.radians(30)), "phi_d_C2": pd3, "Ka_C2": Ka2,
                         "Hd_C2": 0.5 * Ka2 * 18 * 25 + 1.3 * Ka2 * 10 * 5, "Rd_C2": 220 * math.tan(math.radians(pd3))}
    g = c.greenshields(100, 120)
    kA = c.greenshields_density(1800, 100, 120)
    kB = c.greenshields_density(1200, 100, 120, True)
    v["P2-CE204-001"] = {"q_max": g["q_max"], "k_c": g["k_c"], "v_c": g["v_c"], "k_A": kA, "k_B": kB,
                         "u_w": c.shockwave_speed(1800, kA, 1200, kB), "SSD_level": c.aashto_ssd(100)["SSD"],
                         "SSD_down3": c.aashto_ssd(100, grade=-0.03)["SSD"]}
    yn = c.normal_depth_trapezoid(12, 3, 2, 0.015, 0.0008)
    m = c.manning_trapezoid(3, 2, yn, 0.015, 0.0008)
    v["P2-CE205-001"] = {"y_n": yn, "V": m["V"], "y_c": c.critical_depth_trapezoid(12, 3, 2), "Fr": m["Fr"]}
    # ---- CE205 from lecture notes
    g = 9.81
    A1, A2 = math.pi * 0.4 ** 2 / 4, math.pi * 0.3 ** 2 / 4

    def solve(n_parallel):
        def head(Q):
            v1, v2 = Q / A1, Q / n_parallel / A2
            return v1 ** 2 / (2 * g) * (0.5 + 0.02 * 800 / 0.4) + v2 ** 2 / (2 * g) * (0.3 + 0.02 * 600 / 0.3 + 1.0) - 30
        return c._bisect(head, 1e-6, 5.0)
    Q = solve(1)
    v1, v2 = Q / A1, Q / A2
    egl = 100 - v1 ** 2 / (2 * g) * (0.5 + 40)
    v["P2-CE205-002"] = {"Q": Q, "v1": v1, "v2": v2, "EGL_junction": egl, "HGL_junction": egl - v1 ** 2 / (2 * g),
                         "Q_parallel": solve(2)}
    Qw = 0.88 * (2 / 3) ** 1.5 * math.sqrt(g) * 4 * 0.8 ** 1.5
    q = Qw / 4
    Fr = q / 0.25 / math.sqrt(g * 0.25)
    y2 = 0.25 / 2 * (math.sqrt(1 + 8 * Fr ** 2) - 1)
    v["P2-CE205-003"] = {"Q": Qw, "yc": (q * q / g) ** (1 / 3), "Fr1": Fr, "y2": y2,
                         "dE": (y2 - 0.25) ** 3 / (4 * 0.25 * y2),
                         "Q_vnotch": 0.59 * 8 / 15 * math.sqrt(2 * g) * math.tan(math.radians(45)) * 0.3 ** 2.5}
    UH, P = [0, 25, 60, 45, 30, 15, 5, 0], [2, 3]
    drh = [sum(P[m] * UH[n - m] for m in range(2) if 0 <= n - m < len(UH)) for n in range(len(UH) + 1)]
    KT = -math.sqrt(6) / math.pi * (0.5772 + math.log(math.log(50 / 49)))
    K, X, dt = 12, 0.2, 6
    Dm = K - K * X + 0.5 * dt
    v["P2-CE205-004"] = {"area_km2": sum(UH) * 3 * 3600 / 0.01 / 1e6, "DRH_peak": max(drh), "KT": KT,
                         "Q50": 420 + KT * 130, "risk25": 1 - (1 - 1 / 50) ** 25,
                         "C0": (-K * X + 0.5 * dt) / Dm, "C1": (K * X + 0.5 * dt) / Dm, "C2": (K - K * X - 0.5 * dt) / Dm}
    cl = c.clarifier(20000, 40, 2)
    a = c.activated_sludge(20000, 180, 0.3, 2500, 150, 8000)
    v["P2-CE206-001"] = {"A": cl["A"], "D": cl["D"], "depth": cl["depth"], "V_aer": a["V"], "HRT_h": a["HRT_h"],
                         "SRT_d": a["SRT_d"]}
    return v


@pytest.mark.parametrize("q", P2, ids=[q["id"] for q in P2])
def test_part2_key_results(q):
    computed = p2_values()[q["id"]]
    assert set(q["key_results"]) == set(computed), "every stated key result must be recomputed"
    for k, stated in q["key_results"].items():
        assert computed[k] == pytest.approx(stated, rel=6e-3, abs=6e-3), f"{q['id']} {k}: {computed[k]:.4g} vs {stated}"
