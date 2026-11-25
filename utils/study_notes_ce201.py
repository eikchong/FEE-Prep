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
   ("md", "Design philosophy & actions → flexure and shear → cracking and deflection → detailing → structural "
          "members (load path, beams, slabs, columns, bases) → prestressed concrete (Part II, Tan K H). Code: "
          "**EC2** with the Singapore NA; textbook-style design charts and equations."),
 ),
]}

CON[D["L1"]] = {"code": "CE201", "title": "Concrete 1 · Design philosophy, actions & materials", "sections": [
 sec("Limit-state design", (3, 10),
   ("md", "ULS (collapse: flexure, shear, buckling, equilibrium) and SLS (cracking, deflection, vibration, "
          r"durability). Design value $E_d \le R_d$ using characteristic values × partial factors."),
 ),
 sec("Actions & combinations", (11, 20),
   ("eq", r"E_d = \gamma_G G_k + \gamma_Q Q_k\quad(\gamma_G = 1.35\ \text{unfav},\ 1.0\ \text{fav};\ \gamma_Q = 1.5\ \text{unfav},\ 0\ \text{fav})"),
   ("md", "Use pattern loading on continuous members (max/min load on alternate spans). SLS: characteristic, "
          r"frequent ($\psi_1$) and quasi-permanent ($\psi_2$) combinations — quasi-permanent for cracking and "
          "deflection."),
 ),
 sec("Concrete & steel", (21, 33),
   ("eq", r"f_{cd} = \frac{\alpha_{cc}f_{ck}}{\gamma_c} = \frac{0.85f_{ck}}{1.5} = 0.567f_{ck},\qquad f_{yd} = "
          r"\frac{f_{\mathrm{yk}}}{1.15} = 0.87f_{\mathrm{yk}},\qquad E_s = 200\ \text{GPa}"),
   ("md", r"Grades C25/30 … ($f_{\mathrm{ck}}$ cylinder/cube); $f_{\mathrm{ctm}} = 0.30f_{\mathrm{ck}}^{2/3}$; "
          r"$\varepsilon_{\mathrm{cu2}} = 0.0035$; B500 steel (yield strain $435/200\,000 = 0.00217$). "
          r"Annexes: densities (RC $25\ \mathrm{kN/m^3}$), imposed floor loads, bar area tables."),
 ),
]}

