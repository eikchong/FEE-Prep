"""CE104 tutorial questions (OAP tutorials & assignment, CSC practice problems) as q blocks.

Full question statements are from the problem sheets in materials/CE104/tutorials; answers from the official
solutions unless marked otherwise. Numbers are recomputed in tests/test_tutorial_answers.py.
"""
from utils.qblock import q


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


_T = "CE104/tutorials/{}.pdf"
CT = {k: _T.format(k) for k in ["T_Tut1_Solutions", "T_Tut2_Solutions", "T_Classification_Examples_R1", "T_Assignment1",
                                "T_Seepage_A_Solutions", "T_Seepage_B_Solutions", "T_Shear_A_Solutions", "T_Shear_B_Solutions"]}

TUT1_PROFILE = (r"A sand profile has points A (0.0 m, ground surface), B (−2.0 m), C (−5.0 m) and D (−8.0 m). The "
                r"ground water table is at C (−5.0 m). Bulk unit weight $\gamma = 16\ \mathrm{kN/m^3}$ above the "
                r"water table and $19\ \mathrm{kN/m^3}$ below it; take $\gamma_w = 10\ \mathrm{kN/m^3}$.")

CE104Q = {}

CE104Q[CT["T_Tut1_Solutions"]] = {"code": "CE104", "title": "Practice · Tut 1 Effective stress (OAP)", "sections": [
 sec("Q1 Vertical stresses", (2, 2),
   q("OAP Tut 1 Q1",
     TUT1_PROFILE + r" Calculate at points A to D, and plot with depth: (a) the total vertical stress $\sigma_v$, "
     r"(b) the pore water pressure $u$, (c) the effective vertical stress $\sigma'_v$.",
     r"**A: 0 / 0 / 0 · B: 32 / 0 / 32 · C: 80 / 0 / 80 · D: 137 / 30 / 107 kPa** ($\sigma_v$ / $u$ / $\sigma'_v$).",
     r"B: $\sigma_v = 2 \times 16 = 32$. C: $\sigma_v = 5 \times 16 = 80$, still dry so $u = 0$. D: $\sigma_v = 5 "
     r"\times 16 + 3 \times 19 = 137$, $u = 3 \times 10 = 30$, $\sigma'_v = 137 - 30 = 107$. Stresses vary linearly "
     r"between these points. Any capillary rise above the water table would give negative $u$ (suction), making "
     r"$\sigma' > \sigma$ in that zone.",
     figure="p. 2: soil column with A–D and the water table at C.")),
 sec("Q2 Horizontal stresses", (3, 4),
   q("OAP Tut 1 Q2",
     r"For the same profile as Q1, the effective horizontal stress is $\sigma'_h = K_0\sigma'_v$ with $K_0 = 0.43$. "
     r"Calculate at points A to D, and plot with depth: (a) the effective horizontal stress $\sigma'_h$, (b) the total "
     r"horizontal stress $\sigma_h$.",
     r"**$\sigma'_h$: A 0, B 13.8, C 34.4, D 46.0 kPa · $\sigma_h$: A 0, B 13.8, C 34.4, D 76.0 kPa.**",
     r"$\sigma'_h = 0.43\sigma'_v$: B $0.43 \times 32 = 13.76$, C $0.43 \times 80 = 34.4$, D $0.43 \times 107 = 46.0$. "
     r"Then $\sigma_h = \sigma'_h + u$: only D has pore pressure, $46.0 + 30 = 76.0$. Apply $K_0$ to the "
     r"**effective** stress only, never to the total stress.")),
 sec("Q3 Rise of the water table", (5, 5),
   q("OAP Tut 1 Q3",
     r"After prolonged rainfall the ground water table rises to 3 m below the ground surface (−3.0 m). (a) Check the "
     r"effective vertical stress at point C. (b) Without calculation, comment on the effect of the rise on the soil "
     r"strength at C.",
     r"**(a) $\sigma'_v = 66\ \mathrm{kPa}$ at C (was 80 kPa). (b) Lower effective stress → lower frictional "
     r"strength at C.**",
     r"$\sigma_v = 3 \times 16 + 2 \times 19 = 86$; $u = 2 \times 10 = 20$; $\sigma'_v = 86 - 20 = 66\ \mathrm{kPa}$. "
     r"Soil strength is frictional, $\tau_f = \sigma'\tan\phi'$, so it falls with $\sigma'$.")),
]}

