"""CE201 Reinforced & Prestressed Concrete — CE3165 Structural Concrete Design (Du Hongjian; Tan K H, part II).

Lecture decks are text PDFs; the tutorial solutions are scanned and were read by OCR, so only clearly legible
results are quoted. EC2 (SS EN 1992-1-1 + Singapore NA) throughout.
"""


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


C = "CE201/CE3165/"
T = C + "tutorials/"
D = {
    "L0": C + "0 Intro.pdf", "L1": C + "1 Design Philosophy.pdf", "L2": C + "2 Design for Flexure and Shear.pdf",
    "L3": C + "3 Cracking and Deflection.pdf", "L4": C + "4 Detailing of Reinforcement.pdf",
    "L6": C + "6 Prestressed Concrete.pdf", "L7": C + "7 Part II Tan KH.pdf",
    "T1": T + "Tut 1 Analysis for Flexure.pdf", "T2": T + "Tut 2 Design for Flexure.pdf",
    "T3": T + "Tut 3 Design for Shear.pdf", "T4": T + "Tut 4 Cracking and Deflection.pdf",
    "T5": T + "Tut 5 Detailing.pdf", "T6": T + "Tut 6 Load Path.pdf", "T67": T + "Tut 6-7 Structural Members.pdf",
    "T8": T + "Tut 8 Columns and Bases.pdf", "T9": T + "Tut 9 Prestressed.pdf",
}
OUTLINE = [("L0", 7, 1, ["CE201-01"]), ("L1", 33, 2, ["CE201-01"]), ("L2", 68, 3, ["CE201-02", "CE201-03"]),
           ("L3", 22, 4, ["CE201-07"]), ("L4", 26, 5, ["CE201-05", "CE201-08", "CE201-15"]),
           ("L6", 32, 7, ["CE201-16", "CE201-17", "CE201-18", "CE201-19"]), ("L7", 4, 8, ["CE201-01"]),
           ("T1", 16, 21, ["CE201-01", "CE201-02"]), ("T2", 16, 22, ["CE201-02"]), ("T3", 17, 23, ["CE201-03"]),
           ("T4", 11, 24, ["CE201-07"]), ("T5", 12, 25, ["CE201-05", "CE201-15"]), ("T6", 8, 26, ["CE201-01"]),
           ("T67", 32, 27, ["CE201-02", "CE201-03", "CE201-11"]),
           ("T8", 20, 28, ["CE201-09", "CE201-10", "CE201-12", "CE201-13"]), ("T9", 8, 29, ["CE201-16", "CE201-18"])]

CON = {}

CON[D["L0"]] = {"code": "CE201", "title": "Concrete 0 · CE3165 course outline", "sections": [
 sec("Scope", (1, 7),
   ("md", "Design philosophy & actions → flexure and shear → cracking and deflection → detailing → structural members "
          "(load path, beams, slabs, columns, bases) → prestressed concrete (Part II, Tan K H). Code: **EC2** with the "
          "Singapore NA; textbook-style design charts and equations."),
 ),
]}

CON[D["L1"]] = {"code": "CE201", "title": "Concrete 1 · Design philosophy, actions & materials", "sections": [
 sec("Limit-state design", (3, 10),
   ("md", "ULS (collapse: flexure, shear, buckling, equilibrium) and SLS (cracking, deflection, vibration, "
          "durability). Design value E_d ≤ R_d using characteristic values × partial factors."),
 ),
 sec("Actions & combinations", (11, 20),
   ("eq", r"E_d = \gamma_G G_k + \gamma_Q Q_k\quad(\gamma_G = 1.35\ \text{unfav},\ 1.0\ \text{fav};\ \gamma_Q = 1.5\ \text{unfav},\ 0\ \text{fav})"),
   ("md", "Use pattern loading on continuous members (max/min load on alternate spans). SLS: characteristic, frequent "
          "(ψ₁) and quasi-permanent (ψ₂) combinations — quasi-permanent for cracking and deflection."),
 ),
 sec("Concrete & steel", (21, 33),
   ("eq", r"f_{cd} = \frac{\alpha_{cc}f_{ck}}{\gamma_c} = \frac{0.85f_{ck}}{1.5} = 0.567f_{ck},\qquad f_{yd} = \frac{f_{yk}}{1.15} = 0.87f_{yk},\qquad E_s = 200\ \text{GPa}"),
   ("md", "Grades C25/30 … (f_ck cylinder/cube); f_ctm = 0.30f_ck^{2/3}; ε_cu2 = 0.0035; B500 steel (yield strain "
          "435/200 000 = 0.00217). Annexes: densities (RC 25 kN/m³), imposed floor loads, bar area tables."),
 ),
]}

