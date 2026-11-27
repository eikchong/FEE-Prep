"""PE-prep course notes from the shared Drive folder (Preparatory Course for PE Fundamentals of Engineering).

- CE201 Reinforced & Prestressed Concrete (Tan K H) and "Introduction to Beam Design": scanned, read by OCR.
  Both follow BS 8110 / CP65. The FE paper is on Eurocode 2, so these pages are for concepts, procedures and
  the topics the CE3165 notes don't cover; where BS 8110 and EC2 differ the notes say so.
- CE206 Wastewater (Prof Ong Say Leong): over 10 MB on Drive, so notes were written from Drive's text only and
  the slide numbers are approximate (the PDF isn't stored locally).
Worked examples are q blocks with the course's own solutions.
"""
from utils.qblock import q


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


RC = "CE201/CE201_Reinforced_Prestressed_Concrete_Structures.pdf"
BD = "CE201/CE201_Introduction_to_Beam_Design.pdf"
WW = "CE206/CE206_Wastewater_Flowrates_Sewers_Treatment.pdf"

BS = ("tip", r"BS 8110 vs EC2 for the exam: BS uses cube strength $f_{\mathrm{cu}}$ (EC2 cylinder $f_{\mathrm{ck}} "
             r"\approx 0.8f_{\mathrm{cu}}$), loads $1.4G + 1.6Q$ (EC2 $1.35G + 1.5Q$), steel $0.87f_y$ (EC2 "
             r"$f_{\mathrm{yk}}/1.15 = 0.87f_{\mathrm{yk}}$), stress block $0.45f_{\mathrm{cu}}$ over $0.9x$ (EC2 "
             r"$0.567f_{\mathrm{ck}}$ over $0.8x$), $K' = 0.156$ (EC2 0.167). Answer FE questions to EC2.")

PE = {}

