"""CE201 tutorial questions (CE3165 Tut 1–9) as q blocks. Statements are from the tutorial sheets in
materials/CE201 (scanned, read by OCR); answers from the official solutions unless marked otherwise.
Numbers are recomputed in tests/test_tutorial_answers.py."""
from utils.qblock import q
from utils.study_notes_ce201 import D


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


CONQ = {}

CONQ[D["T1"]] = {"code": "CE201", "title": "Concrete practice · Tut 1 Loads & cracked/uncracked sections", "sections": [
 sec("1.1 Design loads & patterns (G 25, Q 15 kN/m, two spans)", (2, 6),
   q("CE3165 Tut 1 Q1.1",
     r"A continuous beam supported at A, B and C has spans AB and BC and a uniform cross-section. The characteristic "
     r"loads on both spans are a dead load of 25 kN/m and an imposed load of 15 kN/m. (a) What are the maximum and "
     r"minimum design loads? (b) Which load arrangements give the maximum (i) shear force at A, (ii) hogging moment "
     r"over support B, (iii) sagging moment in span BC, (iv) reaction at B?",
     r"**(a) max $1.35G + 1.5Q = 56.25\ \mathrm{kN/m}$, min $1.0G = 25\ \mathrm{kN/m}$ · (b) (i) AB max, BC min · (ii) "
     r"both spans max · (iii) BC max, AB min · (iv) both spans max.**",
     r"$1.35 \times 25 + 1.5 \times 15 = 56.25$. Favourable dead load takes $\gamma_G = 1.0$ and no imposed load.")),
 sec("1.2 Cracking moment, curvature & steel stress", (7, 16),
   q("CE3165 Tut 1 Q1.2",
     r"Find the cracking moments of the two sections shown — (a) a 350 × 600 mm rectangle with 3H20 at $d = 520\ "
     r"\mathrm{mm}$ and (b) a T-section with 2H20 at $d = 420\ \mathrm{mm}$ — if $f_{\mathrm{ck}} = 30\ \mathrm{MPa}$ "
     r"($f_{\mathrm{ctm}} = 2.9\ \mathrm{MPa}$, $E_{\mathrm{cm}} = 33\ \mathrm{GPa}$, $E_s = 200\ \mathrm{GPa}$). Also "
     r"find the section curvature just before and just after cracking, and the corresponding steel stresses.",
     r"**(a) $M_{\mathrm{cr}} = 64.1\ \mathrm{kNm}$; $f_s$ 12.7 → 141 MPa; $\phi$ 0.30 → $1.74 \times 10^{-6}\ "
     r"\mathrm{mm^{-1}}$ · (b) $M_{\mathrm{cr}} = 32.8\ \mathrm{kNm}$; $f_s$ 12.8 → 131 MPa; $\phi$ 0.29 → $1.86 "
     r"\times 10^{-6}\ \mathrm{mm^{-1}}$.**",
     r"(a) Uncracked: $\alpha_e = 200/33 = 6.06$, $(\alpha_e - 1)A_s = 4715\ \mathrm{mm^2}$ → $x = 305\ \mathrm{mm}$, "
     r"$I = 6.52 \times 10^9\ \mathrm{mm^4}$, $M_{\mathrm{cr}} = f_{\mathrm{ctm}}I/(h - x) = 2.9 \times 6.52 \times "
     r"10^9/295$. Cracked: $\alpha_e\rho = 0.0311$ → $x = 114\ \mathrm{mm}$, $I = 1.11 \times 10^9\ \mathrm{mm^4}$. "
     r"(b) $x$ 198 → 66.7 mm, $I$ 3.42 → $0.53 \times 10^9\ \mathrm{mm^4}$. Cracking raises the steel stress about 10× "
     r"and the curvature about 6×.", figure="p. 7: sections (a) and (b).")),
]}