CON[D["L2"]] = {"code": "CE201", "title": "Concrete 2 · Flexure (analysis & design) and shear", "sections": [
 sec("Section analysis: elastic uncracked & cracked", (6, 25),
   ("eq", r"\text{cracked: } x = d\left[\sqrt{(\alpha_e\rho)^2 + 2\alpha_e\rho} - \alpha_e\rho\right],\quad I_{cr} = \frac{bx^3}{3} + \alpha_eA_s(d - x)^2,\quad M_{cr} = \frac{f_{ctm}I_u}{h - x_u}"),
   ("md", "Transformed section with α_e = E_s/E_c; uncracked uses (α_e − 1)A_s. Curvature φ = M/(E_cI)."),
 ),
 sec("Collapse (ULS) with the rectangular stress block", (26, 31),
   ("md", "Stress block 0.567f_ck over **0.8x**; strain compatibility ε_cu = 0.0035; steel yields if ε > 0.00217. Find x "
          "from C = T by trial, then take moments."),
 ),
 sec("Design of rectangular sections", (33, 41),
   ("eq", r"K = \frac{M}{bd^2f_{ck}},\quad K' = 0.167\ (x/d \le 0.45),\quad z = d\left[0.5 + \sqrt{0.25 - K/1.134}\right] \le 0.95d,\quad A_s = \frac{M}{0.87f_{yk}z}"),
   ("eq", r"K > K':\quad A'_s = \frac{(K - K')f_{ck}bd^2}{0.87f_{yk}(d - d')},\qquad A_s = \frac{K'f_{ck}bd^2}{0.87f_{yk}z'} + A'_s\quad(d'/x \le 0.38 \text{ so } A'_s \text{ yields})"),
 ),
 sec("Flanged sections", (42, 48),
   ("md", "If 0.8x ≤ h_f, design as rectangular with b = b_eff. Otherwise take the flange outstand force "
          "0.567f_ck(b − b_w)h_f plus a web block; effective flange width b_eff = b_w + Σb_eff,i (≈ l₀/10 each side)."),
 ),
 sec("Shear (variable-strut truss)", (50, 67),
   ("eq", r"V_{Rd,c} = \left[0.12k(100\rho_lf_{ck})^{1/3}\right]b_wd \ge 0.035k^{3/2}f_{ck}^{1/2}b_wd,\quad k = 1 + \sqrt{200/d} \le 2,\ \rho_l \le 0.02"),
   ("eq", r"V_{Rd,max} = \frac{b_wz\nu_1f_{cd}}{\cot\theta + \tan\theta},\ \nu_1 = 0.6\left(1 - \frac{f_{ck}}{250}\right);\qquad \frac{A_{sw}}{s} = \frac{V_{Ed}}{0.87f_{ywk}z\cot\theta},\ \left(\frac{A_{sw}}{s}\right)_{min} = \frac{0.08\sqrt{f_{ck}}b_w}{f_{yk}}"),
   ("md", "1 ≤ cot θ ≤ 2.5 (22°–45°); z ≈ 0.9d; s ≤ 0.75d. Extra tension in the longitudinal steel ΔF = 0.5V cot θ."),
 ),
]}

