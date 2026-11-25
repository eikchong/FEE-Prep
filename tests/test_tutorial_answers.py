"""Tutorial answers: every question has an answer (or is marked "not provided yet"), and the numbers in the
answers are recomputed here. Mismatches with the official sheets are listed in reports/answer_check.md."""
import math

import numpy as np

from utils.qblock import all_questions
from utils.study_notes import STUDY

r = math.radians
close = lambda a, b, tol: abs(a - b) <= tol


def test_every_question_has_an_answer_or_is_marked_not_provided():
    qs = list(all_questions(STUDY))
    assert len(qs) > 250
    for doc, _, qd in qs:
        assert qd["question"].strip(), (doc, qd["set"])
        if qd["answer_source"] == "none":
            assert not qd["answer"]
        else:
            assert qd["answer"].strip().startswith("**"), (doc, qd["set"])   # final answer first, in bold
        assert qd["source"]["doc"] == doc and qd["source"]["page"] >= 1


def test_question_ids_unique():
    ids = [qd["id"] for _, _, qd in all_questions(STUDY)]
    assert len(ids) == len(set(ids))


# ------------------------------------------------------------------ CE201 concrete
def test_ce201_numbers():
    assert close(2.9 * 6.52e9 / (600 - 305) / 1e6, 64.1, 0.05)                       # Tut 1 Mcr
    assert close(0.15 * 1.5 * 25 + 1.5 * 1.5 + 0.01 * 21 * 1.5, 8.19, 0.005)          # Tut 6 slab strip
    assert close(1.35 * (8.19 + 16.8975), 33.87, 0.01)                              # (slide prints 29.42)
    assert close(1.35 * ((16.38 + 4.5) * 2 + 10.986 * 6), 145.36, 0.01)
    MB = -0.25 * 48.75 * (6 ** 3 + 7 ** 3) / (2 * 13)                                  # Tut 7 three-moment
    assert close(MB, -262.0, 0.1)
    n = 1.35 * 4.0 + 1.5 * 3.75
    assert close(n, 11.025, 1e-9) and close(0.0462 * n * 7.3 ** 2, 27.14, 0.01) and close(0.0349 * n * 7.3 ** 2, 20.50, 0.01)
    rho0, rho = math.sqrt(30) / 1000, 393 / 125000
    ld = 11 + 1.5 * math.sqrt(30) * rho0 / rho + 3.2 * math.sqrt(30) * (rho0 / rho - 1) ** 1.5
    assert close(1.5 * ld, 54.9, 0.2) and close(1.5 * ld * 7 / 7.3, 52.7, 0.2)
    assert close(3.46 * 3105 / 500, 21.5, 0.05) and close(26.2 / math.sqrt(183e3 / (300 * 500 * 0.567 * 40)), 113, 1)
    assert close(216 * 3 * 1.3 ** 2 / 2 + (320 - 216) * 3 * 1.3 / 2 * 2 / 3 * 1.3, 723.3, 0.3)   # Tut 8 pad base
    kb = 38.1e9 / (445 * 324400)
    assert close(kb, 263.9, 0.1) and close(1130.5e6 / (0.8 * (325 + kb)) / 1e3, 2400, 1)          # Tut 9 (a)
    assert close(1380.5e6 / (0.8 * (325 + kb)) / 1e3, 2930, 2)                                   # (b)
    E7, E28 = 22 * (33 / 10) ** 0.3, 22 * (48 / 10) ** 0.3
    cam = 2610e3 * 791 * 28000 ** 2 / (8 * E7 * 1e3 * 134e9)
    sw = 5 * 12.7 * 28000 ** 4 / (384 * E7 * 1e3 * 134e9)
    qp = 5 * 19.7 * 28000 ** 4 / (384 * E28 * 1e3 * 134e9) * 2.6
    assert close(cam, 47.9, 0.1) and close(sw, 24.1, 0.1) and close(-cam * 0.8 * 3 + qp, -28, 0.6)


# ------------------------------------------------------------------ CE202 steel
def chi(lam, a):
    ph = 0.5 * (1 + a * (lam - 0.2) + lam ** 2)
    return 1 / (ph + math.sqrt(ph ** 2 - lam ** 2))