CON[D["L2"]] = {"code": "CE201", "title": "Concrete 2 · Flexure (analysis & design) and shear", "sections": [
 sec("Section analysis: elastic uncracked & cracked", (6, 25),
   ("eq", r"\text{cracked: } x = d\left[\sqrt{(\alpha_e\rho)^2 + 2\alpha_e\rho} - \alpha_e\rho\right],\quad I_{cr} = \frac{bx^3}{3} + \alpha_eA_s(d - x)^2,\quad M_{cr} = \frac{f_{ctm}I_u}{h - x_u}"),
   ("md", r"Transformed section with $\alpha_e = E_s/E_c$; uncracked uses $(\alpha_e - 1)A_s$. Curvature $\phi "
          "= M/(E_cI)$."),
 ),
 sec("Collapse (ULS) with the rectangular stress block", (26, 31),
   ("md", r"Stress block $0.567f_{\mathrm{ck}}$ over **0.8x**; strain compatibility $\varepsilon_{\mathrm{cu}} "
          r"= 0.0035$; steel yields if $\varepsilon > 0.00217$. Find x from $C = T$ by trial, then take "
          "moments."),
 ),
 sec("Design of rectangular sections", (33, 41),
   ("eq", r"K = \frac{M}{bd^2f_{ck}},\quad K' = 0.167\ (x/d \le 0.45),\quad z = d\left[0.5 + \sqrt{0.25 - "
          r"K/1.134}\right] \le 0.95d,\quad A_s = \frac{M}{0.87f_{\mathrm{yk}}z}"),
   ("eq", r"K > K':\quad A'_s = \frac{(K - K')f_{ck}bd^2}{0.87f_{\mathrm{yk}}(d - d')},\qquad A_s = "
          r"\frac{K'f_{ck}bd^2}{0.87f_{\mathrm{yk}}z'} + A'_s\quad(d'/x \le 0.38 \text{ so } A'_s \text{ "
          "yields})"),
 ),
 sec("Flanged sections", (42, 48),
   ("md", r"If $0.8x \le h_f$, design as rectangular with $b = b_{\mathrm{eff}}$. Otherwise take the flange "
          r"outstand force $0.567f_{\mathrm{ck}}(b - b_w)h_f$ plus a web block; effective flange width "
          r"$b_{\mathrm{eff}} = b_w + \sum b_{\mathrm{eff,i}}$ (≈ $l_0/10$ each side)."),
 ),
 sec("Shear (variable-strut truss)", (50, 67),
   ("eq", r"V_{Rd,c} = \left[0.12k(100\rho_lf_{ck})^{1/3}\right]b_wd \ge 0.035k^{3/2}f_{ck}^{1/2}b_wd,\quad k = 1 + \sqrt{200/d} \le 2,\ \rho_l \le 0.02"),
   ("eq", r"V_{Rd,max} = \frac{b_wz\nu_1f_{cd}}{\cot\theta + \tan\theta},\ \nu_1 = 0.6\left(1 - "
          r"\frac{f_{ck}}{250}\right);\qquad \frac{A_{sw}}{s} = \frac{V_{Ed}}{0.87f_{ywk}z\cot\theta},\ "
          r"\left(\frac{A_{sw}}{s}\right)_{min} = \frac{0.08\sqrt{f_{ck}}b_w}{f_{\mathrm{yk}}}"),
   ("md", r"$1 \le \cot\theta \le 2.5$ (22°–45°); $z \approx 0.9d$; $s \le 0.75d$. Extra tension in the "
          r"longitudinal steel $\Delta F = 0.5V \cot\theta$."),
 ),
]}

CON[D["L3"]] = {"code": "CE201", "title": "Concrete 3 · Cracking and deflection (SLS)", "sections": [
 sec("Flexural cracking & minimum steel", (4, 9),
   ("eq", r"A_{s,min} = \frac{k_ck f_{ct,eff}A_{ct}}{\sigma_s}\quad(k_c = 0.4 \text{ bending},\ k \le "
          r"1),\qquad A_{s,min} \ge 0.26\frac{f_{ctm}}{f_{\mathrm{yk}}}b_td \ge 0.0013b_td"),
 ),
 sec("Crack control without calculation", (10, 15),
   ("md", r"Find the steel stress under quasi-permanent load ($\sigma_s \approx (f_{\mathrm{yk}}/1.15)(G + "
          r"\psi_2Q)/(1.35G + 1.5Q) \cdot A_{\mathrm{s,req}}/A_{\mathrm{s,prov}}$ or from the cracked "
          "section), then check **max bar size (Table 7.2N)** or **max bar spacing (Table 7.3N)** for $w_k = "
          r"0.3\ \mathrm{mm}$ (typical)."),
 ),
 sec("Deflection by span/effective depth", (16, 21),
   ("eq", r"\frac{l}{d} = K\left[11 + 1.5\sqrt{f_{ck}}\frac{\rho_0}{\rho} + 3.2\sqrt{f_{ck}}\left(\frac{\rho_0}{\rho} - 1\right)^{3/2}\right]\ (\rho \le \rho_0),\quad \rho_0 = 10^{-3}\sqrt{f_{ck}}"),
   ("md", r"$K = 1.0$ simply supported, 1.3 end span, 1.5 interior span, 0.4 cantilever; ×$310/\sigma_s$ (or "
          r"×$A_{\mathrm{s,prov}}/A_{\mathrm{s,req}}$, ≤ 1.5); ×$7/l_{\mathrm{eff}}$ for spans > 7 m; ×0.8 for "
          "flanged $b/b_w > 3$."),
 ),
]}