CON[D["L3"]] = {"code": "CE201", "title": "Concrete 3 · Cracking and deflection (SLS)", "sections": [
 sec("Flexural cracking & minimum steel", (4, 9),
   ("eq", r"A_{s,min} = \frac{k_ck f_{ct,eff}A_{ct}}{\sigma_s}\quad(k_c = 0.4 \text{ bending},\ k \le 1),\qquad A_{s,min} \ge 0.26\frac{f_{ctm}}{f_{yk}}b_td \ge 0.0013b_td"),
 ),
 sec("Crack control without calculation", (10, 15),
   ("md", "Find the steel stress under quasi-permanent load (σ_s ≈ (f_yk/1.15)(G + ψ₂Q)/(1.35G + 1.5Q)·A_s,req/A_s,prov "
          "or from the cracked section), then check **max bar size (Table 7.2N)** or **max bar spacing (Table 7.3N)** "
          "for w_k = 0.3 mm (typical)."),
 ),
 sec("Deflection by span/effective depth", (16, 21),
   ("eq", r"\frac{l}{d} = K\left[11 + 1.5\sqrt{f_{ck}}\frac{\rho_0}{\rho} + 3.2\sqrt{f_{ck}}\left(\frac{\rho_0}{\rho} - 1\right)^{3/2}\right]\ (\rho \le \rho_0),\quad \rho_0 = 10^{-3}\sqrt{f_{ck}}"),
   ("md", "K = 1.0 simply supported, 1.3 end span, 1.5 interior span, 0.4 cantilever; ×310/σ_s (or ×A_s,prov/A_s,req, "
          "≤ 1.5); ×7/l_eff for spans > 7 m; ×0.8 for flanged b/b_w > 3."),
 ),
]}

CON[D["L4"]] = {"code": "CE201", "title": "Concrete 4 · Cover, anchorage and laps", "sections": [
 sec("Cover: durability & fire", (3, 11),
   ("eq", r"c_{nom} = c_{min} + \Delta c_{dev}\ (10\ \text{mm}),\qquad c_{min} = \max\{c_{min,b},\ c_{min,dur},\ 10\ \text{mm}\}"),
   ("md", "c_min,dur from exposure class (XC1 dry … XS sea) and structural class; check minimum dimensions/axis "
          "distance for the fire rating."),
 ),
 sec("Bond & anchorage", (12, 19),
   ("eq", r"f_{bd} = 2.25\eta_1\eta_2f_{ctd},\quad l_{b,rqd} = \frac{\phi}{4}\frac{\sigma_{sd}}{f_{bd}},\quad l_{bd} = \alpha_1\alpha_2\alpha_3\alpha_4\alpha_5\,l_{b,rqd} \ge l_{b,min}"),
   ("md", "η₁ = 1.0 good / 0.7 poor bond; η₂ = 1 for φ ≤ 32. With f_ctd = 0.7(0.30f_ck^{2/3})/1.5 = 0.14f_ck^{2/3}, "
          "**f_bd = 0.315η₁f_ck^{2/3}** (3.0 MPa good / 2.1 MPa poor for C30). l_b,min = max(0.3l_b,rqd, "
          "10φ, 100 mm) in tension. α₁ hooks/bends (0.7 if c_d > 3φ), α₂ cover (1 − 0.15(c_d − φ)/φ, 0.7–1.0)."),
 ),
 sec("Laps", (20, 25),
   ("eq", r"l_0 = \alpha_1\alpha_2\alpha_3\alpha_5\alpha_6\,l_{b,rqd} \ge \max(0.3\alpha_6l_{b,rqd},\ 15\phi,\ 200\ \text{mm}),\quad \alpha_6 = \sqrt{\rho_1/25} \in [1.0, 1.5]"),
 ),
]}

CON[D["L6"]] = {"code": "CE201", "title": "Concrete 6 · Prestressed concrete", "sections": [
 sec("Stress limits & Magnel feasibility", (1, 15),
   ("eq", r"\text{transfer: } \frac{P_0}{A} - \frac{P_0e}{Z_t} + \frac{M_{min}}{Z_t} \ge f_{tt},\quad \frac{P_0}{A} + \frac{P_0e}{Z_b} - \frac{M_{min}}{Z_b} \le f_{ct}\ (\text{similarly at service with }\eta P_0,\ M_{max})"),
   ("md", "Typical limits: compression 0.6f_ck(t) at transfer and 0.6f_ck at service; tension per class (Class 1: none "
          "at service). Plot the four inequalities as lines in 1/P₀ vs e (Magnel diagram) → feasible zone, max e and "
          "min P₀."),
 ),
 sec("Tendon profile, debonding", (16, 18),
   ("md", "Cable zone limits along the span; for pre-tensioned beams debond or deflect strands near supports where "
          "M_min is small."),
 ),
 sec("Deflection & losses", (19, 24),
   ("md", "Short-term camber from prestress (e.g. 5Pe L²/48EI for a parabolic profile) minus load deflection; "
          "long-term with creep. Losses: elastic shortening, relaxation, creep, shrinkage (~15–25 %)."),
 ),
 sec("Ultimate flexure & shear", (25, 31),
   ("md", "ULS moment by strain compatibility with the tendon pre-strain. Shear: uncracked-in-flexure "
          "V_Rd,c = (I b_w/S)√(f_ctd² + α_lσ_cpf_ctd); otherwise the RC expression + 0.15σ_cp b_wd; links as RC."),
 ),
]}

