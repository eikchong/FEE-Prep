"""Condensed study notes written from the CE1101 text notes (S1–S4 statics, M1–M5 mechanics of
materials) — in the same order as the notes, readable on the site without opening the PDFs.

Block types:
  ("md", text)          paragraph / bullets (markdown)
  ("eq", latex)         display equation
  ("steps", [..])       numbered procedure
  ("ex", title, text)   worked-example summary (results as given in the notes)
  ("tip", text)         exam tip / common trap
Section "pages" are the PDF pages of the source file (for 'open original').
"""
from __future__ import annotations

S1 = "CE102/CE1101_S1_Equilibrium_of_Particles.pdf"
S2 = "CE102/CE1101_S2_Equilibrium_of_Rigid_Bodies.pdf"
S3 = "CE102/CE1101_S3_Truss_Structures.pdf"
S4 = "CE102/CE1101_S4_Frame_and_Cable_Structures.pdf"
M1 = "CE102/CE1101_M1_Axial_Force_Members.pdf"
M2 = "CE102/CE1101_M2_Torsional_Members.pdf"
M3 = "CE102/CE1101_M3_Flexural_Members.pdf"
M4 = "CE102/CE1101_M4_Stress_Strain_Bending.pdf"
M5 = "CE102/CE1101_M5_Deflection_of_Beams.pdf"
T1 = "CE102/CE1101_T2L_Tutorial_1.pdf"
T2 = "CE102/CE1101_T2L_Tutorial_2.pdf"
T3 = "CE102/CE1101_T2L_Tutorial_3.pdf"
T4 = "CE102/CE1101_T2L_Tutorial_4.pdf"


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


STUDY: dict[str, dict] = {}

# ============================================================== S1 Statics of particles
STUDY[S1] = {"code": "CE102", "title": "S1 · Statics of particles", "sections": [
 sec("Force, transmissibility & free-body diagrams", (3, 17),
   ("md", "- A **force** is a vector (magnitude + direction). On a rigid body it tends to translate the body along "
          "its **line of action**.\n"
          "- **Principle of transmissibility:** a force may slide along its line of action without changing its "
          "external effect.\n"
          "- A **free-body diagram (FBD)** isolates the object completely from its surroundings and shows *every* "
          "force on it: **active** (applied loads, self-weight) and **passive** (support reactions, cable tensions, "
          "spring forces)."),
   ("steps", ["Draw the outlined shape of the body (idealised model).",
              "Isolate it from supports, cables and other bodies.",
              "Show all forces: loads, weight at the C.G., reactions in every restrained direction.",
              "Label known magnitudes/angles and dimensions."]),
   ("md", "**Internal forces** do not appear on an FBD unless the member is *cut* through."),
   ("ex", "Examples 1.1–1.5 (FBD practice)",
    "Trolley on a beam (symmetric → equal reactions, opposite on the beam); floating crane boom and mobile crane "
    "(frictionless pulley → cable tension unchanged round the pulley; brace is an axial member; pin gives Rx, Ry); "
    "cantilever staircase landing at E1; UTown walkway-cover frame."),
   ("tip", "Frictionless pulley ⇒ the same tension on both sides of the pulley."),
 ),
 sec("Resultant of forces: parallelogram law & Cartesian components", (18, 30),
   ("md", "**Parallelogram law** (two forces at a time) with the triangle rules:"),
   ("eq", r"R^2 = a^2 + b^2 - 2ab\cos\gamma \qquad \frac{a}{\sin\alpha} = \frac{b}{\sin\beta} = \frac{R}{\sin\gamma}"),
   ("md", r"$\gamma$ is the angle *inside the force triangle* opposite R (= 180° − angle between the two "
          "forces). For several forces, resolve into **Cartesian components** and add:"),
   ("eq", r"R_x = \sum F_x,\quad R_y = \sum F_y,\quad R = \sqrt{R_x^2 + R_y^2},\quad \theta = \tan^{-1}\frac{R_y}{R_x}"),
   ("ex", "Example 1.6", r"Two forces 300 N and 350 N combined by cosine then sine rule: $R = 175.0\ "
                         r"\mathrm{N}$; direction found from the triangle angle 89.13° → 30.87° from the "
                         "horizontal."),
   ("ex", "Example 1.8 (eyebolt, three ropes)", r"$F_1 = 80\ \mathrm{N}$, $F_2 = 120\ \mathrm{N}$, $F_3 = 50\ "
                                                r"\mathrm{N}$ resolved with a consistent sign convention → "
                                                r"$\sum F_x = 94.34\ \mathrm{N}$, $\sum F_y = 132.35\ "
                                                r"\mathrm{N}$ → $R = 162.5\ \mathrm{N}$ at 54.5° — the object "
                                                "moves in that direction."),
   ("ex", "Example 1.9 (trolley)", "Choose P so that the resultant of P and 1400 N is vertical: sketch the "
                                   r"parallelogram with R vertical, then sine rule gives P and R (or set $\sum "
                                   "F_x = 0$)."),
   ("tip", "Always state your sign convention before summing components."),
 ),
 sec("Equilibrium of a particle", (31, 43),
   ("md", "Concurrent forces → the body can be treated as a **particle**. It is in **equilibrium** when the "
          "resultant is zero:"),
   ("eq", r"\sum F_x = 0,\qquad \sum F_y = 0"),
   ("ex", "Example 1.10 (lifting a 3000 N beam with a 2-leg sling)", r"Symmetric legs: $2T \sin\theta = 3000$. "
                                                                     r"With $T_{\mathrm{max}} = 6500\ "
                                                                     r"\mathrm{N}$, $\sin\theta = "
                                                                     r"3000/13\,000$ → $\theta = 13.34^\circ$; "
                                                                     r"shortest total rope = $2 \times "
                                                                     r"1.5/\cos 13.34^\circ = 3.08\ "
                                                                     r"\mathrm{m}$. Smaller angles need less "
                                                                     "rope but give larger rope forces."),
   ("ex", "Example 1.11 (100 kg tank, 2 m rope over a pulley)", "Frictionless pulley ⇒ equal tension and "
                                                                r"equal angles. $2T \sin\theta = 981\ "
                                                                r"\mathrm{N}$. Points A–B (0.6 m apart): "
                                                                r"$\theta = 53.13^\circ$, $T = 613\ "
                                                                r"\mathrm{N}$; points C–D (0.3 m): $\theta = "
                                                                r"72.54^\circ$, $T = 514\ \mathrm{N}$ → use "
                                                                "C–D."),
   ("ex", "Cable ABC 2.5 m over a pulley, 25 kg", r"Geometry gives $\cos\theta = 1.5/2.5$ → $\theta = "
                                                  r"53.13^\circ$, $T = 245.3/(2 \sin 53.13^\circ) = 153.3\ "
                                                  r"\mathrm{N}$; then $x = 0.64\ \mathrm{m}$ from the triangle "
                                                  "geometry."),
 ),
]}

# ============================================================== S2 Rigid bodies
STUDY[S2] = {"code": "CE102", "title": "S2 · Equilibrium of rigid bodies", "sections": [
 sec("Moment of a force", (3, 7),
   ("md", "On a rigid body a force both **translates** and **rotates** the body. The rotational effect about a "
          "point is the **moment**:"),
   ("eq", r"M_A = F\,d \quad (d = \text{perpendicular distance from A to the line of action})"),
   ("md", "Equivalent ways: resolve F into components and add the moment of each (Varignon), choosing axes along "
          "and perpendicular to the member if convenient."),
   ("ex", "Example 2.1", "Moment of a 5 kN force about O, done twice — with x–y axes and with axes along the beam "
          "— giving the same answer."),
 ),
 sec("Couples & equivalent force–couple systems", (8, 16),
   ("md", "A **couple** = two equal, opposite, non-collinear parallel forces. Its moment **$M = Fd$ is the "
          "same about every point**. A force F acting at distance d from point A ≡ the same force through A "
          "**plus** a couple $M = Fd$."),
   ("eq", r"\mathbf{R} = \sum \mathbf{F}_i,\qquad M_A^R = \sum M_A(\mathbf{F}_i)"),
   ("ex", "Example 2.2 (traffic light pole)", "Two 20 kg lights replaced at the pole base by a vertical force "
          "392.4 N and a moment 784.8 Nm."),
   ("ex", "Example 2.3 (canopy beam)", "Forces 5 kN, 10 kN and a 6 kN sling → single resultant 10.3 kN, "
                                       r"located by equating moments about A: $x = 0.87\ \mathrm{m}$."),
 ),
 sec("Rigid-body equilibrium, supports, two- & three-force members", (17, 25),
   ("eq", r"\sum F_x = 0,\qquad \sum F_y = 0,\qquad \sum M_O = 0"),
   ("md", "**Supports:** a support exerts a **force** in each direction it prevents translation and a **moment** "
          "if it prevents rotation — roller 1 reaction, pin/hinge 2, fixed/clamped 3.\n\n"
          "- **Two-force member:** the two forces are equal, opposite and **collinear** (along the line joining the "
          "two points).\n"
          "- **Three-force member:** the three forces are **concurrent or parallel**."),
   ("ex", "Example 2.4 (crane boom with cable CD over a pulley)", r"Moments about the pin A → $T_{\mathrm{CD}} "
                                                                  r"= 93.8\ \mathrm{kN}$; force equations give "
                                                                  "A along/perpendicular to the boom (112.6 "
                                                                  "kN, 15.1 kN), i.e. 69.5 kN and 90.0 kN in "
                                                                  "x–y."),
   ("tip", "Take moments about the point where the most unknowns pass — each equation then gives one unknown."),
 ),
 sec("Case study: Leaning Tower of Pisa", (26, 34),
   ("md", "Weight 144 MN acting at the C.G. (27.1 m up a 58.2 m tower tilted 5.6°) is eccentric to the 19.6 m "
          r"base → overturning moment. Assume soil pressure $p = C + 0.625 r \cos\theta$ and integrate over "
          r"the circular base in polar coordinates: $\sum F_y = 0$ gives C, $\sum M_{\mathrm{EW}} = 0$ gives "
          r"the linear term. Maximum pressure at the southern edge ($r = R = 9.8\ \mathrm{m}$, $\theta = 0$)."),
 ),
]}

# ============================================================== S3 Trusses
STUDY[S3] = {"code": "CE102", "title": "S3 · Truss structures", "sections": [
 sec("Trusses, method of joints & special joints", (3, 9),
   ("md", "A truss is made of **straight two-force members** pinned at their ends, **loaded only at joints** → "
          "every member is in pure tension or compression.\n\n"
          "**Method of joints:** treat each joint as a **particle**; start at a joint with **≤ 2 unknown** member "
          "forces; assume tension (arrows away from the joint)."),
   ("eq", r"\sum F_x = 0,\qquad \sum F_y = 0 \quad \text{at each joint}"),
   ("md", "**Special joints** (spot them first — they save a lot of work):\n"
          "- Two collinear members + a third along the same line as a load P: the third carries P, collinear pair equal.\n"
          "- **Two non-collinear members, no load → both zero.**\n"
          "- **Three members, two collinear, no load → the third is zero**; the collinear pair are equal.\n"
          "- Two pairs of collinear members (X-joint), no load → each pair equal."),
 ),
 sec("Method of sections", (10, 19),
   ("md", "If a body is in equilibrium, any part of it is too. Make a clean **cut** through the members you want; "
          "the cut member forces become external forces on either part."),
   ("steps", ["Cut through **no more than 3** members with unknown forces (or, if more, all but one unknown must "
              "be concurrent or parallel).",
              "Choose the simpler side as the free body.",
              "Take **moments about the intersection of two unknowns** to get the third directly.",
              r"Use $\sum F$ in the remaining direction for the last one."]),
   ("ex", "Worked example (15 kN, 5 kN loads)", "Cut through CE, CD, BD; moments about D and C give the chord "
                                                r"forces, $\sum F_y$ gives the diagonal."),
 ),
 sec("Solution strategy for a whole truss", (20, 21),
   ("steps", ["FBD of the entire truss as one rigid body.",
              "Find the support reactions (as many as needed).",
              r"Inspect every joint — is it special? Mark zero-force members (e.g. $F_{\mathrm{BC}} = 0$).",
              "Use joints or sections for the required members, remembering which reactions are known."]),
 ),
 sec("Real-world truss failures & analysis", (22, 47),
   ("ex", "Example 3.1 — I-35W Mississippi bridge (2007)", "Causes: under-designed gusset plates, +20 % "
                                                           "self-weight from added overlay, construction "
                                                           "loads during repairs. Modelled as simply "
                                                           "supported spans; reactions 1114.3 kN and 1485.7 "
                                                           r"kN; by sections: $F_{\mathrm{DE}} = 2905\ "
                                                           r"\mathrm{kN}$ (T, most critical), $F_{\mathrm{KL}} "
                                                           r"= 2743\ \mathrm{kN}$ (C), $F_{\mathrm{GK}} = "
                                                           r"2118\ \mathrm{kN}$ (C) — using moment centres at "
                                                           "member intersections, including an imaginary "
                                                           "point R."),
   ("ex", "Skagit River bridge (2013)", "A tall truck load struck upper members. Single span by joints with "
                                        "equal loads P: bottom chord all tension, top chord all compression "
                                        "(truss acts like a beam); critical CD and DE ($4.80P$, T). Homework: "
                                        "add a horizontal impact force F — use superposition."),
   ("tip", "A truss under gravity behaves like a beam: top chord compression, bottom chord tension, largest chord "
           "forces near midspan, largest diagonals near the supports."),
 ),
 sec("Arch roof truss (non-parallel chords)", (48, 59),
   ("md", "Use symmetry for the reaction (15 kN), then a section through BC, CK, KL. With non-parallel chords, find "
          "the perpendicular lever arms from the geometry (chord 2 m, transverse 0.8 m, angles 22.5°/45°), take "
          "moments about C and K, and finish with force equilibrium. Homework 3.3–3.4: sections on further trusses."),
 ),
]}

# ============================================================== S4 Frames & cables
STUDY[S4] = {"code": "CE102", "title": "S4 · Frames, machines & cables", "sections": [
 sec("Trusses vs frames vs machines; how to solve", (3, 6),
   ("md", "| | Truss | Frames & machines |\n|---|---|---|\n| Members | all two-force | ≥ 1 multi-force member |\n"
          "| Loads | at joints only | anywhere |\n| Method | joints / sections | **dismembering** |\n\n"
          "**Frames** are rigid (one configuration) — overall equilibrium usually gives the reactions. "
          "**Machines** are non-rigid (they transmit and modify forces) — overall equilibrium is *not* enough."),
   ("steps", ["FBD of the entire frame/machine.",
              "Find support reactions as far as possible.",
              "Dismember: FBD of each member, with equal and opposite forces at shared pins.",
              "Identify two-force members first (assume tension, forces along the member).",
              "Each multi-force member gives 3 equations; take moments about a point where all but one unknown "
              "pass so each equation has one unknown."]),
 ),
 sec("Machines & frames — examples", (7, 25),
   ("ex", "Example 4.1 — backhoe dislodging a 5 kN slab", "Slab FBD (rough at K, smooth at J) → bucket force "
                                                          r"$P = 3.97\ \mathrm{kN}$; bucket GHJ → "
                                                          r"$F_{\mathrm{CG}} = 2.67\ \mathrm{kN}$; arm ABCH → "
                                                          r"$F_{\mathrm{AD}} = 11.45\ \mathrm{kN}$; continue "
                                                          "to EF and pin I."),
   ("ex", "Example 4.2 — billboard frames (240 kg, 3 frames)", "Share the load by tributary length: edge "
                                                               r"frame takes W/4 → $P = 294.3\ \mathrm{N}$ at "
                                                               "each hanger. Entire frame → links BG and DG; "
                                                               "frame ABCI → AF; frame CDE → EH. Avoid "
                                                               "solving pin forces you don't need; check with "
                                                               r"$\sum M$ about another point."),
 ),
 sec("Cables under concentrated loads", (26, 36),
   ("md", "Cables resist **tension only**. Between point loads each segment is straight (a two-force member). "
          "There are **4 support unknowns** but only 3 global equations → one extra piece of information is needed: "
          "the **position of one point**, the **tension or slope** somewhere, or the **total length**."),
   ("steps", [r"FBD of the whole cable; write one equation in the chosen primary unknowns (e.g. $\sum M_B = 0$ "
              "for $A_x$, $A_y$).",
              "Cut at the point with extra information and take moments about the cut (position known), or "
              r"use $\sum F$ with the known tension/slope.",
              "If only the length $L_c$ is known: cut at every load, one moment equation per cut, plus the "
              "length equation below.",
              "Then get each segment's slope and tension; the horizontal component is the same everywhere."]),
   ("eq", r"L_c = \sum_{i=1}^{n+1}\sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2}"),
   ("tip", "With no horizontal loads $T_x$ is constant, so the **steepest segment carries the largest "
           "tension**."),
 ),
 sec("Cable examples", (37, 45),
   ("ex", "Example 4.3 — crate hung from a cable via beam EF", "All points known → slopes AB 36.87°, BC "
                                                               "26.57°, CD 45° (steepest → critical, "
                                                               r"$T_{\mathrm{CD}} = 900\ \mathrm{N}$). "
                                                               "Equilibrium at C then B gives the hanger "
                                                               "forces; beam EF then gives the largest crate "
                                                               "weight and its position x."),
   ("ex", "Example 4.4 (homework)", r"Sag $y_C$ unknown → trial $T_{\mathrm{AB}}$ until the first segment "
                                    "reaches 700 N; find the largest mass of cylinder F."),
 ),
]}