CE104Q[CT["T_Tut2_Solutions"]] = {"code": "CE104", "title": "Practice · Tut 2 Phase relationships (OAP)", "sections": [
 sec("Q1 Moist soil sample", (2, 3),
   q("OAP Tut 2 Q1",
     r"In its natural state a moist soil has a volume of $10\,000\ \mathrm{cm^3}$ and weighs 18 kg. Its dry weight is "
     r"15.5 kg. Taking $G_s = 2.70$, calculate (a) the water content, (b) the bulk unit weight, (c) the dry unit "
     r"weight, (d) the void ratio, (e) the porosity and (f) the degree of saturation.",
     r"**(a) $w = 16.1\,\%$ · (b) $\gamma = 17.66\ \mathrm{kN/m^3}$ · (c) $\gamma_d = 15.21\ \mathrm{kN/m^3}$ · "
     r"(d) $e = 0.78$ · (e) $n = 0.44$ · (f) $S_r = 56\,\%$.**",
     r"$w = (18 - 15.5)/15.5 = 0.161$. $\gamma = 18 \times 9.81/1000/0.01 = 17.66$; $\gamma_d = 15.5 \times "
     r"9.81/1000/0.01 = 15.21$. $e = G_s\gamma_w/\gamma_d - 1 = 2.7 \times 10/15.21 - 1 = 0.78$; $n = e/(1 + e) = "
     r"0.44$; $S_r = wG_s/e = 0.161 \times 2.70/0.78 = 0.56$.\n\n"
     r"Note: the solution lists '$M_s = 15.1\ \mathrm{kg}$' (a typo; its numbers use 15.5 kg) and mixes $g = 9.81$ "
     r"(for $\gamma_d$) with $\gamma_w = 10$ (for $e$). With $\gamma_w = 9.81$ throughout, $e = 0.74$, $n = 0.43$ "
     r"and $S_r = 59\,\%$. This is listed in the answer-check report.")),
 sec("Q2 Loosest and densest states", (4, 5),
   q("OAP Tut 2 Q2",
     r"To find $e_{\max}$ and $e_{\min}$ of a sand with $G_s = 2.65$: dry sand poured from a height into a "
     r"$1000\ \mathrm{cm^3}$ container weighs 1.4 kg; a fully saturated sample of the same sand vibrated under water "
     r"fills the same container with 2.1 kg. Compute (a) $e_{\max}$, (b) $e_{\min}$, (c) the dry unit weight in the "
     r"loosest state and (d) the dry unit weight in the densest state.",
     r"**(a) $e_{\max} = 0.93$ · (b) $e_{\min} = 0.56$ · (c) $\gamma_{d,\min} = 13.73\ \mathrm{kN/m^3}$ · "
     r"(d) $\gamma_{d,\max} = 17.0\ \mathrm{kN/m^3}$.**",
     r"Loose: $\gamma_d = 1.4 \times 9.81/1000/0.001 = 13.73$ → $e_{\max} = 2.65 \times 10/13.73 - 1 = 0.93$. "
     r"Dense, saturated: $\gamma = 2.1 \times 9.81/1000/0.001 = 20.60$; from $\gamma = (G_s + e)\gamma_w/(1 + e)$, "
     r"$e = (G_s\gamma_w - \gamma)/(\gamma - \gamma_w) = (26.5 - 20.60)/(20.60 - 10) = 0.56$ → $\gamma_{d,\max} = "
     r"26.5/1.56 = 17.0$.\n\nNote: as in Q1, the solution mixes $g = 9.81$ and $\gamma_w = 10$; see the "
     r"answer-check report.")),
 sec("Q3 In-situ state of the sand", (6, 7),
   q("OAP Tut 2 Q3",
     r"The sand of Q2 is to be used as a compaction material. In situ it has a water content of 15 % and a degree of "
     r"saturation of 55 % ($G_s = 2.65$). Determine (a) the void ratio, (b) the relative density, (c) the packing "
     r"state and (d) the in-situ dry unit weight.",
     r"**(a) $e = 0.72$ · (b) $D_R = 57\,\%$ · (c) medium dense · (d) $\gamma_d = 15.4\ \mathrm{kN/m^3}$.**",
     r"$e = wG_s/S_r = 0.15 \times 2.65/0.55 = 0.72$; $D_R = (e_{\max} - e)/(e_{\max} - e_{\min}) = (0.93 - "
     r"0.72)/(0.93 - 0.56) = 0.57$; bands: very loose 0–15, loose 15–35, **medium dense 35–65**, dense 65–85, very "
     r"dense 85–100 %. $\gamma_d = G_s\gamma_w/(1 + e) = 26.5/1.72 = 15.4$.")),
 sec("Q4 Borrow pit to compacted fill", (8, 9),
   q("OAP Tut 2 Q4",
     r"Soil from a borrow area (in-situ void ratio 0.93) is excavated to build a compacted fill (target void ratio "
     r"0.54) over an area 200 m × 200 m, 2 m deep. $G_s = 2.70$. (a) Estimate the volume to excavate at the borrow "
     r"area. (b) After compaction the water content is 14 %: calculate the bulk unit weight and the percentage of "
     r"air voids. (c) If the site floods and the fill becomes saturated, find the new water content.",
     r"**(a) $V_{\mathrm{borrow}} \approx 100\,260\ \mathrm{m^3}$ · (b) $\gamma = 20.0\ \mathrm{kN/m^3}$, air voids "
     r"$10.5\,\%$ · (c) $w = 20\,\%$.**",
     r"Solids volume is conserved: $V_s = 80\,000/1.54 = 51\,948\ \mathrm{m^3}$ → $V_{\mathrm{borrow}} = 51\,948 "
     r"\times 1.93 = 100\,260\ \mathrm{m^3}$. $\gamma = G_s\gamma_w(1 + w)/(1 + e) = 27 \times 1.14/1.54 = 20.0$; "
     r"$A_v = V_a/V = (e - wG_s)/(1 + e) = (0.54 - 0.378)/1.54 = 10.5\,\%$. Saturated: $w = e/G_s = 0.54/2.70 = "
     r"20\,\%$.")),
 sec("Q5 Cement-treated soft clay", (10, 14),
   q("OAP Tut 2 Q5",
     r"A saturated soft clay has water content 75 % and $G_s = 2.70$. Cement ($G_c = 3.1$) is mixed in as a slurry "
     r"to give an admixture with cement content (cement/soil solids) 20 % and water content (water/(soil solids + "
     r"cement)) 120 %. Per 1 kg of soil solids determine (a) the cement to add, (b) the extra water to add, (c) the "
     r"water/cement ratio of the slurry; also (d) the volume of slurry per $1\ \mathrm{m^3}$ of clay and (e) the bulk "
     r"unit weight of the admixture (assume saturated).",
     r"**(a) 0.20 kg · (b) 0.69 kg · (c) 3.45 · (d) $0.673\ \mathrm{m^3}$ · (e) $14.1\ \mathrm{kN/m^3}$.**",
     r"(a) $c = 0.2s$. (b) $(0.75 + \Delta w)/(1 + 0.2) = 1.2$ → $\Delta w = 0.69\ \mathrm{kg}$. (c) $0.69/0.20 = "
     r"3.45$. (d) Clay: $e = wG_s = 2.025$, $\gamma_d = 27/3.025 = 8.92\ \mathrm{kN/m^3}$, so $1\ \mathrm{m^3}$ holds "
     r"8.92 kN of solids; slurry volume $= 0.2(8.92)/31 + 0.69(8.92)/10 = 0.673\ \mathrm{m^3}$. (e) Per 1 kN of soil "
     r"solids the admixture weighs $1 + 0.2 + 1.44 = 2.64\ \mathrm{kN}$ and occupies $1/27 + 0.2/31 + 1.44/10 = "
     r"0.187\ \mathrm{m^3}$ → $\gamma = 14.1\ \mathrm{kN/m^3}$.")),
]}

