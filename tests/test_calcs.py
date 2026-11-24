"""Calculator functions vs hand-worked examples."""
import math

import pytest

from utils import calcs as c

approx = lambda v, rel=2e-3: pytest.approx(v, rel=rel)  # noqa: E731


def test_soil_phase_hand():
    r = c.soil_phase(2.70, 0.65, 0.18)
    assert r["S"] == approx(0.7477)
    assert r["gamma_d"] == approx(2.70 * 9.81 / 1.65)        # 16.05
    assert r["gamma"] == approx(18.94)
    assert r["gamma_sat"] == approx(19.92)
    assert r["n"] == approx(0.394)


def test_soil_phase_rejects_oversaturated():
    with pytest.raises(ValueError):
        c.soil_phase(2.70, 0.4, 0.30)


def test_effective_stress():
    r = c.effective_stress([(2, 18), (10, 20)], z=6, z_w=2)
    assert r["sigma_v"] == approx(116.0)
    assert r["u"] == approx(39.24)
    assert r["sigma_v_eff"] == approx(76.76)


def test_consolidation_time():
    assert c.consolidation_time(2, 3, 0.5) == approx(0.196 * 9 / 2, rel=5e-3)
    assert c.consolidation_time(2, 3, 0.9) == approx(0.848 * 9 / 2, rel=5e-3)


def test_ec2_singly_reinforced_hand():
    # M = 297.4 kNm, 300 x 540, C30/37, B500: K = 0.1133, z = 479 mm, As = 1428 mm2
    r = c.ec2_rect_beam(297.42, 300, 540, 30)
    assert r["K"] == approx(0.1133)
    assert r["z"] == approx(479.2)
    assert r["As"] == approx(1427.6)
    assert not r["doubly"]
    assert r["As_min"] == approx(0.26 * 0.30 * 30 ** (2 / 3) / 500 * 300 * 540)


def test_ec2_lever_arm_cap():
    r = c.ec2_rect_beam(20, 300, 540, 30)   # tiny K → z capped at 0.95d
    assert r["z"] == approx(0.95 * 540)


def test_ec2_doubly_reinforced():
    # 250 x 450 (d2 = 50), C25, M = 300 kNm → K = 0.237 > 0.167
    r = c.ec2_rect_beam(300, 250, 450, 25)
    assert r["doubly"]
    K = 300e6 / (250 * 450 ** 2 * 25)
    As2 = (K - 0.167) * 25 * 250 * 450 ** 2 / (500 / 1.15 * 400)
    assert r["As2"] == approx(As2)
    z = 450 * (0.5 + math.sqrt(0.25 - 0.167 / 1.134))
    assert r["As"] == approx(0.167 * 25 * 250 * 450 ** 2 / (500 / 1.15 * z) + As2)


def test_short_column_axial():
    r = c.ec2_short_column_axial(3800, 400, 400, 35)
    assert r["N_conc_kN"] == approx(3175.2)
    assert r["sigma_s"] == 400
    assert r["As_simple"] == approx(1562.0)


def test_ec3_ukb_457():
    assert c.ec3_Mc_Rd(1471e3, 355) == approx(522.2)
    Av = c.ec3_Av_rolled_I(8550, 189.9, 12.7, 8.5, 10.2, 428.0)
    assert Av == approx(8550 - 2 * 189.9 * 12.7 + (8.5 + 20.4) * 12.7)
    assert c.ec3_Vpl_Rd(Av, 355) == approx(Av * 355 / math.sqrt(3) / 1e3)


def test_euler():
    assert c.euler_Ncr(210000, 25e6, 5000) == approx(2072.6)
    assert c.euler_Ncr(210000, 25e6, 10000) == approx(518.2)


def test_flexural_buckling_uc254():
    r = c.ec3_flexural_buckling(9310, 355, 5000, 64.6, 0.49)
    assert r["lambda1"] == approx(76.41)
    assert r["lambda_bar"] == approx(1.013)
    assert r["chi"] == approx(0.532, rel=5e-3)
    assert r["Nb_Rd"] == approx(1760, rel=5e-3)