# ============================================================== M1 Axial members
STUDY[M1] = {"code": "CE102", "title": "M1 · Introduction & axial force members", "sections": [
 sec("Statics vs mechanics of materials", (3, 5),
   ("md", "**Statics** gives forces from equilibrium (bodies assumed rigid). **Mechanics of materials** adds "
          "stress–force, strain–deformation and stress–strain relations so we can find deformation.\n\n- "
          r"Statically **determinate**: FBD + equilibrium → forces; then $\sigma\text{–}\varepsilon$ gives "
          "deformation.\n- Statically **indeterminate**: also need **compatibility** (geometry of the deformed "
          "structure)."),
 ),
 sec("Stress, strain & the stress–strain relationship", (6, 13),
   ("md", r"Stress at a point = limit of $\Delta F/\Delta A$: **normal** $\sigma$ (perpendicular) and "
          r"**shear** $\tau$ (in-plane). Sign: a stress on a positive face in a positive direction is positive "
          r"($\tau_{ij}$: i = face, j = direction)."),
   ("eq", r"\sigma_{avg} = \frac{P}{A} \qquad \tau_{avg} = \frac{V}{A} \qquad \text{double shear: } V = \frac{P}{2}"),
   ("eq", r"\varepsilon = \frac{\Delta L}{L} \qquad \gamma_{xy} = \text{change of the right angle (rad)}"),
   ("md", r"Mild steel $\sigma\text{–}\varepsilon$: linear elastic (slope **E**) → yield plateau → strain "
          "hardening → necking/failure."),
   ("eq", r"\varepsilon_{yy} = \varepsilon_{zz} = -\nu\,\varepsilon_{xx}\quad\text{(uniaxial)};\qquad "
          r"\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right]"),
   ("md", "The second form (**generalised Hooke's law**) superposes the strains from normal stresses in all three "
          "directions."),
 ),
 sec("Allowable stress & factor of safety; design examples", (14, 25),
   ("eq", r"n_s = \frac{P_{failure}}{P_{allowable}} = \frac{\sigma_{failure}}{\sigma_{allowable}} \geq 1"),
   ("ex", r"Example 1.1 — mountain-bike suspension pins ($P = 1800\ \mathrm{N}$, $\tau_{\mathrm{ult}} = 150\ "
          r"\mathrm{MPa}$)",
    r"Equilibrium of ABD → $F_{\mathrm{BC}} = 8858\ \mathrm{N}$. Pins in **double shear** carry V/2 each: "
    r"minimum $d_B = 8.67\ \mathrm{mm}$; pin D (resultant 7354.5 N) $d_D = 7.9\ \mathrm{mm}$."),
   ("ex", r"Example 1.2 — cast-in anchor ($a = 30\ \mathrm{mm}$, $h = 100\ \mathrm{mm}$, $d = 10\ "
          r"\mathrm{mm}$)",
    "Check each failure mode — concrete shear (cylinder surface), concrete cone tension + shear (truncated cone, "
    "45°), concrete tension, bolt tension — compute P for each; the **smallest P governs**."),
 ),
 sec("Deformation of axially loaded members", (26, 29),
   ("eq", r"\delta = \frac{PL}{EA} \qquad \delta = \sum_i \frac{P_iL_i}{E_iA_i} \qquad \delta = \int_0^L\frac{P(x)}{E\,A(x)}dx"),
   ("md", "Use internal axial force of each segment (cut and draw an FBD), not the applied loads."),
 ),
 sec("Statically indeterminate members & compatibility", (30, 31),
   ("eq", r"\text{degree of indeterminacy} = \text{no. of unknowns} - \text{no. of equilibrium equations}"),
   ("steps", ["Equilibrium equation(s).", r"Compatibility (e.g. total $\delta = 0$ between fixed ends).",
              r"Force–deformation $\delta = PL/EA$; solve together."]),
 ),
 sec("Truss deflections by geometry", (32, 35),
   ("md", r"Members elongate/shorten by $\delta = NL/EA$ and the joint must move so that all members stay "
          "connected."),
   ("ex", r"Example 1.3 ($P = 15\ \mathrm{kN}$, $A = 100\ \mathrm{mm^2}$, $E = 200\ \mathrm{GPa}$)", "Joint "
                                                                                                     "C: "
                                                                                                     r"$F_{\mathrm{AC}} "
                                                                                                     "= "
                                                                                                     r"9.375\ "
                                                                                                     r"\mathrm{kN}$ "
                                                                                                     "(C), "
                                                                                                     r"$F_{\mathrm{BC}}$ "
                                                                                                     "from "
                                                                                                     r"$\cos\theta "
                                                                                                     "= 4/5$, "
                                                                                                     r"$\sin\theta "
                                                                                                     "= 3/5$; "
                                                                                                     "member "
                                                                                                     "shortenings "
                                                                                                     "→ "
                                                                                                     "geometry "
                                                                                                     "of the "
                                                                                                     "displaced "
                                                                                                     "joint "
                                                                                                     "$C'$ → "
                                                                                                     r"$(\delta_C)_{\mathrm{vert}} "
                                                                                                     r"\approx "
                                                                                                     r"1.46\ "
                                                                                                     r"\mathrm{mm}$."),
 ),
 sec("Pile foundations; rigid bars on cables", (36, 48),
   ("md", "**Pile load test:** kentledge (concrete blocks) and hydraulic jacks check the calculated capacity on a few "
          "piles."),
   ("ex", r"Example 1.4 — 300 mm bored pile, $P = 2000\ \mathrm{kN}$, skin friction increasing linearly with "
          "depth",
    "Equilibrium → friction intensity 266.7 kN/m at the toe (22.2y kN/m); internal force P(y) varies → "
    r"$\delta = \int P(y)dy/AE = 5.28\ \mathrm{mm}$."),
   ("ex", "Example 1.6 — rigid bar ABD on cables BC and CD (6 kN/m)",
    "One moment equation + compatibility from the rotated rigid bar (similar triangles) and cable geometry "
    r"($\delta_{\mathrm{cable}} = \delta_{\mathrm{vertical}} \cos\theta$) → solve the two cable forces."),
 ),
]}

# ============================================================== M2 Torsion
STUDY[M2] = {"code": "CE102", "title": "M2 · Torsional members", "sections": [
 sec("Torsion formula & polar second moment", (3, 9),
   ("md", "Assumptions (circular shafts): axis stays straight, sections stay **plane and circular**, radial "
          r"lines stay straight, small rotations, linear elastic. Shear strain $\gamma = r\,d\theta/dx$ grows "
          "linearly with r."),
   ("eq", r"\tau = \frac{T\,r}{J},\qquad \tau_{max} = \frac{T\,c}{J}"),
   ("eq", r"J_{solid} = \frac{\pi R^4}{2} = \frac{\pi D^4}{32},\qquad J_{hollow} = \frac{\pi}{2}(R_2^4 - R_1^4) = \frac{\pi}{32}(D_2^4 - D_1^4)"),
 ),
 sec("Angle of twist; axial–torsion analogy; limitations", (10, 14),
   ("eq", r"\phi = \frac{TL}{GJ},\qquad \phi = \sum_i\frac{T_iL_i}{G_iJ_i},\qquad \phi = \int_0^L\frac{T(x)}{G\,J(x)}dx"),
   ("md", "| Axial | Torsion |\n|---|---|\n| $\\delta = FL/EA$ | $\\theta = TL/GJ$ |\n| $\\sigma = F/A$ | $\\tau = "
          "Tr/J$ |\n\nValid only for **circular** sections, linear elastic; ignores stress concentrations at "
          "abrupt changes. Sign: **right-hand rule** (thumb outward from the cut face = positive)."),
 ),
 sec("Statically determinate shafts; bolted couplings; distributed torque", (15, 26),
   ("ex", "Example 2.1 — 35 mm shaft, torques 30/25/40/65/80 Nm", "Internal torques by sections: "
                                                                  r"$T_{\mathrm{AB}} = -30$, $T_{\mathrm{BC}} "
                                                                  r"= -55$, $T_{\mathrm{CD}} = -15$, "
                                                                  r"$T_{\mathrm{DE}} = -80\ \mathrm{Nm}$. $J = "
                                                                  r"147\,324\ \mathrm{mm^4}$; $|T|_{\max} = "
                                                                  r"80\ \mathrm{Nm}$ → $\tau_{\mathrm{max}} "
                                                                  r"\approx 9.5\ \mathrm{MPa}$; $\phi_{A/E} = "
                                                                  r"\sum TL/(JG)$ over the four segments."),
   ("ex", r"Example 2.2 — bolted coupling (shaft $r = 30\ \mathrm{mm}$, bolts $d = 10\ \mathrm{mm}$ on $R = "
          r"75\ \mathrm{mm}$)",
    r"'Shaft fails before bolts': bolts in shear, $T = n \cdot (\tau \cdot \pi d^2/4) \cdot R$ vs shaft $T = "
    r"\tau \cdot J/c$ → $n \ge 7.2$ → **8 bolts**."),
   ("ex", "Example 2.3 — drill pipe with end torque $T_A$ and friction torque rising linearly to $t_0$",
    r"Equilibrium $T_B = T_A + t_0L/2$; internal torque varies along the pipe → $\phi$ by integration."),
 ),
 sec("Power transmission", (27, 31),
   ("eq", r"P = T\omega,\qquad \omega = \frac{2\pi N}{60}\ \text{rad/s},\qquad 1\ \text{hp} = 0.745\ \text{kW}"),
   ("ex", r"Example 2.4 — car drive shaft (thin tube, $d_o = 55\ \mathrm{mm}$, 180 hp at 1500 rpm)",
    r"$\omega = 157.1\ \mathrm{rad/s}$, $P = 134.1\ \mathrm{kW}$ → $T = 853.6\ \mathrm{Nm}$; "
    r"$\tau_{\mathrm{allow}}$ → $d_i \le 45.2\ \mathrm{mm}$ → minimum wall 4.9 mm; then check the twist limit."),
   ("ex", "Example 2.5 (homework)", r"Helicopter rotor shaft: 600 hp at 1200 rpm, $\tau_{\mathrm{allow}} = 55\ "
                                    r"\mathrm{MPa}$ (plus twist limit)."),
 ),
 sec("Statically indeterminate torsion", (32, 40),
   ("steps", ["Equilibrium: $T_A + T_B$ = applied torques.",
              "Compatibility: total twist between the fixed ends = 0 (or a known gap/slip).",
              r"Internal torques by sections; $\phi = \sum TL/GJ$; solve."]),
   ("ex", r"Example 2.6 — shower-curtain hanger ($d_o = 30\ \mathrm{mm}$, $t = 1.5\ \mathrm{mm}$, $G = 74\ "
          r"\mathrm{GPa}$, end A free to rotate 0.005 rad)",
    r"If A were loose the twist would exceed 0.005 rad, so A engages: $T_A = 8.43\ \mathrm{Nm}$, $T_B = 11.57\ "
    r"\mathrm{Nm}$; $\tau_{\mathrm{max}} = 15.6\ \mathrm{MPa}$ in segment CD (28.4 Nm)."),
   ("ex", "Example 2.7 — rubber annulus spring", r"Shear stress $\tau = T/(2\pi r^2h)$ decreases with radius; "
                                                 r"twist of the shaft by integrating $\gamma$ across the "
                                                 "annulus."),
 ),
]}

# ============================================================== M3 SFD / BMD
STUDY[M3] = {"code": "CE102", "title": "M3 · Flexural members (SFD & BMD)", "sections": [
 sec("Internal forces & sign convention", (3, 6),
   ("md", "A cut exposes an **axial force N, shear force V and bending moment M** (3 equilibrium equations). "
          "**Deformation sign convention:** +V turns the element clockwise; **+M sags** (compression on top); "
          "tension positive. SFD/BMD give the maxima needed for design."),
 ),
 sec("Load–shear–moment relations", (7, 11),
   ("eq", r"\frac{dV}{dx} = -q \qquad \frac{dM}{dx} = V \qquad V_B - V_A = -\int_A^B q\,dx \qquad M_B - M_A = \int_A^B V\,dx"),
   ("md", "- $q = 0$ → V constant, M linear. Uniform q → V linear, M parabolic.\n- **Point load P (down):** V "
          "drops by P; M has a kink (no jump).\n- **Applied couple $M_0$:** V unchanged; M jumps by $M_0$.\n- "
          "**M is maximum where $V = 0$** (or changes sign)."),
 ),
 sec("Sketching procedure", (12, 12),
   ("steps", ["FBD with loads, reactions and dimensions.", "Support reactions from equilibrium.",
              "Vertical construction lines at every load change.",
              "SFD segment by segment, left to right (start = left reaction).",
              "BMD from the SFD areas; check $M = 0$ at free/pinned ends."]),
 ),
 sec("Worked examples", (13, 36),
   ("ex", "Example 3.1 — gymnast P on a 5 m balance beam, 1.5 m from A", "$R_A = 0.7P$, $R_B = 0.3P$; "
                                                                         r"$M_{\mathrm{max}} = 1.05P$ under "
                                                                         "the load. Case 2: general position "
                                                                         r"x → $M_{\mathrm{max}} = P x(5 - "
                                                                         "x)/5$."),
   ("ex", "Example 3.2 — engine crane boom (5 kN)", "Hydraulic cylinder is a two-force member at 68.2° → its "
                                                    r"force from $\sum M_A$ ($\approx 17.5\ \mathrm{kN}$), pin "
                                                    "A from force equations; SFD/BMD of the boom."),
   ("ex", "Chair frame ABC–BD (person on the seat)", r"Replace by an equivalent FBD; $M = 495\ \mathrm{Nm}$ at "
                                                     "B."),
   ("ex", "Example 3.3 — RC pier cap (stringer loads 60/45 kN, self-weight 8 kN/m)", "Symmetric: reactions "
                                                                                     "163.5 kN each; $M = "
                                                                                     r"-136\ \mathrm{kNm}$ "
                                                                                     "over the supports and "
                                                                                     "−54.75 kNm at midspan "
                                                                                     "(hogging throughout)."),
   ("ex", "Spliced timber beam (8 kN/m)", r"$V = 0$ at 1.5 m from A → $M_{\mathrm{max}}(+) = 9\ \mathrm{kNm}$; "
                                          "$M = 0$ at 3 m → **best location for the splice**."),
   ("ex", "Ski on snow (0.8 kN, trapezoidal reaction)", r"Equilibrium → $w = 0.533\ \mathrm{kN/m}$, then "
                                                        "SFD/BMD."),
 ),
]}