CE104Q[CT["T_Classification_Examples_R1"]] = {"code": "CE104", "title": "Practice · Soil classification examples (USCS & BS EN ISO 14688)", "sections": [
 sec("USCS (ASTM D2487) rules", (2, 3),
   ("steps", ["> 50 % passing 0.075 mm → fine-grained (M/C/O by plasticity chart, A-line); else coarse.",
              "Coarse: G or S by the larger of gravel (75–4.75 mm) / sand (4.75–0.075 mm).",
              r"Fines < 5 %: W or P from grading (GW: $C_u > 4$, SW: $C_u > 6$, and $1 \le C_c \le 3$ for both).",
              "Fines > 12 %: M or C from the plasticity chart. 5–12 %: dual symbol (e.g. GW-GM)."]),
   ("eq", r"C_u = \frac{D_{60}}{D_{10}},\qquad C_c = \frac{D_{30}^2}{D_{10}D_{60}}"),
 ),
 sec("BS EN ISO 14688-2 rules", (4, 6),
   ("md", "Fine if > **35 %** passes 0.063 mm (soil sticks together when wet). Gravel 63–2 mm, sand 2–0.063 "
          r"mm. Secondary terms by proportion: e.g. 'slightly sandy' ($< 20\,\%$), 'sandy', 'very sandy' (> 20 % in "
          r"coarse soils, Table 1A). Grading: well graded $C_u > 15$ and $1 < C_c < 3$; uniform $C_u < 3$; gap graded "
          r"$C_c < 0.5$."),
 ),
 sec("Soils A to E", (7, 20),
   q("OAP classification A–E",
     r"Five soils A–E are given with particle-size distribution curves and Atterberg limits (pp. 7–20). For each soil, "
     r"(a) give the USCS group symbol (ASTM D2487) and (b) write the BS EN ISO 14688 description. Key data: A has 25 % "
     r"fines plotting below the A-line; D has 4 % fines with $C_u = 1.9$, $C_c = 0.92$; E has 10 % fines with "
     r"$C_u = 26$, $C_c = 0.1$.",
     r"**USCS: A GM · B CH · C ML · D SP · E GP-GM. BS: A very sandy, well graded GRAVEL · B high plasticity CLAY · "
     r"C slightly sandy, low plasticity SILT · D slightly silty, uniformly graded SAND · E very sandy, gap graded "
     r"GRAVEL.**",
     r"A: gravel with > 12 % fines below the A-line → GM. D: < 5 % fines, $C_u < 6$ → poorly graded → SP. E: 5–12 % "
     r"fines needs a dual symbol; $C_c = 0.1$ fails $1 \le C_c \le 3$ so the first symbol is GP, giving **GP-GM**. "
     r"The slides print 'GW' for E; the BS description ('gap graded') agrees with the poorly-graded reading.",
     figure="pp. 7–20: grading curves and plasticity-chart points for soils A–E.")),
]}

CE104Q[CT["T_Assignment1"]] = {"code": "CE104", "title": "Practice · Assignment 1 basic characteristics", "sections": [
 sec("Q1 Layered profile with capillary rise", (1, 1),
   q("OAP Assignment 1 Q1",
     r"A soil profile under a long slope: from the ground surface (0.0 m) the soil has $\gamma = 18\ \mathrm{kN/m^3}$ "
     r"($K_0 = 0.6$) above the original water table at −2.0 m and $19\ \mathrm{kN/m^3}$ ($K_0 = 0.6$) below it, down "
     r"to an impermeable layer from −5.0 to −6.0 m ($\gamma = 21\ \mathrm{kN/m^3}$). Below that a layer with "
     r"$\gamma = 21\ \mathrm{kN/m^3}$, $K_0 = 0.45$ lies between impermeable layers and is recharged where it "
     r"outcrops up the slope, 7 m above the ground level. Points: A at −1.0 m, B at −5.0 m, C at −8.0 m. "
     r"$\gamma_w = 10\ \mathrm{kN/m^3}$. (a) Calculate the total horizontal stress $\sigma_h$ at A, B and C, with "
     r"capillary rise to 1 m above the original water table. (b) If the water table rises to 1 m above the ground "
     r"surface, recalculate the effective vertical stress at A, B and C (take $19\ \mathrm{kN/m^3}$ at A when submerged) and comment "
     r"on the soil strength.",
     r"**(a) $\sigma_h$: A 6.8, B 67.8, C 152.7 kPa · (b) $\sigma'_v$: A 9 (was 28), B 45 (was 63), C 18 (was 6) "
     r"kPa** — strength falls at A and B; C, in the confined layer, gains effective stress because its pore pressure "
     r"is set by the recharge level, not the new water table.",
     r"(a) A: $\sigma_v = 18$, $u = -10$ (capillary suction, 1 m above the water table) → $\sigma'_v = 28$, "
     r"$\sigma'_h = 0.6 \times 28 = 16.8$, $\sigma_h = 16.8 - 10 = 6.8$. B: $\sigma_v = 2 \times 18 + 3 \times 19 = "
     r"93$, $u = 30$ → $\sigma'_v = 63$, $\sigma'_h = 37.8$, $\sigma_h = 67.8$. C: $\sigma_v = 93 + 21 + 2 \times 21 "
     r"= 156$, $u = 10 \times (7 + 8) = 150$ (artesian) → $\sigma'_v = 6$, $\sigma'_h = 0.45 \times 6 = 2.7$, "
     r"$\sigma_h = 152.7$.\n\n(b) 1 m of water over the ground: A: $\sigma_v = 10 + 19 = 29$, $u = 20$ → 9. B: "
     r"$\sigma_v = 10 + 5 \times 19 = 105$, $u = 60$ → 45. C: $\sigma_v = 105 + 21 + 42 = 168$, $u = 150$ → 18.\n\n"
     r"Read from the figure (no official solution): the water table is the red line at −2.0 m and A sits 1 m above "
     r"it; the confined layer's head is taken at the +7 m recharge level.",
     figure="p. 1: profile under a slope; water table, layers and points A–C.", src="claude")),
 sec("Q2 Compaction material", (1, 2),
   q("OAP Assignment 1 Q2",
     r"A compaction material has bulk unit weight $18\ \mathrm{kN/m^3}$, in-situ water content 10 %, $G_s = 2.70$, "
     r"LL = 25 %, PL = 22 % and the grading curve on p. 2 (about 27 % finer than 0.063 mm, 4 % finer than 0.002 mm, "
     r"no gravel). (a) Classify it by the USCS. (b) Find the weights of clay, silt and sand solids and of water in "
     r"$1\ \mathrm{m^3}$. (c) The specification is dry density $17.5\ \mathrm{kN/m^3}$ and degree of saturation "
     r"90 %: how much water must be added to every 100 kg of in-situ soil?",
     r"**(a) SM (silty sand) · (b) per $\mathrm{m^3}$: clay ≈ 0.65 kN, silt ≈ 3.8 kN, sand ≈ 12.0 kN, water 1.64 kN · "
     r"(c) add ≈ 7.4 kg of water per 100 kg.**",
     r"(a) Fines ≈ 27 % (< 50 %) → coarse; no gravel → S; fines > 12 % with $\mathrm{PI} = 3 < 4$ (below the A-line) "
     r"→ **SM**. (b) Weight 18 kN, $w = 10\,\%$ → solids $18/1.1 = 16.36\ \mathrm{kN}$, water 1.64 kN; split the "
     r"solids 4 % clay, 23 % silt, 73 % sand (read from the curve, ±2 %). (c) 100 kg = 90.91 kg solids + 9.09 kg "
     r"water. Target $e = 27/17.5 - 1 = 0.543$ → $w = S_re/G_s = 0.9 \times 0.543/2.70 = 18.1\,\%$ → water needed "
     r"$0.181 \times 90.91 = 16.45\ \mathrm{kg}$ → add $16.45 - 9.09 = 7.4\ \mathrm{kg}$.",
     figure="p. 2: particle-size distribution curve.", src="claude")),
 sec("Q3 Sludge + sand + lime landfill", (3, 4),
   q("OAP Assignment 1 Q3",
     r"Sludge is to be mixed with sand and lime (added as a lime–water slurry) so that the solids are in the mass "
     r"ratio sludge : sand : lime = 1.0 : 2.0 : 0.5. Stockpiled sludge: $G_R = 1.2$, $w = 50\,\%$, $\gamma_d = 5\ "
     r"\mathrm{kN/m^3}$. Stockpiled sand: $G_s = 2.65$, $w = 12\,\%$, $e = 1.0$. Lime: $G_L = 3.4$. Estimate (a) the "
     r"void ratio and degree of saturation of the sludge, (b) the dry unit weight of the sand, (c) the mass of "
     r"stockpiled sand to mix with 1 kg of stockpiled sludge, (d) the volume of stockpiled sand to treat "
     r"$1\ \mathrm{m^3}$ of sludge, and (e) the water/lime mass ratio of the slurry so that the final admixture has a "
     r"water content (water/total solids) of 50 %.",
     r"**(a) $e = 1.4$, $S_r = 43\,\%$ · (b) $\gamma_d = 13.25\ \mathrm{kN/m^3}$ · (c) 1.49 kg · (d) $0.755\ "
     r"\mathrm{m^3}$ · (e) water : lime ≈ 2.0.**",
     r"(a) $e = G_R\gamma_w/\gamma_d - 1 = 12/5 - 1 = 1.4$; $S_r = wG_R/e = 0.5 \times 1.2/1.4 = 0.43$. (b) "
     r"$26.5/2 = 13.25$. (c) 1 kg sludge = 0.667 kg solids → 1.333 kg sand solids → $1.333 \times 1.12 = 1.49\ "
     r"\mathrm{kg}$ of stockpiled sand. (d) $1\ \mathrm{m^3}$ sludge = 5 kN solids → 10 kN sand solids → $10/13.25 = "
     r"0.755\ \mathrm{m^3}$. (e) Per 1 kg sludge solids: total solids 3.5 kg, water needed $0.5 \times 3.5 = 1.75$; "
     r"already present $0.5 + 2 \times 0.12 = 0.74$; slurry water $1.01\ \mathrm{kg}$ for 0.5 kg lime → 2.0.",
     src="claude")),
]}