CON[D["L4"]] = {"code": "CE201", "title": "Concrete 4 · Cover, anchorage and laps", "sections": [
 sec("Cover: durability & fire", (3, 11),
   ("eq", r"c_{nom} = c_{min} + \Delta c_{dev}\ (10\ \text{mm}),\qquad c_{min} = \max\{c_{min,b},\ c_{min,dur},\ 10\ \text{mm}\}"),
   ("md", r"$c_{\mathrm{min,dur}}$ from exposure class (XC1 dry … XS sea) and structural class; check minimum "
          "dimensions/axis distance for the fire rating."),
 ),
 sec("Bond & anchorage", (12, 19),
   ("eq", r"f_{bd} = 2.25\eta_1\eta_2f_{ctd},\quad l_{b,rqd} = \frac{\phi}{4}\frac{\sigma_{sd}}{f_{bd}},\quad l_{bd} = \alpha_1\alpha_2\alpha_3\alpha_4\alpha_5\,l_{b,rqd} \ge l_{b,min}"),
   ("md", r"$\eta_1 = 1.0$ good / 0.7 poor bond; $\eta_2 = 1$ for $\phi \le 32$. With $f_{\mathrm{ctd}} = "
          r"0.7(0.30f_{\mathrm{ck}}^{2/3})/1.5 = 0.14f_{\mathrm{ck}}^{2/3}$, $\boldsymbol{f_{\mathrm{bd}} = "
          r"0.315\eta_1f_{\mathrm{ck}}^{2/3}}$ (3.0 MPa good / 2.1 MPa poor for C30). $l_{\mathrm{b,min}} = "
          r"\max(0.3l_{\mathrm{b,rqd}},\ 10\phi,\ 100\ \mathrm{mm})$ in tension. $\alpha_1$ hooks/bends (0.7 "
          r"if $c_d > 3\phi$), $\alpha_2$ cover ($1 - 0.15(c_d - \phi)/\phi$, 0.7–1.0)."),
 ),
 sec("Laps", (20, 25),
   ("eq", r"l_0 = \alpha_1\alpha_2\alpha_3\alpha_5\alpha_6\,l_{b,rqd} \ge \max(0.3\alpha_6l_{b,rqd},\ 15\phi,\ 200\ \text{mm}),\quad \alpha_6 = \sqrt{\rho_1/25} \in [1.0, 1.5]"),
 ),
]}

