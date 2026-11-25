"""CE202 Structural Steel Design — CE3166 Structural Steel Design and System (Ang K K, Pang S D, Liew J Y R).

EC3 (SS EN 1993-1-1/-1-5/-1-8 + Singapore NA).
"""


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


S = "CE202/CE3166/"
T = S + "tutorials/"
D = {
    "L0": S + "0 General Information.pdf", "L1": S + "1 Introduction.pdf",
    "L2": S + "2 Local Buckling and Section Classification.pdf", "L3": S + "3 Compression Members.pdf",
    "L4": S + "4 Tension Members.pdf", "L5": S + "5 Cross Section Moment Resistance.pdf",
    "L6": S + "6 Restrained Beams.pdf", "L7": S + "7 Unrestrained Beams.pdf",
    "L8a": S + "8 Beam-Columns Set 1.pdf", "L8b": S + "8 Beam-Columns Set 2.pdf",
    "L9": S + "9 Plate Girders.pdf", "L10": S + "10b Welded Connections Set 2.pdf",
    "L10a": S + "10a Welded Connections Set 1.pdf", "L11": S + "11 Bolted Connections.pdf",
    "T1": T + "Tut 1 questions.pdf", "T2": T + "Tut 2 section classification soln.pdf",
    "T3": T + "Tut 3 questions.pdf", "T4": T + "Tut 4 questions.pdf", "T5": T + "Tut 5 questions.pdf",
    "T6": T + "Tut 6 soln.pdf", "T6b": T + "Tut 6 part2 soln.pdf", "T7": T + "Tut 7 plate girder soln.pdf",
    "T8w": T + "Tut 8 welds soln.pdf", "T8b": T + "Tut 8 bolts soln.pdf",
}
TEXT_ONLY = set()
OUTLINE = [("L0", 11, 1, ["CE202-01"]), ("L1", 109, 2, ["CE202-01"]), ("L2", 74, 3, ["CE202-02"]),
           ("L3", 108, 4, ["CE202-08"]), ("L4", 54, 5, ["CE202-07"]), ("L5", 27, 6, ["CE202-02", "CE202-03"]),
           ("L6", 53, 7, ["CE202-03"]), ("L7", 64, 8, ["CE202-06"]), ("L8a", 29, 9, ["CE202-09"]),
           ("L8b", 38, 10, ["CE202-09"]), ("L9", 68, 11, ["CE202-04", "CE202-05"]),
           ("L10a", 17, 12, ["CE202-10"]), ("L10", 24, 13, ["CE202-10"]), ("L11", 79, 14, ["CE202-10"]),
           ("T1", 6, 21, ["CE202-01"]), ("T2", 41, 22, ["CE202-02"]), ("T3", 4, 23, ["CE202-08"]),
           ("T4", 2, 24, ["CE202-07"]), ("T5", 3, 25, ["CE202-03", "CE202-06"]), ("T6", 31, 26, ["CE202-09"]),
           ("T6b", 86, 27, ["CE202-09"]), ("T7", 74, 28, ["CE202-04", "CE202-05"]), ("T8w", 43, 29, ["CE202-10"]),
           ("T8b", 50, 30, ["CE202-10"])]

STL = {}

STL[D["L0"]] = {"code": "CE202", "title": "Steel 0 · CE3166 course information", "sections": [
 sec("Scope & references", (1, 11),
   ("md", "Part I (Ang K K): load combinations, section classification, compression, tension, restrained and "
          "unrestrained beams. Part II (Pang S D): beam-columns, multi-storey frames, plate girders, bolted and welded "
          "connections. Bring **SCI P363 (Blue Book) section & design tables** to the exam."),
 ),
]}

STL[D["L1"]] = {"code": "CE202", "title": "Steel 1 · Eurocodes, limit states & load combinations", "sections": [
 sec("Eurocode family & EC3 parts", (12, 14),
   ("md", "EN 1990 basis, EN 1991 actions, EN 1993-1-1 general rules, -1-5 plated elements, -1-8 joints. Principles "
          "(P) must be obeyed; application rules may be replaced if shown to satisfy the principles; NA sets NDPs."),
 ),
 sec("Material properties", (31, 37),
   ("md", r"$E = 210\ \mathrm{GPa}$, $G = 81\ \mathrm{GPa}$, $\nu = 0.3$, $\alpha = 12 \times 10^{-6}\ "
          r"/^\circ\mathrm{C}$. $f_y$ drops with thickness: S275 → 275 ($t \le 16$), 265 ($\le 40$), 255 ($\le "
          r"63$); S355 → 355, 345, 335; $f_u$ 410 (S275), 470 (S355). Ductility: $f_u/f_y \ge 1.10$, "
          r"$\varepsilon_f \ge 15\,\%$, $\varepsilon_u \ge 15\varepsilon_y$. $\gamma_{\mathrm{M0}} = "
          r"\gamma_{\mathrm{M1}} = 1.0$, $\gamma_{\mathrm{M2}} = 1.1$ (Singapore NA)."),
 ),
 sec("Limit states & ULS combinations", (59, 109),
   ("eq", r"\sum\gamma_GG_k + \gamma_{Q,1}Q_{k,1} + \sum_{i>1}\gamma_{Q,i}\psi_{0,i}Q_{k,i}\quad(6.10)\qquad \gamma_G = 1.35/1.0,\ \gamma_Q = 1.5/0"),
   ("md", r"$\psi_0 = 0.7$ for imposed (1.0 storage), 0.5 for wind (Singapore NA). Frames: 1.35G + 1.5Q + "
          r"0.75W + EHF and 1.35G + 1.5W + 1.05Q + EHF. $\boldsymbol{\mathrm{EHF} = \phi N_{\mathrm{Ed}}}$, "
          r"$\phi = (1/200)\alpha_h\alpha_m$, $\alpha_h = 2/\sqrt{h}$ ($\tfrac23 \le \alpha_h \le 1$), "
          r"$\alpha_m = \sqrt{0.5(1 + 1/m)}$; $(0.75W + \mathrm{EHF}) \ge 0.015G$."),
 ),
]}

