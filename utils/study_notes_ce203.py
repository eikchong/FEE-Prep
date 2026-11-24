"""CE203 Geotechnical Engineering — practice pages from CE3115 (slopes, earth pressure, retaining walls)
and CE3116 (site investigation, compaction, shallow & deep foundations) tutorials, in course order.

Answers are taken from the official solutions; where a solution has an error it is flagged with a tip.
Lecture notes for these modules are not loaded yet (the Drive zips are over the 10 MB connector limit).
"""


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


A = "CE203/CE3115/"
F = "CE203/CE3116/"
D = {
    "T1": A + "Tutorial OAP/CE3115 - Tutorial 1 - Infinite Slope Solutions R0.pdf",
    "T2": A + "Tutorial OAP/CE3115 - Tutorial 2 - Slope Stability Solution R0.pdf",
    "A1": A + "Assignment OAP/CE3115 - Assignment 1 Solution R0 (1).pdf",
    "A2": A + "Assignment OAP/CE3115 - Assignment 2 Solution R0.pdf",
    "EX": A + "Tutorial OAP/1920SEM2-CE3115 ExamPaper.pdf",
    "PS1": A + "Tutorial ERSS/CE3115 Problem Set 1 - An Introduction to Underground Construction in Singapore (Solutions).pdf",
    "PS2": A + "Tutorial ERSS/CE3115 Problem Set 2 - Earth Pressure Theory I (Full Solutions).pdf",
    "PS3": A + "Tutorial ERSS/CE3115 Problem Set 3 - Earth Pressure Theory II (Full Solutions).pdf",
    "PS4": A + "Tutorial ERSS/CE3115 Problem Set 4 - Rigid Retaining Structures (Full Solutions).pdf",
    "PS5": A + "Tutorial ERSS/CE3115 Problem Set 5 - Analysis of Rigid Retaining Structures using EC7 (Full Solutions).pdf",
    "PS6": A + "Tutorial ERSS/CE3115 Problem Set 6 - Flexible Retaining Structures I (Full Solutions).pdf",
    "PS7": A + "Tutorial ERSS/CE3115 Problem Set 7 - Flexible Retaining Structures II (Full Solutions).pdf",
    "QZ": A + "Assignment ERSS/Past Year Quiz.pdf",
    "SI": F + "Site Investigation/CE3116 Tutorial - Site Investigation Solutions R0.pdf",
    "SIX": F + "Site Investigation/CE3116 Example Problem - Site Investigation R0.pdf",
    "CP": F + "Compaction/CE3116 Tutorial - Compaction Solutions R0.pdf",
    "ULS": F + "Shallow Foundation/Tutorial Solution - ULS.pdf",
    "SLS": F + "Shallow Foundation/Tutorial Solution - SLS.pdf",
    "PILE": F + "Deep Foundation/CE3116 - Tutorial Sol - DEEPFDNS.pdf",
}

# (key, page_count, seq, topics) — used for lecture_outlines.json
OUTLINE = [("T1", 11, 1, ["CE203-01"]), ("T2", 16, 2, ["CE203-01"]), ("A1", 14, 3, ["CE203-01"]),
           ("A2", 11, 4, ["CE203-01"]), ("PS1", 6, 5, ["CE203-04"]), ("PS2", 15, 6, ["CE203-02"]),
           ("PS3", 19, 7, ["CE203-02"]), ("PS4", 14, 8, ["CE203-03"]), ("PS5", 6, 9, ["CE203-03"]),
           ("PS6", 15, 10, ["CE203-03", "CE203-04"]), ("PS7", 8, 11, ["CE203-03", "CE203-04"]),
           ("QZ", 9, 12, ["CE203-02", "CE203-03"]), ("EX", 9, 13, ["CE203-01", "CE203-02", "CE203-03"]),
           ("SI", 7, 20, ["CE203-05"]), ("SIX", 9, 21, ["CE203-05"]), ("CP", 7, 22, ["CE203-05"]),
           ("ULS", 6, 23, ["CE203-06"]), ("SLS", 22, 24, ["CE203-09"]), ("PILE", 9, 25, ["CE203-07"])]

EC7 = ("tip", "EC7 DA1 quick reference used throughout: **C1** (A1+M1+R1) γ_G = 1.35 unfav / 1.0 fav, γ_Q = 1.5, "
              "strength unfactored; **C2** (A2+M2+R1) γ_G = 1.0, γ_Q = 1.3, tan φ′ and c′ ÷ 1.25, c_u ÷ 1.4. "
              "Check both; the worse one governs.")

GEO = {}

GEO[D["T1"]] = {"code": "CE203", "title": "Slopes 1 · Infinite slopes (CE3115 Tut 1)", "sections": [
 sec("Q1 Effect of slip depth, water, cohesion & weak seams (β = 18°)", (2, 7),
   ("eq", r"F = \frac{c' + \sigma'_v\cos^2\beta\tan\phi'}{\sigma_v\cos\beta\sin\beta}\quad(\text{parallel seepage, slip plane at depth } z)"),
   ("ex", "Slopes A–E at z = 1, 3, 5 m (γ_dry 16.5, γ_sat 20)",
    "A dry, φ′ 30°: **F = 1.78 at every depth** (= tan φ′/tan β) · B GWT at 1 m: 1.78 / 1.15 / 1.04 · "
    "C GWT at surface: **0.89** at every depth (≈ ½ of dry, since γ′/γ_sat ≈ 0.5) · D + c′ = 5 kPa: 1.74 / 1.17 / 1.06 "
    "(cohesion helps most at shallow depth — often ignored for conservatism) · E clay seam (c′ 0, φ′ 25°) at 3 m: **0.72** — "
    "a weak layer governs, so check every interface with that layer's parameters."),
 ),
 sec("Q2 Sand over OC clay, β 14–17°, EC7 DA1-C2", (8, 10),
   ("md", "Effective-stress (slow failure); γ_sat = γ_dry(1 + w) = 19.8; worst case **GWT at the surface**; check both "
          "slope angles. Design strength: φ′_d = tan⁻¹(tan φ′_k/1.25) → sand 33° → 27.5°, clay c′ 5 → 4 kPa, 28° → 23°."),
   ("ex", "F at 3 m (sand / clay) and 5 m (clay)", "β = 14°: 1.03 / 1.13 / 1.02 → just OK · β = 17°: **0.84** / 0.93 / "
          "0.83 → **unstable**. Use the steepest local angle."),
 ),
]}

GEO[D["T2"]] = {"code": "CE203", "title": "Slopes 2 · Finite slopes: mass procedure, Taylor, Bishop (CE3115 Tut 2)", "sections": [
 sec("Q1 Short-term seabed trench in soft clay (c_u 17, γ 16, H 3 m, β 60°)", (2, 4),
   ("eq", r"F = \frac{c_u r^2\theta}{W d}\qquad\text{Taylor: } F = \frac{c_u}{N_s\gamma H},\quad H_{max} = \frac{c_u/\gamma_{cu}}{N_s\gamma}"),
   ("ex", "Mass procedure (r = 5 m, θ = 66°, W = 8.1 × 16, d = 2.03 m)", "C1 (×1.35 on driving): **F = 1.38** · C2 "
          "(c_u ÷ 1.4): **F = 1.33**."),
   ("ex", "Taylor (D → ∞, β 60° → N_s ≈ 0.19)", "C1 **1.38**, C2 **1.33** — identical, so the trial circle is (close "
          "to) the critical one. H_max: β 60° → 4.0 m, β 45° (N_s 0.18) → only 4.2 m → contractor's claim is wrong; 60° "
          "needs less excavation volume."),
 ),
 sec("Q2 Two-layer natural slope — Simplified Bishop", (5, 9),
   ("eq", r"F = \frac{\sum\left[c'b + (W - ub)\tan\phi'\right]\dfrac{\sec\alpha}{1 + \tan\alpha\tan\phi'/F}}{\sum W\sin\alpha + M_N/R}"),
   ("ex", "Result", "DA1-C1 **F = 0.94** (fails) · DA1-C2 **F = 1.08**. C1 governs here."),
 ),
 sec("How to apply EC7 in Bishop", (10, 13),
   ("steps", ["Slices: boundaries at slip entry/exit, slope breaks, layer and water-table crossings, load edges.",
              "C1: ×1.35 on W sin α of slices with **positive** α (driving); negative-α slices (resisting) unfactored; "
              "variable unfavourable surcharge ×1.5, favourable ignored.",
              "C2: W unfactored, surcharge ×1.3, c′/1.25 and tan φ′/1.25 in the numerator **and in n_α**.",
              "External loads/ponded water: add M_N/R to the denominator (negative if restoring).",
              "Start with F = 1, compute n_α, iterate until F converges (usually 2–3 rounds)."]),
 ),
 sec("Ponded water & other details", (14, 15),
   ("md", "Ponded water acts normal to the surface: vertical F_wV = γ_w h_w b, horizontal F_wH = γ_w h_w b tan β, applied "
          "at mid-slice; its moment about the centre goes in as M_N/R (usually restoring at the toe)."),
 ),
]}

GEO[D["A1"]] = {"code": "CE203", "title": "Slopes 3 · River-bank Bishop analysis (CE3115 Assignment 1)", "sections": [
 sec("1a Trial circle, 3 m tension crack, 50 kPa surcharge", (3, 7),
   ("md", "Omit the slice inside the tension crack (crack assumed dry, above GWT), so the surcharge length shrinks from "
          "8.5 to 7 m. 9 slices minimum; ponded water included as point loads."),
   ("ex", "Result", "DA1-C1 **F = 1.083** · DA1-C2 **F = 1.248** (±0.05 depending on slicing)."),
   ("md", "Common mistakes: too few slices; splitting a slice top/bottom; no boundary where the slip crosses the layer "
          "interface; forgetting ponded water or surcharge; adding water pressure in the crack; not using reduced φ′ in n_α."),
 ),
 sec("1b Bed erosion of 3 m (DA1-C1)", (8, 10),
   ("ex", "Toe slice and its ponded water removed", "F drops **1.083 → 0.916** → unstable."),
 ),
 sec("1c Falling water level", (11, 11),
   ("md", "River level drops alone (rapid drawdown): lose the restoring ponded-water moment → F falls. River and GWT "
          "both drop (long term): soil lighter and σ′ higher → F usually rises."),
 ),
 sec("Worked slice (slice 7, C1)", (12, 13),
   ("ex", "W = 3(19 × 8.22 + 18 × 2.25) = 590.1 kN/m; α = sin⁻¹(13.5/26) = 31.3°",
    "Driving 1.35 × 590.1 sin 31.3° = 413.6 · S = 13 × 3 + (590.1 − 10 × 7.97 × 3) tan 28° = **225.6** · "
    "n_α(F = 1) = 0.88 → T ≈ 199 kN/m. (The slide multiplies 232.3 × 0.88 — a typo; the table value 199.5 is right.)"),
 ),
]}

