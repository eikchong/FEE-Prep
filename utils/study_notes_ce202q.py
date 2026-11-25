"""CE202 tutorial questions (CE3166 Tut 1–8) as q blocks. Statements are from the question sheets in
materials/CE202; answers from the official solutions where they exist. Tutorials 1, 3, 4 (Q2) and 5 have no
solution file: those were solved here (src="claude"). Numbers are recomputed in tests/test_tutorial_answers.py."""
from utils.qblock import q
from utils.study_notes_ce202 import D


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


STLQ = {}

STLQ[D["T1"]] = {"code": "CE202", "title": "Steel practice · Tut 1 Load combinations (4-storey braced frame)", "sections": [
 sec("Q1 Four-storey braced frame: beams and columns", (2, 4),
   q("CE3166 Tut 1 Q1",
     r"A 4-storey braced steel frame (Figure Q1; grid 8 m + 6 m across, nine 6 m bays along; storeys 5 + 3 × 4.5 m; "
     r"triangular roof truss spanning the full 14 m) uses simple construction and S355 steel, with pinned bases; wind is "
     r"taken by the bracing. Level 1 slabs span two ways; levels 2 and 3 span one way onto secondary beams at mid-bay. "
     r"Floors: $G_k = 3.5 + 0.5\ \mathrm{kN/m^2}$, $Q_k = 3.0$ (offices) $+ 1.5$ (moveable partitions) "
     r"$\mathrm{kN/m^2}$; roof: $G_k = 0.75 + 0.25$, $Q_k = 0.4\ \mathrm{kN/m^2}$ (category H). (a) Find the design "
     r"moment and shear for beam G1–2 at level 1. (b) The same for beam 2–GF (gridline 2 between F and G) at level 2. "
     r"(c) The ULS axial force in the internal ground-floor column G2. (d) The same for the external column G1, with "
     r"cladding of $4\ \mathrm{kN/m^2}$ per storey. (e) Find the beams' deflection under imposed load.",
     r"**Floor ULS load $1.35 \times 4.0 + 1.5 \times 4.5 = 12.15\ \mathrm{kN/m^2}$ · (a) trapezoidal load, peak "
     r"$72.9\ \mathrm{kN/m}$: $M = 474\ \mathrm{kNm}$, $V = 182\ \mathrm{kN}$ · (b) secondary-beam point load 255 kN "
     r"at mid-span: $M = 383\ \mathrm{kNm}$, $V = 128\ \mathrm{kN}$ · (c) $N = 1531\ \mathrm{kN}$ · (d) $N = 1556\ "
     r"\mathrm{kN}$ (the value used in the Tut 2 solutions) · (e) for L/360: G1–2 needs $I_y \ge 24\,300\ "
     r"\mathrm{cm^4}$, 2–GF $\ge 12\,200\ \mathrm{cm^4}$.**",
     r"(a) Two-way slab, 6 m × 8 m panels on both sides: 45° lines give a trapezoid rising over 3 m to $12.15 \times "
     r"6 = 72.9\ \mathrm{kN/m}$. $W = 72.9 \times (8 + 2)/2 = 364.5$; $M = w(3L^2 - 4a^2)/24 = 72.9 \times 6.5$. "
     r"(b) Slab spans 3 m onto beams and secondary beams (3 m strips, $36.45\ \mathrm{kN/m}$); secondary reactions "
     r"$36.45 \times 4 + 36.45 \times 3 = 255.2$; $M = PL/4$. (c) Column 2 stops at level 3 (the truss spans 1–3), so "
     r"G2 carries three floors of $7 \times 6 = 42\ \mathrm{m^2}$: $3 \times 42 \times 12.15$. (d) Three floors of "
     r"$4 \times 6 = 24\ \mathrm{m^2}$ + roof $7 \times 6 = 42\ \mathrm{m^2}$ + cladding $4 \times 6 \times 18.5 = 444\ "
     r"\mathrm{kN}$: $1.35(288 + 42 + 444) + 1.5(324 + 16.8) = 1556$. Strictly, a category H roof load has $\psi_0 = "
     r"0$, so with floors leading it drops out → 1531 kN. No imposed-load reduction $\alpha_n$ applied. (e) $Q_k$ "
     r"only: trapezoid peak 27 kN/m, $\delta = w(25L^4 - 40a^2L^2 + 16a^4)/(1920EI)$; 2–GF $P_k = 94.5\ "
     r"\mathrm{kN}$, $\delta = PL^3/(48EI)$; $E = 210\ \mathrm{GPa}$, limit L/360 for brittle finishes.",
     figure="p. 3, Figure Q1: plans, section A–A and braced bay.", src="claude", checked=False)),
 sec("Q2 Rooftop crane boom", (5, 6),
   q("CE3166 Tut 1 Q2",
     r"A 9 m crane boom on a rooftop is supported at A and B (6 m apart) and overhangs 3 m to C. Self-weight 25 kN/m, "
     r"imposed load 40 kN/m, lifting machinery and counter mass 100 kN at 3 m from A, gondola with workers 300 kN "
     r"(occupancy) at C. Find (a) the design load for support A, (b) for support B and (c) the maximum bending moment "
     r"in the boom.",
     r"**(a) max compression 323 kN, max uplift 163 kN · (b) $R_B = 1375\ \mathrm{kN}$ · (c) hogging at B 1772 kNm "
     r"(sagging only 547 kNm).**",
     r"Single-source principle: the boom's self-weight takes one factor along its length. (a) Moments about B: "
     r"compression $6R_A = 1.35 \times 150 \times 3 + 1.5 \times 240 \times 3 + 1.35 \times 100 \times 3 - 1.35 "
     r"\times 75 \times 1.5$; uplift $6R_A = 1.0 \times 150 \times 3 + 1.0 \times 100 \times 3 - 1.0 \times 75 \times "
     r"1.5 - 1.5 \times 120 \times 1.5 - 1.5 \times 300 \times 3$. (b) Every load raises $R_B$: $6R_B = 1.35 \times 225 "
     r"\times 4.5 + 1.5 \times 360 \times 4.5 + 1.35 \times 100 \times 3 + 1.5 \times 300 \times 9$. (c) $M_B = 1.35 "
     r"\times 75 \times 1.5 + 1.5 \times 120 \times 1.5 + 1.5 \times 300 \times 3$. (a) is the official partial "
     r"solution; (b)–(c) worked here.", figure="p. 5, Figure Q2.", src="claude")),
]}