PE[RC] = {"code": "CE201", "title": "Concrete PE prep · BS 8110 notes and worked examples (Tan K H)", "sections": [
 sec("Members, loads and partial factors", (3, 7),
   ("md", "Members: slabs (flexure, shear, punching), beams (flexure, shear), columns (axial + flexure), footings "
          "(flexure, shear, punching). Characteristic load = 5 % chance of being exceeded. ULS combinations (BS "
          r"8110): $1.4G + 1.6Q$; $1.0/1.4G + 1.4W$; $1.2(G + Q + W)$; with earth or water pressure the dead and "
          "imposed factors may drop to 1.0 and 0 if that is more severe. SLS factors are 1.0."),
   ("md", r"Material factors $\gamma_m$: steel 1.15 (BS97: 1.05), concrete in flexure/axial 1.5, shear 1.25, bond "
          r"1.4; EC2 uses 1.5 for concrete throughout. Concrete design stress $0.67f_{\mathrm{cu}}/\gamma_m = "
          r"0.45f_{\mathrm{cu}}$."),
   BS,
 ),
 sec("Bending: singly and doubly reinforced sections", (8, 12),
   ("eq", r"K = \frac{M}{f_{cu}bd^2},\quad z = d\left[0.5 + \sqrt{0.25 - K/0.9}\right] \le 0.95d,\quad A_s = \frac{M}{0.87f_yz}"),
   ("eq", r"K > K' = 0.156:\quad A'_s = \frac{(K - K')f_{cu}bd^2}{0.87f_y(d - d')},\quad A_s = \frac{K'f_{cu}bd^2}{0.87f_yz} + A'_s"),
   ("md", r"Assumptions: plane sections stay plane, perfect bond, no concrete tension. ULS when the extreme fibre "
          r"reaches 0.0035. Design under-reinforced ($x = (d - z)/0.45 \le 0.5d$) so the steel yields first. "
          r"With more than 10 % redistribution $K' = 0.402(\beta_b - 0.4) - 0.18(\beta_b - 0.4)^2$. EC2 limits: $x/d$ "
          r"0.45 and $z \le 0.82d$, $K' = 0.167$ up to C35/45; $x/d$ 0.35, $K' = 0.136$ above."),
 ),
 sec("Shear", (13, 16),
   ("eq", r"v = \frac{V}{b_vd},\quad v_c = \frac{0.79}{1.25}\left(\frac{100A_s}{b_vd}\right)^{1/3}\left(\frac{400}{d}\right)^{1/4}\left(\frac{f_{cu}}{25}\right)^{1/3},\quad \frac{A_{sv}}{s_v} = \frac{b_v(v - v_c)}{0.87f_{yv}}"),
   ("md", r"Shear is carried by the concrete (compression zone, aggregate interlock, dowel action) and the links "
          r"(45° truss). Limits: $v \le 0.8\sqrt{f_{\mathrm{cu}}}$ or 5 MPa (else the section is too small); link "
          r"spacing $\le 0.75d$; minimum links $A_{\mathrm{sv}}/s_v \ge 0.4b_v/(0.87f_{\mathrm{yv}})$. Bent-up bars "
          r"may carry at most 50 % of the steel share. EC2 uses $z = 0.9d$ and a variable strut angle."),
 ),
 sec("Torsion", (17, 18),
   ("eq", r"v_t = \frac{2T}{h_{min}^2(h_{max} - h_{min}/3)},\qquad \frac{A_{sv}}{s_v} = \frac{T}{0.8x_1y_1(0.87f_{yv})},\qquad A_{sl} = \frac{A_{sv}f_{yv}(x_1 + y_1)}{s_vf_y}"),
   ("md", r"Plain concrete fails in torsion as soon as helical cracks form, so links are needed above $v_{t,\min} = "
          r"0.067\sqrt{f_{\mathrm{cu}}}$ (max 0.4 MPa). Split T, L and I sections into rectangles that maximise "
          r"$\sum h_{\min}^3h_{\max}$ and share T by stiffness. Closed links plus longitudinal bars spread round the "
          r"perimeter (at least 4, clear spacing ≤ 300 mm) form a space truss. Crushing check: $v + v_t \le "
          r"0.8\sqrt{f_{\mathrm{cu}}}$ or 5 MPa. EC2: thin-walled tube analogy and $T_{\mathrm{Ed}}/T_{\mathrm{Rd,max}} "
          r"+ V_{\mathrm{Ed}}/V_{\mathrm{Rd,max}} \le 1$."),
 ),
 sec("Bond, anchorage and laps", (19, 24),
   ("eq", r"\ell = \frac{f_s\phi}{4f_{bu}},\qquad f_{bu} = \beta\sqrt{f_{cu}}\quad(\beta = 0.5 \text{ ribbed bars in tension, } 0.63 \text{ in compression})"),
   ("md", r"Hooks count as the larger of $8r$ (max $24\phi$) or the actual length; bends $4r$ (max $12\phi$). Minimum "
          r"bend radius $2\phi$ (mild steel), $3\phi$ (high-yield < 25 mm), $4\phi$ (≥ 25 mm); check bearing inside "
          r"bends. Laps: tension = tension anchorage, compression = 1.25 × compression anchorage, at least $15\phi$ or "
          r"300 mm; stagger them away from high stress. ×1.4 at the top of a section or corners with small cover, "
          r"×2.0 when both apply. Links ($\ge \phi/4$, spacing ≤ 200 mm) are needed if $\phi > 25\ \mathrm{mm}$ and "
          r"cover $< 1.5\phi$."),
 ),
 sec("Corbels", (25, 26),
   ("steps", [r"Strut-and-tie: concrete strut force $F_c = 0.45f_{\mathrm{cu}} \times 0.9x\cos\alpha$, tie force $F_t = "
              r"N\cot\alpha$ with $a_v$ = distance from the load to the column face.",
              r"Lever arm $z = d[0.5 + \sqrt{0.25 - (1 + k)ka_v^2/d^2}]/(1 + k)$ with $k = N/(0.9f_{\mathrm{cu}}ba_v)$; "
              r"$x = (d - z)/0.45$.",
              r"Main tie $A_s = F_t/(0.87f_y)$ if it yields (else use strain compatibility), fully anchored at the "
              r"front.",
              r"Horizontal links in the top two-thirds of d: $\sum A_{sv} \ge 0.5A_s$ and enough for $v - 2dv_c/a_v$."]),
 ),
 sec("Durability, deflection and cracking", (27, 37),
   ("md", r"Cover rises with exposure (mild → very severe) and fire rating; the code tables pair cover with a "
          r"maximum w/c, minimum cement content and minimum grade."),
   ("md", r"Deflection by span/depth: allowable $l/d$ = basic ratio (cantilever 7, simply supported 20, continuous "
          r"26; ×0.8 for flanged with $b_w/b \le 0.3$; ×10/span over 10 m) × $F_t$ (tension steel, from the service "
          r"stress $f_s = \tfrac58f_y A_{s,\mathrm{req}}/A_{s,\mathrm{prov}}$ and $M/bd^2$) × $F_c$ (compression "
          "steel). Limits: span/250 overall; span/500 or 20 mm after finishes."),
   ("md", r"Deflection by calculation: curvature of the cracked or uncracked section (take the larger), long-term "
          r"$E_{\mathrm{eff}} = E_c/(1 + \phi)$, plus shrinkage curvature $\varepsilon_{cs}\alpha_eS_s/I$; total = "
          r"short-term from the non-permanent load + long-term from the permanent load + shrinkage; deflection "
          r"$a = K\ell^2(1/r_b)$ ($K = 5/48$ for a uniform load on a simple span)."),
   ("eq", r"w_{max} = \frac{3a_{cr}\varepsilon_m}{1 + 2(a_{cr} - c_{min})/(h - x)}"),
   ("md", r"Crack control usually by bar spacing: clear gap ≤ $47\,000/f_s$ (≈ 170 mm for $f_s = 275$), corner "
          r"distance ≤ half of that; side bars in deep beams. EC2 uses Tables 7.2N/7.3N."),
 ),
 sec("Columns: classification and design", (38, 47),
   ("md", r"Braced if walls or cores take at least 90 % of the horizontal load. Effective height $\ell_e = "
          r"\beta\ell_o$ ($\beta$ from end conditions 1–4, or from the stiffness ratios $\alpha_c$ at each end). Short if "
          r"$\ell_e/h < 15$ (braced) or $< 10$ (unbraced) about both axes; otherwise slender."),
   ("eq", r"N = 0.4f_{cu}A_c + 0.75f_yA_{sc}\ \text{(short, braced, axial)};\qquad M_{add} = N\beta_aKh,\ \beta_a = \frac{1}{2000}\left(\frac{\ell_e}{b'}\right)^2"),
   ("md", r"Bars: at least 4 (rectangular) or 6 (circular), ≥ 12 mm, spacing ≤ 250 mm, $0.4\,\% \le A_{sc}/A_c "
          r"\le 6\,\%$ (8 % horizontally cast, 10 % at laps). Links ≥ $\phi/4$ or 6 mm at ≤ $12\phi_{\min}$; every "
          r"corner and alternate bar restrained, no bar more than 150 mm from a restrained one. Uniaxial design from "
          r"the N–M charts ($N/bh$, $M/bh^2$). Biaxial: if $M_x/h' \ge M_y/b'$ design for $M_x' = M_x + \beta(h'/b')M_y$ "
          r"($\beta$ from $N/bhf_{\mathrm{cu}}$), else the reverse. Slender: $K$ reduces $M_{\mathrm{add}}$ as N exceeds the "
          r"balanced load $N_{\mathrm{bal}} = 0.25f_{\mathrm{cu}}bd$; start with $K = 1$."),
 ),
 sec("Slab systems", (48, 54),
   ("md", r"One-way slabs: design as continuous beams (moment/shear coefficients for near-equal spans). Two-way "
          r"restrained slabs: $m_{sx} = \beta_{sx}nl_x^2$, $m_{sy} = \beta_{sy}nl_x^2$ in the middle strips (¾ of the "
          r"width); edge strips get minimum steel (0.13 % $bh$ high-yield). Torsion steel at discontinuous corners, "
          r"top and bottom both ways over $l_x/5$: ¾ of the mid-span steel where both edges are discontinuous, 3/8 "
          r"where one is."),
   ("md", r"Flat slabs: no beams, simpler formwork, lower storey heights; drop panels cut punching stress. Moments "
          r"by equivalent frame or coefficients, split between column strip and middle strip: hogging 75 / 25 %, "
          r"sagging 55 / 45 %. Deflection: span/depth on the short span (two-way) or the diagonal (flat slabs). "
          r"Cracking: clear spacing ≤ 3d or 750 mm; no further check if $h \le 200\ \mathrm{mm}$ with high-yield steel "
          r"or $100A_s/bd < 0.3\,\%$ (EC2: ≤ 3h or 500 mm)."),
 ),
 sec("Punching shear", (55, 56),
   ("eq", r"v = \frac{V}{ud} \le v_c;\qquad \text{face: } \frac{N}{2(c_x + c_y)d} \le 0.8\sqrt{f_{cu}}\ \text{or 5 MPa};\qquad u_1 \text{ at } 1.5d \text{ from the face}"),
   ("md", r"If $v > v_c$ provide links on at least two perimeters ≤ 0.75d apart, the first about 0.5d from the face "
          r"with ≥ 40 % of the steel, spacing round a perimeter ≤ 1.5d: $\sum A_{sv}\sin\alpha \ge (v - v_c)ud/0.87f_{yv}$ "
          r"for $v \le 1.6v_c$. Check successive perimeters at 0.75d steps until no steel is needed. ($v_c$ uses the "
          "average steel ratio of both directions.) EC2 checks the basic perimeter at 2d."),
 ),
 sec("Pad footings", (57, 61),
   ("eq", r"p_{max} = \frac{N}{BD}\left(1 + \frac{6e}{D}\right)\ (e \le D/6);\qquad p_{max} = \frac{2N}{3B(D/2 - e)}\ (e > D/6)"),
   ("steps", ["Plan size from characteristic loads (plus self-weight) and the safe bearing pressure.",
              "Thickness from shear (often about D/5); check vertical shear at d and punching at 1.5d from the column face.",
              "Bending at the column face as an inverted cantilever under the ULS pressure on one side.",
              r"Spread bars evenly if $\ell_c \le 1.5(c + 3d)$, else concentrate under the column; cover 75 mm cast "
              "against earth, 40 mm on blinding."]),
 ),
 sec("Retaining walls", (62, 63),
   ("md", "Gravity walls (mass concrete, rely on weight; up to about 3 m), cantilever walls (stem on a stiff base, "
          "backfill on the heel helps stability; economic to about 8 m), counterfort walls (thin wall spanning "
          "between counterforts designed as cantilevers). Check stability (ULS), bearing pressures (SLS), then design "
          "the stem, toe and heel as members at ULS and SLS."),
 ),
 sec("Curtailment and detailing", (64, 66),
   ("md", r"Curtailed bars extend beyond the point they are no longer needed by at least d or $12\phi$, and should "
          r"not stop in a tension zone unless special conditions are met; stagger cut-offs. At a simple support each "
          r"tension bar must reach the support centre or d/2 past its face before any hook or bend starts. Simplified "
          "rules apply to continuous beams only when imposed load ≤ dead load."),
 ),
 sec("Worked examples: simply supported beam", (69, 80),
   q("PE prep Ex 1(a)–(b)",
     r"A 300 × 500 mm simply supported beam (effective span 6.2 m, severe exposure, 2 h fire; $f_y = 460$, "
     r"$f_{\mathrm{cu}} = 40\ \mathrm{MPa}$) carries a maximum ULS moment of 216 kNm and 140 kN shear at the support "
     r"face (116 kN at d). Design it for bending and shear and check deflection by span/depth.",
     r"**$d = 434\ \mathrm{mm}$; $K = 0.0956$, $z = 382$, $A_s = 1413$ → 3T25 (1472); top 2T12 · $v = 1.08 < 5\ "
     r"\mathrm{MPa}$, $v \le v_c + 0.4$ → nominal T8 links @ 300 · $l/d = 14.3 <$ allowable $20 \times 0.90 = 18$ "
     r"✓.**",
     r"Cover 40 mm (severe, 2 h) → $d = 500 - 40 - 10 - 12.5$. $A_s = 216 \times 10^6/(0.87 \times 460 \times 382)$. "
     r"Minimum links $0.4 \times 300 \times 300/(0.87 \times 460) = 90\ \mathrm{mm^2}$. Service stress $f_s = "
     r"\tfrac58 \times 460 \times 1413/1472 = 275\ \mathrm{MPa}$, $M/bd^2 = 3.8$ → $F_t = 0.90$."),
   q("PE prep Ex 1(c)",
     r"For the same beam ($E_s = 200$, $E_c = 28\ \mathrm{GPa}$; dead 20 and live 10 kN/m, span 6.2 m, props out at "
     r"28 days, outdoor) estimate the short-term and long-term deflections.",
     r"**Short-term (total load) 15.5 mm < span/250 = 24.8 mm · long-term total 21.8 mm.**",
     r"Mid-span M 144.2 (total) / 96.1 kNm (permanent). Cracked curvatures: $3.87 \times 10^{-6}$ (total), $2.43 "
     r"\times 10^{-6}$ (permanent, short-term), $3.66 \times 10^{-6}$ (permanent, long-term with $\phi = 1.65$, "
     r"$E_{\mathrm{eff}} = 10.6\ \mathrm{GPa}$); shrinkage $0.33 \times 10^{-6}$/mm. Long-term $1/r = (3.87 - 2.43) + "
     r"3.66 + 0.33 = 5.43 \times 10^{-6}$; $a = (5/48) \times 6200^2 \times 5.43 \times 10^{-6}$."),
   q("PE prep Ex 1(d)–(f)",
     r"For the same beam under 144 kNm: estimate the maximum crack width, check the bar-spacing rules, and decide "
     r"where the central T25 bar can stop.",
     r"**$w_{\max} = 0.299\ \mathrm{mm}$ at the bottom corner (0.154 mm at the side) < 0.3 ✓ · clear spacing 64.5 mm "
     r"< 170 mm ✓ · stop the central bar 400 mm from the support face ($0.08\ell = 496 \approx 500\ \mathrm{mm}$ from "
     r"the support centre).**",
     r"$E_c/2 = 14\ \mathrm{GPa}$ → $x = 186.3\ \mathrm{mm}$, $f_s = 263\ \mathrm{MPa}$, $\varepsilon_m = 1.53 "
     r"\times 10^{-3}$ at the corner, $a_{cr} = 75.9\ \mathrm{mm}$.")),
 sec("Worked example: restrained two-way slab", (80, 83),
   q("PE prep Ex 2",
     r"A 175 mm corner slab panel (6 m short span) cast with its edge beams carries 6 kPa dead and 2.5 kPa imposed "
     r"load ($f_{\mathrm{cu}} = 30$, $f_y = 460$). Design it and show the steel.",
     r"**$n = 1.4 \times 6 + 1.6 \times 2.5 = 12.4\ \mathrm{kPa}$ · hogging 20.4 kNm/m → T10 @ 180; sagging 15.2 "
     r"kNm/m → T8 @ 150; edge strips T8 @ 200 (minimum $227.5\ \mathrm{mm^2/m}$) · shear $v = 0.26 < v_c "
     r"= 0.55\ \mathrm{MPa}$ · torsion steel: ¾ × 276 = 207 at the corner discontinuous both ways, 3/8 × 276 = "
     r"$104\ \mathrm{mm^2/m}$ at the other · deflection $38.7 < 26 \times 1.88 = 48.8$ ✓.**",
     r"$d = 155$ (outer, x) and 145 mm (inner). Corner torsion steel in four layers over $l_x/5$.")),
 sec("Worked examples: columns", (84, 87),
   q("PE prep Ex 3–4",
     r"(3) Is the column shown short or slender ($\ell_{ex} = 0.85 \times 4000$ on 200 mm; $\ell_{ey} = 0.75 \times "
     r"3600$ on 400 mm; braced)? (4) Design a short braced column for an ultimate axial load of 2000 kN "
     r"($f_{\mathrm{cu}} = 40$, $f_y = 460$).",
     r"**(3) $3400/200 = 17 > 15$ → slender (about the minor axis; $6.75 < 15$ about the other) · (4) 300 mm square, "
     r"$A_{sc} = 1623$ → 6T20 ($1885\ \mathrm{mm^2}$, 2.1 %), T8 links @ 200.**",
     r"$2000 \times 10^3 = 0.4 \times 40 \times 90\,000 + 0.75 \times 460 \times A_{sc}$."),
   q("PE prep Ex 5",
     r"Design the longitudinal steel for a 500 × 300 mm column with N = 2300 kN, $M_x = 300$ and $M_y = 120\ "
     r"\mathrm{kNm}$ ($f_{\mathrm{cu}} = 40$, $f_y = 460$, 50 mm to bar centres).",
     r"**$M_x/h' = 667 > M_y/b' = 480$ → $M_x' = 300 + 0.55 \times (450/250) \times 120 = 419\ \mathrm{kNm}$; chart: "
     r"$A_{sc} = 3.5\,\% = 5250\ \mathrm{mm^2}$ → 4T32 + 2T40 ($5729\ \mathrm{mm^2}$ effective).**",
     r"$N/bhf_{\mathrm{cu}} = 0.38$ → $\beta = 0.55$; $N/bh = 15.3$, $M/bh^2 = 5.59$.")),
 sec("Worked example: pad footing", (88, 91),
   q("PE prep Ex 6",
     r"Design a pad footing for a 450 mm square column carrying 1400 kN dead and 600 kN imposed (characteristic); "
     r"$f_{\mathrm{cu}} = 30$, $f_y = 460$, safe bearing pressure 180 kPa.",
     r"**3.6 × 3.6 m, 700 mm thick (service 170.8 < 180 kPa) · ULS pressure 225.3 kPa → $M = 1006\ \mathrm{kNm}$, "
     r"$A_s = 4241$ → 15T20 spread evenly · vertical shear $v = 0.34 < v_c = 0.39$ ✓ · punching at 1.5d: $v = 0.29 "
     r"< 0.39\ \mathrm{MPa}$ ✓.**",
     r"$d = 630\ \mathrm{mm}$. Cantilever 1.575 m: $1.575 \times 3.6 \times 225.3 \times 1.575/2$. Perimeter $u = "
     r"2(450 + 450) + 8 \times 1.5 \times 630 = 9360\ \mathrm{mm}$; load outside it $(12.96 - 5.48) \times 225.3$.")),
]}