STL[D["L2"]] = {"code": "CE202", "title": "Steel 2 · Local buckling & section classification", "sections": [
 sec("Why classify", (1, 19),
   ("md", "Plate elements buckle locally before yield if c/t is large. Class 1 plastic hinge with rotation; "
          r"Class 2 $M_{\mathrm{pl}}$ but limited rotation; Class 3 $M_{\mathrm{el}}$ only; Class 4 local "
          r"buckling before yield → effective section. $M_{\mathrm{c,Rd}} = W_{\mathrm{pl}} f_y$ (1, 2), "
          r"$W_{\mathrm{el}} f_y$ (3), $W_{\mathrm{eff}} f_y$ (4)."),
 ),
 sec(r"c/t limits (Table 5.2), $\varepsilon = \sqrt{235/f_y}$", (20, 29),
   ("md", r"**Internal (web) in bending** $72\varepsilon / 83\varepsilon / 124\varepsilon$ · **internal in "
          r"compression** $33\varepsilon / 38\varepsilon / 42\varepsilon$ · bending + compression: Class 1 "
          r"$396\varepsilon/(13\alpha - 1)$, Class 2 $456\varepsilon/(13\alpha - 1)$ ($\alpha > 0.5$); Class 3 "
          r"$42\varepsilon/(0.67 + 0.33\psi)$ ($\psi > -1$) · **outstand flange in compression** $9\varepsilon "
          r"/ 10\varepsilon / 14\varepsilon$ · angles $h/t \le 15\varepsilon$, $(b + h)/2t \le "
          r"11.5\varepsilon$ · CHS $d/t \le 50\varepsilon^2 / 70\varepsilon^2 / 90\varepsilon^2$. $\varepsilon "
          "= 1.0$, 0.92, 0.81 for S235, S275, S355."),
   ("eq", r"\alpha = \frac12 + \frac{N_{Ed}}{2ct_wf_y} \le 1,\qquad \psi = \frac{2N_{Ed}}{Af_y} - 1"),
   ("md", "The section takes the worst class of its elements. Web limits are higher than flange limits because the "
          "web is supported on both edges and usually only partly compressed."),
 ),
 sec("Class 4 effective widths (EN 1993-1-5)", (30, 40),
   ("eq", r"\bar\lambda_p = \frac{\bar b/t}{28.4\varepsilon\sqrt{k_\sigma}},\quad \rho_{int} = \frac{\bar\lambda_p - 0.055(3 + \psi)}{\bar\lambda_p^2},\quad \rho_{out} = \frac{\bar\lambda_p - 0.188}{\bar\lambda_p^2}\ (\le 1)"),
   ("md", r"$k_{\sigma} = 4.0$ internal uniform compression (23.9 pure bending), 0.43 outstand uniform. $\rho "
          r"= 1$ if $\bar{\lambda}_p \le 0.673$ (internal, $\psi = 1$) or ≤ 0.748 (outstand)."),
 ),
 sec("Class 3 web + Class 1/2 flange; design tables", (41, 46),
   ("md", r"May be treated as effective Class 2 using $20\varepsilon t_w$ of web next to the flange and next "
          r"to the PNA. SCI tables give the $n = N_{\mathrm{Ed}}/N_{\mathrm{pl,Rd}}$ limits for Class 2/3 "
          "under combined loading."),
 ),
 sec("Worked examples", (47, 74),
   ("ex", "UB 457×152×52 S275", r"Bending only: Class 1 (tables say Class 2) · + 800 kN: $\alpha$ 0.97, web "
                                "Class 3 ($n = 0.44 > 0.169$) · + 1500 kN: web Class 4 ($n = 0.82 > 0.586$)."),
   ("ex", "Welded I (400×12 flanges, 424×10 web) S355 in compression", r"Flange c/t $15.6 > 14\varepsilon$ → "
                                                                       r"Class 4, $\rho_f = 0.795$; web "
                                                                       r"$\rho_w = 1.0$ → $A_{\mathrm{eff}} = "
                                                                       r"11\,756\ \mathrm{mm^2}$ → "
                                                                       r"$N_{\mathrm{c,Rd}} = "
                                                                       r"\boldsymbol{4173\ \mathrm{kN}}$."),
 ),
]}