STLQ[D["T2"]] = {"code": "CE202", "title": "Steel practice · Tut 2 Section classification", "sections": [
 sec("Q1 Welded box 450×330 (10 mm plates, S275)", (1, 34),
   q("CE3166 Tut 2 Q1",
     r"A supplier offers the welded box section of Figure Q1 (S275 plates 10 mm thick: two 450 mm webs 330 mm apart, "
     r"flanges 530 mm wide with 100 mm outstands, 10 mm welds) for a beam-column. Is it slender under (a) axial "
     r"compression only, (b) major-axis (y–y) bending only, (c) minor-axis (z–z) bending only, (d) 2000 kN axial "
     r"compression with major-axis bending?",
     r"**(a) Class 4 (webs $c/t = 43 > 42\varepsilon = 38.6$) · (b) Class 2 (webs Class 1, internal flange Class 2) · "
     r"(c) Class 4 (webs in uniform compression) · (d) Class 3 ($\psi = -0.258$, web limit 66).**",
     r"$\varepsilon = 0.92$. Internal flange $c/t = 33$: between $33\varepsilon = 30.4$ and $38\varepsilon = 35.0$ → "
     r"Class 2 in compression, Class 1 in bending ($72\varepsilon = 66.2$). Outstands $c/t = 8.0 < 9\varepsilon = 8.28$ "
     r"→ Class 1. (d) $\alpha = \tfrac12[1 + N/(2ct_wf_y)] > 1$ → not Class 2; $\psi = 2N/(Af_y) - 1$ with $A = 19\,600\ "
     r"\mathrm{mm^2}$; Class 3 limit $42\varepsilon/(0.67 + 0.33\psi) = 66 > 43$.", figure="p. 1, Figure Q1.")),
 sec("Q2 Column 254×254×73 S355 under $N + M_y$", (35, 41),
   q("CE3166 Tut 2 Q2",
     r"From Tutorial 1, column G1 carries the ULS compression plus a major-axis moment from the eccentric beam "
     r"reaction (Fig. Q2). Classify a 254×254×73 UC in S355 using the design tables.",
     r"**$N = 1556\ \mathrm{kN}$ → flange Class 2 ($c/t = 7.77$, between $9\varepsilon = 7.29$ and $10\varepsilon = "
     r"8.10$), web Class 1 → overall Class 2.**",
     r"$\varepsilon = 0.81$; web $c/t = 23.3$, $\alpha \ge 1$ → limit $33\varepsilon = 26.7$ (fully compressed) → Class "
     r"1. Table check: $n = 1556/3310 = 0.47$, within the Class 2 range for this section.")),
]}