def test_ltb_mcr_and_chi():
    Mcr = c.ec3_Mcr(8000, 1452e4, 37.1e4, 0.705e12, C1=1.127)
    # hand: π²EIz/L² = 470.2 kN; √(Iw/Iz + L²GIt/(π²EIz)) = 0.3354 m → ×1.127
    a = math.pi ** 2 * 210000 * 1452e4 / 8000 ** 2
    b = math.sqrt(0.705e12 / 1452e4 + 8000 ** 2 * 81000 * 37.1e4 / (math.pi ** 2 * 210000 * 1452e4))
    assert Mcr == approx(1.127 * a * b / 1e6)
    assert Mcr == approx(177.7)
    r = c.ec3_ltb_rolled(1471e3, 355, Mcr, 2.39)
    assert r["alpha_LT"] == 0.49
    assert r["chi_LT"] == approx(0.318, rel=5e-3)


def test_bolt_shear_table_3_4():
    assert c.ec3_bolt_shear(800, 245) == approx(94.08)
    assert c.ec3_bolt_shear(1000, 245, alpha_v=0.5) == approx(98.0)


def test_ec7_factors_annex_d():
    f = c.ec7_bearing_factors(30)
    assert f["Nq"] == approx(18.40)
    assert f["Nc"] == approx(30.14)
    assert f["Ngamma"] == approx(20.09)
    assert c.phi_design(30, 1.25) == approx(24.79)


def test_schmertmann():
    r = c.schmertmann_strip(156, 19, 57, 2.0, [(0, 2, 21000), (2, 4, 28000), (4, 6, 35000), (6, 8, 42000)])
    assert r["Iz_p"] == approx(0.6654)
    assert r["C1"] == approx(0.9391)
    assert r["s_mm"] == approx(15.4, rel=5e-3)


def test_rankine():
    assert c.rankine_Ka(30) == approx(1 / 3)
    assert c.rankine_Kp(30) == approx(3.0)


def test_manning_trapezoid_and_depths():
    r = c.manning_trapezoid(3, 2, 1.0, 0.015, 0.0008)
    assert r["A"] == approx(5.0)
    assert r["P"] == approx(3 + 2 * math.sqrt(5))
    assert r["Q"] == approx((1 / 0.015) * 5 * (5 / (3 + 2 * math.sqrt(5))) ** (2 / 3) * math.sqrt(0.0008))
    yn = c.normal_depth_trapezoid(12, 3, 2, 0.015, 0.0008)
    yc = c.critical_depth_trapezoid(12, 3, 2)
    assert c.manning_trapezoid(3, 2, yn, 0.015, 0.0008)["Q"] == approx(12, rel=1e-6)
    g = c.trapezoid(3, 2, yc)
    assert 12 ** 2 * g["T"] / (9.81 * g["A"] ** 3) == approx(1, rel=1e-6)
    assert c.slope_class(yn, yc).startswith("Mild")


def test_critical_depth_rectangular_matches_closed_form():
    # z = 0 → yc = (q²/g)^(1/3)
    yc = c.critical_depth_trapezoid(10, 4, 0)
    assert yc == approx(((10 / 4) ** 2 / 9.81) ** (1 / 3))


def test_rational():
    assert c.rational_Q(0.85, 120, 25, "ha") == approx(7.083)
    assert c.rational_Q(0.5, 50, 2, "km2") == approx(13.89)


def test_greenshields_and_shockwave():
    g = c.greenshields(100, 120)
    assert (g["q_max"], g["k_c"], g["v_c"]) == (3000, 60, 50)
    k1 = c.greenshields_density(1800, 100, 120)
    k2 = c.greenshields_density(1200, 100, 120, congested=True)
    assert k1 == approx(22.05)
    assert k2 == approx(106.48)
    assert c.shockwave_speed(1800, k1, 1200, k2) == approx(-7.107)
    with pytest.raises(ValueError):
        c.greenshields_density(3500, 100, 120)


def test_aashto_ssd():
    assert c.aashto_ssd(100)["SSD"] == approx(184.2)
    assert c.aashto_ssd(100, grade=-0.03)["SSD"] == approx(193.9)


def test_environmental():
    cl = c.clarifier(20000, 40, 2)
    assert (cl["A"], round(cl["D"], 1), round(cl["depth"], 2)) == (500, 25.2, 3.33)
    a = c.activated_sludge(20000, 180, 0.3, 2500, 150, 8000)
    assert a["V"] == approx(4800) and a["HRT_h"] == approx(5.76) and a["SRT_d"] == approx(10.0)