STL[D["L3"]] = {"code": "CE202", "title": "Steel 3 · Compression members (flexural buckling)", "sections": [
 sec("Cross-section resistance", (5, 10),
   ("eq", r"N_{c,Rd} = \frac{Af_y}{\gamma_{M0}}\ (\text{Class 1–3}),\qquad \frac{A_{eff}f_y}{\gamma_{M0}}\ (\text{Class 4})"),
 ),
 sec("Euler buckling & effective length", (11, 20),
   ("eq", r"N_{cr} = \frac{\pi^2EI}{L_{cr}^2},\qquad \bar\lambda = \sqrt{\frac{Af_y}{N_{cr}}} = \frac{L_{cr}}{i\lambda_1},\quad \lambda_1 = \pi\sqrt{E/f_y} = 93.9\varepsilon"),
   ("md", r"$L_{\mathrm{cr}}$ between inflection points: pinned–pinned 1.0L, fixed–fixed 0.7L (practical), "
          "fixed–pinned 0.85L, cantilever 2.0L; sway modes longer. Intermediate restraints shorten "
          r"$L_{\mathrm{cr}}$ about one axis only."),
 ),
 sec("Buckling resistance & curves", (21, 33),
   ("eq", r"N_{b,Rd} = \frac{\chi Af_y}{\gamma_{M1}},\quad \chi = \frac{1}{\Phi + \sqrt{\Phi^2 - \bar\lambda^2}} \le 1,\quad \Phi = 0.5\left[1 + \alpha(\bar\lambda - 0.2) + \bar\lambda^2\right]"),
   ("md", r"$\alpha$: $a_0$ 0.13, a 0.21, b 0.34, c 0.49, d 0.76. Rolled I (S275/S355): $h/b > 1.2$, $t_f \le "
          r"40$ → **y–y a, z–z b**; $h/b \le 1.2$, $t_f \le 100$ → **y–y b, z–z c**. Hot-finished hollow → a; "
          "cold-formed → c; welded I → b (y), c (z); angles, T, channels → b. Ignore buckling if "
          r"$\bar{\lambda} \le 0.2$."),
 ),
 sec("Worked examples", (34, 72),
   ("ex", r"CM-1: 6 m pinned UC, $N_{\mathrm{Ed}} = 2580\ \mathrm{kN}$, S275", r"UC 356×368×129: $\bar{\lambda}_z = 0.719$, $\chi_z = "
                                                       r"0.712$ → $\boldsymbol{N_{\mathrm{b,Rd}} = 3094\ "
                                                       r"\mathrm{kN}}$ ✓."),
   ("ex", "CM-2: same with mid-height z-restraint", r"UC 254×254×107: $\bar{\lambda}_y$ 0.598 ($\chi$ 0.900), "
                                                    r"$\bar{\lambda}_z$ 0.514 ($\chi$ 0.835) → **3009 kN** ✓."),
   ("ex", r"CM-3: UB 533×210×92 S275, 5 m, $N_{\mathrm{Ed}}$ 1155 kN", r"Web Class 4 ($\rho$ 0.84, $A_{\mathrm{eff}}$ 10 "
                                                         r"930) → $\bar{\lambda}_z$ 1.232, $\chi$ 0.461 → "
                                                         "**1386 kN** ✓."),
   ("ex", "CM-6: 244.5×10 CHS S355, 4 m, 2400 kN", r"$\chi$ 0.854 → 2230 kN ✗ → use 244.5×12.5 (2830 kN)."),
   ("ex", "CM-8: UB 406×140×39 S355 Class 4", r"$A_{\mathrm{eff}} = 4217\ \mathrm{mm^2}$ → "
                                              r"$N_{\mathrm{b,z,Rd}} = \boldsymbol{846\ \mathrm{kN}} < 1005\ "
                                              r"\mathrm{kN}$ ✗."),
 ),
]}

STL[D["L4"]] = {"code": "CE202", "title": "Steel 4 · Tension members", "sections": [
 sec("Gross & net area; staggered holes", (6, 14),
   ("eq", r"A_{net} = A - nd_0t + \sum\frac{s^2t}{4p}\quad(\text{zig-zag path; take the minimum})"),
   ("md", r"$d_0 = d + 2\ \mathrm{mm}$ (M12–M24), d + 3 mm (≥ M27). For angles measure p along the centreline "
          "of thickness."),
 ),
 sec("Tension resistance", (15, 19),
   ("eq", r"N_{t,Rd} = \min\left(N_{pl,Rd} = \frac{Af_y}{\gamma_{M0}},\ N_{u,Rd} = \frac{0.9A_{net}f_u}{\gamma_{M2}}\right),\qquad \gamma_{M2} = 1.1"),
   ("ex", "200 × 25 flat, 6 M20 non-staggered (S275)", r"$N_{\mathrm{pl}} = 1325$, $N_u = 0.9 \times 3900 "
                                                       r"\times 410/1.1 = \boldsymbol{1308\ \mathrm{kN}}$ "
                                                       "(governs)."),
 ),
 sec("Angles connected by one leg (EN 1993-1-8 3.10.3)", (29, 42),
   ("eq", r"N_{u,Rd} = \frac{\beta A_{net}f_u}{\gamma_{M2}},\quad \beta_2 = 0.4\text{–}0.7,\ \beta_3 = 0.5\text{–}0.7\ (\text{interpolate on } p_1/d_0 \text{ between } 2.5 \text{ and } 5);\quad \text{1 bolt: } A = 2(e_2 - 0.5d_0)t"),
   ("md", r"Welded: equal angle or unequal by the long leg → $A_{\mathrm{eff}} = A$; unequal by the short leg "
          "→ gross area of an equal angle with the short leg size."),
   ("ex", "125×75×10 S355, 3 M20 at 100 mm", r"Long leg: $\beta_3 = 0.664$ → **479 kN**; short leg: "
                                             r"$A_{\mathrm{eff}}$ 1400 → **335 kN**."),
 ),
 sec("Slenderness & design", (43, 54),
   ("md", r"$\lambda = L/i_{\mathrm{min}} \le 300$ (main), ≤ 400 (secondary). Example TM-5: 554 kN tie → "
          "bolted 150×90×12 (596 kN) but welded only 100×75×10 (589 kN)."),
 ),
]}

STL[D["L5"]] = {"code": "CE202", "title": "Steel 5 · Cross-section moment resistance", "sections": [
 sec("Elastic–plastic bending", (1, 17),
   ("eq", r"M_{el} = f_yW_{el},\ W_{el} = \frac{I}{y_{max}};\qquad M_{pl} = f_yW_{pl},\ W_{pl} = A_cy_c + A_ty_t\ (\text{about the equal-area axis})"),
   ("md", r"Rectangle: $W_{\mathrm{el}} = bh^2/6$, $W_{\mathrm{pl}} = bh^2/4$ → shape factor 1.5; I-sections ≈ "
          "1.12–1.15."),
 ),
 sec("Examples & classes", (18, 27),
   ("md", "Only Class 1 sections may form plastic hinges for plastic global analysis; Class 2 reach "
          r"$M_{\mathrm{pl}}$ in elastic analysis."),
 ),
]}