def test_ce202_numbers():
    w = 1.35 * 4.0 + 1.5 * 4.5
    assert close(w, 12.15, 1e-9) and close(w * 6 * (3 * 8 ** 2 - 4 * 3 ** 2) / 24, 473.85, 0.01)
    P = w * 3 * (4 + 3)
    assert close(P * 6 / 4, 382.7, 0.1) and close(3 * 42 * w, 1530.9, 0.1)
    assert close(1.35 * (288 + 42 + 444) + 1.5 * (324 + 16.8), 1556.1, 0.1)
    RA = (1.35 * 150 * 3 + 1.5 * 240 * 3 + 1.35 * 100 * 3 - 1.35 * 75 * 1.5) / 6
    RAu = (150 * 3 + 100 * 3 - 75 * 1.5 - 1.5 * 120 * 1.5 - 1.5 * 300 * 3) / 6
    RB = (1.35 * 225 * 4.5 + 1.5 * 360 * 4.5 + 1.35 * 100 * 3 + 1.5 * 300 * 9) / 6
    assert close(RA, 323.4, 0.1) and close(RAu, -163.75, 0.01) and close(RB, 1375.3, 0.1)
    assert close(1.35 * 75 * 1.5 + 1.5 * 120 * 1.5 + 1.5 * 300 * 3, 1771.9, 0.1)
    Fd = 10.89 * 3.5 / math.cos(r(15))
    FAB = (2 * Fd - Fd / 2) / math.sin(r(15))
    assert close(FAB, 228.7, 0.2) and close(FAB * math.cos(r(15)), 220.9, 0.2)
    lam = 3500 / math.cos(r(15)) / (38.5 * 93.9 * math.sqrt(235 / 355))
    assert close(chi(lam, 0.21) * 1520 * 355 / 1e3, 275, 2)
    l1 = 93.9 * math.sqrt(235 / 265)
    assert close(chi(6000 / (77.7 * l1), 0.49) * 15000 * 265 / 1e3, 2450, 10)
    assert close(chi(6000 / (65.9 * l1), 0.49) * 13600 * 265 / 1e3, 1884, 10)
    An = 7200 - 5 * 440 + 2 * 20 * 45 ** 2 / 240 + 2 * 20 * 40 ** 2 / 240
    assert close(An, 5604, 1) and close(0.9 * An * 410 / 1.1 / 1e3, 1880, 1)
    b3 = 0.5 + 0.2 * (90 - 55) / 55
    assert close(b3, 0.627, 0.001) and close(420e3 * 1.1 / (b3 * 410), 1797, 2) and close(b3 * 2006 * 410 / 1.1 / 1e3, 469, 1)
    assert close(0.9 * (2400 - 330) * 410 / 1.1 / 1e3, 694, 1)
    EI = 210e6 * 75800e-8
    d = (70 * 2.5 * (300 - 25) + 70 * 4.5 * (300 - 81)) / 48 / EI
    assert close(d * 1000, 15.3, 0.1)
    G, E = 81000, 210000
    Iz, It, Iw, L = 3434e4, 111e4, 3.18e12, 4500
    a = math.pi ** 2 * E * Iz / L ** 2
    Mcr = 1.77 * a * math.sqrt(Iw / Iz + L ** 2 * G * It / (math.pi ** 2 * E * Iz)) / 1e6
    lt = math.sqrt(869 / Mcr)
    ph = 0.5 * (1 + 0.49 * (lt - 0.4) + 0.75 * lt ** 2)
    x = 1 / (ph + math.sqrt(ph ** 2 - 0.75 * lt ** 2))
    assert close(Mcr, 2139, 10) and close(x * 869, 751, 3)
    assert close((2 * 450 * 30 + 1740 * 10) * 1e-6 * 78.5, 3.49, 0.01)


# ------------------------------------------------------------------ CE103 analysis
def test_ce103_numbers():
    il = lambda x: 6 * (15 - x) / 15 if x >= 6 else 9 * x / 15
    loads = lambda x0: [(9, x0 - 0.9), (18, x0), (27, x0 + 1.2), (9, x0 + 2.1)]
    best = max(sum(p * il(x) for p, x in loads(x0) if 0 <= x <= 15) for x0 in np.arange(0, 15, 0.01))
    assert close(best, 201.4, 0.1)
    assert close(-2 - 1 + 1 + 5 * 1 + 2 * 2, 7, 1e-9)
    assert close((4 ** 3 / 3 - 4 ** 2) - (2 ** 3 / 3 - 2 ** 2) + 4, 10.667, 0.001)
    assert close(0.8 * 12 + 4 * 12 + 20 * 1.5, 87.6, 1e-9) and close(4 * 8 + 20 * 2, 72, 1e-9)
    assert close(0.8 * -2 + 4 * -3 + 20 * -0.5, -23.6, 1e-9)