STLQ[D["T3"]] = {"code": "CE202", "title": "Steel practice · Tut 3 Compression members", "sections": [
 sec("Q1 Roof truss top chord (SHS, S355)", (1, 3),
   q("CE3166 Tut 3 Q1",
     r"An internal roof truss (Fig. 1: 14 m span, 15° pitch, purlins 6 m apart; joints A, B, D, G, H on the top "
     r"chord, C and E on the bottom chord) carries $G_k = 0.75 + 0.15\ \mathrm{kN/m^2}$ and $Q_k = 0.40\ "
     r"\mathrm{kN/m^2}$ applied as joint loads (Fig. 2); joints pinned. (a) Find the reaction at A. (b) Find the "
     r"design forces in top chord AB and bottom chord AC. (c) Select a square hollow section in S355 for AB.",
     r"**(a) $R_A = 78.9\ \mathrm{kN}$ · (b) AB 229 kN compression, AC 221 kN tension · (c) SHS 100×100×4 (hot "
     r"finished): $N_{\mathrm{b,Rd}} \approx 275\ \mathrm{kN}$ (90×90×4 gives only ≈ 213 kN).**",
     r"(a) $1.35 \times 0.90 + 1.5 \times 0.40 = 1.815\ \mathrm{kN/m^2}$ × 6 m = 10.89 kN/m along the slope; $R_A = "
     r"10.89 \times 7/\cos 15^\circ = 78.9$ (official). (b) Joint load $F_d = 39.5\ \mathrm{kN}$ ($F_d/2$ at A). "
     r"Joint A: $F_{AB}\sin 15^\circ = -(78.9 - 19.7)$ → $F_{AB} = -228.7$; $F_{AC} = -F_{AB}\cos 15^\circ = 220.9$. "
     r"(c) $L_{\mathrm{cr}} = 3.5/\cos 15^\circ = 3.62\ \mathrm{m}$; SHS 100×100×4: $A = 15.2\ \mathrm{cm^2}$, $i = "
     r"3.85\ \mathrm{cm}$, Class 1; $\bar\lambda = 3623/(38.5 \times 76.4) = 1.23$, curve a → $\chi = 0.51$ → $0.51 "
     r"\times 540 = 275\ \mathrm{kN}$ (utilisation 0.83). Check section properties against the blue book.",
     figure="p. 1, Figs 1–2.", src="claude", checked=False)),
 sec("Q2 12 m column with different restraints per axis (S275)", (4, 4),
   q("CE3166 Tut 3 Q2",
     r"A 12 m column in a shopping mall carries 650 kN dead and 900 kN imposed axial load; both ends are held in "
     r"position but free to rotate. A beam 3.5 m above the base holds it in position along the z–z axis (no restraint "
     r"to bending about y–y); a secondary beam at mid-height holds it along the y–y axis (no restraint to bending about "
     r"z–z). Select an economical UC in S275, stating the effective length of each segment about both axes and which "
     r"segment governs.",
     r"**$N_{\mathrm{Ed}} = 2228\ \mathrm{kN}$ · $L_{\mathrm{cr,y}}$ = 3.5 / 8.5 m, $L_{\mathrm{cr,z}}$ = 6 / 6 m → "
     r"the upper segment governs ($L_{\mathrm{cr,y}} = 8.5$, $L_{\mathrm{cr,z}} = 6.0\ \mathrm{m}$) · 305×305×118 UC: "
     r"$N_{\mathrm{b,z,Rd}} \approx 2450\ \mathrm{kN}$ (utilisation 0.91).**",
     r"Holding position along z stops displacement in the z direction, i.e. buckling about y–y. $f_y = 265$ ($t_f = "
     r"18.7\ \mathrm{mm}$), $\lambda_1 = 88.4$. z–z: $\bar\lambda = 6000/(77.7 \times 88.4) = 0.87$, curve c → $\chi = "
     r"0.62$ → $0.62 \times 3975 = 2450$. y–y: $\bar\lambda = 0.71$, curve b, $\chi = 0.78$ → 3100. 254×254×107 gives "
     r"≈ 1880 kN ✗ and 305×305×97 ≈ 2030 kN ✗. If you read the restraints the other way round ($L_{\mathrm{cr,z}} = "
     r"8.5\ \mathrm{m}$), you need about 356×368×153.", figure="p. 4, Figure Q2.", src="claude", checked=False)),
]}