STL[D["L6"]] = {"code": "CE202", "title": "Steel 6 · Laterally restrained beams", "sections": [
 sec("Shear resistance", (8, 13),
   ("eq", r"V_{pl,Rd} = \frac{A_v(f_y/\sqrt3)}{\gamma_{M0}},\quad A_v = A - 2bt_f + (t_w + 2r)t_f \ge \eta h_wt_w\ (\text{rolled I});\quad \frac{h_w}{t_w} > 72\frac{\varepsilon}{\eta} \Rightarrow \text{shear buckling}"),
 ),
 sec("Moment resistance & high shear", (14, 19),
   ("eq", r"M_{c,Rd} = \frac{W_{pl}f_y}{\gamma_{M0}};\qquad V_{Ed} > 0.5V_{pl,Rd}:\ \rho = \left(\frac{2V_{Ed}}{V_{pl,Rd}} - 1\right)^2,\ M_{y,V,Rd} = \left(W_{pl} - \frac{\rho A_w^2}{4t_w}\right)\frac{f_y}{\gamma_{M0}}"),
 ),
 sec("Serviceability", (20, 26),
   ("md", "Deflection under unfactored variable load: L/360 (brittle finishes), L/200 general, cantilevers "
          "L/180. Use standard formulas ($5wL^4/(384EI)$, $PL^3/(48EI)$, …)."),
 ),
 sec("Worked examples RB-1 to RB-4", (27, 53),
   ("md", r"Steps: design actions → trial section from $W_{\mathrm{pl,req}} = M_{\mathrm{Ed}}/f_y$ → classify "
          r"→ V check (and shear buckling) → M check (with $\rho$ if high shear) → deflection."),
 ),
]}

STL[D["L7"]] = {"code": "CE202", "title": "Steel 7 · Unrestrained beams (lateral–torsional buckling)", "sections": [
 sec("When LTB matters", (3, 14),
   ("md", "Slender unrestrained beams in major-axis bending buckle by lateral deflection + twist. Ignore LTB "
          r"for CHS/SHS, full lateral restraint, minor-axis bending, or $\bar{\lambda}_{\mathrm{LT}} \le 0.4$ "
          "(rolled) / 0.2 (welded)."),
 ),
 sec("Buckling resistance", (15, 24),
   ("eq", r"M_{b,Rd} = \chi_{LT}\frac{W_yf_y}{\gamma_{M1}},\quad \bar\lambda_{LT} = \sqrt{\frac{W_yf_y}{M_{cr}}},\quad \chi_{LT} = \frac{1}{\Phi_{LT} + \sqrt{\Phi_{LT}^2 - \beta\bar\lambda_{LT}^2}}"),
   ("md", r"General (6.3.2.2): $\bar{\lambda}_{\mathrm{LT,0}} = 0.2$, $\beta = 1$; rolled I curves a ($h/b \le "
          "2$) / b (> 2); welded c / d. Rolled & equivalent welded (6.3.2.3, less conservative): "
          r"$\bar{\lambda}_{\mathrm{LT,0}} = 0.4$, $\beta = 0.75$, curves b ($h/b \le 2$) / c, "
          r"$\chi_{\mathrm{LT}} \le 1/\bar{\lambda}_{\mathrm{LT}}^2$."),
 ),
 sec("Elastic critical moment", (25, 34),
   ("eq", r"M_{cr} = C_1\frac{\pi^2EI_z}{L_{cr}^2}\sqrt{\frac{I_w}{I_z} + \frac{L_{cr}^2GI_T}{\pi^2EI_z}}"),
   ("eq", r"C_1 = 1.77 - 1.04\psi + 0.27\psi^2 \le 2.60\ (\text{linear moment},\ \psi = M_2/M_1);\quad \text{UDL } 1.127,\ \text{central point } 1.348"),
   ("md", r"$L_{\mathrm{cr}} = kL$ (k from end restraint); **destabilising load** (on the top flange, free to "
          r"move with it) → $L_{\mathrm{cr}} = 1.2kL$; cantilevers use separate k tables with $C_1 = 1$."),
 ),
 sec("Design procedure & examples", (35, 64),
   ("ex", "URB-1: 9 m beam restrained at load points, S275", r"UB 457×191×82: segment BC (3 m, $\psi$ 0.82, "
                                                             r"$C_1$ 1.10) → $M_{\mathrm{cr}}$ 1182 kNm, "
                                                             r"$\bar{\lambda}_{\mathrm{LT}}$ 0.653, $\chi$ "
                                                             r"0.810 → $\boldsymbol{M_{\mathrm{b,Rd}} = 408\ "
                                                             r"\mathrm{kNm}} > 396.5$ ✓; deflection $15\ "
                                                             r"\mathrm{mm} < L/360$."),
   ("ex", "URB-2: 10 m unrestrained, UB 533×210×101 S355", r"$M_{\mathrm{cr}}$ 258 kNm, "
                                                           r"$\bar{\lambda}_{\mathrm{LT}}$ 1.87, $\chi$ 0.277 "
                                                           r"→ $M_{\mathrm{b,Rd}} = 249$ ≪ 816 kNm ✗ → UB "
                                                           "533×312×182 (965 kNm)."),
 ),
]}