CONQ[D["T2"]] = {"code": "CE201", "title": "Concrete practice · Tut 2 Design for flexure", "sections": [
 sec("2.1 Non-standard section at collapse", (3, 6),
   q("CE3165 Tut 2 Q2.1",
     r"Find the moment at collapse of the non-standard section in Fig. Q-2.1 for sagging (compression on top) about a "
     r"horizontal axis; $f_{\mathrm{ck}} = 30\ \mathrm{MPa}$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$.",
     r"**$x = 167.4\ \mathrm{mm}$ ($C = T = 653\ \mathrm{kN}$), $M_{\mathrm{Rd}} \approx 164\ \mathrm{kNm}$.**",
     r"Strain compatibility: guess x, find each bar's strain and stress, iterate (200 → 150 → 167.4 mm) until the "
     r"concrete force equals the steel force.", figure="p. 3, Fig. Q-2.1.")),
 sec(r"2.2 Simply supported 8 m beam, $h \le 650\ \mathrm{mm}$", (8, 11),
   q("CE3165 Tut 2 Q2.2",
     r"A simply supported rectangular beam spans 8 m and carries a characteristic dead load (including self-weight) of "
     r"18 kN/m and an imposed load of 20 kN/m. Its overall depth is limited to 650 mm. (a) Find the minimum width if "
     r"it is singly reinforced, and the steel area. (b) Design the mid-span section for a 300 mm width. (c) Design it "
     r"for a 200 mm width. $f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$, cover to the bar centroid "
     r"45 mm.",
     r"**$w = 54.3\ \mathrm{kN/m}$, $M = 434.4\ \mathrm{kNm}$, $d = 605\ \mathrm{mm}$ · (a) $b \approx 237\ \mathrm{mm}$, "
     r"$A_s = 2014\ \mathrm{mm^2}$ · (b) $K = 0.132$, $z = 524$, $A_s = 1907\ \mathrm{mm^2}$ · (c) $K = 0.198 > K'$ → "
     r"$A'_s = 280$, $A_s \approx 1980\ \mathrm{mm^2}$.**",
     r"$w = 1.35 \times 18 + 1.5 \times 20$; $M = wL^2/8$. (a) $b = M/(0.167f_{\mathrm{ck}}d^2)$ with $z = 0.82d$.")),
 sec("2.3 Inverted L and T sections", (12, 13),
   q("CE3165 Tut 2 Q2.3",
     r"Find the reinforcement for the sections shown to resist a design sagging moment of 500 kNm (inverted L-section, "
     r"$b = 750$, $d = 500\ \mathrm{mm}$) and 350 kNm (inverted T-section with the web in compression, $b = 250$, "
     r"$d = 385\ \mathrm{mm}$); $f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$.",
     r"**L-section: $K = 0.089$, $z = 457$, $A_s = 2516\ \mathrm{mm^2}$ · T-section: $K = 0.315 > K'$ → doubly "
     r"reinforced, $A'_s \approx 1174$, $A_s \approx 2528\ \mathrm{mm^2}$.**",
     r"In the L-section the stress block ($0.8x$) stays within the flange, so it is designed as a rectangle.",
     figure="p. 12: the two sections.")),
 sec("2.4 Flanged beam capacity", (14, 16),
   q("CE3165 Tut 2 Q2.4",
     r"For the flanged beam of Fig. Q-2.4 ($f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$): (a) find the "
     r"maximum sagging resistance of the singly reinforced section for $x/d = 0.45$ and the tension steel (H25, $d = "
     r"600\ \mathrm{mm}$); (b) find the overall depth with 50 mm cover and 25 mm clear between rows; (c) with that "
     r"depth, find the maximum hogging moment of the singly reinforced section and the flange steel (H25, 50 mm clear "
     r"cover).",
     r"**(a) $M_{\mathrm{Rd}} = 1212\ \mathrm{kNm}$, $A_s = 5470\ \mathrm{mm^2}$ → 12H25 · (b) $h = 712.5\ \mathrm{mm}$ "
     r"· (c) web $b = 300$, $d = 650$: $M' = 0.167f_{\mathrm{ck}}bd^2 = 635\ \mathrm{kNm}$, $A_s = 2740\ "
     r"\mathrm{mm^2}$ → 6H25.**", "", figure="p. 14, Fig. Q-2.4.")),
]}