CON[D["L7"]] = {"code": "CE201", "title": "Concrete 7 · Part II (Tan K H) outline", "sections": [
 sec("Part II scope", (1, 4),
   ("md", "Prestressed concrete, structural members and design project. (Structural Members deck, 22 MB on Drive, "
          "isn't imported — Tutorials 6–8 cover load path, beams, slabs, columns and bases.)"),
 ),
]}

# ------------------------------------------------------------------ tutorials
CON[D["T1"]] = {"code": "CE201", "title": "Concrete practice · Tut 1 Loads & cracked/uncracked sections", "sections": [
 sec("1.1 Design loads & patterns (G 25, Q 15 kN/m, two spans)", (2, 6),
   ("ex", "Answers", "Max 1.35G + 1.5Q = **56.25 kN/m**; min 1.0G = **25 kN/m** · V_A max: AB max, BC min · hogging at B: "
          "both spans max · sagging BC: BC max, AB min · reaction B: both max."),
 ),
 sec("1.2 Cracking moment, curvature & steel stress", (7, 16),
   ("ex", "(a) 350 × 600, 3H20 at d 520 / (b) T-section, 2H20 at d 420 (f_ck 30, f_ctm 2.9, E_c 33 GPa)",
    "(a) x 305 → 114 mm, I 6.52 → 1.11 × 10⁹ mm⁴, **M_cr = 64.1 kNm**, f_s 12.7 → 141 MPa, φ 0.30 → 1.74 × 10⁻⁶/mm · "
    "(b) x 198 → 66.7 mm, I 3.42 → 0.53 × 10⁹, **M_cr = 32.8 kNm**, f_s 12.8 → 131 MPa, φ 0.29 → 1.86 × 10⁻⁶/mm. "
    "Cracking increases steel stress ~10× and curvature ~6×."),
 ),
]}

CON[D["T2"]] = {"code": "CE201", "title": "Concrete practice · Tut 2 Design for flexure", "sections": [
 sec("2.1 Non-standard section at collapse", (3, 6),
   ("ex", "Strain compatibility (f_ck 30, f_yk 500)", "Iterate x: 200 → 150 → **x = 167.4 mm** (C = T = 653 kN) → "
          "**M_Rd ≈ 164 kNm**."),
 ),
 sec("2.2 Simply supported 8 m beam, h ≤ 650 mm", (8, 11),
   ("ex", "w = 54.3 kN/m, M = 434.4 kNm, d = 605 mm", "(a) singly reinforced minimum b = M/(0.167f_ckd²) ≈ **237 mm**, "
          "A_s = 2014 mm² · (b) b = 300: K = 0.132, z = 524 mm, **A_s = 1907 mm²** · (c) b = 200: K = 0.198 > K′ → "
          "**A′_s = 280 mm², A_s ≈ 1980 mm²**."),
 ),
 sec("2.3 Inverted L and T sections", (12, 13),
   ("ex", "Answers", "L-section (b 750, d 500, M 500): K 0.089, z 457, 0.8x within flange → **A_s = 2516 mm²** · T-section "
          "web in compression (b 250, d 385, M 350): K 0.315 → doubly reinforced **A′_s ≈ 1174, A_s ≈ 2528 mm²**."),
 ),
 sec("2.4 Flanged beam capacity", (14, 16),
   ("ex", "x/d = 0.45, d = 600", "Sagging M_Rd = **1212 kNm**, A_s = 5470 → 12H25, h = 712.5 mm · hogging (web b 300, "
          "d 650): M′ = 0.167bd²f_ck = **635 kNm**, A_s = 2740 → 6H25."),
 ),
]}