STL[D["L8a"]] = {"code": "CE202", "title": "Steel 8a · Beam-columns: cross-section resistance", "sections": [
 sec("Shear, then moment in presence of axial force", (1, 17),
   ("eq", r"\text{I/H, } n = \frac{N_{Ed}}{N_{pl,Rd}},\ a = \frac{A - 2bt_f}{A} \le 0.5:\quad M_{N,y,Rd} = M_{pl,y,Rd}\frac{1-n}{1-0.5a} \le M_{pl,y,Rd}"),
   ("eq", r"\text{Biaxial: } \left(\frac{M_{y,Ed}}{M_{N,y,Rd}}\right)^{2} + \left(\frac{M_{z,Ed}}{M_{N,z,Rd}}\right)^{5n \ge 1} \le 1;\qquad \text{Class 3: } \frac{N_{Ed}}{Af_y} + \frac{M_{y}}{W_{el,y}f_y} + \frac{M_z}{W_{el,z}f_y} \le 1"),
   ("md", r"No reduction about y if $N_{\mathrm{Ed}} \le 0.25N_{\mathrm{pl,Rd}}$ and ≤ $0.5h_wt_wf_y$. Reduce "
          r"$f_y$ in the web if $V_{\mathrm{Ed}} > 0.5V_{\mathrm{pl,Rd}}$."),
 ),
 sec("Example BC-1", (18, 29),
   ("md", r"Classify under the actual N (n-limits), check V, compute $M_{\mathrm{N,Rd}}$ and the interaction "
          "at the critical sections (ends and points of maximum moment)."),
 ),
]}

STL[D["L8b"]] = {"code": "CE202", "title": "Steel 8b · Beam-columns: member buckling (6.61/6.62)", "sections": [
 sec("Interaction equations", (2, 5),
   ("eq", r"\frac{N_{Ed}}{\chi_yN_{Rk}/\gamma_{M1}} + k_{yy}\frac{M_{y,Ed}}{\chi_{LT}M_{y,Rk}/\gamma_{M1}} + k_{yz}\frac{M_{z,Ed}}{M_{z,Rk}/\gamma_{M1}} \le 1"),
   ("eq", r"\frac{N_{Ed}}{\chi_zN_{Rk}/\gamma_{M1}} + k_{zy}\frac{M_{y,Ed}}{\chi_{LT}M_{y,Rk}/\gamma_{M1}} + k_{zz}\frac{M_{z,Ed}}{M_{z,Rk}/\gamma_{M1}} \le 1"),
 ),
 sec("Interaction factors (Annex A / Annex B)", (6, 19),
   ("md", r"Annex B (simpler): Class 1–2 I-sections: $k_{yy} = C_{\mathrm{my}}[1 + (\bar{\lambda}_y - 0.2)n_y] "
          r"\le C_{\mathrm{my}}(1 + 0.8n_y)$ with $n_y = "
          r"N_{\mathrm{Ed}}/(\chi_yN_{\mathrm{Rk}}/\gamma_{\mathrm{M1}})$; $k_{yz} = 0.6k_{zz}$; $k_{zy}$ from "
          "Table B.2 for torsionally flexible members; $C_m$ from Table B.3 (linear moment $C_m = 0.6 + "
          r"0.4\psi \ge 0.4$)."),
 ),
 sec("Example BC-2 & tips", (20, 38),
   ("md", r"Find $N_{\mathrm{b,y,Rd}}$, $N_{\mathrm{b,z,Rd}}$, $M_{\mathrm{b,Rd}}$ ($C_1$ for the segment), "
          "$C_m$ factors and k, then both equations for every segment between restraints. Axial tension "
          "relieves LTB (use the beam checks)."),
 ),
]}

STL[D["L9"]] = {"code": "CE202", "title": "Steel 9 · Plate girders (EN 1993-1-5)", "sections": [
 sec("Initial sizing & moment (flanges carry M)", (1, 17),
   ("md", r"$h \approx L/12\text{–}L/20$ (0.05–0.10L simple), $b \approx 0.25\text{–}0.35h$, $t_f \approx "
          r"0.04\text{–}0.08b$, $t_w \approx 0.005\text{–}0.010d$. Flange at least Class 3 ($c_f/t_f \le "
          r"14\varepsilon$)."),
   ("eq", r"M_{f,Rd} = \frac{A_ff_{yf}(d + t_f)}{\gamma_{M0}} \ge M_{Ed}"),
 ),
 sec("Web: flange-induced buckling & shear buckling", (18, 31),
   ("eq", r"\frac{d}{t_w} \le k\frac{E}{f_{yf}}\sqrt{\frac{A_w}{A_{fc}}}\ (k = 0.55 \text{ elastic});\qquad \frac{d}{t_w} > \frac{72\varepsilon}{\eta}\ \text{or}\ \frac{31\varepsilon\sqrt{k_\tau}}{\eta} \Rightarrow \text{shear buckling}"),
   ("eq", r"V_{b,Rd} = \chi_w\frac{f_{yw}dt_w}{\sqrt3\gamma_{M1}} + \frac{b_ft_f^2f_{yf}}{c\gamma_{M1}}\left[1 - \left(\frac{M_{Ed}}{M_{f,Rd}}\right)^2\right] \le \frac{\eta f_{yw}dt_w}{\sqrt3\gamma_{M1}}"),
   ("md", r"$\bar{\lambda}_w = d/(86.4t_w\varepsilon)$ (end stiffeners only) or "
          r"$d/(37.4t_w\varepsilon\sqrt{k_{\tau}})$; $k_{\tau} = 5.34 + 4(d/a)^2$ ($a/d \ge 1$). Non-rigid end "
          r"post: $\chi_w = \eta$ ($\bar{\lambda}_w < 0.83/\eta$), $0.83/\bar{\lambda}_w$ otherwise. $c = "
          r"a[0.25 + 1.6b_ft_f^2f_{\mathrm{yf}}/(dt_w^2f_{\mathrm{yw}})]$."),
   ("ex", "PG-1: 25 m girder, M 14 028 kNm, V 1910 kN, S275", "700×40 flanges, 1920×13 web: "
                                                              r"$M_{\mathrm{f,Rd}}$ **14 543 kNm** ✓ · no "
                                                              r"intermediate stiffeners: $V_{\mathrm{b,Rd}} = "
                                                              r"1782\ \mathrm{kN}$ ✗ · stiffeners at 3 m: "
                                                              r"$\chi_w$ 0.51 → **2034 kN** ✓."),
 ),
 sec("Transverse forces (patch loading)", (32, 41),
   ("eq", r"F_{Rd} = \frac{\chi_Ff_{yw}l_yt_w}{\gamma_{M1}},\quad l_y = s_s + 2t_f\left(1 + \sqrt{\frac{f_{yf}b_f}{f_{yw}t_w} + m_2}\right),\quad \chi_F = \frac{0.5}{\bar\lambda_F} \le 1,\ k_F = 6 + 2(d/a)^2"),
   ("ex", "PG-2: 2000 kN point load on 700×40 / 1920×13 girder", r"$s_s$ 79.5, $l_y$ 951 mm, $\bar{\lambda}_F$ "
                                                                 r"1.62 → $F_{\mathrm{Rd}} = \boldsymbol{1050\ "
                                                                 r"\mathrm{kN}} < 2000\ \mathrm{kN}$ → bearing "
                                                                 "stiffener required."),
 ),
 sec("Stiffeners: slenderness, stiffness, bearing, buckling", (42, 68),
   ("md", r"Effective section = stiffener + $15\varepsilon t_w$ of web each side. $b_s/t_s \le "
          r"1/(5.3\sqrt{f_y/E})$ (≈ 12 for S275). Intermediate: $I_{\mathrm{st}} \ge 0.75dt_w^3$ ($a/d \ge "
          r"\sqrt{2}$) or $1.5d^3t_w^3/a^2$. Load-bearing: bearing on net area (minus cope holes) and buckling "
          r"with curve c, $L_{\mathrm{cr}} = d$; axial force = $F_{\mathrm{Ed}}$ + tension-field force "
          r"$V_{\mathrm{Ed}} - f_{\mathrm{ywd}}t_w/(\sqrt{3}\bar{\lambda}_w^2\gamma_{\mathrm{M1}})$."),
   ("ex", "PG-5: two 165×15 stiffeners at the 2000 kN load", r"Slenderness $11 < 12$ ✓, I ✓, bearing $2373 \ge "
                                                             r"2000$ ✓, but $N_{\mathrm{Ed}} = 2000 + 776 = "
                                                             r"2776 > N_{\mathrm{b,Rd}} = 2630\ \mathrm{kN}$ ✗ "
                                                             "→ enlarge."),
 ),
]}