STLQ[D["T4"]] = {"code": "CE202", "title": "Steel practice · Tut 4 Tension members", "sections": [
 sec("Q1 20 mm plate with M20 bolts (S275)", (1, 2),
   q("CE3166 Tut 4 Q1",
     r"A 20 mm S275 plate, 360 mm wide, is connected by M20 bolts (holes 22 mm) in three staggered lines (Figure Q1: "
     r"line 1 at 60, 180, 300 mm; line 2, 45 mm further in, at 120 and 240 mm; line 3, another 40 mm in, at 180 mm). "
     r"Find its tension capacity.",
     r"**$N_{\mathrm{pl,Rd}} = 1908\ \mathrm{kN}$, $A_{\mathrm{net,min}} = 5604\ \mathrm{mm^2}$ → $N_{\mathrm{u,Rd}} = "
     r"1880\ \mathrm{kN}$ → $N_{\mathrm{t,Rd}} = 1880\ \mathrm{kN}$.**",
     r"$f_y = 265$ ($t > 16$), $f_u = 410$. Paths: straight through line 1: $7200 - 3 \times 440 = 5880$; zig-zag lines "
     r"1–2 (5 holes, 4 diagonals of $s = 45$): $5675$; through all three lines (60–120–180(line 3)–240–300): $7200 - 5 "
     r"\times 440 + 2 \times 20 \times 45^2/240 + 2 \times 20 \times 40^2/240 = 5604$ — the minimum. $N_u = 0.9 \times "
     r"5604 \times 410/1.1$. (The path that governs is worked here; the sheet gives the final 1880 kN.)",
     figure="p. 1, Figure Q1.")),
 sec("Q2 Spliced angle, 420 kN, three M20 on one leg", (1, 2),
   q("CE3166 Tut 4 Q2",
     r"A tension diagonal in an S275 truss is spliced with a 160 × 15 mm S275 plate (Figure Q2) and must carry 420 "
     r"kN. Select an angle for a splice with one line of three M20 bolts on one leg at 90 mm pitch, and check the "
     r"splice plate.",
     r"**$\beta_3 = 0.63$ → $A_{\mathrm{net}} \ge 1797\ \mathrm{mm^2}$ → L100×100×12 ($A = 2270$, $A_{\mathrm{net}} = "
     r"2006$, $N_{\mathrm{u,Rd}} = 469\ \mathrm{kN}$; 100×100×10 gives only 1700 ✗) · plate: $N_{\mathrm{pl,Rd}} = "
     r"660$, $N_{\mathrm{u,Rd}} = 694\ \mathrm{kN}$ → OK.**",
     r"EC3-1-8 3.10.3: $p_1/d_0 = 90/22 = 4.1$, between 2.5 ($\beta_3 = 0.5$) and 5.0 ($\beta_3 = 0.7$) → $\beta_3 = 0.5 + 0.2 \times (90 - "
     r"55)/55 = 0.627$; $N_{\mathrm{u,Rd}} = \beta_3A_{\mathrm{net}}f_u/\gamma_{M2}$. Plate: $2400 \times 275$ and "
     r"$0.9 \times (2400 - 22 \times 15) \times 410/1.1$.", figure="p. 1, Figure Q2.", src="claude", checked=False)),
]}