GEO[D["A2"]] = {"code": "CE203", "title": "Slopes 4 · Slope stabilisation options (CE3115 Assignment 2)", "sections": [
 sec("Strategy (SLIDE, DA1-C2, 50 kPa footing 2 m from crest)", (3, 4),
   ("steps", ["Check the existing slope, then with the surcharge.",
              "Try horizontal drains first (only useful if the GWT lies inside the sliding mass).",
              "Then flattening, benching, buttressing with the same cut/fill area, and combinations.",
              "Use Morgenstern–Price/GLE for comparison; auto-refine search so the critical surface is found."]),
 ),
 sec("Results by location", (5, 10),
   ("ex", "F (original → +surcharge → fixed)", "L1 0.999 → 0.991 → buttress 1.041 (GWT already outside the mass, "
          "drains useless) · L2 1.060 → 0.925 → drains (GWT moved 4–7 m back) 1.057 · L3 clay seam, very wide mass: "
          "1.014 → 0.881 → buttress + drain 1.013 (flattening/benching alone make it worse) · L4 1.358 → 1.084, no works."),
 ),
]}

GEO[D["PS1"]] = {"code": "CE203", "title": "Retaining 1 · Underground construction in Singapore (CE3115 PS1)", "sections": [
 sec("Regulatory terms & GBW thresholds", (1, 2),
   ("md", "**ERSS** earth retaining/stabilising structures; **TERS** temporary ERSS. **QP** (PE with practising "
          "certificate, accountable), **AC** (accredited checker, independent check), **BCA** regulator. Geotechnical "
          "building works: tunnels > 2 m; excavations, ERSS or slopes > **6 m**; foundations of buildings ≥ 30 storeys."),
 ),
 sec("Choosing a wall & wall types", (4, 5),
   ("md", "Open site (Tuas, 1 basement, 5–7 m) → **sheet piles** fine. Urban (Orchard, 35 storeys next to a hotel) → "
          "stiff **secant pile or diaphragm wall** to limit ground movement. Sheet piles: fast, reusable / noisy, hard in "
          "stiff soil, flexible. Soldier pile & lagging: cheap, fast / not watertight, flexible. D-wall: stiff, "
          "watertight, permanent / expensive, specialist plant. **Ground freezing** used at Marina Bay (TEL under NSL/CCL)."),
 ),
]}

GEO[D["PS2"]] = {"code": "CE203", "title": "Earth pressure 1 · K₀, Rankine, water & layers (CE3115 PS2)", "sections": [
 sec("Q1–Q2 At-rest pressure", (1, 2),
   ("eq", r"K_0 = \frac{\nu}{1-\nu}\ (\text{elastic, laterally constrained}),\qquad K_0 = 1 - \sin\phi'\ (\text{Jaky, NC})"),
   ("ex", "Q2 sand φ 30°, e 0.5, G_s 2.7, 15 m", "GWT at surface: σ′_v = 166.5, σ′_h = 83.3 kPa at 15 m · GWT lowered to "
          "7 m: σ′_v = 123.9 at 7 m and 212.7 at 15 m (σ′_h half)."),
 ),
 sec("Q3–Q6 Concepts, tension cut, Rankine thrust", (3, 3),
   ("md", "Passive needs much more movement: σ_h must rise from K₀σ_v past σ_v to K_pσ_v, versus a small drop to K_aσ_v."),
   ("eq", r"K_a = \frac{1-\sin\phi}{1+\sin\phi},\quad \sigma_a = K_a\sigma'_v - 2c'\sqrt{K_a},\quad z_0 = \frac{2c'}{\gamma\sqrt{K_a}}\ \left(\phi = 0:\ z_0 = \frac{2c_u}{\gamma}\right)"),
   ("ex", "Q4 3 m cut, c_u 30, γ 16", "Tension zone 2c_u/γ = **3.75 m > 3 m** → theoretically stands unsupported."),
   ("ex", "Q5 7 m, γ 17.3, φ 30° / Q6 5 m passive, γ 18", "P_a = ½(⅓)(17.3)(7²) = **141 kN/m** horizontal at H/3 · "
          "P_p = ½(3)(18)(5²) = **675 kN/m**."),
 ),
 sec("Q7 c′–φ′ backfill (8 m, c′ 20, φ′ 25°, γ 17.5)", (4, 4),
   ("ex", "Thrust ignoring tension", "σ_a = −25.5 kPa at top, 31.3 at base; z₀ = 3.59 m → P_a = ½(4.41)(31.3) = "
          "**69 kN/m** at 1.47 m above base."),
 ),
 sec("Q8–Q10 Water in the backfill", (5, 7),
   ("ex", "Q8 5 m, φ 36°", "Dry: P_a = **57 kN/m** · saturated: P_a 31.5 + water 122.5 = **154 kN/m** (water dominates)."),
   ("ex", "Q9 6 m, φ 32°, e 0.6", "Dry: σ_a 30.5, P 91.5 · submerged: σ′_a 19.2, P 57.6 + water 176.6 kN/m."),
   ("ex", "Q10 10 m, GWT 3 m, q 14 kPa", "Sum the pressure-diagram parts (K_aγH₁, K_aγ′H₂, K_aq, γ_wH₂) → **502 kN/m**."),
 ),
 sec("Q11 Two layers + 50 kPa surcharge", (8, 9),
   ("ex", "6 m wall; sand over c′–φ′ clay, GWT 1.5 m", "Pressures jump at the interface (different K_a and −2c√K_a). "
          "Total **294.6 kN/m** acting **2.17 m** above the base."),
 ),
 sec("Q12 Passive with sloping backfill", (10, 11),
   ("tip", "Rankine's sloping-backfill K_p gives *decreasing* passive force as β rises (β ≈ 20° for 450 kN) — unrealistic. "
           "Coulomb / Caquot–Kérisel show it increases; 450 kN < 675 kN (β = 0) so no passive failure. Don't use Rankine "
           "passive with β > 0."),
 ),
]}

GEO[D["PS3"]] = {"code": "CE203", "title": "Earth pressure 2 · Cohesion, Coulomb & curved surfaces (CE3115 PS3)", "sections": [
 sec("Q1–Q2 Clay backfill & tension cracks", (1, 3),
   ("ex", "Q1 soft clay c_u 10, γ 16.5, 6 m", "z₀ = 2c_u/γ = **1.21 m**; σ_a at base 79 kPa; P_a = 177 kN/m with tension, "
          "**189 kN/m** after cracking."),
   ("ex", "Q2 c′ 12, φ′ 20°, β 10°, 4.6 m", "z₀ = 1.73 m → P_a = **41.5 kN/m**, horizontal 40.8."),
 ),
 sec("Q3–Q6 Coulomb, densification, layered", (4, 8),
   ("ex", "Q3 Coulomb δ 15°", "K_a = 0.387 → P_a = **46.4 kN/m** at H/3, inclined δ to the wall normal."),
   ("ex", "Q4 loose (e 0.7, φ 30°) vs dense (e 0.4, φ 40°)", "p_a 52 → 41 kPa, p_p 468 → 870 kPa — densifying lowers "
          "active and raises passive."),
   ("ex", "Q5 7.32 m, c 12, φ 20°", "z₀ ≈ 2.0 m → σ_a = 45.3 at base → **P_a = 120 kN/m**."),
   ("ex", "Q6 sandy clay over sand", "z₀ = 2.1 m > 1.5 m layer → crack through the clay; sand: 8.2 → 34.1 kPa."),
 ),
 sec("Q7–Q8 Active vs passive moments about the base", (9, 13),
   ("ex", "Q7 / Q8", "Q7: ΣP_a 215 kN at 2.09 m, ΣP_p 323 kN at 1.33 m, M_p/M_a = **0.96** → rotates · Q8: P_a 554 kN at "
          "3.74 m, P_p 389 kN, ratio **0.31**. Water pressures on both sides cancel only if levels match."),
 ),
 sec("Q9–Q10 Surcharge, rough wall, flooding", (14, 15),
   ("ex", "Q9 8 m, q 15", "Smooth 232 kN · rough δ 20°: 209 kN (horizontal 196)."),
   ("ex", "Q10 flood to surface", "Lateral force 62.4 → 39 (soil) + 125 (water) = 164 kN → **+163 %**. Drainage matters."),
 ),
 sec("Q11–Q13 Plane vs curved passive surfaces", (16, 19),
   ("ex", "Q13 3 m wall, γ 18, φ 37° — horizontal passive", "Rankine/Coulomb smooth **324** · Coulomb δ/φ 0.5 → 674, "
          "0.8 → 1254 · Caquot–Kérisel curved 0.5 → **583**, 0.8 → **729 kN/m**."),
   ("tip", "Coulomb's plane surface overestimates passive badly for rough walls (δ > φ/3); use curved-surface (Caquot–"
           "Kérisel) K_p. Q11–12: δ 20° → 10 230 vs 8 325 kN; δ 30° → 19 947 vs 11 100 kN."),
 ),
]}