STL[D["L10a"]] = {"code": "CE202", "title": "Steel 10a · Welding: processes, weldability, weld types", "sections": [
 sec("Welding basics", (1, 17),
   ("md", "Fusion welding with a heat-affected zone (HAZ). Weldability via carbon equivalent CEV; risks: hydrogen "
          "cracking (preheat, low-hydrogen electrodes), brittle fracture, lamellar tearing. Joint types: butt, tee, "
          "lap, corner; welds: full/partial-penetration butt welds (full penetration = parent strength) and fillet welds."),
 ),
]}

STL[D["L10"]] = {"code": "CE202", "title": "Steel 10b · Fillet weld design (EN 1993-1-8 4.5)", "sections": [
 sec("Detailing rules", (1, 6),
   ("md", r"Throat $a = 0.7s$ (leg s) for equal legs at 90°; effective length $\ge \max(30\ \mathrm{mm},\ "
          "6a)$; return ends; angles 60°–120°."),
 ),
 sec("Simplified method", (7, 12),
   ("eq", r"F_{w,Rd} = f_{vw,d}\,a,\qquad f_{vw,d} = \frac{f_u/\sqrt3}{\beta_w\gamma_{M2}}\quad(\beta_w = 0.85\ \text{S275},\ 0.90\ \text{S355})"),
   ("md", r"Use the weaker connected part's $f_u$; resultant force per unit length $F_{\mathrm{w,Ed}} \le "
          r"F_{\mathrm{w,Rd}}$."),
 ),
 sec("Directional method", (13, 19),
   ("eq", r"\sqrt{\sigma_\perp^2 + 3(\tau_\perp^2 + \tau_\parallel^2)} \le \frac{f_u}{\beta_w\gamma_{M2}},\qquad \sigma_\perp \le \frac{0.9f_u}{\gamma_{M2}}"),
   ("md", "Transverse welds are ~1.22× stronger than longitudinal (K factor in SCI tables)."),
 ),
 sec("Weld groups under moment & shear", (20, 24),
   ("md", "Treat the weld as a line: flanges take the moment ($F = M/(h - t_f)$), web welds take the shear; "
          "or use polar/elastic properties of the weld group ($I_w$, $J_w$) and combine stresses vectorially."),
 ),
]}