PE[BD] = {"code": "CE201", "title": "Concrete PE prep · Introduction to beam and column design (BS 8110)", "sections": [
 sec("Limit states, characteristic values and load cases", (2, 6),
   ("md", "Design for the ultimate limit state (collapse, mechanism, buckling, overturning) and check the "
          "serviceability limit states (deflection, cracking, durability, vibration, fire). Characteristic strength: "
          "5 % of results fall below it. Pattern loading for maximum span moment: 1.4G + 1.6Q on that span, 1.0G on "
          r"the adjacent spans; for support moments load the two adjacent spans fully."),
   BS,
 ),
 sec("Frame analysis: subframes and coefficients", (7, 9),
   ("md", "Braced frames carry vertical load only: analyse a whole floor with its columns, a subframe of each beam "
          "with its neighbours, or a continuous beam with columns giving no rotational restraint. Continuous-beam "
          r"coefficients (Q ≤ G, ≥ 3 near-equal spans within 15 %, uniform load): end-span middle $0.09F\ell$, first "
          r"interior support $-0.11F\ell$, interior span $0.07F\ell$, interior supports $-0.08F\ell$; shear $0.45F$ "
          r"(outer support) and $0.6F$ (first interior); no redistribution then. Unbraced frames: worse of the braced "
          r"case and $1.2(G + Q)$ plus $1.2W$ with hinges at mid-length; overall stability under $1.0G + 1.4W$."),
 ),
 sec("Moment redistribution", (9, 13),
   ("md", r"A ductile (under-reinforced) section that reaches its capacity acts as a hinge, so elastic moments may be "
          r"redistributed provided (1) equilibrium holds, (2) $x/d \le \beta_b - 0.4$ at the critical sections, and "
          r"(3) each section keeps at least 70 % of its elastic moment (90 %, i.e. ≤ 10 % redistribution, for frames "
          r"over 4 storeys giving lateral stability). $\beta_b$ = moment after / before redistribution. The 70 % "
          r"rule stops hogging regions cracking at service when designed for sagging at ultimate."),
 ),
 sec("Durability and fire cover", (11, 12),
   ("md", "Nominal cover grows with exposure (mild 20–25, moderate 25–35, severe 30–40 mm, very severe 30–50, "
          "with matching grade and w/c limits) and with fire rating (e.g. 2 h: simply supported beams 40 mm, "
          r"continuous 30 mm; minimum beam width 200 mm, slab thickness 125 mm)."),
 ),
 sec("Section design for bending", (14, 19),
   ("md", r"Strain compatibility with $\varepsilon_{cu} = 0.0035$: guess x, find the steel strains and stresses, "
          r"iterate until $0.45f_{\mathrm{cu}} \times 0.9xb = f_sA_s - f'_sA'_s$. Compression steel yields if $d'/x "
          r"\le 0.43$ (for 460 MPa steel). Flanged sections: if $0.9x \le h_f$ design as a rectangle of width b; "
          r"otherwise take moments about the flange centroid."),
 ),
 sec("Anchorage, laps and curtailment", (20, 24),
   ("md", r"Bond coefficient $\beta$ (Table 3.28) gives $f_{bu} = \beta\sqrt{f_{\mathrm{cu}}}$; anchorage and lap lengths "
          r"come as multiples of $\phi$ (Table 3.29). Simplified curtailment rules apply to beams under essentially uniform "
          "load."),
 ),
 sec("Shear and torsion", (25, 33),
   ("md", r"Shear failure is brittle, so ultimate strength should be governed by flexure. Design shear stress $v = "
          r"V/bd$; links where $v > v_c + 0.4$, nominal links otherwise (minor members excepted); bent-up bars may "
          r"carry up to half. Torsion: space-truss model; closed links at $s_v \le \min(x_1, y_1/2, 200\ "
          r"\mathrm{mm})$ and longitudinal bars spread round the perimeter."),
 ),
 sec("Deflection and crack control", (34, 37),
   ("md", r"Final deflection ≤ span/250; after finishes ≤ span/500 or 20 mm. Span/depth method with $F_t$ and "
          r"$F_c$; for flanged beams the basic ratio 20.8 applies when $b_w/b \le 0.3$. Crack control by bar spacing "
          r"(beams: clear gap $\le 47\,000/f_s$; slabs: $\le 75\,000\beta_b/f_y$ and 300 mm)."),
 ),
 sec("Robustness and ties", (38, 39),
   ("md", r"Every structure must resist a notional horizontal force of 1.5 % of the characteristic dead load at each "
          r"level. Ties: peripheral, internal (both ways), column/wall and vertical; basic force $F_t = \min[60,\ 20 + "
          r"4n_0]$ kN/m ($n_0$ = storeys). Internal ties carry the larger of $F_t$ and $F_t(g_k + q_k)\ell_r/(7.5 \times "
          r"5)$ per metre; column ties the larger of $2F_t$, $F_t\ell_s/2.5$ and 3 % of the column's ultimate load. "
          "Vertical ties are needed from five storeys up."),
   q("Beam design notes: tie example",
     r"A 4-storey frame has internal ties at 5.5 m spacing ($g_k + q_k$ and spans as in the notes; $f_y = 460$). "
     r"Find the internal tie force and steel, and the external column tie force (column ultimate load 1500 kN, storey "
     r"height 4 m).",
     r"**$F_t = 20 + 4 \times 4 = 36\ \mathrm{kN/m}$ → internal tie 76.4 kN/m × 5.5 m = 420 kN, $A_s = 1049\ "
     r"\mathrm{mm^2}$ → 2T32 · column tie $\max(72,\ 55,\ 45) = 55\ \mathrm{kN}$, $A_s = 137\ \mathrm{mm^2}$.**",
     r"$A_s = 420 \times 10^3/(0.87 \times 460) = 1049$; $55 \times 10^3/(0.87 \times 460) = 137$.")),
 sec("Columns", (40, 55),
   ("md", r"Axial capacity $N = 0.45f_{\mathrm{cu}}A_c + 0.87f_yA_{sc}$ (design formula $0.4f_{\mathrm{cu}}A_c + "
          r"0.75f_yA_{sc}$ allows for a minimum eccentricity). Shear in columns: no check for $M/N < 0.75h$ beyond $v "
          r"\le 0.8\sqrt{f_{\mathrm{cu}}}$; otherwise $v'_c = v_c + 0.75(N/A_c)(Vd/M)$. Slender braced columns: "
          r"$M_i = 0.4M_1 + 0.6M_2 \ge 0.4M_2$, design moment = max of $M_2$, $M_i + M_{\mathrm{add}}$, $M_1 + "
          r"M_{\mathrm{add}}/2$ and $Ne_{\min}$ ($e_{\min} = 0.05h$ ≤ 20 mm); unbraced: use the average deflection of "
          r"the storey and put $M_{\mathrm{add}}$ at the column end."),
   q("Beam design notes: slender braced column",
     r"A braced 400 × 500 mm column, 6.5 m effective height, carries N = 2500 kN with end moments 200 and 250 kNm "
     r"about the major axis ($f_{\mathrm{cu}} = 40$, $f_y = 460$). Find the design moment and steel.",
     r"**$\ell_e/b = 16.25 > 15$ → slender · $M_i = 230$, $M_{\mathrm{add}} = 2500 \times 0.13 \times 0.5 = 162.5\ "
     r"\mathrm{kNm}$ ($K = 1$) → 392.5 kNm; the chart then gives $K = 0.75$, so $M = 230 + 0.75 \times 162.5 = "
     r"352\ \mathrm{kNm}$ → $A_{sc} = 1.4\,\% = 2800$ → 4T32 ($3216\ \mathrm{mm^2}$).**",
     r"$\beta_a = 16.25^2/2000 = 0.13$; $M_i = 0.4 \times 200 + 0.6 \times 250$. Repeat with the new K until it "
     r"settles.")),
]}