CON[D["L6"]] = {"code": "CE201", "title": "Concrete 6 · Prestressed concrete", "sections": [
 sec("Stress limits & Magnel feasibility", (1, 15),
   ("eq", r"\text{transfer: } \frac{P_0}{A} - \frac{P_0e}{Z_t} + \frac{M_{min}}{Z_t} \ge f_{tt},\quad \frac{P_0}{A} + \frac{P_0e}{Z_b} - \frac{M_{min}}{Z_b} \le f_{ct}\ (\text{similarly at service with }\eta P_0,\ M_{max})"),
   ("md", r"Typical limits: compression $0.6f_{\mathrm{ck}}(t)$ at transfer and $0.6f_{\mathrm{ck}}$ at "
          "service; tension per class (Class 1: none at service). Plot the four inequalities as lines in "
          "$1/P_0$ vs e (Magnel diagram) → feasible zone, max e and min $P_0$."),
 ),
 sec("Tendon profile, debonding", (16, 18),
   ("md", "Cable zone limits along the span; for pre-tensioned beams debond or deflect strands near supports "
          r"where $M_{\mathrm{min}}$ is small."),
 ),
 sec("Deflection & losses", (19, 24),
   ("md", "Short-term camber from prestress (e.g. $5PeL^2/(48EI)$ for a parabolic profile) minus load "
          "deflection; long-term with creep. Losses: elastic shortening, relaxation, creep, shrinkage (~15–25 "
          "%)."),
 ),
 sec("Ultimate flexure & shear", (25, 31),
   ("md", "ULS moment by strain compatibility with the tendon pre-strain. Shear: uncracked-in-flexure "
          r"$V_{\mathrm{Rd,c}} = (I b_w/S)\sqrt{f_{\mathrm{ctd}}^2 + "
          r"\alpha_l\sigma_{\mathrm{cp}}f_{\mathrm{ctd}}}$; otherwise the RC expression + "
          r"$0.15\sigma_{\mathrm{cp}} b_wd$; links as RC."),
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
   ("ex", "Answers", r"Max $1.35G + 1.5Q = \boldsymbol{56.25\ \mathrm{kN/m}}$; min $1.0G = \boldsymbol{25\ "
                     r"\mathrm{kN/m}}$ · $V_A$ max: AB max, BC min · hogging at B: both spans max · sagging "
                     "BC: BC max, AB min · reaction B: both max."),
 ),
 sec("1.2 Cracking moment, curvature & steel stress", (7, 16),
   ("ex", r"(a) 350 × 600, 3H20 at d 520 / (b) T-section, 2H20 at d 420 ($f_{\mathrm{ck}}$ 30, "
          r"$f_{\mathrm{ctm}}$ 2.9, $E_c$ 33 GPa)",
    r"(a) x 305 → 114 mm, I 6.52 → $1.11 \times 10^9\ \mathrm{mm^4}$, $\boldsymbol{M_{\mathrm{cr}} = 64.1\ "
    r"\mathrm{kNm}}$, $f_s$ 12.7 → 141 MPa, $\phi$ 0.30 → $1.74 \times 10^{-6}\ \mathrm{mm^{-1}}$ · (b) x 198 "
    r"→ 66.7 mm, I 3.42 → $0.53 \times 10^9$, $\boldsymbol{M_{\mathrm{cr}} = 32.8\ \mathrm{kNm}}$, $f_s$ 12.8 "
    r"→ 131 MPa, $\phi$ 0.29 → $1.86 \times 10^{-6}\ \mathrm{mm^{-1}}$. Cracking increases steel stress ~10× "
    "and curvature ~6×."),
 ),
]}

CON[D["T2"]] = {"code": "CE201", "title": "Concrete practice · Tut 2 Design for flexure", "sections": [
 sec("2.1 Non-standard section at collapse", (3, 6),
   ("ex", r"Strain compatibility ($f_{\mathrm{ck}}$ 30, $f_{\mathrm{yk}}$ 500)", "Iterate x: 200 → 150 → "
                                                                        r"$\boldsymbol{x = 167.4\ "
                                                                        r"\mathrm{mm}}$ ($C = T = 653\ "
                                                                        r"\mathrm{kN}$) → "
                                                                        r"$\boldsymbol{M_{\mathrm{Rd}} \approx "
                                                                        r"164\ \mathrm{kNm}}$."),
 ),
 sec(r"2.2 Simply supported 8 m beam, $h \le 650\ \mathrm{mm}$", (8, 11),
   ("ex", r"$w = 54.3\ \mathrm{kN/m}$, $M = 434.4\ \mathrm{kNm}$, $d = 605\ \mathrm{mm}$", "(a) singly "
                                                                                           "reinforced "
                                                                                           "minimum $b = "
                                                                                           r"M/(0.167f_{\mathrm{ck}}d^2) "
                                                                                           r"\approx "
                                                                                           r"\boldsymbol{237\ "
                                                                                           r"\mathrm{mm}}$, "
                                                                                           r"$A_s = 2014\ "
                                                                                           r"\mathrm{mm^2}$ · "
                                                                                           "(b) $b = 300$: $K "
                                                                                           "= 0.132$, $z = "
                                                                                           r"524\ "
                                                                                           r"\mathrm{mm}$, "
                                                                                           r"$\boldsymbol{A_s "
                                                                                           r"= 1907\ "
                                                                                           r"\mathrm{mm^2}}$ · "
                                                                                           "(c) $b = 200$: $K "
                                                                                           "= 0.198 > K'$ → "
                                                                                           r"**$A'_s = 280\ "
                                                                                           r"\mathrm{mm^2}$, "
                                                                                           r"$A_s \approx "
                                                                                           r"1980\ "
                                                                                           r"\mathrm{mm^2}$**."),
 ),
 sec("2.3 Inverted L and T sections", (12, 13),
   ("ex", "Answers", r"L-section (b 750, d 500, M 500): K 0.089, z 457, 0.8x within flange → $\boldsymbol{A_s "
                     r"= 2516\ \mathrm{mm^2}}$ · T-section web in compression (b 250, d 385, M 350): K 0.315 → "
                     r"doubly reinforced **$A'_s \approx 1174$, $A_s \approx 2528\ \mathrm{mm^2}$**."),
 ),
 sec("2.4 Flanged beam capacity", (14, 16),
   ("ex", "$x/d = 0.45$, $d = 600$", r"Sagging $M_{\mathrm{Rd}} = \boldsymbol{1212\ \mathrm{kNm}}$, $A_s = 5470$ → "
                                 r"12H25, $h = 712.5\ \mathrm{mm}$ · hogging (web b 300, d 650): $M' = "
                                 r"0.167bd^2f_{\mathrm{ck}} = \boldsymbol{635\ \mathrm{kNm}}$, $A_s = 2740$ → "
                                 "6H25."),
 ),
]}

