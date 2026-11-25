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

EC7 = ("tip", r"EC7 DA1 quick reference used throughout: **C1** (A1+M1+R1) $\gamma_G = 1.35$ unfav / 1.0 fav, "
              r"$\gamma_Q = 1.5$, strength unfactored; **C2** (A2+M2+R1) $\gamma_G = 1.0$, $\gamma_Q = 1.3$, "
              r"$\tan\phi'$ and $c'$ ÷ 1.25, $c_u$ ÷ 1.4. Check both; the worse one governs.")

GEO = {}

GEO[D["T1"]] = {"code": "CE203", "title": "Slopes 1 · Infinite slopes (CE3115 Tut 1)", "sections": [
 sec(r"Q1 Effect of slip depth, water, cohesion & weak seams ($\beta = 18^\circ$)", (2, 7),
   ("eq", r"F = \frac{c' + \sigma'_v\cos^2\beta\tan\phi'}{\sigma_v\cos\beta\sin\beta}\quad(\text{parallel seepage, slip plane at depth } z)"),
   ("ex", r"Slopes A–E at $z = 1$, 3, 5 m ($\gamma_{\mathrm{dry}}$ 16.5, $\gamma_{\mathrm{sat}}$ 20)",
    r"A dry, $\phi'$ 30°: **$F = 1.78$ at every depth** ($= \tan\phi'/\tan\beta$) · B GWT at 1 m: 1.78 / 1.15 "
    r"/ 1.04 · C GWT at surface: **0.89** at every depth (≈ $\tfrac12$ of dry, since "
    r"$\gamma'/\gamma_{\mathrm{sat}} \approx 0.5$) · D + $c' = 5\ \mathrm{kPa}$: 1.74 / 1.17 / 1.06 (cohesion "
    r"helps most at shallow depth — often ignored for conservatism) · E clay seam ($c'$ 0, $\phi'$ 25°) at 3 "
    "m: **0.72** — a weak layer governs, so check every interface with that layer's parameters."),
 ),
 sec(r"Q2 Sand over OC clay, $\beta$ 14–17°, EC7 DA1-C2", (8, 10),
   ("md", r"Effective-stress (slow failure); $\gamma_{\mathrm{sat}} = \gamma_{\mathrm{dry}}(1 + w) = 19.8$; "
          r"worst case **GWT at the surface**; check both slope angles. Design strength: $\phi'_d = \tan^{-1} "
          r"(\tan\phi'_k/1.25)$ → sand 33° → 27.5°, clay $c'$ 5 → 4 kPa, 28° → 23°."),
   ("ex", "F at 3 m (sand / clay) and 5 m (clay)", r"$\beta = 14^\circ$: 1.03 / 1.13 / 1.02 → just OK · $\beta "
                                                   r"= 17^\circ$: **0.84** / 0.93 / 0.83 → **unstable**. Use "
                                                   "the steepest local angle."),
 ),
]}

GEO[D["T2"]] = {"code": "CE203", "title": "Slopes 2 · Finite slopes: mass procedure, Taylor, Bishop (CE3115 Tut 2)", "sections": [
 sec(r"Q1 Short-term seabed trench in soft clay ($c_u$ 17, $\gamma$ 16, H 3 m, $\beta$ 60°)", (2, 4),
   ("eq", r"F = \frac{c_u r^2\theta}{W d}\qquad\text{Taylor: } F = \frac{c_u}{N_s\gamma H},\quad H_{max} = \frac{c_u/\gamma_{cu}}{N_s\gamma}"),
   ("ex", r"Mass procedure ($r = 5\ \mathrm{m}$, $\theta = 66^\circ$, $W = 8.1 \times 16$, $d = 2.03\ "
          r"\mathrm{m}$)", "C1 (×1.35 on driving): "
                                                                         r"$\boldsymbol{F = 1.38}$ · C2 ($c_u$ "
                                                                         r"÷ 1.4): $\boldsymbol{F = 1.33}$."),
   ("ex", r"Taylor (D → $\infty$, $\beta$ 60° → $N_s \approx 0.19$)", "C1 **1.38**, C2 **1.33** — identical, so the trial circle is "
                                                r"(close to) the critical one. $H_{\mathrm{max}}$: $\beta$ 60° "
                                                r"→ 4.0 m, $\beta$ 45° ($N_s$ 0.18) → only 4.2 m → "
                                                "contractor's claim is wrong; 60° needs less excavation "
                                                "volume."),
 ),
 sec("Q2 Two-layer natural slope — Simplified Bishop", (5, 9),
   ("eq", r"F = \frac{\sum\left[c'b + (W - ub)\tan\phi'\right]\dfrac{\sec\alpha}{1 + \tan\alpha\tan\phi'/F}}{\sum W\sin\alpha + M_N/R}"),
   ("ex", "Result", r"DA1-C1 $\boldsymbol{F = 0.94}$ (fails) · DA1-C2 $\boldsymbol{F = 1.08}$. C1 governs "
                    "here."),
 ),
 sec("How to apply EC7 in Bishop", (10, 13),
   ("steps", ["Slices: boundaries at slip entry/exit, slope breaks, layer and water-table crossings, load edges.",
              r"C1: ×1.35 on W $\sin\alpha$ of slices with **positive** $\alpha$ (driving); negative-$\alpha$ "
              "slices (resisting) unfactored; variable unfavourable surcharge ×1.5, favourable ignored.",
              r"C2: W unfactored, surcharge ×1.3, $c'/1.25$ and $\tan\phi'/1.25$ in the numerator **and in "
              r"$n_{\alpha}$**.",
              "External loads/ponded water: add $M_N/R$ to the denominator (negative if restoring).",
              r"Start with $F = 1$, compute $n_{\alpha}$, iterate until F converges (usually 2–3 rounds)."]),
 ),
 sec("Ponded water & other details", (14, 15),
   ("md", r"Ponded water acts normal to the surface: vertical $F_{\mathrm{wV}} = \gamma_w h_w b$, horizontal "
          r"$F_{\mathrm{wH}} = \gamma_w h_w b \tan\beta$, applied at mid-slice; its moment about the centre "
          "goes in as $M_N/R$ (usually restoring at the toe)."),
 ),
]}

GEO[D["A1"]] = {"code": "CE203", "title": "Slopes 3 · River-bank Bishop analysis (CE3115 Assignment 1)", "sections": [
 sec("1a Trial circle, 3 m tension crack, 50 kPa surcharge", (3, 7),
   ("md", "Omit the slice inside the tension crack (crack assumed dry, above GWT), so the surcharge length shrinks from "
          "8.5 to 7 m. 9 slices minimum; ponded water included as point loads."),
   ("ex", "Result", r"DA1-C1 $\boldsymbol{F = 1.083}$ · DA1-C2 $\boldsymbol{F = 1.248}$ (±0.05 depending on "
                    "slicing)."),
   ("md", "Common mistakes: too few slices; splitting a slice top/bottom; no boundary where the slip crosses "
          "the layer interface; forgetting ponded water or surcharge; adding water pressure in the crack; not "
          r"using reduced $\phi'$ in $n_{\alpha}$."),
 ),
 sec("1b Bed erosion of 3 m (DA1-C1)", (8, 10),
   ("ex", "Toe slice and its ponded water removed", "F drops **1.083 → 0.916** → unstable."),
 ),
 sec("1c Falling water level", (11, 11),
   ("md", "River level drops alone (rapid drawdown): lose the restoring ponded-water moment → F falls. River "
          r"and GWT both drop (long term): soil lighter and $\sigma'$ higher → F usually rises."),
 ),
 sec("Worked slice (slice 7, C1)", (12, 13),
   ("ex", r"$W = 3(19 \times 8.22 + 18 \times 2.25) = 590.1\ \mathrm{kN/m}$; $\alpha = \sin^{-1} (13.5/26) = "
          r"31.3^\circ$",
    r"Driving $1.35 \times 590.1 \sin 31.3^\circ = 413.6$ · $S = 13 \times 3 + (590.1 - 10 \times 7.97 \times "
    r"3) \tan 28^\circ = \boldsymbol{225.6}$ · $n_{\alpha}(F = 1) = 0.88$ → $T \approx 199\ \mathrm{kN/m}$. "
    "(The slide multiplies 232.3 × 0.88 — a typo; the table value 199.5 is right.)"),
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
   ("ex", r"Q2 sand $\phi$ 30°, e 0.5, $G_s$ 2.7, 15 m", r"GWT at surface: $\sigma'_v = 166.5$, $\sigma'_h = 83.3\ "
                                                 r"\mathrm{kPa}$ at 15 m · GWT lowered to 7 m: $\sigma'_v = "
                                                 r"123.9$ at 7 m and 212.7 at 15 m ($\sigma'_h$ half)."),
 ),
 sec("Q3–Q6 Concepts, tension cut, Rankine thrust", (3, 3),
   ("md", r"Passive needs much more movement: $\sigma_h$ must rise from $K_0\sigma_v$ past $\sigma_v$ to "
          r"$K_p\sigma_v$, versus a small drop to $K_a\sigma_v$."),
   ("eq", r"K_a = \frac{1-\sin\phi}{1+\sin\phi},\quad \sigma_a = K_a\sigma'_v - 2c'\sqrt{K_a},\quad z_0 = \frac{2c'}{\gamma\sqrt{K_a}}\ \left(\phi = 0:\ z_0 = \frac{2c_u}{\gamma}\right)"),
   ("ex", r"Q4 3 m cut, $c_u$ 30, $\gamma$ 16", r"Tension zone $2c_u/\gamma = \boldsymbol{3.75\ \mathrm{m} > 3\ "
                                      r"\mathrm{m}}$ → theoretically stands unsupported."),
   ("ex", r"Q5 7 m, $\gamma$ 17.3, $\phi$ 30° / Q6 5 m passive, $\gamma$ 18", r"$P_a = \tfrac12 (\tfrac13)(17.3)(7^2) = "
                                                          r"\boldsymbol{141\ \mathrm{kN/m}}$ horizontal at H/3 "
                                                          r"· $P_p = \tfrac12 (3)(18)(5^2) = \boldsymbol{675\ "
                                                          r"\mathrm{kN/m}}$."),
 ),
 sec(r"Q7 $c'\text{–}\phi'$ backfill (8 m, $c'$ 20, $\phi'$ 25°, $\gamma$ 17.5)", (4, 4),
   ("ex", "Thrust ignoring tension", r"$\sigma_a = -25.5\ \mathrm{kPa}$ at top, 31.3 at base; $z_0 = 3.59\ "
                                     r"\mathrm{m}$ → $P_a = \tfrac12 (4.41)(31.3) = \boldsymbol{69\ "
                                     r"\mathrm{kN/m}}$ at 1.47 m above base."),
 ),
 sec("Q8–Q10 Water in the backfill", (5, 7),
   ("ex", r"Q8 5 m, $\phi$ 36°", r"Dry: $P_a = \boldsymbol{57\ \mathrm{kN/m}}$ · saturated: $P_a$ 31.5 + water "
                           r"$122.5 = \boldsymbol{154\ \mathrm{kN/m}}$ (water dominates)."),
   ("ex", r"Q9 6 m, $\phi$ 32°, e 0.6", r"Dry: $\sigma_a$ 30.5, P 91.5 · submerged: $\sigma'_a$ 19.2, P 57.6 + water "
                                  "176.6 kN/m."),
   ("ex", "Q10 10 m, GWT 3 m, q 14 kPa", r"Sum the pressure-diagram parts ($K_a\gamma H_1$, $K_a\gamma'H_2$, "
                                         r"$K_aq$, $\gamma_wH_2$) → **502 kN/m**."),
 ),
 sec("Q11 Two layers + 50 kPa surcharge", (8, 9),
   ("ex", r"6 m wall; sand over $c'\text{–}\phi'$ clay, GWT 1.5 m", "Pressures jump at the interface (different $K_a$ and "
                                                       r"$-2c\sqrt{K_a}$). Total **294.6 kN/m** acting **2.17 "
                                                       "m** above the base."),
 ),
 sec("Q12 Passive with sloping backfill", (10, 11),
   ("tip", r"Rankine's sloping-backfill $K_p$ gives *decreasing* passive force as $\beta$ rises ($\beta "
           r"\approx 20^\circ$ for 450 kN) — unrealistic. Coulomb / Caquot–Kérisel show it increases; $450\ "
           r"\mathrm{kN} < 675\ \mathrm{kN}$ ($\beta = 0$) so no passive failure. Don't use Rankine passive "
           r"with $\beta > 0$."),
 ),
]}