CONQ[D["T3"]] = {"code": "CE201", "title": "Concrete practice · Tut 3 Design for shear", "sections": [
 sec(r"3.1 300 × 700 beam, 3H25, $f_{\mathrm{ck}}$ 35", (3, 6),
   q("CE3165 Tut 3 Q3.1",
     r"The reinforced section of Fig. Q-3.1 ($b_w = 300\ \mathrm{mm}$, $d = 645\ \mathrm{mm}$, 3H25 with $A_s = 1470\ "
     r"\mathrm{mm^2}$) is in sagging, $f_{\mathrm{ck}} = 35\ \mathrm{MPa}$. (a) Find the maximum design shear it can "
     r"carry (i) without and (ii) with shear reinforcement. (b) Find the links needed for a design shear of (i) 100 kN "
     r"and (ii) 500 kN.",
     r"**(a)(i) $V_{\mathrm{Rd,c}} = 108\ \mathrm{kN}$ · (ii) $V_{\mathrm{Rd,max}} = 1048\ \mathrm{kN}$ ($\theta = "
     r"45^\circ$) · (b)(i) 100 kN < 108 kN → minimum links H8@350 · (ii) H16 two-leg @200.**",
     r"$k = 1 + \sqrt{200/645} = 1.56$, $\rho = 0.0076$. Minimum $A_{\mathrm{sw}}/s = 0.08\sqrt{f_{\mathrm{ck}}}b_w/"
     r"f_{\mathrm{yk}} = 0.284$, spacing $\le 0.75d = 484\ \mathrm{mm}$.", figure="p. 5, Fig. Q-3.1.")),
 sec("3.2 Links along a simply supported beam", (7, 12),
   q("CE3165 Tut 3 Q3.2",
     r"The beam of Fig. Q-3.2 carries a characteristic dead load of 16 kN/m (including self-weight) and an imposed "
     r"load of 30 kN/m, with the bending steel shown. (a) Check shear at the face of the support. (b) Find the spacing "
     r"of H10 U-links at 0.65 m, 1 m and 2.5 m from the support centre lines. $f_{\mathrm{yk}} = 500$, "
     r"$f_{\mathrm{ck}} = 25\ \mathrm{MPa}$; the anchorage length of the longitudinal bars is 1 m.",
     r"**$w = 66.6\ \mathrm{kN/m}$ · 0.65 m ($V = 223\ \mathrm{kN}$): H10@125 · 1.0 m (200 kN): H10@150 · 2.5 m "
     r"(100 kN < $V_{\mathrm{Rd,c}} = 116\ \mathrm{kN}$): minimum H10@350.**",
     r"$w = 1.35 \times 16 + 1.5 \times 30$. Where the bars are not yet fully anchored, use only the anchored area in "
     r"$\rho$ for $V_{\mathrm{Rd,c}}$.", figure="p. 8, Fig. Q-3.2.")),
 sec(r"3.3 Flanged beam, 8 m span, $w = 174\ \mathrm{kN/m}$", (13, 17),
   q("CE3165 Tut 3 Q3.3",
     r"A beam spans 7 m face to face (effective span 8 m) with the flanged section of Fig. Q-3.3 ($b_w = 350$, $d = "
     r"775\ \mathrm{mm}$, 6H32 in two layers running to the supports). It carries a characteristic dead load of 40 "
     r"kN/m (including self-weight) and an imposed load of 80 kN/m. $f_{\mathrm{yk}} = 500$, $f_{\mathrm{ck}} = 35\ "
     r"\mathrm{MPa}$. (a) Is the section big enough for the design shear? (b) Find the shear reinforcement at the "
     r"critical section. (c) Find where minimum shear reinforcement is enough.",
     r"**(a) $V$ at the face $609\ \mathrm{kN} < V_{\mathrm{Rd,max}} = 1469\ \mathrm{kN}$ ✓ · (b) $V$ at d from the "
     r"face 474 kN → H10 two-leg @100 · extra longitudinal tension needs ≈ $545\ \mathrm{mm^2}$.**",
     r"$w = 1.35 \times 40 + 1.5 \times 80 = 174\ \mathrm{kN/m}$; $V_{\mathrm{face}} = 174 \times 3.5$. (c) minimum "
     r"links where $V_{\mathrm{Ed}} \le V_{\mathrm{Rd,c}}$, measured from the support.",
     figure="p. 14, Fig. Q-3.3.")),
]}

