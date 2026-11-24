import pandas as pd
import streamlit as st

from utils import calcs
from utils.state import init

init()
st.title("Quick calculators")
st.caption("Pure functions from `utils/calcs.py` (unit-tested). Show your working in the exam — "
           "these are for checking.")

tabs = st.tabs(["Soil phase", "EC2 beam", "EC3 Mc,Rd / Vpl,Rd", "Euler Ncr", "EC7 Nq/Nc/Nγ",
                "Manning trapezoid", "Rational method", "Greenshields"])


def show(d: dict, fmt: dict | None = None):
    fmt = fmt or {}
    cols = st.columns(min(4, len(d)))
    for i, (k, (v, unit)) in enumerate(d.items()):
        cols[i % len(cols)].metric(k, f"{v:{fmt.get(k, '.3g')}} {unit}".strip())


with tabs[0]:
    c = st.columns(3)
    Gs = c[0].number_input("Gs", 2.0, 3.2, 2.70, 0.01)
    e = c[1].number_input("Void ratio e", 0.05, 5.0, 0.65, 0.01)
    w = c[2].number_input("Water content w (%)", 0.0, 300.0, 18.0, 0.5) / 100
    try:
        r = calcs.soil_phase(Gs, e, w)
        show({"S": (r["S"] * 100, "%"), "n": (r["n"], ""), "γd": (r["gamma_d"], "kN/m³"),
              "γ": (r["gamma"], "kN/m³"), "γsat": (r["gamma_sat"], "kN/m³"), "γ′": (r["gamma_sub"], "kN/m³")},
             {"S": ".1f", "γd": ".2f", "γ": ".2f", "γsat": ".2f", "γ′": ".2f"})
        st.latex(r"Se = wG_s,\quad \gamma = \frac{(G_s + Se)\gamma_w}{1+e}")
    except ValueError as ex:
        st.error(str(ex))

with tabs[1]:
    c = st.columns(4)
    M = c[0].number_input("M_Ed (kNm)", 1.0, 5000.0, 297.4)
    b = c[1].number_input("b (mm)", 100.0, 3000.0, 300.0)
    d = c[2].number_input("d (mm)", 100.0, 3000.0, 540.0)
    fck = c[3].selectbox("f_ck (N/mm²)", [20, 25, 30, 32, 35, 40, 45, 50], index=2)
    c = st.columns(3)
    fyk = c[0].number_input("f_yk", 250.0, 600.0, 500.0)
    d2 = c[1].number_input("d₂ (mm)", 20.0, 200.0, 50.0)
    Kp = c[2].number_input("K′", 0.10, 0.21, 0.167, 0.001, format="%.3f",
                           help=calcs.NA_DEPENDENT["K_prime"])
    r = calcs.ec2_rect_beam(M, b, d, fck, fyk, d2, Kp)
    show({"K": (r["K"], ""), "z": (r["z"], "mm"), "z/d": (r["z_over_d"], ""), "x": (r["x"], "mm"),
          "As": (r["As"], "mm²"), "As2": (r["As2"], "mm²"), "As,min": (r["As_min"], "mm²")},
         {"K": ".4f", "z": ".0f", "z/d": ".3f", "x": ".0f", "As": ".0f", "As2": ".0f", "As,min": ".0f"})
    st.info("Doubly reinforced (K > K′)" if r["doubly"] else "Singly reinforced (K ≤ K′)")
    st.caption("αcc = 0.85, γc = 1.5, γs = 1.15 assumed. ⚠ " + calcs.NA_DEPENDENT["alpha_cc"])

with tabs[2]:
    st.caption("Default: UKB 457×191×67, S355")
    c = st.columns(4)
    Wpl = c[0].number_input("W_pl (cm³)", 1.0, 50000.0, 1471.0) * 1e3
    fy = c[1].number_input("f_y (N/mm²)", 235.0, 460.0, 355.0)
    g0 = c[2].number_input("γ_M0", 1.0, 1.2, 1.0, 0.05, help=calcs.NA_DEPENDENT["gamma_M0"])
    A = c[3].number_input("A (mm²)", 100.0, 1e5, 8550.0)
    c = st.columns(5)
    bf = c[0].number_input("b (mm)", 10.0, 1000.0, 189.9)
    tf = c[1].number_input("t_f (mm)", 1.0, 100.0, 12.7)
    tw = c[2].number_input("t_w (mm)", 1.0, 100.0, 8.5)
    rr = c[3].number_input("r (mm)", 0.0, 50.0, 10.2)
    hw = c[4].number_input("h_w (mm)", 10.0, 2000.0, 428.0)
    Av = calcs.ec3_Av_rolled_I(A, bf, tf, tw, rr, hw)
    show({"Mc,Rd": (calcs.ec3_Mc_Rd(Wpl, fy, g0), "kNm"), "Av": (Av, "mm²"),
          "Vpl,Rd": (calcs.ec3_Vpl_Rd(Av, fy, g0), "kN"), "ε": (calcs.ec3_epsilon(fy), "")},
         {"Mc,Rd": ".1f", "Av": ".0f", "Vpl,Rd": ".0f", "ε": ".3f"})

with tabs[3]:
    c = st.columns(4)
    E = c[0].number_input("E (N/mm²)", 1000.0, 300000.0, 210000.0)
    I = c[1].number_input("I (×10⁶ mm⁴)", 0.01, 1e5, 25.0) * 1e6
    L = c[2].number_input("L (m)", 0.1, 100.0, 5.0)
    ends = {"Pinned–pinned (1.0)": 1.0, "Fixed–free (2.0)": 2.0, "Fixed–pinned (0.7)": 0.7, "Fixed–fixed (0.5)": 0.5}
    k = ends[c[3].selectbox("End conditions", list(ends))]
    show({"L_cr": (k * L, "m"), "N_cr": (calcs.euler_Ncr(E, I, k * L * 1000), "kN")}, {"L_cr": ".2f", "N_cr": ".1f"})