CON[D["T3"]] = {"code": "CE201", "title": "Concrete practice · Tut 3 Design for shear", "sections": [
 sec(r"3.1 300 × 700 beam, 3H25, $f_{\mathrm{ck}}$ 35", (3, 6),
   ("ex", "Answers", r"$k = 1.56$, $\rho = 0.0076$ → $\boldsymbol{V_{\mathrm{Rd,c}} = 108\ \mathrm{kN}}$ · "
                     r"$V_{\mathrm{Rd,max}}$ ($\theta$ 45°) = **1048 kN** · $V_{\mathrm{Ed}} = 100\ "
                     r"\mathrm{kN} < V_{\mathrm{Rd,c}}$ → minimum links ($A_{\mathrm{sw}}/s \ge 0.284$) "
                     r"**H8@350** ($\le 0.75d = 484$) · higher $V_{\mathrm{Ed}}$ → H16 two-leg @200."),
 ),
 sec("3.2 Links along a simply supported beam", (7, 12),
   ("ex", r"$w = 66.6\ \mathrm{kN/m}$, H10 U-links", "0.65 m (V 223 kN): **H10@125** · 1.0 m (V 200 kN): **H10@150** · 2.5 "
                                        r"m (V 100 kN, $V_{\mathrm{Rd,c}}$ 116 kN): minimum **H10@350** ($\le "
                                        "356$)."),
 ),
 sec(r"3.3 Flanged beam, 8 m span, $w = 174\ \mathrm{kN/m}$", (13, 17),
   ("ex", "Answers", r"V at face $609\ \mathrm{kN} < V_{\mathrm{Rd,max}}$ 1469 kN ✓ · V at d from face 474 kN "
                     r"→ **H10 two-leg @100** · extra longitudinal tension $\Delta F$ → additional $A_s "
                     r"\approx 545\ \mathrm{mm^2}$."),
 ),
]}

CON[D["T4"]] = {"code": "CE201", "title": "Concrete practice · Tut 4 Cracking & deflection", "sections": [
 sec("4.2 8 m simply supported 300 × 600 beam, 3H25", (2, 7),
   ("ex", "Answers", r"Uncracked x 333.8, I $6.98 \times 10^9$ → $\boldsymbol{M_{\mathrm{cr}} = 68.5\ "
                     r"\mathrm{kNm}}$ · cracked x 239.7, I $4.14 \times 10^9$ · SLS $M = 96\ \mathrm{kNm}$ → "
                     r"$\sigma_s \approx \boldsymbol{136\ \mathrm{MPa}}$ → bar size and spacing within Tables "
                     r"7.2N/7.3N · $A_{\mathrm{s,min}} = 185 < 1470$ ✓ · allowable l/d 16.1 > actual 14.3 ✓."),
 ),
 sec("4.3 One-way continuous slab, 100 mm, H10", (8, 11),
   ("ex", "Answers", r"$F = 46.8\ \mathrm{kN/m}$, $M = 0.075FL = 10.5\ \mathrm{kNm/m}$, $A_s$ 371 → "
                     r"**H10@200** (393) · crack spacing limit ≈ $112\ \mathrm{mm} < 200$ → tighten spacing · "
                     r"deflection: allowable ≈ $1.5 \times 24.8 = 37.2$ < actual $3000/70 = 42.9$ ✗ — more "
                     "steel alone can't fix it (factor capped at 1.5); deepen the slab."),
 ),
]}