CONQ[D["T4"]] = {"code": "CE201", "title": "Concrete practice · Tut 4 Cracking & deflection", "sections": [
 sec("4.2 8 m simply supported 300 × 600 beam, 3H25", (2, 7),
   q("CE3165 Tut 4 Q4.2",
     r"The simply supported beam of Fig. Q-4.2 (300 × 600 mm, 3H25) spans 8 m in an office building and carries an "
     r"imposed load of 25 kN/m plus self-weight ($25\ \mathrm{kN/m^3}$). $f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = "
     r"500\ \mathrm{MPa}$, $A_{s,\mathrm{prov}} = A_{s,\mathrm{reqd}}$, creep coefficient 2.0, $w_{\max} = 0.3\ "
     r"\mathrm{mm}$. (a) Find the steel stress just before and after cracking. (b) Check cracking by minimum steel "
     r"and bar size or spacing. (c) Check deflection by span/effective depth.",
     r"**(a) uncracked $x = 333.8$, $I = 6.98 \times 10^9$ → $M_{\mathrm{cr}} = 68.5\ \mathrm{kNm}$; cracked $x = "
     r"239.7$, $I = 4.14 \times 10^9\ \mathrm{mm^4}$ · (b) SLS $M = 96\ \mathrm{kNm}$ → $\sigma_s \approx 136\ "
     r"\mathrm{MPa}$, within Tables 7.2N/7.3N; $A_{s,\min} = 185 < 1470$ ✓ · (c) allowable l/d 16.1 > actual 14.3 ✓.**",
     "", figure="p. 3, Fig. Q-4.2.")),
 sec("4.3 One-way continuous slab, 100 mm, H10", (8, 11),
   q("CE3165 Tut 4 Q4.3",
     r"Fig. Q-4.3 shows the end span of a one-way continuous slab, 100 mm thick, effective span 3 m, carrying a "
     r"characteristic dead load (including self-weight) of $6\ \mathrm{kN/m^2}$ and an imposed load of $5\ "
     r"\mathrm{kN/m^2}$. H10 bars, 25 mm cover, $\gamma_G = 1.35$, $\gamma_Q = 1.5$, $f_{\mathrm{ck}} = 30$, "
     r"$f_{\mathrm{yk}} = 500\ \mathrm{MPa}$, quasi-permanent steel stress 310 MPa. (a) Find the mid-span bar spacing "
     r"to the nearest 25 mm (take $M = 0.075FL$). (b) Check cracking at mid-span by maximum bar size and spacing "
     r"($w_{\max} = 0.3\ \mathrm{mm}$, $E_s/E_{c,\mathrm{eff}} = 10$); suggest a fix if it fails. (c) Check deflection "
     r"by span/effective depth; can it be fixed by closer spacing without smaller bars?",
     r"**(a) $F = 46.8\ \mathrm{kN/m}$, $M = 10.5\ \mathrm{kNm/m}$, $A_s = 371$ → H10@200 (393) · (b) spacing limit ≈ "
     r"112 mm < 200 → use closer bars · (c) allowable ≈ $1.5 \times 24.8 = 37.2$ < actual $3000/70 = 42.9$ ✗ — more "
     r"steel can't fix it (the factor is capped at 1.5); deepen the slab.**",
     r"$F = (1.35 \times 6 + 1.5 \times 5) \times 3$; $d = 100 - 25 - 5 = 70\ \mathrm{mm}$.",
     figure="p. 8, Fig. Q-4.3.")),
]}

CONQ[D["T5"]] = {"code": "CE201", "title": "Concrete practice · Tut 5 Anchorage & laps", "sections": [
 sec("5.1 Bent-up H16 bars, poor bond", (3, 5),
   q("CE3165 Tut 5 Q5.1",
     r"Two H16 tension bars are bent up at 45° at the end of a simply supported beam (Fig. Q-5.1). Find the total bond "
     r"length from the start of the bend if the bars reach their design strength, and the straight length $l_s$ if "
     r"$r = 3\phi$. $f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$, poor bond, cover $c = c_1 = 55\ "
     r"\mathrm{mm}$, $b = 300\ \mathrm{mm}$.",
     r"**$f_{\mathrm{bd}} = 2.1\ \mathrm{MPa}$, $l_{\mathrm{b,rqd}} = 828\ \mathrm{mm}$ → with the $\alpha$ factors "
     r"$l_{\mathrm{bd}} \approx 542\ \mathrm{mm}$.**",
     r"$f_{\mathrm{bd}} = 2.25 \times 0.7 \times 0.21f_{\mathrm{ck}}^{2/3}/1.5 = 0.7 \times 0.315 \times 30^{2/3}$; "
     r"$l_{\mathrm{b,rqd}} = (\phi/4)(f_{\mathrm{yd}}/f_{\mathrm{bd}})$.", figure="p. 4, Fig. Q-5.1.")),
 sec("5.2 Curtailment of bars", (6, 9),
   q("CE3165 Tut 5 Q5.2",
     r"For the beam of Fig. Q-5.2 (20 kN/m, 8 m span, 4H16 bottom bars, H8@250 links, $b = 250$, $d = 450$, cover 30 "
     r"mm, good bond), find the distance s from A at which two of the bottom H16 bars can be curtailed, considering "
     r"bending, shear and anchorage. $f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$.",
     r"**$f_{\mathrm{bd}} = 3.0\ \mathrm{MPa}$, $l_{\mathrm{b,rqd}} = 580$, $l_{\mathrm{bd}} \approx 553\ "
     r"\mathrm{mm}$; s = the point where the two remaining bars resist M, moved back by the shift $a_l = z\cot\theta/2$ "
     r"and extended by $l_{\mathrm{bd}}$.**", "", figure="p. 6, Fig. Q-5.2.")),
 sec("5.3 Anchorage at a simple support", (10, 12),
   q("CE3165 Tut 5 Q5.3",
     r"The beam of Fig. Q-5.3 (300 × 800 mm, 2H32 bottom bars) is simply supported over an effective span of 9.6 m "
     r"and carries $g_k = 20\ \mathrm{kN/m}$ (including self-weight) and $q_k = 16\ \mathrm{kN/m}$; $f_{\mathrm{ck}} = "
     r"30$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$. (a) Find the vertical links for the shear at the face of the support "
     r"($\theta = 45^\circ$). (b) Find the force in the bottom bars at the face of the support from bending and shear. "
     r"(c) Can the bars be anchored over the support without bending? (good bond, 50 mm clear cover, ignore links in "
     r"the support).",
     r"**$w = 51\ \mathrm{kN/m}$ · (a) H10@200 · (b) bar stress ≈ 131 MPa · (c) required anchorage ≈ 300 mm, governed "
     r"by the minimum ($\approx 10\phi = 320\ \mathrm{mm}$), which fits within the support → straight bars OK.**",
     r"$w = 1.35 \times 20 + 1.5 \times 16 = 51$. At a support the force to anchor is $V_{\mathrm{Ed}}a_l/z$.",
     figure="p. 9, Fig. Q-5.3.")),
]}

