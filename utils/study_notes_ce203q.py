"""CE203 tutorial questions (CE3115 slopes & ERSS problem sets, assignments, quiz, exam; CE3116 foundations) as
q blocks. Statements are from the question sheets in materials/CE203; answers from the official solutions unless
marked otherwise. Numbers are recomputed in tests/test_tutorial_answers.py."""
from utils.qblock import q
from utils.study_notes_ce203 import D, EC7


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


GEOQ = {}

# ======================================================================== CE3115 slopes (OAP)
GEOQ[D["T1"]] = {"code": "CE203", "title": "Slopes 1 · Infinite slopes (CE3115 Tutorial 1)", "sections": [
 sec("Q1 Infinite slopes A–E", (2, 7),
   ("eq", r"F = \frac{c' + \sigma'_v\cos^2\beta\tan\phi'}{\sigma_v\cos\beta\sin\beta}\quad(\text{parallel seepage, slip plane at depth } z)"),
   q("CE3115 Tut 1 Q1",
     r"Five infinite slopes inclined at $\beta = 18^\circ$ in sandy soil ($\phi' = 30^\circ$, $\gamma_{\mathrm{dry}} = "
     r"16.5$, $\gamma_{\mathrm{sat}} = 20\ \mathrm{kN/m^3}$) are checked on slip planes 1, 3 and 5 m below the "
     r"surface, with seepage parallel to the slope and $\gamma_w = 10\ \mathrm{kN/m^3}$ (no EC7 factors): A dry; B "
     r"water table 1 m below the surface; C water table at the surface; D as A/B but with $c' = 5\ \mathrm{kPa}$; E with "
     r"a clay seam ($c' = 0$, $\phi' = 25^\circ$) at 3 m. Calculate the factors of safety and comment on the effect of "
     r"(i) slip depth in a dry slope, (ii) water, (iii) a rising water table, (iv) cohesion and (v) a weak seam.",
     r"**A: $F = 1.78$ at every depth · B: 1.78 / 1.15 / 1.04 · C: 0.89 at every depth · D: 1.74 / 1.17 / 1.06 · "
     r"E (seam at 3 m): 0.72.**",
     r"A dry cohesionless slope has $F = \tan\phi'/\tan\beta = 0.577/0.325 = 1.78$, independent of depth. Water lowers "
     r"F; with the water table at the surface $F \approx (\gamma'/\gamma_{\mathrm{sat}})\tan\phi'/\tan\beta \approx "
     r"\tfrac12$ of dry. Cohesion helps most at shallow depth (often ignored for conservatism). A weak seam governs — "
     r"check every interface with that layer's parameters.",
     figure="pp. 2–7: slope sketches A–E.")),
 sec("Q2 Sand over OC clay (EC7 DA1-C2)", (8, 10),
   q("CE3115 Tut 1 Q2",
     r"A long slope inclined at 14°–17° has 0–3 m medium dense sand ($\gamma = 16.5\ \mathrm{kN/m^3}$, $w = 20\,\%$, "
     r"$\phi' = 33^\circ$), 3–5 m overconsolidated clay ($\gamma = 16.5$, $w = 20\,\%$, $s_u = 40\ \mathrm{kPa}$, "
     r"$c' = 5\ \mathrm{kPa}$, $\phi' = 28^\circ$) and sandstone below 5 m. The water table was 2 m below ground at the "
     r"time of the investigation but rises close to the surface in prolonged rain. Using EC7 DA1-C2, check whether the "
     r"slope is stable, making conservative assumptions where needed.",
     r"**$\beta = 14^\circ$: F = 1.03 (3 m, sand) / 1.13 (3 m, clay) / 1.02 (5 m) → just OK · $\beta = 17^\circ$: "
     r"0.84 / 0.93 / 0.83 → unstable.**",
     r"Slow failure → effective stress. $\gamma_{\mathrm{sat}} = \gamma_{\mathrm{dry}}(1 + w) = 19.8$; worst case "
     r"water table at the surface; use the steepest local angle. Design strength: $\phi'_d = \tan^{-1}(\tan\phi'_k/1.25)$ "
     r"→ sand 33° → 27.5°, clay $c'$ 5 → 4 kPa and 28° → 23°.")),
]}

GEOQ[D["T2"]] = {"code": "CE203", "title": "Slopes 2 · Finite slopes: mass procedure, Taylor, Bishop (CE3115 Tutorial 2)", "sections": [
 sec("Q1 Seabed trench in soft clay", (2, 4),
   ("eq", r"F = \frac{c_u r^2\theta}{W d}\qquad\text{Taylor: } F = \frac{c_u}{N_s\gamma H},\quad H_{max} = \frac{c_u/\gamma_{cu}}{N_s\gamma}"),
   q("CE3115 Tut 2 Q1",
     r"A temporary seabed trench for a pipeline is cut in soft clay ($s_u = 17\ \mathrm{kPa}$, $c' = 12\ \mathrm{kPa}$, "
     r"$\phi' = 28^\circ$, $\gamma = 16\ \mathrm{kN/m^3}$) with 3 m deep sides at 60°. A trial circle has radius 5 m "
     r"subtending 66°; the sliding mass has area $8.1\ \mathrm{m^2}$ with its weight acting 2.03 m from the centre. "
     r"(a) Find the short-term factor of safety by the mass procedure for DA1-C1 and C2. (b) Find it from Taylor's chart "
     r"(hard layer at 50 m) for C1 and C2. (c) Compare and explain. (d) A contractor proposes 45° sides to allow a deeper "
     r"trench: assess the claim with Taylor's chart and DA1-C2.",
     r"**(a) C1 $F = 1.38$, C2 $F = 1.33$ · (b) C1 1.38, C2 1.33 ($N_s \approx 0.19$) · (c) identical, so the trial "
     r"circle is (close to) the critical one · (d) $H_{\max}$ ≈ 4.0 m at 60° and only 4.2 m at 45° ($N_s \approx 0.18$) "
     r"→ the claim is wrong; 60° needs less excavation.**",
     r"$M_R = c_ur^2\theta = 17 \times 25 \times 66\pi/180 = 489.5$; $M_D = 8.1 \times 16 \times 2.03 = 263.1$. "
     r"C1: $489.5/(1.35 \times 263.1) = 1.38$. C2: $(489.5/1.4)/263.1 = 1.33$.",
     figure="p. 2, Figure 1: trench section with the trial circle.")),
 sec("Q2 Two-layer natural slope — Simplified Bishop", (5, 9),
   ("eq", r"F = \frac{\sum\left[c'b + (W - ub)\tan\phi'\right]\dfrac{\sec\alpha}{1 + \tan\alpha\tan\phi'/F}}{\sum W\sin\alpha + M_N/R}"),
   q("CE3115 Tut 2 Q2",
     r"For the two-layered natural slope in Figure 2 (water table as a piezometric line), check the stability by the "
     r"Simplified Bishop method to EC7 DA1-C1 and DA1-C2.",
     r"**DA1-C1 $F = 0.94$ (fails) · DA1-C2 $F = 1.08$ → C1 governs.**",
     r"Slice the mass; C1 factors the driving $W\sin\alpha$ of positive-$\alpha$ slices by 1.35; C2 divides $c'$ and "
     r"$\tan\phi'$ by 1.25 in the numerator and in $n_{\alpha}$. Iterate F from 1.0.",
     figure="pp. 5–9, Figure 2: slope, layers, trial circle.")),
 sec("How to apply EC7 in Bishop", (10, 13),
   ("steps", ["Slices: boundaries at slip entry/exit, slope breaks, layer and water-table crossings, load edges.",
              r"C1: ×1.35 on W $\sin\alpha$ of slices with **positive** $\alpha$ (driving); negative-$\alpha$ "
              "slices (resisting) unfactored; variable unfavourable surcharge ×1.5, favourable ignored.",
              r"C2: W unfactored, surcharge ×1.3, $c'/1.25$ and $\tan\phi'/1.25$ in the numerator **and in "
              r"$n_{\alpha}$**.",
              "External loads/ponded water: add $M_N/R$ to the denominator (negative if restoring).",
              r"Start with $F = 1$, compute $n_{\alpha}$, iterate until F converges (usually 2–3 rounds)."]),
   EC7,
 ),
 sec("Ponded water & other details", (14, 15),
   ("md", r"Ponded water acts normal to the surface: vertical $F_{\mathrm{wV}} = \gamma_w h_w b$, horizontal "
          r"$F_{\mathrm{wH}} = \gamma_w h_w b \tan\beta$, applied at mid-slice; its moment about the centre goes in as "
          "$M_N/R$ (usually restoring at the toe)."),
 ),
]}