CE104Q[CT["T_Seepage_A_Solutions"]] = {"code": "CE104", "title": "Practice · Seepage A — gradients, quick condition, permeameters (CSC)", "sections": [
 sec("Q1 Quick condition", (1, 2),
   q("CSC Seepage A Q1",
     r"A soil sample ($\gamma_{\mathrm{sat}} = 20\ \mathrm{kN/m^3}$, length $L = 5\ \mathrm{m}$) sits in a tube with "
     r"2 m of water above it ($h_w = 2\ \mathrm{m}$); a riser on the left keeps the inflow head $h$ above the top "
     r"water level, so water flows upward through the soil. (a) Evaluate the critical hydraulic gradient. (b) Find "
     r"the head $h$ that causes quick conditions. (c) Compute the seepage force per unit volume at quick conditions. "
     r"(d) Show with seepage forces that quick conditions develop under the head of (b).",
     r"**(a) $i_c = 1$ · (b) $h = 5\ \mathrm{m}$ · (c) $j = 10\ \mathrm{kN/m^3}$ · (d) upward seepage force $50A$ = "
     r"buoyant weight $50A$.**",
     r"(a) $i_c = \gamma'/\gamma_w = 10/10 = 1$. (b) Datum at the bottom: $h_P = 5 + 2 + h$, $h_Q = 2 + 5 = 7$ → "
     r"$i = h/5 = 1$ → $h = 5\ \mathrm{m}$. (c) $j = \gamma_wi_c = 10$. (d) Seepage force on the column $jAL = 10 "
     r"\times 5A = 50A$ upward; buoyant weight $\gamma'AL = 10 \times 5A = 50A$ downward → the soil 'floats'.",
     figure="p. 1, Figure 1: upward-flow permeameter with riser tube.")),
 sec("Q2 Downward flow", (3, 3),
   q("CSC Seepage A Q2",
     r"Same set-up as Q1, but the water level in the left-hand riser is held at elevation C, 2 m above the base of the "
     r"sample (elevation A). Compute (a) the hydraulic gradient, (b) the effective stress at elevation A and (c) the "
     r"seepage force per unit volume.",
     r"**(a) $i = -1$ (downward) · (b) $\sigma'_A = 100\ \mathrm{kPa}$ · (c) $j = 10\ \mathrm{kN/m^3}$ acting "
     r"downward.**",
     r"$h_P = 2$, $h_Q = 7$ → $i = (2 - 7)/5 = -1$. $\sigma_A = 20 \times 5 + 10 \times 2 = 120$, $u_A = 2 \times 10 = "
     r"20$ → $\sigma' = 100$. Downward flow adds to the effective stress.")),
 sec("Q3 Artesian sand below clay", (4, 5),
   q("CSC Seepage A Q3",
     r"A 4 m clay layer ($\gamma_{\mathrm{sat}} = 20\ \mathrm{kN/m^3}$) lies under 4 m of sand ($\gamma_{\mathrm{sat}} = "
     r"19$, $\gamma_{\mathrm{dry}} = 16.5\ \mathrm{kN/m^3}$) whose top is the ground surface. The water table is 2 m "
     r"below ground. The clay sits on sand under artesian pressure: water in a standpipe rises 4 m above the ground. "
     r"Calculate the effective vertical stress at the top and base of the clay. If the dry sand is excavated, at what "
     r"depth will the effective stress at the base of the clay become zero?",
     r"**Top of clay 51 kPa · base of clay 31 kPa · excavation depth ≈ 1.9 m.**",
     r"Top: $\sigma = 16.5 \times 2 + 19 \times 2 = 71$, $u = 20$ → 51. Base: $\sigma = 71 + 20 \times 4 = 151$, "
     r"$u = 10 \times 12 = 120$ → 31. Removing $d$ of dry sand: $31 - 16.5d = 0$ → $d = 1.88 \approx 1.9\ "
     r"\mathrm{m}$. (The short-answer sheet repeats '51' for the base; it is 31.)")),
 sec("Q4 Base heave", (6, 6),
   q("CSC Seepage A Q4",
     r"A 10 m clay layer (unit weight $17.5\ \mathrm{kN/m^3}$) overlies sand; its top is the ground surface. An "
     r"excavation in the clay failed when it reached 6.5 m depth. Calculate the depth of water in a standpipe sunk to "
     r"the sand layer.",
     r"**Water stands 3.875 m below the ground surface (6.125 m above the top of the sand).**",
     r"At failure $\sigma'$ at the base of the clay is zero: $17.5 \times (10 - 6.5) - 10(10 - d) = 0$ → $d = 3.875\ "
     r"\mathrm{m}$, where $d$ is the depth of the standpipe water level below the ground.")),
 sec("Q5–Q6 Constant-head tests", (7, 8),
   ("eq", r"k = \frac{QL}{hAt},\qquad v_s = \frac{v}{n}"),
   q("CSC Seepage A Q5",
     r"A sand sample 5 cm in diameter and 15 cm long, prepared at porosity 60 %, is tested in a constant-head "
     r"permeameter. The total head is kept at 30 cm and $40\ \mathrm{cm^3}$ of water is collected in 5 s at 20 °C. "
     r"Calculate the coefficient of permeability and the seepage velocity.",
     r"**$k = 0.204\ \mathrm{cm/s}$ · $v_s = 0.68\ \mathrm{cm/s}$.**",
     r"$A = \pi \times 5^2/4 = 19.63\ \mathrm{cm^2}$; $k = QL/(hAt) = 40 \times 15/(30 \times 19.63 \times 5) = 0.204$; "
     r"$v = ki = 0.204 \times 30/15 = 0.407$; $v_s = v/n = 0.407/0.6 = 0.68\ \mathrm{cm/s}$."),
   q("CSC Seepage A Q6",
     r"A constant-head cell of 75 mm internal diameter has tappings A, B, C at 100 mm vertical spacing. Three tests "
     r"(upward flow) give Q = 281.5, 422.5 and 591.0 ml per 10 minutes, with heads above datum at A/B/C of "
     r"139.0/100.0/60.0, 208.5/150.5/91.5 and 292.0/210.0/127.0 mm. Determine k in m/s (average of the six values).",
     r"**$k \approx 2.70 \times 10^{-4}\ \mathrm{m/s}$.**",
     r"$A = 44.2\ \mathrm{cm^2}$, $t = 600\ \mathrm{s}$, $L = 10\ \mathrm{cm}$ between tappings. For each test use "
     r"the A–B and B–C head drops, e.g. test 1: $k = 281.5 \times 10/(3.9 \times 44.2 \times 600) = 0.0272\ "
     r"\mathrm{cm/s}$. The six values lie between 0.0265 and 0.0272 cm/s; mean $0.0270\ \mathrm{cm/s}$.")),
 sec("Q7–Q8 Falling-head tests", (9, 10),
   ("eq", r"k = \frac{aL}{At}\ln\frac{h_1}{h_2},\qquad k_{20} = k_TR_T,\ R_T = 2.42 - 0.475\ln T"),
   q("CSC Seepage A Q7",
     r"Falling-head test on a silty clay: sample area $80\ \mathrm{cm^2}$, length 10 cm, head falls from 90 cm to "
     r"84 cm in 15 minutes, standpipe diameter 6 mm, temperature 22 °C. Determine k at the reference temperature of "
     r"20 °C, using $k_{20} = k_TR_T$ with $R_T = 2.42 - 0.475\ln T$.",
     r"**$k_{20} = 2.57 \times 10^{-6}\ \mathrm{cm/s}$.**",
     r"$a = \pi \times 0.6^2/4 = 0.283\ \mathrm{cm^2}$; $k_{22} = 0.283 \times 10/(80 \times 900)\ln(90/84) = 2.70 "
     r"\times 10^{-6}\ \mathrm{cm/s}$; $R_{22} = 2.42 - 0.475\ln 22 = 0.952$ → $2.57 \times 10^{-6}$."),
   q("CSC Seepage A Q8",
     r"A falling-head test in a cell 100 mm in diameter and 127 mm high gave $h_1 = 560\ \mathrm{mm}$, $h_2 = 465\ "
     r"\mathrm{mm}$ in $t = 1081\ \mathrm{s}$ with a 7 mm standpipe. Determine (a) k in m/s and (b) the time for the "
     r"same head drop with a 4 mm standpipe.",
     r"**(a) $k = 1.07 \times 10^{-7}\ \mathrm{m/s}$ · (b) $t \approx 353\ \mathrm{s}$.**",
     r"(a) $a = 3.85 \times 10^{-5}$, $A = 7.854 \times 10^{-3}\ \mathrm{m^2}$; $k = aL\ln(h_1/h_2)/(At) = 1.07 "
     r"\times 10^{-7}$. (b) For the same k and heads $t \propto a$: $1081 \times (4/7)^2 = 353\ \mathrm{s}$.")),
]}