CONQ[D["T6"]] = {"code": "CE201", "title": "Concrete practice · Tut 6 Load path & take-down", "sections": [
 sec("Slab → beam → column loads", (1, 8),
   q("CE3165 Tut 6 Q1",
     r"The part plan of a multi-storey residential block (Fig. Q-1) has a 150 mm slab with clay floor tiles on 10 mm "
     r"mortar screed, 400 × 600 mm beams, a 225 mm brick wall and 5 mm continuous glazing. Find the characteristic and "
     r"design ultimate loads for the slab and for beams D1–D2 and D1–E1, taking the tiles as $0.5\ \mathrm{kN/m^2}$ "
     r"and partitions as $1.0\ \mathrm{kN/m^2}$ (concrete $25$, screed $21$, brick $19\ \mathrm{kN/m^3}$).",
     r"**D1–D2: slab share 8.19 + beam and wall 16.90 = 25.09 kN/m characteristic → design $1.35 \times 25.09 = 33.9\ "
     r"\mathrm{kN/m}$ (the slide prints 29.42) · D1–E1: 41.76 kN point load from the secondary beam + 10.99 kN/m → "
     r"107.7 kN characteristic, 145.4 kN design.**",
     r"Slab strip 1.5 m wide: $0.15 \times 1.5 \times 25 + 1.5 \times 1.5 + 0.01 \times 21 \times 1.5 = 8.19$. "
     r"Beam: $0.4 \times 0.45 \times 25 + 0.225 \times 2.9 \times 19 = 16.90$. Secondary beam onto D1–E1: $(16.38 + "
     r"4.5) \times 4/2 = 41.76\ \mathrm{kN}$; own line load $0.4 \times 0.65 \times 25 + 0.225 \times 1 \times 19 + "
     r"0.005 \times 1.69 \times 25 = 10.99$. Only dead loads are listed on the slide.",
     figure="p. 3, Fig. Q-1: part plan and section A–A.")),
]}