GEO[D["PS3"]] = {"code": "CE203", "title": "Earth pressure 2 · Cohesion, Coulomb & curved surfaces (CE3115 PS3)", "sections": [
 sec("Q1–Q2 Clay backfill & tension cracks", (1, 3),
   ("ex", r"Q1 soft clay $c_u$ 10, $\gamma$ 16.5, 6 m", r"$z_0 = 2c_u/\gamma = \boldsymbol{1.21\ \mathrm{m}}$; "
                                              r"$\sigma_a$ at base 79 kPa; $P_a = 177\ \mathrm{kN/m}$ with "
                                              "tension, **189 kN/m** after cracking."),
   ("ex", r"Q2 $c'$ 12, $\phi'$ 20°, $\beta$ 10°, 4.6 m", r"$z_0 = 1.73\ \mathrm{m}$ → $P_a = \boldsymbol{41.5\ "
                                            r"\mathrm{kN/m}}$, horizontal 40.8."),
 ),
 sec("Q3–Q6 Coulomb, densification, layered", (4, 8),
   ("ex", r"Q3 Coulomb $\delta$ 15°", r"$K_a = 0.387$ → $P_a = \boldsymbol{46.4\ \mathrm{kN/m}}$ at H/3, inclined "
                              r"$\delta$ to the wall normal."),
   ("ex", r"Q4 loose (e 0.7, $\phi$ 30°) vs dense (e 0.4, $\phi$ 40°)", "$p_a$ 52 → 41 kPa, $p_p$ 468 → 870 kPa — "
                                                             "densifying lowers active and raises passive."),
   ("ex", r"Q5 7.32 m, c 12, $\phi$ 20°", r"$z_0 \approx 2.0\ \mathrm{m}$ → $\sigma_a = 45.3$ at base → "
                                    r"$\boldsymbol{P_a = 120\ \mathrm{kN/m}}$."),
   ("ex", "Q6 sandy clay over sand", r"$z_0 = 2.1\ \mathrm{m} > 1.5\ \mathrm{m}$ layer → crack through the "
                                     "clay; sand: 8.2 → 34.1 kPa."),
 ),
 sec("Q7–Q8 Active vs passive moments about the base", (9, 13),
   ("ex", "Q7 / Q8", r"Q7: $\sum P_a$ 215 kN at 2.09 m, $\sum P_p$ 323 kN at 1.33 m, $M_p/M_a = "
                     r"\boldsymbol{0.96}$ → rotates · Q8: $P_a$ 554 kN at 3.74 m, $P_p$ 389 kN, ratio "
                     "**0.31**. Water pressures on both sides cancel only if levels match."),
 ),
 sec("Q9–Q10 Surcharge, rough wall, flooding", (14, 15),
   ("ex", "Q9 8 m, q 15", r"Smooth 232 kN · rough $\delta$ 20°: 209 kN (horizontal 196)."),
   ("ex", "Q10 flood to surface", "Lateral force 62.4 → 39 (soil) + 125 (water) = 164 kN → **+163 %**. Drainage matters."),
 ),
 sec("Q11–Q13 Plane vs curved passive surfaces", (16, 19),
   ("ex", r"Q13 3 m wall, $\gamma$ 18, $\phi$ 37° — horizontal passive", "Rankine/Coulomb smooth **324** · Coulomb "
                                                            r"$\delta/\phi$ 0.5 → 674, 0.8 → 1254 · "
                                                            "Caquot–Kérisel curved 0.5 → **583**, 0.8 → **729 "
                                                            "kN/m**."),
   ("tip", r"Coulomb's plane surface overestimates passive badly for rough walls ($\delta > \phi/3$); use "
           r"curved-surface (Caquot–Kérisel) $K_p$. Q11–12: $\delta$ 20° → 10 230 vs 8 325 kN; $\delta$ 30° → "
           "19 947 vs 11 100 kN."),
 ),
]}

GEO[D["PS4"]] = {"code": "CE203", "title": "Retaining 2 · Gravity & cantilever walls, FoS (CE3115 PS4)", "sections": [
 sec(r"Q1 Gravity wall 6.6 × 3.2 m, $\phi'$ 35°, no front soil", (1, 2),
   ("eq", r"FoS_{OT} = \frac{\sum M_R}{\sum M_O}\ge 2,\quad FoS_{sl} = \frac{N\tan\delta_b + P_p + c_bB}{P_a}\ge 1.5,\quad p = \frac{N}{B}\left(1 \pm \frac{6e}{B}\right)"),
   ("ex", r"$K_a$ 0.27, $P_a$ 106 kN, W 507 kN, $\delta_b = 0.8\phi' = 28^\circ$", r"Overturning $811/233 = \boldsymbol{3.5}$ · "
                                                               r"sliding $269.5/106 = \boldsymbol{2.5}$ · $l = "
                                                               r"577.8/506.9 = 1.14\ \mathrm{m}$, $e = 0.46 < "
                                                               r"B/6$ → $p_{\mathrm{max}}$ **295**, "
                                                               r"$p_{\mathrm{min}}$ **22 kPa**."),
 ),
 sec("Q2–Q3 Adding 2 m of front soil; smooth base", (3, 5),
   ("ex", "Passive 133 kN at 0.67 m", "Q2: OT 3.86, sliding **3.8**, p 280/37 · Q3 smooth base: sliding "
                                      "133/106 = **$1.26 < 1.5$ ✗** (passive alone is not enough), p 254/63."),
   ("md", r"In bearing, only the passive actually mobilised ($P_p/\mathrm{FoS}_{\mathrm{sl}}$) is counted in "
          "the moment."),
 ),
 sec(r"Q4 $c'\text{–}\phi'$ backfill with 20 kPa surcharge", (6, 8),
   ("ex", r"$c'$ 10, $\phi'$ 25°, $\delta_b$ 15°, $c_b$ 10", r"$z_0 = 0.63\ \mathrm{m}$, $P_a = 131.7\ "
                                                             r"\mathrm{kN}$ · OT **3.5** · sliding (151 "
                                                             "passive + 136 friction + 32 adhesion)/131.7 = "
                                                             "**2.4** · p 283/34 kPa."),
 ),
 sec("Q5–Q6 Cantilever & gravity walls with heel soil", (9, 14),
   ("ex", r"Q5 sloping backfill $\beta$ 20°", r"$P_a = 71.3\ \mathrm{kN}$ (67 H, 24 V) · sliding **1.9** · OT **3.3** "
                                       "· p 99.6 / 40.2 kPa."),
   ("ex", "Q6 gravity wall on clay", "$P_a$ 93 kN at 1.78 m, $P_p$ 57 kN · OT **3.5** · sliding **1.9** · p "
                                     "167.5 / 39.4 kPa."),
   ("md", "Use a **virtual back** through the heel: soil above the heel counts as wall weight; Rankine applies there."),
 ),
]}

GEO[D["PS5"]] = {"code": "CE203", "title": "Retaining 3 · Same wall to EC7 DA1 (CE3115 PS5)", "sections": [
 sec("EQU (overturning)", (1, 2),
   ("md", r"$\gamma_{\mathrm{G,dst}}$ 1.1, $\gamma_{\mathrm{G,stb}}$ 0.9, $\gamma_{\phi}$ 1.25 → $\phi_d = "
          r"29.3^\circ$, $K_a$ 0.343, $K_p$ 2.92. Stabilising 793 > destabilising 325 kNm → OK (over-design "
          "2.4)."),
 ),
 sec("GEO DA1-C1 (sliding, bearing)", (3, 5),
   ("ex", "Smooth base, passive only", r"$P_a = 1.35 \times 106 = \boldsymbol{143\ \mathrm{kN}} > P_p = 133\ "
                                       r"\mathrm{kN}$ → **sliding fails**. Fix sliding before checking "
                                       "bearing."),
   ("tip", "In the bearing check the solution factors N by 1.35 but leaves the moments unfactored, giving $e "
           r"= 0.74\ \mathrm{m}$ and $p_{\mathrm{min}} = -83\ \mathrm{kPa}$. Keep factors consistent (factor "
           "the action effects together) when you redo it."),
 ),
 sec("GEO DA1-C2", (5, 6),
   ("ex", r"$\phi_d$ 29.3°", "$P_a = 134.3 > P_p$ 105.1 → **sliding fails** · bearing p 289/28 kPa ($e = 0.44 "
                             "< B/6$)."),
 ),
]}