CE104Q[CT["T_Seepage_B_Solutions"]] = {"code": "CE104", "title": "Practice · Seepage B — flow nets, sheet piles, dams (CSC)", "sections": [
 sec("Q1 Sheet pile flow net", (1, 3),
   ("eq", r"q = kH\frac{N_f}{N_d}"),
   q("CSC Seepage B Q1",
     r"A sheet pile retains 4.5 m of water upstream with 1.5 m downstream (head loss $H = 3\ \mathrm{m}$); the "
     r"geometry, element A and the impermeable stratum are as in Figure 1. The flow net has $N_f = 5$ and $N_d = 11$. "
     r"$k = 0.02\ \mathrm{mm/s}$, $\gamma_{\mathrm{sat}} = 20\ \mathrm{kN/m^3}$. (a) Estimate the flow in "
     r"$\mathrm{m^3/day}$ per metre run. (b) For element A ($l = 1.5\ \mathrm{m}$, 2.5 drops from upstream) find the "
     r"average velocity and the effective vertical stress. (c) Find the effective vertical stress at the toe of the "
     r"pile on its downstream side. (d) Find the factor of safety against quick conditions, defined as critical over "
     r"existing gradient along the downstream face.",
     r"**(a) $q = 2.36\ \mathrm{m^3/day/m}$ · (b) $v = 0.0131\ \mathrm{m/h}$, $\sigma'_A = 51.8\ \mathrm{kPa}$ · "
     r"(c) $\sigma' = 17.4\ \mathrm{kPa}$ · (d) FoS = 2.21.**",
     r"(a) $q = 2 \times 10^{-5} \times 3 \times 5/11 = 2.73 \times 10^{-5}\ \mathrm{m^3/s} = 2.36\ "
     r"\mathrm{m^3/day}$. (b) $v = ki = 2 \times 10^{-5} \times (3/11)/1.5 = 3.64 \times 10^{-6}\ \mathrm{m/s}$; head "
     r"lost to A $3 \times 2.5/11 = 0.68\ \mathrm{m}$ → $u = 53.2$ → $\sigma'_A = 51.8\ \mathrm{kPa}$ (45 with no "
     r"flow). (c) Lost to the toe $3 \times 6/11 = 1.64\ \mathrm{m}$ → $u = 43.6$, $\sigma = 60$ → 17.4. (d) Exit "
     r"gradient along the downstream face $(7.36 - 6)/3 = 0.453$ → $i_c/i = 1/0.453 = 2.21$.",
     figure="p. 1, Figure 1: sheet pile with flow net, element A.")),
 sec("Q2 Piezometers around a sheet pile", (4, 5),
   q("CSC Seepage B Q2",
     r"A flow net for flow round a single row of sheet piles has $N_f = 3$ and $N_d = 6$, with 5 m of water upstream "
     r"and 1.5 m downstream (head loss 3.5 m); $k = 4.2 \times 10^{-3}\ \mathrm{cm/s}$. Points a, b, c, d lie after "
     r"1, 2, 5 and 5 potential drops. Determine (a) how high above the ground the water rises in piezometers at a, b, "
     r"c and d, and (b) the seepage per metre run.",
     r"**(a) a 4.42 m, b 3.83 m, c 2.08 m, d 2.08 m · (b) $q = 7.35 \times 10^{-5}\ \mathrm{m^3/s}$ per m.**",
     r"Each drop loses $3.5/6 = 0.583\ \mathrm{m}$; height above ground $= 5 - n_d \times 0.583$. "
     r"$q = 4.2 \times 10^{-5} \times 3.5 \times 3/6 = 7.35 \times 10^{-5}$.",
     figure="p. 2, Figure 2: flow net and points a–d.")),
 sec("Q3–Q4 Draw your own flow net", (6, 7),
   q("CSC Seepage B Q3",
     r"Sheet pile with upstream water depth $H_1 = 6\ \mathrm{m}$, downstream $H_2 = 1.5\ \mathrm{m}$, embedment "
     r"$D = 3\ \mathrm{m}$ in a layer $D_1 = 6\ \mathrm{m}$ thick over an impermeable base; $k = 4 \times 10^{-4}\ "
     r"\mathrm{cm/s}$. Draw the flow net and calculate the seepage per metre run.",
     r"**$q \approx 0.78\ \mathrm{m^3/day}$ per m** (flow net $N_f/N_d \approx 4/8$).",
     r"$q = kHN_f/N_d = 4 \times 10^{-6} \times 4.5 \times 4/8 = 9.0 \times 10^{-6}\ \mathrm{m^3/s} = 0.78\ "
     r"\mathrm{m^3/day}$.", figure="p. 3, Figure 3: sheet pile geometry."),
   q("CSC Seepage B Q4",
     r"Same arrangement as Q3 with $H_1 = 3\ \mathrm{m}$, $H_2 = 0.5\ \mathrm{m}$, $D = 1.5\ \mathrm{m}$, "
     r"$D_1 = 3.75\ \mathrm{m}$. Draw the flow net and calculate the seepage per metre run.",
     r"**$q \approx 0.52\ \mathrm{m^3/day}$ per m** (flow net $N_f/N_d \approx 3/5$).",
     r"$q = 4 \times 10^{-6} \times 2.5 \times 3/5 = 6.0 \times 10^{-6}\ \mathrm{m^3/s} = 0.52\ \mathrm{m^3/day}$.")),
 sec("Q5–Q7 Concrete dam", (8, 10),
   q("CSC Seepage B Q5",
     r"A concrete dam with an 11 m base retains 5 m of water; the downstream water is 1 m above the ground (head loss "
     r"4 m). It sits on a 9.5 m isotropic permeable layer ($k = 10^{-5}\ \mathrm{m/s}$) over an impermeable stratum. "
     r"Sketch the flow net and calculate the flow under the dam in $\mathrm{m^3/day}$ per metre.",
     r"**$q \approx 1.73\ \mathrm{m^3/day}$ per m** ($N_f/N_d \approx 3/6$).",
     r"$q = 10^{-5} \times 4 \times 3/6 \times 86\,400 = 1.73$. (The solution text mentions an '8 m' base/layer — a "
     r"leftover typo; the figure and answer are for 11 m on 9.5 m.)", figure="p. 4, Figure 5."),
   q("CSC Seepage B Q6",
     r"As Q5 but with a 5 m dam base. Sketch the flow net and calculate the flow under the dam.",
     r"**$q \approx 2.16\ \mathrm{m^3/day}$ per m** ($N_f/N_d \approx 5/8$).",
     r"$q = 10^{-5} \times 4 \times 5/8 \times 86\,400 = 2.16$. A shorter base shortens the seepage path, so flow and "
     r"exit gradient rise.", figure="p. 4, Figure 6."),
   q("CSC Seepage B Q7",
     r"As Q6 (5 m base) with a 5 m horizontal impermeable blanket added upstream. Sketch the flow net and calculate "
     r"the flow under the dam.",
     r"**$q \approx 1.73\ \mathrm{m^3/day}$ per m** ($N_f/N_d \approx 4/8$).",
     r"$q = 10^{-5} \times 4 \times 4/8 \times 86\,400 = 1.73$. The blanket lengthens the seepage path like a longer "
     r"base.", figure="p. 5, Figure 7.")),
 sec("Q8–Q9 Dam on silty sand", (11, 13),
   q("CSC Seepage B Q8",
     r"A dam retaining 10 m of water stands on silty sand ($k = 2 \times 10^{-3}\ \mathrm{cm/s}$) over an "
     r"impermeable layer. Sketch the flow net and estimate the flow beneath the dam in $\mathrm{m^3/day}$ per metre.",
     r"**$q \approx 7.2\ \mathrm{m^3/day}$ per m** ($N_f/N_d \approx 5/12$).",
     r"$q = 2 \times 10^{-5} \times 10 \times 5/12 \times 86\,400 = 7.2$.", figure="p. 5, Figure 8."),
   q("CSC Seepage B Q9",
     r"For the dam of Q8 (dimensions in Figure 9: water depth $6h = 10\ \mathrm{m}$, base $11h$ with 45° cut-offs of "
     r"depth $h$ at each end), use your flow net to calculate the uplift force on the dam.",
     r"**Uplift ≈ 1752 kN/m.**",
     r"Each potential drop is $10/12 = 0.833\ \mathrm{m}$. Pressure head at a base point = (water depth + depth below "
     r"ground) $- n_d \times 0.833$; e.g. at D: $13.33 - 2 \times 0.833 = 11.66\ \mathrm{m}$ … at I: 5.0 m. "
     r"Uplift $= \gamma_w \times$ area of the pressure-head diagram ≈ 1752 kN/m.", figure="p. 6, Figure 9.")),
]}