# ======================================================================== CE206 wastewater
_TXT = ("tip", "Notes from the text of a scanned 16 MB PDF (not stored here): slide numbers are approximate and "
               "figures are missing. Open the Drive copy for diagrams.")

PE[WW] = {"code": "CE206", "title": "Wastewater PE prep · Flows, sewers, treatment and activated sludge (Ong S L)", "sections": [
 sec("Population projection", (1, 20),
   _TXT,
   ("eq", r"\text{Arithmetic: } P_t = P_0 + K\Delta t;\quad \text{uniform-\% method: } \ln P_t = \ln P_0 + K'\Delta t;\quad \text{logistic: } P = \frac{P_{sat}}{1 + ae^{b\Delta t}}"),
   ("eq", r"\text{Declining growth: } P_t = P_0 + (P_{sat} - P_0)(1 - e^{-K''\Delta t}),\ K'' = -\frac{1}{n}\ln\frac{P_{sat} - P_1}{P_{sat} - P_0}"),
   ("md", r"Logistic constants from three censuses n years apart: $P_{sat} = [2P_0P_1P_2 - P_1^2(P_0 + P_2)]/(P_0P_2 "
          r"- P_1^2)$. Other methods: graphical extension, ratio to a larger region ($P = K_rP_R$), land use ($P = "
          r"\sum A_iy_i$ with densities e.g. public housing 400–740, medium density 250, light industry 120 persons/ha) "
          "and equivalent population (e.g. 0.5 per university student or staff, 3.5 per hospital bed)."),
   q("Wastewater notes: City A",
     r"City A had 4411, 6193, 6629, 19 351 and 39 418 people in 1950–1990 (10-year steps). Project 2005 by the "
     r"arithmetic, uniform-percentage, logistic and declining-growth (saturation 63 000) methods.",
     r"**Arithmetic 44 311 · uniform % 73 629 · logistic 58 290 ($P_{sat} = 63\,008$) · declining growth 53 736 · "
     r"graphical 71 500 → expect 44 000–74 000.**",
     r"Arithmetic and uniform-% by regression on all five censuses. Logistic from the 1970/80/90 censuses. Declining "
     r"growth from 1980/90: $K'' = 0.062$, $\Delta t = 25$: $19\,351 + 43\,649(1 - e^{-1.55})$.")),
 sec("Wastewater flows and peaking", (21, 28),
   ("md", r"$Q = P \times$ per-capita discharge (local data, or standard values such as 130–180 L/cap·d high-density "
          r"residential and 235–270 for low density and industry). Flows peak 6–8 am and 6–8 pm; small sewers see "
          r"bigger swings. Minimum flow (≈ 0.4 × average) sets the flattest slope; maximum flow sizes sewers and "
          r"works. Infiltration ≈ 0.8 L/s per ha or 2.5 L/s per m diameter per km."),
   ("eq", r"PF = 1 + \frac{14}{4 + \sqrt P}\ (\text{Harmon, } P \text{ in thousands});\qquad PF = 5P^{-0.16}\ (\text{common in the region})"),
   ("md", "Design periods: pumping stations about 10 years, treatment plants 15–20 years; both need peak, average "
          "and minimum flows with infiltration."),
 ),
 sec("Sewer hydraulics", (29, 34),
   ("eq", r"V = \frac{1}{n}R^{2/3}S^{1/2},\qquad R = \frac{D}{4}\ \text{(full circular pipe)},\qquad n = 0.013\ \text{new},\ 0.015\ \text{old}"),
   ("md", "Size and slope: assume D and S, compute full-flow V and Q, check capacity ≥ design flow, revise. Part-full "
          "flow from the hydraulic-elements chart (d/D → q/Q and v/V). Keep velocity between about 0.6 (self-cleansing) "
          "and 2.4 m/s."),
   q("Wastewater notes: part-full sewer",
     r"A 1200 mm concrete sewer on a slope of 0.0015 ($n = 0.013$) flows 740 mm deep. Find the flow and velocity.",
     r"**Full: $V = 1.34\ \mathrm{m/s}$, $Q = 1.51\ \mathrm{m^3/s}$ · $d/D = 0.62$ → $q/Q = 0.72$, $v/V = 1.08$ → $q "
     r"= 1.09\ \mathrm{m^3/s}$, $v = 1.45\ \mathrm{m/s}$.**",
     r"$V = (1/0.013)(0.3)^{2/3}(0.0015)^{1/2}$; $A = \pi \times 1.2^2/4$.")),
 sec("Wastewater characteristics and treatment methods", (35, 82),
   ("md", r"Typical domestic sewage: total solids 300–1200 (≈ 700) mg/L, suspended 100–400 (220), $\mathrm{BOD_5}$ "
          r"100–400 (≈ 220), COD 200–1000 (500), total N 15–90 (40), ammonia 0–50 (25), total P 5–20 (8) mg/L; about "
          r"70 % of suspended solids are volatile. Coliforms by membrane/plate counts (30–300 colonies per plate) or "
          r"multiple-tube MPN tables. Toxicity: 96 h $\mathrm{LC_{50}}$ from bioassays; permissible concentration "
          r"1/10–1/100 of the 96 h median tolerance limit."),
   ("md", r"Singapore Trade Effluent Regulations (sewer / watercourse / controlled watercourse), mg/L: "
          r"$\mathrm{BOD_5}$ 400 / 50 / 20, COD 600 / 100 / 60, SS 400 / 50 / 30, oil & grease 60 / 10 / 5."),
   ("md", "Unit operations (physical): screening, sedimentation, filtration, aeration, flotation. Unit processes "
          "(chemical): precipitation (e.g. P removal with iron), neutralisation, gas stripping, coagulation, ion "
          "exchange, oxidation, disinfection. Biological: activated sludge, trickling filters (BOD removal 40–85 %), "
          "rotating biological contactors, anaerobic contact, stabilisation lagoons, nitrification/denitrification, "
          r"anaerobic digestion (HRT 15–20 d, 40–60 % organic solids reduction; methane explosive at 5–15 %)."),
   ("eq", r"\mathrm{NH_4^+ + 2O_2 \to NO_3^- + 2H^+ + H_2O}\ (4.57\ \mathrm{g\ O_2/g\ N});\qquad \mathrm{6NO_3^- + 5CH_3OH \to 5CO_2 + 3N_2 + 7H_2O + 6OH^-}"),
 ),
 sec("Preliminary treatment: screens and grit chambers", (83, 103),
   ("md", "Bar screens: hand-cleaned 25–50 mm openings at 30–45°, mechanical 15–75 mm at 45–90°, approach velocity "
          "0.6–1.0 m/s, head loss < 0.1 m clean and < 0.3 m in use. Grit chambers protect pumps and pipes and cut "
          "digester cleaning; horizontal-flow types remove grit over 0.2 mm."),
   ("eq", r"v_s = \frac{g(\rho_p - \rho)d^2}{18\mu}\ (N_R < 0.3);\qquad C_D = \frac{24}{N_R} + \frac{3}{\sqrt{N_R}} + 0.34;\qquad V_H = \sqrt{\frac{8\beta(S - 1)gd}{f}}"),
   ("md", r"Keep $V_H$ between the scour velocity of organics and that of grit (e.g. 5.6–18.6 cm/s for 0.2 mm grit). "
          r"Constant velocity needs a section matched to the outlet weir: rectangular channel with a proportional "
          r"weir, parabolic channel with a rectangular (Parshall-type) control. Length $L \ge DV_H/v_s$ plus inlet and "
          r"outlet allowance. Typical horizontal-flow design: detention 45–90 s, $V_H$ ≈ 0.3 m/s. Aerated grit "
          r"chambers: 2–5 min detention at peak, depth 2–5 m, width:depth ≈ 1.5:1, air 0.2–0.5 $\mathrm{m^3/min}$ per m "
          r"of length."),
   q("Wastewater notes: settling velocity",
     r"Find the terminal settling velocity of a 0.5 mm sand grain (shape factor 0.85, $\rho_p = 2600\ "
     r"\mathrm{kg/m^3}$) in water at 20 °C ($\rho = 998.2$, $\mu = 1.002 \times 10^{-3}\ \mathrm{Pa\,s}$).",
     r"**About 0.083 m/s (Stokes gives 0.22 m/s, but $N_R = 93$ is transitional, so iterate with $C_D$).**",
     r"Iterate $v_s = \sqrt{4g(\rho_p - \rho)d/(3C_D\rho)}$ with $N_R = \phi v_sd\rho/\mu$: 0.11 → 0.09 → 0.085 → "
     r"0.083 m/s."),
   q("Wastewater notes: aerated grit chamber",
     r"Design aerated grit chambers for an average flow of $0.5\ \mathrm{m^3/s}$ with a peaking factor of 2.75.",
     r"**Two chambers, 3 min at peak → $124\ \mathrm{m^3}$ each, 3 m deep × 3.6 m wide × 11.5 m long; air ≈ $4.0\ "
     r"\mathrm{m^3/min}$ per chamber; grit ≈ $0.65\ \mathrm{m^3/d}$.**",
     r"Peak $1.375\ \mathrm{m^3/s}$; $0.5 \times 1.375 \times 180 = 123.75$; air $0.35 \times 11.5$; grit $15\ "
     r"\mathrm{m^3}$ per $10^6\ \mathrm{m^3}$.")),
 sec("Primary sedimentation", (104, 110),
   ("md", r"Removes settleable and floating solids ahead of biological treatment: settleable solids 90–95 %, SS "
          r"50–70 %, $\mathrm{BOD_5}$ 20–40 %. Detention 1.5–2.5 h (longer turns septic); overflow rate 32–49 "
          r"$\mathrm{m^3/m^2 \cdot d}$ at average flow, 81–122 at peak; weir loading 124–496 (typical 248) "
          r"$\mathrm{m^3/m \cdot d}$. Rectangular tanks 3–4.5 m deep, 15–90 m long; circular 3–60 m diameter."),
 ),
 sec("Process kinetics and reactors", (111, 141),
   ("eq", r"r = -KC^n;\quad \text{zero order } C = C_0 - Kt;\quad \text{first order } C = C_0e^{-Kt};\quad \text{second order } \frac1C = \frac1{C_0} + Kt"),
   ("eq", r"\text{Michaelis–Menten: } V = \frac{V_m[S]}{K_m + [S]};\qquad K_T = K_{20}\theta^{T - 20}"),
   ("eq", r"\text{First order: batch/PFR } t = \frac1K\ln\frac{C_0}{C};\qquad \text{CSTR } t = \frac1K\left(\frac{C_0}{C} - 1\right)"),
   ("md", r"A CSTR needs a longer detention for the same removal (for $C_0 = 245$, $C = 50\ \mathrm{mg/L}$, $K = 8.3\ "
          r"\mathrm{d^{-1}}$: batch/PFR 4.6 h, CSTR 11.3 h) but buffers shock and toxic loads. CSTRs in series "
          "approach plug flow; recycle pushes a PFR towards a CSTR."),
 ),
 sec("Microbiology and growth kinetics", (142, 175),
   ("md", r"Nutrients: $\mathrm{BOD : N : P} \approx 100 : 5 : 1$ (or 1 g N per 30 g and 1 g P per 140 g COD "
          r"removed). Classify microbes by energy source (photo/chemo-trophs), carbon source (auto/hetero-trophs), "
          r"oxygen (aerobic, anaerobic, facultative) and temperature (psychrophilic 12–18, mesophilic 27–38, "
          r"thermophilic 49–57 °C optimum); pH 6.5–7.5 best. Batch growth: lag, exponential, stationary, death."),
   ("eq", r"\mu = \frac{\mu_mS}{K_s + S},\qquad Y_{obs} = \frac{Y}{1 + k_d\theta_c},\qquad T_d = \frac{\ln 2}{\mu_m}"),
   q("Wastewater notes: nutrient balance",
     r"1000 L of industrial waste ($\mathrm{BOD_5}$ 1500, N 30, P 0 mg/L) is blended with domestic sewage (BOD 200, N "
     r"35, P 10 mg/L). How much sewage is needed for BOD : N : P = 100 : 5 : 1?",
     r"**About 1875 L (set by phosphorus; nitrogen needs only 1800 L).**",
     r"P: $(1500 \times 1000 + 200V)/(10V) = 100$ → $V = 1875$. N: $(1500 \times 1000 + 200V)/(30 \times 1000 + 35V) = "
     r"100/5$ → $V = 1800$.")),
 sec("Activated sludge process", (176, 215),
   ("eq", r"\theta_c = \frac{VX}{Q_wX_r + (Q - Q_w)X_e},\qquad \frac{1}{\theta_c} = Y\frac{Q(S_0 - S)}{VX} - k_d"),
   ("eq", r"S = \frac{K_s(1 + k_d\theta_c)}{\theta_c(Yk - k_d) - 1}"),
   ("eq", r"X = \frac{\theta_c}{\theta}\cdot\frac{Y(S_0 - S)}{1 + k_d\theta_c},\qquad P_x = \frac{VX}{\theta_c},\qquad O_2 = \frac{Q(S_0 - S)}{f} - 1.42P_x\ (+\ 4.57Q\cdot TKN)"),
   ("md", r"Mixed liquor is mainly aerobic and facultative bacteria; protozoa and rotifers clean up dispersed "
          r"bacteria. Filamentous bulking from very high or low loads, missing nutrients, low pH or DO, infrequent "
          r"wasting. SVI = settled volume after 30 min (mL/L) ÷ MLSS (g/L). Loading: high-rate (MCRT 0.2–0.5 d, F/M "
          r"0.4–1.5), conventional (5–15 d, 0.2–0.4), extended aeration (20–30 d, 0.05–0.15). Keep DO ≥ 2 mg/L. Typical "
          r"kinetics at 20 °C: $\mu_m$ 2–10 (5) $\mathrm{d^{-1}}$, $K_s$ 25–100 (60) mg/L BOD, Y 0.4–0.8 (0.6), "
          r"$k_d$ 0.04–0.075 (0.06) $\mathrm{d^{-1}}$. SBRs fill, react, settle, decant and idle in one tank (no "
          "clarifier or return pumping)."),
   ("steps", [r"Choose $\theta_c$ and get S from the kinetic constants.",
              r"Choose MLSS X, then $V = Q\theta$ from the X equation.",
              r"Return ratio from a clarifier balance: $X(1 + R) = RX_r$.",
              r"Sludge wasted $P_x = VX/\theta_c$; oxygen demand from the BOD removed minus $1.42P_x$ (plus nitrification)."]),
 ),
 sec("Aeration design", (216, 239),
   ("eq", r"\frac{dC}{dt} = K_La(C_s - C),\qquad C_s \approx \frac{475 - 2.65S}{33.5 + T}\cdot\frac{P - p}{760 - p},\qquad \alpha = \frac{K_La_{ww}}{K_La_{tap}},\ \beta = \frac{C_{s,ww}}{C_{s,tap}}"),
   ("eq", r"N = N_0\frac{\beta C_{s} - C_L}{9.2}\alpha\,1.024^{T - 20}"),
   ("md", "Manufacturers rate aerators in clean water at 20 °C, 760 mm Hg and zero DO; correct to field conditions. "
          "For diffused air and submerged turbines use the mean saturation over the depth, $C_s[(P_b/2941) + (O_t/42)]$ "
          r"with $P_b = 73.8H + P$ (mm Hg) and $O_t$ the oxygen left in the exit air (6–10 % of the 21 % absorbed). "
          r"Turbines give 0.9–1.2 (single) or 1.5–1.8 (dual impeller) kg $\mathrm{O_2}$/kWh. Power = oxygen demand ÷ "
          "field transfer rate."),
 ),
]}