STLQ[D["T5"]] = {"code": "CE202", "title": "Steel practice · Tut 5 Beams (restrained vs unrestrained)", "sections": [
 sec("10 m primary beam with two secondary-beam loads (S275)", (1, 3),
   q("CE3166 Tut 5 Q1",
     r"A 10 m simply supported S275 primary beam (Figure Q1) receives two secondary beams at 2.5 m and 5.5 m from one "
     r"end, each bringing 70 kN dead and 70 kN imposed load (self-weight negligible). Select an economical UB "
     r"(utilisation > 0.8) if (1) it is fully restrained against lateral-torsional buckling, (2) it is restrained "
     r"only by the secondary beams and the end connections. Check ULS and SLS.",
     r"**$P = 200\ \mathrm{kN}$, reactions 240/160 kN, $M_{\max} = 720\ \mathrm{kNm}$ · (1) 610×229×101: "
     r"$M_{\mathrm{c,Rd}} = 792\ \mathrm{kNm}$ (0.91), deflection 15.3 mm < L/360 = 27.8 ✓ · (2) 610×229×113: segment "
     r"5.5–10 m governs, $M_{\mathrm{b,Rd}} \approx 751\ \mathrm{kNm}$ (0.96).**",
     r"(1) official: $W_{\mathrm{pl,y}} = 2880\ \mathrm{cm^3}$, $f_y = 275$; shear fine. Deflection under $Q_k$: $\sum "
     r"Pa(3L^2 - 4a^2)/(48EI)$ with $a = 2.5$ and $4.5\ \mathrm{m}$, $I_y = 75\,800\ \mathrm{cm^4}$. (2) Segments 2.5 / "
     r"3.0 / 4.5 m. End segment 4.5 m, M 720 → 0, $C_1 = 1.77$. 610×229×113 ($f_y = 265$, $M_{\mathrm{pl}} = 869$; $I_z "
     r"= 3434$, $I_t = 111\ \mathrm{cm^4}$, $I_w = 3.18\ \mathrm{dm^6}$): $M_{\mathrm{cr}} = 2139\ \mathrm{kNm}$, "
     r"$\bar\lambda_{\mathrm{LT}} = 0.64$, rolled-section method (curve c, $\beta = 0.75$) → $\chi = 0.864$. Middle "
     r"segment (3 m, $\psi = 0.83$, $C_1 \approx 1.09$): 791 kNm. 610×229×101 gives 665 kNm on the end segment ✗ "
     r"(756 kNm with the f modification — marginal).", figure="p. 1, Figure Q1.", src="claude", checked=False)),
]}

STLQ[D["T6"]] = {"code": "CE202", "title": "Steel practice · Tut 6 Beam-columns: cross-section checks", "sections": [
 sec("Theory recap", (1, 11),
   ("md", "Plastic interaction for Class 1–2, linear elastic for Class 3 (conservative for 1–2)."),
 ),
 sec("Q1 Portal column, N 160 kN, M 530 kNm (S355)", (12, 17),
   q("CE3166 Tut 6 Q1 (cross-section)",
     r"A portal-frame column of 5.6 m clear height (Figure Q1b) has a pinned base and a laterally restrained top; the "
     r"rigid rafter connection delivers a factored axial force of 160 kN and moment of 530 kNm. Select an S355 section "
     r"and check its cross-section resistance.",
     r"**UKB 533×165×66 (Class 2, $n$ below the limit for moment reduction) satisfies cross-section strength.**",
     r"With $n = N_{\mathrm{Ed}}/N_{\mathrm{pl,Rd}}$ small, $M_{\mathrm{N,y,Rd}} = M_{\mathrm{pl,y,Rd}}$; check "
     r"shear separately.", figure="p. 2, Figure Q1b.")),
 sec("Q2 UC 254×254×73 S275 chord (800 kN + 200 kN mid-span + 100 kNm end moments)", (18, 31),
   q("CE3166 Tut 6 Q2 (cross-section)",
     r"A 6 m truss chord, a 254×254×73 UC in S275 with simple end connections, carries 800 kN axial force, a 200 kN "
     r"mid-span transverse load and 100 kNm end moments (Figure Q2). Check its cross-section capacity.",
     r"**Class 1; $V_{\mathrm{pl,Rd}} = 406 > 100\ \mathrm{kN}$ (low shear); $N_{\mathrm{pl,Rd}} = 2560\ \mathrm{kN}$, "
     r"$M_{\mathrm{pl,y,Rd}} = 273\ \mathrm{kNm}$; mid-span $M = 200\ \mathrm{kNm}$ · linear interaction 0.31 + 0.73 > 1 "
     r"✗, but the plastic check $M_{\mathrm{N,y,Rd}} = 211 \ge 200\ \mathrm{kNm}$ ✓.**",
     r"$n = 800/2560 = 0.313 > 0.25$ → $M_{\mathrm{N,y,Rd}} = M_{\mathrm{pl,y,Rd}}(1 - n)/(1 - 0.5a)$. Mid-span "
     r"moment $= 200 \times 6/4 - 100$.", figure="p. 3, Figure Q2.")),
]}