GEOQ[D["A1"]] = {"code": "CE203", "title": "Slopes 3 · River-bank Bishop analysis (CE3115 Assignment 1)", "sections": [
 sec("1a Trial circle with tension crack and surcharge", (3, 7),
   q("CE3115 Assignment 1 (a)",
     r"A river bank of two soil layers (Figure 1) carries a variable surcharge of 30–50 kPa on its crest; the water "
     r"table is a phreatic line, $\gamma_w = 10\ \mathrm{kN/m^3}$. For the given trial slip surface and centre, find "
     r"the factor of safety by the Simplified Bishop method to EC7 DA1-C1 and DA1-C2, assuming 3 m deep tension cracks "
     r"at the top of the slope. Show the slices, a calculation table and the working for one slice.",
     r"**DA1-C1 $F = 1.083$ · DA1-C2 $F = 1.248$** (±0.05 depending on slicing; 50 kPa surcharge).",
     r"Omit the slice inside the (dry) tension crack, so the surcharge length shrinks from 8.5 to 7 m; at least 9 slices; "
     r"ponded water included as point loads. Worked slice 7 (C1): $W = 3(19 \times 8.22 + 18 \times 2.25) = 590.1\ "
     r"\mathrm{kN/m}$, $\alpha = \sin^{-1}(13.5/26) = 31.3^\circ$; driving $1.35 \times 590.1\sin 31.3^\circ = 413.6$; "
     r"$S = 13 \times 3 + (590.1 - 10 \times 7.97 \times 3)\tan 28^\circ = 225.6$; $n_{\alpha}(F = 1) = 0.88$ → "
     r"$T \approx 199\ \mathrm{kN/m}$ (the slide multiplies 232.3 × 0.88 — a typo; the table value 199.5 is right). "
     r"Common mistakes: too few slices, splitting a slice top/bottom, no boundary at the layer interface, forgetting "
     r"ponded water or surcharge, water pressure in the crack, unreduced $\phi'$ in $n_{\alpha}$.",
     figure="p. 2, Figure 1: river bank section, layers, trial circle.")),
 sec("1b Bed erosion", (8, 10),
   q("CE3115 Assignment 1 (b)",
     r"Long-term bed erosion could deepen the river bed by 3 m (Figure 2). Using DA1-C1, check the bank, omitting the "
     r"affected slice and keeping the water level unchanged.",
     r"**F drops from 1.083 to 0.916 → unstable.**",
     r"Removing the toe slice removes resisting weight and its restoring ponded-water moment.")),
 sec("1c Falling water level", (11, 11),
   q("CE3115 Assignment 1 (c)",
     r"Without calculation, comment on how a drop in the river water level affects the stability of the bank.",
     r"**A drop of the river alone (rapid drawdown) lowers F; a drop of both river and water table (long term) usually "
     r"raises F.**",
     r"The ponded water gives a restoring moment that is lost on drawdown while pore pressures in the bank stay high. "
     r"If the water table in the bank also falls, the soil is lighter on the slip surface but $\sigma'$ rises, so F "
     r"usually increases.")),
]}

GEOQ[D["A2"]] = {"code": "CE203", "title": "Slopes 4 · Slope stabilisation options (CE3115 Assignment 2)", "sections": [
 sec("Stabilisation at four locations (SLIDE)", (3, 10),
   q("CE3115 Assignment 2",
     r"Pumping stations will be built at four locations along a river bank with different soil profiles. Using SLIDE "
     r"and EC7 DA1-C2: (a) check the existing slopes (Simplified Bishop, Spencer, GLE/Morgenstern–Price); (b) each "
     r"station sits on a 5 m wide footing (variable bearing pressure 50 kPa) with its outer edge 2 m from the crest — "
     r"choose and justify the most efficient stabilisation at each location (flattening, benching, buttressing, "
     r"horizontal drains modelled as a shift of the water table).",
     r"**F original → with surcharge → stabilised: L1 0.999 → 0.991 → buttress 1.041 · L2 1.060 → 0.925 → drains "
     r"1.057 · L3 1.014 → 0.881 → buttress + drain 1.013 · L4 1.358 → 1.084, no works needed.**",
     r"Strategy: check the existing slope, then add the surcharge; try drains first (only useful if the water table "
     r"lies inside the sliding mass — at L1 it is already outside, so drains are useless); then flattening, benching, "
     r"buttressing with the same cut/fill area, and combinations. At L3 (clay seam, very wide mass) flattening or "
     r"benching alone make it worse. Use auto-refine search so the critical surface is found.",
     figure="pp. 2–5: sections of locations 1–4.")),
]}

# ======================================================================== CE3115 ERSS problem sets
GEOQ[D["PS1"]] = {"code": "CE203", "title": "Retaining 1 · Underground construction in Singapore (CE3115 Tutorial PS1)", "sections": [
 sec("Regulations, wall choice, wall types", (1, 5),
   q("CE3115 PS1 Q1–Q2",
     r"(1) What do ERSS and TERS stand for? (2a) What do QP, AC and BCA stand for? (2b) Which activities are "
     r"'geotechnical building works' (GBW) — is a 1 m deep excavation for a shallow drain one? (2c) Do all GBW need "
     r"QP and AC approval?",
     r"**ERSS: earth retaining or stabilising structures; TERS: temporary earth retaining structures. QP: qualified "
     r"person (PE with a practising certificate, accountable for the design); AC: accredited checker (independent "
     r"check); BCA: Building and Construction Authority (regulator). GBW include tunnels > 2 m in diameter, "
     r"excavations, ERSS or slopes > 6 m deep/high, and foundations of buildings of 30 storeys or more — a 1 m drain "
     r"excavation is not GBW. Requirements (QP and/or AC) depend on the category of work.**", ""),
   q("CE3115 PS1 Q3–Q5",
     r"(3a) A four-storey factory with one basement on an empty plot in Tuas: what retaining wall would you propose? "
     r"(3b) A 35-storey extension next to an existing hotel on Orchard Road: what earth retention is likely needed? "
     r"(4) List pros and cons of steel sheet pile walls, soldier pile walls and diaphragm walls. (5) How does ground "
     r"freezing work, and has it been used in Singapore?",
     r"**(3a) Sheet piles (open site, 5–7 m dig) · (3b) a stiff secant-pile or diaphragm wall to limit ground movement "
     r"next to the hotel · (5) freeze pipes turn pore water to ice, giving a strong watertight zone; used at Marina Bay "
     r"for the Thomson–East Coast Line under existing lines.**",
     r"(4) Sheet piles: fast, reusable / noisy, hard to drive in stiff soil, flexible. Soldier pile and lagging: cheap, "
     r"fast / not watertight, flexible. Diaphragm wall: stiff, watertight, can be permanent / expensive, specialist "
     r"plant.")),
]}