GEO[D["PS4"]] = {"code": "CE203", "title": "Retaining 2 · Gravity & cantilever walls, FoS (CE3115 PS4)", "sections": [
 sec("Q1 Gravity wall 6.6 × 3.2 m, φ′ 35°, no front soil", (1, 2),
   ("eq", r"FoS_{OT} = \frac{\sum M_R}{\sum M_O}\ge 2,\quad FoS_{sl} = \frac{N\tan\delta_b + P_p + c_bB}{P_a}\ge 1.5,\quad p = \frac{N}{B}\left(1 \pm \frac{6e}{B}\right)"),
   ("ex", "K_a 0.27, P_a 106 kN, W 507 kN, δ_b = 0.8φ′ = 28°", "Overturning 811/233 = **3.5** · sliding 269.5/106 = "
          "**2.5** · l = 577.8/506.9 = 1.14 m, e = 0.46 < B/6 → p_max **295**, p_min **22 kPa**."),
 ),
 sec("Q2–Q3 Adding 2 m of front soil; smooth base", (3, 5),
   ("ex", "Passive 133 kN at 0.67 m", "Q2: OT 3.86, sliding **3.8**, p 280/37 · Q3 smooth base: sliding 133/106 = "
          "**1.26 < 1.5 ✗** (passive alone is not enough), p 254/63."),
   ("md", "In bearing, only the passive actually mobilised (P_p/FoS_sl) is counted in the moment."),
 ),
 sec("Q4 c′–φ′ backfill with 20 kPa surcharge", (6, 8),
   ("ex", "c′ 10, φ′ 25°, δ_b 15°, c_b 10", "z₀ = 0.63 m, P_a = 131.7 kN · OT **3.5** · sliding (151 passive + 136 "
          "friction + 32 adhesion)/131.7 = **2.4** · p 283/34 kPa."),
 ),
 sec("Q5–Q6 Cantilever & gravity walls with heel soil", (9, 14),
   ("ex", "Q5 sloping backfill β 20°", "P_a = 71.3 kN (67 H, 24 V) · sliding **1.9** · OT **3.3** · p 99.6 / 40.2 kPa."),
   ("ex", "Q6 gravity wall on clay", "P_a 93 kN at 1.78 m, P_p 57 kN · OT **3.5** · sliding **1.9** · p 167.5 / 39.4 kPa."),
   ("md", "Use a **virtual back** through the heel: soil above the heel counts as wall weight; Rankine applies there."),
 ),
]}

GEO[D["PS5"]] = {"code": "CE203", "title": "Retaining 3 · Same wall to EC7 DA1 (CE3115 PS5)", "sections": [
 sec("EQU (overturning)", (1, 2),
   ("md", "γ_G,dst 1.1, γ_G,stb 0.9, γ_φ 1.25 → φ_d = 29.3°, K_a 0.343, K_p 2.92. Stabilising 793 > destabilising 325 kNm "
          "→ OK (over-design 2.4)."),
 ),
 sec("GEO DA1-C1 (sliding, bearing)", (3, 5),
   ("ex", "Smooth base, passive only", "P_a = 1.35 × 106 = **143 kN** > P_p 133 kN → **sliding fails**. Fix sliding "
          "before checking bearing."),
   ("tip", "In the bearing check the solution factors N by 1.35 but leaves the moments unfactored, giving e = 0.74 m "
           "and p_min = −83 kPa. Keep factors consistent (factor the action effects together) when you redo it."),
 ),
 sec("GEO DA1-C2", (5, 6),
   ("ex", "φ_d 29.3°", "P_a = 134.3 > P_p 105.1 → **sliding fails** · bearing p 289 / 28 kPa (e = 0.44 < B/6)."),
 ),
]}

GEO[D["PS6"]] = {"code": "CE203", "title": "Retaining 4 · Cantilever sheet piles (CE3115 PS6)", "sections": [
 sec("Q1–Q2 Cantilever in sand (H 6 m, γ 17, φ 30°)", (1, 6),
   ("steps", ["Simplified: moments about the toe C of active K_aγ(H + d₀) and passive K_pγd₀ → d₀; design D = 1.2 d₀.",
              "Max moment at zero shear: K_a(H + d_s)² = K_p d_s².",
              "Section modulus Z = M_max/f_b."]),
   ("ex", "Answers", "0.944(6 + d₀)³ = 8.5 d₀³ → d₀ = 5.56 → **D = 6.7 m** · d_s = 3 m → **M_max = 460 kNm/m** · "
          "Z = 460/175 000 = **2.63 × 10⁻³ m³/m**. Net-pressure method: D ≈ 6.0 m, same M_max."),
   ("tip", "The solution writes Z = 26.25 × 10⁻² m³ — a units slip; 460 kNm ÷ 175 000 kPa = 2.63 × 10⁻³ m³ per metre."),
 ),
 sec("Q3–Q4 Same wall with water at 3 m both sides", (7, 11),
   ("ex", "Water cancels (equal levels)", "Simplified d₀ = 7.3 → **D = 8.7 m**, M_max **504 kNm** at 4 m · net-pressure: "
          "D = 7.8 m, M_max 506 kNm."),
 ),
 sec("Q5 Layered sand (limiting pressure profile)", (12, 15),
   ("ex", "Loose over medium-dense sand", "Solve horizontal and moment equilibrium together: d = 3.82 m, z = 0.41 m → "
          "**D ≈ 3.9 m** · M_max **198 kNm** at 1.83 m below dredge level."),
 ),
]}

GEO[D["PS7"]] = {"code": "CE203", "title": "Retaining 5 · Anchored walls, free-earth support (CE3115 PS7)", "sections": [
 sec("Q1 Free earth support (tie 1 m below top)", (1, 3),
   ("steps", ["Draw active (dry above GWT, γ′ below) and passive K_pγ′D; water cancels if levels match.",
              "Moments about the tie T → cubic in D.", "Horizontal equilibrium → tie force T."]),
   ("ex", "Answer", "**D = 2.22 m**, **T = 30.5 kN/m**."),
 ),
 sec("Q2–Q3 Factor of safety on passive", (4, 8),
   ("ex", "FS 2", "K_pm = K_p/2 → **D = 4.0 m, T = 37.8 kN/m** · trapezoidal mobilised passive (α = 0.293) → **D = 4.25 m, "
          "T = 32.3 kN/m**."),
 ),
]}

GEO[D["QZ"]] = {"code": "CE203", "title": "Retaining 6 · Past-year quiz (earth pressure & walls)", "sections": [
 sec("True/false concepts", (1, 2),
   ("md", "Gravity walls: dead weight is critical, not embedment (embedment matters for flexible walls) · soldier pile & "
          "lagging can't be used below a high water table without dewatering · K_p > 1 means σ′_h > σ′_v · Coulomb's "
          "plane passive surface can be far from reality."),
 ),
 sec("K₀ from OCR; Mohr pole", (3, 5),
   ("eq", r"K_{0,OC} = (1 - \sin\phi')\,OCR^{\sin\phi'}"),
   ("ex", "σ′_p = 100 kPa (from oedometer), σ′_v0 = 33, φ′ 35°", "OCR ≈ 3 → **K₀ = 0.81**. Mohr question: pole at "
          "(6, −4), shear on vertical plane 4 kPa."),
 ),
 sec("Gravity wall 7 m (c′ 10, φ′ 28°, 2 m front soil, no base friction)", (6, 9),
   ("ex", "Answers", "K_a 0.361, σ_a 30.2, P_a 75.6 kN · K_p 2.77, σ_p 33.3 → 125.8 kPa, P_p 159.1 kN · sliding "
          "159.1/75.6 = **2.11** · overturning 709/126 = **5.6** · e = 0.26 m, p_max **211.5**, p_min 66 kPa → bearing "
          "FoS 500/211.5 = **2.36 < 3 ✗**. Surcharge behind raises P_a → both FoS fall."),
   ("md", "The quiz answer ignores the c′ reduction on the active side (σ_a = K_aγz) — conservative."),
 ),
]}

GEO[D["EX"]] = {"code": "CE203", "title": "Exam · CE3115 AY19/20 paper (slopes, walls, sheet piles)", "sections": [
 sec("Q1 River bank with bench & tension crack (Bishop, DA1-C2)", (2, 5),
   ("ex", "Answer key", "1a first-trial **F ≈ 1.2** (50 kPa surcharge) · 1b rock at +2 m forces a non-circular/compound "
          "slip → F likely rises; analyse with Spencer or Morgenstern–Price · 1c erosion: F ≈ **0.9** → potentially "
          "unstable."),
 ),
 sec("Q2 Seabed trench (same as Tut 2 Q1)", (5, 6),
   ("ex", "Answer key", "Mass procedure **1.33**; Taylor **1.33** (critical circle found); 45° gives no real depth gain — "
          "60° is cheaper."),
 ),
 sec("Q3 Cantilever wall, layered backfill, EC7 sliding", (7, 8),
   ("md", "Theory: Coulomb's plane passive surface errs for rough walls; Rankine's driving moment is usually bigger "
          "because Coulomb's thrust is inclined (its vertical component helps). Min surcharge for no crack in the sandy "
          "clay: K_aq − 2c′√K_a ≥ 0 at the top, i.e. **q = 2c′/√K_a** (c′ 13, φ′ 24° → K_a 0.42 → q ≈ 40 kPa). No "
          "official numbers for the rest."),
 ),
 sec("Q4 Sheet pile in clay (s_u 30) with sand backfill", (8, 9),
   ("md", "Flexible walls rely on embedment because passive resistance is their main stabilising force; gravity walls "
          "rely on weight. Q4b/c: work back the backfill height h from D = 3.6 m (net clay pressure 4c_u − q in front) "
          "— no official answer supplied."),
 ),
]}

GEO[D["SI"]] = {"code": "CE203", "title": "Foundations 1 · Site investigation: SPT, CPTu, PMT, permeability (CE3116 Tut 2)", "sections": [
 sec("a) SPT corrections", (1, 2),
   ("eq", r"(N_1)_{60} = N\cdot\frac{E_r}{60}\cdot\lambda\cdot C_N,\qquad C_N = \frac{300}{200 + \sigma'_v}\ (\text{dense sand}),\qquad s_u \approx 5N_{60}\ \text{kPa}"),
   ("ex", "3 m gravelly sand (N 28, σ′_v 47.5) / 10 m clay (N 8)", "28 × 70/60 × 0.75 × 1.21 ≈ **30** → D_R 65–85 % → "
          "φ′ 37° + 2° (gravelly) = **39°** · clay: 8 × 70/60 × 0.95 ≈ 9 → **s_u ≈ 45 kPa** (no C_N for clay)."),
 ),
 sec("b–c) CPTu: soil type & strength", (2, 3),
   ("eq", r"q_t = q_c + (1-a)u_2,\quad Q_t = \frac{q_t - \sigma_{v0}}{\sigma'_{v0}},\quad F_r = \frac{f_s}{q_t - \sigma_{v0}},\quad I_c = \sqrt{(3.47 - \log Q_t)^2 + (1.22 + \log F_r)^2}"),
   ("ex", "3 m", "q_t 9.13 MPa, Q_t 191, F_r 0.19 % → **I_c = 1.29 < 1.31 → gravelly/dense sand** ✓ · Baldi: D_R ≈ 80 % → "
          "φ′ 39°."),
   ("ex", "10 m clay", "q_t = 0.76 + 0.25 × 0.202 = 0.81 MPa, σ_v0 194 kPa → s_u = (q_t − σ_v0)/N_kt = **31 kPa**."),
 ),
 sec("d–e) Menard pressuremeter", (3, 4),
   ("eq", r"E = 2(1+\nu)\left[V_c + \bar V\right]\frac{\Delta p}{\Delta V},\qquad s_u = \frac{p_L - p_0}{N_p}"),
   ("ex", "Unload–reload points 5–6", "E_ur = 3 × 936 × 50/14 = **10 MPa**, G = 3.3 MPa, cavity strain 0.8 % · p₀ 144, "
          "p_L 360 (at V = V_c + 2V₀) → s_u = 216/5.5 = **39 kPa**."),
 ),
 sec("f–g) Compare s_u; Hvorslev permeability", (5, 5),
   ("ex", "s_u at 10 m", "SPT 45, CPT 31, PMT 39, lab UU 36 kPa — lab is the direct measure; calibrate N_kt, N_p to it."),
   ("eq", r"k = \frac{\pi r^2}{F\,T},\qquad F = \frac{2\pi L}{\ln\left[L/D + \sqrt{1 + (L/D)^2}\right]}"),
   ("ex", "L 0.3 m, D 0.1 m, T (at H/H₀ = 0.37) ≈ 80 s", "F = 1.04 m → **k = 9.4 × 10⁻⁵ m/s**, within the CPTu range "
          "10⁻⁵–10⁻³ m/s."),
   ("tip", "The solution calls I_c = 2.0 'gravelly sand'; on Robertson's chart 1.31–2.05 is zone 6 (clean to silty sand). "
           "The k range quoted still fits."),
 ),
]}