GEO[D["PS6"]] = {"code": "CE203", "title": "Retaining 4 · Cantilever sheet piles (CE3115 PS6)", "sections": [
 sec(r"Q1–Q2 Cantilever in sand (H 6 m, $\gamma$ 17, $\phi$ 30°)", (1, 6),
   ("steps", [r"Simplified: moments about the toe C of active $K_a\gamma(H + d_0)$ and passive $K_p\gamma d_0$ "
              "→ $d_0$; design $D = 1.2 d_0$.",
              "Max moment at zero shear: $K_a(H + d_s)^2 = K_p d_s^2$.",
              r"Section modulus $Z = M_{\mathrm{max}}/f_b$."]),
   ("ex", "Answers", r"$0.944(6 + d_0)^3 = 8.5 d_0^3$ → $d_0 = 5.56$ → $\boldsymbol{D = 6.7\ \mathrm{m}}$ · "
                     r"$d_s = 3\ \mathrm{m}$ → $\boldsymbol{M_{\mathrm{max}} = 460\ \mathrm{kNm/m}}$ · $Z = "
                     r"460/175\,000 = \boldsymbol{2.63 \times 10^{-3}\ \mathrm{m^3/m}}$. Net-pressure method: "
                     r"$D \approx 6.0\ \mathrm{m}$, same $M_{\mathrm{max}}$."),
   ("tip", r"The solution writes $Z = 26.25 \times 10^{-2}\ \mathrm{m^3}$ — a units slip; 460 kNm ÷ $175\,000\ "
           r"\mathrm{kPa} = 2.63 \times 10^{-3}\ \mathrm{m^3}$ per metre."),
 ),
 sec("Q3–Q4 Same wall with water at 3 m both sides", (7, 11),
   ("ex", "Water cancels (equal levels)", r"Simplified $d_0 = 7.3$ → $\boldsymbol{D = 8.7\ \mathrm{m}}$, "
                                          r"$M_{\mathrm{max}}$ **504 kNm** at 4 m · net-pressure: $D = 7.8\ "
                                          r"\mathrm{m}$, $M_{\mathrm{max}}$ 506 kNm."),
 ),
 sec("Q5 Layered sand (limiting pressure profile)", (12, 15),
   ("ex", "Loose over medium-dense sand", r"Solve horizontal and moment equilibrium together: $d = 3.82\ "
                                          r"\mathrm{m}$, $z = 0.41\ \mathrm{m}$ → $\boldsymbol{D \approx 3.9\ "
                                          r"\mathrm{m}}$ · $M_{\mathrm{max}}$ **198 kNm** at 1.83 m below "
                                          "dredge level."),
 ),
]}

GEO[D["PS7"]] = {"code": "CE203", "title": "Retaining 5 · Anchored walls, free-earth support (CE3115 PS7)", "sections": [
 sec("Q1 Free earth support (tie 1 m below top)", (1, 3),
   ("steps", [r"Draw active (dry above GWT, $\gamma'$ below) and passive $K_p\gamma'D$; water cancels if "
              "levels match.",
              "Moments about the tie T → cubic in D.", "Horizontal equilibrium → tie force T."]),
   ("ex", "Answer", r"$\boldsymbol{D = 2.22\ \mathrm{m}}$, $\boldsymbol{T = 30.5\ \mathrm{kN/m}}$."),
 ),
 sec("Q2–Q3 Factor of safety on passive", (4, 8),
   ("ex", "FS 2", r"$K_{\mathrm{pm}} = K_p/2$ → **$D = 4.0\ \mathrm{m}$, $T = 37.8\ \mathrm{kN/m}$** · "
                  r"trapezoidal mobilised passive ($\alpha = 0.293$) → **$D = 4.25\ \mathrm{m}$, $T = 32.3\ "
                  r"\mathrm{kN/m}$**."),
 ),
]}

GEO[D["QZ"]] = {"code": "CE203", "title": "Retaining 6 · Past-year quiz (earth pressure & walls)", "sections": [
 sec("True/false concepts", (1, 2),
   ("md", "Gravity walls: dead weight is critical, not embedment (embedment matters for flexible walls) · "
          "soldier pile & lagging can't be used below a high water table without dewatering · $K_p > 1$ means "
          r"$\sigma'_h > \sigma'_v$ · Coulomb's plane passive surface can be far from reality."),
 ),
 sec("$K_0$ from OCR; Mohr pole", (3, 5),
   ("eq", r"K_{0,OC} = (1 - \sin\phi')\,OCR^{\sin\phi'}"),
   ("ex", r"$\sigma'_p = 100\ \mathrm{kPa}$ (from oedometer), $\sigma'_{v0} = 33$, $\phi'$ 35°", r"$\mathrm{OCR} \approx 3$ → $\boldsymbol{K_0 "
                                                                 "= 0.81}$. Mohr question: pole at (6, −4), "
                                                                 "shear on vertical plane 4 kPa."),
 ),
 sec(r"Gravity wall 7 m ($c'$ 10, $\phi'$ 28°, 2 m front soil, no base friction)", (6, 9),
   ("ex", "Answers", r"$K_a$ 0.361, $\sigma_a$ 30.2, $P_a$ 75.6 kN · $K_p$ 2.77, $\sigma_p$ 33.3 → 125.8 kPa, "
                     r"$P_p$ 159.1 kN · sliding $159.1/75.6 = \boldsymbol{2.11}$ · overturning $709/126 = "
                     r"\boldsymbol{5.6}$ · $e = 0.26\ \mathrm{m}$, $p_{\mathrm{max}}$ **211.5**, "
                     r"$p_{\mathrm{min}}$ 66 kPa → bearing FoS 500/211.5 = **$2.36 < 3$ ✗**. Surcharge behind "
                     "raises $P_a$ → both FoS fall."),
   ("md", r"The quiz answer ignores the $c'$ reduction on the active side ($\sigma_a = K_a\gamma z$) — "
          "conservative."),
 ),
]}

GEO[D["EX"]] = {"code": "CE203", "title": "Exam · CE3115 AY19/20 paper (slopes, walls, sheet piles)", "sections": [
 sec("Q1 River bank with bench & tension crack (Bishop, DA1-C2)", (2, 5),
   ("ex", "Answer key", r"1a first-trial $\boldsymbol{F \approx 1.2}$ (50 kPa surcharge) · 1b rock at +2 m "
                        "forces a non-circular/compound slip → F likely rises; analyse with Spencer or "
                        r"Morgenstern–Price · 1c erosion: $F \approx \boldsymbol{0.9}$ → potentially unstable."),
 ),
 sec("Q2 Seabed trench (same as Tut 2 Q1)", (5, 6),
   ("ex", "Answer key", "Mass procedure **1.33**; Taylor **1.33** (critical circle found); 45° gives no real depth gain — "
          "60° is cheaper."),
 ),
 sec("Q3 Cantilever wall, layered backfill, EC7 sliding", (7, 8),
   ("md", "Theory: Coulomb's plane passive surface errs for rough walls; Rankine's driving moment is usually "
          "bigger because Coulomb's thrust is inclined (its vertical component helps). Min surcharge for no "
          r"crack in the sandy clay: $K_aq - 2c'\sqrt{K_a} \ge 0$ at the top, i.e. $\boldsymbol{q = "
          r"2c'/\sqrt{K_a}}$ ($c'$ 13, $\phi'$ 24° → $K_a$ 0.42 → $q \approx 40\ \mathrm{kPa}$). No official "
          "numbers for the rest."),
 ),
 sec("Q4 Sheet pile in clay ($s_u$ 30) with sand backfill", (8, 9),
   ("md", "Flexible walls rely on embedment because passive resistance is their main stabilising force; "
          r"gravity walls rely on weight. Q4b/c: work back the backfill height h from $D = 3.6\ \mathrm{m}$ "
          "(net clay pressure $4c_u - q$ in front) — no official answer supplied."),
 ),
]}

GEO[D["SI"]] = {"code": "CE203", "title": "Foundations 1 · Site investigation: SPT, CPTu, PMT, permeability (CE3116 Tut 2)", "sections": [
 sec("a) SPT corrections", (1, 2),
   ("eq", r"(N_1)_{60} = N\cdot\frac{E_r}{60}\cdot\lambda\cdot C_N,\qquad C_N = \frac{300}{200 + \sigma'_v}\ (\text{dense sand}),\qquad s_u \approx 5N_{60}\ \text{kPa}"),
   ("ex", r"3 m gravelly sand (N 28, $\sigma'_v$ 47.5) / 10 m clay (N 8)", r"$28 \times 70/60 \times 0.75 \times 1.21 "
                                                                   r"\approx \boldsymbol{30}$ → $D_R$ 65–85 % "
                                                                   r"→ $\phi'$ 37° + 2° (gravelly) = **39°** · "
                                                                   r"clay: $8 \times 70/60 \times 0.95 \approx "
                                                                   r"9$ → $\boldsymbol{s_u \approx 45\ "
                                                                   r"\mathrm{kPa}}$ (no $C_N$ for clay)."),
 ),
 sec("b–c) CPTu: soil type & strength", (2, 3),
   ("eq", r"q_t = q_c + (1-a)u_2,\quad Q_t = \frac{q_t - \sigma_{v0}}{\sigma'_{v0}},\quad F_r = \frac{f_s}{q_t - \sigma_{v0}},\quad I_c = \sqrt{(3.47 - \log Q_t)^2 + (1.22 + \log F_r)^2}"),
   ("ex", "3 m", "$q_t$ 9.13 MPa, $Q_t$ 191, $F_r$ 0.19 % → **$I_c = 1.29 < 1.31$ → gravelly/dense sand** ✓ · "
                 r"Baldi: $D_R \approx 80\,\%$ → $\phi'$ 39°."),
   ("ex", "10 m clay", r"$q_t = 0.76 + 0.25 \times 0.202 = 0.81\ \mathrm{MPa}$, $\sigma_{v0}$ 194 kPa → $s_u = "
                       r"(q_t - \sigma_{v0})/N_{\mathrm{kt}} = \boldsymbol{31\ \mathrm{kPa}}$."),
 ),
 sec("d–e) Menard pressuremeter", (3, 4),
   ("eq", r"E = 2(1+\nu)\left[V_c + \bar V\right]\frac{\Delta p}{\Delta V},\qquad s_u = \frac{p_L - p_0}{N_p}"),
   ("ex", "Unload–reload points 5–6", r"$E_{\mathrm{ur}} = 3 \times 936 \times 50/14 = \boldsymbol{10\ "
                                      r"\mathrm{MPa}}$, $G = 3.3\ \mathrm{MPa}$, cavity strain 0.8 % · $p_0$ "
                                      "144, $p_L$ 360 (at $V = V_c + 2V_0$) → $s_u = 216/5.5 = "
                                      r"\boldsymbol{39\ \mathrm{kPa}}$."),
 ),
 sec("f–g) Compare $s_u$; Hvorslev permeability", (5, 5),
   ("ex", "$s_u$ at 10 m", "SPT 45, CPT 31, PMT 39, lab UU 36 kPa — lab is the direct measure; calibrate "
                         r"$N_{\mathrm{kt}}$, $N_p$ to it."),
   ("eq", r"k = \frac{\pi r^2}{F\,T},\qquad F = \frac{2\pi L}{\ln\left[L/D + \sqrt{1 + (L/D)^2}\right]}"),
   ("ex", "L 0.3 m, D 0.1 m, T (at $H/H_0 = 0.37$) ≈ 80 s", r"$F = 1.04\ \mathrm{m}$ → $\boldsymbol{k = 9.4 "
                                                         r"\times 10^{-5}\ \mathrm{m/s}}$, within the CPTu "
                                                         r"range $10^{-5}\text{–}10^{-3}\ \mathrm{m/s}$."),
   ("tip", "The solution calls $I_c = 2.0$ 'gravelly sand'; on Robertson's chart 1.31–2.05 is zone 6 (clean "
           "to silty sand). The k range quoted still fits."),
 ),
]}