STLQ[D["T6b"]] = {"code": "CE202", "title": "Steel practice · Tut 6 part 2 Beam-columns: member buckling", "sections": [
 sec("Q1 Portal column with restraint 1.6 m below the top", (1, 52),
   q("CE3166 Tut 6 Q1 (buckling)",
     r"For the portal column of Q1 (N 160 kN, M 530 kNm at the top, pinned base, 5.6 m), select another S355 section "
     r"and check its buckling resistance if an intermediate lateral restraint is added 1.6 m below the top.",
     r"**UKB 533×210×82: top segment interaction 0.49 / 0.74 ≤ 1, bottom segment 0.39 / 0.64 ≤ 1 → adequate.**",
     r"Check each segment with equations 6.61/6.62, its own $L_{\mathrm{cr}}$, $C_1$ from the moment shape and $k$ "
     r"factors from Annex B.")),
 sec("Q2 UC 254×254×73 chord", (53, 86),
   q("CE3166 Tut 6 Q2 (buckling)",
     r"Check the buckling resistance of the 254×254×73 chord of Q2. Discuss: how would axial tension change the "
     r"checks; how do you choose $C_1$; which equation gives the $C_m$ factors?",
     r"**Class 1, buckling resistance adequate (Annex B k-factors, $C_m$ from the moment shape).** Axial tension "
     r"removes flexural buckling and reduces LTB risk.", "")),
]}