CE104Q[CT["T_Shear_A_Solutions"]] = {"code": "CE104", "title": "Practice · Shear strength A — direct shear & Mohr circles (CSC)", "sections": [
 sec("Q1 Direct shear on dry sand", (1, 1),
   q("CSC Shear A Q1",
     r"(a) A dry sand fails in direct shear at a shear stress of 135 kPa under a normal stress of 200 kPa. Find the "
     r"angle of internal friction $\phi$. (b) A second sample of the same sand is tested at a normal stress of "
     r"145 kPa. What shear stress will cause failure?",
     r"**(a) $\phi = 34^\circ$ · (b) $\tau_f = 97.9\ \mathrm{kPa}$.**",
     r"Dry sand, $c = 0$: $\tan\phi = 135/200 = 0.675$ → $34^\circ$. $\tau_f = 145\tan 34^\circ = 97.9$.")),
 sec("Q2 Damp sand, two tests", (2, 2),
   q("CSC Shear A Q2",
     r"Two direct shear tests on damp sand: at a normal stress of 50 kPa the sample fails at 33 kPa shear; at 80 kPa "
     r"it fails at 51 kPa. Determine the angle of internal friction and the apparent cohesion.",
     r"**$\phi = 31^\circ$ · apparent cohesion $c = 3\ \mathrm{kPa}$.**",
     r"Slope $\tan\phi = (51 - 33)/(80 - 50) = 0.6$ → $31^\circ$; intercept $c = 33 - 0.6 \times 50 = 3\ "
     r"\mathrm{kPa}$ (apparent cohesion from suction in the damp sand).")),
 sec("Q3 Shear box forces", (3, 3),
   q("CSC Shear A Q3",
     r"Dry sand in a circular shear box of 50 mm diameter fails at a shear force of 130 N under a normal load of "
     r"200 N. (a) Find the normal and shear stresses at failure. (b) Find $\phi$. (c) What is the probable state of "
     r"the sample?",
     r"**(a) $\sigma = 102\ \mathrm{kPa}$, $\tau_f = 66\ \mathrm{kPa}$ · (b) $\phi = 33^\circ$ · (c) loose to medium "
     r"dense.**",
     r"$A = \pi \times 50^2/4 = 1963\ \mathrm{mm^2}$; $\sigma = 200/1963 = 0.102\ \mathrm{N/mm^2}$, $\tau_f = 0.066$; "
     r"$\tan\phi = 66/102$ → $33^\circ$.")),
 sec("Q4 Strength under a new building", (4, 4),
   q("CSC Shear A Q4",
     r"(a) A uniform deposit of dry granular soil has unit weight $19.6\ \mathrm{kN/m^3}$ and $\phi = 35^\circ$. What "
     r"is the shear strength on a horizontal plane 4 m below the ground? (b) A building will raise the vertical stress "
     r"there by $60\ \mathrm{kN/m^2}$ and the shear stress on that plane by $52\ \mathrm{kN/m^2}$. Does the shear "
     r"stress exceed the shear strength?",
     r"**(a) $\tau_f = 54.9\ \mathrm{kPa}$ · (b) no: strength rises to 96.9 kPa > 52 kPa.**",
     r"$\sigma_v = 19.6 \times 4 = 78.4$ → $\tau_f = 78.4\tan 35^\circ = 54.9$. After loading $\sigma_v = 138.4$ → "
     r"$\tau_f = 138.4\tan 35^\circ = 96.9 > 52$.")),
 sec("Q5 Mohr circle states", (5, 5),
   q("CSC Shear A Q5",
     r"Describe the state of samples A to D whose Mohr circles are: (a) A, a point on the normal-stress axis; (b) B, "
     r"too small to touch the failure envelope; (c) C, just tangent to the envelope; (d) D, so large that part of it "
     r"lies above the envelope.",
     r"**(a) isotropic (all-round equal) stress · (b) stable, not yet yielding · (c) yielding on the failure plane · "
     r"(d) impossible stress state.**",
     r"The envelope is the limit of stress states the soil can carry, so a circle cannot cross it.")),
]}