# ------------------------------------------------------------------ CE102 statics & mechanics
def test_ce102_numbers():
    th = math.asin(4.5 / 20)
    assert close(1.5 * math.tan(th), 0.346, 0.001) and close(1 + 2 * math.sqrt(1 + 0.231 ** 2), 3.053, 0.01)
    d = math.sqrt((3.08 - 1) ** 2 / 4 - 1)
    assert close(d, 0.29, 0.01) and close(4.5 / math.sin(math.atan(d)), 16.4, 0.2)
    T = (6 * 5.2 + 0.15 * 5.5 ** 2) * math.sqrt(16 + 5.5 ** 2) / (4 * 5.5)
    assert close(T, 11.05, 0.02) and close((2.5 * 6 * 5.2 + 0.15 * 5.5 ** 2) * math.sqrt(46.25) / 22, 25.5, 0.05)
    assert close(40 / math.cos(r(30)), 46.19, 0.01) and close(40 * math.sqrt(36 + 2.25) / 6, 41.2, 0.05)
    H = math.sqrt(1000 ** 2 - 300 ** 2)
    y1 = 450 / H
    assert close(y1, 0.472, 0.001) and close(2 * (math.hypot(1.5, y1) + math.hypot(3, y1)), 9.22, 0.005)
    assert close(1 / 2 + 1 / 3 + 1 / 8, 23 / 24, 1e-12)
    assert close(150 * 63.62 * math.sqrt(1 - 0.28 ** 2), 9161, 2)
    ex, ez = (120 - 0.34 * 160) / 87000, (160 - 0.34 * 120) / 87000
    assert close(100 * ex, 0.0754, 1e-4) and close(75 * ez, 0.1028, 1e-4) and close((100 * 100 * ex + 75 * 75 * ez) / 125, 0.122, 1e-3)
    assert close(50e3 * 5000 * math.log(2) / (80e3 * 10 * 25), 8.66, 0.01)
    assert close(0.00223 * (22000 + 6.1 * 450) / (22000 + 6.1 * 225), 0.00236, 1e-5) and close(0.00223 * 450, 1.0, 0.01)
    assert close(math.degrees(math.acos(1 / math.sqrt(3))), 54.7, 0.05)
    th = 16000 / (350e6 * 0.04 + 233.33e6 * 0.0225)
    assert close(0.4 * th * 1000, 0.333, 0.001)
    J1, J2 = math.pi * 0.04 ** 4 / 32, math.pi * 0.03 ** 4 / 32
    phiD = 1.5 * 600 / (80e9 * J1) + 400 * 1.5 / (80e9 * J2)
    assert close(math.degrees(phiD), 7.97, 0.01) and close(16 * 600 / (math.pi * 0.04 ** 3) / 1e6, 47.7, 0.1)
    assert close(16 * 400 / (math.pi * 0.03 ** 3) / 1e6, 75.5, 0.1)
    assert close(7.3125 * 1.3 + 15 * 1.5 - 75 * 0.9, -35.49, 0.01) and close(-7.3125 - 15 + 75, 52.69, 0.01)
    Ty = 45 * 1.35 / 1.8
    Tx = Ty * 1.8 / 1.17
    assert close(Tx / 1.8 + (Ty * 0.9 - 45 * 0.45) * 0.11 / 70e-6 / 1e3, 44.8, 0.1)
    x = 55 / 36
    y = 0.5 * x ** 3 / 6 - 0.5 * (x - 1) ** 3 / 6 - (2.25 - 1 / 1.5 + 0 - 1 / 24) / 3 * x
    assert close(y, -0.500, 0.002)
    Tab = 19.62 / (0.5 * math.cos(r(45)) / math.sin(r(45)) + math.cos(r(30)))   # 1-54
    assert close(Tab / (math.pi * 36) * 1e3, 127, 0.5)
    I = 2 * 12 * 249 ** 3 / 12 + 2 * (100 * 12 ** 3 / 12 + 1200 * 43.5 ** 2)
    assert close(30 * I / 52200 / 1e3, 20.4, 0.05)
    assert close(-15 + math.hypot(15, 12), 4.21, 0.01) and close(math.hypot(15, 12), 19.2, 0.01)
    g = 2 * -300 - (650 + 480)
    assert close(565 + math.hypot(85, g / 2), 1434, 1) and close(2 * math.hypot(85, g / 2), 1738, 1)

    def sec(P):
        return P / 9480 * (1 + 0.4453 / math.cos(5250 / (2 * 131.9) * math.sqrt(P / (200e3 * 9480))))
    assert close(sec(1550e3), 250, 1) and close(math.pi ** 2 * 200e3 * 23.4e6 / 5250 ** 2 / 1e3, 1676, 1)


# ------------------------------------------------------------------ hydraulics & CE203 extras
def test_hydraulics_extra_numbers():
    assert close(9.8 * 2 * 1.5, 29.4, 1e-9) and close(9.8 * 2.6 * 1.2, 30.58, 0.01)
    assert close(29.4 + 9.8 * 0.9 * (2 + 3.2) / 2, 52.3, 0.05)
    assert close(9.8 * (-881 * 0.2 + 13600 * 0.08 + 809 * 0.32 - 998 * 0.26 + 1.2 * 0.09) / 1e3, 8.93, 0.01)
    H, hT, l, c = 24.38, 3.05, 18.29, 0.8
    assert close(H ** 3 / 6 + hT * l ** 2 / 2 + (H - hT) * l ** 2 / 3, 5304, 3)
    assert close(hT ** 3 / c ** 2 / 3 + 2.4 * H * l ** 2 / 3, 6539, 3)
    assert close(60 / (2 * math.pi * 30), 0.318, 0.001) and close(998 * 0.5 * 0.1 / 1.14e-3, 43771, 1)