GEOQ[D["PS2"]] = {"code": "CE203", "title": "Earth pressure 1 · K₀, Rankine, water & layers (CE3115 Tutorial PS2)", "sections": [
 sec("Q1–Q2 At-rest pressure", (1, 2),
   ("eq", r"K_0 = \frac{\nu}{1-\nu}\ (\text{elastic, laterally constrained}),\qquad K_0 = 1 - \sin\phi'\ (\text{Jaky, NC})"),
   q("CE3115 PS2 Q1",
     r"Find the coefficient of lateral pressure K for a laterally constrained elastic column (Young's modulus E, "
     r"Poisson's ratio $\nu$) under a vertical stress increase $\sigma_v$.",
     r"**$K = \nu/(1 - \nu)$.**",
     r"No lateral strain: $\varepsilon_h = [\sigma_h - \nu(\sigma_h + \sigma_v)]/E = 0$ → $\sigma_h(1 - \nu) = "
     r"\nu\sigma_v$."),
   q("CE3115 PS2 Q2",
     r"A normally consolidated sand ($\phi = 30^\circ$, $e = 0.5$, $G_s = 2.7$) is 15 m deep with the water table at "
     r"the surface; $\gamma_w = 9.81\ \mathrm{kN/m^3}$. (a) Draw the vertical and horizontal effective stress profiles. "
     r"(b) Redo them after the water table is lowered to 7 m (no capillary rise).",
     r"**(a) at 15 m: $\sigma'_v = 166.5$, $\sigma'_h = 83.3\ \mathrm{kPa}$ · (b) $\sigma'_v = 123.9$ at 7 m and "
     r"212.7 at 15 m; $\sigma'_h$ is half of $\sigma'_v$.**",
     r"$K_0 = 1 - \sin 30^\circ = 0.5$. $\gamma_d = G_s\gamma_w/(1 + e) = 17.66$, $\gamma' = (G_s - 1)\gamma_w/(1 + e) "
     r"= 11.1\ \mathrm{kN/m^3}$; profiles are linear between the water table and the base.")),
 sec("Q3–Q6 Concepts, tension cut, Rankine thrust", (3, 3),
   ("eq", r"K_a = \frac{1-\sin\phi}{1+\sin\phi},\quad \sigma_a = K_a\sigma'_v - 2c'\sqrt{K_a},\quad z_0 = \frac{2c'}{\gamma\sqrt{K_a}}\ \left(\phi = 0:\ z_0 = \frac{2c_u}{\gamma}\right)"),
   q("CE3115 PS2 Q3", r"Why does the passive state need much more wall displacement than the active state?",
     r"**Because $\sigma_h$ must rise from $K_0\sigma_v$ past $\sigma_v$ all the way to $K_p\sigma_v$, whereas the "
     r"active state needs only a small drop to $K_a\sigma_v$.**", ""),
   q("CE3115 PS2 Q4",
     r"Does a 3 m temporary vertical cut in clay ($c_u = 30\ \mathrm{kPa}$, $\gamma = 16\ \mathrm{kN/m^3}$) need a "
     r"retaining wall in theory?",
     r"**No: the tension-crack depth $2c_u/\gamma = 3.75\ \mathrm{m} > 3\ \mathrm{m}$, so it stands unsupported in "
     r"theory.**", ""),
   q("CE3115 PS2 Q5",
     r"A 7 m vertical-backed wall retains cohesionless soil ($\gamma = 17.3\ \mathrm{kN/m^3}$, $\phi = 30^\circ$) with "
     r"a horizontal surface. Find the Rankine active thrust per metre and its direction.",
     r"**$P_a = 141\ \mathrm{kN/m}$, horizontal, at $H/3$ above the base.**",
     r"$P_a = \tfrac12 K_a\gamma H^2 = \tfrac12 \times \tfrac13 \times 17.3 \times 7^2 = 141$."),
   q("CE3115 PS2 Q6",
     r"A 5 m rigid wall supports dry cohesionless backfill ($\phi = 30^\circ$, $\gamma = 18\ \mathrm{kN/m^3}$). Find "
     r"the Rankine passive force per metre.",
     r"**$P_p = 675\ \mathrm{kN/m}$.**", r"$P_p = \tfrac12 \times 3 \times 18 \times 5^2 = 675$.")),
 sec(r"Q7 $c'\text{–}\phi'$ backfill", (4, 4),
   q("CE3115 PS2 Q7",
     r"Find the total active thrust per metre on an 8 m smooth vertical wall retaining soil with $c' = 20\ "
     r"\mathrm{kPa}$, $\phi' = 25^\circ$, $\gamma = 17.5\ \mathrm{kN/m^3}$.",
     r"**$P_a = 69\ \mathrm{kN/m}$ (ignoring tension), acting 1.47 m above the base.**",
     r"$K_a = 0.406$: $\sigma_a = -25.5\ \mathrm{kPa}$ at the top and 31.3 kPa at the base; $z_0 = 3.59\ \mathrm{m}$ → "
     r"$P_a = \tfrac12 \times 4.41 \times 31.3 = 69$.")),
 sec("Q8–Q10 Water in the backfill", (5, 7),
   q("CE3115 PS2 Q8",
     r"A 5 m smooth vertical wall: find the active thrust (a) with no water ($c' = 0$, $\phi' = 36^\circ$, $\gamma = "
     r"17.5\ \mathrm{kN/m^3}$) and (b) with the water table at the surface ($\gamma_{\mathrm{sat}} = 19.5$, "
     r"$\gamma_w = 9.81\ \mathrm{kN/m^3}$).",
     r"**(a) $P_a = 57\ \mathrm{kN/m}$ · (b) 31.5 (soil) + 122.5 (water) = 154 kN/m — water dominates.**", ""),
   q("CE3115 PS2 Q9",
     r"A 6 m cantilever wall retains sand ($e = 0.6$, $\phi = 32^\circ$, $G_s = 2.7$). Find the active pressure at the "
     r"base and the resultant when the backfill is (i) dry and (ii) submerged, plus the water force; $\gamma_w = 9.81$.",
     r"**(i) $\sigma_a = 30.5\ \mathrm{kPa}$, $P = 91.5\ \mathrm{kN/m}$ · (ii) $\sigma'_a = 19.2$, $P = 57.6$ plus "
     r"water 176.6 kN/m.**", "", figure="p. 6, Figure Q9."),
   q("CE3115 PS2 Q10",
     r"A 10 m wall retains sand ($G_s = 2.65$, $e = 0.65$, $\phi = 30^\circ$) with the water table 3 m below the "
     r"surface and a surcharge $q = 14\ \mathrm{kPa}$. Draw the active pressure diagram and find the total thrust per "
     r"metre ($\gamma_w = 9.81$).",
     r"**Total thrust ≈ 502 kN/m.**",
     r"Sum the parts $K_a\gamma H_1$, $K_a\gamma'H_2$, $K_aq$ and $\gamma_wH_2$.", figure="p. 7, Figure Q10.")),
 sec("Q11 Two layers with surcharge", (8, 9),
   q("CE3115 PS2 Q11",
     r"A 6 m wall supports two 3 m layers: upper $c' = 0$, $\phi' = 30^\circ$, $\gamma_{\mathrm{dry}} = 17.5$, "
     r"$\gamma_{\mathrm{sat}} = 19.5$; lower $c' = 10\ \mathrm{kPa}$, $\phi' = 18^\circ$, $\gamma_{\mathrm{sat}} = 19\ "
     r"\mathrm{kN/m^3}$. Surcharge 50 kPa, water table 1.5 m below ground, $\gamma_w = 9.81$. Find the total thrust and "
     r"its line of action.",
     r"**Total 294.6 kN/m acting 2.17 m above the base.**",
     r"The pressure jumps at the interface (different $K_a$ and the $-2c\sqrt{K_a}$ term).")),
 sec("Q12 Passive with sloping backfill", (10, 11),
   q("CE3115 PS2 Q12",
     r"A force of 450 kN/m pushes a smooth 5 m wall into dry sand ($\phi = 30^\circ$, $\gamma = 18\ \mathrm{kN/m^3}$) "
     r"whose surface slopes up at $\beta$. Find the maximum $\beta$ without passive failure.",
     r"**$\beta \approx 20^\circ$ by Rankine — but treat this with caution.**",
     r"Rankine's sloping-backfill $K_p$ gives a passive force that *decreases* as $\beta$ rises, which is unrealistic; "
     r"Coulomb and Caquot–Kérisel show it increases. With $\beta = 0$ the passive force is 675 kN > 450 kN, so there "
     r"is no passive failure. Don't use Rankine passive with $\beta > 0$.", figure="p. 10, Figure Q12.")),
]}

GEOQ[D["PS3"]] = {"code": "CE203", "title": "Earth pressure 2 · Cohesion, Coulomb & curved surfaces (CE3115 Tutorial PS3)", "sections": [
 sec("Q1–Q2 Clay backfill & tension cracks", (1, 3),
   q("CE3115 PS3 Q1",
     r"A 6 m wall retains soft saturated clay ($\gamma = 16.5\ \mathrm{kN/m^3}$, $s_u = 10\ \mathrm{kPa}$, $\phi = 0$). "
     r"Find (a) the maximum tension-crack depth, (b) $P_a$ before cracking and (c) $P_a$ after cracking.",
     r"**(a) $z_0 = 1.21\ \mathrm{m}$ · (b) 177 kN/m · (c) 189 kN/m.**",
     r"$z_0 = 2s_u/\gamma = 20/16.5$; base pressure $16.5 \times 6 - 20 = 79\ \mathrm{kPa}$; (b) $\tfrac12 \times 6 "
     r"\times 99 - 20 \times 6 = 177$; (c) $\tfrac12 \times 79 \times 4.79 = 189$."),
   q("CE3115 PS3 Q2",
     r"A 4.6 m wall retains clay ($\gamma = 19\ \mathrm{kN/m^3}$, $\phi' = 20^\circ$, $c' = 12\ \mathrm{kPa}$) "
     r"sloping at $\beta = 10^\circ$, on rock. Find the Rankine active force after the tension crack forms.",
     r"**$P_a = 41.5\ \mathrm{kN/m}$ (horizontal component 40.8), with $z_0 = 1.73\ \mathrm{m}$.**", "",
     figure="p. 2, Figure Q2.")),
 sec("Q3–Q6 Coulomb, densification, layered", (4, 8),
   q("CE3115 PS3 Q3",
     r"A 4 m wall with its back inclined at 5° supports soil ($\gamma = 15\ \mathrm{kN/m^3}$, $\phi' = 30^\circ$) "
     r"sloping at 10°, with wall friction $\delta' = 15^\circ$. Estimate the active force, its direction and location.",
     r"**$K_a = 0.387$ → $P_a = 46.4\ \mathrm{kN/m}$ at $H/3$, inclined at $\delta$ to the wall normal.**", "",
     figure="p. 3, Figure Q3."),
   q("CE3115 PS3 Q4",
     r"A 10 m counterfort wall retains cohesionless backfill with $e = 0.7$, $\phi = 30^\circ$ when loose and "
     r"$e = 0.4$, $\phi = 40^\circ$ when dense ($G_s = 2.7$). Compare the Rankine active and passive pressures.",
     r"**Base active pressure 52 → 41 kPa and passive 468 → 870 kPa from loose to dense** — densifying lowers active "
     r"and raises passive.", ""),
   q("CE3115 PS3 Q5",
     r"A 7.32 m vertical-backed wall retains sandy loam ($\gamma = 17.3\ \mathrm{kN/m^3}$, $c = 12\ \mathrm{kPa}$, "
     r"$\phi = 20^\circ$) with a horizontal surface; no wall friction. Find the active thrust.",
     r"**$P_a = 120\ \mathrm{kN/m}$** ($z_0 \approx 2.0\ \mathrm{m}$, $\sigma_a = 45.3\ \mathrm{kPa}$ at the base).", ""),
   q("CE3115 PS3 Q6",
     r"A 6 m rigid wall has dry backfill: 1.5 m sandy clay ($\phi = 20^\circ$, $c = 12.15\ \mathrm{kPa}$, $\gamma = "
     r"16.4$) over sand ($\phi = 30^\circ$, $c = 0$, $\gamma = 17.25\ \mathrm{kN/m^3}$). Find the total active force and "
     r"draw the pressure diagram.",
     r"**The crack ($z_0 = 2.1\ \mathrm{m}$) passes through the whole 1.5 m clay layer; the sand pressure rises from "
     r"8.2 to 34.1 kPa.**", "", figure="p. 5, Figure Q6.")),
 sec("Q7–Q8 Active vs passive moments", (9, 13),
   q("CE3115 PS3 Q7–Q8",
     r"For the frictionless walls in Figures Q7 and Q8 (layered backfill, surcharge in Q7), find the active and passive "
     r"pressure distributions, the forces and their locations, and the ratio of passive to active moment about the base.",
     r"**Q7: $\sum P_a = 215\ \mathrm{kN}$ at 2.09 m, $\sum P_p = 323\ \mathrm{kN}$ at 1.33 m, $M_p/M_a = 0.96$ → "
     r"the wall rotates · Q8: $P_a = 554\ \mathrm{kN}$ at 3.74 m, $P_p = 389\ \mathrm{kN}$, ratio 0.31.**",
     r"Water pressures on the two sides cancel only if the levels match.", figure="pp. 6–7, Figures Q7–Q8.")),
 sec("Q9–Q10 Surcharge, rough wall, flooding", (14, 15),
   q("CE3115 PS3 Q9",
     r"An 8 m wall retains soil ($\gamma = 18\ \mathrm{kN/m^3}$, $\phi = 30^\circ$) with a 15 kPa surcharge; water "
     r"below the base. Find the active force for (a) a smooth wall and (b) a rough wall ($\delta = 20^\circ$).",
     r"**(a) 232 kN/m · (b) 209 kN/m (horizontal 196).**", ""),
   q("CE3115 PS3 Q10",
     r"A 5 m rough wall ($\delta = 20^\circ$, back inclined 10°) supports a 15° slope ($G_s = 2.7$, $e = 1.25$, "
     r"$\phi = 30^\circ$). After a flood the water table rises from below the base to the surface. Find the percentage "
     r"increase in lateral force ($\gamma_w = 10$, ignore seepage).",
     r"**62.4 → 39 (soil) + 125 (water) = 164 kN → about +163 %.** Drainage matters.", "")),
 sec("Q11–Q13 Plane vs curved passive surfaces", (16, 19),
   q("CE3115 PS3 Q11–Q12",
     r"A 10 m gravity wall with a vertical back pushes against sand ($\phi = 40^\circ$, $\gamma = 18.5\ "
     r"\mathrm{kN/m^3}$). Find the passive thrust for a plane surface and for a curved surface with $\delta = 20^\circ$; "
     r"then the reduction for a curved surface with $\delta = 30^\circ$.",
     r"**$\delta = 20^\circ$: 10 230 kN (plane) vs 8 325 kN (curved) · $\delta = 30^\circ$: 19 947 vs 11 100 kN.**",
     r"Coulomb's plane surface badly overestimates passive for rough walls ($\delta > \phi/3$); use curved-surface "
     r"(Caquot–Kérisel) $K_p$."),
   q("CE3115 PS3 Q13",
     r"A 3 m vertical wall is pushed into granular soil ($\gamma = 18\ \mathrm{kN/m^3}$, $\phi = 37^\circ$, level "
     r"ground). Compare the horizontal passive force by Rankine/Coulomb (smooth), Coulomb with $\delta/\phi = 0.5$ and "
     r"0.8, and Caquot–Kérisel (curved) for the same ratios.",
     r"**Smooth 324 · Coulomb 0.5 → 674, 0.8 → 1254 · Caquot–Kérisel 0.5 → 583, 0.8 → 729 kN/m.**", "")),
]}

