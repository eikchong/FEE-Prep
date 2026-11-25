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

# Tutorial pages (questions as q blocks) live in utils/study_notes_ce201q.py.