GEO[D["SIX"]] = {"code": "CE203", "title": "Foundations 1a · Site investigation worked example (CE3116)", "sections": [
 sec("Classification, SPT, CPTu, PMT, Hvorslev", (1, 9),
   ("md", r"Same workflow as Tut 2 at different depths: LL 30, PL 15 → PI 15 · corrected $N \approx 32$ (sand "
          r"→ $\phi'$; clay → $c_u = 5N = 160\ \mathrm{kPa}$) · CPTu at 12.5 m: $q_t$ 17.08 MPa, $F_r$ 1.03 % "
          r"→ sand, $D_R \approx 82\,\%$; at 24 m: $q_t$ 3.76 MPa, $F_r$ 4.7 % → clay, $c_u = (3763 - 450)/20 "
          r"= \boldsymbol{166\ \mathrm{kPa}}$ · PMT initial modulus ≈ **63 MPa** (cavity strain 2.4 %)."),
 ),
]}

GEO[D["CP"]] = {"code": "CE203", "title": "Foundations 2 · Compaction specification (CE3116 Tut 1)", "sections": [
 sec("a) Compaction curves & ZAV", (1, 2),
   ("eq", r"\rho_d = \frac{\rho}{1+w},\qquad \rho_{d,ZAV/S_r} = \frac{G_s\rho_w}{1 + wG_s/S_r}"),
   ("md", r"Low-w drop in dry density for the gravelly sand is **bulking**. Plot $S_r = 100/85/70\,\%$ lines."),
 ),
 sec(r"b) Target density from $D_R = 75\,\%$", (3, 4),
   ("eq", r"\rho_{d,field} = \frac{\rho_{d,min}}{1 - D_R\left(\dfrac{\rho_{d,max} - \rho_{d,min}}{\rho_{d,max}}\right)}"),
   ("ex", "Borrow 1 ($G_s$ 2.65, e 0.4–0.85)", r"$\rho_{\mathrm{d,min}}$ 1432, $\rho_{\mathrm{d,max}}$ 1893 → "
                                             r"target $\boldsymbol{1750\ \mathrm{kg/m^3}}$; SP MDD 1898 at OMC "
                                             r"12.7 % → $\mathrm{RC} \approx 92\,\%$, w 8–17 %. Borrow 2 "
                                             r"(sandy silt): SP MDD 1759 ($\mathrm{RC} \approx 100\,\%$, "
                                             "impractical) → use Modified Proctor (MDD 1856, w 13–19 %)."),
   ("md", "Achievable RC is 90–95 %; > 100 % means that energy can't reach the target."),
 ),
 sec("c–d) Rollers & lift thickness", (4, 4),
   ("md", "Gravelly sand: smooth-wheel or **vibratory**; sandy silt: pneumatic or **tamping-foot**. ~5 passes "
          "reach $D_R$ 75 % to ≈ **0.5 m** lifts."),
 ),
 sec("Truck trips & water to add", (4, 6),
   ("ex", r"300 × 300 × 3 m at $1750\ \mathrm{kg/m^3}$ → 472 500 t solids", r"Borrow 1: $M = 519\,750\ \mathrm{t}$ wet; "
                                                              r"trips by mass $519\,750/28 = "
                                                              r"\boldsymbol{18\,563}$ (governs) vs by volume "
                                                              "16 169 · Borrow 2: 19 406 trips. Water: $(12.5 "
                                                              r"- 8)\,\% \times 472\,500\ \mathrm{t} = "
                                                              r"\boldsymbol{21\,263\ \mathrm{t}}$ (borrow 1) "
                                                              "and 14 175 t (borrow 2)."),
 ),
 sec("Sand-cone check", (6, 7),
   ("ex", "Zone A / Zone B", r"A: $V = 2980/1.55 = 1923\ \mathrm{cm^3}$ → $\rho$ 1820, w 7 % → $\rho_d$ "
                             r"$\boldsymbol{1701 < 1750}$ → add ≥ 1 % water · B: $\rho_d$ **1695**, wet of "
                             "optimum → dry it and add compactive effort."),
 ),
]}

GEO[D["ULS"]] = {"code": "CE203", "title": "Foundations 3 · Pad footings to EC7 — bearing resistance (CE3116)", "sections": [
 sec("Q1 Square pad on firm clay (G 800, Q 300 kN, D 2 m)", (1, 3),
   ("eq", r"\text{Undrained: } R/A' = (\pi + 2)c_u s_c + q\qquad \text{Drained: } R/A' = c'N_cs_ci_c + q'N_qs_qi_q + \tfrac{1}{2}\gamma'B'N_\gamma s_\gamma i_\gamma"),
   ("ex", r"$B = 2.2\ \mathrm{m}$ undrained", "$V_k$ 1002 kN (incl. base, column, backfill) · C1 $1803 < 1889$ ✓ · C2 "
                                 "$1392 < 1403$ ✓."),
   ("ex", r"Drained ($\phi'$ 24°, GWT 0.6 m)", "Include uplift on the base (or use buoyant weights): $V_k$ "
                                               r"936 kN · C2: $\phi_d$ 19.6° → $R = 1137 < V = 1326$ ✗ → "
                                               r"$\boldsymbol{B = 2.4\ \mathrm{m}}$ ($R = 1377 > V = 1352$). "
                                               "Drained C2 governs."),
 ),
 sec("Q2 Inclined load (G 500, Q 1500, H 120 kN)", (3, 4),
   ("md", r"Independent variable loads: horizontal × $\psi_0 = 0.7$. $e = Hh/V$ → $B' = B - 2e$; s and i "
          "factors with $m = (2 + B'/L')/(1 + B'/L')$."),
   ("ex", r"$B = 2.39\ \mathrm{m}$", "C1 $V = 3110 < R = 5384$ · C2 $V = 2587 < R = 2827$ → **C2 governs**."),
 ),
 sec("Q3 Tall column: large moment (H 75 kN at 5 m)", (5, 6),
   ("md", r"Vertical load is **favourable** for overturning → take G with $\gamma = 1.0$ and drop the variable "
          "vertical load."),
   ("ex", r"$B = 2.64\ \mathrm{m}$", r"C1: $e = 1.12\ \mathrm{m}$ (e/B 0.43), $B' = 0.39\ \mathrm{m}$, $V = "
                                     "501 < R = 509$ · C2: $V = 501 < R = 541$ → C1 governs. With $e/B > 1/3$ "
                                     r"add 0.2 m → $\boldsymbol{B \approx 2.84\ \mathrm{m}}$. (The slide's "
                                     "final '2.m' is a typo.)"),
 ),
]}

GEO[D["SLS"]] = {"code": "CE203", "title": "Foundations 4 · Stress distribution & settlement (CE3116)", "sections": [
 sec("Q1 Stress under an L-shaped footing (q 300 kPa, z 4 m)", (2, 5),
   ("ex", "Fadum / Newmark", r"Three 2 × 2 m rectangles, $m = n = 0.5$ → $I = 0.085$ → $\Delta \sigma = 3 "
                             r"\times 0.085 \times 300 = \boldsymbol{76.5\ \mathrm{kPa}}$ · Newmark: 51 blocks "
                             r"× $0.005 \times 300 = \boldsymbol{76.5\ \mathrm{kPa}}$."),
 ),
 sec("Q2a Immediate settlement — 6 m tank, 200 kPa", (6, 9),
   ("eq", r"s_i = \mu_0\mu_1\frac{qB}{E},\qquad E_{ave} = \frac{\sum E_iH_i}{\sum H_i}"),
   ("ex", r"$E_{\mathrm{ave}}$ 17.5 MPa, $H/B = 1$, $D/B = 0$", r"$\mu_0$ 0.4, $\mu_1$ 1.0 → $\boldsymbol{s_i = 27\ "
                                              r"\mathrm{mm}}$."),
 ),
 sec(r"Q2b–d $e\text{–}\log p'$, Casagrande $p'_c$, Schmertmann correction", (10, 13),
   ("ex", r"Clay: $\gamma_{\mathrm{sat}}$ 17.52, $G_s$ 2.73", "$w = 0.44$ → $e_0 = 1.20$ · $p'_0$ (mid-clay) "
                                                              r"38.6 kPa · $\boldsymbol{p'_c \approx 81\ "
                                                              r"\mathrm{kPa}}$ (OC) · corrected curve: **$C_c$ "
                                                              r"0.42, $C_{\mathrm{ur}}$ 0.08** (field VCL "
                                                              "through $0.42e_0$)."),
 ),
 sec("Q2e Consolidation settlement (two sub-layers)", (14, 17),
   ("eq", r"s_{oed} = \frac{H}{1+e_0}\left[C_{ur}\log\frac{p'_c}{p'_0} + C_c\log\frac{p'_0 + \Delta p}{p'_c}\right],\qquad s_c = \mu\,s_{oed}"),
   ("ex", r"$\Delta p$ from the circular-load chart", r"Layer 1 ($\Delta p$ 160) **129 mm** + layer 2 ($\Delta "
                                                      r"p$ 104) $\boldsymbol{90\ \mathrm{mm}} = 219\ "
                                                      r"\mathrm{mm}$ · Skempton–Bjerrum $\mu = 0.9$ ($A = "
                                                      r"0.8$) → $\boldsymbol{s_c = 197\ \mathrm{mm}}$."),
 ),
 sec("Q2f–h Secondary compression & totals", (18, 21),
   ("eq", r"t_p = t_{100}\left(\frac{H_{field}}{H_{lab}}\right)^2,\qquad s_s = H\,C_\alpha\log\frac{t}{t_p}"),
   ("ex", r"$C_{\alpha}$ 0.0035, $t_{100}$ 82 min", r"$t_p = 82 \times (1.5/0.0135)^2$ min = **1.93 yr** → $s_s = 3000 \times "
                                     r"0.0035 \times \log(100/1.93) = \boldsymbol{18\ \mathrm{mm}}$ · totals "
                                     "27 → 224 → **242 mm** (immediate 11 %, primary **81 %**, secondary 8 "
                                     "%)."),
 ),
]}