# ============================================================== M4 Bending stress
STUDY[M4] = {"code": "CE102", "title": "M4 · Stress & strain due to bending", "sections": [
 sec("Curvature & bending strain", (3, 7),
   ("md", "Plane sections remain plane and normal to the axis; the beam bends into a circular arc of radius "
          r"$\rho$. Fibres above the neutral surface shorten, below lengthen (for +M)."),
   ("eq", r"\kappa = \frac{1}{\rho} = \frac{d\theta}{ds},\qquad \varepsilon_x = -\frac{y}{\rho} = -\kappa y"),
 ),
 sec("Normal stress, neutral axis & flexure formula", (8, 12),
   ("eq", r"\sigma_x = E\varepsilon_x = -E\kappa y"),
   ("md", r"$\sum F_x = 0$ (pure bending) ⇒ $\int y\,dA = 0$ ⇒ **neutral axis through the centroid** (linear "
          r"elastic). $\sum M = M$ gives the moment–curvature relation ($EI$ = flexural rigidity):"),
   ("eq", r"\kappa = \frac{M}{EI} \qquad \sigma_x = -\frac{My}{I} \qquad \sigma_{max} = \frac{M}{S},\ S = \frac{I}{c}"),
   ("tip", "+M: tension below the N.A., compression above. Under the same M the section with the larger S has "
           "the smaller stress."),
 ),
 sec("Centroid, second moment, parallel axis & superposition", (13, 16),
   ("eq", r"\bar{y} = \frac{\sum A_iy_i}{\sum A_i} \qquad I = \sum\left(I_{c,i} + A_id_i^2\right) \qquad I_{rect} = \frac{bh^3}{12}"),
   ("md", "About an axis of symmetry you can add/subtract rectangles directly (superposition), e.g. hollow box = "
          "outer − inner."),
 ),
 sec("Composite beams — transformed section", (17, 20),
   ("eq", r"n = \frac{E_2}{E_1},\quad b^* = nb \qquad \sigma_1 = -\frac{My}{I_t},\quad \sigma_2 = -n\frac{My}{I_t}"),
   ("md", "Transform material 2 into material 1 by scaling **widths only** (depth unchanged); find the N.A. "
          "and $I_t$ of the transformed section. Examples: timber + steel plate, concrete slab on steel beam, "
          "RC."),
 ),
 sec("Worked examples & applications", (21, 47),
   ("ex", "Example 4.1 — glued hollow timber box", "Top and bottom boards resist **85.9 %** of M (force resultant "
          "of the trapezoidal stress block × lever arm) → webs can be thinned."),
   ("ex", "Built-up 15 mm boards — two layouts for 150 kNm", "Compare section moduli; the larger S gives the lower "
          "stress."),
   ("ex", "Example 4.2 — diving board (80 kg at the tip)", r"$M_{\mathrm{max}} = 1962\ \mathrm{Nm}$ at support "
                                                           "B; T-shaped section: N.A. 11.4 mm from the top, "
                                                           r"$I = 5.1 \times 10^5\ \mathrm{mm^4}$ → $\sigma = "
                                                           r"Mc/I \approx 43.9\ \mathrm{MPa}$ at that face "
                                                           "(check the other face too)."),
   ("ex", "Example 4.3 — timber railway tie (70 kN rails, uniform ballast reaction 60.87 kN/m)", r"$M_{\mathrm{max}} "
                                                                                                 r"= 12.25\ "
                                                                                                 r"\mathrm{kNm}$ "
                                                                                                 "→ required "
                                                                                                 "thickness "
                                                                                                 r"$t = 98.4\ "
                                                                                                 r"\mathrm{mm}$ "
                                                                                                 "from "
                                                                                                 r"$\sigma_{\mathrm{allow}}$ "
                                                                                                 "and $S = "
                                                                                                 "bt^2/6$."),
   ("ex", r"Composite concrete slab on steel I-beam ($\sigma_c \le 15$, $\sigma_s \le 165\ \mathrm{MPa}$)", "Transform concrete into steel "
          "(b/n); N.A. 177 mm/323 mm; check which material reaches its limit first — the smaller moment governs."),
   ("md", "Applications: aluminium truss girders (I by parallel-axis of the chord tubes), **castellated beams** "
          "(cut and re-weld an I-beam → deeper, stiffer for the same steel)."),
 ),
]}

# ============================================================== M5 Deflection
STUDY[M5] = {"code": "CE102", "title": "M5 · Deflection of beams", "sections": [
 sec("Elastic curve & direct integration", (3, 13),
   ("eq", r"\kappa \approx \frac{d^2y}{dx^2} \quad\Rightarrow\quad EI\,y'' = M(x),\quad EI\,y''' = V,\quad EI\,y'''' = -q"),
   ("steps", ["Write M(x) for each segment (one function per segment).",
              r"Integrate twice: $EIy' = \int M\,dx + C_1$, $EIy = \iint M\,dx\,dx + C_1x + C_2$.",
              "Boundary conditions at supports ($y = 0$; $y' = 0$ at fixed ends).",
              "Continuity of y and $y'$ where segments meet."]),
   ("ex", "Example 5.1 — garden bench (two equal loads P on overhangs a, span b)",
    r"Three segments; BCs $y = 0$ at A and B, continuity of slope. Results: $\theta_A = Pab/(2EI)$, "
    r"$\delta_{\mathrm{mid}} = Pab^2/(8EI)$ (upward), $\delta_{\mathrm{end}} = Pa^2(2a + 3b)/(6EI)$."),
 ),
 sec("Superposition", (14, 14),
   ("md", "$EIy'' = M$ is **linear**, so deflections/slopes from separate load cases can be **added** (use "
          "standard tables)."),
 ),
 sec("Moment-area method", (15, 23),
   ("eq", r"\theta_{B/A} = \int_A^B\frac{M}{EI}dx \qquad t_{B/A} = \int_A^B\frac{M}{EI}\,\bar{x}_B\,dx"),
   ("md", "1st theorem: change in slope between A and B = **area** of the M/EI diagram. 2nd theorem: deviation of B "
          "from the tangent at A = **first moment of that area about B**. Angles +ve anticlockwise; B to the right "
          "of A. Draw M/EI **by parts** (one diagram per load) to use standard shapes:"),
   ("md", "| Shape | Area | Centroid from the zero end |\n|---|---|---|\n| rectangle | bh | b/2 |\n| triangle | "
          "bh/2 | 2b/3 |\n| parabolic spandrel ($y \\propto x^2$) | bh/3 | 3b/4 |\n| n-th degree spandrel | "
          "bh/(n+1) | (n+1)b/(n+2) |"),
 ),
 sec("Applications & examples", (24, 50),
   ("ex", r"Onshore pipeline span (stainless steel, $d_o = 330\ \mathrm{mm}$, $t = 6\ \mathrm{mm}$, $w = 1.4\ "
          r"\mathrm{kN/m}$)",
    "Treat one span as simply supported; M/EI diagram; $t_B/A$ and $t_C/A$ → midspan deflection; maximum span "
    "from the allowable deflection."),
   ("ex", "Example 5.3 — fibre-reinforced concrete beam (four-point bending)", "M/EI by parts; deflection at "
                                                                               "C from $t_D/A$ and $t_E/A$; "
                                                                               "cross-check with a second "
                                                                               "measured deflection."),
   ("ex", "Example 5.4 — RC retaining wall (cantilever, 8.5 kN/m triangular pressure, 6 m)", "Base shear 153 "
                                                                                             "kN, moment 306 "
                                                                                             "kNm; M/EI is "
                                                                                             "cubic → "
                                                                                             r"$\theta_A$ = "
                                                                                             r"area, $\delta_A "
                                                                                             "= t_A/B$."),
   ("ex", r"Roller position so that $\delta_C = \delta_D$ (overhang tip = max span deflection)", "Max in AB "
                                                                                                 "where slope "
                                                                                                 "= 0; equate "
                                                                                                 "the two "
                                                                                                 "expressions "
                                                                                                 "and solve "
                                                                                                 "the "
                                                                                                 "quadratic "
                                                                                                 "for a in "
                                                                                                 "terms of L."),
 ),
]}


# ============================================================== CE2155 (continuation of CE1101)
C0 = "CE102/CE2155_0_Introduction.pdf"
C1 = "CE102/CE2155_1_MoM_Revision.pdf"
C2 = "CE102/CE2155_2_Shear_Stress.pdf"
C3 = "CE102/CE2155_3_Combined_Loading.pdf"
C4 = "CE102/CE2155_4_Stress_Strain_Transformation.pdf"

STUDY[C0] = {"code": "CE102", "title": "CE2155 0 · Course map", "sections": [
 sec("Where structural mechanics fits", (1, 8),
   ("md", "CE2155 continues CE1101: **transverse shear stress, combined loading, 2-D stress & strain "
          "transformation, column buckling and failure criteria** (60 %), plus concrete & steel materials (40 "
          r"%). Static equilibrium in 3-D: 6 equations ($\sum F = 0$, $\sum M = 0$ in vector form); revise "
          "SFD/BMD of cantilevers and simply supported beams before starting."),
   ("eq", r"\sum\mathbf{F} = \mathbf{0},\qquad \sum\mathbf{M}_O = \mathbf{0}\quad(\text{6 scalar equations in 3-D})"),
 ),
]}

STUDY[C1] = {"code": "CE102", "title": "CE2155 1 · Mechanics of materials revision", "sections": [
 sec("Stress: normal, shear, 3-D state, complementary shear", (2, 5),
   ("md", r"Average normal stress $\sigma = P/A$ is accurate away from load points (**Saint-Venant's "
          r"principle**). Average shear in double shear $\tau = F/(2A)$. The 3-D state has $\sigma_x$, "
          r"$\sigma_y$, $\sigma_z$ and $\tau_{xy}$, $\tau_{yz}$, $\tau_{zx}$. **Complementary shear:** shear "
          "stresses on adjacent perpendicular faces are equal in magnitude and both point towards, or both "
          "away from, the common edge."),
   ("eq", r"\tau_{xy} = \tau_{yx},\quad \tau_{yz} = \tau_{zy},\quad \tau_{zx} = \tau_{xz}"),
 ),
 sec("Strain & stress–strain relations", (6, 15),
   ("md", "Normal strain = change in length per unit length; shear strain = change in the originally right "
          "angle (+ if the angle becomes smaller). Normal strains change volume, shear strains change shape. "
          "Engineering stress/strain use the original $A_0$ and $L_0$."),
   ("eq", r"\sigma = E\varepsilon,\qquad \nu = -\frac{\varepsilon_{lat}}{\varepsilon_{long}},\qquad \tau = G\gamma,\qquad G = \frac{E}{2(1+\nu)}"),
   ("ex", r"Example 1 — steel bar, 80 kN, $E = 200\ \mathrm{GPa}$, $\nu = 0.32$", r"$\sigma = P/A$ → $\varepsilon = \sigma/E$ → "
                                                                 r"$\delta = \varepsilon L$; lateral strain "
                                                                 r"$-\nu\varepsilon$ gives the change of the "
                                                                 "cross-section dimensions."),
 ),
 sec("Axial load, torsion & bending revision", (16, 26),
   ("eq", r"\delta = \int\frac{P(x)}{A(x)E}dx \qquad \tau = \frac{T\rho}{J},\ \phi = \frac{TL}{GJ} \qquad \sigma = -\frac{My}{I}"),
   ("md", "Torsion formulae are for **circular** sections only (non-circular sections warp). Euler–Bernoulli "
          "assumptions: plane sections stay plane and perpendicular to the axis, negligible in-plane distortion, "
          "axis length unchanged → linear strain → (elastic) linear stress."),
   ("ex", "Example 2 — I of a built-up section", r"Neutral axis by $\sum(A \cdot y)/\sum A$, then $I = "
                                                 r"\sum(bh^3/12 + Ad^2)$ — tabulate (an Excel layout is "
                                                 "shown)."),
   ("ex", "Example 3 — simply supported I-beam under UDL", r"$M_{\mathrm{max}} = 22.5\ \mathrm{kNm}$ at "
                                                           r"midspan; $\sigma_{\mathrm{max}} = Mc/I$ at the "
                                                           "extreme fibre; check also the web–flange junction "
                                                           r"($\sigma = My_B/I$)."),
 ),
 sec("SFD/BMD, elastic curve & moment–curvature", (27, 32),
   ("eq", r"\frac{dV}{dx} = w,\quad \frac{dM}{dx} = V \qquad \frac{1}{\rho} = \frac{M}{EI},\quad EI\frac{d^2v}{dx^2} = M"),
   ("md", "Signs here: upward load +, sagging moment +. Sketch the **elastic curve** to check the solution "
          "(supports, points of inflection where $M = 0$). Integrate with boundary conditions; discontinuity "
          "(Macaulay) functions handle partial UDLs and point loads."),
 ),
]}

STUDY[C2] = {"code": "CE102", "title": "CE2155 2 · Shear stress in beams", "sections": [
 sec("Transverse & longitudinal shear", (3, 6),
   ("md", "V produces transverse shear stress on the section; by complementary shear the same stress acts "
          "**longitudinally**. Three loose boards slide and each carries P/3; glued boards act as one deeper "
          "beam (much stiffer and stronger) — the glue carries the longitudinal shear. Shear exists because "
          "$V = dM/dx$: unequal M on the two faces of a slice must be balanced by shear on the cut."),
 ),
 sec("The shear formula", (7, 12),
   ("eq", r"\tau = \frac{VQ}{It},\qquad Q = \int_{A'}y\,dA = \bar{y}'A'"),
   ("md", r"$\boldsymbol{A'}$ = the part of the section beyond the level considered (the part 'held on' by the "
          r"shear); $\bar{y}'$ = distance from the N.A. to the centroid of $A'$; t = width at that level; I = "
          "whole section about the N.A."),
   ("eq", r"\text{Rectangle: } \tau = \frac{6V}{bh^3}\left(\frac{h^2}{4} - y^2\right),\qquad \tau_{max} = 1.5\frac{V}{bh}\ \text{at the N.A.}"),
   ("tip", r"The formula assumes $\tau$ uniform across the width t — poor for wide, shallow sections and at "
           "abrupt width changes."),
 ),
 sec("Examples: circular sections & glued T-beam", (13, 16),
   ("ex", r"Example 2 — solid shaft vs tube, $V = 4\ \mathrm{kN}$", r"Q of the semicircle above the diameter ($\bar{y} = "
                                                       r"4c/3\pi$); $\tau$ at mid-height of the solid shaft = "
                                                       "4V/3A, compared with V/A average; the tube has a "
                                                       "higher peak."),
   ("ex", "Example 3 — T-beam from two 150 × 30 mm boards", r"$V_{\mathrm{max}} = 19.5\ \mathrm{kN}$; $A'$ = "
                                                            r"top board, $t = 30\ \mathrm{mm}$ (glue width) → "
                                                            r"$\tau_{\mathrm{glue}} = VQ/(It) \approx 4.88\ "
                                                            r"\mathrm{MPa}$ (vs 2.17 MPa average)."),
 ),
 sec("Shear flow & fastener spacing", (17, 23),
   ("eq", r"q = \frac{VQ}{I}\ \ (\text{force per unit length}),\qquad s = \frac{F_{fastener}}{q_{per\ fastener\ line}}"),
   ("md", "Built-up beams need fasteners (glue, welds, bolts, nails, shear studs) to resist q. Split q "
          "between the number of fastener lines that hold $A'$ on."),
   ("ex", "T-beam (above)", r"$q = 146\ \mathrm{kN/m}$ — the glue must resist 146 kN per metre of beam."),
   ("ex", r"Example 4 — nailed box beam, $V = 80\ \mathrm{N}$, nail capacity 30 N", r"$I = 2295 \times 10^3\ "
                                                                                    r"\mathrm{mm^4}$. At B: $q "
                                                                                    r"= VQ/I = 1.18\ "
                                                                                    r"\mathrm{N/mm}$ shared by "
                                                                                    "two nail lines (0.59 "
                                                                                    "N/mm each) → $s_B "
                                                                                    r"\approx 51\ "
                                                                                    r"\mathrm{mm}$; at C: "
                                                                                    "0.353 N/mm per line → "
                                                                                    r"$s_C \approx 85\ "
                                                                                    r"\mathrm{mm}$."),
 ),
 sec("Thin-walled members", (24, 33),
   ("md", "In thin walls shear flow runs **along the wall** (normal component negligible). In an I-section it "
          "flows from the flange tips inward, down the web and out to the bottom tips. Use **centre-line "
          "dimensions** for I, Q."),
   ("eq", r"\text{Flange: } q = \frac{Vt\,d}{2I}x\ \ (\text{linear}),\qquad \text{Web: } q = \frac{Vt}{I}\left[\frac{db}{2} + \frac{1}{2}\left(\frac{d^2}{4} - y^2\right)\right]\ \ (\text{quadratic})"),
   ("md", "q varies **linearly** on segments perpendicular to V and **quadratically** on segments parallel/inclined "
          "to V; the web carries almost all of V, flange horizontal components cancel."),
   ("ex", r"Example 5 — thin-walled box, $V = 10\ \mathrm{kN}$", "$q_B = 0$ ($A' = 0$ at the corner point on the axis of "
                                                    "symmetry), $q_C$ and $q_D$ from Q of the shaded areas, "
                                                    "halved because two walls hold $A'$ on."),
 ),
]}