CON[D["T3"]] = {"code": "CE201", "title": "Concrete practice · Tut 3 Design for shear", "sections": [
 sec("3.1 300 × 700 beam, 3H25, f_ck 35", (3, 6),
   ("ex", "Answers", "k = 1.56, ρ = 0.0076 → **V_Rd,c = 108 kN** · V_Rd,max (θ 45°) = **1048 kN** · V_Ed = 100 kN < V_Rd,c → "
          "minimum links (A_sw/s ≥ 0.284) **H8@350** (≤ 0.75d = 484) · higher V_Ed → H16 two-leg @200."),
 ),
 sec("3.2 Links along a simply supported beam", (7, 12),
   ("ex", "w = 66.6 kN/m, H10 U-links", "0.65 m (V 223 kN): **H10@125** · 1.0 m (V 200 kN): **H10@150** · 2.5 m "
          "(V 100 kN, V_Rd,c 116 kN): minimum **H10@350** (≤ 356)."),
 ),
 sec("3.3 Flanged beam, 8 m span, w = 174 kN/m", (13, 17),
   ("ex", "Answers", "V at face 609 kN < V_Rd,max 1469 kN ✓ · V at d from face 474 kN → **H10 two-leg @100** · extra "
          "longitudinal tension ΔF → additional A_s ≈ 545 mm²."),
 ),
]}

CON[D["T4"]] = {"code": "CE201", "title": "Concrete practice · Tut 4 Cracking & deflection", "sections": [
 sec("4.2 8 m simply supported 300 × 600 beam, 3H25", (2, 7),
   ("ex", "Answers", "Uncracked x 333.8, I 6.98 × 10⁹ → **M_cr = 68.5 kNm** · cracked x 239.7, I 4.14 × 10⁹ · SLS "
          "M = 96 kNm → σ_s ≈ **136 MPa** → bar size and spacing within Tables 7.2N/7.3N · A_s,min 185 < 1470 ✓ · "
          "allowable l/d 16.1 > actual 14.3 ✓."),
 ),
 sec("4.3 One-way continuous slab, 100 mm, H10", (8, 11),
   ("ex", "Answers", "F = 46.8 kN/m, M = 0.075FL = 10.5 kNm/m, A_s 371 → **H10@200** (393) · crack spacing limit "
          "≈ 112 mm < 200 → tighten spacing · deflection: allowable ≈ 1.5 × 24.8 = 37.2 < actual 3000/70 = 42.9 ✗ — "
          "more steel alone can't fix it (factor capped at 1.5); deepen the slab."),
 ),
]}

CON[D["T5"]] = {"code": "CE201", "title": "Concrete practice · Tut 5 Anchorage & laps", "sections": [
 sec("5.1 Bent-up H16 bars, poor bond", (3, 5),
   ("ex", "f_ck 30", "f_bd = 0.7 × 0.315 × 30^{2/3} = 2.1 MPa → l_b,rqd = **828 mm** → with α factors **l_bd ≈ 542 mm**."),
 ),
 sec("5.2 Curtailment of bars", (6, 9),
   ("ex", "Good bond, f_bd 3.0 MPa", "l_b,rqd 580 → **l_bd ≈ 553 mm**; find s from A where the remaining bars resist "
          "M plus the shift rule (a_l = z cot θ/2)."),
 ),
 sec("5.3 Anchorage at a simple support", (10, 12),
   ("ex", "w = 51 kN/m, 2H32", "Links H10@200 · force to anchor from V and shift → σ ≈ 131 MPa → required anchorage "
          "≈ 300 mm, governed by the minimum (≈ 10φ = 320 mm) within the support."),
 ),
]}

CON[D["T6"]] = {"code": "CE201", "title": "Concrete practice · Tut 6 Load path & take-down", "sections": [
 sec("Slab → beam → column loads", (1, 8),
   ("md", "Slab 150 mm (25 × 0.15 + finishes + services) → one-way/two-way to beams; add beam self-weight "
          "0.4 × (0.6 − 0.15) × 25 and wall loads 0.225 × h × 19 → line loads (e.g. 16.9 kN/m char., 1.35 × 25.1 = "
          "29.4 kN/m design); column load = tributary reactions (e.g. 41.8 + 11.0 × 6 ≈ 108 kN char.)."),
 ),
]}