GEOQ[D["PS4"]] = {"code": "CE203", "title": "Retaining 2 · Gravity & cantilever walls, FoS (CE3115 Tutorial PS4)", "sections": [
 sec("Q1 Gravity wall, no front soil", (1, 2),
   ("eq", r"FoS_{OT} = \frac{\sum M_R}{\sum M_O}\ge 2,\quad FoS_{sl} = \frac{N\tan\delta_b + P_p + c_bB}{P_a}\ge 1.5,\quad p = \frac{N}{B}\left(1 \pm \frac{6e}{B}\right)"),
   q("CE3115 PS4 Q1",
     r"A smooth concrete gravity wall 6.6 m high and 3.2 m wide ($\gamma = 24\ \mathrm{kN/m^3}$) retains dry soil "
     r"($c' = 0$, $\phi' = 35^\circ$, $\gamma = 18\ \mathrm{kN/m^3}$); base friction $\phi_b = 0.8\phi'$. Ignoring the "
     r"2 m of soil in front, find the factors of safety against overturning and sliding and the base pressures.",
     r"**Overturning 3.5 · sliding 2.5 · $p_{\max} = 295$, $p_{\min} = 22\ \mathrm{kPa}$.**",
     r"$K_a = 0.27$, $P_a = 106\ \mathrm{kN}$, $W = 507\ \mathrm{kN}$, $\delta_b = 28^\circ$. Overturning $811/233$; "
     r"sliding $269.5/106$; $\bar x = 577.8/506.9 = 1.14\ \mathrm{m}$, $e = 0.46 < B/6$.", figure="p. 1, Figure Q1.")),
 sec("Q2–Q3 Front soil; smooth base", (3, 5),
   q("CE3115 PS4 Q2–Q3",
     r"Repeat Q1 (2) including the 2 m of soil in front of the wall, and (3) also assuming a smooth base with no "
     r"frictional resistance.",
     r"**(2) overturning 3.86, sliding 3.8, $p = 280/37\ \mathrm{kPa}$ · (3) sliding $133/106 = 1.26 < 1.5$ ✗, $p = "
     r"254/63\ \mathrm{kPa}$.**",
     r"Passive 133 kN at 0.67 m above the base. In bearing count only the passive actually mobilised "
     r"($P_p/\mathrm{FoS}_{\mathrm{sl}}$) in the moment.")),
 sec(r"Q4 $c'\text{–}\phi'$ backfill with surcharge", (6, 8),
   q("CE3115 PS4 Q4",
     r"The same wall with a 20 kPa surcharge on dry backfill of $c' = 10\ \mathrm{kPa}$, $\phi' = 25^\circ$, "
     r"$\gamma = 18$; base friction $\delta' = 15^\circ$ and adhesion $c_b = 10\ \mathrm{kPa}$; include the front soil. "
     r"Find the factors of safety against overturning and sliding and the base pressures.",
     r"**Overturning 3.5 · sliding 2.4 · $p = 283/34\ \mathrm{kPa}$.**",
     r"$z_0 = 0.63\ \mathrm{m}$, $P_a = 131.7\ \mathrm{kN}$; sliding (151 passive + 136 friction + 32 adhesion)/131.7.",
     figure="p. 2, Figure Q4.")),
 sec("Q5–Q6 Cantilever & gravity walls with heel soil", (9, 14),
   q("CE3115 PS4 Q5",
     r"For the cantilever wall in Figure Q5 (dry backfill $c' = 0$, $\phi' = 30^\circ$, $\gamma = 17$, sloping at 20°; "
     r"base friction 20°, no adhesion; wall $24\ \mathrm{kN/m^3}$), find the pressure on the "
     r"vertical plane ab, the factors of safety against sliding and overturning, and the base pressures.",
     r"**$P_a = 71.3\ \mathrm{kN}$ (67 horizontal, 24 vertical) · sliding 1.9 · overturning 3.3 · $p = 99.6/40.2\ "
     r"\mathrm{kPa}$.**",
     r"Use a virtual back through the heel: soil above the heel counts as wall weight and Rankine applies there.",
     figure="p. 3, Figure Q5."),
   q("CE3115 PS4 Q6",
     r"For the gravity wall in Figure Q6 on clay (dry sand behind and in front, $\phi' = 30^\circ$, $\gamma = 19.5$; "
     r"base friction 20°), find the factors of safety against overturning and sliding and the toe and heel pressures.",
     r"**$P_a = 93\ \mathrm{kN}$ at 1.78 m, $P_p = 57\ \mathrm{kN}$ · overturning 3.5 · sliding 1.9 · $p = 167.5/39.4\ "
     r"\mathrm{kPa}$.**", "", figure="p. 4, Figure Q6.")),
]}

GEOQ[D["PS5"]] = {"code": "CE203", "title": "Retaining 3 · Same wall to EC7 DA1 (CE3115 Tutorial PS5)", "sections": [
 sec("EC7 DA1 checks of PS4 Q3", (1, 6),
   q("CE3115 PS5 Q1",
     r"Repeat Problem Set 4 Question 3 (gravity wall with front soil and a smooth base) using EC7 Design Approach 1. "
     r"Are the answers consistent with the earlier factors of safety?",
     r"**EQU: stabilising 793 > destabilising 325 kNm → OK · GEO C1: sliding $P_a = 143 > P_p = 133\ \mathrm{kN}$ → "
     r"fails · GEO C2: $134.3 > 105.1$ → fails; bearing 289/28 kPa · consistent with PS4 Q3 (FoS 1.26 < 1.5).**",
     r"EQU: $\gamma_{G,\mathrm{dst}} = 1.1$, $\gamma_{G,\mathrm{stb}} = 0.9$, $\gamma_{\phi} = 1.25$ → $\phi_d = "
     r"29.3^\circ$, $K_a = 0.343$, $K_p = 2.92$. C1: $P_a = 1.35 \times 106 = 143$. Fix sliding before checking bearing. "
     r"The official C1 bearing figures ($p_{\max} = 511$, $p_{\min} = -83\ \mathrm{kPa}$) factor N by 1.35 but leave "
     r"the moments unfactored; keep factors consistent when you redo it."),
   EC7,
 ),
]}