CONQ[D["T67"]] = {"code": "CE201", "title": "Concrete practice · Tut 6–7 Continuous beams & slabs", "sections": [
 sec("6.1 Moment envelope & redistribution", (1, 10),
   q("CE3165 Tut 7 Q6.1",
     r"The continuous beam of Fig. Q-6.1 (spans 6 m and 7 m, constant section) carries $G_k = 25\ \mathrm{kN/m}$ "
     r"(including self-weight) and $Q_k = 10\ \mathrm{kN/m}$. Derive the elastic bending moment and shear envelopes, "
     r"then (a) the 70 % elastic envelopes and (b) the envelopes after 10 % redistribution of the support moment.",
     r"**Max load 48.75, min 33.75 kN/m · elastic $M_B$: −206.4 (both spans max), −181.9 (AB min), −167.5 kNm (BC "
     r"min) · 10 % redistribution → $M_B = -185.8\ \mathrm{kNm}$, $V_A = 115.3$, $V_{B,\mathrm{left}} = 177.2\ "
     r"\mathrm{kN}$.**",
     r"Three-moment equation: $2M_B(6 + 7) = -\tfrac14(w_1 \cdot 6^3 + w_2 \cdot 7^3)$. LC1: $V_A = 111.85$, $V_B = "
     r"180.65$ / $170.63\ \mathrm{kN}$. Check the redistribution limit $\delta \ge k_1 + k_2x_u/d$.",
     figure="p. 3, Fig. Q-6.1.")),
 sec(r"6.2 Design a two-span beam ($f_{\mathrm{ck}}$ 30, $f_{\mathrm{yk}}$ 500)", (11, 24),
   q("CE3165 Tut 7 Q4",
     r"The two-span continuous beam of Fig. Q-4 (two 8 m spans, flanged section) carries $g_k = 20\ \mathrm{kN/m}$ "
     r"(including self-weight) and $q_k = 24\ \mathrm{kN/m}$; $f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = 500\ "
     r"\mathrm{MPa}$; cover to bar centre 60 mm (bottom) and 40 mm (top). (a) Find the design moment and shear "
     r"envelopes. (b) Design for flexure and shear and sketch the steel. (c) Check deflection.",
     r"**Mid-span 324 kNm → 3H25 · interior support −360 kNm → $K = 0.127 > K' = 0.123$ (after redistribution) → "
     r"$A'_s$ 2H25, $A_s$ 4H25 · shear: interior 262 kN → H10@125, exterior 173 kN → H10@150, elsewhere H10@400 · "
     r"deflection by l/d ✓.**", "", figure="p. 12, Fig. Q-4.")),
 sec("6.3 Cantilevering roof slab", (25, 32),
   q("CE3165 Tut 7 Q6.3",
     r"Fig. Q-6.3 shows a one-way roof slab spanning 4.0 m and cantilevering 1.5 m over a wall. Choose a slab depth, "
     r"estimate the dead load and design the slab for an imposed load of $2\ \mathrm{kN/m^2}$ ($f_{\mathrm{ck}} = 30$, "
     r"$f_{\mathrm{yk}} = 500\ \mathrm{MPa}$); sketch the steel.",
     r"**150 mm slab, 20 mm cover: $G = 3.75$, $w_{\max} = 8.06$, $w_{\min} = 5.06\ \mathrm{kN/m^2}$ · mid-span $M = "
     r"13.3\ \mathrm{kNm/m}$ → $A_s = 258$ → H12@300 (377) · shear 18.4 kN < $V_{\mathrm{Rd,c}} = 62\ \mathrm{kN}$, no "
     r"links · l/d: span 32.3 < 39.2 ✓, cantilever 12.1 < 15.7 ✓.**",
     r"$d = 150 - 20 - 6 = 124\ \mathrm{mm}$; $K = 0.0287$, $z = 0.95d = 118$. Pattern loads: max on the span with min "
     r"on the cantilever, and the reverse; the minimum factor here is 1.35 on G alone (the slide's $w_{\min}$). Check "
     r"cover and concrete grade for durability.", figure="p. 22, Fig. Q-6.3.")),
 sec("6.4 Two-way slab panel", (29, 32),
   q("CE3165 Tut 7 Q6.4",
     r"The two-way floor of Fig. Q-6.4 is a 150 mm slab on 350 mm wide beams, designed for an imposed load of $3.75\ "
     r"\mathrm{kN/m^2}$ and a dead load (including self-weight) of $4.0\ \mathrm{kN/m^2}$. For the panel between "
     r"gridlines A, B, 2 and 3 ($l_x = 7.3$, $l_y = 8.5\ \mathrm{m}$): (a) find and sketch the short-span bending "
     r"steel, (b) the torsion steel at the corners, (c) check deflection. $f_{\mathrm{ck}} = 30$, $f_{\mathrm{yk}} = "
     r"500\ \mathrm{MPa}$, 20 mm cover.",
     r"**$n = 11.03\ \mathrm{kN/m^2}$, $l_y/l_x = 1.16$ · (a) edge $m = 0.0462nl_x^2 = 27.1\ \mathrm{kNm/m}$ → $A_s "
     r"= 528$ → H10@150; mid-span $0.0349nl_x^2 = 20.5$ → $A_s = 396$ → H10@200 ($393\ \mathrm{mm^2/m}$) · (b) corners $148.5\ "
     r"\mathrm{mm^2/m}$ → H10@300 · (c) actual l/d 58.4 > allowable 52.7 ✗.**",
     r"$n = 1.35 \times 4.0 + 1.5 \times 3.75$; coefficients from the two-way slab table (one short edge "
     r"discontinuous). $d = 150 - 20 - 5 = 125\ \mathrm{mm}$. Deflection: $\rho = 393/125\,000 = 0.00314$, $\rho_0 = 0.00548$ → basic "
     r"l/d 36.6, × K 1.5 = 54.9, × 7/7.3 for a span over 7 m = 52.7 (the OCR of the slide shows 34.02 for the basic "
     r"value; 54.92/1.5 = 36.6).", figure="p. 29, Fig. Q-6.4.")),
]}