GEO[D["SIX"]] = {"code": "CE203", "title": "Foundations 1a · Site investigation worked example (CE3116)", "sections": [
 sec("Classification, SPT, CPTu, PMT, Hvorslev", (1, 9),
   ("md", "Same workflow as Tut 2 at different depths: LL 30, PL 15 → PI 15 · corrected N ≈ 32 (sand → φ′; clay → "
          "c_u = 5N = 160 kPa) · CPTu at 12.5 m: q_t 17.08 MPa, F_r 1.03 % → sand, D_R ≈ 82 %; at 24 m: q_t 3.76 MPa, "
          "F_r 4.7 % → clay, c_u = (3763 − 450)/20 = **166 kPa** · PMT initial modulus ≈ **63 MPa** (cavity strain 2.4 %)."),
 ),
]}

GEO[D["CP"]] = {"code": "CE203", "title": "Foundations 2 · Compaction specification (CE3116 Tut 1)", "sections": [
 sec("a) Compaction curves & ZAV", (1, 2),
   ("eq", r"\rho_d = \frac{\rho}{1+w},\qquad \rho_{d,ZAV/S_r} = \frac{G_s\rho_w}{1 + wG_s/S_r}"),
   ("md", "Low-w drop in dry density for the gravelly sand is **bulking**. Plot S_r = 100/85/70 % lines."),
 ),
 sec("b) Target density from D_R = 75 %", (3, 4),
   ("eq", r"\rho_{d,field} = \frac{\rho_{d,min}}{1 - D_R\left(\dfrac{\rho_{d,max} - \rho_{d,min}}{\rho_{d,max}}\right)}"),
   ("ex", "Borrow 1 (G_s 2.65, e 0.4–0.85)", "ρ_d,min 1432, ρ_d,max 1893 → target **1750 kg/m³**; SP MDD 1898 at OMC "
          "12.7 % → RC ≈ 92 %, w 8–17 %. Borrow 2 (sandy silt): SP MDD 1759 (RC ≈ 100 %, impractical) → use Modified "
          "Proctor (MDD 1856, w 13–19 %)."),
   ("md", "Achievable RC is 90–95 %; > 100 % means that energy can't reach the target."),
 ),
 sec("c–d) Rollers & lift thickness", (4, 4),
   ("md", "Gravelly sand: smooth-wheel or **vibratory**; sandy silt: pneumatic or **tamping-foot**. ~5 passes reach "
          "D_R 75 % to ≈ **0.5 m** lifts."),
 ),
 sec("Truck trips & water to add", (4, 6),
   ("ex", "300 × 300 × 3 m at 1750 kg/m³ → 472 500 t solids", "Borrow 1: M = 519 750 t wet; trips by mass 519 750/28 = "
          "**18 563** (governs) vs by volume 16 169 · Borrow 2: 19 406 trips. Water: (12.5 − 8) % × 472 500 t = "
          "**21 263 t** (borrow 1) and 14 175 t (borrow 2)."),
 ),
 sec("Sand-cone check", (6, 7),
   ("ex", "Zone A / Zone B", "A: V = 2980/1.55 = 1923 cm³ → ρ 1820, w 7 % → ρ_d **1701 < 1750** → add ≥ 1 % water · "
          "B: ρ_d **1695**, wet of optimum → dry it and add compactive effort."),
 ),
]}

GEO[D["ULS"]] = {"code": "CE203", "title": "Foundations 3 · Pad footings to EC7 — bearing resistance (CE3116)", "sections": [
 sec("Q1 Square pad on firm clay (G 800, Q 300 kN, D 2 m)", (1, 3),
   ("eq", r"\text{Undrained: } R/A' = (\pi + 2)c_u s_c + q\qquad \text{Drained: } R/A' = c'N_cs_ci_c + q'N_qs_qi_q + \tfrac{1}{2}\gamma'B'N_\gamma s_\gamma i_\gamma"),
   ("ex", "B = 2.2 m undrained", "V_k 1002 kN (incl. base, column, backfill) · C1 1803 < 1889 ✓ · C2 1392 < 1403 ✓."),
   ("ex", "Drained (φ′ 24°, GWT 0.6 m)", "Include uplift on the base (or use buoyant weights): V_k 936 kN · C2: φ_d 19.6° → "
          "R 1137 < V 1326 ✗ → **B = 2.4 m** (R 1377 > V 1352). Drained C2 governs."),
 ),
 sec("Q2 Inclined load (G 500, Q 1500, H 120 kN)", (3, 4),
   ("md", "Independent variable loads: horizontal × ψ₀ = 0.7. e = Hh/V → B′ = B − 2e; s and i factors with "
          "m = (2 + B′/L′)/(1 + B′/L′)."),
   ("ex", "B = 2.39 m", "C1 V 3110 < R 5384 · C2 V 2587 < R 2827 → **C2 governs**."),
 ),
 sec("Q3 Tall column: large moment (H 75 kN at 5 m)", (5, 6),
   ("md", "Vertical load is **favourable** for overturning → take G with γ = 1.0 and drop the variable vertical load."),
   ("ex", "B = 2.64 m", "C1: e = 1.12 m (e/B 0.43), B′ = 0.39 m, V 501 < R 509 · C2: V 501 < R 541 → C1 governs. With "
          "e/B > 1/3 add 0.2 m → **B ≈ 2.84 m**. (The slide's final '2.m' is a typo.)"),
 ),
]}

GEO[D["SLS"]] = {"code": "CE203", "title": "Foundations 4 · Stress distribution & settlement (CE3116)", "sections": [
 sec("Q1 Stress under an L-shaped footing (q 300 kPa, z 4 m)", (2, 5),
   ("ex", "Fadum / Newmark", "Three 2 × 2 m rectangles, m = n = 0.5 → I = 0.085 → Δσ = 3 × 0.085 × 300 = **76.5 kPa** · "
          "Newmark: 51 blocks × 0.005 × 300 = **76.5 kPa**."),
 ),
 sec("Q2a Immediate settlement — 6 m tank, 200 kPa", (6, 9),
   ("eq", r"s_i = \mu_0\mu_1\frac{qB}{E},\qquad E_{ave} = \frac{\sum E_iH_i}{\sum H_i}"),
   ("ex", "E_ave 17.5 MPa, H/B = 1, D/B = 0", "μ₀ 0.4, μ₁ 1.0 → **s_i = 27 mm**."),
 ),
 sec("Q2b–d e–log p′, Casagrande p′_c, Schmertmann correction", (10, 13),
   ("ex", "Clay: γ_sat 17.52, G_s 2.73", "w = 0.44 → e₀ = 1.20 · p′₀ (mid-clay) 38.6 kPa · **p′_c ≈ 81 kPa** (OC) · "
          "corrected curve: **C_c 0.42, C_ur 0.08** (field VCL through 0.42e₀)."),
 ),
 sec("Q2e Consolidation settlement (two sub-layers)", (14, 17),
   ("eq", r"s_{oed} = \frac{H}{1+e_0}\left[C_{ur}\log\frac{p'_c}{p'_0} + C_c\log\frac{p'_0 + \Delta p}{p'_c}\right],\qquad s_c = \mu\,s_{oed}"),
   ("ex", "Δp from the circular-load chart", "Layer 1 (Δp 160) **129 mm** + layer 2 (Δp 104) **90 mm** = 219 mm · "
          "Skempton–Bjerrum μ = 0.9 (A = 0.8) → **s_c = 197 mm**."),
 ),
 sec("Q2f–h Secondary compression & totals", (18, 21),
   ("eq", r"t_p = t_{100}\left(\frac{H_{field}}{H_{lab}}\right)^2,\qquad s_s = H\,C_\alpha\log\frac{t}{t_p}"),
   ("ex", "C_α 0.0035, t₁₀₀ 82 min", "t_p = 82 × (1.5/0.0135)² min = **1.93 yr** → s_s = 3000 × 0.0035 × log(100/1.93) = "
          "**18 mm** · totals 27 → 224 → **242 mm** (immediate 11 %, primary **81 %**, secondary 8 %)."),
 ),
]}