GEOQ[D["PS6"]] = {"code": "CE203", "title": "Retaining 4 · Cantilever sheet piles (CE3115 Tutorial PS6)", "sections": [
 sec("Q1–Q2 Cantilever in dry sand", (1, 6),
   q("CE3115 PS6 Q1–Q2",
     r"A cantilever sheet pile retains 6 m of sand ($\gamma = 17\ \mathrm{kN/m^3}$, $\phi = 30^\circ$). (a) Find the "
     r"embedment by the simplified approach, (b) the maximum bending moment and its location, (c) the minimum section "
     r"modulus for $f_b = 175\ \mathrm{MN/m^2}$. (Q2: repeat with the net pressure diagram method.)",
     r"**(a) $D = 6.7\ \mathrm{m}$ · (b) $M_{\max} = 460\ \mathrm{kNm/m}$ at 3 m below dredge level · (c) $Z = 2.63 "
     r"\times 10^{-3}\ \mathrm{m^3/m}$ · net-pressure method: $D \approx 6.0\ \mathrm{m}$, same $M_{\max}$.**",
     r"Moments about the toe: $0.944(6 + d_0)^3 = 8.5d_0^3$ → $d_0 = 5.56$, $D = 1.2d_0$. Zero shear: "
     r"$K_a(H + d_s)^2 = K_pd_s^2$ → $d_s = 3\ \mathrm{m}$. $Z = 460/175\,000$. (The solution writes $26.25 \times "
     r"10^{-2}\ \mathrm{m^3}$ — a units slip.)", figure="p. 1, Figure Q-1.")),
 sec("Q3–Q4 Water both sides", (7, 11),
   q("CE3115 PS6 Q3–Q4",
     r"As Q1, but the water table is 3 m below the top on both sides ($\gamma_{\mathrm{dry}} = 17$, "
     r"$\gamma_{\mathrm{sat}} = 19\ \mathrm{kN/m^3}$). Find D and the maximum moment by the simplified approach (Q3) "
     r"and the net pressure method (Q4).",
     r"**Simplified: $d_0 = 7.3$ → $D = 8.7\ \mathrm{m}$, $M_{\max} = 504\ \mathrm{kNm}$ at 4 m · net pressure: "
     r"$D = 7.8\ \mathrm{m}$, $M_{\max} = 506\ \mathrm{kNm}$.**", "Equal water levels cancel.",
     figure="p. 2, Figure Q-3.")),
 sec("Q5 Layered sand", (12, 15),
   q("CE3115 PS6 Q5",
     r"A sheet pile retains 5 m of loose sand ($\gamma = 16$, $\phi = 28^\circ$) over medium dense sand ($\gamma = "
     r"18$, $\phi = 35^\circ$) that extends below the dredge level. Find D by the idealised limiting pressure profile "
     r"and the maximum bending moment.",
     r"**$D \approx 3.9\ \mathrm{m}$ · $M_{\max} = 198\ \mathrm{kNm}$ at 1.83 m below dredge level.**",
     r"Solve horizontal and moment equilibrium together: $d = 3.82\ \mathrm{m}$, $z = 0.41\ \mathrm{m}$.",
     figure="p. 3, Figure Q-5.")),
]}

GEOQ[D["PS7"]] = {"code": "CE203", "title": "Retaining 5 · Anchored walls, free-earth support (CE3115 Tutorial PS7)", "sections": [
 sec("Q1 Free earth support", (1, 3),
   q("CE3115 PS7 Q1",
     r"A smooth single-propped wall retains 5 m of sand ($G_s = 2.67$, $\gamma_d = 13\ \mathrm{kN/m^3}$, $\phi = "
     r"30^\circ$) with a tie 1 m below the top and the water table 2 m below the top; $\gamma_w = 9.8$. Find the "
     r"embedment and the tie force by the free earth support method.",
     r"**$D = 2.22\ \mathrm{m}$, $T = 30.5\ \mathrm{kN/m}$.**",
     r"Active pressure (dry above the water table, $\gamma'$ below) and passive $K_p\gamma'D$; water cancels. Moments "
     r"about the tie give a cubic in D; horizontal equilibrium gives T.", figure="p. 1, Figure Q-1.")),
 sec("Q2–Q3 Factor of safety on passive", (4, 8),
   q("CE3115 PS7 Q2–Q3",
     r"For the same wall, find D and T with FS = 2 on passive resistance: (Q2) using $K_{pm} = K_p/2$, a steeper "
     r"triangular distribution; (Q3) using a trapezoidal mobilised distribution giving $F_{pm} = \tfrac12 K_p\gamma "
     r"D^2/\mathrm{FS}$.",
     r"**(Q2) $D = 4.0\ \mathrm{m}$, $T = 37.8\ \mathrm{kN/m}$ · (Q3) $D = 4.25\ \mathrm{m}$, $T = 32.3\ "
     r"\mathrm{kN/m}$ ($\alpha = 0.293$).**", "", figure="p. 2, Figure Q-3.")),
]}

GEOQ[D["QZ"]] = {"code": "CE203", "title": "Retaining 6 · Past-year quiz (earth pressure & walls)", "sections": [
 sec("True/false concepts", (1, 2),
   q("CE3115 Quiz P1–P5",
     r"True or false, with reasons: (1) embedment depth is the most critical design parameter for gravity walls; (2) "
     r"soldier pile and lagging walls can't be used below a high water table without extensive dewatering; (3) in a "
     r"frictional soil $K_p > 1$, so passive $\sigma'_h > \sigma'_v$; (4) Coulomb's passive failure line is close to "
     r"reality; (5) identify the wall type in the photo.",
     r"**(1) False — dead weight governs gravity walls; embedment matters for flexible walls · (2) True · (3) True · "
     r"(4) False — the passive plane surface can be far from the real curved surface · (5) a diaphragm wall.**", "")),
 sec("$K_0$ from OCR; Mohr pole", (3, 5),
   ("eq", r"K_{0,OC} = (1 - \sin\phi')\,OCR^{\sin\phi'}"),
   q("CE3115 Quiz P6–P7",
     r"(6) A clay sample from 4.3 m has $\sigma'_{v0} = 33\ \mathrm{kPa}$ and $\phi' = 35^\circ$; from the oedometer "
     r"curve find $\sigma'_p$ and estimate $K_0$. (7A) For the stress block in Figure A find the pole and the shear "
     r"stress on the vertical plane. (7B) In Figure B find $\sigma_1$.",
     r"**(6) $\sigma'_p = 100\ \mathrm{kPa}$, OCR ≈ 3, $K_0 = 0.81$ · (7A) pole at (6, −4), shear on the vertical "
     r"plane 4 kPa · (7B) $\sigma_1$ = 5 kPa (the pole).**", r"$K_0 = (1 - \sin 35^\circ) \times 3^{\sin 35^\circ}$.")),
 sec("Gravity wall 7 m", (6, 9),
   q("CE3115 Quiz P8–P9",
     r"A smooth 7 m gravity wall ($24\ \mathrm{kN/m^3}$) retains backfill with $c' = 10\ \mathrm{kPa}$, $\phi' = "
     r"28^\circ$, $\gamma = 16.7\ \mathrm{kN/m^3}$, with 2 m of the same soil in front; no base friction or adhesion; no "
     r"water. Find (1) $K_a$, the active thrust and base active stress (ignoring tension), (2) $K_p$, the passive thrust "
     r"and base passive stress, (3) the factor of safety against sliding, (4) against overturning, and (5) check bearing "
     r"(ultimate 500 kPa).",
     r"**(1) $K_a = 0.361$, $\sigma_a = 30.2\ \mathrm{kPa}$, $P_a = 75.6\ \mathrm{kN}$ · (2) $K_p = 2.77$, $\sigma_p$ "
     r"33.3 → 125.8 kPa, $P_p = 159.1\ \mathrm{kN}$ · (3) sliding $159.1/75.6 = 2.11$ · (4) overturning $709/126 = 5.6$ "
     r"· (5) $e = 0.26\ \mathrm{m}$, $p_{\max} = 211.5$, $p_{\min} = 66\ \mathrm{kPa}$ → bearing FoS $500/211.5 = 2.36 < "
     r"3$ ✗.**",
     r"A surcharge behind raises $P_a$, so both factors fall. The quiz answer ignores the $c'$ reduction on the active "
     r"side ($\sigma_a = K_a\gamma z$) — conservative.")),
]}