CON[D["T5"]] = {"code": "CE201", "title": "Concrete practice · Tut 5 Anchorage & laps", "sections": [
 sec("5.1 Bent-up H16 bars, poor bond", (3, 5),
   ("ex", r"$f_{\mathrm{ck}}$ 30", r"$f_{\mathrm{bd}} = 0.7 \times 0.315 \times 30^{2/3} = 2.1\ \mathrm{MPa}$ "
                                   r"→ $l_{\mathrm{b,rqd}} = \boldsymbol{828\ \mathrm{mm}}$ → with $\alpha$ "
                                   r"factors $\boldsymbol{l_{\mathrm{bd}} \approx 542\ \mathrm{mm}}$."),
 ),
 sec("5.2 Curtailment of bars", (6, 9),
   ("ex", r"Good bond, $f_{\mathrm{bd}}$ 3.0 MPa", r"$l_{\mathrm{b,rqd}}$ 580 → $\boldsymbol{l_{\mathrm{bd}} \approx 553\ "
                                     r"\mathrm{mm}}$; find s from A where the remaining bars resist M plus the "
                                     r"shift rule ($a_l = z \cot\theta/2$)."),
 ),
 sec("5.3 Anchorage at a simple support", (10, 12),
   ("ex", r"$w = 51\ \mathrm{kN/m}$, 2H32", r"Links H10@200 · force to anchor from V and shift → $\sigma \approx 131\ "
                               r"\mathrm{MPa}$ → required anchorage ≈ 300 mm, governed by the minimum "
                               r"($\approx 10\phi = 320\ \mathrm{mm}$) within the support."),
 ),
]}

CON[D["T6"]] = {"code": "CE201", "title": "Concrete practice · Tut 6 Load path & take-down", "sections": [
 sec("Slab → beam → column loads", (1, 8),
   ("md", "Slab 150 mm (25 × 0.15 + finishes + services) → one-way/two-way to beams; add beam self-weight 0.4 "
          r"× (0.6 − 0.15) × 25 and wall loads 0.225 × h × 19 → line loads (e.g. 16.9 kN/m char., $1.35 \times "
          r"25.1 = 29.4\ \mathrm{kN/m}$ design); column load = tributary reactions (e.g. $41.8 + 11.0 \times 6 "
          r"\approx 108\ \mathrm{kN}$ char.)."),
 ),
]}

CON[D["T67"]] = {"code": "CE201", "title": "Concrete practice · Tut 6–7 Continuous beams & slabs", "sections": [
 sec("6.1 Moment envelope & redistribution", (1, 10),
   ("ex", "G 25, Q 10 kN/m, spans 6 + 7 m", "Max load 48.75, min 33.75 kN/m · elastic $M_B = "
                                            r"\boldsymbol{-206.4\ \mathrm{kNm}}$ · 10 % redistribution → "
                                            r"−185.8 kNm (check x/d limit, $\delta \ge k_1 + k_2x/d$)."),
 ),
 sec(r"6.2 Design a two-span beam ($f_{\mathrm{ck}}$ 30, $f_{\mathrm{yk}}$ 500)", (11, 24),
   ("ex", "Answers", "Mid-span 324 kNm → **3H25** · interior support −360 kNm → K $0.127 > K'$ 0.123 (after "
                     "redistribution) → $A'_s$ 2H25, $A_s$ 4H25 · shear: interior 262 kN → **H10@125**, "
                     "exterior 173 kN → **H10@150**, elsewhere minimum H10@400 · deflection by l/d ✓."),
 ),
 sec("6.3 Cantilevering roof slab", (25, 32),
   ("ex", "G 3.75 + Q 2 kPa", r"$w_{\mathrm{max}}$ 8.06, $w_{\mathrm{min}}$ 5.06 kPa (pattern loading for "
                              r"cantilever + back span); mid-span $M \approx 13.3\ \mathrm{kNm/m}$; check "
                              "cover and grade for durability."),
 ),
]}