GEO[D["PILE"]] = {"code": "CE203", "title": "Foundations 5 · Piles to EC7: downdrag, load tests, tension (CE3116)", "sections": [
 sec("Q1 Downdrag on an end-bearing pile", (1, 2),
   ("eq", r"q_s = K_s\sigma'_v\tan\delta'\ (\text{sand}),\qquad q_s = c_u = 0.3\sigma'_v\ (\text{soft NC clay}),\qquad D_k = \sum q_sA_s"),
   ("ex", "250 mm pile through 4 m fill + 10 m soft clay to rock", "Sand: 0.455 × 36 × 0.649 × 4 = **42.5 kN** · clay: "
          "0.3 × 107.8 × 10 = **323.4 kN** · W_p 20.5 · design load C1 = 1.35(350 + 42.5 + 323.4 + 20.5) + 1.5 × 150 = "
          "**1219 kN**, C2 = 931 kN. Downdrag is a permanent action; on rock take the full (upper-bound) value."),
 ),
 sec("Q2 Resistance from static load tests (CFA Ø600, 11 m)", (3, 4),
   ("ex", "Two tests to 4000 kN, no failure", "R_ck = min(4000/ξ₁ 1.47, 4000/ξ₂ 1.35) = **2721 kN** (split 15 % base / "
          "85 % shaft) · C1 F 1920 < 2721 · C2: 2721/1.7 = **1601 kN** > F 1460 → OK (ratio 1.10 → C2 governs). Pile "
          "weight is excluded — the test already includes it."),
 ),
 sec("Q3 Resistance from ground parameters (same pile)", (5, 6),
   ("ex", "Undrained (q_b = 9c_u + σ_v, q_s = 0.4c_u, model factor 1.35)", "R_bk 1179 + R_sk 1758 → C1 2938 > 2021, C2 "
          "1950 > 1535 ✓."),
   ("ex", "Drained (N_q 60, K_s 1.5, δ′ 36°)", "Subtract base uplift 25 kN · R_bk 1386 + R_sk 1244 → C2 **1815 > 1510** ✓ "
          "(C2 governs)."),
 ),
 sec("Q4–Q5 Tension piles under a flooded tank", (7, 9),
   ("ex", "U_k = 3872 kN, W_k = 3200 kN", "Net uplift C1 1.35(U − W) = 907 kN, C2 672 kN · from test: R_tk = 2100/1.55 = "
          "1355 kN (the slide divides 2000, giving 1290) → C2 R = 1290/1.7 = 759 > 672 ✓ · from ground parameters: q_t = "
          "1.5 × 97.5 × tan 36° = 106 kPa → R_tk 1538 kN → C2 1538/2.0 = 769 > 672 ✓."),
   ("tip", "Netting U − W before factoring treats uplift and tank weight as one source. Factored separately "
           "(1.35U − 1.0W = 2027 kN) C1 would fail; EC7 UPL uses γ_dst 1.0 / γ_stb 0.9 (≈ 992 kN). The two answers also "
           "use different γ_s,t (1.7 vs 2.0) — check the Singapore NA table."),
 ),
]}

for _k in ("T2", "PS5", "ULS"):
    GEO[D[_k]]["sections"][0]["blocks"].append(EC7)


# ---------------------------------------------------------------- CE3115 lecture notes (OAP slopes, ERSS walls)
L = A + "Lectures/"
D.update({
    "L0": L + "OAP 0 Introduction.pdf", "LS": L + "OAP 1 Stability of Slopes R0.pdf", "LR": L + "OAP 9 Revision Notes R0.pdf",
    "E2": L + "ERSS 2 Earth Pressure Theories.pdf", "E2a": L + "ERSS 2a Mohr Circle Pole.pdf",
    "E3": L + "ERSS 3 Rigid Retaining Structures.pdf", "E4": L + "ERSS 4 Application of EC7 for ERSS.pdf",
    "E5": L + "ERSS 5 Flexible Retaining Structures.pdf", "E6": L + "ERSS 6 Introduction to Deep Excavations.pdf",
    "E7": L + "ERSS 7 Quiz key points.pdf",
})
OUTLINE += [("L0", 7, 0.4, ["CE203-01"]), ("LS", 80, 0.5, ["CE203-01"]), ("LR", 15, 4.5, ["CE203-01"]),
            ("E2", 175, 5.5, ["CE203-02"]), ("E2a", 4, 5.6, ["CE203-02"]), ("E3", 63, 7.5, ["CE203-03"]),
            ("E4", 57, 8.5, ["CE203-03"]), ("E5", 99, 9.5, ["CE203-03", "CE203-04"]), ("E6", 33, 11.5, ["CE203-04"]),
            ("E7", 9, 12.5, ["CE203-02", "CE203-03"])]
TEXT_ONLY = {D["LS"]}   # > 10 MB on Drive: notes written from its text; original pages not stored locally

GEO[D["L0"]] = {"code": "CE203", "title": "CE3115 · Course outline (slopes & earth-retaining structures)", "sections": [
 sec("Scope", (1, 7),
   ("md", "Part 1 (A/Prof Okky Purwana): stability of natural and man-made slopes — infinite slopes, mass procedure, "
          "Taylor's chart, Simplified Bishop, Spencer/Morgenstern–Price, stabilisation, all to **EC7 DA1**. Part 2 "
          "(ERSS): earth-pressure theory, rigid walls, EC7 for walls, flexible (sheet-pile/anchored) walls, deep "
          "excavations. Main references: Abramson et al. *Slope Stability and Stabilization*; Craig; Ou *Deep Excavation*."),
 ),
]}

GEO[D["LS"]] = {"code": "CE203", "title": "Slopes 0 · Stability of slopes — lecture notes (OAP)", "sections": [
 sec("Types and causes of slope failure", (9, 20),
   ("md", "Modes: **fall, topple, slide, spread, flow**. Slides: rotational circular (homogeneous fills/clays), "
          "non-circular (layered), **translational** (shallow plane parallel to the surface — sands, residual soil over "
          "rock; D/L ≪ 0.1), **compound** (deeper weak stratum; D/L 0.10–0.15); rotational D/L 0.15–0.33."),
   ("md", "Causes — **more shear stress**: steepening, overloading the crest, removing toe support (excavation, erosion, "
          "rapid drawdown), water in cracks, swelling clays, earthquakes. **Less strength**: rising GWT/saturation "
          "(loss of suction), seepage erosion, weathering, progressive/strain-softening failure."),
 ),
 sec("Geology & Singapore formations", (21, 27),
   ("md", "Residual soils (weathering grades VI → I), colluvium, alluvium, marine clays. Singapore: Bukit Timah "
          "Granite, Jurong Formation (weathered sedimentary rock), Old Alluvium, Kallang Formation (soft marine clay "
          "up to ~40 m). Rainfall-induced failures cluster in **Dec–Jan** on slopes steeper than ~27° (1V:2H)."),
 ),
 sec("Soil mechanics for slopes: drained vs undrained, total vs effective", (28, 41),
   ("md", "'Three rules': geometry, soil strength, **groundwater**. Dense sand/OC clay dilate (negative Δu when "
          "undrained → s_u > drained); loose sand/NC clay contract (positive Δu → s_u < drained)."),
   ("md", "**Embankment on soft clay**: FoS is lowest at end of construction (use s_u, φ_u = 0) and rises with "
          "consolidation. **Excavation in clay**: negative Δu dissipates → FoS falls with time → long-term drained "
          "(c′, φ′) analysis governs."),
 ),
 sec("Getting strength parameters", (42, 47),
   ("eq", r"\left(\frac{s_u}{\sigma'_{v0}}\right)_{NC} = 0.11 + 0.0037\,PI\ (\text{Skempton}),\qquad \frac{s_u}{\sigma'_{v0}} = 0.22\,OCR^{0.8}\ (\text{Ladd})"),
   ("md", "Tests: UU/unconfined → s_u (short term); CU with pore pressure or CD → c′, φ′; ring shear → residual. "
          "Sands from (N₁)₆₀: very loose 29–32°, loose 32–35°, medium 35–37°, dense 37–40°, very dense 40–42°; "
          "silty sand −3°, gravelly sand +2°."),
 ),
 sec("Groundwater effects", (48, 56),
   ("eq", r"u = \gamma_wh_w\cos^2\alpha_w\ (\text{flowing, parallel seepage}),\qquad \tau_f = c' + (u_a - u_w)\tan\phi^b + (\sigma - u_a)\tan\phi'\ (\text{unsaturated})"),
   ("md", "Suction adds 'apparent cohesion' that is lost when rain saturates the slope. Ponded water at the toe is "
          "**stabilising**."),
 ),
 sec("Analysis approaches & factor of safety", (57, 62),
   ("md", "Limit equilibrium (pre-defined surface, ULS only — this module), FEM (φ–c reduction, gives displacement), "
          "limit analysis. Traditional lumped FoS = available strength / mobilised stress: **≥ 1.3 temporary, ≥ 1.5 "
          "permanent**. EC7 uses partial factors instead."),
 ),
 sec("EC7 for slopes (Singapore NA: DA1 only)", (63, 67),
   ("md", "DA1-C1: A1 (γ_G 1.35 unfav/1.0 fav, γ_Q 1.5/0) + M1 (all 1.0). DA1-C2: A2 (γ_G 1.0, γ_Q 1.3) + M2 (tan φ′, "
          "c′ ÷ 1.25; c_u ÷ 1.4). FoS = factored resisting / factored disturbing ≥ 1.0. In C1, soil upslope of the "
          "rotation centre (α > 0) is unfavourable ×1.35; downslope (α < 0) favourable ×1.0."),
 ),
 sec("Infinite slopes", (68, 77),
   ("eq", r"F = \frac{c' + \left[(1-m)\gamma + m(\gamma_{sat} - \gamma_w)\right]z\cos^2\beta\tan\phi'}{\left[(1-m)\gamma + m\gamma_{sat}\right]z\cos\beta\sin\beta}\quad(\text{GWT at } mz \text{ above the slip plane})"),
   ("md", "Dry sand: F = tan φ′/tan β (independent of z). Saturated with parallel seepage: F = (γ′/γ_sat) tan φ′/tan β "
          "≈ **½** of dry. Slip-plane u: parallel seepage γ_wz cos²β, horizontal seepage γ_wz, downward "
          "drainage 0. For drained infinite slopes **only DA1-C2** matters (C1 scales both sides)."),
   ("tip", "This deck is 13.7 MB on Drive, so only its text was imported (to slide ~77); finite slopes, Bishop and "
           "Spencer are covered by the Revision Notes, Tutorial 2 and Assignment 1 pages."),
 ),
]}

