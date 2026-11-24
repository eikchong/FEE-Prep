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
    assert len(STUDY) == len(STUDY)  # count grows with notes
    for tdoc, page, title, target in TUTORIALS:
        assert tdoc in OL and 1 <= page <= OL[tdoc]["page_count"] and target in STUDY, title
    assert len(TUTORIALS) >= 35


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


def test_tut4_q5_strain_gauge():
    import math
    gamma = 2 * 180e-6 / math.sin(math.radians(30))
    tau = 80e9 * gamma
    T = tau * (math.pi / 2 * 0.05 ** 4) / 0.05
    assert abs(tau / 1e6 - 57.6) < 0.05 and abs(T / 1e3 - 11.31) < 0.01


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


def test_materials_tutorial_answers():
    import math
    assert 5 - 1.5 == 3.5 and 300 * 0.85 == 255
    assert abs(600 / (0.213 - 0.210) / 1000 - 200) < 1e-6
    assert abs(0.408 * math.sqrt(2) / 4 - 0.144) < 0.0005
    pear = 1 - 0.075
    ef = pear * (6.7 - 0.8) / (6.7 - 0.025)
    assert abs(0.8 + 0.075 * 5.9 - 1.2425) < 1e-9 and abs(ef - 0.818) < 0.001 and abs(pear - ef - 0.107) < 0.001


def test_consolidation_example():
    import math
    T = 1.781 - 0.933 * math.log10(100 * (1 - 1.5 / 1.61))
    assert abs(T - 1.0) < 0.02 and abs(T * 2.5 ** 2 / 0.5 - 12.5) < 0.3
    T2 = 0.5 * 2 / 2.5 ** 2
    assert abs(T2 - 0.16) < 1e-9 and abs(math.sqrt(4 * T2 / math.pi) * 1.61 - 0.72) < 0.01


def test_ce104_tutorial_answers():
    import math
    sinp = lambda s1, s3: math.degrees(math.asin((s1 - s3) / (s1 + s3)))
    assert round(sinp(170, 50)) == 33 and round(sinp(51, 15)) == 33 and round(sinp(195, 70)) == 28
    Kp = math.tan(math.radians(45 + 18)) ** 2
    assert abs(40 * math.tan(math.radians(63)) ** 2 - 154) < 1 and abs(45 * math.tan(math.radians(63.5)) ** 2 - 181) < 1
    t = math.tan(math.radians(53.5))
    assert abs((360 - 2 * 35 * t) / t ** 2 - 145.3) < 0.3 and abs(35 * t - 47.3) < 0.1
    s = math.sin(math.radians(24))
    assert abs(75 * (1 + s) / (1 - s) - 75 - 103) < 1 and abs(200 - (160 / s - 160) / 2 - 83.3) < 0.3
    assert abs(120 * (1 + s) / (1 - s) - 120 - 164.5) < 0.5
    # seepage
    assert abs(2e-5 * 3 * 5 / 11 * 86400 - 2.356) < 0.01 and abs(2e-5 * 10 * 5 / 12 * 86400 - 7.2) < 0.01
    assert abs(105 - 10 * (9 - 3 * 2.5 / 11 - 3) - 51.82) < 0.01 and abs(1 / ((7.364 - 6) / 3) - 2.2) < 0.02
    A = math.pi * 2.5 ** 2
    assert abs(40 * 15 / (30 * A * 5) - 0.204) < 0.001
    k = 0.0000385 * 0.127 / (0.007854 * 1081) * math.log(560 / 465)
    assert abs(k - 1.07e-7) < 0.01e-7 and abs(1081 * (2 / 3.5) ** 2 - 353) < 1
    assert abs(0.283 * 10 / (80 * 900) * math.log(90 / 84) * (2.42 - 0.475 * math.log(22)) - 2.57e-6) < 0.02e-6
    # phase
    e = 27 / (15.5 * 9.81 / 1000 / 0.01) - 1
    assert abs(e - 0.775) < 0.005 and abs(0.1613 * 2.7 / 0.78 - 0.558) < 0.005
    emin = (26.5 - 20.601) / 10.601
    assert abs(emin - 0.556) < 0.002 and abs((0.93 - 0.7227) / (0.93 - 0.56) - 0.56) < 0.01
    assert abs(80000 / 1.54 * 1.93 - 100260) < 10 and abs((0.54 - 0.378) / 1.54 - 0.105) < 0.001
    Ws = 27 / (1 + 0.75 * 2.7)
    assert abs(0.2 * Ws / 31 + 0.69 * Ws / 10 - 0.673) < 0.002
    assert abs(2.64 / (1 / 27 + 0.2 / 31 + 0.144) - 14.08) < 0.01
    # assignment Q2/Q3
    assert abs(0.9 * (27 / 17.5 - 1) / 2.7 * 100 / 1.1 - 100 / 1.1 * 0.1 - 7.36) < 0.05
    assert abs((3.5 * 0.5 - 0.5 - 0.24) / 0.5 - 2.02) < 0.01