GEO[D["PILE"]] = {"code": "CE203", "title": "Foundations 5 · Piles to EC7: downdrag, load tests, tension (CE3116)", "sections": [
 sec("Q1 Downdrag on an end-bearing pile", (1, 2),
   ("eq", r"q_s = K_s\sigma'_v\tan\delta'\ (\text{sand}),\qquad q_s = c_u = 0.3\sigma'_v\ (\text{soft NC clay}),\qquad D_k = \sum q_sA_s"),
   ("ex", "250 mm pile through 4 m fill + 10 m soft clay to rock", r"Sand: $0.455 \times 36 \times 0.649 "
                                                                   r"\times 4 = \boldsymbol{42.5\ "
                                                                   r"\mathrm{kN}}$ · clay: $0.3 \times 107.8 "
                                                                   r"\times 10 = \boldsymbol{323.4\ "
                                                                   r"\mathrm{kN}}$ · $W_p$ 20.5 · design load "
                                                                   "C1 = $1.35(350 + 42.5 + 323.4 + 20.5) + "
                                                                   r"1.5 \times 150 = \boldsymbol{1219\ "
                                                                   r"\mathrm{kN}}$, C2 = 931 kN. Downdrag is a "
                                                                   "permanent action; on rock take the full "
                                                                   "(upper-bound) value."),
 ),
 sec("Q2 Resistance from static load tests (CFA Ø600, 11 m)", (3, 4),
   ("ex", "Two tests to 4000 kN, no failure", r"$R_{\mathrm{ck}} = \min(4000/\xi_1,\ 4000/\xi_2)$ with $\xi_1 "
                                              r"= 1.47$, $\xi_2 = 1.35$ = **2721 kN** (split 15 % base / 85 % "
                                              "shaft) · C1 $F = 1920 < 2721$ · C2: $2721/1.7 = "
                                              r"\boldsymbol{1601\ \mathrm{kN}} > F = 1460$ → OK (ratio 1.10 → "
                                              "C2 governs). Pile weight is excluded — the test already "
                                              "includes it."),
 ),
 sec("Q3 Resistance from ground parameters (same pile)", (5, 6),
   ("ex", r"Undrained ($q_b = 9c_u + \sigma_v$, $q_s = 0.4c_u$, model factor 1.35)", r"$R_{\mathrm{bk}} + "
                                                                                     r"R_{\mathrm{sk}} = 1179 "
                                                                                     "+ 1758$ → C1 $2938 > "
                                                                                     "2021$, C2 $1950 > 1535$ "
                                                                                     "✓."),
   ("ex", r"Drained ($N_q$ 60, $K_s$ 1.5, $\delta'$ 36°)", r"Subtract base uplift 25 kN · $R_{\mathrm{bk}} + "
                                                           r"R_{\mathrm{sk}} = 1386 + 1244$ → C2 "
                                                           r"$\boldsymbol{1815 > 1510}$ ✓ (C2 governs)."),
 ),
 sec("Q4–Q5 Tension piles under a flooded tank", (7, 9),
   ("ex", r"$U_k = 3872\ \mathrm{kN}$, $W_k = 3200\ \mathrm{kN}$", r"Net uplift C1 $1.35(U - W) = 907\ \mathrm{kN}$, C2 672 kN · from "
                                          r"test: $R_{\mathrm{tk}} = 2100/1.55 = 1355\ \mathrm{kN}$ (the slide "
                                          "divides 2000, giving 1290) → C2 $R = 1290/1.7 = 759 > 672$ ✓ · "
                                          r"from ground parameters: $q_t = 1.5 \times 97.5 \times \tan "
                                          r"36^\circ = 106\ \mathrm{kPa}$ → $R_{\mathrm{tk}}$ 1538 kN → C2 "
                                          "$1538/2.0 = 769 > 672$ ✓."),
   ("tip", "Netting U − W before factoring treats uplift and tank weight as one source. Factored separately "
           r"($1.35U - 1.0W = 2027\ \mathrm{kN}$) C1 would fail; EC7 UPL uses $\gamma_{\mathrm{dst}} = 1.0$ / "
           r"$\gamma_{\mathrm{stb}} = 0.9$ ($\approx 992\ \mathrm{kN}$). The two answers also use different "
           r"$\gamma_{s,t}$ (1.7 vs 2.0) — check the Singapore NA table."),
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
OUTLINE += [("L0", 7, 0.4, ["CE203-01"]), ("LS", 153, 0.5, ["CE203-01"]), ("LR", 15, 4.5, ["CE203-01"]),
            ("E2", 175, 5.5, ["CE203-02"]), ("E2a", 4, 5.6, ["CE203-02"]), ("E3", 63, 7.5, ["CE203-03"]),
            ("E4", 57, 8.5, ["CE203-03"]), ("E5", 99, 9.5, ["CE203-03", "CE203-04"]), ("E6", 33, 11.5, ["CE203-04"]),
            ("E7", 9, 12.5, ["CE203-02", "CE203-03"])]
TEXT_ONLY = set()   # docs over 10 MB on Drive: notes written from text only; original pages not stored locally

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
   ("md", "'Three rules': geometry, soil strength, **groundwater**. Dense sand/OC clay dilate (negative "
          r"$\Delta u$ when undrained → $s_u$ > drained); loose sand/NC clay contract (positive $\Delta u$ → "
          "$s_u$ < drained)."),
   ("md", r"**Embankment on soft clay**: FoS is lowest at end of construction (use $s_u$, $\phi_u = 0$) and "
          r"rises with consolidation. **Excavation in clay**: negative $\Delta u$ dissipates → FoS falls with "
          r"time → long-term drained ($c'$, $\phi'$) analysis governs."),
 ),
 sec("Getting strength parameters", (42, 47),
   ("eq", r"\left(\frac{s_u}{\sigma'_{v0}}\right)_{NC} = 0.11 + 0.0037\,PI\ (\text{Skempton}),\qquad \frac{s_u}{\sigma'_{v0}} = 0.22\,OCR^{0.8}\ (\text{Ladd})"),
   ("md", r"Tests: UU/unconfined → $s_u$ (short term); CU with pore pressure or CD → $c'$, $\phi'$; ring shear "
          "→ residual. Sands from $(N_1)_{60}$: very loose 29–32°, loose 32–35°, medium 35–37°, dense 37–40°, "
          "very dense 40–42°; silty sand −3°, gravelly sand +2°."),
 ),
 sec("Groundwater effects", (49, 57),
   ("eq", r"u = \gamma_wh_w\cos^2\alpha_w\ (\text{flowing, parallel seepage}),\qquad \tau_f = c' + (u_a - u_w)\tan\phi^b + (\sigma - u_a)\tan\phi'\ (\text{unsaturated})"),
   ("md", "Suction adds 'apparent cohesion' that is lost when rain saturates the slope. Ponded water at the toe is "
          "**stabilising**."),
 ),
 sec("Analysis approaches & factor of safety", (58, 65),
   ("md", r"Limit equilibrium (pre-defined surface, ULS only — this module), FEM ($\phi\text{–}c$ reduction, "
          r"gives displacement), limit analysis. Traditional lumped $\mathrm{FoS}$ = available strength / "
          "mobilised stress: **≥ 1.3 temporary, ≥ 1.5 permanent**. EC7 uses partial factors instead."),
 ),
 sec("EC7 for slopes (Singapore NA: DA1 only)", (66, 69),
   ("md", r"DA1-C1: A1 ($\gamma_G$ 1.35 unfav/1.0 fav, $\gamma_Q$ 1.5/0) + M1 (all 1.0). DA1-C2: A2 "
          r"($\gamma_G$ 1.0, $\gamma_Q$ 1.3) + M2 ($\tan\phi'$, $c'$ ÷ 1.25; $c_u$ ÷ 1.4). $\mathrm{FoS}$ = "
          "factored resisting / factored disturbing ≥ 1.0. In C1, soil upslope of the rotation centre "
          r"($\alpha > 0$) is unfavourable ×1.35; downslope ($\alpha < 0$) favourable ×1.0."),
 ),
 sec("Infinite slopes", (70, 81),
   ("eq", r"F = \frac{c' + \left[(1-m)\gamma + m(\gamma_{sat} - \gamma_w)\right]z\cos^2\beta\tan\phi'}{\left[(1-m)\gamma + m\gamma_{sat}\right]z\cos\beta\sin\beta}\quad(\text{GWT at } mz \text{ above the slip plane})"),
   ("md", r"Dry sand: $F = \tan\phi'/\tan\beta$ (independent of z). Saturated with parallel seepage: $F = "
          r"(\gamma'/\gamma_{\mathrm{sat}}) \tan\phi'/\tan\beta \approx \boldsymbol{\tfrac12}$ of dry. "
          r"Slip-plane u: parallel seepage $\gamma_w z\cos^2\beta$, horizontal seepage $\gamma_w z$, downward "
          "drainage 0. For drained infinite slopes **only DA1-C2** matters (C1 scales both sides)."),
 ),
 sec("Finite slopes: mass procedure (undrained, $c_u$)", (82, 91),
   ("eq", r"F = \frac{c_u\,r^2\theta}{\sum W_id_i}\ (\theta \text{ in rad}),\qquad \text{layered: } F = \frac{r^2\sum c_{ui}\theta_i}{\sum W_id_i}"),
   ("md", "Total-stress, short-term (end of construction) check on saturated clay, circular slip, moments "
          "about the centre. Split the mass into rectangles/triangles; blocks behind the centre ($d < 0$) "
          "resist."),
   ("eq", r"\text{tension crack: } d_c = \frac{2c_u}{\gamma},\qquad P_w = \tfrac12\gamma_wd_c^2\ (\text{acts at } d_c/3 \text{ above crack base; no strength along the crack})"),
   ("md", "EC7: **C1** — unfavourable permanent ×1.35, unfavourable variable ×1.5, favourable permanent ×1.0, "
          "favourable variable ignored; $c_u$ ÷ 1.0. **C2** — permanent ×1.0, unfavourable variable ×1.3, "
          "$c_u$ ÷ 1.4."),
   ("ex", r"Example: 12 m cut, $c_{\mathrm{uk}} = 60\ \mathrm{kPa}$, $\gamma = 20$", r"$M_D = 18\,163\ \mathrm{kNm/m}$, $M_R = 60 \times "
                                                      r"16.5^2 \times \pi/2 = 25\,659\ \mathrm{kNm/m}$ → **C1 "
                                                      r"$F = 25\,659/(1.35 \times 18\,163) = 1.05$**, **C2 $F "
                                                      r"= (25\,659/1.4)/18\,163 = 1.01$** — both OK."),
   ("ex", "Example: two clay layers $c_u$ 20/40 kPa, 20 kPa surcharge, water-filled crack",
          r"$d_c = 2 \times 20/19 = 2.1\ \mathrm{m}$, $P_w = 22.1\ \mathrm{kN}$; $M_D$: $W_1$ 2 777 (unfav), "
          r"$W_2$ −116 (fav), Q 438, $P_w$ 64; $M_R = 4\,518\ \mathrm{kNm}$. C1: $M_D = 1.35(2\,777 + 64) + "
          r"1.5(438) - 116 = 4\,376$ → $F = 1.03$. **C2: $M_D = 3\,294$, $M_R = 4\,518/1.4 = 3\,227$ → $F = "
          "0.98$ (not OK, governs).**"),
 ),
 sec("Taylor's chart", (92, 92),
   ("eq", r"N_s = \frac{c_u}{F\gamma H}\ \Rightarrow\ F = \frac{c_u}{N_s\gamma H}\quad(N_s \text{ from chart for slope angle } \beta \text{ and depth factor})"),
   ("md", r"Quick preliminary FoS for homogeneous clay ($\phi_u = 0$), e.g. temporary cuts."),
 ),
 sec("Method of slices: general", (93, 98),
   ("eq", r"F = \frac{\sum\left(c'l + N'\tan\phi'\right)}{\sum W\sin\alpha}\quad(\text{moments about the circle centre})"),
   ("md", "Effective-stress analysis handles layering and pore pressure. Search a grid of centres × radii for "
          "the minimum F. Methods differ in the interslice-force assumption: **Fellenius** (no E, X; moment "
          "only), **Bishop simplified** (E only, moment), **Janbu** (E only, force), **Spencer** (constant "
          r"X/E, both), **Morgenstern–Price** ($X = \lambda f(x)E$, both), **Sarma**. EC7: if horizontal "
          "equilibrium isn't checked, interslice forces must be horizontal → Bishop, Spencer, M-P acceptable. "
          "Bishop is within ~5% of M-P."),
 ),
 sec("Simplified Bishop (circular)", (99, 109),
   ("eq", r"F = \frac{1}{\sum W\sin\alpha}\sum\left[c'b + (W - ub)\tan\phi'\right]\frac{\sec\alpha}{1 + \tan\alpha\tan\phi'/F}"),
   ("steps", [r"Slice the mass; get W, $u$ ($= \gamma_w h_w$), $\alpha$ for each slice ($\alpha < 0$ downslope "
              "of the centre).",
              r"C1: ×1.35 on W $\sin\alpha$ for slices with $\alpha > 0$ (unfavourable), ×1.0 for $\alpha < "
              "0$; variable surcharge ×1.5.",
              r"C2: $c'$ ÷ 1.25 and $\tan\phi'$ ÷ 1.25 in the numerator and in $n_{\alpha}$; variable "
              "surcharge ×1.3.",
              "Extra moments $M_N$ from external loads/ponded water: add $M_N/R$ to the denominator.",
              r"Assume F (e.g. 1.0), compute $n_{\alpha}$, update F; iterate to convergence."]),
   ("ex", r"Example: residual clayey silt $c'_k = 8\ \mathrm{kPa}$, $\phi'_k = 26^\circ$, $\gamma = 18$", "Five slices on a given circle "
                                                                            "(companion spreadsheet): "
                                                                            "**DA1.C1 $F = 1.20$, DA1.C2 $F = "
                                                                            "1.39$**."),
 ),
 sec("Non-circular slips & Spencer", (110, 122),
   ("md", "Thin weak layers, shallow hard strata or geosynthetic interfaces give non-circular/composite "
          "surfaces — forcing circles **overestimates** F (James Bay dike: circular 1.45 vs non-circular "
          "Spencer/FEM ≈ 1.25)."),
   ("eq", r"X_i = \lambda E_i,\ \lambda = \tan\theta;\qquad N' = W\cos\alpha - ul - Q\sin(\alpha - \theta),\quad Q_i = Z_{i+1} - Z_i"),
   ("md", r"For trial $\theta$, march slice-by-slice from $Z_0 = 0$ and adjust F until $Z_N = 0$ (force "
          "equilibrium) and, separately, until the thrust-line lever arm $h_N = 0$ (moment equilibrium). Plot "
          r"$F_f(\theta)$ and $F_m(\theta)$: the intersection gives F and $\theta$. Fredlund & Krahn (1977) "
          r"example: $F \approx 1.37\text{–}1.41$."),
 ),
 sec("Practical details", (123, 125),
   ("md", "Slice boundaries at: slip entry/exit, slope breaks, layer and phreatic-line crossings, load edges. "
          "Hand calcs ~1% accuracy with modest slice numbers; software ≥ 30 slices, ≤ 3° subtended each. "
          r"Start centres 1–2H above the slope mid-point. Ponded water: point load $\gamma_w h_w b$ on each "
          r"slice (vertical; horizontal $\gamma_w h_w b \tan\beta$ on inclined faces) → moment $M_N$, add "
          "$M_N/R$ to the denominator."),
 ),
 sec("Signs of instability, stabilisation & monitoring", (126, 152),
   ("md", "**Signs**: crest/toe cracks, tilting fences/poles/trees, bulging toe, new seepage, broken pipes, jammed "
          "doors. **Reduce driving forces**: unload/regrade the crest, flatten, bench/terrace, lightweight fill. "
          "**Increase resistance**: surface drainage (cut-off/berm drains), sub-surface drainage (horizontal "
          "drains, wells, trench drains), toe buttress/berm, surface protection (turfing, shotcrete, erosion mats), "
          "reinforcement (soil nails, ground anchors, micropiles), retaining structures. LTA CDC specs apply in SG."),
   ("md", "**Monitoring**: inclinometers (lateral movement profile), piezometers/standpipes (pore pressure/GWT), "
          "settlement markers and surveying, tiltmeters, crack meters, rain gauges; trigger levels with response plans."),
 ),
]}