GEO[D["LR"]] = {"code": "CE203", "title": "Slopes 5 · Revision notes — slopes checklist (OAP)", "sections": [
 sec("Strength & safety factor", (2, 4),
   ("md", "Natural/old slopes: pore pressures steady → **effective stress (c′, φ′)**. New slopes in clay: Δu hard to "
          "predict → **total stress (s_u, φ_u = 0)**, valid only for NC/lightly OC clay. GWT rise is detrimental; ponded "
          "water helps."),
 ),
 sec("Infinite slopes", (5, 5),
   ("md", "Check every layer interface; c′ = 0 dry or fully saturated → F independent of z; partially saturated → F "
          "falls with depth. **Only DA1-C2** applies."),
 ),
 sec("Mass procedure & Taylor's chart (short term, c_u)", (6, 7),
   ("eq", r"F = \frac{c_u\,r^2\theta}{W d},\qquad F = \frac{c_u}{N_s\gamma H}\quad(N_s = f(\beta, D))"),
   ("md", "DA1-C2 (c_u ÷ 1.4) normally governs. In C1 ideally split the mass into parts up/down-slope of the centre."),
 ),
 sec("Simplified Bishop — exam checklist", (8, 12),
   ("steps", ["Draw slices with numbers and key dimensions; boundaries at slope vertices, layer and GWT crossings.",
              "W per slice from trapezoids (show h_ave per layer); compute α from geometry (sin α = x/R).",
              "u = γ_w h_w (don't forget γ_w); one n_α per slice using the parameters at the slice base.",
              "C2: factor strength first; C1: 1.35/1.0 on W sin α by sign of α; surcharge variable, ponded water permanent.",
              "Divide external-load and water moments by R; tension crack: no strength but weight remains.",
              "Start F = 1.0 and iterate."]),
 ),
 sec("Spencer & stabilisation", (13, 14),
   ("md", "Spencer satisfies force **and** moment equilibrium (parallel interslice forces) — good for non-circular "
          "slips; Morgenstern–Price is more general. Stabilisation: **benching** removes mass where it drives most; "
          "flattening spreads the cut; **buttressing** adds restoring weight at the toe (less lever arm); **horizontal "
          "drains** lower the GWT → higher σ′."),
 ),
]}

GEO[D["E2"]] = {"code": "CE203", "title": "Earth pressure 0 · Lateral earth pressure theories (ERSS lecture)", "sections": [
 sec("At-rest pressure K₀", (6, 22),
   ("eq", r"K_{0,nc} = 1 - \sin\phi'\ (\text{Jaky}),\quad K_{nc} = 0.19 + 0.233\log PI\ (\text{Alpan}),\quad K_0 = K_{nc}\,OCR^{n},\ n = \sin\phi'\ \text{or}\ 0.54\times10^{-PI/281}"),
   ("md", "K₀ always uses **effective** stresses. Singapore marine clay (φ′ 22°, PI 55): K_nc ≈ 0.60–0.63. Heavily OC "
          "clays can have K₀ > 1 (Gault clay 2–4 → OCR ≈ 20–180)."),
 ),
 sec("Wall movement, active & passive states", (25, 35),
   ("md", "Wall moves away → σ′_h falls to K_aσ′_v (small movement, ~0.1–0.5 % H); towards the soil → rises to "
          "K_pσ′_v (much larger movement, several %). Disturbance during construction changes K₀."),
 ),
 sec("Rankine active (smooth wall, lower-bound)", (36, 74),
   ("eq", r"\sigma'_a = K_a\sigma'_v - 2c'\sqrt{K_a},\quad K_a = \frac{1-\sin\phi'}{1+\sin\phi'} = \tan^2\!\left(45^\circ - \frac{\phi'}{2}\right);\qquad \phi = 0:\ \sigma_a = \sigma_v - 2s_u"),
   ("md", "Slip planes at **45° + φ′/2** to the horizontal. Surcharge q adds K_aq uniformly. Tension depth "
          "z₀ = 2c′/(γ√K_a); ignore tension (cracks may fill with water). Sloping backfill β (c′ = 0): "
          "K_a = cos β (cos β − √(cos²β − cos²φ′))/(cos β + √(cos²β − cos²φ′))."),
 ),
 sec("Rankine passive", (75, 116),
   ("eq", r"\sigma'_p = K_p\sigma'_v + 2c'\sqrt{K_p},\quad K_p = \frac{1+\sin\phi'}{1-\sin\phi'} = \frac{1}{K_a};\qquad \phi = 0:\ \sigma_p = \sigma_v + 2s_u"),
   ("md", "Passive slip planes at 45° − φ′/2. Rankine is a lower bound (safe) but can't handle wall friction."),
 ),
 sec("Coulomb wedge method (upper bound, wall friction)", (117, 161),
   ("md", "Trial planar wedges; maximise P_a (minimise P_p) over the wedge angle; force polygons handle c, c_w, δ, "
          "sloping walls and backfills. Closed forms exist for cohesionless soil; P_a acts at δ to the wall normal → "
          "P_ah = P_a sin(α + δ). Usually δ ≈ ⅔φ′ for concrete."),
 ),
 sec("Curved surfaces: Caquot–Kérisel & EC7 Annex C", (162, 175),
   ("md", "Real passive surfaces are curved (log-spiral). Coulomb's plane **overestimates K_p badly when δ > φ′/3**; "
          "use Caquot–Kérisel tables or **EC7 Annex C** charts (K_ah, K_ph for δ = 0, ⅔φ′, φ′). Active is less "
          "sensitive."),
 ),
]}

GEO[D["E2a"]] = {"code": "CE203", "title": "Earth pressure 0a · Mohr circle & the pole method", "sections": [
 sec("Pole (origin of planes)", (1, 4),
   ("steps", ["Plot the stresses on two perpendicular planes and draw the circle.",
              "From the point for a known plane, draw a line parallel to that plane — it meets the circle at the **pole**.",
              "A line from the pole parallel to any other plane cuts the circle at the stresses on that plane.",
              "Principal planes: lines from the pole to σ₁ and σ₃."]),
   ("ex", "Quiz: σ_x = 12, σ_y = 0, τ = 6 kPa", "Pole at (0, −6); stresses on plane D–D′: σ = 12, τ = 6 kPa."),
 ),
]}

GEO[D["E3"]] = {"code": "CE203", "title": "Retaining 0 · Rigid retaining walls — stability checks (ERSS lecture)", "sections": [
 sec("Wall types & failure modes", (2, 11),
   ("md", "Gravity (mass), cantilever RC (L/T), counterfort/buttress, crib, gabion, reinforced soil. Failure modes: "
          "**sliding, overturning, bearing, deep-seated (overall) slip, seepage/piping**, plus structural failure."),
 ),
 sec("Sliding", (12, 22),
   ("eq", r"FoS_{sl} = \frac{N\tan\delta_b + c_bB + P_p}{P_a}\ \ge 1.5\ (\text{effective});\qquad \text{undrained base: } s_uB + P_p"),
   ("md", "δ_b ≈ ⅔φ′ to φ′. Passive in front is often ignored (it may be excavated or need large movement)."),
 ),
 sec("Overturning", (23, 26),
   ("eq", r"FoS_{OT} = \frac{\sum M_{resisting,\ toe}}{\sum M_{overturning,\ toe}}\ \ge 2"),
 ),
 sec("Bearing pressure & eccentricity", (27, 40),
   ("eq", r"e = \frac{B}{2} - \frac{\sum M_{net,toe}}{N},\qquad p_{max,min} = \frac{N}{B}\left(1 \pm \frac{6e}{B}\right)\ (e \le B/6),\qquad FoS_b = \frac{q_{ult}}{p_{max}}\ \ge 3"),
   ("md", "Keep the resultant in the **middle third**; if e > B/6 the heel lifts: p_max = 2N/(3(B/2 − e))."),
 ),
 sec("Overall slip & seepage", (41, 48),
   ("md", "Check a deep circular slip around the wall (slope methods). Drain the backfill (weep holes, filter, "
          "drainage blanket) — water pressure can double the thrust."),
 ),
 sec("Worked example", (49, 63),
   ("md", "Follow PS4: virtual back, Rankine pressures, tabulate forces and lever arms about the toe, then the three "
          "FoS checks."),
 ),
]}

GEO[D["E4"]] = {"code": "CE203", "title": "Retaining 0a · Eurocode 7 for earth-retaining structures (ERSS lecture)", "sections": [
 sec("Why limit states", (4, 14),
   ("md", "A single FoS hides where the uncertainty is; EC7 factors actions, materials and resistances separately. "
          "Singapore: SS EN 1997-1 + NA → **DA1 only**."),
 ),
 sec("Limit states & terminology", (15, 30),
   ("md", "**EQU** (rigid-body overturning), **STR** (structural), **GEO** (ground: sliding, bearing, overall), UPL "
          "(uplift), HYD (piping). Actions G/Q, favourable vs unfavourable; geometry tolerances (over-dig ΔH = 10 % of "
          "retained height ≤ 0.5 m); limit earth pressures from Annex C."),
 ),
 sec("Partial factor sets", (23, 26),
   ("md", "EQU: γ_G,dst 1.1, γ_G,stb 0.9, γ_Q 1.5, γ_φ′ = γ_c′ = 1.25 (corrected slide), γ_cu 1.4. GEO C1: γ_G 1.35/1.0, "
          "γ_Q 1.5, materials 1.0, R1 1.0. GEO C2: γ_G 1.0, γ_Q 1.3, tan φ′ and c′ ÷ 1.25, c_u ÷ 1.4, R1 1.0."),
 ),
 sec("Worked example: EQU overturning, GEO sliding & bearing", (31, 57),
   ("md", "Recompute K_a, K_p with design φ′ where required; factor the active thrust as destabilising and the wall "
          "weight/passive as stabilising; check E_d ≤ R_d. See PS5 for the full numbers (sliding fails with a smooth "
          "base in both combinations)."),
 ),
]}

GEO[D["E5"]] = {"code": "CE203", "title": "Retaining 0b · Flexible walls: cantilever & anchored (ERSS lecture)", "sections": [
 sec("Flexible walls & methods", (1, 13),
   ("md", "Sheet piles, soldier piles, contiguous/secant piles, D-walls — stability from **embedment passive "
          "resistance**. Numerical (FEM/subgrade reaction) or classical limit-equilibrium methods."),
 ),
 sec("Cantilever wall: simplified method", (14, 45),
   ("steps", ["Active K_aγ(h + d₀) behind, passive K_pγd₀ in front, ignore the toe reversal.",
              "Moments about the toe C → d₀; **D = 1.2 d₀** to allow for the reaction below C.",
              "M_max where shear = 0; Z = M_max/f_b."]),
 ),
 sec("Cantilever wall: net-pressure (more realistic) method", (46, 65),
   ("eq", r"a = \frac{p_{a1}}{\gamma(K_p - K_a)},\qquad \text{solve horizontal + moment equilibrium for } Y \text{ and } z;\ D = a + Y"),
 ),
 sec("Cantilever to EC7 DA1", (66, 78),
   ("md", "Apply partial factors to K (via design φ′) and actions, solve simultaneously for embedment; C2 usually "
          "governs embedment, C1 the bending moment."),
 ),
 sec("Single-propped/anchored walls: free earth support", (79, 98),
   ("md", "Wall rotates about the prop; take moments about the tie for D, then horizontal equilibrium for T. "
          "Traditional FS ≈ 2 on K_p (or a mobilised trapezoid). Free-earth support over-predicts moments in flexible "
          "walls — **Rowe/Potts–Fourie** moment-reduction factors depend on wall flexibility."),
 ),
]}