CONQ[D["T8"]] = {"code": "CE201", "title": "Concrete practice · Tut 8 Columns & pad bases", "sections": [
 sec("7.1 Classify columns (braced/unbraced, slenderness)", (1, 6),
   ("eq", r"\lambda = \frac{l_0}{i},\qquad \lambda_{lim} = \frac{20ABC}{\sqrt n},\ n = \frac{N_{Ed}}{A_cf_{cd}}"),
   q("CE3165 Tut 8 Q7.1",
     r"Considering only in-plane behaviour, classify columns AB and CH of the frame in Fig. Q-7.1 as short or slender "
     r"if the frame is (a) braced and (b) unbraced. All members are 300 mm deep normal to the frame; $g_k = 30$, "
     r"$q_k = 10\ \mathrm{kN/m}$, $f_{\mathrm{ck}} = 40\ \mathrm{MPa}$.",
     r"**AB: braced $l_0 = 3105$, $\lambda = 21.5 < \lambda_{\lim} = 113$ → short; unbraced $l_0 = 7660$, $\lambda = 53 > "
     r"46.5$ → slender · CH: braced $l_0 = 3013$, $\lambda = 26 < 48.1$ → short; unbraced $l_0 = 6246$, $\lambda = 54 > "
     r"19.9$ → slender.**",
     r"AB: $k_1 = 0.914$, $k_2 = 0.386$, $N_{\mathrm{Ed}} = 183\ \mathrm{kN}$, $n = 0.0538$; braced $l_0 = 0.5l\sqrt{"
     r"(1 + k_1/(0.45 + k_1))(1 + k_2/(0.45 + k_2))}$. CH: $k = 0.1$ (minimum), $N_{\mathrm{Ed}} = 805\ \mathrm{kN}$, "
     r"$n = 0.296$. $\lambda = 3.46l_0/h$; limits $26.2/\sqrt n$ (braced) and $10.8/\sqrt n$ (unbraced), the course's "
     r"simplified values.", figure="p. 3, Fig. Q-7.1.")),
 sec("7.2 Short braced column, uniaxial & biaxial", (7, 14),
   q("CE3165 Tut 8 Q7.2",
     r"A short braced 400 × 500 mm column carries at ULS (i) $N = 3000\ \mathrm{kN}$, $M_y = 390$, $M_z = 0$; (ii) $N "
     r"= 2000$, $M_y = 360$, $M_z = 240$; (iii) $N = 2000$, $M_y = 400$, $M_z = 350\ \mathrm{kNm}$. Design the "
     r"longitudinal and lateral steel ($f_{\mathrm{ck}} = 35$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$, cover to bar "
     r"centres 50 mm).",
     r"**(ii) 6H32 ($4830\ \mathrm{mm^2}$) · (iii) enhanced single-axis moment $M' = M_z + \beta(h'/b')M_y \approx 581\ "
     r"\mathrm{kNm}$ → read $A_s$ from the N–M chart.**",
     r"Use the interaction chart for each case; for biaxial bending design for the enhanced moment about the more "
     r"critical axis ($\beta = 0.743$ here), or check $(M_z/M_{\mathrm{Rdz}})^a + (M_y/M_{\mathrm{Rdy}})^a \le 1$.")),
 sec("7.3 Pad base 3 × 3 × 0.4 m (N 1800 kN, M 540 kNm)", (15, 20),
   q("CE3165 Tut 8 Q7.3",
     r"A 400 × 400 mm column sits centrally on a 400 mm thick square base 3 m wide, carrying an ultimate axial load of "
     r"1800 kN and moment of 540 kNm parallel to one side. The base has H20@150 both ways. (i) Check the bending steel "
     r"in the direction of the moment. (ii) Check vertical and punching shear; suggest a fix if it fails. 40 mm clear "
     r"cover, $f_{\mathrm{ck}} = 35$, $f_{\mathrm{yk}} = 500\ \mathrm{MPa}$.",
     r"**Pressures 320 / 80 kPa · $M$ at the column face 723 kNm → $A_s = 5010 < 6270\ \mathrm{mm^2}$ ✓ · beam shear "
     r"at d: $V_{\mathrm{Ed}} = 804\ \mathrm{kN}$ vs $V_{\mathrm{Rd,c}}$; punching at 2d with $v_{\mathrm{Rd,c}} \approx "
     r"0.58\text{–}0.59\ \mathrm{MPa}$.**",
     r"$p = N/A \pm 6M/B^3 = 200 \pm 120$; at the face $p = 80 + 240 \times 1.7/3 = 216$; $M = 216 \times 3 \times "
     r"1.3^2/2 + (320 - 216) \times 3 \times 1.3/2 \times \tfrac23 \times 1.3$; $d = 340\ \mathrm{mm}$, $z = 0.947d$. "
     r"If shear fails, thicken the base.")),
]}

