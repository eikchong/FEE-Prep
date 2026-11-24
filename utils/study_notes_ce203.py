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