GEO[D["E6"]] = {"code": "CE203", "title": "Retaining 0c · Deep excavations: toe kick-in & basal heave (ERSS lecture)", "sections": [
 sec("Multi-propped walls & overall failure modes", (1, 12),
   ("md", "Two overall checks for braced excavations (BCA **TR26 (2010)**): **toe kick-in** of the embedded wall "
          "and **basal heave** of soft clay."),
 ),
 sec("Toe kick-in", (13, 16),
   ("eq", r"F_p = \frac{P_pL_p + M_s}{P_aL_a}\ \ge 1.5\ \text{(gross pressure method, moments about the lowest strut)};\quad F_p \ge 1.2 \text{ if } M_s = 0"),
 ),
 sec("Basal heave: Terzaghi (shallow, B > H_e)", (17, 28),
   ("eq", r"F_b = \frac{5.7s_uB_1 + s_{u}H_e}{(\gamma H_e + q_s)B_1},\quad B_1 = \frac{B}{\sqrt2}\ (\text{or } D \text{ if a hard layer is shallower})"),
   ("md", "Require F_b ≥ 1.5. Treats heave as a bearing failure with side shear on the vertical plane."),
 ),
 sec("Basal heave: Bjerrum & Eide (deep excavations)", (29, 31),
   ("eq", r"F_b = \frac{s_uN_c}{\gamma H_e + q_s}\quad(N_c \text{ from Skempton: } f(H_e/B, B/L))"),
 ),
 sec("Course wrap-up", (32, 33),
   ("md", "Part 2 learning outcomes: K₀/K_a/K_p, Rankine–Coulomb–Caquot-Kérisel, rigid and flexible wall design to "
          "EC7, deep-excavation stability."),
 ),
]}

GEO[D["E7"]] = {"code": "CE203", "title": "Retaining 6a · Quiz key points (ERSS, second paper)", "sections": [
 sec("Concepts", (1, 3),
   ("md", "K uses effective stresses ✓ · buttress walls use thin webs ✓ · Rankine is not the earliest (Coulomb 1776 "
          "came first) · Coulomb's driving moment is usually smaller because its inclined thrust has a stabilising "
          "vertical component."),
   ("ex", "Gault clay (φ′ 22°, PI 45, K₀ 2–4) → OCR", "Alpan: K_nc 0.575, n 0.373 → OCR **28–180** · Mayne–Kulhawy: "
          "K_nc 0.625, n 0.375 → OCR **22–142**."),
 ),
 sec("Gravity wall with 20° sloping backfill (c′ 25, φ′ 20°)", (6, 9),
   ("ex", "Answers", "β = φ′ → K_a = cos β = 0.94; z₀ = 2.87 m → P_a = 144.6 (horizontal 135.8) kN · K_p 2.04, P_p = "
          "**379.4 kN** · sliding **2.79** · overturning 822.5/187.2 = **4.39** · e = 0.04 m, p 187.5/148.5 kPa → "
          "bearing 450/187.5 = **2.4 < 3** ✗ · flattening the backfill drops K_a to 0.49 → both FoS rise."),
   ("tip", "The answer sheet's line '(2) σ_p = 125.8 kPa' is a copy-over from the other quiz; the base passive stress "
           "here is 181.5 kPa."),
 ),
]}


# ---------------------------------------------------------------- CE3116 lecture notes (foundations)
FL = F + "Lectures/"
D.update({
    "F1": FL + "1 CE3116_Intro.pdf", "F2": FL + "2 DeepFoundation.pdf", "F21": FL + "2.1 DeepFoundation AdditionalNotes.pdf",
    "F31": FL + "3.1 ShallowFoundation ULS PART1.pdf", "F32": FL + "3.2 ShallowFoundation SLS PART 2.pdf",
    "F4": FL + "4 Compaction of Soils R1.pdf", "F5": FL + "5 Site Investigation R1.pdf",
    "F6": FL + "6 Revision Lecture (Compaction and SI).pdf",
})
OUTLINE += [("F1", 8, 14.1, ["CE203-08"]), ("F5", 100, 19.1, ["CE203-05"]), ("F4", 64, 19.5, ["CE203-05"]),
            ("F6", 15, 19.8, ["CE203-05"]), ("F31", 79, 22.5, ["CE203-06"]), ("F32", 129, 23.5, ["CE203-09"]),
            ("F2", 113, 24.5, ["CE203-07"]), ("F21", 24, 24.6, ["CE203-07"])]
TEXT_ONLY.add(D["F5"])

GEO[D["F1"]] = {"code": "CE203", "title": "CE3116 · Foundation engineering course outline", "sections": [
 sec("Scope", (1, 8),
   ("md", "Shallow foundations (ULS bearing, SLS settlement), deep foundations (piles to EC7), soil compaction and "
          "site investigation. Design to **EC7 DA1** with the Singapore NA."),
 ),
]}

GEO[D["F5"]] = {"code": "CE203", "title": "Foundations 0 · Site investigation — lecture notes", "sections": [
 sec("Stages: desk study, reconnaissance, subsurface exploration", (1, 15),
   ("md", "Desk study (geological maps/memoirs, old boreholes, air photos, utilities, adjacent foundations) → "
          "walk-over (previous grading, landslides, drainage, distress in nearby buildings, access) → geophysics + "
          "boreholes/in-situ tests → **ground model** → design."),
 ),
 sec("Geophysical surveys", (16, 24),
   ("md", "Seismic refraction/reflection, surface waves (MASW) → stratigraphy and V_s (small-strain stiffness); "
          "resistivity, EM, GPR → layering, cavities, water (clay low resistivity, rock high); crosshole/downhole/"
          "suspension logging in boreholes. Use them to position boreholes."),
 ),
 sec("Planning: depth, number, sampling", (25, 35),
   ("md", "EC7-2 minimum depth below founding level: strip footing z_a ≥ max(6 m, 3b_F); raft z_a ≥ 1.5b_B; piles "
          "z_a ≥ max(b_g, 3D_F, 5 m) below the deepest toe (2 m if competent rock is proven). BCA/IES/ACES Advisory "
          "Note 1/03 (≥ 10 storeys): e.g. ~5 boreholes for 1200 m², 10 for 3000 m², 26 for 7500 m², placed at heavy "
          "columns. Sample every **1.5 m** (≤ 3 m) and at every change of stratum."),
 ),
 sec("SPT", (40, 54),
   ("eq", r"N_{60} = N\frac{E_r}{60}\lambda,\qquad (N_1)_{60} = N_{60}C_N,\quad C_N = \frac{200}{100 + \sigma'_v}\ (D_R 40\text{–}60\%),\ \frac{300}{200 + \sigma'_v}\ (60\text{–}80\%),\ \frac{170}{70 + \sigma'_v}\ (OC)\ \le 2"),
   ("md", "63.5 kg hammer, 760 mm drop, 150 mm seating + 2 × 150 mm counted. Rod-length λ: 0.75 (3–4 m), 0.85 "
          "(4–6 m), 0.95 (6–10 m), 1.0 (> 10 m). Clay: s_u ≈ 5N₆₀ kPa (Stroud f₁ ≈ 4.5–6 by PI); no C_N for clay. "
          "Disturbed sample only; unreliable in soft clay, silt and gravel."),
 ),
 sec("CPT / CPTu", (55, 72),
   ("eq", r"q_t = q_c + u_2(1 - a),\quad Q_t = \frac{q_t - \sigma_{v0}}{\sigma'_{v0}},\quad F_r = \frac{f_s}{q_t - \sigma_{v0}},\quad B_q = \frac{u_2 - u_0}{q_t - \sigma_{v0}},\quad s_u = \frac{q_t - \sigma_{v0}}{N_{kt}}"),
   ("md", "I_c zones: < 1.31 gravelly/dense sand · 1.31–2.05 clean to silty sand · 2.05–2.60 sand mixtures · "
          "2.60–2.95 silt mixtures · 2.95–3.60 clay · > 3.60 organic. N_kt 15–20 (10 soft, 30 fissured) — calibrate. "
          "σ′_p ≈ 0.33(q_t − σ_v0). Sands: Baldi D_R, φ′ = 17.6 + 11 log[q_t/(100σ′_v0)^0.5]; q_c 0–2.5 / 2.5–5 / "
          "5–10 / 10–20 / > 20 MPa ≈ very loose → very dense. Fast, continuous, no sample."),
 ),
 sec("Pressuremeter & other tests", (73, 100),
   ("md", "Ménard (pre-bored), self-boring, push-in. E from an unload–reload loop: E = 2(1 + ν)(V_c + V̄)Δp/ΔV; "
          "limit pressure p_L at V = V_c + 2V₀; s_u = (p_L − p₀)/N_p. Also vane shear (s_u in soft clay), "
          "dilatometer, undisturbed sampling (thin-wall, Mazier), field permeability (Hvorslev rising/falling head), "
          "piezometers."),
   ("tip", "This deck is 14 MB on Drive, so only its text was imported; page numbers here are approximate slide numbers."),
 ),
]}