STL[D["L11"]] = {"code": "CE202", "title": "Steel 11 · Bolted connections (EN 1993-1-8 3.6)", "sections": [
 sec("Bolt categories, spacing & edge distances", (1, 24),
   ("md", "Classes 4.6, 8.8, 10.9; Category A bearing, B/C slip-resistant (preloaded), D/E tension. Minimum "
          "$e_1 = 1.2d_0$, $e_2 = 1.2d_0$, $p_1 = 2.2d_0$, $p_2 = 2.4d_0$; maximum 14t or 200 mm in "
          "compression."),
 ),
 sec("Shear, bearing, tension", (25, 50),
   ("eq", r"F_{v,Rd} = \frac{\alpha_vf_{ub}A}{\gamma_{M2}}\ (\alpha_v = 0.6 \text{ for 4.6/8.8 through threads, } 0.5 \text{ for 10.9}),\qquad F_{b,Rd} = \frac{k_1\alpha_bf_udt}{\gamma_{M2}}"),
   ("eq", r"\alpha_b = \min\left(\frac{e_1}{3d_0},\ \frac{p_1}{3d_0} - \frac14,\ \frac{f_{ub}}{f_u},\ 1\right),\quad k_1 = \min\left(2.8\frac{e_2}{d_0} - 1.7,\ 1.4\frac{p_2}{d_0} - 1.7,\ 2.5\right),\quad F_{t,Rd} = \frac{0.9f_{ub}A_s}{\gamma_{M2}}"),
   ("eq", r"\text{combined: } \frac{F_{v,Ed}}{F_{v,Rd}} + \frac{F_{t,Ed}}{1.4F_{t,Rd}} \le 1;\qquad B_{p,Rd} = \frac{0.6\pi d_mt_pf_u}{\gamma_{M2}}\ (\text{punching})"),
 ),
 sec("Block tearing, long joints, preloaded bolts", (51, 79),
   ("eq", r"V_{eff,1,Rd} = \frac{f_uA_{nt}}{\gamma_{M2}} + \frac{f_yA_{nv}}{\sqrt3\gamma_{M0}}\ (\text{concentric});\qquad F_{s,Rd} = \frac{k_sn\mu}{\gamma_{M3}}F_{p,C},\ F_{p,C} = 0.7f_{ub}A_s"),
   ("md", r"Long joints ($L_j > 15d$) reduce shear resistance by $\beta_{\mathrm{Lf}}$. Eccentric bolt groups: "
          r"elastic method with $F = V/n + M r/\sum r^2$."),
 ),
]}

# ------------------------------------------------------------------ tutorials
STL[D["T1"]] = {"code": "CE202", "title": "Steel practice · Tut 1 Load combinations (4-storey braced frame)", "sections": [
 sec("Questions", (1, 6),
   ("md", "Floors: G 3.5 + 0.5 kPa, Q 3.0 (office, cat. B) + 1.5 (moveable partitions); roof G 0.75 + 0.25, Q "
          "0.4 (cat. H); wind 925 kN on the long face. Derive ULS combinations (imposed leading vs wind "
          r"leading, $\psi_0$ 0.7 / 0.5), EHF, and member forces for beams, columns and bracing. No official "
          "solution file — check with the lecture's combination rules."),
 ),
]}

STL[D["T2"]] = {"code": "CE202", "title": "Steel practice · Tut 2 Section classification", "sections": [
 sec("Q1 Welded box 450×330 (10 mm plates, S275)", (1, 20),
   ("ex", "Answers", r"(a) compression: webs c/t $43 > 42\varepsilon = 38.6$ → **Class 4** · internal flanges "
                     r"33 → Class 2 · outstands $8.0 < 9\varepsilon$ → Class 1 · (b) major-axis bending: webs "
                     r"Class 1 → overall **Class 2** · (c) minor-axis bending: see worked $\alpha$, $\psi$ · "
                     r"(d) $N = 2000\ \mathrm{kN}$ + $M_y$: web Class 3 → overall **Class 3**."),
 ),
 sec("Q2 Column 254×254×73 S355 under $N + M_y$", (21, 41),
   ("ex", "Answer", r"Compute $n = N_{\mathrm{Ed}}/N_{\mathrm{pl,Rd}}$ from the Tut 1 ULS force and compare "
                    "with the SCI n-limits → flange Class 2, web Class 1 → overall **Class 2**."),
 ),
]}

STL[D["T3"]] = {"code": "CE202", "title": "Steel practice · Tut 3 Compression members", "sections": [
 sec("Q1 Roof truss top chord (SHS, S355)", (1, 3),
   ("ex", "Partial solution", r"$w = 1.35 \times 0.90 + 1.5 \times 0.40 = 1.815\ \mathrm{kPa}$ × 6 m purlin "
                              r"spacing = 10.89 kN/m → $R_A = \tfrac12 (2 \times 10.89 \times 7/\cos 15^\circ) "
                              r"= \boldsymbol{78.9\ \mathrm{kN}}$; then chord forces by joints and select an "
                              "SHS."),
 ),
 sec("Q2 12 m column with different restraints per axis (S275)", (4, 4),
   ("md", r"$N_{\mathrm{Ed}} = 1.35 \times 650 + 1.5 \times 900 = 2228\ \mathrm{kN}$. Segments: z–z restrained "
          r"at 3.5 m ($L_{\mathrm{cr,z}} = 8.5\ \mathrm{m}$ governs the upper part), y–y restrained at 6 m "
          r"($L_{\mathrm{cr,y}} = 6\ \mathrm{m}$). Check each segment about its own axis and pick a UC."),
 ),
]}

STL[D["T4"]] = {"code": "CE202", "title": "Steel practice · Tut 4 Tension members", "sections": [
 sec("Q1 20 mm plate with M20 bolts (S275)", (1, 2),
   ("ex", "Partial solution", r"$A = 7200\ \mathrm{mm^2}$, $f_y$ 265, $f_u$ 410 · $N_{\mathrm{pl}} = "
                              r"\boldsymbol{1908\ \mathrm{kN}}$ · net paths $5880 / 5778 / 5675\ "
                              r"\mathrm{mm^2}$ → $N_u = 0.9A_{\mathrm{net,min}} \times 410/1.1$; the sheet's "
                              r"answer $\boldsymbol{N_{\mathrm{t,Rd}} = 1880\ \mathrm{kN}}$ implies "
                              r"$A_{\mathrm{net,min}} \approx 5600\ \mathrm{mm^2}$, so check every zig-zag "
                              "path (most holes, fewest diagonals)."),
 ),
 sec("Q2 Spliced angle, 420 kN, three M20 on one leg", (1, 2),
   ("md", r"Use $\beta_3$ ($p_1 = 90\ \mathrm{mm}$, $d_0 = 22$ → $p_1/d_0 = 4.1$ → $\beta_3 \approx 0.63$) on "
          r"$A_{\mathrm{net}}$ of the connected angle; check the 160 × 15 splice plate for $N_{\mathrm{pl}}$ "
          "and $N_u$."),
 ),
]}