GEO[D["LR"]] = {"code": "CE203", "title": "Slopes 5 · Revision notes — slopes checklist (OAP)", "sections": [
 sec("Strength & safety factor", (2, 4),
   ("md", r"Natural/old slopes: pore pressures steady → **effective stress ($c'$, $\phi'$)**. New slopes in "
          r"clay: $\Delta u$ hard to predict → **total stress ($s_u$, $\phi_u = 0$)**, valid only for "
          "NC/lightly OC clay. GWT rise is detrimental; ponded water helps."),
 ),
 sec("Infinite slopes", (5, 5),
   ("md", "Check every layer interface; $c' = 0$ dry or fully saturated → F independent of z; partially "
          "saturated → F falls with depth. **Only DA1-C2** applies."),
 ),
 sec("Mass procedure & Taylor's chart (short term, $c_u$)", (6, 7),
   ("eq", r"F = \frac{c_u\,r^2\theta}{W d},\qquad F = \frac{c_u}{N_s\gamma H}\quad(N_s = f(\beta, D))"),
   ("md", "DA1-C2 ($c_u$ ÷ 1.4) normally governs. In C1 ideally split the mass into parts up/down-slope of "
          "the centre."),
 ),
 sec("Simplified Bishop — exam checklist", (8, 12),
   ("steps", ["Draw slices with numbers and key dimensions; boundaries at slope vertices, layer and GWT crossings.",
              r"W per slice from trapezoids (show $h_{\mathrm{ave}}$ per layer); compute $\alpha$ from "
              r"geometry ($\sin\alpha = x/R$).",
              r"$u = \gamma_w h_w$ (don't forget $\gamma_w$); one $n_{\alpha}$ per slice using the parameters "
              "at the slice base.",
              r"C2: factor strength first; C1: 1.35/1.0 on W $\sin\alpha$ by sign of $\alpha$; surcharge "
              "variable, ponded water permanent.",
              "Divide external-load and water moments by R; tension crack: no strength but weight remains.",
              "Start $F = 1.0$ and iterate."]),
 ),
 sec("Spencer & stabilisation", (13, 14),
   ("md", "Spencer satisfies force **and** moment equilibrium (parallel interslice forces) — good for "
          "non-circular slips; Morgenstern–Price is more general. Stabilisation: **benching** removes mass "
          "where it drives most; flattening spreads the cut; **buttressing** adds restoring weight at the toe "
          r"(less lever arm); **horizontal drains** lower the GWT → higher $\sigma'$."),
 ),
]}

GEO[D["E2"]] = {"code": "CE203", "title": "Earth pressure 0 · Lateral earth pressure theories (ERSS lecture)", "sections": [
 sec("At-rest pressure $K_0$", (6, 22),
   ("eq", r"K_{0,nc} = 1 - \sin\phi'\ (\text{Jaky}),\quad K_{nc} = 0.19 + 0.233\log PI\ (\text{Alpan}),\quad K_0 = K_{nc}\,OCR^{n},\ n = \sin\phi'\ \text{or}\ 0.54\times10^{-PI/281}"),
   ("md", r"$K_0$ always uses **effective** stresses. Singapore marine clay ($\phi'$ 22°, PI 55): "
          r"$K_{\mathrm{nc}} \approx 0.60\text{–}0.63$. Heavily OC clays can have $K_0 > 1$ (Gault clay 2–4 → "
          r"$\mathrm{OCR} \approx 20\text{–}180$)."),
 ),
 sec("Wall movement, active & passive states", (25, 35),
   ("md", r"Wall moves away → $\sigma'_h$ falls to $K_a\sigma'_v$ (small movement, ~0.1–0.5 % H); towards the "
          r"soil → rises to $K_p\sigma'_v$ (much larger movement, several %). Disturbance during construction "
          "changes $K_0$."),
 ),
 sec("Rankine active (smooth wall, lower-bound)", (36, 74),
   ("eq", r"\sigma'_a = K_a\sigma'_v - 2c'\sqrt{K_a},\quad K_a = \frac{1-\sin\phi'}{1+\sin\phi'} = \tan^2\!\left(45^\circ - \frac{\phi'}{2}\right);\qquad \phi = 0:\ \sigma_a = \sigma_v - 2s_u"),
   ("md", r"Slip planes at $\boldsymbol{45^\circ + \phi'/2}$ to the horizontal. Surcharge q adds $K_aq$ "
          r"uniformly. Tension depth $z_0 = 2c'/(\gamma\sqrt{K_a})$; ignore tension (cracks may fill with "
          r"water). Sloping backfill $\beta$ ($c' = 0$): $K_a = \cos\beta (\cos\beta - \sqrt{\cos^2 \beta - "
          r"\cos^2 \phi'})/(\cos\beta + \sqrt{\cos^2 \beta - \cos^2 \phi'})$."),
 ),
 sec("Rankine passive", (75, 116),
   ("eq", r"\sigma'_p = K_p\sigma'_v + 2c'\sqrt{K_p},\quad K_p = \frac{1+\sin\phi'}{1-\sin\phi'} = \frac{1}{K_a};\qquad \phi = 0:\ \sigma_p = \sigma_v + 2s_u"),
   ("md", r"Passive slip planes at $45^\circ - \phi'/2$. Rankine is a lower bound (safe) but can't handle wall "
          "friction."),
 ),
 sec("Coulomb wedge method (upper bound, wall friction)", (117, 161),
   ("md", "Trial planar wedges; maximise $P_a$ (minimise $P_p$) over the wedge angle; force polygons handle "
          r"c, $c_w$, $\delta$, sloping walls and backfills. Closed forms exist for cohesionless soil; $P_a$ "
          r"acts at $\delta$ to the wall normal → $P_{\mathrm{ah}} = P_a \sin(\alpha + \delta)$. Usually "
          r"$\delta \approx \tfrac23 \phi'$ for concrete."),
 ),
 sec("Curved surfaces: Caquot–Kérisel & EC7 Annex C", (162, 175),
   ("md", "Real passive surfaces are curved (log-spiral). Coulomb's plane **overestimates $K_p$ badly when "
          r"$\delta > \phi'/3$**; use Caquot–Kérisel tables or **EC7 Annex C** charts ($K_{\mathrm{ah}}$, "
          r"$K_{\mathrm{ph}}$ for $\delta = 0$, $\tfrac23 \phi'$, $\phi'$). Active is less sensitive."),
 ),
]}