STUDY[C3] = {"code": "CE102", "title": "CE2155 3 · Combined loading", "sections": [
 sec("Superposition of P, T, M and V", (2, 3),
   ("md", "Valid while the material is linear elastic and geometry changes are small. Find the internal P, T, M, V "
          "**at the centroid of the section**, compute each stress at the point, then add."),
   ("eq", r"\sigma = \frac{P}{A} \pm \frac{M_zy}{I_z} \pm \frac{M_yz}{I_y} \qquad \tau = \frac{T\rho}{J} + \frac{VQ}{It}"),
 ),
 sec("2-D examples", (4, 7),
   ("ex", "Example 1 — member AB, point C at a top corner", r"Internal forces at C: $P = -16.45\ \mathrm{kN}$, "
                                                            r"$M = 32.89\ \mathrm{kNm}$ (sagging), $V = 21.93\ "
                                                            r"\mathrm{kN}$. At the top corner $\tau = 0$ ($Q = "
                                                            r"0$) and $\sigma = -P/A - Mc/I$ (compression)."),
   ("ex", "Example 2 — 40 kN at the corner of a block", "Move the force to the centroid: axial 40 kN + two moments; "
          "superpose the three stress planes → largest 875 kPa compression at corner C."),
 ),
 sec("3-D loading with vector mechanics", (8, 16),
   ("eq", r"\mathbf{M}_O = \mathbf{r}\times\mathbf{F} = \begin{vmatrix}\mathbf{i} & \mathbf{j} & \mathbf{k}\\ r_x & r_y & r_z\\ F_x & F_y & F_z\end{vmatrix}"),
   ("ex", "Example 3 — 7.5 mm-radius rod fixed at C, 500 N and 800 N loads",
    r"At section A: $P = 500\ \mathrm{N}$, $V = 800\ \mathrm{N}$, $T = 11\,200\ \mathrm{N\cdot cm}$, $M = "
    r"8000$ and 7000 N·cm. Point A on the neutral axis of the 8000 moment. Superpose: $\sigma = 2.83 + 211.3 = "
    r"214.1\ \mathrm{MPa}$, $\tau = 6.04 + 169 = 175.0\ \mathrm{MPa}$."),
   ("md", "**The big picture:** equilibrium → internal actions → stress formulae → state of stress → Mohr's "
          "circle → maximum stresses → failure criteria; and strain → deflection (serviceability), buckling "
          "(stability)."),
 ),
]}

STUDY[C4] = {"code": "CE102", "title": "CE2155 4 · Stress & strain transformation", "sections": [
 sec("Plane stress & sign convention", (2, 4),
   ("md", "Why a chalk in torsion breaks on a **45° helix**: the maximum *tensile* stress acts at 45° to the "
          r"axis. Plane stress keeps $\sigma_x$, $\sigma_y$, $\tau_{xy}$ (out-of-plane components zero). "
          r"$\tau_{xy}$ is positive on a +x face in +y (or −x face in −y); $\theta$ positive anticlockwise."),
 ),
 sec("Transformation equations", (5, 11),
   ("eq", r"\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos2\theta + \tau_{xy}\sin2\theta"),
   ("eq", r"\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta \qquad \sigma_{y'} = \sigma_x + \sigma_y - \sigma_{x'}"),
   ("md", r"Derived from equilibrium of a wedge cut at $\theta$ (forces = stress × area, not stresses)."),
   ("ex", "Example 1 — element rotated 30° clockwise", r"$\theta = -30^\circ$ in the equations; plotting "
                                                       r"$\sigma_{x'}$ against $\theta$ shows a max 54.6 MPa "
                                                       r"and min −84.6 MPa, and $\tau$ between ±69.6 MPa."),
 ),
 sec("Principal stresses & maximum in-plane shear", (12, 16),
   ("eq", r"\tan2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y} \qquad \sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}"),
   ("eq", r"\tau_{max,\,in\text{-}plane} = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2},\quad \sigma_{avg}\ \text{on those planes},\quad \theta_s = \theta_p \pm 45^\circ"),
   ("md", r"No shear on principal planes. Example 2 (bar in tension): $\sigma_1 = P/A$, $\sigma_2 = 0$; "
          r"$\tau_{\mathrm{max}} = P/2A$ on 45° planes — why ductile bars show 45° slip lines."),
 ),
 sec("Mohr's circle for plane stress", (17, 23),
   ("eq", r"(\sigma_{x'} - \sigma_{avg})^2 + \tau_{x'y'}^2 = R^2,\qquad R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}"),
   ("steps", [r"Centre C = ($\sigma_{\mathrm{avg}}$, 0).", r"Plot reference point A = ($\sigma_x$, $\tau_{xy}$) with **$\tau$ "
                                        "positive downward** (notes' convention).", "Radius $R = CA$.", r"A rotation $\theta$ of the element = $\boldsymbol{2\theta}$ "
                                                "on the circle, same sense.",
              r"$\sigma_1$, $\sigma_2$ where the circle meets the $\sigma$ axis; $\tau_{\mathrm{max}} = R$ at "
              "the top/bottom."]),
   ("ex", "Example 3", "Reference A(−8, −6); element rotated 30° anticlockwise → rotate CA by 60°."),
   ("ex", "Example 4 — point on a shaft", r"A(−12, −6): centre −6, $R = \sqrt{6^2 + 6^2} = 8.49$ → $\sigma_1 = "
                                          r"2.49$, $\sigma_2 = -14.49\ \mathrm{MPa}$."),
 ),
 sec("Absolute maximum shear stress", (24, 26),
   ("md", "Consider all three planes ($\\sigma_3 = 0$ in plane stress):\n- $\\sigma_1$, $\\sigma_2$ **same sign** "
          "→ $\\tau_{\\mathrm{abs,max}} = \\sigma_{\\mathrm{max}}/2$ (out-of-plane!).\n- $\\sigma_1$, $\\sigma_2$ "
          r"**opposite signs** → $\tau_{\mathrm{abs,max}} = (\sigma_1 - \sigma_2)/2$ (in-plane)."),
   ("ex", "Example 5 — thin pressure vessel", "Hoop and longitudinal stresses are principal and both tensile "
                                              r"→ $\tau_{\mathrm{abs,max}} = \sigma_{\mathrm{hoop}}/2$."),
 ),
 sec("Generalised Hooke's law, plane strain & strain rosettes", (27, 38),
   ("eq", r"\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right],\qquad \gamma_{xy} = \frac{\tau_{xy}}{G}"),
   ("md", r"**Plane strain** transforms exactly like plane stress with $\sigma$ → $\varepsilon$ and $\tau$ → "
          r"$\gamma/2$ (Mohr's circle: $\gamma/2$ positive downward)."),
   ("eq", r"\varepsilon_{x'} = \frac{\varepsilon_x + \varepsilon_y}{2} + \frac{\varepsilon_x - \varepsilon_y}{2}\cos2\theta + \frac{\gamma_{xy}}{2}\sin2\theta"),
   ("md", r"**Strain rosette:** three gauges a, b, c at known angles each give one equation $\varepsilon_i = "
          r"\varepsilon_x \cos^2 \theta_i + \varepsilon_y \sin^2 \theta_i + \gamma_{xy} \sin\theta_i "
          r"\cos\theta_i$ → solve for $\varepsilon_x$, $\varepsilon_y$, $\gamma_{xy}$ → Mohr's circle → "
          r"principal strains; then Hooke's law ($\sigma_3 = 0$) gives the principal stresses (Examples 7–8)."),
 ),
]}

C5 = "CE102/CE2155_5_Column_Buckling.pdf"
C6 = "CE102/CE2155_6_Material_Failure.pdf"

STUDY[C5] = {"code": "CE102", "title": "CE2155 5 · Column buckling", "sections": [
 sec("Stability & the critical load", (2, 5),
   ("md", "Equilibrium can be **stable** (returns when disturbed), **neutral** (stays displaced) or "
          "**unstable** (moves away). A slender compression member can fail by **buckling** (sudden, "
          r"geometric) before the material fails. The **critical load $P_{\mathrm{cr}}$** is the load at "
          "neutral equilibrium — find it from equilibrium in the *displaced* shape, not the original one."),
   ("ex", "Spring–bar model", r"Two rigid bars of length L/2 with a lateral spring k: $P\tan\theta$ balances "
                              r"the spring force $kL\theta/2$ for small $\theta$ → $P_{\mathrm{cr}} = kL/4$. "
                              r"Below $P_{\mathrm{cr}}$ stable, above unstable; $P_{\mathrm{cr}}$ is the "
                              "**bifurcation point**."),
 ),
 sec("Ideal pin-ended column — Euler load", (6, 11),
   ("md", "Ideal column: perfectly straight, load through the centroid, linear elastic. $M = -Pv$ gives "
          r"$EIv'' + Pv = 0$ (an eigenvalue problem); non-trivial solutions need $\sin(kL) = 0$."),
   ("eq", r"P_{cr} = \frac{\pi^2EI}{L^2}\ (n = 1),\qquad \text{higher modes } P_n = \frac{n^2\pi^2EI}{L^2}"),
   ("eq", r"\sigma_{cr} = \frac{P_{cr}}{A} = \frac{\pi^2E}{(L/r)^2},\qquad r = \sqrt{I/A},\quad L/r = \text{slenderness ratio}"),
   ("md", "Same end conditions both ways → buckles about the **weak axis** (least I). Euler is valid only "
          r"while $\sigma_{\mathrm{cr}} \le \sigma_Y$ (elastic buckling)."),
   ("ex", "Example 1 — W200×46 pin-ended column", r"Check $\sigma_{\mathrm{cr}}$ about y–y against $\sigma_Y = "
                                                  r"250\ \mathrm{MPa}$: $\sigma_{\mathrm{cr}} > \sigma_Y$, so "
                                                  r"the steel **yields first** and $P = \sigma_Y A$ governs."),
   ("tip", r"Always check both: $P_{\mathrm{cr}}$ (each axis, with its own effective length) and the squash "
           r"load $\sigma_Y A$ — the smallest governs."),
 ),
 sec("End conditions & effective length", (12, 16),
   ("eq", r"P_{cr} = \frac{\pi^2EI}{(KL)^2}"),
   ("md", "| Ends | K | $L_e$ |\n|---|---|---|\n| pinned–pinned | 1.0 | L |\n| fixed–free (cantilever) | 2.0 | "
          "2L |\n| fixed–pinned | 0.7 | 0.7L |\n| fixed–fixed | 0.5 | 0.5L |\n\n$L_e$ = distance between points "
          r"of zero moment (inflection points). Cantilever: $P_{\mathrm{cr}} = \pi^2EI/(4L^2)$."),
   ("ex", r"Example 2 — 8 m column fixed at both ends, braced at mid-height about y–y ($E = 200\ "
          r"\mathrm{GPa}$, $\sigma_Y = 410\ \mathrm{MPa}$)",
    r"x–x: $K = 0.5$, $L_e = 4\ \mathrm{m}$ → 1653 kN; y–y: fixed bottom, pinned at the brace, $L_e = 0.7 "
    r"\times 4 = 2.8\ \mathrm{m}$ → **461 kN**; yield 1255 kN → buckling about y–y governs at 461 kN."),
 ),
 sec("Eccentric load & the secant formula", (17, 24),
   ("md", "A load P at eccentricity e is equivalent to P plus a moment $Pe$. The column deflects from the "
          r"start; the deflection grows without bound as P → $P_{\mathrm{cr}}$, so yielding at mid-height "
          "usually governs first."),
   ("eq", r"v_{max} = e\left[\sec\left(\sqrt{\frac{P}{EI}}\frac{L}{2}\right) - 1\right]"),
   ("eq", r"\sigma_{max} = \frac{P}{A}\left[1 + \frac{ec}{r^2}\sec\left(\frac{L_e}{2r}\sqrt{\frac{P}{EA}}\right)\right]"),
   ("md", "$ec/r^2$ = **eccentricity ratio**; as it → 0 the curve tends to Euler. Solve for P by trial with "
          r"$\sigma_{\mathrm{max}} = \sigma_Y$."),
   ("ex", r"Example 3 — column fixed at the base, braced in x at the top, $e = 200\ \mathrm{mm}$ about x–x "
          r"($\sigma_Y = 250\ \mathrm{MPa}$)",
    r"(1) Weak-axis Euler with fixed–pinned $K = 0.7$; (2) strong axis: fixed–free ($K = 2$, $L_e = 8\ "
    r"\mathrm{m}$), secant formula with $c = 105\ \mathrm{mm}$, $r_x = 89.9\ \mathrm{mm}$, trial and error → "
    "**419 kN** governs."),
   ("tip", "Buckling is geometrically non-linear — superposition does not apply."),
 ),
]}

STUDY[C6] = {"code": "CE102", "title": "CE2155 6 · Material failure", "sections": [
 sec("Ductile materials & yield criteria", (2, 7),
   ("md", "Mild steel in tension: yield → necking → micro-voids coalesce → **cup-and-cone** fracture with "
          "~45° shear lips. Ductile failure starts with **yielding**, which is shear-controlled. In "
          r"multi-axial stress, compare with the uniaxial test via principal stresses $\sigma_1$, $\sigma_2$ "
          "(plane stress)."),
   ("md", r"**Tresca (maximum shear stress):** yielding when $\tau_{\mathrm{abs,max}} = \sigma_Y/2$."),
   ("eq", r"\text{same sign: } |\sigma_1| \le \sigma_Y,\ |\sigma_2| \le \sigma_Y \qquad \text{opposite signs: } |\sigma_1 - \sigma_2| \le \sigma_Y"),
   ("md", "**von Mises (maximum distortion energy):** yielding when the distortion strain-energy density reaches "
          "its uniaxial-yield value."),
   ("eq", r"\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2 \le \sigma_Y^2"),
   ("md", "Tresca's hexagon lies inside the von Mises ellipse → Tresca is more conservative."),
   ("ex", r"Example 1 — 5 mm-radius steel shaft, axial load + torque ($\sigma_Y = 360\ \mathrm{MPa}$)",
    r"$\sigma$ from P/A and $\tau = Tc/J$ at the surface → principal stresses of opposite sign. Tresca: "
    r"$|\sigma_1 - \sigma_2| > 360$ → **fails**; von Mises: < $360^2$ → **does not fail** — the stress point "
    "lies between the two criteria."),
 ),
 sec("Brittle materials", (8, 11),
   ("md", "Little or no yielding; sudden fracture governed by flaws. Weak in tension (cast iron, concrete: "
          r"$f_t \approx 10\,\%$ of $f_c$)."),
   ("md", "**Maximum normal stress (Rankine):** fracture when the largest principal stress reaches "
          r"$\sigma_{\mathrm{ult}}$."),
   ("eq", r"|\sigma_1| \le \sigma_{ult},\qquad |\sigma_2| \le \sigma_{ult}"),
   ("ex", r"Example 2 — cast-iron shaft, $T = 400\ \mathrm{Nm}$, $\sigma_{\mathrm{ult}} = 150\ \mathrm{MPa}$", "Pure "
                                                                                                               "shear "
                                                                                                               "→ "
                                                                                                               r"$\sigma_1 "
                                                                                                               "= "
                                                                                                               r"-\sigma_2 "
                                                                                                               "= "
                                                                                                               r"\tau_{\mathrm{max}} "
                                                                                                               "= "
                                                                                                               r"2T/(\pi "
                                                                                                               "c^3)$. "
                                                                                                               "Set "
                                                                                                               "equal "
                                                                                                               "to "
                                                                                                               "150 "
                                                                                                               "MPa "
                                                                                                               "→ "
                                                                                                               "$c "
                                                                                                               "= "
                                                                                                               r"11.9\ "
                                                                                                               r"\mathrm{mm}$."),
   ("md", "**Mohr's failure criterion** (different tension/compression strengths): draw the Mohr circles of "
          "the uniaxial tension, uniaxial compression and torsion tests; their envelope is the failure boundary. "
          "A stress state is safe if its circle lies inside the envelope."),
 ),
 sec("Cyclic loading & fatigue", (12, 14),
   ("md", "Unloading from the plastic range leaves a **permanent set**; reloading follows E up to a **higher "
          "yield point** (strain hardening) with reduced ductility.\n\n**Fatigue:** repeated loading can cause "
          "brittle fracture below the yield stress — the largest cause of failure of metal parts under dynamic "
          "load. The **S–N curve** gives cycles to failure N against stress amplitude S; the **endurance limit** is "
          "the amplitude below which no fatigue failure occurs (steels; not aluminium or concrete)."),
   ("md", "**Course map:** equilibrium → internal actions → stresses (strength check with failure criteria) → "
          "strains → deflection (serviceability) → buckling (stability)."),
 ),
]}