GEO[D["F4"]] = {"code": "CE203", "title": "Foundations 0a · Compaction of soils — lecture notes", "sections": [
 sec("Principles & phase relations", (1, 13),
   ("eq", r"\rho_d = \frac{\rho}{1+w} = \frac{G_s\rho_w}{1+e},\qquad \rho_{d,S_r} = \frac{G_s\rho_w}{1 + wG_s/S_r}"),
   ("md", "Compaction expels **air** (not water) to raise density, strength and stiffness and cut permeability."),
 ),
 sec("Laboratory tests", (14, 25),
   ("md", "Standard Proctor (2.5 kg rammer, 3 layers × 27 blows) vs Modified (4.5 kg, 5 layers): more energy → higher "
          "MDD at lower OMC; curves sit left of the zero-air-voids line."),
 ),
 sec("Factors & soil types", (26, 37),
   ("md", "Coarse soils: bulking at low w (3–5 %), best compacted dry or saturated by **vibration**. Fine soils: dry of "
          "optimum → flocculated, stiffer, more permeable, swell-prone; wet of optimum → dispersed, flexible, less "
          "permeable (good for liners/cores)."),
 ),
 sec("Field equipment", (38, 44),
   ("md", "Smooth-wheel (crushed rock, sand), **vibratory** (granular), pneumatic-tyred (silts, mixed), sheepsfoot/"
          "tamping-foot (clays); lift thickness and number of passes from trials."),
 ),
 sec("Specification & control", (45, 63),
   ("md", "Specify relative compaction RC = ρ_d,field/ρ_d,max (typically ≥ 90–95 %) with a w window, or end-product D_R. "
          "Check by sand cone, nuclear gauge, core cutter, balloon; intelligent compaction monitoring for large fills."),
 ),
]}

GEO[D["F6"]] = {"code": "CE203", "title": "Foundations 0b · Revision: compaction & site investigation", "sections": [
 sec("Compaction checklist", (2, 6),
   ("steps", ["Plot both compaction curves with ZAV/S_r lines.", "Target ρ_d from D_R, then RC = target/MDD (aim 90–95 %).",
              "Allowable w range from the curve; pick rollers by soil type; lift thickness from D_R–depth chart.",
              "Truck trips: mass and volume capacity (with bulking) — the larger governs.", "Sand-cone results → adjust w or energy."]),
 ),
 sec("Site-investigation checklist", (7, 14),
   ("steps", ["SPT: E_r/60, rod λ, C_N only for sand → D_R → φ′ (±2–3° for gravelly/silty).",
              "CPTu: q_t, Q_t, F_r → I_c → soil type and k range; s_u = (q_t − σ_v0)/N_kt.",
              "PMT: unload–reload modulus, p_L, s_u = (p_L − p₀)/N_p.",
              "Hvorslev: T at H/H₀ = 0.37, k = πr²/(F T).", "Compare s_u from all methods with lab UU."]),
 ),
]}

GEO[D["F31"]] = {"code": "CE203", "title": "Foundations 1 · Shallow foundations: ULS bearing to EC7 — lecture notes", "sections": [
 sec("Foundation types & bearing failure modes", (1, 29),
   ("md", "Shallow (pads, strips, rafts; D/B ≲ 1) vs deep. Failure modes: general shear (dense/stiff), local shear, "
          "punching (loose/soft)."),
 ),
 sec("Limit states & EC7 sets", (30, 42),
   ("md", "ULS (bearing, sliding, overall) and SLS (settlement, rotation). DA1-C1 A1+M1+R1, DA1-C2 A2+M2+R1; foundation "
          "self-weight and backfill are permanent unfavourable for bearing."),
 ),
 sec("Effective area & undrained resistance", (43, 47),
   ("eq", r"B' = B - 2e_B,\ L' = L - 2e_L,\ A' = B'L';\qquad \frac{R}{A'} = (\pi + 2)c_ub_cs_ci_c + q,\quad s_c = 1 + 0.2\frac{B'}{L'}"),
 ),
 sec("Drained resistance (EC7 Annex D)", (48, 53),
   ("eq", r"\frac{R}{A'} = c'N_cb_cs_ci_c + q'N_qb_qs_qi_q + \tfrac12\gamma'B'N_\gamma b_\gamma s_\gamma i_\gamma"),
   ("eq", r"N_q = e^{\pi\tan\phi'}\tan^2\!\left(45^\circ + \frac{\phi'}{2}\right),\ N_c = (N_q - 1)\cot\phi',\ N_\gamma = 2(N_q - 1)\tan\phi',\ s_q = 1 + \frac{B'}{L'}\sin\phi',\ s_\gamma = 1 - 0.3\frac{B'}{L'}"),
   ("md", "Inclination: i_q = (1 − H/(V + A′c′cot φ′))^m, i_γ = (…)^{m+1}, m = (2 + B′/L′)/(1 + B′/L′)."),
 ),
 sec("Eccentric load & sliding", (54, 56),
   ("md", "Keep e within B/6 for SLS; if e/B > 1/3 take special care (enlarge). Sliding: H_d ≤ V′_d tan δ_d "
          "(drained) or A′c_u (undrained)."),
 ),
 sec("Worked examples (sand pad, stiff-clay pad)", (57, 79),
   ("md", "See the ULS tutorial page: C2 usually governs drained width; check undrained (c_u/1.4) and drained cases."),
 ),
]}

GEO[D["F32"]] = {"code": "CE203", "title": "Foundations 2 · Shallow foundations: settlement (SLS) — lecture notes", "sections": [
 sec("Components & limits", (3, 28),
   ("md", "s = s_i (immediate, undrained distortion) + s_c (consolidation) + s_s (secondary). EC7 guide limits: "
          "**max settlement 50 mm, differential 20 mm, relative rotation 1/500**."),
 ),
 sec("Footings on sand — SPT methods", (29, 52),
   ("md", "Terzaghi–Peck / Peck–Hanson–Thornburn / Meyerhof charts give allowable pressure for 25 mm settlement. "
          "Meyerhof: s = 7.68C_dq_net/(1.5N) for B < 1.2 m. Water-table and depth corrections (C_w, C_N)."),
 ),
 sec("Footings on sand — Schmertmann (CPT)", (53, 66),
   ("eq", r"s = C_1C_2\,q_{net}\sum\frac{I_z}{E}\Delta z,\quad C_1 = 1 - 0.5\frac{\sigma'_{v0}}{q_{net}},\quad C_2 = 1 + 0.2\log_{10}\frac{t}{0.1},\quad E \approx 2\text{–}4\,q_c"),
   ("md", "I_z peaks ≈ 0.6 at B/2 below the base (square) and goes to zero at 2B (square) / 4B (strip). Usually "
          "conservative."),
 ),
 sec("Footings on clay — immediate & consolidation", (67, 84),
   ("eq", r"s_i = \mu_0\mu_1\frac{qB}{E_u};\qquad s_{oed} = \sum\frac{H}{1+e_0}\left[C_r\log\frac{\sigma'_c}{\sigma'_0} + C_c\log\frac{\sigma'_0 + \Delta\sigma}{\sigma'_c}\right],\quad s_c = \mu\,s_{oed}"),
   ("md", "Janbu–Bjerrum–Kjaernsli μ₀ (D/B), μ₁ (H/B, L/B). Skempton–Bjerrum μ from pore-pressure A and H/B "
          "(≈ 0.6–1.0)."),
 ),
 sec("Stress distribution", (85, 98),
   ("md", "Boussinesq point load; pressure bulbs (≈ 0.1q at 2B square / 4B strip); overlapping bulbs under adjacent "
          "footings; Fadum influence factors for rectangle corners (superpose); Newmark chart; 2:1 spread as a check."),
 ),
 sec("Secondary compression & time", (99, 129),
   ("eq", r"s_s = H\,C_\alpha\log\frac{t}{t_p},\qquad t_p = t_{lab}\left(\frac{H_{dr,field}}{H_{dr,lab}}\right)^2"),
 ),
]}

GEO[D["F2"]] = {"code": "CE203", "title": "Foundations 3 · Piles to EC7 — lecture notes", "sections": [
 sec("Pile types & failure modes", (1, 6),
   ("md", "Driven (precast, steel), bored/cast-in-situ, CFA; end-bearing vs friction. ULS: ground (compression, "
          "tension), structural; SLS: settlement, downdrag, lateral."),
 ),
 sec("EC7 procedure", (7, 22),
   ("steps", ["Design actions F_c,d: C1 (A1: 1.35G + 1.5Q) and C2 (A2: 1.0G + 1.3Q); downdrag is a permanent action.",
              "Characteristic resistance from load tests (ξ₁, ξ₂), ground tests (ξ₃, ξ₄) or calculation (model factor).",
              "Design resistance R_c,d = R_b,k/γ_b + R_s,k/γ_s (R1 in C1, R4 in C2).", "Check F_c,d ≤ R_c,d for both."]),
 ),
 sec("Characteristic values & model factor", (23, 42),
   ("md", "Characteristic ground value = cautious estimate of the mean governing the limit state. Calculated "
          "resistance ÷ **model factor 1.55** (1.35 if verified by a load test). Load tests: "
          "R_ck = min(R_mean/ξ₁, R_min/ξ₂) (e.g. two tests: ξ₁ 1.47, ξ₂ 1.35)."),
 ),
 sec("Resistance factors R4 (C2)", (43, 50),
   ("md", "Driven: base 1.7 (1.5 with SLS check), shaft 1.5 (1.3), total 1.7 (1.5), tension 2.0 (1.7). Bored: base "
          "2.0 (1.7), shaft 1.6 (1.4), total 2.0 (1.7), tension 2.0 (1.7). CFA between the two. R1 (C1) all 1.0."),
 ),
 sec("Calculating resistance", (51, 73),
   ("eq", r"\text{Clay: } q_b = 9c_u + \sigma_{v0},\ q_s = \alpha c_u;\qquad \text{Sand: } q_b = N_q\sigma'_{v0},\ q_s = K_s\sigma'_{v0}\tan\delta'"),
   ("md", "α ≈ 0.4–0.5 for stiff clay; K_s depends on installation (higher for driven); N_q from Berezantsev. "
          "Subtract base uplift in drained analyses; include pile weight unless using load-test resistance."),
 ),
 sec("Downdrag example & SPT-based design", (77, 103),
   ("md", "Negative skin friction in settling soft clay adds to the load (full value if the toe is on rock). SPT "
          "design: cautious N in each stratum (ignore scattered fill values), q_s and q_b from N correlations, then "
          "factor and size the length."),
 ),
 sec("Tension piles & structural capacity", (104, 113),
   ("md", "R_t,d = R_t,k/γ_s,t; buoyancy and uplift checked with UPL as well as GEO; check the pile section "
          "structurally (concrete crushing, reinforcement in tension)."),
 ),
]}

GEO[D["F21"]] = {"code": "CE203", "title": "Foundations 3a · Pile design from SPT/CPT (additional notes)", "sections": [
 sec("SPT and CPT correlations for piles", (1, 24),
   ("md", "Supplementary slides on SPT (energy, corrections, EPRI EL-6800 correlations) and CPT (profiles, "
          "direct CPT pile design). Use local correlations for shaft and base resistance and calibrate with load tests."),
 ),
]}