CON[D["T8"]] = {"code": "CE201", "title": "Concrete practice · Tut 8 Columns & pad bases", "sections": [
 sec("7.1 Classify columns (braced/unbraced, slenderness)", (1, 6),
   ("eq", r"\lambda = \frac{l_0}{i},\qquad \lambda_{lim} = \frac{20ABC}{\sqrt n},\ n = \frac{N_{Ed}}{A_cf_{cd}}"),
   ("md", "$l_0$ from the relative stiffness $k_1$, $k_2$ at the ends (braced 0.5–1.0 l, unbraced ≥ 1.0 l)."),
 ),
 sec("7.2 Short braced column, uniaxial & biaxial", (7, 14),
   ("ex", r"400 × 500, $f_{\mathrm{ck}}$ 35", "Use the N–M interaction chart; biaxial (iii): enhanced single-axis moment "
                                r"$M' = M_z + \beta(h'/b')M_y = 350 + 0.743 \times \ldots \approx "
                                r"\boldsymbol{581\ \mathrm{kNm}}$ → read $A_s$ · (ii) **6H32** ($4830\ "
                                r"\mathrm{mm^2}$). EC2 check: $(M_z/M_{\mathrm{Rdz}})^a + "
                                r"(M_y/M_{\mathrm{Rdy}})^a \le 1$."),
 ),
 sec("7.3 Pad base 3 × 3 × 0.4 m (N 1800 kN, M 540 kNm)", (15, 20),
   ("ex", "Answers", "Pressure distribution with $e = M/N$; moment at the column face ≈ **723 kNm** → $A_s "
                     r"\approx 5010\ \mathrm{mm^2}$ ✓ · beam shear at d from the face ($V_{\mathrm{Ed}}$ 804 "
                     r"kN vs $V_{\mathrm{Rd,c}}$) · punching at 2d control perimeter ($V_{\mathrm{Ed}}$ vs "
                     r"$v_{\mathrm{Rd,c}} \cdot u \cdot d$, $v \approx 0.58\text{–}0.59\ \mathrm{MPa}$)."),
 ),
]}

CON[D["T9"]] = {"code": "CE201", "title": "Concrete practice · Tut 9 Prestressed design", "sections": [
 sec("8.1 Class 1 I-beam, 20 m span — minimum $P_0$", (1, 4),
   ("md", r"$A_c = 324\,400\ \mathrm{mm^2}$, $I = 38.1 \times 10^9$, $y_b = 445\ \mathrm{mm}$; limits −1/15 "
          r"MPa at transfer ($f_{\mathrm{ck}}(t) = 25$), 0/24 MPa at service ($f_{\mathrm{ck}}$ 40). "
          r"$M_{\mathrm{min}} = 405.5\ \mathrm{kNm}$ (self-weight 8.11 kN/m), $M_{\mathrm{max}} = 1130.5\ "
          r"\mathrm{kNm}$ (live 10) or 1380.5 kNm (live 15). Write the four Magnel inequalities and find the "
          "minimum $P_0$ at the maximum feasible e."),
 ),
 sec("8.2 Pre-tensioned beam, 28 m, 15.7 mm strands", (5, 8),
   ("md", "Check stresses at transfer (7 days, self-weight 12.7 kN/m) and at SLS (quasi-permanent 19.7 kN/m), "
          r"then deflection and losses; $f_{\mathrm{pk}}$ 1770, $f_{\mathrm{p0.1k}}$ 1495, $E_p$ 195 GPa."),
 ),
]}