# ============================================================== CE101 — CE2155 materials part
_M = "CE101/CE2155_M{}.pdf"
MAT = {k: _M.format(k) for k in ["1_introduction", "2_Cement", "3_aggregate", "4_chemical_admixture",
                                  "5_fresh_concrete", "6_hardened_concrete", "7_mix_design",
                                  "8_creep_and_shrinkage", "9_durability", "10_steel_property",
                                  "11_steel_composition_and_structure", "12_wood",
                                  "CE2155_material_part_review_session_Spring_2020"]}

STUDY[MAT["1_introduction"]] = {"code": "CE101", "title": "Materials 1 · Introduction", "sections": [
 sec("Requirements & constituents", (3, 17),
   ("md", "Construction materials must satisfy **performance** (strength, shape-ability, volume stability, "
          "durability), **availability** (local, plentiful, cheap) and **sustainability** (low "
          r"energy/$\mathrm{CO_2}$, recyclable). Concrete = cement + water + fine & coarse aggregate + air (+ "
          "admixtures); paste → mortar → concrete. 60–90 % of construction material by volume is concrete; "
          r"cement carries most of its $\mathrm{CO_2}$."),
 ),
]}

STUDY[MAT["2_Cement"]] = {"code": "CE101", "title": "Materials 2 · Cement & SCMs", "sections": [
 sec("Portland cement: raw materials & clinker phases", (4, 6),
   ("md", r"$\approx \tfrac23$ limestone (CaO) + $\tfrac13$ clay/shale ($\mathrm{SiO_2}$, $\mathrm{Al_2O_3}$) "
          r"→ kiln → clinker, inter-ground with **gypsum**. Cement notation: $C = \mathrm{CaO}$, $S = "
          r"\mathrm{SiO_2}$, $A = \mathrm{Al_2O_3}$, $F = \mathrm{Fe_2O_3}$, $H = \mathrm{H_2O}$, $\bar{S} = "
          "\\mathrm{SO_3}$.\n\n| Phase | Hydrates | Role |\n|---|---|---|\n| $\\mathrm{C_3S}$ | fast, high heat | "
          "early strength (first 3–4 weeks) |\n| $\\mathrm{C_2S}$ | slow | later strength |\n| $\\mathrm{C_3A}$ | "
          "very fast (flash set) | controlled by gypsum |\n| $\\mathrm{C_4AF}$ | like $\\mathrm{C_3A}$, slower | "
          "little strength |\n\nCement manufacture ≈ **8 % of human $\\mathrm{CO_2}$** (fuel + $\\mathrm{CaCO_3}$ "
          r"→ CaO + $\mathrm{CO_2}$). Fineness is critical."),
 ),
 sec("Hydration products & stages", (7, 13),
   ("eq", r"2\mathrm{C_3S} + 11\mathrm{H} \rightarrow \mathrm{C_3S_2H_8} + 3\mathrm{CH} \qquad 2\mathrm{C_2S} + 9\mathrm{H} \rightarrow \mathrm{C_3S_2H_8} + \mathrm{CH}"),
   ("md", r"- **C-S-H**: 50–60 % of paste, huge surface area ($100\text{–}700\ \mathrm{m^2/g}$) → van der "
          "Waals bonding → **main source of strength**.\n- **CH** (portlandite): 20–25 %, weak, soluble → "
          "durability & strength problems.\n- **$\\mathrm{C_3A}$ + gypsum → ettringite (AFt)**; when gypsum is "
          r"used up, ettringite + $\mathrm{C_3A}$ → **monosulfate (AFm)**. Later external sulfate converts AFm "
          "back to AFt → expansion (sulfate attack).\n- Early rate: $\\boldsymbol{\\mathrm{C_3A} > \\mathrm{C_3S} "
          "> \\mathrm{C_4AF} > \\mathrm{C_2S}}$.\n- Heat-evolution stages: dissolution → induction (dormant) → "
          "acceleration (initial set) → deceleration (final set, hardening) → steady state."),
   ("tip", r"Ways to reduce early hydration rate: less $\mathrm{C_3A}/\mathrm{C_3S}$ (Type IV), coarser "
           "cement, SCM replacement, retarders, cooler concrete."),
 ),
 sec("ASTM cement types & microstructure", (14, 16),
   ("md", "| ASTM | Name | Use |\n|---|---|---|\n| I | OPC | general |\n| II | modified | moderate sulfate / heat |\n"
          "| III | rapid hardening | high early strength, cold weather, precast |\n| IV | low heat | mass concrete, hot "
          "weather |\n| V | sulfate resisting | sulfate soils/groundwater |\n\n"
          "Hardened paste porosity: **gel pores** (< 10 nm, part of C-S-H) and **capillary pores** (> 10 nm, "
          "leftover water space — governs permeability). **ITZ** around aggregate is the weak zone. "
          "EN equivalents: SS EN 197-1 CEM I–V, classes 32.5/42.5/52.5 N or R."),
 ),
 sec("Supplementary cementitious materials", (17, 27),
   ("eq", r"\mathrm{SiO_2 + Ca(OH)_2 + H_2O \rightarrow C\text{-}S\text{-}H}\quad\text{(pozzolanic reaction)}"),
   ("md", r"- **Fly ash** — Class F (bituminous coal, $\mathrm{SiO_2} + \mathrm{Al_2O_3} + \mathrm{Fe_2O_3} "
          r"\ge 70\,\%$, pozzolanic), Class C (lignite, ≥ 50 %, some self-cementing); spherical → better "
          "flow.\n- **Silica fume** — 10–100 nm, very reactive, sticky paste, early strength.\n- **GGBS** — "
          r"quenched blast-furnace slag (CaO 35–45 %, $\mathrm{SiO_2} 32\text{–}38\,\%$), latent hydraulic, "
          "activated by cement.\n- Rice husk ash, natural pozzolans (Pozzuoli volcanic ash).\n\n**Effects:** "
          "lower and slower heat; better cohesion; lower early but good long-term strength; less CH, finer "
          "pores → **better sulfate and chloride resistance**."),
 ),
]}

STUDY[MAT["3_aggregate"]] = {"code": "CE101", "title": "Materials 3 · Aggregate", "sections": [
 sec("Role & classification", (3, 5),
   ("md", "Inert granular filler occupying **65–75 %** of concrete volume; controls E, shrinkage, abrasion "
          "and cost. Coarse ≥ 4.75 mm, fine < 4.75 mm. By origin: igneous (excellent), sedimentary (~80 % of "
          r"supply), metamorphic; recycled/industrial. By density: lightweight to heavyweight ($> 2800\ "
          r"\mathrm{kg/m^3}$)."),
 ),
 sec("Grading, maximum size & fineness modulus", (6, 11),
   ("md", "Continuous grading minimises voids → less paste. **Maximum size** = smallest sieve through which all "
          "passes; nominal max = sieve retaining 5–10 %; limited by member size and bar spacing."),
   ("eq", r"FM = \frac{\sum\text{cumulative \% retained on standard sieves}}{100}"),
   ("md", r"Fine aggregate $\mathrm{FM} \approx 2.3\text{–}3.1$ (higher = coarser); used in mix design. Same "
          r"$\mathrm{FM}$ ≠ same grading."),
 ),
 sec("Moisture states, specific gravity, unit weight", (12, 17),
   ("md", "OD (oven-dry, 105 °C) → AD (air-dry) → **SSD** (pores full, surface dry) → wet."),
   ("eq", r"A = \frac{W_{SSD} - W_{OD}}{W_{OD}},\quad MC = \frac{W_{stock} - W_{OD}}{W_{OD}},\quad SM = MC - A"),
   ("md", "Absorption 1–2 % for normal aggregate; **effective absorption** = water needed AD → SSD. Bulk "
          r"specific gravity 2.5–2.8 (includes pores). Dry-rodded unit weight $1450\text{–}1750\ "
          r"\mathrm{kg/m^3}$ (needed for ACI coarse aggregate content)."),
 ),
]}

STUDY[MAT["4_chemical_admixture"]] = {"code": "CE101", "title": "Materials 4 · Chemical admixtures", "sections": [
 sec("Water reducers & superplasticisers", (3, 11),
   ("md", "Cement particles **flocculate** (opposite surface charges) and trap water. WRAs disperse them by "
          "**electrostatic repulsion** (adsorbed anionic molecules) and/or **steric hindrance** (long side "
          "chains, PCE superplasticisers) → trapped water released.\n\nUse them to (1) raise workability at the "
          "same w/c, (2) cut water → lower w/c → strength & durability, (3) cut cement at the same w/c and "
          "slump (heat, cost, $\\mathrm{CO_2}$).\n\nASTM C494: **A** water-reducing, **D** WR + retarding, **E** "
          "WR + accelerating, **F** high-range WR (superplasticiser), **G** HRWR + retarding."),
 ),
 sec("Air-entraining admixtures", (12, 16),
   ("md", "Freezing water expands ~10 %. AE surfactants (hydrophilic head, hydrophobic tail) stabilise micro "
          "air bubbles (> 1 µm) that give ice room and relieve pressure (cryo-suction draws water to the "
          r"voids). Side effects: better flow, **lower strength**. Third pore type after gel ($< 10\ "
          r"\mathrm{nm}$) and capillary (10 nm–1 µm)."),
 ),
 sec("Retarders & accelerators", (17, 23),
   ("md", "**Retarders** (sugars, phosphates, borates) slow dissolution of "
          r"$\mathrm{Ca^{2+}}/\mathrm{Al^{3+}}$ → longer plastic stage: hot weather, large pours (no cold "
          r"joints), long transport. **Accelerators**: $\mathrm{CaCl_2}$ is the most effective but **chlorides "
          "corrode reinforcement** — avoid in RC. Ready-mix concrete depends on admixtures.\n\nCanada in winter "
          "→ accelerator + air-entrainer; Singapore summer → retarder + water reducer."),
 ),
]}

STUDY[MAT["5_fresh_concrete"]] = {"code": "CE101", "title": "Materials 5 · Fresh concrete", "sections": [
 sec("Workability & the slump test", (3, 8),
   ("md", "Workability = work needed for full compaction **without segregation** (flowability + cohesiveness). "
          "Slump forms: **true**, **shear** (repeat), **collapse** (very wet/lean). Not for very low/high "
          "workability; EN 206 recommends slump for 10–210 mm."),
 ),
 sec("Segregation & bleeding", (9, 11),
   ("md", "**Segregation** = components separate (too wet or too dry, few fines, over-vibration) → cannot compact. "
          "**Bleeding** = water rises before set → weak top layer, voids under bars and stones. Control: grading, "
          "smaller max size, more/finer sand, SCMs, air entrainment, lower water."),
 ),
 sec("Factors affecting workability; slump loss", (12, 17),
   ("md", "Water content (main factor), aggregate amount/grading/shape (rounded better), temperature (↑T ↓"
          "workability), cement fineness, admixtures (fly ash ↑, silica fume ↓ without SP). **Slump loss** is "
          "roughly linear, fastest in the first 0.5–1 h (hydration, adsorption, evaporation) → start higher, use "
          "retarders/SP, avoid uncontrolled re-tempering water."),
 ),
 sec("Setting & plastic shrinkage", (18, 23),
   ("md", "Setting by penetration resistance (ASTM C403): **initial set 3.5 MPa, final set 27.6 MPa**. "
          "**Plastic shrinkage** cracking when evaporation rate > bleeding rate (hot, windy, dry) → moisten "
          "formwork, windbreaks, cool concrete, fog spray, curing membrane."),
 ),
]}

STUDY[MAT["6_hardened_concrete"]] = {"code": "CE101", "title": "Materials 6 · Hardened concrete", "sections": [
 sec("Structure & compressive behaviour", (3, 6),
   ("md", "Aggregate is linear-brittle, paste is non-linear; concrete is weaker than both because of the **ITZ** "
          "(20–40 µm, porous, oriented CH, ettringite, pre-existing micro-cracks). Micro-cracks stable to ~30 % of "
          "ultimate, then grow; unstable near failure. Test ≥ 3 specimens; reject one deviating > 15 % from the "
          "mean."),
 ),
 sec("Tensile strength tests", (7, 10),
   ("eq", r"f_{t,split} = \frac{2P}{\pi LD} \qquad R = \frac{PL}{bd^2}\ \ \text{(4-point, break in middle third)}"),
   ("md", r"Splitting/$f_c \approx 0.08\text{–}0.14$; flexural/$f_c \approx 0.11\text{–}0.23$; the ratio falls "
          "as strength rises. Splitting ≈ 5–12 % above direct tension."),
 ),
 sec("Factors affecting strength", (11, 14),
   ("md", r"**w/c** (porosity) dominates; in HSC the ITZ is no longer the weak link. Age: $f_{28}/f_7 \approx "
          r"1.3\text{–}1.7$. Higher curing temperature → faster gain but **lower ultimate** strength. "
          "Hydration stops below **80 % RH** — curing must supply moisture. Early hydration rate: Type III > "
          "I > II > V > IV."),
 ),
 sec("Modulus of elasticity", (15, 17),
   ("eq", r"E_c = 0.043\,w^{1.5}\sqrt{f'_c}\ \text{MPa (ACI 318; } w\text{ in kg/m}^3)"),
   ("md", r"Secant modulus (ASTM C469 at $40\,\% f'_c$; BS 1881 at 33 %). E rises with aggregate "
          "stiffness/volume, falls with porosity; **saturated specimens show ~15 % higher E** (opposite to "
          r"strength). Eurocode: $E_{\mathrm{cm}} = 22(f_{\mathrm{cm}}/10)^{0.3}\ \mathrm{GPa}$."),
 ),
]}

STUDY[MAT["7_mix_design"]] = {"code": "CE101", "title": "Materials 7 · Mix design (ACI 211)", "sections": [
 sec("Design aims & fundamentals", (3, 6),
   ("md", "Design for workability, strength, durability, economy, appearance. **Abrams' law** (empirical): "
          r"$f_c = A/B^{w/c}$ ($A \approx 96.5\ \mathrm{MPa}$, $B \approx 4$). Larger, well-graded aggregate → "
          "less water; more sand → more cohesive."),
 ),
 sec("Required average strength", (7, 9),
   ("eq", r"f'_{cr} = f'_c + 1.34s \qquad f'_{cr} = f'_c + 2.33s - 3.5\ \ (f'_c \le 35\ \text{MPa; use the larger})"),
   ("md", r"No data on s: $f'_c < 20$ → +7.0; 20–35 → +8.5; > 35 → $1.1f'_c + 5.0\ \mathrm{MPa}$ "
          r"(conservative). Eurocode/SS EN 206 practice uses target mean $\approx f_{\mathrm{ck}} + 1.64s$."),
 ),
 sec("The 10 steps", (10, 26),
   ("steps", ["Required information (gradings, FM, dry-rodded unit weight, specific gravities, absorption, member "
              "sizes, exposure).",
              "Choose slump for the member type.",
              r"Max aggregate size ≤ 1/5 narrowest form dimension, $\tfrac34$ clear bar spacing, $\tfrac34$ "
              r"cover, $\tfrac13$ slab depth.",
              "Mixing water & entrapped air from the table (larger aggregate → less water; more slump → more water).",
              "w/c = lower of strength (table) and durability (exposure) limits; Singapore (SS 544) — go one exposure "
              "class higher for the hot climate.",
              "Cement = water ÷ w/c (check minimum cement content).",
              "Coarse aggregate = (table volume for max size & sand FM) × dry-rodded unit weight.",
              "Fine aggregate by the mass method (unit weight − others) or the absolute-volume method.",
              "Adjust for aggregate moisture (SSD basis → as-batched).",
              "Trial batch and adjust."]),
   ("ex", "Moisture adjustment (lecture example, worked)",
    r"SSD mix: cement 400, water 200, CA 1050, FA $710\ \mathrm{kg/m^3}$. CA air-dry (absorption 1 %, "
    r"effective absorption 0.5 %) → batch $1050 \times 0.995 = 1044.8\ \mathrm{kg}$, +5.3 kg water; FA wet "
    r"(absorption 1.3 %, MC 4.5 % → surface moisture 3.2 %) → batch $710 \times 1.032 = 732.7\ \mathrm{kg}$, "
    r"−22.7 kg water → **water ≈ $182.5\ \mathrm{kg/m^3}$**."),
   ("tip", "cube ≈ 1.25 × cylinder strength (course assumption)."),
 ),
 sec("Trial-batch adjustments", (27, 29),
   ("md", "Strength low (workability OK) → lower w/c by adding cement at the same water. Slump low (strength "
          r"OK) → add water **and** cement (~$6\ \mathrm{kg/m^3}$ water ≈ +25 mm slump) or WRA/SP. Segregation "
          "→ more fine, less coarse."),
 ),
]}

