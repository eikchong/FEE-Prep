"""Formula & code-sheet content. LaTeX is kept inside the matplotlib-mathtext subset so the
same strings render in st.latex (KaTeX) and in the printable PDF.

verify=True → value depends on a Nationally Determined Parameter: "verify against Singapore NA".
"""
from __future__ import annotations

def F(title, latex="", clause="", note="", verify=False, src=None, legacy=False):
    """One sheet entry. latex="" → a text-only key point. src=(doc, page) cites the lecture notes."""
    return {"title": title, "latex": latex, "clause": clause, "note": note, "verify": verify,
            "src": {"doc": src[0], "page": src[1]} if src else None, "legacy": legacy}

FORMULAS: dict[str, list[dict]] = {
 "CE101": [
  F("Axial deformation", r"\delta = \frac{N L}{A E}", "", "Hooke's law; E_steel = 200–210 GPa"),
  F("Poisson's ratio", r"\nu = -\frac{\varepsilon_{lat}}{\varepsilon_{long}}"),
  F("Thermal strain", r"\varepsilon_T = \alpha \Delta T", "", "α ≈ 12×10⁻⁶ /°C (steel), 10×10⁻⁶ /°C (concrete)"),
  F("Concrete mean strength", r"f_{cm} = f_{ck} + 8\ \mathrm{MPa}", "EC2 Table 3.1"),
  F("Concrete tensile strength", r"f_{ctm} = 0.30 f_{ck}^{2/3}\quad (f_{ck}\leq 50)", "EC2 Table 3.1"),
  F("Concrete modulus", r"E_{cm} = 22\left(\frac{f_{cm}}{10}\right)^{0.3}\ \mathrm{GPa}", "EC2 Table 3.1"),
  F("Target mean strength (mix design)", r"f_m = f_{ck} + k s", "", "k = 1.64 for 5% defectives"),
  F("Creep strain", r"\varepsilon_{cc}(t) = \varphi(t,t_0)\frac{\sigma_c}{E_c}", "EC2 3.1.4"),
 ],
 "CE102": [
  F("Bending stress", r"\sigma = \frac{M y}{I} = \frac{M}{W}"),
  F("Shear stress (beam)", r"\tau = \frac{V Q}{I b}"),
  F("Torsion (circular)", r"\tau = \frac{T r}{J},\quad \theta = \frac{T L}{G J},\quad J = \frac{\pi d^4}{32}"),
  F("Truss determinacy", r"m + r = 2j", "", "m + r > 2j → indeterminate; < 2j → mechanism"),
  F("SS beam, UDL", r"M_{max} = \frac{wL^2}{8},\quad \delta_{max} = \frac{5wL^4}{384EI}"),
  F("SS beam, central point load", r"M_{max} = \frac{PL}{4},\quad \delta_{max} = \frac{PL^3}{48EI}"),
  F("Cantilever, tip load", r"M = PL,\quad \delta = \frac{PL^3}{3EI}"),
  F("Cantilever, UDL", r"M = \frac{wL^2}{2},\quad \delta = \frac{wL^4}{8EI}"),
 ],
 "CE103": [
  F("Unit-load (virtual work) deflection", r"\delta = \int \frac{M m}{EI}\,dx + \sum \frac{N n L}{AE}"),
  F("Fixed-end moments (UDL / central P)", r"FEM = \frac{wL^2}{12},\quad FEM = \frac{PL}{8}"),
  F("Member stiffness", r"k = \frac{4EI}{L}\ (\mathrm{far\ fixed}),\quad k = \frac{3EI}{L}\ (\mathrm{far\ pinned})",
    "", "carry-over factor ½ to a fixed far end"),
  F("Slope-deflection", r"M_{AB} = \frac{2EI}{L}\left(2\theta_A + \theta_B - \frac{3\Delta}{L}\right) + FEM_{AB}"),
  F("Euler buckling", r"N_{cr} = \frac{\pi^2 EI}{L_{cr}^2}", "", "L_cr: pinned 1.0L, fixed–free 2.0L, fixed–fixed 0.5L, fixed–pinned 0.7L"),
  F("Plastic collapse (fixed beam, central P)", r"P_c = \frac{8 M_p}{L}", "", "Fixed UDL: w_c = 16M_p/L²; SS UDL: 8M_p/L²"),
  F("Shape factor", r"\nu = \frac{W_{pl}}{W_{el}}", "", "rectangle 1.5; I-section ≈ 1.12–1.15"),
 ],
 "CE104": [
  F("Phase relations", r"Se = wG_s,\quad \gamma = \frac{(G_s + Se)\gamma_w}{1+e},\quad n = \frac{e}{1+e}"),
  F("Effective stress", r"\sigma' = \sigma - u"),
  F("Mohr–Coulomb", r"\tau_f = c' + \sigma'_n \tan\varphi'", "", "undrained: τ_f = c_u"),
  F("Darcy", r"q = k i A"),
  F("Consolidation settlement (NC clay)", r"s_c = \frac{C_c H}{1+e_0}\log_{10}\frac{\sigma'_f}{\sigma'_0}", "", "or s = m_v Δσ′ H"),
  F("Time factor", r"T_v = \frac{c_v t}{H_{dr}^2},\quad T_v \approx \frac{\pi}{4}U^2\ (U\leq 0.6)", "", "T_v(50%) = 0.197, T_v(90%) = 0.848"),
  F("Flow net seepage", r"q = k H \frac{N_f}{N_d}"),
  F("Critical hydraulic gradient", r"i_c = \frac{\gamma'}{\gamma_w}"),
 ],
 "CE105": [
  F("Hydrostatic thrust", r"F = \rho g \bar{h} A,\quad y_{cp} = \bar{y} + \frac{I_G}{A\bar{y}}"),
  F("Metacentric height", r"GM = \frac{I}{V_d} - BG", "", "stable if GM > 0"),
  F("Continuity", r"Q = A_1 V_1 = A_2 V_2"),
  F("Bernoulli", r"\frac{p_1}{\rho g} + \frac{V_1^2}{2g} + z_1 = \frac{p_2}{\rho g} + \frac{V_2^2}{2g} + z_2 + h_L"),
  F("Momentum", r"\sum F = \rho Q (V_2 - V_1)"),
  F("Reynolds / Froude", r"Re = \frac{\rho V D}{\mu},\quad Fr = \frac{V}{\sqrt{gL}}"),
  F("Froude similitude", r"V_r = L_r^{1/2},\quad Q_r = L_r^{5/2},\quad t_r = L_r^{1/2}"),
 ],
 "CE201": [
  F("ULS combination (fundamental)", r"E_d = \sum \gamma_G G_k + \gamma_Q Q_{k,1} + \sum \gamma_Q \psi_0 Q_{k,i}",
    "EC0 6.10 (or 6.10a/b)", "γ_G = 1.35, γ_Q = 1.5 (recommended)", True),
  F("Design strengths", r"f_{cd} = \frac{\alpha_{cc} f_{ck}}{\gamma_c},\quad f_{yd} = \frac{f_{yk}}{\gamma_s}",
    "EC2 3.1.6, 2.4.2.4", "γ_c = 1.5, γ_s = 1.15; α_cc NA value", True),
  F("Flexure: K and lever arm", r"K = \frac{M}{b d^2 f_{ck}},\quad z = d\left[0.5 + \sqrt{0.25 - \frac{K}{1.134}}\right] \leq 0.95d",
    "EC2 6.1 (rect. block, α_cc = 0.85)", "K′ = 0.167 with no redistribution", True),
  F("Tension steel", r"A_s = \frac{M}{f_{yd} z}", "EC2 6.1"),
  F("Compression steel (K > K′)", r"A_{s2} = \frac{(K - K')f_{ck} b d^2}{f_{yd}(d - d_2)}", "EC2 6.1", "", True),
  F("Minimum tension steel", r"A_{s,min} = 0.26\frac{f_{ctm}}{f_{yk}} b_t d \geq 0.0013 b_t d", "EC2 9.2.1.1"),
  F("Shear without links", r"V_{Rd,c} = \left[C_{Rd,c} k (100\rho_l f_{ck})^{1/3}\right] b_w d,\quad k = 1 + \sqrt{200/d} \leq 2",
    "EC2 6.2.2 (6.2a)", "C_Rd,c = 0.18/γ_c; v_min = 0.035k^{3/2}f_ck^{1/2}", True),
  F("Shear links", r"\frac{A_{sw}}{s} = \frac{V_{Ed}}{0.9 d f_{ywd}\cot\theta},\quad 1 \leq \cot\theta \leq 2.5",
    "EC2 6.2.3 (6.8)"),
  F("Strut crushing", r"V_{Rd,max} = \frac{\alpha_{cw} b_w z \nu_1 f_{cd}}{\cot\theta + \tan\theta},\quad \nu_1 = 0.6\left(1 - \frac{f_{ck}}{250}\right)",
    "EC2 6.2.3 (6.9)"),
  F("Minimum eccentricity", r"e_0 = \max(h/30,\ 20\ \mathrm{mm})", "EC2 6.1(4)"),
  F("Slenderness limit", r"\lambda_{lim} = \frac{20 A B C}{\sqrt{n}},\quad n = \frac{N_{Ed}}{A_c f_{cd}}", "EC2 5.8.3.1", "A = 0.7, B = 1.1, C = 0.7 if unknown", True),
  F("Nominal curvature 2nd-order moment", r"M_2 = N_{Ed} e_2,\quad e_2 = \frac{1}{r}\frac{l_0^2}{c},\quad \frac{1}{r_0} = \frac{f_{yd}}{0.45 E_s d}",
    "EC2 5.8.8"),
  F("Basic span/depth", r"\frac{l}{d} = K\left[11 + 1.5\sqrt{f_{ck}}\frac{\rho_0}{\rho} + 3.2\sqrt{f_{ck}}\left(\frac{\rho_0}{\rho} - 1\right)^{3/2}\right]\ (\rho \leq \rho_0)",
    "EC2 7.4.2 (7.16a)", "ρ₀ = √f_ck × 10⁻³", True),
  F("Punching basic perimeter", r"v_{Ed} = \frac{\beta V_{Ed}}{u_i d},\quad u_1\ \mathrm{at}\ 2d", "EC2 6.4"),
  F("Prestress: stress at a fibre", r"\sigma = \frac{P}{A} \pm \frac{P e}{Z} \mp \frac{M}{Z}", "EC2 5.10", "check at transfer and service"),
 ],
 "CE202": [
  F("ε and classification", r"\varepsilon = \sqrt{235/f_y}", "EC3 Table 5.2", "flange outstand c/t ≤ 9ε (Class 1), web c/t ≤ 72ε (bending)"),
  F("Bending resistance", r"M_{c,Rd} = \frac{W_{pl} f_y}{\gamma_{M0}}", "EC3 6.2.5", "W_el for Class 3", True),
  F("Shear resistance", r"V_{pl,Rd} = \frac{A_v (f_y/\sqrt{3})}{\gamma_{M0}},\quad A_v = A - 2bt_f + (t_w + 2r)t_f",
    "EC3 6.2.6", "high shear if V_Ed > 0.5V_pl,Rd (6.2.8)"),
  F("Shear buckling check", r"\frac{h_w}{t_w} > \frac{72\varepsilon}{\eta}", "EC3 6.2.6(6), EN 1993-1-5"),
  F("Flexural buckling", r"\bar{\lambda} = \frac{L_{cr}}{i\lambda_1},\quad \lambda_1 = 93.9\varepsilon,\quad \Phi = 0.5[1 + \alpha(\bar{\lambda} - 0.2) + \bar{\lambda}^2]",
    "EC3 6.3.1.2", "α: a0 0.13, a 0.21, b 0.34, c 0.49, d 0.76"),
  F("Buckling reduction", r"\chi = \frac{1}{\Phi + \sqrt{\Phi^2 - \bar{\lambda}^2}} \leq 1,\quad N_{b,Rd} = \frac{\chi A f_y}{\gamma_{M1}}", "EC3 6.3.1"),
  F("Elastic critical LTB moment", r"M_{cr} = C_1\frac{\pi^2 E I_z}{L^2}\sqrt{\frac{I_w}{I_z} + \frac{L^2 G I_t}{\pi^2 E I_z}}",
    "SN003 / NCCI", "C₁ = 1.127 UDL, 1.348 central point load, 1.0 uniform moment"),
  F("LTB (rolled sections)", r"\Phi_{LT} = 0.5[1 + \alpha_{LT}(\bar{\lambda}_{LT} - 0.4) + 0.75\bar{\lambda}_{LT}^2],\quad \chi_{LT} = \frac{1}{\Phi_{LT} + \sqrt{\Phi_{LT}^2 - 0.75\bar{\lambda}_{LT}^2}}",
    "EC3 6.3.2.3", "h/b ≤ 2 curve b; > 2 curve c", True),
  F("Combined N + M", r"\frac{N_{Ed}}{\chi_y N_{Rk}/\gamma_{M1}} + k_{yy}\frac{M_{y,Ed}}{\chi_{LT}M_{y,Rk}/\gamma_{M1}} + k_{yz}\frac{M_{z,Ed}}{M_{z,Rk}/\gamma_{M1}} \leq 1",
    "EC3 6.3.3 (6.61/6.62)"),
  F("Bolt shear", r"F_{v,Rd} = \frac{\alpha_v f_{ub} A}{\gamma_{M2}}", "EC3-1-8 Table 3.4", "α_v = 0.6 (8.8, 4.6), 0.5 (10.9)", True),
  F("Bolt bearing", r"F_{b,Rd} = \frac{k_1 \alpha_b f_u d t}{\gamma_{M2}}", "EC3-1-8 Table 3.4", "", True),
  F("Fillet weld (simplified)", r"F_{w,Rd} = \frac{f_u/\sqrt{3}}{\beta_w \gamma_{M2}} a", "EC3-1-8 4.5.3.3", "β_w = 0.9 (S355)", True),
  F("Frame stability", r"\alpha_{cr} = \frac{H_{Ed}}{V_{Ed}}\frac{h}{\delta_{H,Ed}}", "EC3 5.2.1", "≥ 10 elastic, ≥ 15 plastic → 1st order OK"),
 ],
 "CE203": [
  F("EC7 Design Approach 1", r"\mathrm{C1: A1+M1+R1}\quad \mathrm{C2: A2+M2+R1}", "EC7 2.4.7.3.4",
    "A1: γ_G 1.35/γ_Q 1.5; A2: 1.0/1.3; M2: γ_φ′ = γ_c′ = 1.25, γ_cu = 1.4", True),
  F("Bearing factors", r"N_q = e^{\pi\tan\varphi'}\tan^2\left(45 + \frac{\varphi'}{2}\right),\quad N_c = (N_q - 1)\cot\varphi',\quad N_\gamma = 2(N_q - 1)\tan\varphi'",
    "EC7 Annex D.4"),
  F("Drained bearing resistance", r"\frac{R}{A'} = c'N_c b_c s_c i_c + q'N_q b_q s_q i_q + 0.5\gamma' B' N_\gamma b_\gamma s_\gamma i_\gamma",
    "EC7 Annex D (D.2)", "rectangular: s_q = 1 + (B′/L′)sinφ′"),
  F("Undrained bearing resistance", r"\frac{R}{A'} = (\pi + 2) c_u b_c s_c i_c + q", "EC7 Annex D (D.1)"),
  F("Rankine coefficients", r"K_a = \frac{1 - \sin\varphi'}{1 + \sin\varphi'},\quad K_p = \frac{1}{K_a},\quad K_0 = 1 - \sin\varphi'"),
  F("Design friction angle", r"\varphi'_d = \tan^{-1}\left(\frac{\tan\varphi'_k}{\gamma_{\varphi'}}\right)", "EC7 2.4.6.2"),
  F("Schmertmann settlement", r"s = C_1 C_2 \Delta p \sum \frac{I_z}{E}\Delta z,\quad I_{zp} = 0.5 + 0.1\sqrt{\frac{\Delta p}{\sigma'_{vp}}}",
    "EC7-2 Annex D", "strip: peak at z = B, zero at 4B; E = 3.5q_c (strip), 2.5q_c (square)"),
  F("Pile resistance", r"R_{c,d} = \frac{R_{b,k}}{\gamma_b} + \frac{R_{s,k}}{\gamma_s},\quad R_{s,k} = \sum q_{s,k} A_s", "EC7 7.6.2", "include ξ correlation factors", True),
  F("Infinite slope (dry, c′ = 0)", r"FoS = \frac{\tan\varphi'}{\tan\beta}"),
 ],
 "CE204": [
  F("Fundamental relation", r"q = k v"),
  F("Greenshields", r"v = v_f\left(1 - \frac{k}{k_j}\right),\quad q_{max} = \frac{v_f k_j}{4},\quad k_c = \frac{k_j}{2}"),
  F("Shockwave speed", r"u_w = \frac{q_2 - q_1}{k_2 - k_1}"),
  F("AASHTO stopping sight distance", r"SSD = 0.278 V t + \frac{V^2}{254\left(\frac{a}{9.81} \pm G\right)}", "AASHTO Green Book 3.2",
    "t = 2.5 s, a = 3.4 m/s²; level: 0.039V²/a"),
  F("Crest vertical curve (S < L)", r"L = \frac{A S^2}{658}", "AASHTO", "h₁ = 1.08 m, h₂ = 0.60 m; A in %"),
  F("Horizontal curve", r"R = \frac{V^2}{127(e + f)}", "AASHTO"),
  F("Webster optimum cycle", r"C_0 = \frac{1.5L + 5}{1 - Y},\quad Y = \sum y_i"),
  F("Flexible pavement (AASHTO 93)", r"SN = a_1 D_1 + a_2 D_2 m_2 + a_3 D_3 m_3", "AASHTO 1993"),
 ],
 "CE205": [
  F("Darcy–Weisbach", r"h_f = f\frac{L}{D}\frac{V^2}{2g},\quad h_m = K\frac{V^2}{2g}"),
  F("Manning", r"Q = \frac{1}{n} A R^{2/3} S_0^{1/2}"),
  F("Trapezoid geometry", r"A = (b + zy)y,\quad P = b + 2y\sqrt{1+z^2},\quad T = b + 2zy"),
  F("Critical flow", r"\frac{Q^2 T}{g A^3} = 1,\quad y_c = \left(\frac{q^2}{g}\right)^{1/3}\ (\mathrm{rect.})"),
  F("Froude number", r"Fr = \frac{V}{\sqrt{g D}},\quad D = A/T"),
  F("Hydraulic jump (rect.)", r"\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right),\quad \Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}"),
  F("GVF", r"\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}", "", "mild: y_n > y_c (M1, M2, M3); steep: y_n < y_c"),
  F("Rational method", r"Q = \frac{C i A}{360}\ (A\ \mathrm{in\ ha}),\quad Q = 0.278 C i A\ (A\ \mathrm{in\ km^2})", "PUB COP Surface Water Drainage"),
  F("Return period", r"P = 1 - \left(1 - \frac{1}{T}\right)^n", "", "risk of ≥1 exceedance in n years"),
  F("Muskingum", r"O_2 = C_0 I_2 + C_1 I_1 + C_2 O_1"),
 ],
 "CE206": [
  F("Overflow rate", r"v_0 = \frac{Q}{A_s}", "", "primary 30–50 m³/m²·d (average)"),
  F("Detention time", r"t_d = \frac{V}{Q}"),
  F("BOD exertion", r"BOD_t = L_0(1 - e^{-kt})"),
  F("F/M ratio", r"\frac{F}{M} = \frac{Q S_0}{V X}", "", "conventional 0.2–0.4 d⁻¹"),
  F("Solids retention time", r"\theta_c = \frac{V X}{Q_w X_r + Q_e X_e}"),
  F("Biomass in reactor", r"X = \frac{\theta_c Y (S_0 - S)}{\theta (1 + k_d\theta_c)}"),
  F("Sludge volume index", r"SVI = \frac{SV_{30}\ (\mathrm{mL/L}) \times 1000}{MLSS\ (\mathrm{mg/L})}"),
  F("Chick–Watson disinfection", r"\ln\frac{N}{N_0} = -k C^n t"),
 ],
}