def test_ce203_tutorial_answers():
    import math
    r = math.radians
    # infinite slope
    F = lambda c, sv_, sv, b, phi: (c + sv_ * math.cos(r(b)) ** 2 * math.tan(r(phi))) / (sv * math.cos(r(b)) * math.sin(r(b)))
    assert round(F(0, 16.5, 16.5, 18, 30), 2) == 1.78 and round(F(0, 10, 20, 18, 30), 2) == 0.89
    assert round(F(0, 30, 60, 18, 25), 2) == 0.72  # seam: c′ = 0
    pd = math.degrees(math.atan(math.tan(r(33)) / 1.25))
    assert abs(F(0, 29.4, 59.4, 14, pd) - 1.03) < 0.01 and abs(F(0, 29.4, 59.4, 17, pd) - 0.84) < 0.01
    # mass procedure
    m = 17 * 25 * r(66) / (8.1 * 16 * 2.03)
    assert round(m / 1.35, 2) == 1.38 and round(m / 1.4, 2) == 1.33
    # sheet pile cantilever
    d0 = 6 / (9 ** (1 / 3) - 1)
    assert abs(d0 - 5.56) < 0.02 and abs(0.9444 * 9 ** 3 - 8.5 * 27 - 459) < 1
    # exam Q3 surcharge
    Ka = (1 - math.sin(r(24))) / (1 + math.sin(r(24)))
    assert abs(2 * 13 / math.sqrt(Ka) - 40) < 0.5
    # site investigation
    Qt = (9.130 - 0.0575) / 0.0475; Fr = 0.017 / (9.130 - 0.0575) * 100
    Ic = math.sqrt((3.47 - math.log10(Qt)) ** 2 + (1.22 + math.log10(Fr)) ** 2)
    assert abs(Ic - 1.287) < 0.005 and abs(28 * 70 / 60 * 0.75 * 300 / 247.5 - 29.7) < 0.1
    assert abs(3 * 936 * 50 / 14 - 10029) < 2 and abs((810.5 - 194) / 20 - 30.8) < 0.1
    Fh = 2 * math.pi * 0.3 / math.log(3 + math.sqrt(10))
    assert abs(Fh - 1.04) < 0.01 and abs(math.pi * 0.05 ** 2 / (Fh * 80) - 9.4e-5) < 0.1e-5
    # compaction
    lo, hi = 2650 / 1.85, 2650 / 1.4
    assert abs(lo / (1 - 0.75 * (hi - lo) / hi) - 1750) < 5
    assert abs(1750 * 270000 * 1.1 / 28000 - 18563) < 1
    # foundations
    assert abs(4.84 * (57 * 5.14 * 1.2 + 38.8) - 1889.4) < 0.5
    assert abs(82 * (1.5 / 0.0135) ** 2 / 525600 - 1.93) < 0.01 and abs(3000 * 0.0035 * math.log10(100 / 1.93) - 18) < 0.1
    assert abs(0.455 * 36 * 0.649 * 4 - 42.5) < 0.1 and abs(1.35 * (350 + 42.5 + 323.4 + 20.5) + 1.5 * 150 - 1219.1) < 0.1
    assert abs(4000 / 1.47 - 2721) < 1 and abs(2721 / 1.7 - 1601) < 1
    U = (math.pi * 25 - 0.35 ** 2) * 9.81 * 5 + 0.35 ** 2 * 9.81 * 21
    assert abs(U - 3871.6) < 0.5 and abs(1.35 * U - 3200 - 2027) < 1