with tabs[4]:
    phi = st.slider("φ′ (°)", 0.0, 45.0, 30.0, 0.5)
    gphi = st.radio("γ_φ′", [1.0, 1.25], horizontal=True, format_func=lambda g: f"{g} ({'M1' if g == 1 else 'M2'})")
    pd_ = calcs.phi_design(phi, gphi)
    f = calcs.ec7_bearing_factors(pd_) if pd_ > 0 else {"Nq": 1.0, "Nc": 5.14, "Ngamma": 0.0}
    show({"φ′d": (pd_, "°"), "Nq": (f["Nq"], ""), "Nc": (f["Nc"], ""), "Nγ": (f["Ngamma"], "")},
         {"φ′d": ".2f", "Nq": ".2f", "Nc": ".2f", "Nγ": ".2f"})
    st.caption("EC7 Annex D.4. φ = 0 → undrained N_c = π + 2.")

with tabs[5]:
    c = st.columns(5)
    bb = c[0].number_input("b (m)", 0.0, 100.0, 3.0)
    z = c[1].number_input("z (H:1V)", 0.0, 10.0, 2.0)
    n = c[2].number_input("Manning n", 0.008, 0.2, 0.015, 0.001, format="%.3f")
    S0 = c[3].number_input("S₀", 1e-6, 0.5, 0.0008, format="%.5f")
    mode = c[4].radio("Solve", ["Q from y", "y from Q"])
    if mode == "Q from y":
        y = st.number_input("Depth y (m)", 0.01, 50.0, 1.295)
    else:
        Q = st.number_input("Q (m³/s)", 0.001, 1e5, 12.0)
        y = calcs.normal_depth_trapezoid(Q, bb, z, n, S0)
    r = calcs.manning_trapezoid(bb, z, y, n, S0)
    yc = calcs.critical_depth_trapezoid(r["Q"], bb, z)
    show({"y": (y, "m"), "A": (r["A"], "m²"), "P": (r["P"], "m"), "R": (r["R"], "m"), "Q": (r["Q"], "m³/s"),
          "V": (r["V"], "m/s"), "Fr": (r["Fr"], ""), "y_c": (yc, "m")},
         {k: ".3f" for k in ["y", "A", "P", "R", "Q", "V", "Fr", "y_c"]})
    st.info(f"Slope: **{calcs.slope_class(y, yc)}** · flow is {'subcritical' if r['Fr'] < 1 else 'supercritical'}"
            + (" (y taken as normal depth)" if mode == "y from Q" else " (classification valid if y = y_n)"))

with tabs[6]:
    c = st.columns(4)
    C = c[0].number_input("Runoff coefficient C", 0.05, 1.0, 0.85)
    i = c[1].number_input("Intensity i (mm/h)", 1.0, 500.0, 120.0)
    unit = c[2].radio("Area unit", ["ha", "km2"], horizontal=True)
    Ar = c[3].number_input("Area", 0.01, 1e5, 25.0)
    show({"Q": (calcs.rational_Q(C, i, Ar, unit), "m³/s")}, {"Q": ".3f"})
    st.latex(r"Q = \frac{CiA}{360}\ (A\ \mathrm{ha}) = 0.278\,CiA\ (A\ \mathrm{km^2})")

with tabs[7]:
    c = st.columns(2)
    vf = c[0].number_input("Free-flow speed v_f (km/h)", 10.0, 200.0, 100.0)
    kj = c[1].number_input("Jam density k_j (veh/km)", 10.0, 300.0, 120.0)
    g = calcs.greenshields(vf, kj)
    show({"q_max": (g["q_max"], "veh/h"), "k_c": (g["k_c"], "veh/km"), "v_c": (g["v_c"], "km/h")},
         {"q_max": ".0f", "k_c": ".1f", "v_c": ".1f"})
    st.markdown("**Shockwave between two states**")
    c = st.columns(4)
    q1 = c[0].number_input("q₁ (veh/h)", 0.0, g["q_max"], min(1800.0, g["q_max"]))
    s1 = c[1].radio("State 1", ["uncongested", "congested"], key="s1")
    q2 = c[2].number_input("q₂ (veh/h)", 0.0, g["q_max"], min(1200.0, g["q_max"]))
    s2 = c[3].radio("State 2", ["uncongested", "congested"], index=1, key="s2")
    k1 = calcs.greenshields_density(q1, vf, kj, s1 == "congested")
    k2 = calcs.greenshields_density(q2, vf, kj, s2 == "congested")
    if abs(k2 - k1) > 1e-9:
        uw = calcs.shockwave_speed(q1, k1, q2, k2)
        show({"k₁": (k1, "veh/km"), "k₂": (k2, "veh/km"), "u_w": (uw, "km/h")},
             {"k₁": ".1f", "k₂": ".1f", "u_w": ".2f"})
        st.caption("Negative u_w → shockwave moves upstream.")
    st.markdown("**AASHTO stopping sight distance**")
    c = st.columns(3)
    V = c[0].number_input("Design speed (km/h)", 20.0, 140.0, 100.0)
    t = c[1].number_input("Reaction time (s)", 0.5, 5.0, 2.5)
    G = c[2].number_input("Grade G (%; − = downgrade)", -12.0, 12.0, 0.0) / 100
    ssd = calcs.aashto_ssd(V, t, grade=G)
    show({"Reaction": (ssd["reaction"], "m"), "Braking": (ssd["braking"], "m"), "SSD": (ssd["SSD"], "m")},
         {"Reaction": ".1f", "Braking": ".1f", "SSD": ".1f"})