CON[D["T67"]] = {"code": "CE201", "title": "Concrete practice · Tut 6–7 Continuous beams & slabs", "sections": [
 sec("6.1 Moment envelope & redistribution", (1, 10),
   ("ex", "G 25, Q 10 kN/m, spans 6 + 7 m", "Max load 48.75, min 33.75 kN/m · elastic M_B = **−206.4 kNm** · 10 % "
          "redistribution → −185.8 kNm (check x/d limit, δ ≥ k₁ + k₂x/d)."),
 ),
 sec("6.2 Design a two-span beam (f_ck 30, f_yk 500)", (11, 24),
   ("ex", "Answers", "Mid-span 324 kNm → **3H25** · interior support −360 kNm → K 0.127 > K′ 0.123 (after "
          "redistribution) → A′_s 2H25, A_s 4H25 · shear: interior 262 kN → **H10@125**, exterior 173 kN → **H10@150**, "
          "elsewhere minimum H10@400 · deflection by l/d ✓."),
 ),
 sec("6.3 Cantilevering roof slab", (25, 32),
   ("ex", "G 3.75 + Q 2 kPa", "w_max 8.06, w_min 5.06 kPa (pattern loading for cantilever + back span); mid-span "
          "M ≈ 13.3 kNm/m; check cover and grade for durability."),
 ),
]}

CON[D["T8"]] = {"code": "CE201", "title": "Concrete practice · Tut 8 Columns & pad bases", "sections": [
 sec("7.1 Classify columns (braced/unbraced, slenderness)", (1, 6),
   ("eq", r"\lambda = \frac{l_0}{i},\qquad \lambda_{lim} = \frac{20ABC}{\sqrt n},\ n = \frac{N_{Ed}}{A_cf_{cd}}"),
   ("md", "l₀ from the relative stiffness k₁, k₂ at the ends (braced 0.5–1.0 l, unbraced ≥ 1.0 l)."),
 ),
 sec("7.2 Short braced column, uniaxial & biaxial", (7, 14),
   ("ex", "400 × 500, f_ck 35", "Use the N–M interaction chart; biaxial (iii): enhanced single-axis moment "
          "M′ = M_z + β(h′/b′)M_y = 350 + 0.743 × … ≈ **581 kNm** → read A_s · (ii) **6H32** (4830 mm²). EC2 check: "
          "(M_z/M_Rdz)^a + (M_y/M_Rdy)^a ≤ 1."),
 ),
 sec("7.3 Pad base 3 × 3 × 0.4 m (N 1800 kN, M 540 kNm)", (15, 20),
   ("ex", "Answers", "Pressure distribution with e = M/N; moment at the column face ≈ **723 kNm** → A_s ≈ 5010 mm² ✓ · "
          "beam shear at d from the face (V_Ed 804 kN vs V_Rd,c) · punching at 2d control perimeter (V_Ed vs "
          "v_Rd,c·u·d, v ≈ 0.58–0.59 MPa)."),
 ),
]}

CON[D["T9"]] = {"code": "CE201", "title": "Concrete practice · Tut 9 Prestressed design", "sections": [
 sec("8.1 Class 1 I-beam, 20 m span — minimum P₀", (1, 4),
   ("md", "A_c = 324 400 mm², I = 38.1 × 10⁹, y_b = 445 mm; limits −1/15 MPa at transfer (f_ck(t) 25), 0/24 MPa at "
          "service (f_ck 40). M_min = 405.5 kNm (self-weight 8.11 kN/m), M_max = 1130.5 kNm (live 10) or 1380.5 kNm "
          "(live 15). Write the four Magnel inequalities and find the minimum P₀ at the maximum feasible e."),
 ),
 sec("8.2 Pre-tensioned beam, 28 m, 15.7 mm strands", (5, 8),
   ("md", "Check stresses at transfer (7 days, self-weight 12.7 kN/m) and at SLS (quasi-permanent 19.7 kN/m), then "
          "deflection and losses; f_pk 1770, f_p0.1k 1495, E_p 195 GPa."),
 ),
]}