GEO[D["E2a"]] = {"code": "CE203", "title": "Earth pressure 0a · Mohr circle & the pole method", "sections": [
 sec("Pole (origin of planes)", (1, 4),
   ("steps", ["Plot the stresses on two perpendicular planes and draw the circle.",
              "From the point for a known plane, draw a line parallel to that plane — it meets the circle at the **pole**.",
              "A line from the pole parallel to any other plane cuts the circle at the stresses on that plane.",
              r"Principal planes: lines from the pole to $\sigma_1$ and $\sigma_3$."]),
   ("ex", r"Quiz: $\sigma_x = 12$, $\sigma_y = 0$, $\tau = 6\ \mathrm{kPa}$", "Pole at (0, −6); stresses on "
                                                                              r"plane D–D′: $\sigma = 12$, "
                                                                              r"$\tau = 6\ \mathrm{kPa}$."),
 ),
]}

GEO[D["E3"]] = {"code": "CE203", "title": "Retaining 0 · Rigid retaining walls — stability checks (ERSS lecture)", "sections": [
 sec("Wall types & failure modes", (2, 11),
   ("md", "Gravity (mass), cantilever RC (L/T), counterfort/buttress, crib, gabion, reinforced soil. Failure modes: "
          "**sliding, overturning, bearing, deep-seated (overall) slip, seepage/piping**, plus structural failure."),
 ),
 sec("Sliding", (12, 22),
   ("eq", r"FoS_{sl} = \frac{N\tan\delta_b + c_bB + P_p}{P_a}\ \ge 1.5\ (\text{effective});\qquad \text{undrained base: } s_uB + P_p"),
   ("md", r"$\delta_b \approx \tfrac23 \phi'$ to $\phi'$. Passive in front is often ignored (it may be "
          "excavated or need large movement)."),
 ),
 sec("Overturning", (23, 26),
   ("eq", r"FoS_{OT} = \frac{\sum M_{resisting,\ toe}}{\sum M_{overturning,\ toe}}\ \ge 2"),
 ),
 sec("Bearing pressure & eccentricity", (27, 40),
   ("eq", r"e = \frac{B}{2} - \frac{\sum M_{net,toe}}{N},\qquad p_{max,min} = \frac{N}{B}\left(1 \pm \frac{6e}{B}\right)\ (e \le B/6),\qquad FoS_b = \frac{q_{ult}}{p_{max}}\ \ge 3"),
   ("md", r"Keep the resultant in the **middle third**; if $e > B/6$ the heel lifts: $p_{\mathrm{max}} = "
          "2N/(3(B/2 - e))$."),
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
   ("md", "**EQU** (rigid-body overturning), **STR** (structural), **GEO** (ground: sliding, bearing, "
          "overall), UPL (uplift), HYD (piping). Actions G/Q, favourable vs unfavourable; geometry tolerances "
          r"(over-dig $\Delta H = 10\,\%$ of retained height ≤ 0.5 m); limit earth pressures from Annex C."),
 ),
 sec("Partial factor sets", (23, 26),
   ("md", r"EQU: $\gamma_{\mathrm{G,dst}}$ 1.1, $\gamma_{\mathrm{G,stb}}$ 0.9, $\gamma_Q$ 1.5, $\gamma_{\phi'} "
          r"= \gamma_{c'} = 1.25$ (corrected slide), $\gamma_{\mathrm{cu}}$ 1.4. GEO C1: $\gamma_G$ 1.35/1.0, "
          r"$\gamma_Q$ 1.5, materials 1.0, R1 1.0. GEO C2: $\gamma_G$ 1.0, $\gamma_Q$ 1.3, $\tan\phi'$ and "
          "$c'$ ÷ 1.25, $c_u$ ÷ 1.4, R1 1.0."),
 ),
 sec("Worked example: EQU overturning, GEO sliding & bearing", (31, 57),
   ("md", r"Recompute $K_a$, $K_p$ with design $\phi'$ where required; factor the active thrust as "
          r"destabilising and the wall weight/passive as stabilising; check $E_d \le R_d$. See PS5 for the "
          "full numbers (sliding fails with a smooth base in both combinations)."),
 ),
]}