STL[D["T5"]] = {"code": "CE202", "title": "Steel practice · Tut 5 Beams (restrained vs unrestrained)", "sections": [
 sec("10 m primary beam with two secondary-beam loads (S275)", (1, 3),
   ("ex", "Partial solution", r"Point loads $1.35 \times 70 + 1.5 \times 70 = 200\ \mathrm{kN}$ at 2.5 m and "
                              r"5.5 m → reactions 240/160 kN, $M_{\mathrm{max}} = \boldsymbol{720\ "
                              r"\mathrm{kNm}}$ · fully restrained: **610×229×101 UB** adequate for V and M · "
                              "restrained only at the secondary beams: check LTB per segment ($C_1$ from "
                              r"$\psi$) and choose a heavier/wider section with $M_{\mathrm{b,Rd}} \ge 720\ "
                              r"\mathrm{kNm}$; check deflection L/360."),
 ),
]}

STL[D["T6"]] = {"code": "CE202", "title": "Steel practice · Tut 6 Beam-columns: cross-section checks", "sections": [
 sec("Theory recap", (1, 11),
   ("md", "Plastic interaction for Class 1–2, linear elastic for Class 3 (conservative for 1–2)."),
 ),
 sec("Q1 Portal column, N 160 kN, M 530 kNm (S355)", (12, 17),
   ("ex", "Answer", "n below the Class 2 limit → **UKB 533×165×66** satisfies cross-section strength."),
 ),
 sec("Q2 UC 254×254×73 S275 chord (800 kN + 200 kN mid-span + 100 kNm end moments)", (18, 31),
   ("ex", "Answer", "Class 1; shear adequate; at the critical section the first trial is **inadequate**, the "
                    r"revised check is adequate (reduce $M_{\mathrm{N,Rd}}$ for n and check the "
                    "biaxial/uniaxial interaction)."),
 ),
]}

STL[D["T6b"]] = {"code": "CE202", "title": "Steel practice · Tut 6 part 2 Beam-columns: member buckling", "sections": [
 sec("Q1 Portal column with restraint 1.6 m below the top", (1, 52),
   ("ex", "Answer", r"**UKB 533×210×82 (S355)**: top segment interaction $0.49 / 0.74 \le 1$, bottom segment "
                    r"$0.39 / 0.64 \le 1$ → adequate against buckling."),
 ),
 sec("Q2 UC 254×254×73 chord", (53, 86),
   ("ex", "Answer", "Class 1; buckling resistance **adequate** (Annex B k-factors, $C_m$ from the moment "
                    "shape; axial tension case discussed)."),
 ),
]}

STL[D["T7"]] = {"code": "CE202", "title": "Steel practice · Tut 7 Plate girder (12 m, S275)", "sections": [
 sec("(a)–(b) Actions and the largest UB", (1, 20),
   ("ex", "Answers", "UB 1016×305×487: Class 1, shear adequate, **moment inadequate** → plate girder needed."),
 ),
 sec(r"(c)–(d) Flange sizing ($h \le 1.8\ \mathrm{m}$, $b/t_f \approx 15$)", (21, 34),
   ("ex", "Answer", r"Try $\boldsymbol{t_f = 30\ \mathrm{mm}}$ (450 × 30 flanges, 10 mm web) → moment "
                    "adequate; compare self-weight with the UB."),
 ),
 sec("(e)–(f) Stiffener positions & shear buckling", (35, 47),
   ("ex", "Answers", r"$V_{\mathrm{max}} = 1500\ \mathrm{kN} < V_{\mathrm{pl,Rd}}$ ✓ · panel AB (a/d 0.86): "
                     r"$1500 < V_{\mathrm{bw,Rd}}$ ✓ · panel BC (a/d 1.15): $1425 > V_{\mathrm{b,Rd}}$ ✗ → add "
                     "a stiffener · panel CD (a/d 1.44): 525 ✓."),
 ),
 sec("(g)–(i) Patch loading & stiffeners", (48, 74),
   ("ex", "Answers", r"Unstiffened web under 800 kN: $\boldsymbol{F_{\mathrm{Rd}} < 800\ \mathrm{kN}}$ → "
                     "stiffener needed · 2 × 120×10 load-bearing stiffeners: stiffness ✓, bearing ✓ ($800 < "
                     r"F_{\mathrm{bc}}$), buckling ✓ · 2 × 80×10 intermediate stiffeners checked for "
                     r"$I_{\mathrm{st}}$."),
 ),
]}

STL[D["T8w"]] = {"code": "CE202", "title": "Steel practice · Tut 8 Welds (extended end plate, 8 mm fillets)", "sections": [
 sec("Weld group: F 300 kN, M 200 kNm on 457×191×67 UB", (1, 43),
   ("ex", "Answers", "Flange welds carry $M/(h - t_f)$ as tension/compression, web welds the shear. First "
                     "layouts: weld capacity **inadequate** by the simplified method; the less conservative "
                     "directional method shows it is **adequate** — compare both."),
 ),
]}

STL[D["T8b"]] = {"code": "CE202", "title": "Steel practice · Tut 8 Bolts (M20 8.8 end plate)", "sections": [
 sec("Bolt tension from M and combined check", (1, 50),
   ("ex", "Answers", "Rotation about the compression flange, tension ∝ distance → top-row bolt force from "
                     r"$M/\sum(y^2) \cdot y_{\mathrm{max}}$ · **tension resistance adequate** but **combined "
                     r"shear + tension inadequate** for the top bolts ($F_v/F_{\mathrm{v,Rd}} + "
                     r"F_t/(1.4F_{\mathrm{t,Rd}}) > 1$) · bearing $30\ \mathrm{kN} < F_{\mathrm{b,Rd}}$ ✓ → "
                     "add bolts or use 10.9."),
 ),
]}