OUTLINE = {
    RC: ("CE201", 91, 40, "PE prep: Reinforced & prestressed concrete (Tan K H, BS 8110)",
         [(3, 7, ["CE201-01"]), (8, 12, ["CE201-02"]), (13, 16, ["CE201-03"]), (17, 18, ["CE201-04"]),
          (19, 24, ["CE201-05"]), (25, 26, ["CE201-06"]), (27, 28, ["CE201-08"]), (29, 37, ["CE201-07"]),
          (38, 47, ["CE201-09", "CE201-10"]), (48, 54, ["CE201-11"]), (55, 56, ["CE201-12"]),
          (57, 61, ["CE201-13"]), (62, 63, ["CE201-14"]), (64, 66, ["CE201-15"]),
          (69, 80, ["CE201-02", "CE201-07"]), (80, 83, ["CE201-11"]), (84, 87, ["CE201-09", "CE201-10"]),
          (88, 91, ["CE201-13"])]),
    BD: ("CE201", 55, 41, "PE prep: Introduction to beam and column design (BS 8110)",
         [(2, 6, ["CE201-01"]), (7, 9, ["CE201-01"]), (9, 13, ["CE201-02"]), (11, 12, ["CE201-08", "CE201-21"]),
          (14, 19, ["CE201-02"]), (20, 24, ["CE201-05", "CE201-15"]), (25, 33, ["CE201-03", "CE201-04"]),
          (34, 37, ["CE201-07"]), (38, 39, ["CE201-15"]), (40, 55, ["CE201-09", "CE201-10"])]),
    WW: ("CE206", 239, 1, "PE prep: Wastewater flows, sewers, treatment, activated sludge (Ong S L) — text only",
         [(1, 34, ["CE206-04"]), (35, 82, ["CE206-05", "CE206-06"]), (83, 110, ["CE206-05"]),
          (111, 175, ["CE206-06"]), (176, 239, ["CE206-06"])]),
}