GEOQ[D["EX"]] = {"code": "CE203", "title": "Exam · CE3115 AY19/20 paper (slopes, walls, sheet piles)", "sections": [
 sec("Q1 River bank with bench & tension crack", (2, 5),
   q("CE3115 Exam Q1",
     r"(a) A three-layer river bank is stabilised by benching, with a permanent surcharge on a 5 m bench. For the given "
     r"trial circle, find the first-trial factor of safety by the Simplified Bishop method to DA1-C2, with 2.5 m "
     r"tension cracks at the top (7–8 slices, surcharge 10–50 kPa, $\gamma_w = 10$). (b) A level hard rock stratum lies "
     r"at +2.0 m: how does it affect F and how would you re-analyse? (c) After 3 m of bed erosion, with resisting force "
     r"1626 kN/m and driving force 1588 kN/m (DA1-C1) and the affected slice omitted ($n_{\alpha} = 1.42$), is the bank "
     r"stable?",
     r"**(a) $F \approx 1.2$ (first trial, 50 kPa surcharge) · (b) the rock forces a non-circular or compound slip → F "
     r"likely rises; re-analyse with Spencer or Morgenstern–Price · (c) $F \approx 0.9$ → potentially unstable.**", "",
     figure="pp. 2–4, Figures Q1a and Q1c.")),
 sec("Q2 Seabed trench", (5, 6),
   q("CE3115 Exam Q2",
     r"Same seabed trench as Tutorial 2 Q1 (soft clay $s_u = 17\ \mathrm{kPa}$, $\gamma = 16$, 3 m deep, 60° sides, "
     r"trial circle as drawn). (a) Short-term F by the mass procedure (DA1-C2). (b) F from Taylor's chart (firm stratum "
     r"very deep) and comparison. (c) Assess a contractor's claim that 45° sides allow a deeper trench, comparing "
     r"excavation volumes with a 3 m base width.",
     r"**(a) 1.33 · (b) 1.33 — the trial circle is the critical one · (c) 45° gives no real depth gain; 60° is "
     r"cheaper.**", "")),
 sec("Q3 Cantilever wall with layered backfill", (7, 8),
   q("CE3115 Exam Q3",
     r"(a) Why can Coulomb's passive approach give large errors for very rough walls? (b) Why is Coulomb's driving "
     r"moment often less critical than Rankine's? For the cantilever wall in Figure Q3 (sandy clay $c' = 13\ "
     r"\mathrm{kPa}$, $\phi' = 24^\circ$, $\gamma = 17$ over sand; surcharge q behind the virtual back): (c) the minimum "
     r"surcharge for no tension crack in the sandy clay; (d) the force diagram; (e) factors of safety against sliding, "
     r"overturning and bearing (ultimate 250 kPa); (f) GEO sliding to DA1-C1.",
     r"**(a) the real passive surface is curved; a plane is far from it when wall friction is high · (b) Coulomb's "
     r"thrust is inclined, and its vertical component resists overturning · (c) $q = 2c'/\sqrt{K_a} \approx 40\ "
     r"\mathrm{kPa}$ ($K_a = 0.42$) · (d)–(f) work from Figure Q3 (no official numbers).**",
     r"(c) No tension at the top of the clay: $K_aq - 2c'\sqrt{K_a} \ge 0$. For (e)–(f) take the active thrust on the "
     r"virtual back from each layer (with the surcharge), water pressures, wall and heel-soil weights, then the usual "
     r"checks; in (f) factor the permanent thrust by 1.35 and the water pressures as variable actions.",
     figure="p. 6, Figure Q3: wall dimensions and layers.", src="claude", checked=False)),
 sec("Q4 Sheet pile in clay with sand backfill", (8, 9),
   q("CE3115 Exam Q4",
     r"(a) Why do flexible walls rely on embedment while gravity walls often neglect passive resistance? (b) A smooth "
     r"sheet pile retains sand ($\gamma = 18\ \mathrm{kN/m^3}$, $\phi' = 28^\circ$, $c' = 0$) to height h above the "
     r"water table at the dredge line, and is embedded in deep marine clay with $s_u = 30\ \mathrm{kPa}$. The simplified "
     r"approach gave $D = 3.6\ \mathrm{m}$ (FoS 1 on passive). Find h. (c) Find the maximum bending moment and its "
     r"location.",
     r"**(a) passive resistance is the main stabilising force of a flexible wall; a gravity wall relies on its weight · "
     r"(b) $h \approx 3.96\ \mathrm{m}$ · (c) $M_{\max} \approx 94\ \mathrm{kNm/m}$ at 1.05 m below the dredge line.**",
     r"$K_a = 0.361$. Net clay resistance below the dredge line $4s_u - \gamma h$. With $D = 1.2d_0$, $d_0 = 3.0\ "
     r"\mathrm{m}$; moments about the toe: $\tfrac12 K_a\gamma h^2(d_0 + h/3) = (4s_u - \gamma h)d_0^2/2$ → $1.083h^3 + "
     r"9.747h^2 + 81h - 540 = 0$ → $h = 3.96$. Then $P_a = 50.9\ \mathrm{kN/m}$, zero shear at $z = 50.9/48.7 = 1.05\ "
     r"\mathrm{m}$, $M_{\max} = 50.9(1.05 + 1.32) - 48.7 \times 1.05^2/2 = 94$.", src="claude",
     figure="p. 8, Figure Q4.")),
]}

# ======================================================================== CE3116 foundations
GEOQ[D["SI"]] = {"code": "CE203", "title": "Foundations 1 · Site investigation: SPT, CPTu, PMT, permeability (CE3116 Tut 2)", "sections": [
 sec("a) SPT corrections", (1, 2),
   ("eq", r"(N_1)_{60} = N\cdot\frac{E_r}{60}\cdot\lambda\cdot C_N,\qquad C_N = \frac{300}{200 + \sigma'_v}\ (\text{dense sand}),\qquad s_u \approx 5N_{60}\ \text{kPa}"),
   q("CE3116 Tut 2 (a)",
     r"At a reclaimed site (gravelly sand 0–6 m, sandy clay 6–14 m with PI 30 % and OCR 2, silty sand below; water "
     r"table at 2 m; $\gamma = 19$ above and $19.5\ \mathrm{kN/m^3}$ below), the SPT hammer efficiency is 70 %. "
     r"Correct the N-values at 3 m (N = 28) and 10 m (N = 8) and estimate the strength parameter of each soil.",
     r"**3 m: $(N_1)_{60} \approx 30$ → $\phi' \approx 39^\circ$ · 10 m clay: $N_{60} \approx 9$ → $s_u \approx 45\ "
     r"\mathrm{kPa}$.**",
     r"Sand: $28 \times 70/60 \times 0.75 \times 1.21 \approx 30$ → $D_R$ 65–85 % → $\phi' = 37^\circ + 2^\circ$ "
     r"(gravelly). Clay: $8 \times 70/60 \times 0.95 \approx 9$; no $C_N$ for clay.", figure="p. 2, Figure 1.")),
 sec("b–c) CPTu: soil type & strength", (2, 3),
   ("eq", r"q_t = q_c + (1-a)u_2,\quad Q_t = \frac{q_t - \sigma_{v0}}{\sigma'_{v0}},\quad F_r = \frac{f_s}{q_t - \sigma_{v0}},\quad I_c = \sqrt{(3.47 - \log Q_t)^2 + (1.22 + \log F_r)^2}"),
   q("CE3116 Tut 2 (b)–(c)",
     r"From the CPTu record ($a = 0.75$; $q_c = 9.12\ \mathrm{MPa}$ at 3 m, $0.76\ \mathrm{MPa}$ at 10 m): (b) find "
     r"the soil behaviour type index $I_c$ at 3 m and compare with the borehole; (c) estimate the strength parameters at "
     r"3 m and 10 m with $N_{kt} = 20$.",
     r"**(b) $I_c = 1.29 < 1.31$ → gravelly/dense sand ✓ · (c) 3 m: $D_R \approx 80\,\%$ → $\phi' \approx 39^\circ$; "
     r"10 m: $s_u = 31\ \mathrm{kPa}$.**",
     r"3 m: $q_t = 9.13\ \mathrm{MPa}$, $Q_t = 191$, $F_r = 0.19\,\%$. 10 m: $q_t = 0.76 + 0.25 \times 0.202 = 0.81\ "
     r"\mathrm{MPa}$, $\sigma_{v0} = 194\ \mathrm{kPa}$, $s_u = (q_t - \sigma_{v0})/N_{kt}$.")),
 sec("d–e) Menard pressuremeter", (3, 4),
   ("eq", r"E = 2(1+\nu)\left[V_c + \bar V\right]\frac{\Delta p}{\Delta V},\qquad s_u = \frac{p_L - p_0}{N_p}"),
   q("CE3116 Tut 2 (d)–(e)",
     r"From the Menard test at 10 m ($\nu = 0.5$, cell volume $750\ \mathrm{cm^3}$, Figure 2): (d) a representative "
     r"Young's and shear modulus free of disturbance effects, and the average cavity strain; (e) $s_u$ with $N_p = 5.5$.",
     r"**(d) $E_{ur} = 10\ \mathrm{MPa}$, $G = 3.3\ \mathrm{MPa}$, cavity strain 0.8 % · (e) $s_u = 39\ "
     r"\mathrm{kPa}$.**",
     r"Use the unload–reload loop: $E = 3 \times 936 \times 50/14$. $p_0 = 144$, $p_L = 360$ (at $V = V_c + 2V_0$) → "
     r"$216/5.5$.", figure="p. 3, Figure 2.")),
 sec("f–g) Compare su; Hvorslev permeability", (5, 5),
   ("eq", r"k = \frac{\pi r^2}{F\,T},\qquad F = \frac{2\pi L}{\ln\left[L/D + \sqrt{1 + (L/D)^2}\right]}"),
   q("CE3116 Tut 2 (f)–(g)",
     r"(f) Compare $s_u$ at 10 m from the SPT, CPTu, pressuremeter and UU tests (36 kPa). (g) From the rising-head test "
     r"at 22 m (casing 100 mm, perforated length 300 mm, Figure 3) find k by Hvorslev and compare with the CPTu range "
     r"for $I_c = 2.0$.",
     r"**(f) SPT 45, CPT 31, PMT 39, UU 36 kPa — calibrate $N_{kt}$ and $N_p$ to the lab value · (g) $k = 9.4 \times "
     r"10^{-5}\ \mathrm{m/s}$, within the CPTu range $10^{-5}$–$10^{-3}\ \mathrm{m/s}$.**",
     r"$F = 1.04\ \mathrm{m}$, $T \approx 80\ \mathrm{s}$ (at $H/H_0 = 0.37$). The solution calls $I_c = 2.0$ 'gravelly "
     r"sand'; on Robertson's chart 1.31–2.05 is zone 6 (clean to silty sand); the k range still fits.",
     figure="p. 4, Figure 3.")),
]}