STUDY[MAT["8_creep_and_shrinkage"]] = {"code": "CE101", "title": "Materials 8 · Creep & shrinkage", "sections": [
 sec("Autogenous & thermal shrinkage", (3, 7),
   ("md", "**Autogenous**: hydration products occupy less volume than reactants (≈ 15 % less for "
          r"$\mathrm{C_3S}$), early age, no moisture loss; significant at low w/c. **Thermal**: hydration heat "
          "then cooling under restraint (mass pours, walls cast on old bases)."),
   ("eq", r"\varepsilon = \alpha\Delta T = 10\times10^{-6}\times15 = 150\times10^{-6},\qquad \sigma = E\varepsilon = 20\,000\times150\times10^{-6} = 3\ \text{MPa}"),
   ("md", "3 MPa ≈ concrete tensile strength → cracking. Control: chilled water/ice/aggregate, place in the cool of "
          "the day, low cement / low-heat cement / SCMs, cooling pipes, insulation."),
 ),
 sec("Drying & plastic shrinkage", (8, 11),
   ("md", "Drying shrinkage from **capillary tension** in drying pores. More with more paste (less aggregate), "
          "softer aggregate, drier air, thinner members. Plastic shrinkage = while still plastic (evaporation > "
          "bleeding); drying shrinkage = after hardening."),
 ),
 sec("Creep", (12, 16),
   ("md", "Strain increasing with time under constant stress (re-organisation of C-S-H, moisture movement). "
          "Models: Maxwell (spring + dashpot in series), Kelvin-Voigt (parallel). More creep with more paste, "
          "softer aggregate, **higher stress**."),
   ("tip", "Check the figure on p. 15: the slide states *less* creep in drier air and in smaller sizes. The "
           r"usual textbook/EC2 trend (drying creep) is the opposite — creep coefficient $\phi$ rises at lower "
           "RH and smaller notional size $h_0$ (EC2 Annex B). Confirm which case the slide's data shows "
           "before relying on it."),
 ),
]}

STUDY[MAT["9_durability"]] = {"code": "CE101", "title": "Materials 9 · Durability", "sections": [
 sec("Physical attack: frost, fire, wear", (3, 9),
   ("md", "**Frost** (cracking, scaling) → air entrainment. **Fire**: 40–500 °C C-S-H dries, steam pressure "
          "(denser concrete spalls more); > 700 °C chemical decomposition → refractory (high-alumina) cement up "
          "to 1600 °C. **Abrasion/erosion** → low w/c and hard aggregate at the surface, avoid laitance."),
 ),
 sec("Chemical attack: sulfate & ASR", (10, 16),
   ("md", "**Sulfate**: sulfate enters → gypsum (≈ 120 % expansion) and AFm → ettringite (≈ 55 % solid volume "
          r"increase) → spalling. Mitigate: dense low-w/c concrete, SCMs/blended cement, low $\mathrm{C_3A}$, "
          "SRPC.\n\n**ASR** ('concrete cancer'): alkali pore solution ($\\mathrm{pH} > 13$) attacks reactive "
          r"silica → expansive gel, map cracking, no cure. Mitigate: SCMs ($\mathrm{pH} < 11$), non-reactive "
          "aggregate, low-alkali cement."),
 ),
 sec("Reinforcement corrosion & permeability", (17, 24),
   ("md", "Corrosion products expand → cracking, spalling, exposed bars. Mitigate: waterproof coatings, adequate "
          "**cover**, low-permeability concrete (low w/c, SCMs, curing), limit **chlorides** (catalyst) in "
          "materials and ingress.\n\n**Permeability** is the common thread: depends on porosity, capillary pore "
          "size and continuity — **w/c is the single most important factor**."),
 ),
]}

STUDY[MAT["10_steel_property"]] = {"code": "CE101", "title": "Materials 10 · Steel properties", "sections": [
 sec("Steel vs concrete; tensile behaviour", (3, 13),
   ("md", "Steel: ~200× concrete in tension, ~20× in compression, 3× the density, no volume change, ~20× the "
          r"price and ~30× the $\mathrm{CO_2}$ per unit. Tensile test: elastic → yield → strain hardening → "
          "necking → fracture. Unload/reload follows the same E (strain hardening raises the yield point). "
          r"Strength and ductility trade off; toughness = area under the $\sigma\text{–}\varepsilon$ curve."),
   ("eq", r"\sigma_T = \sigma(1 + \varepsilon),\qquad \varepsilon_T = \ln(1 + \varepsilon)\quad\text{(constant volume)}"),
 ),
]}

STUDY[MAT["11_steel_composition_and_structure"]] = {"code": "CE101", "title": "Materials 11 · Steel composition & structure", "sections": [
 sec("Metallic bonding & unit cells", (3, 4),
   ("md", "Non-directional metallic bonds let planes slip (ductility); C-S-H's covalent bonds break "
          "instead.\n\n| Cell | Atoms | a vs r | Packing |\n|---|---|---|---|\n| simple cubic | 1 | $a = 2r$ | "
          "0.52 |\n| BCC | 2 | $\\sqrt{3}a = 4r$ | 0.68 |\n| FCC | 4 | $\\sqrt{2}a = 4r$ | 0.74 |"),
 ),
 sec("Phase diagrams & the lever rule", (5, 8),
   ("eq", r"\frac{M_{solid}}{M_{liquid}} = \frac{w_0 - w_L}{w_S - w_0}"),
   ("ex", "Cu–50 % Ni at 1300 °C", r"Liquid 46 % Ni, solid $\alpha$ 58 % Ni → $M_L/M_S = (58 - 50)/(50 - 46) = "
                                   r"2{:}1$ → $\tfrac23$ liquid, $\tfrac13$ solid."),
 ),
 sec("Fe–C diagram: ferrite, austenite, cementite, pearlite", (9, 17),
   ("md", r"$\delta$-iron (BCC) → 1401 °C → **austenite $\gamma$** (FCC) → 908 °C → **ferrite $\alpha$** "
          r"(BCC). C solubility: $\gamma$ 2.0 %, $\delta$ 0.10 %, $\alpha$ 0.025 %. **Cementite "
          r"$\mathrm{Fe_3C}$** (6.7 % C) is very hard and brittle. Eutectoid at **727 °C, 0.8 % C**: $\gamma$ "
          "→ $\\alpha + \\mathrm{Fe_3C}$ as thin plates = **pearlite**.\n\n- Hypo-eutectoid (< 0.8 % C, "
          "structural steels): pro-eutectoid ferrite + pearlite.\n- Eutectoid (0.8 %): pearlite.\n- "
          r"Hyper-eutectoid ($> 0.8\,\%$): pro-eutectoid $\mathrm{Fe_3C}$ + pearlite."),
   ("ex", "Eutectoid steel just below 727 °C", r"$M_{\alpha}/M_{\mathrm{Fe_3C}} = (6.7 - 0.8)/(0.8 - 0.025) = "
                                               "7.6$ → ≈ 88 % ferrite, 12 % cementite."),
 ),
 sec("Welding & weldability", (18, 19),
   ("md", "Metal next to the weld exceeds 727 °C (austenite); on fast cooling the HAZ can form **martensite** "
          "(brittle). Weldability decreases as carbon and alloy content rise (→ carbon equivalent, preheat)."),
 ),
]}

STUDY[MAT["12_wood"]] = {"code": "CE101", "title": "Materials 12 · Wood (not examined in CE2155)", "sections": [
 sec("Structure, moisture & strength", (3, 14),
   ("md", "Low-carbon material (mass-timber towers). Sapwood/heartwood; earlywood (large thin cells) vs latewood "
          "(dense, dominates shrinkage). Directions: longitudinal (strongest), radial, tangential. Softwoods = "
          "tracheids; hardwoods = fibres + vessels. Moisture as % of oven-dry mass; bound vs free water. **Fibre "
          "saturation point ≈ 25–30 %**: above it strength is constant; below it strength rises and the wood "
          "shrinks as it dries. Seasoning: air or kiln."),
   ("tip", "Linked to CE101-18 (mass engineered timber, CLT, glulam) — tested in FEE 2019 Part 1."),
 ),
]}

STUDY[MAT["CE2155_material_part_review_session_Spring_2020"]] = {"code": "CE101", "title": "Materials review — checklist for the paper", "sections": [
 sec("What you must be able to do", (2, 14),
   ("md", "- **Cement:** raw materials, clinker phases, hydration products (C-S-H, CH, ettringite, monosulfate — "
          "no chemical formulae needed), ASTM Types I–V, ITZ & porosity.\n"
          "- **SCMs:** pozzolanic reaction; fly ash F/C, slag, silica fume, RHA — reactivity, fineness, effect on "
          "workability, heat, strength, durability.\n"
          "- **Aggregate:** specific gravity vs unit weight, classification, FM, absorption, total/surface moisture.\n"
          "- **Admixtures:** WRA/SP, AE, retarder, accelerator — mechanism, effects, applications.\n"
          "- **Fresh concrete:** workability, slump, segregation & bleeding, slump loss, plastic vs drying shrinkage.\n"
          "- **Hardened:** factors on strength (w/c, age, curing, humidity, cement, aggregate) and on E.\n"
          "- **Mix design:** be able to do the **ACI 10-step design**.\n"
          "- **Dimensional stability:** origin, factors and mitigation of each shrinkage type and creep.\n"
          "- **Durability:** mechanisms & mitigation; w/c, cement content, permeability.\n"
          "- **Steel:** tensile test, strength vs ductility, true vs engineering stress; unit cells, lever rule, "
          "Fe–C diagram (ferrite, cementite, pearlite).\n- Wood: not examined."),
 ),
]}

# CE101 materials tutorials (q blocks, one page per sheet) live in utils/study_notes_ce101q.py.

# ============================================================== CE104 Soil mechanics (CE2112)
G1 = "CE104/CE104_1_Groundwater_Permeability_Seepage.pdf"
G2 = "CE104/CE104_2_Shear_Strength.pdf"

STUDY[G1] = {"code": "CE104", "title": "Soil 8 · Groundwater, permeability & seepage", "sections": [
 sec("Groundwater conditions & pore pressure", (3, 17),
   ("eq", r"\sigma' = \sigma - u,\qquad u = \gamma_w z_w\ \text{(hydrostatic)}"),
   ("md", "Effective stress controls soil **strength and compressibility**; most geotechnical problems "
          "involve groundwater. A **standpipe piezometer** (20–25 mm pipe, porous tip) reads the "
          "pore-pressure head.\n\n- **Hydrostatic**: u increases at $\\gamma_w$ per metre.\n- **Artesian** "
          "(aquifer under clay recharged from higher ground): head above ground level; u in the clay rises "
          "*faster* than hydrostatic — beware **base heave** when excavating into the clay.\n- "
          "**Underdrained** (aquifer pumped down): steady *downward* seepage, u rises *slower* than "
          "hydrostatic."),
 ),
 sec("Heads & Darcy's law", (18, 26),
   ("eq", r"h = z + \frac{u}{\gamma_w} + \frac{v^2}{2g}\ \ (\text{velocity head negligible in soil})"),
   ("eq", r"q = Aki = Ak\frac{\Delta h}{L},\qquad v = ki\ \ (\text{superficial velocity over the whole area})"),
   ("md", "Water flows from high to low **total** head; laminar flow. Work problems with a table of elevation, "
          "pressure and total head at each point, choosing any datum."),
 ),
 sec("Permeability", (27, 32),
   ("eq", r"\text{constant head: } k = \frac{QL}{Aht}\qquad \text{falling head: } k = \frac{aL}{At}\ln\frac{h_1}{h_2}"),
   ("md", "| Soil | k (cm/s) | Drainage |\n|---|---|---|\n| clean gravel | $10^1\\text{–}10^2$ | good |\n| clean "
          "sand / sand–gravel | $10^{-1}\\text{–}10^{-4}$ | good |\n| very fine sand, silt | "
          "$10^{-5}\\text{–}10^{-6}$ | poor |\n| clay | < $10^{-7}$ | practically impervious |\n\nConstant head "
          "for coarse soils; falling head for fine soils."),
 ),
 sec("Seepage forces & the quick condition", (33, 42),
   ("eq", r"j = i\gamma_w\ \text{per unit volume},\qquad \sigma' = \gamma'L \mp i\gamma_w L\ \ (\text{down}: +,\ \text{up}: -)"),
   ("eq", r"i_c = \frac{\gamma'}{\gamma_w} \approx 1"),
   ("md", r"Upward flow reduces effective stress; when $\sigma' = 0$ the sand is **quick** (boiling, piping). "
          "Seepage force acts **in the direction of flow** and is added vectorially to the buoyant weight."),
 ),
 sec("2-D seepage: flow nets", (43, 66),
   ("eq", r"\frac{\partial^2h}{\partial x^2} + \frac{\partial^2h}{\partial z^2} = 0 \qquad q = kH\frac{N_f}{N_d}\ \text{per metre}"),
   ("md", "Flow lines ⟂ equipotentials, curvilinear **squares**, flow lines never cross. Identify boundary "
          "equipotentials (water-covered soil surfaces) and boundary flow lines (impermeable surfaces, "
          "sheet-pile faces). Use symmetry (double $N_f$ for the full section). Head at a point = upstream "
          r"head − (drops passed) × $H/N_d$; $u = \gamma_w(h - z)$."),
   ("ex", r"Cofferdam in fine sand ($k = 1.5 \times 10^{-4}\ \mathrm{m/s}$, $H = 16\ \mathrm{m}$)", "$N_f = 4$ (2 × 2 by symmetry), $N_d = 8$ "
                                                                   r"→ $q = kH N_f/N_d$ = **$1.2 \times "
                                                                   r"10^{-3}\ \mathrm{m^3/s}$ per m**."),
   ("ex", "Flood-condition effective stresses", r"Point A without seepage: $\sigma = 2 \times 10 + 21 \times "
                                                r"18 = 398$, $u = 230$ → $\sigma' = \boldsymbol{168\ "
                                                r"\mathrm{kPa}}$; with seepage $u = 190$ → $\sigma' = "
                                                r"\boldsymbol{208\ \mathrm{kPa}}$. Point B near the exit: "
                                                r"$\sigma = 72$, $u = 80$ → $\sigma' = \boldsymbol{-8\ "
                                                r"\mathrm{kPa}}$ → quick condition/piping risk at the toe."),
 ),
 sec("Anisotropic soil", (67, 85),
   ("eq", r"k_x\frac{\partial^2h}{\partial x^2} + k_z\frac{\partial^2h}{\partial z^2} = 0,\quad x_T = x\sqrt{\frac{k_z}{k_x}},\quad k' = \sqrt{k_xk_z}"),
   ("md", r"Draw the section with horizontal distances scaled by $\sqrt{k_z/k_x}$ (vertical unchanged), sketch "
          "a normal flow net, then $q = k'H N_f/N_d$. Example: $k_x = 4k_z$ → horizontal scale halved; $k' = "
          r"2 \times 10^{-6}\ \mathrm{m/s}$."),
 ),
 sec("Unconfined flow & the phreatic surface", (86, 112),
   ("md", "Dupuit assumptions: flat free surface, horizontal streamlines, vertical equipotentials, v uniform with "
          "depth."),
   ("eq", r"q = kh\frac{dh}{dx}\ \Rightarrow\ h^2 = h_0^2 - \frac{x}{L}\left(h_0^2 - h_L^2\right),\qquad q = \frac{k}{2L}\left(h_0^2 - h_L^2\right)"),
   ("md", "The **Dupuit parabola**. In earth dams the phreatic line must not exit on the downstream face "
          "(sloughing, piping, collapse); the maximum exit gradient is at the smallest flow-net element near "
          "the toe → compare with $i_c$. Remedy: **toe drain** / filter to pull the phreatic surface inside "
          "the dam."),
 ),
]}