def test_ce203_extra_numbers():
    Ka = (1 - math.sin(r(28))) / (1 + math.sin(r(28)))
    h = 3.96
    assert close(1.083 * h ** 3 + 9.747 * h ** 2 + 81 * h - 540, 0, 3)
    Pa = 0.5 * Ka * 18 * h ** 2
    z = Pa / (4 * 30 - 18 * h)
    assert close(Pa, 50.9, 0.1) and close(z, 1.05, 0.01) and close(Pa * (z + h / 3) - (120 - 18 * h) * z ** 2 / 2, 94, 0.5)
    assert close(0.575 * 28.1 ** 0.373, 2, 0.01) and close(0.625 * 141.7 ** 0.375, 4, 0.02)


# ------------------------------------------------------------------ moved from test_study_notes.py
def test_tut4_q5_strain_gauge():
    import math
    gamma = 2 * 180e-6 / math.sin(math.radians(30))
    tau = 80e9 * gamma
    T = tau * (math.pi / 2 * 0.05 ** 4) / 0.05
    assert abs(tau / 1e6 - 57.6) < 0.05 and abs(T / 1e3 - 11.31) < 0.01


def test_materials_tutorial_answers():
    import math
    assert 5 - 1.5 == 3.5 and 300 * 0.85 == 255
    assert abs(600 / (0.213 - 0.210) / 1000 - 200) < 1e-6
    assert abs(0.408 * math.sqrt(2) / 4 - 0.144) < 0.0005
    pear = 1 - 0.075
    ef = pear * (6.7 - 0.8) / (6.7 - 0.025)
    assert abs(0.8 + 0.075 * 5.9 - 1.2425) < 1e-9 and abs(ef - 0.818) < 0.001 and abs(pear - ef - 0.107) < 0.001


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


def test_steel_answers():
    import math
    def chi(lam, a):
        ph = 0.5 * (1 + a * (lam - 0.2) + lam ** 2)
        return 1 / (ph + math.sqrt(ph ** 2 - lam ** 2))
    Ncr = math.pi ** 2 * 210000 * 146e6 / 6000 ** 2 / 1e3
    lam = math.sqrt(16400 * 265 / 1e3 / Ncr)
    assert abs(Ncr - 8406) < 5 and abs(lam - 0.719) < 0.002 and abs(chi(lam, 0.49) * 16400 * 265 / 1e3 - 3094) < 5
    assert abs(0.9 * 3900 * 410 / 1.1 / 1e3 - 1308) < 1 and abs(0.664 * 1690 * 470 / 1.1 / 1e3 - 479) < 1
    G = 210000 / 2.6
    Mcr = 1.10 * math.pi ** 2 * 210000 * 1870e4 / 3000 ** 2 * math.sqrt(0.922e12 / 1870e4 + 3000 ** 2 * G * 69.2e4 / (math.pi ** 2 * 210000 * 1870e4)) / 1e6
    lt = math.sqrt(1830e3 * 275 / (Mcr * 1e6))
    assert abs(Mcr - 1182) < 5 and abs(lt - 0.653) < 0.003 and abs(chi(lt, 0.34) * 1830 * 0.275 - 408) < 2
    assert abs(700 * 40 * 265 * (2000 - 40) / 1e6 - 14543) < 1
    assert abs(0.83 / (1920 / (86.4 * 13 * math.sqrt(235 / 275))) * 13 * 1920 * 275 / math.sqrt(3) / 1e3 - 1779) < 15
    assert abs(1.35 * 0.9 + 1.5 * 0.4 - 1.815) < 1e-9 and abs(0.5 * 2 * 10.89 * 7 / math.cos(math.radians(15)) - 78.92) < 0.05


def test_analysis_answers():
    import numpy as np
    k = np.array([-0.1667, -0.0729, 0.0938])
    assert abs(k @ [-47.57, 41.14, -20.57] + 31.5 - 34.5) < 0.05   # Tut 2 Q1(a)
    assert abs(k @ [-20.57, 41.14, -20.57] + 36 - 34.5) < 0.05     # Tut 2 Q1(b)
    import math                                                     # plastic: propped cantilever UDL
    a = min((x for x in np.linspace(0.3, 0.5, 20001)), key=lambda a: 2 * (1 + a) / (a * (1 - a)))
    assert abs(a - (math.sqrt(2) - 1)) < 1e-3 and abs(2 * (1 + a) / (a * (1 - a)) - 11.66) < 0.01