LEGACY_NOTE = "Legacy (BS 8110 / BS 5950) methods are not acceptable in FEE 2027 — Eurocodes + Singapore NA only."


# Subjects with lecture notes get sections in lecture order (filled per subject below / in
# utils/formulas_notes.py). Subjects without notes fall back to the flat FORMULAS list.
SECTIONS: dict[str, list[dict]] = {}


def sections(code: str) -> list[dict]:
    """[{title, src, items}] in lecture order; legacy items are kept out (see legacy_items)."""
    if code in SECTIONS:
        secs = list(SECTIONS[code])
        if FORMULAS.get(code):   # our original code-reference entries, after the lecture-order sections
            secs.append({"title": "Quick reference (not from the notes)", "src": None, "items": FORMULAS[code]})
    else:
        secs = [{"title": None, "src": None, "items": FORMULAS.get(code, [])}]
    return [{**sec, "items": [f for f in sec["items"] if not f.get("legacy")]} for sec in secs]


LEGACY: dict[str, list[dict]] = {}   # code -> legacy (non-Eurocode) items found in the notes


def legacy_items(code: str) -> list[dict]:
    return ([f for sec in SECTIONS.get(code, []) for f in sec["items"] if f.get("legacy")]
            + LEGACY.get(code, []))


def all_items(code: str) -> list[dict]:
    return [f for sec in sections(code) for f in sec["items"]]


def codes() -> list[str]:
    return list(dict.fromkeys([*FORMULAS, *SECTIONS]))


try:  # lecture-note content lives in its own module to keep this file readable
    from utils.formulas_notes import NOTES_LEGACY, NOTES_SECTIONS
    SECTIONS.update(NOTES_SECTIONS)
    LEGACY.update(NOTES_LEGACY)
except ImportError:  # pragma: no cover
    pass