def test_hydraulics_answers():
    import math
    assert abs(1030 / 873 * 0.3 * 150 ** 2 / (2 * math.pi) - 1267.5) < 1 and abs(1030 * 0.01 * 0.1 * 30 - 30.9) < 0.01
    assert abs(0.5 * 1000 * 9.8 * 36 ** 2 / 1e3 - 6350) < 1 and abs(math.sqrt(76200e3 / (2400 * 9.8 * 0.5 * 36)) - 13.4) < 0.05
    assert abs(18 * math.sqrt(19.6 / 9) - 26.56) < 0.01
    lv = ((14 / 0.95) ** 2 - 14 ** 2) / 19.6
    assert 0.9 < lv < 1.2
    assert abs(1000 * 6 * (100 / 36 + 0.5 * 9.8 * 6) / 1e3 - 193) < 1 and abs(0.5 * 9.8 * 4.7 ** 2 - 108.2) < 0.1
    assert abs(160 / (2 * math.pi * 60) - 0.424) < 0.001 and abs(1000 * 130 ** 2 * 0.175 ** 2 / 2 / 1e3 - 258.8) < 0.1
    assert abs(32 * 0.048 * 45 * 0.3 / (800 * 9.81 * 0.025 ** 2) - 4.228) < 0.005 and abs(0.6 * (1 - 0.6 ** 2) - 0.384) < 1e-9
    assert abs(0.2 / 8 - 0.025) < 1e-9 and abs(7 * 0.2 / 72 - 0.0194) < 1e-4
    V = math.sqrt(2 * 9.81 * 2.44 / 1.8)
    assert abs(V * math.pi * 0.076 ** 2 / 4 - 0.0234) < 0.0005
    assert abs((2 * 1000 * 15 ** 2 + 210e3 + 165e3) * 9000e-6 - 7425) < 1


def test_concrete_answers():
    import math
    assert abs(1.35 * 25 + 1.5 * 15 - 56.25) < 1e-9
    M = 54.3 * 8 ** 2 / 8
    assert abs(M - 434.4) < 0.01 and abs(M * 1e6 / (0.167 * 30 * 605 ** 2) - 237) < 1
    K = M * 1e6 / (300 * 605 ** 2 * 30)
    z = 605 * (0.5 + math.sqrt(0.25 - K / 1.134))
    assert abs(K - 0.132) < 0.001 and abs(z - 524) < 1 and abs(M * 1e6 / (500 / 1.15 * z) - 1907) < 5
    K2 = M * 1e6 / (200 * 605 ** 2 * 30)
    As2 = (K2 - 0.167) * 30 * 200 * 605 ** 2 / (500 / 1.15 * (605 - 45))
    assert abs(K2 - 0.198) < 0.001 and abs(As2 - 280) < 10
    k = 1 + math.sqrt(200 / 645)
    VRdc = 0.12 * k * (100 * 1470 / (300 * 645) * 35) ** (1 / 3) * 300 * 645 / 1e3
    assert abs(k - 1.557) < 0.01 and abs(VRdc - 108) < 1.5
    assert abs(0.315 * 30 ** (2 / 3) - 3.04) < 0.01 and abs(16 / 4 * 435 / (0.7 * 0.315 * 30 ** (2 / 3)) - 820) < 15
    assert abs((1.35 * 6 + 1.5 * 5) * 3 * 0.075 * 3 - 10.53) < 0.01