STLQ[D["T7"]] = {"code": "CE202", "title": "Steel practice · Tut 7 Plate girder (12 m, S275)", "sections": [
 sec("(a)–(b) Actions and the largest UB", (1, 20),
   q("CE3166 Tut 7 (a)–(b)",
     r"A 12 m simply supported S275 girder, laterally and torsionally restrained, carries three point loads ($G_k = "
     r"203.7$, $Q_k = 350\ \mathrm{kN}$ at 3.5, 6.0 and 8.5 m) and distributed loads $g_k = 14.8$ (including 4 kN/m "
     r"self-weight), $q_k = 20\ \mathrm{kN/m}$. (a) Draw the shear and moment diagrams and find the maximum deflection. "
     r"(b) Check shear, moment and deflection if the largest UB, 1016×305×487, is used.",
     r"**UB 1016×305×487: Class 1, shear adequate, deflection under $Q_k$ $2.52 + 5.87 + 9.11 = 17.5\ \mathrm{mm} < "
     r"L/360 = 33.3\ \mathrm{mm}$ ✓, moment inadequate → a plate girder is needed.**",
     r"Design point load $1.35 \times 203.7 + 1.5 \times 350 = 800\ \mathrm{kN}$; $w = 1.35 \times 14.8 + 1.5 "
     r"\times 20 = 50\ \mathrm{kN/m}$ → $V_{\max} = 1.5 \times 800 + 50 \times 6 = 1500\ \mathrm{kN}$.",
     figure="p. 1, Figure Q1.")),
 sec(r"(c)–(d) Flange sizing ($h \le 1.8\ \mathrm{m}$, $b/t_f \approx 15$)", (21, 34),
   q("CE3166 Tut 7 (c)–(d)",
     r"(c) With the depth limited to 1.8 m, size the flange plates for moment ($b/t_f \approx 15$). (d) With a 10 mm "
     r"web, find the girder's self-weight and compare it with the UB's.",
     r"**$t_f = 30\ \mathrm{mm}$, 450 × 30 flanges with a 10 mm web → moment adequate; self-weight about 3.5 kN/m, "
     r"less than the UB's 4.8 kN/m.**",
     r"Flange force ≈ $M/(h - t_f)$; area $= 2 \times 450 \times 30 + 1740 \times 10 = 44\,400\ \mathrm{mm^2}$ → "
     r"$44\,400 \times 10^{-6} \times 78.5 = 3.5\ \mathrm{kN/m}$.")),
 sec("(e)–(f) Stiffener positions & shear buckling", (35, 47),
   q("CE3166 Tut 7 (e)–(f)",
     r"(e) Suggest positions for transverse stiffeners. (f) With a 10 mm web and 450 × 30 flanges, check the shear "
     r"resistance with those stiffener positions.",
     r"**Stiffeners at 0, 1.5, 3.5 and 6.0 m (and symmetrically), $d = 1740\ \mathrm{mm}$ · $V_{\max} = 1500\ "
     r"\mathrm{kN} < V_{\mathrm{pl,Rd}}$ ✓ · AB (a/d 0.86): $1500 < V_{\mathrm{bw,Rd}}$ ✓ · BC (a/d 1.15): $1425 > "
     r"V_{\mathrm{b,Rd}}$ ✗ → add a stiffener · CD (a/d 1.44): 525 ✓.**",
     r"Deflection in (a) uses $Q_k$ only: UDL + central load + the two symmetric loads.")),
 sec("(g)–(i) Patch loading & stiffeners", (48, 74),
   q("CE3166 Tut 7 (g)–(i)",
     r"(g) Without transverse stiffeners, check the web under the point loads for local buckling. (h) Can a pair of "
     r"120 × 10 mm plates (30 mm cope holes) stiffen the web at the point loads? (i) Can a pair of 80 × 10 mm plates "
     r"serve as intermediate stiffeners carrying no external load?",
     r"**(g) $F_{\mathrm{Rd}} < 800\ \mathrm{kN}$ → stiffeners needed · (h) 2 × 120×10: stiffness ✓, bearing ✓ (800 < "
     r"$F_{\mathrm{bc}}$), buckling ✓ · (i) 2 × 80×10: $I_{\mathrm{st}}$ requirement met ✓.**", "")),
]}

STLQ[D["T8w"]] = {"code": "CE202", "title": "Steel practice · Tut 8 Welds (extended end plate, 8 mm fillets)", "sections": [
 sec("Weld group: F 300 kN, M 200 kNm on 457×191×67 UB", (1, 43),
   q("CE3166 Tut 8 Q1(a)",
     r"An extended end plate (20 mm, Figure Q1) transfers a beam reaction $F = 300\ \mathrm{kN}$ and hogging moment "
     r"$M = 200\ \mathrm{kNm}$ from a 457×191×67 UB (S275) to a 406×178×54 UB column (S355), bolted with M20 grade "
     r"8.8 bolts and welded to the beam with 8 mm fillet welds all round. Taking the moment in the flanges and the shear "
     r"in the web, check the weld group.",
     r"**Simplified method: weld inadequate; directional method (less conservative): adequate.**",
     r"Flange welds carry $M/(h - t_f)$ as tension/compression; web welds carry the shear.",
     figure="p. 1, Figure Q1.")),
]}

STLQ[D["T8b"]] = {"code": "CE202", "title": "Steel practice · Tut 8 Bolts (M20 8.8 end plate)", "sections": [
 sec("Bolt tension from M and combined check", (1, 50),
   q("CE3166 Tut 8 Q1(b)–(c)",
     r"For the same connection: (b) find the maximum bolt tension due to M, with the centre of rotation at the "
     r"compression flange and bolt force proportional to distance from it; (c) check the bolts for combined shear and "
     r"tension.",
     r"**(b) top-row force $= M y_{\max}/\sum y^2$ · (c) tension resistance adequate, but combined shear + tension "
     r"inadequate for the top bolts → add bolts or use grade 10.9.**",
     r"Combined: $F_v/F_{\mathrm{v,Rd}} + F_t/(1.4F_{\mathrm{t,Rd}}) \le 1$. Bearing $30\ \mathrm{kN} < "
     r"F_{\mathrm{b,Rd}}$ ✓.")),
]}