GEO[D["E5"]] = {"code": "CE203", "title": "Retaining 0b · Flexible walls: cantilever & anchored (ERSS lecture)", "sections": [
 sec("Flexible walls & methods", (1, 13),
   ("md", "Sheet piles, soldier piles, contiguous/secant piles, D-walls — stability from **embedment passive "
          "resistance**. Numerical (FEM/subgrade reaction) or classical limit-equilibrium methods."),
 ),
 sec("Cantilever wall: simplified method", (14, 45),
   ("steps", [r"Active $K_a\gamma(h + d_0)$ behind, passive $K_p\gamma d_0$ in front, ignore the toe reversal.",
              r"Moments about the toe C → $d_0$; $\boldsymbol{D = 1.2 d_0}$ to allow for the reaction below C.",
              r"$M_{\mathrm{max}}$ where shear = 0; $Z = M_{\mathrm{max}}/f_b$."]),
 ),
 sec("Cantilever wall: net-pressure (more realistic) method", (46, 65),
   ("eq", r"a = \frac{p_{a1}}{\gamma(K_p - K_a)},\qquad \text{solve horizontal + moment equilibrium for } Y \text{ and } z;\ D = a + Y"),
 ),
 sec("Cantilever to EC7 DA1", (66, 78),
   ("md", r"Apply partial factors to K (via design $\phi'$) and actions, solve simultaneously for embedment; "
          "C2 usually governs embedment, C1 the bending moment."),
 ),
 sec("Single-propped/anchored walls: free earth support", (79, 98),
   ("md", "Wall rotates about the prop; take moments about the tie for D, then horizontal equilibrium for T. "
          r"Traditional $\mathrm{FS} \approx 2$ on $K_p$ (or a mobilised trapezoid). Free-earth support "
          "over-predicts moments in flexible walls — **Rowe/Potts–Fourie** moment-reduction factors depend on "
          "wall flexibility."),
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
 sec("Basal heave: Terzaghi (shallow, $B > H_e$)", (17, 28),
   ("eq", r"F_b = \frac{5.7s_uB_1 + s_{u}H_e}{(\gamma H_e + q_s)B_1},\quad B_1 = \frac{B}{\sqrt2}\ (\text{or } D \text{ if a hard layer is shallower})"),
   ("md", r"Require $F_b \ge 1.5$. Treats heave as a bearing failure with side shear on the vertical plane."),
 ),
 sec("Basal heave: Bjerrum & Eide (deep excavations)", (29, 31),
   ("eq", r"F_b = \frac{s_uN_c}{\gamma H_e + q_s}\quad(N_c \text{ from Skempton: } f(H_e/B, B/L))"),
 ),
 sec("Course wrap-up", (32, 33),
   ("md", "Part 2 learning outcomes: $K_0/K_a/K_p$, Rankine–Coulomb–Caquot-Kérisel, rigid and flexible wall "
          "design to EC7, deep-excavation stability."),
 ),
]}

GEO[D["E7"]] = {"code": "CE203", "title": "Retaining 6a · Quiz key points (ERSS, second paper)", "sections": [
 sec("Concepts", (1, 3),
   ("md", "K uses effective stresses ✓ · buttress walls use thin webs ✓ · Rankine is not the earliest (Coulomb 1776 "
          "came first) · Coulomb's driving moment is usually smaller because its inclined thrust has a stabilising "
          "vertical component."),
   ("ex", r"Gault clay ($\phi'$ 22°, PI 45, $K_0$ 2–4) → OCR", r"Alpan: $K_{\mathrm{nc}}$ 0.575, n 0.373 → OCR "
                                                      r"**28–180** · Mayne–Kulhawy: $K_{\mathrm{nc}}$ 0.625, n "
                                                      "0.375 → OCR **22–142**."),
 ),
 sec(r"Gravity wall with 20° sloping backfill ($c'$ 25, $\phi'$ 20°)", (6, 9),
   ("ex", "Answers", r"$\beta = \phi'$ → $K_a = \cos\beta = 0.94$; $z_0 = 2.87\ \mathrm{m}$ → $P_a = 144.6$ "
                     r"(horizontal 135.8) kN · $K_p$ 2.04, $P_p = \boldsymbol{379.4\ \mathrm{kN}}$ · sliding "
                     r"**2.79** · overturning $822.5/187.2 = \boldsymbol{4.39}$ · $e = 0.04\ \mathrm{m}$, p "
                     r"187.5/148.5 kPa → bearing $450/187.5 = \boldsymbol{2.4 < 3}$ ✗ · flattening the "
                     "backfill drops $K_a$ to 0.49 → both FoS rise."),
   ("tip", r"The answer sheet's line '(2) $\sigma_p = 125.8\ \mathrm{kPa}$' is a copy-over from the other "
           "quiz; the base passive stress here is 181.5 kPa."),
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
   ("md", "Seismic refraction/reflection, surface waves (MASW) → stratigraphy and $V_s$ (small-strain "
          "stiffness); resistivity, EM, GPR → layering, cavities, water (clay low resistivity, rock high); "
          "crosshole/downhole/suspension logging in boreholes. Use them to position boreholes."),
 ),
 sec("Planning: depth, number, sampling", (25, 35),
   ("md", r"EC7-2 minimum depth below founding level: strip footing $z_a \ge \max(6\ \mathrm{m},\ 3b_F)$; raft "
          r"$z_a \ge 1.5b_B$; piles $z_a \ge \max(b_g,\ 3D_F,\ 5\ \mathrm{m})$ below the deepest toe (2 m if "
          "competent rock is proven). BCA/IES/ACES Advisory Note 1/03 (≥ 10 storeys): e.g. ~5 boreholes for "
          r"$1200\ \mathrm{m^2}$, 10 for $3000\ \mathrm{m^2}$, 26 for $7500\ \mathrm{m^2}$, placed at heavy "
          r"columns. Sample every $\boldsymbol{1.5\ \mathrm{m}}$ ($\le 3\ \mathrm{m}$) and at every change of "
          "stratum."),
 ),
 sec("SPT", (40, 54),
   ("eq", r"N_{60} = N\frac{E_r}{60}\lambda,\qquad (N_1)_{60} = N_{60}C_N,\quad C_N = \frac{200}{100 + \sigma'_v}\ (D_R 40\text{–}60\%),\ \frac{300}{200 + \sigma'_v}\ (60\text{–}80\%),\ \frac{170}{70 + \sigma'_v}\ (OC)\ \le 2"),
   ("md", r"63.5 kg hammer, 760 mm drop, 150 mm seating + 2 × 150 mm counted. Rod-length $\lambda$: 0.75 (3–4 "
          r"m), 0.85 (4–6 m), 0.95 (6–10 m), 1.0 (> 10 m). Clay: $s_u \approx 5N_{60}$ kPa (Stroud $f_1 "
          r"\approx 4.5\text{–}6$ by PI); no $C_N$ for clay. Disturbed sample only; unreliable in soft clay, "
          "silt and gravel."),
 ),
 sec("CPT / CPTu", (55, 72),
   ("eq", r"q_t = q_c + u_2(1 - a),\quad Q_t = \frac{q_t - \sigma_{v0}}{\sigma'_{v0}},\quad F_r = \frac{f_s}{q_t - \sigma_{v0}},\quad B_q = \frac{u_2 - u_0}{q_t - \sigma_{v0}},\quad s_u = \frac{q_t - \sigma_{v0}}{N_{kt}}"),
   ("md", "$I_c$ zones: < 1.31 gravelly/dense sand · 1.31–2.05 clean to silty sand · 2.05–2.60 sand mixtures "
          r"· 2.60–2.95 silt mixtures · 2.95–3.60 clay · > 3.60 organic. $N_{\mathrm{kt}}$ 15–20 (10 soft, 30 "
          r"fissured) — calibrate. $\sigma'_p \approx 0.33(q_t - \sigma_{v0})$. Sands: Baldi $D_R$, $\phi' = "
          r"17.6 + 11 \log[q_t/(100\sigma'_{v0})^{0.5}]$; $q_c$ $0\text{–}2.5 / 2.5\text{–}5 / 5\text{–}10 / "
          r"10\text{–}20 / > 20\ \mathrm{MPa}$ ≈ very loose → very dense. Fast, continuous, no sample."),
 ),
 sec("Pressuremeter & other tests", (73, 100),
   ("md", r"Ménard (pre-bored), self-boring, push-in. E from an unload–reload loop: $E = 2(1 + \nu)(V_c + "
          r"\bar{V})\Delta p/\Delta V$; limit pressure $p_L$ at $V = V_c + 2V_0$; $s_u = (p_L - p_0)/N_p$. "
          "Also vane shear ($s_u$ in soft clay), dilatometer, undisturbed sampling (thin-wall, Mazier), field "
          "permeability (Hvorslev rising/falling head), piezometers."),
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
   ("md", r"Specify relative compaction $\mathrm{RC} = \rho_{\mathrm{d,field}}/\rho_{\mathrm{d,max}}$ "
          "(typically ≥ 90–95 %) with a w window, or end-product $D_R$. Check by sand cone, nuclear gauge, "
          "core cutter, balloon; intelligent compaction monitoring for large fills."),
 ),
]}

GEO[D["F6"]] = {"code": "CE203", "title": "Foundations 0b · Revision: compaction & site investigation", "sections": [
 sec("Compaction checklist", (2, 6),
   ("steps", ["Plot both compaction curves with ZAV/$S_r$ lines.", r"Target $\rho_d$ from $D_R$, then "
                                                                 r"$\mathrm{RC}$ = target/MDD (aim 90–95 %).",
              "Allowable w range from the curve; pick rollers by soil type; lift thickness from $D_R$–depth "
              "chart.",
              "Truck trips: mass and volume capacity (with bulking) — the larger governs.", "Sand-cone results → adjust w or energy."]),
 ),
 sec("Site-investigation checklist", (7, 14),
   ("steps", [r"SPT: $E_r/60$, rod $\lambda$, $C_N$ only for sand → $D_R$ → $\phi'$ (±2–3° for "
              "gravelly/silty).",
              "CPTu: $q_t$, $Q_t$, $F_r$ → $I_c$ → soil type and k range; $s_u = (q_t - "
              r"\sigma_{v0})/N_{\mathrm{kt}}$.",
              "PMT: unload–reload modulus, $p_L$, $s_u = (p_L - p_0)/N_p$.",
              r"Hvorslev: T at $H/H_0 = 0.37$, $k = \pi r^2/(F T)$.", "Compare $s_u$ from all methods with lab UU."]),
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
   ("md", r"Inclination: $i_q = (1 - H/(V + A'c'\cot\phi'))^m$, $i_{\gamma} = (\ldots)^{m+1}$, $m = (2 + "
          "B'/L')/(1 + B'/L')$."),
 ),
 sec("Eccentric load & sliding", (54, 56),
   ("md", r"Keep e within B/6 for SLS; if $e/B > 1/3$ take special care (enlarge). Sliding: $H_d \le V'_d "
          r"\tan\delta_d$ (drained) or $A'c_u$ (undrained)."),
 ),
 sec("Worked examples (sand pad, stiff-clay pad)", (57, 79),
   ("md", "See the ULS tutorial page: C2 usually governs drained width; check undrained ($c_u/1.4$) and "
          "drained cases."),
 ),
]}

GEO[D["F32"]] = {"code": "CE203", "title": "Foundations 2 · Shallow foundations: settlement (SLS) — lecture notes", "sections": [
 sec("Components & limits", (3, 28),
   ("md", "$s = s_i$ (immediate, undrained distortion) + $s_c$ (consolidation) + $s_s$ (secondary). EC7 guide "
          "limits: **max settlement 50 mm, differential 20 mm, relative rotation 1/500**."),
 ),
 sec("Footings on sand — SPT methods", (29, 52),
   ("md", "Terzaghi–Peck / Peck–Hanson–Thornburn / Meyerhof charts give allowable pressure for 25 mm "
          r"settlement. Meyerhof: $s = 7.68C_dq_{\mathrm{net}}/(1.5N)$ for $B < 1.2\ \mathrm{m}$. Water-table "
          "and depth corrections ($C_w$, $C_N$)."),
 ),
 sec("Footings on sand — Schmertmann (CPT)", (53, 66),
   ("eq", r"s = C_1C_2\,q_{net}\sum\frac{I_z}{E}\Delta z,\quad C_1 = 1 - 0.5\frac{\sigma'_{v0}}{q_{net}},\quad C_2 = 1 + 0.2\log_{10}\frac{t}{0.1},\quad E \approx 2\text{–}4\,q_c"),
   ("md", "$I_z$ peaks ≈ 0.6 at B/2 below the base (square) and goes to zero at 2B (square) / 4B (strip). "
          "Usually conservative."),
 ),
 sec("Footings on clay — immediate & consolidation", (67, 84),
   ("eq", r"s_i = \mu_0\mu_1\frac{qB}{E_u};\qquad s_{oed} = \sum\frac{H}{1+e_0}\left[C_r\log\frac{\sigma'_c}{\sigma'_0} + C_c\log\frac{\sigma'_0 + \Delta\sigma}{\sigma'_c}\right],\quad s_c = \mu\,s_{oed}"),
   ("md", r"Janbu–Bjerrum–Kjaernsli $\mu_0$ (D/B), $\mu_1$ (H/B, L/B). Skempton–Bjerrum $\mu$ from "
          "pore-pressure A and H/B (≈ 0.6–1.0)."),
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
   ("steps", ["Design actions $F_{c,d}$: C1 (A1: 1.35G + 1.5Q) and C2 (A2: 1.0G + 1.3Q); downdrag is a "
              "permanent action.",
              r"Characteristic resistance from load tests ($\xi_1$, $\xi_2$), ground tests ($\xi_3$, $\xi_4$) "
              "or calculation (model factor).",
              r"Design resistance $R_{c,d} = R_{b,k}/\gamma_b + R_{s,k}/\gamma_s$ (R1 in C1, R4 in C2).", r"Check $F_{c,d} \le "
                                                                                       "R_{c,d}$ for both."]),
 ),
 sec("Characteristic values & model factor", (23, 42),
   ("md", "Characteristic ground value = cautious estimate of the mean governing the limit state. Calculated "
          r"resistance ÷ **model factor 1.55** (1.35 if verified by a load test). Load tests: $R_{\mathrm{ck}} "
          r"= \min(R_{\mathrm{mean}}/\xi_1,\ R_{\mathrm{min}}/\xi_2)$ (e.g. two tests: $\xi_1$ 1.47, $\xi_2$ "
          "1.35)."),
 ),
 sec("Resistance factors R4 (C2)", (43, 50),
   ("md", "Driven: base 1.7 (1.5 with SLS check), shaft 1.5 (1.3), total 1.7 (1.5), tension 2.0 (1.7). Bored: base "
          "2.0 (1.7), shaft 1.6 (1.4), total 2.0 (1.7), tension 2.0 (1.7). CFA between the two. R1 (C1) all 1.0."),
 ),
 sec("Calculating resistance", (51, 73),
   ("eq", r"\text{Clay: } q_b = 9c_u + \sigma_{v0},\ q_s = \alpha c_u;\qquad \text{Sand: } q_b = N_q\sigma'_{v0},\ q_s = K_s\sigma'_{v0}\tan\delta'"),
   ("md", r"$\alpha \approx 0.4\text{–}0.5$ for stiff clay; $K_s$ depends on installation (higher for driven); "
          "$N_q$ from Berezantsev. Subtract base uplift in drained analyses; include pile weight unless using "
          "load-test resistance."),
 ),
 sec("Downdrag example & SPT-based design", (77, 103),
   ("md", "Negative skin friction in settling soft clay adds to the load (full value if the toe is on rock). "
          "SPT design: cautious N in each stratum (ignore scattered fill values), $q_s$ and $q_b$ from N "
          "correlations, then factor and size the length."),
 ),
 sec("Tension piles & structural capacity", (104, 113),
   ("md", r"$R_{t,d} = R_{t,k}/\gamma_{s,t}$; buoyancy and uplift checked with UPL as well as GEO; check the "
          "pile section structurally (concrete crushing, reinforcement in tension)."),
 ),
]}

GEO[D["F21"]] = {"code": "CE203", "title": "Foundations 3a · Pile design from SPT/CPT (additional notes)", "sections": [
 sec("SPT and CPT correlations for piles", (1, 24),
   ("md", "Supplementary slides on SPT (energy, corrections, EPRI EL-6800 correlations) and CPT (profiles, "
          "direct CPT pile design). Use local correlations for shaft and base resistance and calibrate with load tests."),
 ),
]}