GEOQ[D["SIX"]] = {"code": "CE203", "title": "Foundations 1a · Site investigation worked example (CE3116)", "sections": [
 sec("Classification, SPT, CPTu, PMT, Hvorslev", (1, 9),
   q("CE3116 SI example",
     r"Worked example in the same format as Tutorial 2, at different depths: classify the clay from its Atterberg "
     r"limits (LL 30 %, PL 15 %), correct the SPT N-value and estimate strength, interpret the CPTu at 12.5 m and 24 m "
     r"($N_{kt} = 20$), and find the initial modulus from the pressuremeter curve.",
     r"**PI = 15 % · corrected $N \approx 32$ (clay: $c_u = 5N = 160\ \mathrm{kPa}$) · 12.5 m: $q_t = 17.08\ "
     r"\mathrm{MPa}$, $F_r = 1.03\,\%$ → sand, $D_R \approx 82\,\%$ · 24 m: $q_t = 3.76\ \mathrm{MPa}$, $F_r = "
     r"4.7\,\%$ → clay, $c_u = (3763 - 450)/20 = 166\ \mathrm{kPa}$ · PMT initial modulus ≈ 63 MPa (cavity strain "
     r"2.4 %).**", "")),
]}

GEOQ[D["CP"]] = {"code": "CE203", "title": "Foundations 2 · Compaction specification (CE3116 Tut 1)", "sections": [
 sec("Q1 Specification for field compaction", (1, 4),
   ("eq", r"\rho_d = \frac{\rho}{1+w},\qquad \rho_{d,ZAV/S_r} = \frac{G_s\rho_w}{1 + wG_s/S_r},\qquad \rho_{d,field} = \frac{\rho_{d,min}}{1 - D_R\left(\dfrac{\rho_{d,max} - \rho_{d,min}}{\rho_{d,max}}\right)}"),
   q("CE3116 Tut 1 Q1",
     r"A 300 m × 300 m site is to be filled 3 m deep and compacted to a relative density of 75 %. Borrow 1 (gravelly "
     r"sand: $w = 10\,\%$, $G_s = 2.65$, $S_r = 40\,\%$, $e$ 0.4–0.85) and borrow 2 (sandy silt: $w = 15\,\%$, $G_s = "
     r"2.72$, $S_r = 55\,\%$, $e$ 0.4–1.0) have the Standard (and, for borrow 2, Modified) Proctor data on p. 1. Prepare "
     r"a specification: (a) compaction curves with the zero-air-void curve, (b) target field dry density, relative "
     r"compaction and water-content range, (c) suitable rollers, (d) maximum lift thickness.",
     r"**Borrow 1: target $\rho_d = 1750\ \mathrm{kg/m^3}$, SP MDD 1898 at OMC 12.7 % → RC ≈ 92 %, w 8–17 % · borrow 2: "
     r"SP MDD 1759 gives RC ≈ 100 % (impractical) → use Modified Proctor (MDD 1856, w 13–19 %) · rollers: vibratory for "
     r"the gravelly sand, tamping-foot or pneumatic for the sandy silt · lifts ≈ 0.5 m.**",
     r"$\rho_{d,\min} = 1432$, $\rho_{d,\max} = 1893\ \mathrm{kg/m^3}$ for borrow 1. The low-w drop in dry density for "
     r"the gravelly sand is bulking. Achievable RC is 90–95 %; > 100 % means that energy cannot reach the target.")),
 sec("Q2 Truck trips & water", (4, 6),
   q("CE3116 Tut 1 Q2",
     r"For each material find (a) the number of truck trips (28 t payload, $22\ \mathrm{m^3}$ bucket, 20 % bulking) and "
     r"(b) the water to add before compaction, allowing 2 % moisture loss in transport.",
     r"**Borrow 1: 18 563 trips (mass governs; 16 169 by volume), water 21 263 t · borrow 2: 19 406 trips, water "
     r"14 175 t.**",
     r"Solids $300 \times 300 \times 3 \times 1.75 = 472\,500\ \mathrm{t}$; borrow 1 wet mass $519\,750\ \mathrm{t}$ "
     r"→ $519\,750/28$; water $(12.5 - 8)\,\% \times 472\,500$.")),
 sec("Q3 Sand-cone checks", (6, 7),
   q("CE3116 Tut 1 Q3",
     r"Sand-cone tests (Ottawa sand $1550\ \mathrm{kg/m^3}$) in zone A (material 1: 2980 g of sand in the hole, soil "
     r"w = 7.0 %) and zone B (material 2: 2570 g, w = 21.0 %). What measures will meet the target dry density?",
     r"**Zone A: $\rho_d = 1701 < 1750$ — dry of optimum, add at least 1 % water and recompact · zone B: $\rho_d \approx "
     r"1695$, wet of optimum — dry it out and add compactive effort.**",
     r"A: hole volume $2980/1.55 = 1923\ \mathrm{cm^3}$ → $\rho = 1820$, $\rho_d = 1820/1.07 = 1701$.")),
]}

GEOQ[D["ULS"]] = {"code": "CE203", "title": "Foundations 3 · Pad footings to EC7 — bearing resistance (CE3116 Tutorial)", "sections": [
 sec("Q1 Square pad on firm clay", (1, 3),
   ("eq", r"\text{Undrained: } R/A' = (\pi + 2)c_u s_c + q\qquad \text{Drained: } R/A' = c'N_cs_ci_c + q'N_qs_qi_q + \tfrac{1}{2}\gamma'B'N_\gamma s_\gamma i_\gamma"),
   q("CE3116 Shallow Q1",
     r"A square pad 0.7 m thick with a 0.4 m square column (concrete $24\ \mathrm{kN/m^3}$) carries 800 kN permanent and "
     r"300 kN variable load at 2.0 m depth in firm clay ($c_{uk} = 57\ \mathrm{kPa}$, $c'_k = 0$, $\phi'_k = 24^\circ$; "
     r"$\gamma = 18$ above and 20 below the water table at 0.6 m; $\gamma_w = 9.81$). Find the width for ULS.",
     r"**$B = 2.4\ \mathrm{m}$ (drained DA1-C2 governs).**",
     r"Undrained, $B = 2.2$: $V_k = 1002\ \mathrm{kN}$ (base, column, backfill); C1 $1803 < 1889$ ✓, C2 $1392 < 1403$ ✓. "
     r"Drained (include uplift on the base): $V_k = 936$; C2 $\phi_d = 19.6^\circ$ → $R = 1137 < V = 1326$ ✗ → $B = 2.4$: "
     r"$R = 1377 > V = 1352$ ✓."),
   EC7,
 ),
 sec("Q2 Inclined load", (3, 4),
   q("CE3116 Shallow Q2",
     r"A square pad at 1.0 m depth carries 500 kN permanent and 1500 kN variable vertical load plus an independent "
     r"variable horizontal load of 120 kN on its top (concrete $24\ \mathrm{kN/m^3}$; soil $c'_k = 10\ \mathrm{kPa}$, "
     r"$\phi'_k = 28^\circ$, $\gamma = 20$, water deep). Check $B = 2.39\ \mathrm{m}$.",
     r"**C1 $V = 3110 < R = 5384$ · C2 $V = 2587 < R = 2827$ → OK, C2 governs.**",
     r"Independent variable loads: the horizontal one takes $\psi_0 = 0.7$. $e = Hh/V$ → $B' = B - 2e$; shape and "
     r"inclination factors with $m = (2 + B'/L')/(1 + B'/L')$.")),
 sec("Q3 Tall column with a large moment", (5, 6),
   q("CE3116 Shallow Q3",
     r"A square pad at 1.2 m depth carries 300 kN permanent and 150 kN variable vertical load and an independent "
     r"variable horizontal load of 75 kN 5 m above founding level; $c' = 0$, $\phi'_k = 34^\circ$, water at founding "
     r"level, $\gamma = 19/21$. Find the width for drained conditions (ignore the column weight), also treating the "
     r"vertical load as favourable.",
     r"**$B \approx 2.84\ \mathrm{m}$** (2.64 m satisfies the check, plus 0.2 m because $e/B > 1/3$).",
     r"Vertical load is favourable for overturning → G with $\gamma = 1.0$, no variable vertical load. $B = 2.64$: C1 "
     r"$e = 1.12\ \mathrm{m}$ ($e/B = 0.43$), $B' = 0.39\ \mathrm{m}$, $V = 501 < R = 509$; C2 $V = 501 < R = 541$ → C1 "
     r"governs. (The slide's final '2.m' is a typo.)")),
]}