CONQ[D["T9"]] = {"code": "CE201", "title": "Concrete practice · Tut 9 Prestressed design", "sections": [
 sec("8.1 Class 1 I-beam, 20 m span — minimum $P_0$", (1, 6),
   q("CE3165 Tut 9 Q8.1",
     r"A Class 1 prestressed I-beam (Fig. Q-8.1) spans 20 m simply supported and carries an imposed dead load of 4.5 "
     r"kN/m and live load of 10 kN/m. $f_{\mathrm{ck}}(t) = 25$, $f_{\mathrm{ck}} = 40\ \mathrm{MPa}$, $A_c = 324\,400\ "
     r"\mathrm{mm^2}$, $I = 38.1 \times 10^9\ \mathrm{mm^4}$, $y_b = 445\ \mathrm{mm}$, minimum cover to the tendon "
     r"centroid 120 mm, $\eta = 0.8$. (a) Find the minimum initial prestress at mid-span. (b) Find it if the live load "
     r"rises to 15 kN/m.",
     r"**(a) $P_0 = 2400\ \mathrm{kN}$ at $e_0 = 325\ \mathrm{mm}$ · (b) $P_0 \approx 2930\ \mathrm{kN}$ at $e_0 = 325\ "
     r"\mathrm{mm}$.**",
     r"Self-weight $0.3244 \times 25 = 8.11\ \mathrm{kN/m}$ → $M_{\min} = 405.5\ \mathrm{kNm}$; $M_{\max} = 1130.5$ "
     r"(live 10) or 1380.5 kNm (live 15). Limits −1/15 MPa at transfer, 0/24 MPa in service; $k_t = 211.6$, $k_b = "
     r"263.9\ \mathrm{mm}$; $e_{\max} = 445 - 120 = 325$. Governing inequality (iv): $e_0 \ge -263.9 + M_{\max}/"
     r"(0.8P_0)$ → $P_0 = M_{\max}/(0.8 \times 588.9)$. Part (b) is worked from the official inequalities; the slide's "
     r"final value isn't legible.", figure="p. 3, Fig. Q-8.1.", src="claude")),
 sec("8.2 Pre-tensioned beam, 28 m, 15.7 mm strands", (7, 8),
   q("CE3165 Tut 9 Q8.2",
     r"A pre-tensioned beam (Fig. Q-8.2) spans 28 m simply supported and carries 4 kN/m dead load besides its own "
     r"weight and 10 kN/m imposed load. $P_0 = 2610\ \mathrm{kN}$ from 14 × 15.7 mm strands at constant $e_0 = 791\ "
     r"\mathrm{mm}$. Transfer is at 7 days; dead and quasi-permanent load ($\psi_2 = 0.3$) at 28 days. $f_{\mathrm{ck}}"
     r"(t) = 25$, $f_{\mathrm{ck}} = 40\ \mathrm{MPa}$, $A_c = 508\,000\ \mathrm{mm^2}$, $I = 134 \times 10^9\ "
     r"\mathrm{mm^4}$, $\eta = 0.8$, $\phi(\infty, 7) = 2$, $\phi(\infty, 28) = 1.6$. Check (a) the camber from "
     r"prestress and self-weight at transfer and (b) the SLS deflection.",
     r"**(a) $-47.9 + 24.1 = -23.8\ \mathrm{mm}$ (upward) · (b) $-115.0 + 87.0 = -28\ \mathrm{mm}$, within $L/250 = "
     r"112\ \mathrm{mm}$ ✓.**",
     r"$E_{\mathrm{cm}}(7) = 22[(25 + 8)/10]^{0.3} = 31.5$, $E_{\mathrm{cm}} = 35.2\ \mathrm{GPa}$. Prestress camber "
     r"$P_0e_0L^2/(8EI) = 47.9\ \mathrm{mm}$; self-weight ($12.7\ \mathrm{kN/m}$) $5wL^4/(384EI) = 24.1$. Long term: "
     r"$47.9 \times 0.8 \times (1 + 2) = 115.0$ up; quasi-permanent $19.7\ \mathrm{kN/m}$ at 35.2 GPa: $33.4 \times (1 "
     r"+ 1.6) = 87.0$ down.", figure="p. 8, Fig. Q-8.2.")),
]}