_SIN = r"\sin\phi = \frac{\sigma_1 - \sigma_3}{\sigma_1 + \sigma_3},\qquad \sigma_1 = \sigma_3\tan^2\!\left(45^\circ + \frac{\phi}{2}\right) + 2c\tan\!\left(45^\circ + \frac{\phi}{2}\right)"

CE104Q[CT["T_Shear_B_Solutions"]] = {"code": "CE104", "title": "Practice · Shear strength B — triaxial, UU/CU/CD (CSC)", "sections": [
 sec("Q1–Q3 Triaxial on dry sand", (1, 2),
   ("eq", _SIN),
   q("CSC Shear B Q1",
     r"A dry cohesionless soil is tested in a triaxial test at a confining pressure of 50 kPa and fails at an axial "
     r"stress of 170 kPa. What is $\phi$?",
     r"**$\phi = 33^\circ$.**", r"$\sin\phi = (170 - 50)/(170 + 50) = 0.545$ → $33^\circ$."),
   q("CSC Shear B Q2",
     r"A dry sand has $\phi = 36^\circ$. In a triaxial test at a confining pressure of 40 kPa, what maximum axial "
     r"stress (major principal stress) should be predicted?",
     r"**$\sigma_{1f} = 154\ \mathrm{kPa}$.**", r"$\sigma_1 = 40\tan^2(63^\circ) = 40 \times 3.85 = 154$."),
   q("CSC Shear B Q3",
     r"A level granular deposit has $\phi = 37^\circ$. At one depth the lateral pressure is 45 kPa. Find the maximum "
     r"vertical pressure for incipient shear failure. If $K_0 = 1 - \sin\phi$, is the soil close to failure?",
     r"**$\sigma_{v,\max} = 181\ \mathrm{kPa}$; with $K_0 = 0.398$ the actual $\sigma_v = 113\ \mathrm{kPa}$, so "
     r"the soil is not close to failure.**",
     r"$\sigma_{v,\max} = 45\tan^2(63.5^\circ) = 181$. At rest $\sigma_v = 45/0.398 = 113 < 181$.")),
 sec("Q4 Will the building cause failure?", (2, 2),
   q("CSC Shear B Q4",
     r"A foundation will raise the principal stresses at a point in dry sand ($\phi = 34^\circ$) to 195 kPa and "
     r"70 kPa. Would these stresses cause shear failure?",
     r"**No: the mobilised angle is 28° < 34°.**", r"$\sin\phi_m = (195 - 70)/(195 + 70) = 0.472$ → $28^\circ$.")),
 sec("Q5–Q6 Strength on a plane", (3, 3),
   q("CSC Shear B Q5",
     r"Dry sand fails in a triaxial test at an axial stress of 51 kPa with a confining pressure of 15 kPa. What shear "
     r"strength is expected in a direct shear test at a normal stress of 125 kPa?",
     r"**$\tau_f = 81\ \mathrm{kPa}$.**", r"$\sin\phi = 36/66$ → $\phi = 33^\circ$; $\tau_f = 125\tan 33^\circ = 81$."),
   q("CSC Shear B Q6",
     r"A mixed soil has $c = 22\ \mathrm{kPa}$ and $\phi = 28^\circ$. What shear strength is expected on a plane with "
     r"a normal stress of 70 kPa?",
     r"**$\tau_f = 59.2\ \mathrm{kPa}$.**", r"$\tau_f = 22 + 70\tan 28^\circ = 59.2$.")),
 sec("Q7–Q8 UU area correction; CIU parameters", (4, 4),
   q("CSC Shear B Q7",
     r"A UU test: specimen length 110 mm, diameter 50 mm, shortening 8 mm at failure, failure load 0.145 kN. Compute "
     r"the undrained shear strength $s_u$.",
     r"**$s_u = 34.3\ \mathrm{kPa}$.**",
     r"$\varepsilon_a = 8/110 = 0.073$; corrected area $A = A_0/(1 - \varepsilon_a) = 1.963 \times 10^{-3}/0.927 = "
     r"2.12 \times 10^{-3}\ \mathrm{m^2}$; $q_f = 0.145/0.00212 = 68.5$; $s_u = q_f/2 = 34.3$."),
   q("CSC Shear B Q8",
     r"A CIU triaxial test series gave: cell pressures 100, 200, 300 kPa; deviator stresses at failure 238, 307, "
     r"389 kPa; pore pressures at failure 36, 108, 197 kPa. Determine the total and effective stress strength "
     r"parameters.",
     r"**Effective: $\phi' \approx 40^\circ$, $c' \approx 0$ · total: $\phi_{\mathrm{cu}} \approx 16^\circ$, "
     r"$c_{\mathrm{cu}} \approx 60\ \mathrm{kPa}$.**",
     r"Effective circles $\sigma'_3/\sigma'_1$: 64/302, 92/399, 103/492; with $c' = 0$, $\sin\phi' = (\sigma'_1 - "
     r"\sigma'_3)/(\sigma'_1 + \sigma'_3)$ gives 40.6°, 38.7°, 40.8°. Total circles 100/338, 200/507, 300/689: a "
     r"best-fit tangent $R = c\cos\phi + p\sin\phi$ through ($p$, $R$) = (219, 119), (353.5, 153.5), (494.5, 194.5) "
     r"gives $\sin\phi = 0.274$ and $c\cos\phi = 59$. The solution sheet gives no numbers (it refers to the lecture "
     r"example).", src="claude")),
 sec("Q9–Q10 UU, unconfined, CU and CD on one clay", (5, 6),
   q("CSC Shear B Q9",
     r"A UU triaxial test on a clay reaches a maximum axial stress of 106 kPa at a confining stress of 40 kPa. What "
     r"is $c_u$? What axial stress would cause failure in an unconfined compression test on the same soil?",
     r"**$c_u = 33\ \mathrm{kPa}$; unconfined failure at $q_u = 66\ \mathrm{kPa}$.**",
     r"$c_u = (106 - 40)/2 = 33$; in unconfined compression $\sigma_3 = 0$ so $\sigma_1 = 2c_u = 66$."),
   q("CSC Shear B Q10",
     r"Three triaxial tests on a saturated clay, all at a cell pressure of $200\ \mathrm{kN/m^2}$; $c' = 0$, "
     r"$\phi' = 24^\circ$. (a) Undrained test: pore pressure at failure 125 kPa; find the deviator stress at failure. "
     r"(b) Consolidated-undrained test: maximum deviator stress 160 kPa; find the pore pressure at failure. (c) Drained "
     r"test with back pressure 80 kPa: find the deviator stress at failure.",
     r"**(a) $q_f = 103\ \mathrm{kPa}$ · (b) $u_f = 83.3\ \mathrm{kPa}$ · (c) $q_f = 164.5\ \mathrm{kPa}$.**",
     r"$\sigma'_1 = \sigma'_3\tan^2(57^\circ) = 2.371\sigma'_3$. (a) $\sigma'_3 = 75$ → $\sigma'_1 = 178$ → 103. "
     r"(b) $\sigma'_1 - \sigma'_3 = 160$ → $\sigma'_3 = 160/1.371 = 116.7$ → $u = 200 - 116.7 = 83.3$. (c) "
     r"$\sigma'_3 = 120$ → $\sigma'_1 = 284.5$ → 164.5.")),
 sec("Q11 Total-stress parameters", (7, 8),
   q("CSC Shear B Q11",
     r"A cohesive soil has undrained parameters $c_u = 35\ \mathrm{kN/m^2}$ and $\phi_u = 17^\circ$. (a) In an "
     r"undrained triaxial test a specimen fails at a total axial stress of $360\ \mathrm{kN/m^2}$: find the cell "
     r"pressure. (b) What undrained shear strength would an unconfined compression test indicate?",
     r"**(a) $\sigma_3 = 145.3\ \mathrm{kPa}$ · (b) $s_u = 47.3\ \mathrm{kPa}$.**",
     r"$\tan^2(53.5^\circ) = 1.826$, $2c\tan 53.5^\circ = 94.6$: (a) $360 = 1.826\sigma_3 + 94.6$ → 145.3. (b) "
     r"$\sigma_3 = 0$ → $\sigma_1 = 94.6$ → $s_u = 47.3$.")),
]}