STUDY[G2] = {"code": "CE104", "title": "Soil 9 · Shear strength of soils", "sections": [
 sec("Strength, failure & stress–strain of soil", (2, 21),
   ("md", "Soil strength is **shear** strength — it governs almost every geotechnical limit state (bearing, "
          "slopes, walls). 'Failure' may mean collapse or a limiting strain (soft soils: often **20 % strain** in "
          "triaxial). Strength depends on the loading mode (compression, extension, simple shear) and drainage."),
 ),
 sec("Mohr circle & the pole method", (22, 41),
   ("eq", r"\sigma_\theta = \frac{\sigma_1 + \sigma_3}{2} + \frac{\sigma_1 - \sigma_3}{2}\cos2\theta,\qquad \tau_\theta = \frac{\sigma_1 - \sigma_3}{2}\sin2\theta"),
   ("md", r"Soil sign convention: **compression positive**, $\theta$ anticlockwise from the $\sigma_1$ plane. "
          "Max shear (at 45°) is not on the failure plane. **Pole (origin of planes):** a line from the pole "
          "parallel to a plane meets the circle at the stresses on that plane."),
   ("eq", r"\theta_f = 45^\circ + \frac{\phi}{2}\ \ (\text{failure plane from the major principal plane})"),
   ("ex", r"Example 1 — dry sand on the failure plane: $\tau = 3.5$, $\sigma = 10\ \mathrm{kPa}$", r"$\tan\phi = 3.5/10$ → $\phi = "
                                                                            r"19.3^\circ$."),
   ("ex", "Examples 2–4", r"$\sigma_1 = 40$, $\sigma_3 = 20\ \mathrm{kPa}$: on a plane at 30°, $\sigma = 35\ "
                          r"\mathrm{kPa}$, $\tau = 8.7\ \mathrm{kPa}$; with shear on the element (40, 15)/(20, "
                          r"−15) find the principal directions from $\tan 2\theta = 15/10$ → $2\theta = "
                          r"56^\circ$."),
 ),
 sec("Friction & the Mohr–Coulomb criterion", (42, 58),
   ("eq", r"\tau_f = c' + \sigma'_n\tan\phi' \qquad \sigma'_1 = \sigma'_3\tan^2\!\left(45^\circ + \frac{\phi'}{2}\right) + 2c'\tan\!\left(45^\circ + \frac{\phi'}{2}\right)"),
   ("eq", r"\sin\phi' = \frac{\sigma'_1 - \sigma'_3}{\sigma'_1 + \sigma'_3 + 2c'\cot\phi'}\qquad \text{FS} = \frac{\tau_f}{\tau}"),
   ("md", r"Granular strength comes from **friction** and interlocking (dilation). Undrained clay: $\phi = 0$, "
          r"$\tau_f = s_u$ (horizontal envelope). Always plot **effective** stresses for drained behaviour "
          r"($\sigma' = \sigma - u$ shifts the circle left by u, same size)."),
 ),
 sec("Direct shear & simple shear", (59, 80),
   ("md", "Two-half box, normal load N, shear on a **forced horizontal plane**. Dense sand: peak then drop to "
          "residual, dilates; loose sand: no peak, contracts. Run ≥ 3 normal loads → envelope. Cheap, fast, "
          "simple; but drainage cannot be controlled (hard for clays), non-uniform stress, forced plane. In "
          r"situ $\sigma'_h = K_0\sigma'_v$ ($K_0 \approx 1 - \sin\phi'$ for NC soil)."),
   ("ex", r"Example — sandy silt, $\sigma_n = 65\ \mathrm{kPa}$, $K_0 = 0.5$, $\tau_f = 41\ \mathrm{kPa}$", r"Initial circle $\sigma_1 = 65$, "
                                                                        r"$\sigma_3 = 32.5$; failure point "
                                                                        r"(65, 41) → $\phi = \tan^{-1} (41/65) "
                                                                        r"\approx 32^\circ$."),
 ),
 sec("Triaxial test: stresses, compression & extension", (81, 101),
   ("eq", r"q = \sigma_1 - \sigma_3 = \frac{F}{A},\qquad A = \frac{A_0(1 - \varepsilon_v)}{1 - \varepsilon_a}\ \ (\text{corrected area})"),
   ("md", r"Cylindrical specimen in a pressurised cell: $\sigma_3$ = cell pressure, $\sigma_1 = \sigma_3$ + "
          r"deviator. Compression ($\sigma_1$ vertical) vs extension ($\sigma_1$ radial) give different "
          "strengths — relevant to different parts of a slip surface. **Back-pressure** saturates the "
          "specimen; drainage valve open/closed sets drained/undrained."),
 ),
 sec("UU, CU and CD tests", (102, 119),
   ("md", "| Test | Consolidation | Shearing | Gives |\n|---|---|---|---|\n| **UU** | no | undrained | $s_u$ "
          "($\\phi_u = 0$) |\n| **CU** | yes | undrained, measure u | $c'$, $\\phi'$ (and $s_u$) |\n| **CD** | "
          r"yes | drained (slow) | $c'$, $\phi'$ |"),
   ("ex", "UU on clay A", r"Different cell pressures give the same deviator at failure → $\phi_u = 0$, "
                          r"$\boldsymbol{s_u = 35\ \mathrm{kPa}}$."),
   ("ex", r"CD on sand — $\sigma_3 = 120\ \mathrm{kPa}$, deviator at failure 220 kPa", r"$\sigma_1 = 340\ "
                                                                                       r"\mathrm{kPa}$; $c' = "
                                                                                       r"0$ → $\sin\phi' = "
                                                                                       "(340 - 120)/(340 + "
                                                                                       "120)$ → "
                                                                                       r"$\boldsymbol{\phi' "
                                                                                       r"\approx 29^\circ}$ "
                                                                                       "(28.6°)."),
   ("md", r"Typical $\phi'$: gravel 40–55°, sand loose dry 28–34°, dense dry 36–45° (sandy gravel highest). "
          r"$\phi'$ is a parameter, not a strength: drained strength **increases with depth** via $\sigma'$."),
 ),
 sec("Drained vs undrained; OCR; pore-pressure parameters", (120, 142),
   ("md", "Field vane, lab vane, mini-cone and pocket penetrometer give quick $s_u$. Use **drained** strength "
          r"($c'$, $\phi'$ with $\sigma'$) for long-term/slow loading; **undrained** $s_u$ for rapid loading "
          r"of low-permeability clay (short-term). $\mathrm{OCR} = \sigma'_p/\sigma'_{v0}$ (NC = 1)."),
   ("eq", r"\Delta u = B\left[\Delta\sigma_3 + A(\Delta\sigma_1 - \Delta\sigma_3)\right],\qquad B = 1\ \text{for saturated soil}"),
   ("md", r"$A_f > 0$ (≈ 0.5–1) for NC clay/loose sand (contractive, positive $\Delta u$); $A_f < 0$ for "
          r"heavily OC clay/dense sand (dilative, negative $\Delta u$). **Correlations:** $E_u \approx "
          r"200\text{–}500 s_u$ (≈ $300 s_u$ first estimate); for NC clay $s_u/\sigma'_{v0} \approx 0.22$ "
          "(Mesri) or 0.11 + 0.0037 PI (Skempton)."),
   ("eq", r"\tau_{ff} = \frac{(\sigma'_1 - \sigma'_3)_f}{2}\cos\phi'\quad(\text{shear stress on the failure plane at failure})"),
 ),
]}

_S = "CE104/{}.pdf"
SOIL = {k: _S.format(k) for k in ["S01_Introduction", "S02_Basic_Concepts", "S03_Singapore_Soil_Formation",
                                   "S04_Phase_Relationships", "S05_Effective_Stress", "S06_Stresses_and_Strains",
                                   "S07_Compression_Behaviour", "S08_Consolidation_Time_Dependent",
                                   "S08c_1D_consolidation_derivation", "S99_Summary"]}

STUDY[SOIL["S01_Introduction"]] = {"code": "CE104", "title": "Soil 0 · Course map (CE2112)", "sections": [
 sec("Parts & order", (2, 11),
   ("md", "1. **Geology & basic characteristics** (weeks 1–4): origin of soils, Singapore geology, effective "
          "stress, phase relations, particle size, index properties, classification.\n2. **Permeability & "
          "seepage** (4–7): Darcy, permeability tests, flow nets, seepage forces.\n3. **Compressibility & "
          "consolidation** (7–10): compression of granular/fine soils, elastic settlement, compression "
          "indices, 1-D consolidation, $c_v$, preloading.\n4. **Shear strength** (10–13): Mohr–Coulomb, "
          "triaxial, drained/undrained, Skempton's A & B.\n\nMain text: Knappett & Craig, *Craig's Soil "
          "Mechanics*."),
 ),
]}

STUDY[SOIL["S02_Basic_Concepts"]] = {"code": "CE104", "title": "Soil 1 · Introduction & basic concepts", "sections": [
 sec("Geotechnical engineering", (2, 25),
   ("md", "Geotechnical work: piles, deep excavations, diaphragm walls, tunnelling (TBM/EPB), reclamation, ground "
          "improvement, offshore foundations, lab and field testing. Failures (NUS slope, Nicoll Highway, open-pit "
          "and tailings dam collapses) show why. Unlike structural design, the ground is a natural, variable, "
          "continuous medium — behaviour can't be fully quantified, so rely on observation, testing and judgement."),
 ),
 sec("Rocks, soils & groundwater", (26, 40),
   ("md", "Rocks: igneous, sedimentary, metamorphic. Soils by origin: **residual** (weathered in place), "
          "colluvial, eolian, alluvial, glacial, marine. Physical weathering → granular (same mineralogy, > 2 "
          "µm); chemical weathering → **clay** (new minerals, < 2 µm). Soil = solids + water (+ air): dry, "
          "saturated, unsaturated.\n\n**Groundwater table** = surface where $u = 0$. Soil above it may still be "
          "saturated by **capillary rise**; pore pressure there is negative (suction)."),
   ("eq", r"h_c = \frac{4T\cos\alpha}{d\,\gamma_w}\ \ (\propto 1/d),\qquad u = -\gamma_w h_c\ \text{at the top of the capillary zone}"),
 ),
 sec("Stress, strain & how soil gains strength", (41, 51),
   ("md", "Soil treated as a deformable continuum: stress = load/area (normal, shear), strain = response, "
          "modulus = stress/strain (measured by test). Soils fail by **shearing** — grains slide/roll, not "
          "crush (except calcareous sands). Resistance = **inter-particle friction** (∝ normal force) + "
          r"**interlocking** (denser packing → dilation → higher $\phi'$); sometimes cementation. Typical "
          r"$\phi' \approx 30^\circ$ sands, 20–28° clays."),
 ),
 sec("Effective stress principle", (52, 58),
   ("eq", r"\sigma' = \sigma - u\qquad \text{water at/above ground, uniform soil: } \sigma' = \gamma' d"),
   ("md", "Effective stress = inter-particle contact force per unit area; it controls friction, strength and "
          r"stiffness. Higher u → lower $\sigma'$ → lower strength. Seabed soil at $d = 0$ has $\sigma' = 0$ "
          "however deep the water — seabed soils are soft."),
 ),
 sec("Packing density: phase relations", (59, 70),
   ("eq", r"e = \frac{V_v}{V_s},\quad n = \frac{e}{1+e},\quad w = \frac{W_w}{W_s},\quad S_r = \frac{V_w}{V_v},\quad Se = wG_s"),
   ("eq", r"\gamma_d = \frac{G_s\gamma_w}{1+e},\quad \gamma = \frac{(G_s + S_re)\gamma_w}{1+e},\quad \gamma_{sat} = \frac{(G_s + e)\gamma_w}{1+e},\quad \gamma' = \gamma_{sat} - \gamma_w"),
   ("md", "Use $V_s = 1$ as the working assumption. Volumes are hard to measure, so work from weights and "
          "$G_s$."),
 ),
 sec("Packability: sand vs clay, $G_s$, relative density", (71, 79),
   ("md", "Sand: physical weathering, bulky grains, behaviour set by grading and packing. Clay: chemical "
          "weathering, plate-like minerals with charged surfaces holding adsorbed water → plasticity and "
          r"activity matter. $\boldsymbol{G_s} \approx 2.60$ sands, 2.65–2.85 clays (pycnometer)."),
   ("eq", r"D_R = \frac{e_{max} - e}{e_{max} - e_{min}}\times100\%"),
   ("md", "| $D_R\\,\\%$ | State | $\\phi'$ (°) |\n|---|---|---|\n| 0–15 | very loose | 29–32 |\n| 15–35 | loose | "
          "32–35 |\n| 35–65 | medium dense | 35–37 |\n| 65–85 | dense | 37–40 |\n| 85–100 | very dense | 40–42 |"),
 ),
 sec("Particle size distribution", (80, 90),
   ("md", "Sieve analysis for > 0.063 mm; **hydrometer** (Stokes' law, deflocculated suspension) for silt/clay down "
          "to ~2 µm."),
   ("eq", r"C_U = \frac{D_{60}}{D_{10}},\qquad C_C = \frac{D_{30}^2}{D_{60}D_{10}}"),
   ("md", "**Well graded: $C_U > 15$ and $C_C$ 1–3**; uniformly graded $C_U < 3$; gap graded $C_C < 0.5$. "
          "Well-graded soils pack densely → stronger, less compressible."),
 ),
 sec("Atterberg limits & classification", (91, 104),
   ("md", "Water content regimes: solid → (SL) → semi-solid → (PL) → plastic → (LL) → liquid. **LL** by fall "
          r"cone (30°, 80 g cone penetrates **20 mm**; $s_u \approx 2\ \mathrm{kPa}$) preferred to Casagrande. "
          r"$\mathrm{PL}$ = lowest w at which soil can be rolled into 3 mm threads."),
   ("eq", r"PI = LL - PL,\qquad LI = \frac{w - PL}{PI}\quad(LI = 0\ \text{at PL},\ 1\ \text{at LL})"),
   ("md", r"$\mathrm{PI}$ ≈ water-content change that alters strength ~100×; high PI → large "
          "compression/swelling. **BS classification:** fine-grained if > 35 % passes 0.063 mm. Plasticity "
          "chart: C (clay, above A-line) / M (silt, below) / O (organic); plasticity L < 35, I 35–50, H "
          "50–70, V > 70 % LL. Coarse: G/S + W/P/U/C/F."),
 ),
]}

STUDY[SOIL["S03_Singapore_Soil_Formation"]] = {"code": "CE104", "title": "Soil 2 · Singapore soil formations", "sections": [
 sec("The four main formations", (2, 4),
   ("md", "| Formation | Where | What |\n|---|---|---|\n| **Bukit Timah Granite** | north & central | igneous rock + "
          "residual soils |\n| **Jurong Formation** | west (incl. NUS) | sedimentary rocks + residual soils |\n"
          "| **Old Alluvium** | east | Quaternary sediments |\n| **Kallang Formation** | south, coast, downtown, "
          "valleys | recent sediments, marine clay |"),
 ),
 sec("Bukit Timah Granite", (5, 8),
   ("md", "Triassic granite weathered to: stiff–hard clayey silt near surface (to ~20 m) over dense sandy silt/silty "
          "sand (~10–20 m), then rock. Challenges: **corestones and undulating rockhead** (TBMs enter/exit rock "
          "repeatedly); sandy silt can **flow** under high pore pressure → ground loss."),
 ),
 sec("Jurong Formation", (9, 11),
   ("md", "Late Triassic–Early Jurassic sandstone, mudstone, siltstone, shale, folded/faulted. **Extremely "
          "variable** with depth and location; weathered to stiff soil ($s_u$ 100–200 kPa) in places, "
          "near-intact rock elsewhere (e.g. under parts of the CBD)."),
 ),
 sec("Old Alluvium", (12, 14),
   ("md", "5–0.5 Ma, poorly lithified clayey coarse sand with pebble stringers — soil-like at top, weak-rock-like "
          "below. Highly heterogeneous; sandy → **flows under water pressure**; high permeability → water ingress "
          "into excavations."),
 ),
 sec("Kallang Formation (marine clay)", (15, 17),
   ("md", "Holocene marine, alluvial, estuarine deposits covering ~25 % of the island. **Upper marine clay**: very "
          "soft–soft, high LL/PI, 5–8 % organics; **lower marine clay**: soft–medium stiff (deposited 12–18 ka). "
          "Very low permeability → consolidation settlement over **50–100 years**; deep excavation risks "
          "(Nicoll Highway collapse, 2004)."),
   ("tip", "FEE 2017 Part 2 Q3 (pile selection near an MRT viaduct on marine clay) draws directly on this."),
 ),
]}

