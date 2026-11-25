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

# Practice pages (tutorial questions as q blocks) live in utils/study_notes_ce203q.py.



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

# E7 (quiz key points) is a practice page: see utils/study_notes_ce203q.py.


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