GEOQ[D["SLS"]] = {"code": "CE203", "title": "Foundations 4 · Stress distribution & settlement (CE3116 Tutorial)", "sections": [
 sec("Q1 Stress under an L-shaped footing", (2, 5),
   q("CE3116 Settlement Q1",
     r"An L-shaped footing made of three 2 m × 2 m squares carries 300 kPa. Find the stress increase 4 m below the "
     r"corner point A using (a) Fadum's chart and (b) Newmark's chart.",
     r"**(a) 76.5 kPa · (b) 76.5 kPa.**",
     r"(a) Three 2 × 2 rectangles with A at a corner: $m = n = 0.5$ → $I = 0.085$ → $3 \times 0.085 \times 300$. "
     r"(b) 51 blocks × $0.005 \times 300$.")),
 sec("Q2a Immediate settlement", (6, 9),
   ("eq", r"s_i = \mu_0\mu_1\frac{qB}{E},\qquad E_{ave} = \frac{\sum E_iH_i}{\sum H_i}"),
   q("CE3116 Settlement Q2(a)",
     r"A 6 m diameter tank applies 200 kPa to 1.5 m sand ($E = 20\ \mathrm{MPa}$) over 3 m clay ($E = 10$) over 1.5 m "
     r"sand ($E = 30\ \mathrm{MPa}$); water table 1.5 m. Estimate the average immediate settlement.",
     r"**$s_i \approx 27\ \mathrm{mm}$** ($E_{ave} = 17.5\ \mathrm{MPa}$, $\mu_0 = 0.4$, $\mu_1 = 1.0$).", "")),
 sec("Q2b–d Compression curve", (10, 13),
   q("CE3116 Settlement Q2(b)–(d)",
     r"For the clay ($\gamma_{\mathrm{sat}} = 17.52\ \mathrm{kN/m^3}$, $G_s = 2.73$) with the oedometer data on p. 10: "
     r"(b) plot $e$–$\log p'$, (c) find $p'_c$ by Casagrande, (d) correct the curve by Schmertmann and find $C_c$ and "
     r"the unload–reload index.",
     r"**$e_0 = 1.20$, $p'_0 = 38.6\ \mathrm{kPa}$ at mid-clay · $p'_c \approx 81\ \mathrm{kPa}$ (OC) · $C_c = 0.42$, "
     r"$C_{ur} = 0.08$.**", r"$w = 0.44$ → $e_0 = wG_s$; the field VCL passes through $0.42e_0$.")),
 sec("Q2e Consolidation settlement", (14, 17),
   ("eq", r"s_{oed} = \frac{H}{1+e_0}\left[C_{ur}\log\frac{p'_c}{p'_0} + C_c\log\frac{p'_0 + \Delta p}{p'_c}\right],\qquad s_c = \mu\,s_{oed}"),
   q("CE3116 Settlement Q2(e)",
     r"Estimate the consolidation settlement of the clay in two sub-layers (pore-pressure coefficient 0.8).",
     r"**Oedometer settlement 129 + 90 = 219 mm → $s_c = 0.9 \times 219 \approx 197\ \mathrm{mm}$.**",
     r"$\Delta p$ from the circular-load chart: 160 and 104 kPa; Skempton–Bjerrum $\mu = 0.9$ for $A = 0.8$.")),
 sec("Q2f–h Secondary compression & totals", (18, 21),
   ("eq", r"t_p = t_{100}\left(\frac{H_{field}}{H_{lab}}\right)^2,\qquad s_s = H\,C_\alpha\log\frac{t}{t_p}"),
   q("CE3116 Settlement Q2(f)–(h)",
     r"With $C_{\alpha} = 0.0035$ and $t_{100} = 82\ \mathrm{min}$ in a 2.7 cm double-drained oedometer sample, "
     r"estimate the secondary compression after 100 years and the total settlement immediately, after primary "
     r"consolidation and after 100 years.",
     r"**$t_p = 1.93\ \mathrm{yr}$, $s_s = 18\ \mathrm{mm}$ · totals 27 → 224 → 242 mm (immediate 11 %, primary "
     r"81 %, secondary 8 %).**",
     r"$t_p = 82 \times (1.5/0.0135)^2$ min; $s_s = 3000 \times 0.0035 \times \log(100/1.93)$.")),
]}

GEOQ[D["PILE"]] = {"code": "CE203", "title": "Foundations 5 · Piles to EC7: downdrag, load tests, tension (CE3116 Tutorial)", "sections": [
 sec("Q1 Downdrag", (1, 2),
   ("eq", r"q_s = K_s\sigma'_v\tan\delta'\ (\text{sand}),\qquad q_s = c_u = 0.3\sigma'_v\ (\text{soft NC clay}),\qquad D_k = \sum q_sA_s"),
   q("CE3116 Piles Q1",
     r"A 250 mm square precast pile ($23.4\ \mathrm{kN/m^3}$) carries 350 kN permanent and 150 kN variable load. It is "
     r"driven through 4 m of loose sand fill ($\gamma = 18$, $\phi'_k = 33^\circ$) placed on 10 m of very soft organic "
     r"clay ($\gamma = 15$, $c_{uk} = 0.3\sigma'_v$ above the preconsolidation pressure) to limestone; water 1 m below "
     r"the original ground. Find the downdrag force and the ULS design load.",
     r"**Downdrag 42.5 (sand) + 323.4 (clay) kN · design load C1 = 1219 kN, C2 = 931 kN.**",
     r"Sand $0.455 \times 36 \times 0.649 \times 4$; clay $0.3 \times 107.8 \times 10$; pile weight 20.5 kN. C1 = "
     r"$1.35(350 + 42.5 + 323.4 + 20.5) + 1.5 \times 150$. Downdrag is a permanent action; on rock take the full "
     r"value.")),
 sec("Q2 Resistance from load tests", (3, 4),
   q("CE3116 Piles Q2",
     r"Verify a 600 mm CFA pile, 11 m long, for 1200 kN permanent and 200 kN variable load. Two nearby trial piles were "
     r"taken to 4000 kN without failure (600 kN of it on the base). Ground: 2 m fill over very stiff glacial till. Use "
     r"the correlation factors.",
     r"**$R_{ck} = 2721\ \mathrm{kN}$ · C1 $F = 1920 < 2721$ · C2 $2721/1.7 = 1601 > F = 1460$ → OK; C2 governs "
     r"(ratio 1.10).**",
     r"$R_{ck} = \min(4000/1.47,\ 4000/1.35)$; split 15 % base / 85 % shaft. Pile weight is excluded — the test "
     r"already includes it.")),
 sec("Q3 Resistance from ground parameters", (5, 6),
   q("CE3116 Piles Q3",
     r"Same pile from ground parameters: till $c_{uk}$ rising from 100 kPa at 2 m to 600 kPa at 11 m, $\gamma = 22$, "
     r"$\phi'_{ks} = 36^\circ$ (shaft), $\phi'_{kb} = 34^\circ$ (base); fill 18 and concrete $24\ \mathrm{kN/m^3}$; "
     r"water at 2 m; $\alpha = 0.4$, $K_s = 1.5$.",
     r"**Undrained: $R_{bk} + R_{sk} = 1179 + 1758$ → C1 $2938 > 2021$, C2 $1950 > 1535$ ✓ · drained: $1386 + 1244$ "
     r"→ C2 $1815 > 1510$ ✓ (C2 governs).**",
     r"Undrained $q_b = 9c_u + \sigma_v$, $q_s = 0.4c_u$, model factor 1.35. Drained $N_q = 60$, $\delta' = 36^\circ$; "
     r"subtract 25 kN base uplift.")),
 sec("Q4–Q5 Tension piles under a flooded tank", (7, 9),
   q("CE3116 Piles Q4–Q5",
     r"A 10 m diameter tank (3200 kN) on dense sandy gravel ($\phi'_k = 40^\circ$, $\gamma = 22$) can be flooded 5 m "
     r"deep. Verify a 350 mm square precast tension pile driven 16 m: (Q4) from a nearby trial pile with ultimate "
     r"tension 2100 kN; (Q5) from ground parameters ($K_s = 1.5$, $\delta = 0.9\phi'_k$, water at the surface).",
     r"**Uplift $U_k = 3872$, $W_k = 3200\ \mathrm{kN}$ → net design uplift C1 907, C2 672 kN · test: C2 $R = 1290/1.7 "
     r"= 759 > 672$ ✓ · ground: $R_{tk} = 1538$ → C2 $1538/2.0 = 769 > 672$ ✓.**",
     r"$q_t = 1.5 \times 97.5 \times \tan 36^\circ = 106\ \mathrm{kPa}$. The slide divides 2000 instead of 2100 "
     r"(→ 1290 instead of 1355). Netting U − W before factoring treats uplift and tank weight as one source; factored "
     r"separately ($1.35U - 1.0W = 2027\ \mathrm{kN}$) C1 would fail, and EC7 UPL uses $\gamma_{\mathrm{dst}} = 1.0$ / "
     r"$\gamma_{\mathrm{stb}} = 0.9$ (≈ 992 kN). The two answers also use different $\gamma_{s,t}$ (1.7 vs 2.0) — check "
     r"the Singapore NA.")),
]}