STUDY[SOIL["S04_Phase_Relationships"]] = {"code": "CE104", "title": "Soil 1a · Phase relationships (supplement)", "sections": [
 sec("Formulae with $V_s = 1$", (2, 4),
   ("eq", r"V = 1 + e,\ \ V_w = S_re,\ \ W_s = G_s\gamma_w,\ \ W_w = S_re\gamma_w,\ \ A_v = \frac{e - wG_s}{1+e}"),
   ("eq", r"\gamma = \frac{G_s\gamma_w(1 + w)}{1 + e}\qquad \text{saturated: } e = wG_s,\ \gamma_{sat} = \frac{G_s\gamma_w(1+w)}{1 + wG_s}"),
   ("tip", "Draw the phase diagram with $V_s = 1$, fill in volumes then weights — every relationship follows."),
 ),
]}

STUDY[SOIL["S05_Effective_Stress"]] = {"code": "CE104", "title": "Soil 1b · Effective stress calculations", "sections": [
 sec("Hydrostatic examples", (2, 4),
   ("md", r"Water table at or above ground in uniform soil → $\sigma' = \gamma'd$ (water depth irrelevant). "
          r"Otherwise build a table: total stress $\sigma = \sum\gamma_id_i$ (bulk above GWT, saturated below, "
          r"+ water above ground), $u = \gamma_w$ × depth below the GWT, $\sigma' = \sigma - u$."),
   ("ex", r"Water 1000 m deep over soil, point 3 m below seabed ($\gamma_{\mathrm{sat}} = 18$)", r"$\sigma = 3 "
                                                                                                 r"\times 18 + "
                                                                                                 r"1000 \times "
                                                                                                 "10 = "
                                                                                                 r"10\,054$; "
                                                                                                 "$u = 1003 "
                                                                                                 r"\times 10 = "
                                                                                                 r"10\,030$ → "
                                                                                                 r"$\sigma' = "
                                                                                                 r"\boldsymbol{24\ "
                                                                                                 r"\mathrm{kPa}}$ "
                                                                                                 "($= 3 "
                                                                                                 r"\times 8$)."),
   ("ex", "GWT below ground", r"Point B at 2 m ($\gamma = 16$) above GWT: $\sigma = 32$, $u = 0$ → $\sigma' = "
                              r"32\ \mathrm{kPa}$; continue below the GWT with $\gamma_{\mathrm{sat}}$ and $u "
                              r"= \gamma_w(z - z_w)$."),
 ),
]}

STUDY[SOIL["S99_Summary"]] = {"code": "CE104", "title": "Soil · Part 1 summary (checklist)", "sections": [
 sec("What to know from Part 1", (2, 12),
   ("md", "- Rock types and soil origins; granular vs clay (physical vs chemical weathering, 2 µm "
          "boundary).\n- Groundwater table, confined/artesian aquifers, capillary rise and suction.\n- Stress, "
          "strain, modulus; soils fail by sliding/rolling — friction + interlocking.\n- Effective stress "
          "principle and hydrostatic calculations.\n- Phase relations, $D_R$.\n- Grading ($C_U$, $C_C$), "
          "Atterberg limits, PI, LI; BS/ISO classification and the plasticity chart."),
 ),
]}

STUDY[SOIL["S06_Stresses_and_Strains"]] = {"code": "CE104", "title": "Soil 5 · Stresses, strains & moduli", "sections": [
 sec("Why stresses & strains", (1, 8),
   ("md", "Two design requirements: **stability** (ULS — shear failure of the skeleton, not particle "
          r"crushing) and **serviceability** (deformations). Stiffness $k = F/\delta$ depends on geometry; "
          r"**modulus** $E = \sigma/\varepsilon$ is a material property. In saturated soil the skeleton "
          r"carries normal and shear stress, water only normal stress → $\sigma' = \sigma - u$ (contact area ≪ "
          "total area)."),
 ),
 sec("Stress & strain at a point (soil sign convention)", (9, 15),
   ("md", r"Six independent stress components ($\tau_{xy} = \tau_{yx}$ etc.); **compression positive** in soil "
          r"mechanics. Strains: $\varepsilon_x = -\partial v_x/\partial x$, $\gamma_{xy} = -(\partial "
          r"v_x/\partial y + \partial v_y/\partial x)$."),
 ),
 sec("Elastic moduli: E, G, K, D", (16, 25),
   ("eq", r"\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right],\quad G = \frac{E}{2(1+\nu)},\quad K = \frac{E}{3(1-2\nu)},\quad \varepsilon_v = \frac{p}{K}"),
   ("eq", r"D = \frac{E(1-\nu)}{(1+\nu)(1-2\nu)} = \frac{1}{m_v}\quad(\text{constrained modulus: lateral strains} = 0)"),
   ("md", "E: load in one direction, others free. **D (1-D/oedometer)** is used in consolidation via $m_v$. "
          "Real soil is non-linear and inelastic — linear moduli are convenient approximations."),
 ),
]}

STUDY[SOIL["S07_Compression_Behaviour"]] = {"code": "CE104", "title": "Soil 6 · Compression behaviour", "sections": [
 sec("Isotropic vs 1-D compression", (2, 7),
   ("md", "Isotropic (triaxial cell pressure, bulk modulus) and **1-D** (oedometer: rigid ring, no lateral "
          "strain, constrained modulus — models wide fills and reclamation). Neither can cause shear failure. "
          r"Drained: $u = 0$, $\sigma' = \sigma$; $\sigma'_h = K\sigma'_v$."),
 ),
 sec(r"$e\text{–}\log p'$: VCL, swelling lines & preconsolidation", (8, 14),
   ("md", r"Below $\boldsymbol{p'_c}$ the soil is stiff and nearly elastic (**swelling–recompression line**, "
          "slope $C_s$); above it, large irreversible compression on the **virgin compression line** (slope "
          "$C_c$, particle rearrangement). $p'_c$ = highest past effective stress. **Casagrande method**: "
          "max-curvature point → tangent & horizontal → bisector → extend the VCL back to meet it."),
   ("eq", r"\text{VCL: } \Delta e = -C_c\log\frac{p'_2}{p'_1}\qquad \text{SRL: } \Delta e = -C_s\log\frac{p'_2}{p'_1}\quad(\text{effective stresses only})"),
   ("eq", r"m_v = \frac{\Delta\varepsilon}{\Delta\sigma'} = \frac{-\Delta e}{(1+e_0)\Delta\sigma'},\qquad D = \frac{1}{m_v}"),
 ),
 sec("1-D settlement", (15, 17),
   ("eq", r"\rho = \frac{H\,\Delta e}{1 + e_0}\qquad \text{NC: } \rho = \frac{C_cH}{1+e_0}\log\frac{\sigma'_0 + \Delta\sigma'}{\sigma'_0}\qquad \rho = m_v\,\Delta\sigma'\,H"),
   ("md", r"OC soil crossing $p'_c$: $C_s$ from $\sigma'_0$ to $p'_c$, then $C_c$ beyond. $C_c$ correlates "
          "with PI. VCL is unique for a clay but sands have different VCLs as vibration densifies them."),
 ),
]}

STUDY[SOIL["S08_Consolidation_Time_Dependent"]] = {"code": "CE104", "title": "Soil 7 · Consolidation & time-dependent behaviour", "sections": [
 sec("Why consolidation takes time", (2, 10),
   ("md", "Saturated clay compresses only as water drains out — governed by permeability. Examples: drawdown "
          "beside excavations; Singapore reclamation (fill 2–3 years, settlement over decades); **Kansai "
          r"airport** ~10 m settlement over 50–100 years. Questions: **how much** ($\Delta e$ or $m_v$) and "
          "**how long** ($c_v$)."),
 ),
 sec("Short-term, long-term & excess pore pressure", (11, 29),
   ("md", r"Spring–piston analogy: just after a wide load $\Delta \sigma$ the **excess pore pressure** $u_0 = "
          r"\Delta \sigma$ carries it all ($\sigma'$ unchanged); in the long term u → 0 and $\sigma'$ "
          r"increases by $\Delta \sigma$. Excess pwp = total − long-term equilibrium pwp. At a drained "
          r"boundary $u = 0$ immediately; at an impermeable boundary $\partial u/\partial z = 0$. "
          "**Isochrones** show u(z) at successive times."),
   ("eq", r"U_z = \frac{u_0 - u}{u_0},\qquad \bar{U} = \frac{\text{area dissipated}}{\text{area of initial } u_0 \text{ profile}} = \frac{\rho_t}{\rho_\infty}"),
 ),
 sec("Terzaghi's 1-D consolidation equation", (30, 37),
   ("eq", r"c_v\frac{\partial^2u}{\partial z^2} = \frac{\partial u}{\partial t},\qquad c_v = \frac{k}{m_v\gamma_w}"),
   ("md", "Assumptions: homogeneous, saturated, incompressible grains and water, 1-D flow and strain, Darcy, "
          "k and $m_v$ constant. Derived from equilibrium, compatibility, $m_v$, effective stress, Darcy and "
          "continuity (see the derivation supplement)."),
   ("eq", r"T_v = \frac{c_vt}{D^2}\quad(D = \text{longest drainage path: } H/2 \text{ for double drainage})"),
 ),
 sec("Solutions & isochrones", (38, 52),
   ("eq", r"\bar{U} \approx \sqrt{\frac{4T_v}{\pi}}\ (\bar{U} < 0.6),\qquad T_v = 1.781 - 0.933\log_{10}\left[100(1 - \bar{U})\right]\ (\bar{U} > 0.6)"),
   ("md", "Double drainage = two single-drainage problems back to back (mid-depth acts as impermeable). "
          "$T_{50} = 0.197$, $T_{90} = 0.848$. Other initial profiles: **triangular** (e.g. rapid drawdown "
          "with an aquifer below), trapezoidal, layered (Luscher). Use the chart matching the $u_0$ shape and "
          "drainage — the centre curve (trapezoidal, double drainage, includes rectangular) is most used."),
   ("ex", r"Reclamation: 50 kPa on 5 m marine clay over sandstone ($c_v = 0.5\ \mathrm{m^2/yr}$, $\rho_\infty "
          r"= 1.61\ \mathrm{m}$)",
    r"Double drainage, $D = 2.5\ \mathrm{m}$. Settle 1.5 m: $\bar{U} = 0.932$ → $T \approx 1.0$ → $t = 1.0 "
    r"\times 2.5^2/0.5 = \boldsymbol{12.5\ \mathrm{yr}}$. After 2 yr: $T = 0.16$ → $\bar{U} \approx 0.45$ → "
    "**0.72 m**."),
 ),
 sec("Oedometer: $C_c$, $C_s$, $m_v$ and $c_v$ (curve fitting)", (55, 71),
   ("md", r"$c_v = k/(m_v\gamma_w)$ is rarely used (k is hard to measure) — fit the settlement–time curve "
          "instead. Real curves have immediate settlement (air) and **secondary compression**."),
   ("eq", r"\text{Taylor } \sqrt{t}\text{: } c_v = \frac{0.848\,D^2}{t_{90}}\qquad \text{Casagrande log } t\text{: } c_v = \frac{0.197\,D^2}{t_{50}}"),
   ("md", "**Taylor:** corrected origin, line through the initial straight part, second line with 1.15× the "
          "inverse slope → meets the curve at $t_{90}$. **Casagrande:** correct zero using $t_2 = 4t_1$ "
          r"($\rho_2 - \rho_1 = \rho_1$ offset), end of primary from the intersection of the primary and "
          "secondary tangents, take the midpoint → $t_{50}$."),
 ),
 sec("General 1-D dissipation problems", (72, 75),
   ("steps", [r"Sketch $\sigma$, $u$, $\sigma'$ before the change (initial).",
              r"Sketch them just after the change (short term: undrained, $\sigma'$ unchanged in clay, $\Delta "
              r"u = \Delta \sigma$).",
              "Sketch the long-term equilibrium (steady seepage or hydrostatic).",
              "Initial excess pwp = short-term − long-term u → choose the matching chart and drainage → T → "
              r"t, settlement = $\bar{U}\rho_\infty$."]),
 ),
]}

STUDY[SOIL["S08c_1D_consolidation_derivation"]] = {"code": "CE104", "title": "Soil 7a · Derivation of the 1-D consolidation equation", "sections": [
 sec("Derivation outline", (1, 3),
   ("steps", [r"Equilibrium: $\partial \sigma/\partial z + \gamma = 0$; with the load $p_0$ constant in time, "
              r"$\partial \sigma'/\partial t = -\partial u/\partial t$.",
              r"Compatibility: $d\varepsilon = -de/(1 + e)$.",
              r"Stress–strain: $m_v = -de/[(1 + e)d\sigma']$.",
              r"Darcy: $v = -k \partial (u/\gamma_w)/\partial z$.",
              r"Continuity: $-\partial v/\partial z = \partial \varepsilon/\partial t = m_v \partial "
              r"\sigma'/\partial t = -m_v \partial u/\partial t$.",
              r"Combine → $c_v\,\partial^2u/\partial z^2 = \partial u/\partial t$ with $c_v = "
              r"k/(m_v\gamma_w)$; normalise with $Z = z/D$, $T = c_vt/D^2$."]),
   ("md", r"Supplementary sheets: **consolidation curves** ($\bar{U}\text{–}T$ for rectangular, triangular and "
          "trapezoidal initial profiles, single/double drainage) and **double-drainage isochrones** — keep "
          "them in your binder."),
 ),
]}

# CE104 tutorial questions live in utils/study_notes_ce104q.py (q blocks)


# ---------------------------------------------------------------- CE203 geotechnical (separate module)
from utils.study_notes_ce203 import GEO as _GEO  # noqa: E402

STUDY.update(_GEO)

from utils.study_notes_hyd import HYD as _HYD  # noqa: E402

STUDY.update(_HYD)

from utils.study_notes_ce201 import CON as _CON  # noqa: E402

STUDY.update(_CON)

from utils.study_notes_ce202 import STL as _STL  # noqa: E402

STUDY.update(_STL)

from utils.study_notes_ce103 import ANA as _ANA  # noqa: E402

STUDY.update(_ANA)

from utils.study_notes_ce104q import CE104Q as _CE104Q  # noqa: E402

STUDY.update(_CE104Q)

from utils.study_notes_ce203q import GEOQ as _GEOQ  # noqa: E402

STUDY.update(_GEOQ)

from utils.study_notes_ce201q import CONQ as _CONQ  # noqa: E402

STUDY.update(_CONQ)

from utils.study_notes_ce202q import STLQ as _STLQ  # noqa: E402

STUDY.update(_STLQ)

from utils.study_notes_ce103q import ANAQ as _ANAQ  # noqa: E402

STUDY.update(_ANAQ)

from utils.study_notes_hydq import HYDQ as _HYDQ  # noqa: E402

STUDY.update(_HYDQ)

from utils.study_notes_ce101q import MATQ as _MATQ  # noqa: E402

STUDY.update(_MATQ)

from utils.study_notes_ce102q import MECHQ as _MECHQ  # noqa: E402

STUDY.update(_MECHQ)

from utils.study_notes_pe import PE as _PE  # noqa: E402

STUDY.update(_PE)

# keep last: give every tutorial question its source doc/page and a stable id
from utils.qblock import fill_sources as _fill_sources  # noqa: E402

_fill_sources(STUDY)
