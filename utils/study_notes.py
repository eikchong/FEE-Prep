"""Condensed study notes written from the CE1101 text notes (S1–S4 statics, M1–M5 mechanics of
materials) — in the same order as the notes, readable on the site without opening the PDFs.

Block types:
  ("md", text)          paragraph / bullets (markdown)
  ("eq", latex)         display equation
  ("steps", [..])       numbered procedure
  ("ex", title, text)   worked-example summary (results as given in the notes)
  ("tip", text)         exam tip / common trap
  ("tut", text)         tutorial question that practises this section
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
   ("md", "γ is the angle *inside the force triangle* opposite R (= 180° − angle between the two forces). "
          "For several forces, resolve into **Cartesian components** and add:"),
   ("eq", r"R_x = \sum F_x,\quad R_y = \sum F_y,\quad R = \sqrt{R_x^2 + R_y^2},\quad \theta = \tan^{-1}\frac{R_y}{R_x}"),
   ("ex", "Example 1.6", "Two forces 300 N and 350 N combined by cosine then sine rule: R = 175.0 N; direction "
          "found from the triangle angle 89.13° → 30.87° from the horizontal."),
   ("ex", "Example 1.8 (eyebolt, three ropes)", "F₁ = 80 N, F₂ = 120 N, F₃ = 50 N resolved with a consistent sign "
          "convention → ΣFx = 94.34 N, ΣFy = 132.35 N → R = 162.5 N at 54.5° — the object moves in that direction."),
   ("ex", "Example 1.9 (trolley)", "Choose P so that the resultant of P and 1400 N is vertical: sketch the "
          "parallelogram with R vertical, then sine rule gives P and R (or set ΣFx = 0)."),
   ("tip", "Always state your sign convention before summing components."),
 ),
 sec("Equilibrium of a particle", (31, 43),
   ("md", "Concurrent forces → the body can be treated as a **particle**. It is in **equilibrium** when the "
          "resultant is zero:"),
   ("eq", r"\sum F_x = 0,\qquad \sum F_y = 0"),
   ("ex", "Example 1.10 (lifting a 3000 N beam with a 2-leg sling)", "Symmetric legs: 2T sinθ = 3000. With "
          "T_max = 6500 N, sinθ = 3000/13 000 → θ = 13.34°; shortest total rope = 2 × 1.5/cos13.34° = 3.08 m. "
          "Smaller angles need less rope but give larger rope forces."),
   ("ex", "Example 1.11 (100 kg tank, 2 m rope over a pulley)", "Frictionless pulley ⇒ equal tension and equal "
          "angles. 2T sinθ = 981 N. Points A–B (0.6 m apart): θ = 53.13°, T = 613 N; points C–D (0.3 m): "
          "θ = 72.54°, T = 514 N → use C–D."),
   ("ex", "Cable ABC 2.5 m over a pulley, 25 kg", "Geometry gives cosθ = 1.5/2.5 → θ = 53.13°, "
          "T = 245.3/(2 sin53.13°) = 153.3 N; then x = 0.64 m from the triangle geometry."),
   ("tut", "Tutorial 1 Q1 — scoreboard (9 kN) on cable ABC: choose the cable length so that T ≤ 20 kN and the "
           "drop d ≤ 0.3 m (particle equilibrium at B, 2T sinθ = W)."),
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
   ("md", "A **couple** = two equal, opposite, non-collinear parallel forces. Its moment **M = Fd is the same "
          "about every point**. A force F acting at distance d from point A ≡ the same force through A **plus** a "
          "couple M = Fd."),
   ("eq", r"\mathbf{R} = \sum \mathbf{F}_i,\qquad M_A^R = \sum M_A(\mathbf{F}_i)"),
   ("ex", "Example 2.2 (traffic light pole)", "Two 20 kg lights replaced at the pole base by a vertical force "
          "392.4 N and a moment 784.8 Nm."),
   ("ex", "Example 2.3 (canopy beam)", "Forces 5 kN, 10 kN and a 6 kN sling → single resultant 10.3 kN, located "
          "by equating moments about A: x = 0.87 m."),
 ),
 sec("Rigid-body equilibrium, supports, two- & three-force members", (17, 25),
   ("eq", r"\sum F_x = 0,\qquad \sum F_y = 0,\qquad \sum M_O = 0"),
   ("md", "**Supports:** a support exerts a **force** in each direction it prevents translation and a **moment** "
          "if it prevents rotation — roller 1 reaction, pin/hinge 2, fixed/clamped 3.\n\n"
          "- **Two-force member:** the two forces are equal, opposite and **collinear** (along the line joining the "
          "two points).\n"
          "- **Three-force member:** the three forces are **concurrent or parallel**."),
   ("ex", "Example 2.4 (crane boom with cable CD over a pulley)", "Moments about the pin A → T_CD = 93.8 kN; force "
          "equations give A along/perpendicular to the boom (112.6 kN, 15.1 kN), i.e. 69.5 kN and 90.0 kN in x–y."),
   ("tip", "Take moments about the point where the most unknowns pass — each equation then gives one unknown."),
   ("tut", "Tutorial 1 Q2 — jib crane for a 6 kN engine (with dynamic factor): position of the hoist that "
           "governs the tie-rod force and pin reactions."),
   ("tut", "Tutorial 2 Q6 — stack of blocks: maximum overhang x before tipping (moment equilibrium about each "
           "edge, block by block from the top)."),
 ),
 sec("Case study: Leaning Tower of Pisa", (26, 34),
   ("md", "Weight 144 MN acting at the C.G. (27.1 m up a 58.2 m tower tilted 5.6°) is eccentric to the 19.6 m "
          "base → overturning moment. Assume soil pressure p = C + 0.625 r cosθ and integrate over the circular base "
          "in polar coordinates: ΣF_y = 0 gives C, ΣM_EW = 0 gives the linear term. Maximum pressure at the "
          "southern edge (r = R = 9.8 m, θ = 0)."),
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
              "Use ΣF in the remaining direction for the last one."]),
   ("ex", "Worked example (15 kN, 5 kN loads)", "Cut through CE, CD, BD; moments about D and C give the chord "
          "forces, ΣF_y gives the diagonal."),
 ),
 sec("Solution strategy for a whole truss", (20, 21),
   ("steps", ["FBD of the entire truss as one rigid body.",
              "Find the support reactions (as many as needed).",
              "Inspect every joint — is it special? Mark zero-force members (e.g. F_BC = 0).",
              "Use joints or sections for the required members, remembering which reactions are known."]),
 ),
 sec("Real-world truss failures & analysis", (22, 47),
   ("ex", "Example 3.1 — I-35W Mississippi bridge (2007)", "Causes: under-designed gusset plates, +20 % self-weight "
          "from added overlay, construction loads during repairs. Modelled as simply supported spans; reactions "
          "1114.3 kN and 1485.7 kN; by sections: F_DE = 2905 kN (T, most critical), F_KL = 2743 kN (C), "
          "F_GK = 2118 kN (C) — using moment centres at member intersections, including an imaginary point R."),
   ("ex", "Skagit River bridge (2013)", "A tall truck load struck upper members. Single span by joints with equal "
          "loads P: bottom chord all tension, top chord all compression (truss acts like a beam); critical CD and "
          "DE = 4.80P (T). Homework: add a horizontal impact force F — use superposition."),
   ("tip", "A truss under gravity behaves like a beam: top chord compression, bottom chord tension, largest chord "
           "forces near midspan, largest diagonals near the supports."),
   ("tut", "Tutorial 1 Q3 — water-tank tower under wind (3 kPa): choose the minimum stable bracing pattern that "
           "minimises the main-leg forces (GH critical)."),
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
          "P = 3.97 kN; bucket GHJ → F_CG = 2.67 kN; arm ABCH → F_AD = 11.45 kN; continue to EF and pin I."),
   ("ex", "Example 4.2 — billboard frames (240 kg, 3 frames)", "Share the load by tributary length: edge frame takes "
          "W/4 → P = 294.3 N at each hanger. Entire frame → links BG and DG; frame ABCI → AF; frame CDE → EH. "
          "Avoid solving pin forces you don't need; check with ΣM about another point."),
   ("tut", "Tutorial 2 Q4 — pin-connected structure: tension in rod BD and pin forces; then choose the 'best' "
           "position of D along CE by tabulating the forces against x."),
 ),
 sec("Cables under concentrated loads", (26, 36),
   ("md", "Cables resist **tension only**. Between point loads each segment is straight (a two-force member). "
          "There are **4 support unknowns** but only 3 global equations → one extra piece of information is needed: "
          "the **position of one point**, the **tension or slope** somewhere, or the **total length**."),
   ("steps", ["FBD of the whole cable; write one equation in the chosen primary unknowns (e.g. ΣM_B = 0 for A_x, A_y).",
              "Cut at the point with extra information and take moments about the cut (position known), or use "
              "ΣF with the known tension/slope.",
              "If only the length L_c is known: cut at every load, one moment equation per cut, plus the length "
              "equation below.",
              "Then get each segment's slope and tension; the horizontal component is the same everywhere."]),
   ("eq", r"L_c = \sum_{i=1}^{n+1}\sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2}"),
   ("tip", "With no horizontal loads T_x is constant, so the **steepest segment carries the largest tension**."),
 ),
 sec("Cable examples", (37, 45),
   ("ex", "Example 4.3 — crate hung from a cable via beam EF", "All points known → slopes AB 36.87°, BC 26.57°, "
          "CD 45° (steepest → critical, T_CD = 900 N). Equilibrium at C then B gives the hanger forces; beam EF "
          "then gives the largest crate weight and its position x."),
   ("ex", "Example 4.4 (homework)", "Sag y_C unknown → trial T_AB until the first segment reaches 700 N; find the "
          "largest mass of cylinder F."),
   ("tut", "Tutorial 2 Q5 — traffic lights (15 kg, 30 kg) on a cable: sag y₂ ≤ 1.0 m and T ≤ 1000 N → minimum "
           "cable length and the sags at all load points."),
 ),
]}

# ============================================================== M1 Axial members
STUDY[M1] = {"code": "CE102", "title": "M1 · Introduction & axial force members", "sections": [
 sec("Statics vs mechanics of materials", (3, 5),
   ("md", "**Statics** gives forces from equilibrium (bodies assumed rigid). **Mechanics of materials** adds "
          "stress–force, strain–deformation and stress–strain relations so we can find deformation.\n\n"
          "- Statically **determinate**: FBD + equilibrium → forces; then σ–ε gives deformation.\n"
          "- Statically **indeterminate**: also need **compatibility** (geometry of the deformed structure)."),
 ),
 sec("Stress, strain & the stress–strain relationship", (6, 13),
   ("md", "Stress at a point = limit of ΔF/ΔA: **normal** σ (perpendicular) and **shear** τ (in-plane). Sign: a stress "
          "on a positive face in a positive direction is positive (τ_ij: i = face, j = direction)."),
   ("eq", r"\sigma_{avg} = \frac{P}{A} \qquad \tau_{avg} = \frac{V}{A} \qquad \text{double shear: } V = \frac{P}{2}"),
   ("eq", r"\varepsilon = \frac{\Delta L}{L} \qquad \gamma_{xy} = \text{change of the right angle (rad)}"),
   ("md", "Mild steel σ–ε: linear elastic (slope **E**) → yield plateau → strain hardening → necking/failure."),
   ("eq", r"\varepsilon_{yy} = \varepsilon_{zz} = -\nu\,\varepsilon_{xx}\quad\text{(uniaxial)};\qquad "
          r"\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right]"),
   ("md", "The second form (**generalised Hooke's law**) superposes the strains from normal stresses in all three "
          "directions."),
   ("tut", "Tutorial 3 Q1(b) — air-inflated fabric under biaxial σx = 120 MPa, σz = 160 MPa (E = 87 GPa, ν = 0.34): "
           "change in length of the sides and the diagonal."),
 ),
 sec("Allowable stress & factor of safety; design examples", (14, 25),
   ("eq", r"n_s = \frac{P_{failure}}{P_{allowable}} = \frac{\sigma_{failure}}{\sigma_{allowable}} \geq 1"),
   ("ex", "Example 1.1 — mountain-bike suspension pins (P = 1800 N, τ_ult = 150 MPa)",
    "Equilibrium of ABD → F_BC = 8858 N. Pins in **double shear** carry V/2 each: minimum d_B = 8.67 mm; "
    "pin D (resultant 7354.5 N) d_D = 7.9 mm."),
   ("ex", "Example 1.2 — cast-in anchor (a = 30 mm, h = 100 mm, d = 10 mm)",
    "Check each failure mode — concrete shear (cylinder surface), concrete cone tension + shear (truncated cone, "
    "45°), concrete tension, bolt tension — compute P for each; the **smallest P governs**."),
   ("tut", "Tutorial 3 Q1(a) — connecting rod AB: maximum allowable piston force from σ_c on the rod "
           "(depends on the crank geometry R/L)."),
 ),
 sec("Deformation of axially loaded members", (26, 29),
   ("eq", r"\delta = \frac{PL}{EA} \qquad \delta = \sum_i \frac{P_iL_i}{E_iA_i} \qquad \delta = \int_0^L\frac{P(x)}{E\,A(x)}dx"),
   ("md", "Use internal axial force of each segment (cut and draw an FBD), not the applied loads."),
   ("tut", "Tutorial 3 Q2(a) — tapered plate (width 2a → a): δ = (PL/Eta) ln 2. Q2(b) — hanging mine cable with "
           "self-weight: strain varies linearly along the cable."),
 ),
 sec("Statically indeterminate members & compatibility", (30, 31),
   ("eq", r"\text{degree of indeterminacy} = \text{no. of unknowns} - \text{no. of equilibrium equations}"),
   ("steps", ["Equilibrium equation(s).", "Compatibility (e.g. total δ = 0 between fixed ends).",
              "Force–deformation δ = PL/EA; solve together."]),
 ),
 sec("Truss deflections by geometry", (32, 35),
   ("md", "Members elongate/shorten by δ = NL/EA and the joint must move so that all members stay connected."),
   ("ex", "Example 1.3 (P = 15 kN, A = 100 mm², E = 200 GPa)", "Joint C: F_AC = 9.375 kN (C), F_BC from cosθ = 4/5, "
          "sinθ = 3/5; member shortenings → geometry of the displaced joint C′ → (δ_C)vert ≈ 1.46 mm."),
   ("tut", "Tutorial 3 Q3(a) — choose the angle θ for a two-bar truss of minimum weight at equal allowable stress."),
 ),
 sec("Pile foundations; rigid bars on cables", (36, 48),
   ("md", "**Pile load test:** kentledge (concrete blocks) and hydraulic jacks check the calculated capacity on a few "
          "piles."),
   ("ex", "Example 1.4 — 300 mm bored pile, P = 2000 kN, skin friction increasing linearly with depth",
    "Equilibrium → friction intensity 266.7 kN/m at the toe (22.2y kN/m); internal force P(y) varies → "
    "δ = ∫P(y)dy/AE = 5.28 mm."),
   ("ex", "Example 1.6 — rigid bar ABD on cables BC and CD (6 kN/m)",
    "One moment equation + compatibility from the rotated rigid bar (similar triangles) and cable geometry "
    "(δ_cable = δ_vertical cosθ) → solve the two cable forces."),
   ("tut", "Tutorial 3 Q3(b) — rigid ABCD on brass and aluminium rods: displacement of D under 40 kN."),
 ),
]}

# ============================================================== M2 Torsion
STUDY[M2] = {"code": "CE102", "title": "M2 · Torsional members", "sections": [
 sec("Torsion formula & polar second moment", (3, 9),
   ("md", "Assumptions (circular shafts): axis stays straight, sections stay **plane and circular**, radial lines stay "
          "straight, small rotations, linear elastic. Shear strain γ = r dθ/dx grows linearly with r."),
   ("eq", r"\tau = \frac{T\,r}{J},\qquad \tau_{max} = \frac{T\,c}{J}"),
   ("eq", r"J_{solid} = \frac{\pi R^4}{2} = \frac{\pi D^4}{32},\qquad J_{hollow} = \frac{\pi}{2}(R_2^4 - R_1^4) = \frac{\pi}{32}(D_2^4 - D_1^4)"),
 ),
 sec("Angle of twist; axial–torsion analogy; limitations", (10, 14),
   ("eq", r"\phi = \frac{TL}{GJ},\qquad \phi = \sum_i\frac{T_iL_i}{G_iJ_i},\qquad \phi = \int_0^L\frac{T(x)}{G\,J(x)}dx"),
   ("md", "| Axial | Torsion |\n|---|---|\n| δ = FL/EA | θ = TL/GJ |\n| σ = F/A | τ = Tr/J |\n\n"
          "Valid only for **circular** sections, linear elastic; ignores stress concentrations at abrupt changes. "
          "Sign: **right-hand rule** (thumb outward from the cut face = positive)."),
 ),
 sec("Statically determinate shafts; bolted couplings; distributed torque", (15, 26),
   ("ex", "Example 2.1 — 35 mm shaft, torques 30/25/40/65/80 Nm", "Internal torques by sections: T_AB = −30, "
          "T_BC = −55, T_CD = −15, T_DE = −80 Nm. J = 147 324 mm⁴; |T|max = 80 Nm → τ_max ≈ 9.5 MPa; "
          "φ_A/E = ΣTL/JG over the four segments."),
   ("ex", "Example 2.2 — bolted coupling (shaft r = 30 mm, bolts d = 10 mm on R = 75 mm)",
    "'Shaft fails before bolts': bolts in shear, T = n·(τ·πd²/4)·R vs shaft T = τ·J/c → n ≥ 7.2 → **8 bolts**."),
   ("ex", "Example 2.3 — drill pipe with end torque T_A and friction torque rising linearly to t₀",
    "Equilibrium T_B = T_A + t₀L/2; internal torque varies along the pipe → φ by integration."),
   ("tut", "Tutorial 4 Q4(a) — geared shafts (G = 80 GPa, d₁ = 40 mm, d₂ = 30 mm, T = 400 Nm): rotation at D and "
           "τ_max in each shaft (gear ratio transfers torque and rotation). Q4(b) — rod with linearly varying "
           "distributed torque reaction: t₀ and twist at A."),
 ),
 sec("Power transmission", (27, 31),
   ("eq", r"P = T\omega,\qquad \omega = \frac{2\pi N}{60}\ \text{rad/s},\qquad 1\ \text{hp} = 0.745\ \text{kW}"),
   ("ex", "Example 2.4 — car drive shaft (thin tube, d_o = 55 mm, 180 hp at 1500 rpm)",
    "ω = 157.1 rad/s, P = 134.1 kW → T = 853.6 Nm; τ_allow → d_i ≤ 45.2 mm → minimum wall 4.9 mm; then check the "
    "twist limit."),
   ("ex", "Example 2.5 (homework)", "Helicopter rotor shaft: 600 hp at 1200 rpm, τ_allow = 55 MPa (plus twist limit)."),
 ),
 sec("Statically indeterminate torsion", (32, 40),
   ("steps", ["Equilibrium: T_A + T_B = applied torques.",
              "Compatibility: total twist between the fixed ends = 0 (or a known gap/slip).",
              "Internal torques by sections; φ = ΣTL/GJ; solve."]),
   ("ex", "Example 2.6 — shower-curtain hanger (d_o = 30 mm, t = 1.5 mm, G = 74 GPa, end A free to rotate 0.005 rad)",
    "If A were loose the twist would exceed 0.005 rad, so A engages: T_A = 8.43 Nm, T_B = 11.57 Nm; "
    "τ_max = 15.6 MPa in segment CD (28.4 Nm)."),
   ("ex", "Example 2.7 — rubber annulus spring", "Shear stress τ = T/(2πr²h) decreases with radius; twist of the "
          "shaft by integrating γ across the annulus."),
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
   ("md", "- q = 0 → V constant, M linear. Uniform q → V linear, M parabolic.\n"
          "- **Point load P (down):** V drops by P; M has a kink (no jump).\n"
          "- **Applied couple M₀:** V unchanged; M jumps by M₀.\n"
          "- **M is maximum where V = 0** (or changes sign)."),
 ),
 sec("Sketching procedure", (12, 12),
   ("steps", ["FBD with loads, reactions and dimensions.", "Support reactions from equilibrium.",
              "Vertical construction lines at every load change.",
              "SFD segment by segment, left to right (start = left reaction).",
              "BMD from the SFD areas; check M = 0 at free/pinned ends."]),
 ),
 sec("Worked examples", (13, 36),
   ("ex", "Example 3.1 — gymnast P on a 5 m balance beam, 1.5 m from A", "R_A = 0.7P, R_B = 0.3P; M_max = 1.05P "
          "under the load. Case 2: general position x → M_max = P x(5 − x)/5."),
   ("ex", "Example 3.2 — engine crane boom (5 kN)", "Hydraulic cylinder is a two-force member at 68.2° → its "
          "force from ΣM_A (≈ 17.5 kN), pin A from force equations; SFD/BMD of the boom."),
   ("ex", "Chair frame ABC–BD (person on the seat)", "Replace by an equivalent FBD; M = 495 Nm at B."),
   ("ex", "Example 3.3 — RC pier cap (stringer loads 60/45 kN, self-weight 8 kN/m)", "Symmetric: reactions "
          "163.5 kN each; M = −136 kNm over the supports and −54.75 kNm at midspan (hogging throughout)."),
   ("ex", "Spliced timber beam (8 kN/m)", "V = 0 at 1.5 m from A → M_max(+) = 9 kNm; M = 0 at 3 m → **best "
          "location for the splice**."),
   ("ex", "Ski on snow (0.8 kN, trapezoidal reaction)", "Equilibrium → w = 0.533 kN/m, then SFD/BMD."),
   ("tut", "Tutorial 4 Q5(a) — beam with overhang and point loads: SFD/BMD, maxima and deflected shape. "
           "Q5(b) — aircraft wing as a tapered cantilever: reactions at the fuselage, SFD/BMD."),
 ),
]}

# ============================================================== M4 Bending stress
STUDY[M4] = {"code": "CE102", "title": "M4 · Stress & strain due to bending", "sections": [
 sec("Curvature & bending strain", (3, 7),
   ("md", "Plane sections remain plane and normal to the axis; the beam bends into a circular arc of radius ρ. "
          "Fibres above the neutral surface shorten, below lengthen (for +M)."),
   ("eq", r"\kappa = \frac{1}{\rho} = \frac{d\theta}{ds},\qquad \varepsilon_x = -\frac{y}{\rho} = -\kappa y"),
 ),
 sec("Normal stress, neutral axis & flexure formula", (8, 12),
   ("eq", r"\sigma_x = E\varepsilon_x = -E\kappa y"),
   ("md", "ΣF_x = 0 (pure bending) ⇒ ∫y dA = 0 ⇒ **neutral axis through the centroid** (linear elastic). "
          "ΣM = M gives the moment–curvature relation (EI = flexural rigidity):"),
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
   ("md", "Transform material 2 into material 1 by scaling **widths only** (depth unchanged); find the N.A. and "
          "I_t of the transformed section. Examples: timber + steel plate, concrete slab on steel beam, RC."),
 ),
 sec("Worked examples & applications", (21, 47),
   ("ex", "Example 4.1 — glued hollow timber box", "Top and bottom boards resist **85.9 %** of M (force resultant "
          "of the trapezoidal stress block × lever arm) → webs can be thinned."),
   ("ex", "Built-up 15 mm boards — two layouts for 150 kNm", "Compare section moduli; the larger S gives the lower "
          "stress."),
   ("ex", "Example 4.2 — diving board (80 kg at the tip)", "M_max = 1962 Nm at support B; T-shaped section: "
          "N.A. 11.4 mm from the top, I = 5.1 × 10⁵ mm⁴ → σ = Mc/I ≈ 43.9 MPa at that face (check the other face too)."),
   ("ex", "Example 4.3 — timber railway tie (70 kN rails, uniform ballast reaction 60.87 kN/m)", "M_max = 12.25 kNm "
          "→ required thickness t = 98.4 mm from σ_allow and S = bt²/6."),
   ("ex", "Composite concrete slab on steel I-beam (σ_c ≤ 15, σ_s ≤ 165 MPa)", "Transform concrete into steel "
          "(b/n); N.A. 177 mm/323 mm; check which material reaches its limit first — the smaller moment governs."),
   ("md", "Applications: aluminium truss girders (I by parallel-axis of the chord tubes), **castellated beams** "
          "(cut and re-weld an I-beam → deeper, stiffer for the same steel)."),
   ("tut", "Tutorial 4 Q6(a) — beam AB pinned at A and held by cable BC: combined axial + bending stress at "
           "section D."),
 ),
]}

# ============================================================== M5 Deflection
STUDY[M5] = {"code": "CE102", "title": "M5 · Deflection of beams", "sections": [
 sec("Elastic curve & direct integration", (3, 13),
   ("eq", r"\kappa \approx \frac{d^2y}{dx^2} \quad\Rightarrow\quad EI\,y'' = M(x),\quad EI\,y''' = V,\quad EI\,y'''' = -q"),
   ("steps", ["Write M(x) for each segment (one function per segment).",
              "Integrate twice: EIy′ = ∫M dx + C₁, EIy = ∫∫M + C₁x + C₂.",
              "Boundary conditions at supports (y = 0; y′ = 0 at fixed ends).",
              "Continuity of y and y′ where segments meet."]),
   ("ex", "Example 5.1 — garden bench (two equal loads P on overhangs a, span b)",
    "Three segments; BCs y = 0 at A and B, continuity of slope. Results: θ_A = Pab/2EI, "
    "δ_mid = Pab²/8EI (upward), δ_end = Pa²(2a + 3b)/6EI."),
 ),
 sec("Superposition", (14, 14),
   ("md", "EIy″ = M is **linear**, so deflections/slopes from separate load cases can be **added** (use standard "
          "tables)."),
   ("tut", "Tutorial 4 Q6(b) — span 3L with a point load at L and UDL over the last third: maximum deflection and "
           "its location (superposition or integration)."),
 ),
 sec("Moment-area method", (15, 23),
   ("eq", r"\theta_{B/A} = \int_A^B\frac{M}{EI}dx \qquad t_{B/A} = \int_A^B\frac{M}{EI}\,\bar{x}_B\,dx"),
   ("md", "1st theorem: change in slope between A and B = **area** of the M/EI diagram. 2nd theorem: deviation of B "
          "from the tangent at A = **first moment of that area about B**. Angles +ve anticlockwise; B to the right "
          "of A. Draw M/EI **by parts** (one diagram per load) to use standard shapes:"),
   ("md", "| Shape | Area | Centroid from the zero end |\n|---|---|---|\n| rectangle | bh | b/2 |\n"
          "| triangle | bh/2 | 2b/3 |\n| parabolic spandrel (y ∝ x²) | bh/3 | 3b/4 |\n| n-th degree spandrel | bh/(n+1) | "
          "(n+1)b/(n+2) |"),
 ),
 sec("Applications & examples", (24, 50),
   ("ex", "Onshore pipeline span (stainless steel, d_o = 330 mm, t = 6 mm, w = 1.4 kN/m)",
    "Treat one span as simply supported; M/EI diagram; t_B/A and t_C/A → midspan deflection; maximum span from the "
    "allowable deflection."),
   ("ex", "Example 5.3 — fibre-reinforced concrete beam (four-point bending)", "M/EI by parts; deflection at C from "
          "t_D/A and t_E/A; cross-check with a second measured deflection."),
   ("ex", "Example 5.4 — RC retaining wall (cantilever, 8.5 kN/m triangular pressure, 6 m)", "Base shear 153 kN, "
          "moment 306 kNm; M/EI is cubic → θ_A = area, δ_A = t_A/B."),
   ("ex", "Roller position so that δ_C = δ_D (overhang tip = max span deflection)", "Max in AB where slope = 0; "
          "equate the two expressions and solve the quadratic for a in terms of L."),
 ),
]}

# ============================================================== tutorials 1–4 (question index)
TUTORIALS = [
 (T1, 1, "Q1 Scoreboard on cable ABC — length for T ≤ 20 kN, drop ≤ 0.3 m", S1),
 (T1, 2, "Q2 Jib crane for a 6 kN engine — tie-rod force & pin reactions", S2),
 (T1, 3, "Q3 Water-tank tower under wind — minimal bracing, main-leg forces", S3),
 (T2, 1, "Q4 Pin-connected structure — rod BD tension, best position of D", S4),
 (T2, 2, "Q5 Traffic-light cable — minimum length for sag ≤ 1 m, T ≤ 1000 N", S4),
 (T2, 3, "Q6 Stacked blocks — maximum overhang", S2),
 (T3, 1, "Q1 Connecting rod allowable force; biaxial fabric strains", M1),
 (T3, 2, "Q2 Tapered plate elongation; hanging mine cable strains", M1),
 (T3, 3, "Q3 Minimum-weight two-bar truss; rigid bar on brass & aluminium rods", M1),
 (T4, 1, "Q4 Geared shafts; rod with distributed torque", M2),
 (T4, 2, "Q5 SFD/BMD — overhanging beam; aircraft wing", M3),
 (T4, 3, "Q6 Combined stress at a section; max deflection under combined loads", M5),
]

# ============================================================== CE2155 (continuation of CE1101)
C0 = "CE102/CE2155_0_Introduction.pdf"
C1 = "CE102/CE2155_1_MoM_Revision.pdf"
C2 = "CE102/CE2155_2_Shear_Stress.pdf"
C3 = "CE102/CE2155_3_Combined_Loading.pdf"
C4 = "CE102/CE2155_4_Stress_Strain_Transformation.pdf"

STUDY[C0] = {"code": "CE102", "title": "CE2155 0 · Course map", "sections": [
 sec("Where structural mechanics fits", (1, 8),
   ("md", "CE2155 continues CE1101: **transverse shear stress, combined loading, 2-D stress & strain "
          "transformation, column buckling and failure criteria** (60 %), plus concrete & steel materials (40 %). "
          "Static equilibrium in 3-D = 6 equations (ΣF = 0, ΣM = 0 in vector form); revise SFD/BMD of cantilevers "
          "and simply supported beams before starting."),
   ("eq", r"\sum\mathbf{F} = \mathbf{0},\qquad \sum\mathbf{M}_O = \mathbf{0}\quad(\text{6 scalar equations in 3-D})"),
 ),
]}

STUDY[C1] = {"code": "CE102", "title": "CE2155 1 · Mechanics of materials revision", "sections": [
 sec("Stress: normal, shear, 3-D state, complementary shear", (2, 5),
   ("md", "Average normal stress σ = P/A is accurate away from load points (**Saint-Venant's principle**). "
          "Average shear in double shear τ = F/(2A). The 3-D state has σx, σy, σz and τxy, τyz, τzx. "
          "**Complementary shear:** shear stresses on adjacent perpendicular faces are equal in magnitude and both "
          "point towards, or both away from, the common edge."),
   ("eq", r"\tau_{xy} = \tau_{yx},\quad \tau_{yz} = \tau_{zy},\quad \tau_{zx} = \tau_{xz}"),
 ),
 sec("Strain & stress–strain relations", (6, 15),
   ("md", "Normal strain = change in length per unit length; shear strain = change in the originally right angle "
          "(+ if the angle becomes smaller). Normal strains change volume, shear strains change shape. Engineering "
          "stress/strain use the original A₀ and L₀."),
   ("eq", r"\sigma = E\varepsilon,\qquad \nu = -\frac{\varepsilon_{lat}}{\varepsilon_{long}},\qquad \tau = G\gamma,\qquad G = \frac{E}{2(1+\nu)}"),
   ("ex", "Example 1 — steel bar, 80 kN, E = 200 GPa, ν = 0.32", "σ = P/A → ε = σ/E → δ = εL; lateral strain −νε "
          "gives the change of the cross-section dimensions."),
 ),
 sec("Axial load, torsion & bending revision", (16, 26),
   ("eq", r"\delta = \int\frac{P(x)}{A(x)E}dx \qquad \tau = \frac{T\rho}{J},\ \phi = \frac{TL}{GJ} \qquad \sigma = -\frac{My}{I}"),
   ("md", "Torsion formulae are for **circular** sections only (non-circular sections warp). Euler–Bernoulli "
          "assumptions: plane sections stay plane and perpendicular to the axis, negligible in-plane distortion, "
          "axis length unchanged → linear strain → (elastic) linear stress."),
   ("ex", "Example 2 — I of a built-up section", "Neutral axis by Σ(A·y)/ΣA, then I = Σ(bh³/12 + Ad²) — "
          "tabulate (an Excel layout is shown)."),
   ("ex", "Example 3 — simply supported I-beam under UDL", "M_max = 22.5 kNm at midspan; σ_max = Mc/I at the extreme "
          "fibre; check also the web–flange junction (σ = My_B/I)."),
 ),
 sec("SFD/BMD, elastic curve & moment–curvature", (27, 32),
   ("eq", r"\frac{dV}{dx} = w,\quad \frac{dM}{dx} = V \qquad \frac{1}{\rho} = \frac{M}{EI},\quad EI\frac{d^2v}{dx^2} = M"),
   ("md", "Signs here: upward load +, sagging moment +. Sketch the **elastic curve** to check the solution "
          "(supports, points of inflection where M = 0). Integrate with boundary conditions; discontinuity "
          "(Macaulay) functions handle partial UDLs and point loads."),
 ),
]}

STUDY[C2] = {"code": "CE102", "title": "CE2155 2 · Shear stress in beams", "sections": [
 sec("Transverse & longitudinal shear", (3, 6),
   ("md", "V produces transverse shear stress on the section; by complementary shear the same stress acts "
          "**longitudinally**. Three loose boards slide and each carries P/3; glued boards act as one deeper beam "
          "(much stiffer and stronger) — the glue carries the longitudinal shear. Shear exists because "
          "V = dM/dx: unequal M on the two faces of a slice must be balanced by shear on the cut."),
 ),
 sec("The shear formula", (7, 12),
   ("eq", r"\tau = \frac{VQ}{It},\qquad Q = \int_{A'}y\,dA = \bar{y}'A'"),
   ("md", "**A′** = the part of the section beyond the level considered (the part 'held on' by the shear); "
          "ȳ′ = distance from the N.A. to the centroid of A′; t = width at that level; I = whole section about "
          "the N.A."),
   ("eq", r"\text{Rectangle: } \tau = \frac{6V}{bh^3}\left(\frac{h^2}{4} - y^2\right),\qquad \tau_{max} = 1.5\frac{V}{bh}\ \text{at the N.A.}"),
   ("tip", "The formula assumes τ uniform across the width t — poor for wide, shallow sections and at abrupt "
           "width changes."),
 ),
 sec("Examples: circular sections & glued T-beam", (13, 16),
   ("ex", "Example 2 — solid shaft vs tube, V = 4 kN", "Q of the semicircle above the diameter (ȳ = 4c/3π); τ at "
          "mid-height of the solid shaft = 4V/3A, compared with V/A average; the tube has a higher peak."),
   ("ex", "Example 3 — T-beam from two 150 × 30 mm boards", "V_max = 19.5 kN; A′ = top board, t = 30 mm (glue "
          "width) → τ_glue = VQ/It ≈ 4.88 MPa (vs 2.17 MPa average)."),
 ),
 sec("Shear flow & fastener spacing", (17, 23),
   ("eq", r"q = \frac{VQ}{I}\ \ (\text{force per unit length}),\qquad s = \frac{F_{fastener}}{q_{per\ fastener\ line}}"),
   ("md", "Built-up beams need fasteners (glue, welds, bolts, nails, shear studs) to resist q. Split q between "
          "the number of fastener lines that hold A′ on."),
   ("ex", "T-beam (above)", "q = 146 kN/m — the glue must resist 146 kN per metre of beam."),
   ("ex", "Example 4 — nailed box beam, V = 80 N, nail capacity 30 N", "I = 2295 × 10³ mm⁴. At B: q = VQ/I = 1.18 "
          "N/mm shared by two nail lines (0.59 N/mm each) → s_B ≈ 51 mm; at C: 0.353 N/mm per line → s_C ≈ 85 mm."),
 ),
 sec("Thin-walled members", (24, 33),
   ("md", "In thin walls shear flow runs **along the wall** (normal component negligible). In an I-section it "
          "flows from the flange tips inward, down the web and out to the bottom tips. Use **centre-line "
          "dimensions** for I, Q."),
   ("eq", r"\text{Flange: } q = \frac{Vt\,d}{2I}x\ \ (\text{linear}),\qquad \text{Web: } q = \frac{Vt}{I}\left[\frac{db}{2} + \frac{1}{2}\left(\frac{d^2}{4} - y^2\right)\right]\ \ (\text{quadratic})"),
   ("md", "q varies **linearly** on segments perpendicular to V and **quadratically** on segments parallel/inclined "
          "to V; the web carries almost all of V, flange horizontal components cancel."),
   ("ex", "Example 5 — thin-walled box, V = 10 kN", "q_B = 0 (A′ = 0 at the corner point on the axis of symmetry), "
          "q_C and q_D from Q of the shaded areas, halved because two walls hold A′ on."),
 ),
]}

STUDY[C3] = {"code": "CE102", "title": "CE2155 3 · Combined loading", "sections": [
 sec("Superposition of P, T, M and V", (2, 3),
   ("md", "Valid while the material is linear elastic and geometry changes are small. Find the internal P, T, M, V "
          "**at the centroid of the section**, compute each stress at the point, then add."),
   ("eq", r"\sigma = \frac{P}{A} \pm \frac{M_zy}{I_z} \pm \frac{M_yz}{I_y} \qquad \tau = \frac{T\rho}{J} + \frac{VQ}{It}"),
 ),
 sec("2-D examples", (4, 7),
   ("ex", "Example 1 — member AB, point C at a top corner", "Internal forces at C: P = −16.45 kN, M = 32.89 kNm "
          "(sagging), V = 21.93 kN. At the top corner τ = 0 (Q = 0) and σ = −P/A − Mc/I (compression)."),
   ("ex", "Example 2 — 40 kN at the corner of a block", "Move the force to the centroid: axial 40 kN + two moments; "
          "superpose the three stress planes → largest 875 kPa compression at corner C."),
 ),
 sec("3-D loading with vector mechanics", (8, 16),
   ("eq", r"\mathbf{M}_O = \mathbf{r}\times\mathbf{F} = \begin{vmatrix}\mathbf{i} & \mathbf{j} & \mathbf{k}\\ r_x & r_y & r_z\\ F_x & F_y & F_z\end{vmatrix}"),
   ("ex", "Example 3 — 7.5 mm-radius rod fixed at C, 500 N and 800 N loads",
    "At section A: P = 500 N, V = 800 N, T = 11 200 N·cm, M = 8000 and 7000 N·cm. Point A on the neutral axis "
    "of the 8000 moment. Superpose: σ = 2.83 + 211.3 = 214.1 MPa, τ = 6.04 + 169 = 175.0 MPa."),
   ("md", "**The big picture:** equilibrium → internal actions → stress formulae → state of stress → Mohr's "
          "circle → maximum stresses → failure criteria; and strain → deflection (serviceability), buckling "
          "(stability)."),
 ),
]}

STUDY[C4] = {"code": "CE102", "title": "CE2155 4 · Stress & strain transformation", "sections": [
 sec("Plane stress & sign convention", (2, 4),
   ("md", "Why a chalk in torsion breaks on a **45° helix**: the maximum *tensile* stress acts at 45° to the axis. "
          "Plane stress keeps σx, σy, τxy (out-of-plane components zero). τxy is positive on a +x face in +y "
          "(or −x face in −y); θ positive anticlockwise."),
 ),
 sec("Transformation equations", (5, 11),
   ("eq", r"\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos2\theta + \tau_{xy}\sin2\theta"),
   ("eq", r"\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2}\sin2\theta + \tau_{xy}\cos2\theta \qquad \sigma_{y'} = \sigma_x + \sigma_y - \sigma_{x'}"),
   ("md", "Derived from equilibrium of a wedge cut at θ (forces = stress × area, not stresses)."),
   ("ex", "Example 1 — element rotated 30° clockwise", "θ = −30° in the equations; plotting σx′ against θ shows a "
          "max 54.6 MPa and min −84.6 MPa, and τ between ±69.6 MPa."),
 ),
 sec("Principal stresses & maximum in-plane shear", (12, 16),
   ("eq", r"\tan2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y} \qquad \sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}"),
   ("eq", r"\tau_{max,\,in\text{-}plane} = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2},\quad \sigma_{avg}\ \text{on those planes},\quad \theta_s = \theta_p \pm 45^\circ"),
   ("md", "No shear on principal planes. Example 2 (bar in tension): σ₁ = P/A, σ₂ = 0; τ_max = P/2A on 45° planes "
          "— why ductile bars show 45° slip lines."),
 ),
 sec("Mohr's circle for plane stress", (17, 23),
   ("eq", r"(\sigma_{x'} - \sigma_{avg})^2 + \tau_{x'y'}^2 = R^2,\qquad R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}"),
   ("steps", ["Centre C = (σ_avg, 0).", "Plot reference point A = (σx, τxy) with **τ positive downward** (notes' "
              "convention).", "Radius R = CA.", "A rotation θ of the element = **2θ** on the circle, same sense.",
              "σ₁, σ₂ where the circle meets the σ axis; τ_max = R at the top/bottom."]),
   ("ex", "Example 3", "Reference A(−8, −6); element rotated 30° anticlockwise → rotate CA by 60°."),
   ("ex", "Example 4 — point on a shaft", "A(−12, −6): centre −6, R = √(6² + 6²) = 8.49 → σ₁ = 2.49, σ₂ = −14.49 "
          "MPa."),
 ),
 sec("Absolute maximum shear stress", (24, 26),
   ("md", "Consider all three planes (σ₃ = 0 in plane stress):\n"
          "- σ₁, σ₂ **same sign** → τ_abs,max = σ_max/2 (out-of-plane!).\n"
          "- σ₁, σ₂ **opposite signs** → τ_abs,max = (σ₁ − σ₂)/2 (in-plane)."),
   ("ex", "Example 5 — thin pressure vessel", "Hoop and longitudinal stresses are principal and both tensile → "
          "τ_abs,max = σ_hoop/2."),
 ),
 sec("Generalised Hooke's law, plane strain & strain rosettes", (27, 38),
   ("eq", r"\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right],\qquad \gamma_{xy} = \frac{\tau_{xy}}{G}"),
   ("md", "**Plane strain** transforms exactly like plane stress with σ → ε and τ → γ/2 (Mohr's circle: γ/2 "
          "positive downward)."),
   ("eq", r"\varepsilon_{x'} = \frac{\varepsilon_x + \varepsilon_y}{2} + \frac{\varepsilon_x - \varepsilon_y}{2}\cos2\theta + \frac{\gamma_{xy}}{2}\sin2\theta"),
   ("md", "**Strain rosette:** three gauges a, b, c at known angles each give one equation εᵢ = εx cos²θᵢ + "
          "εy sin²θᵢ + γxy sinθᵢ cosθᵢ → solve for εx, εy, γxy → Mohr's circle → principal strains; then "
          "Hooke's law (σ₃ = 0) gives the principal stresses (Examples 7–8)."),
 ),
]}

C5 = "CE102/CE2155_5_Column_Buckling.pdf"
C6 = "CE102/CE2155_6_Material_Failure.pdf"

STUDY[C5] = {"code": "CE102", "title": "CE2155 5 · Column buckling", "sections": [
 sec("Stability & the critical load", (2, 5),
   ("md", "Equilibrium can be **stable** (returns when disturbed), **neutral** (stays displaced) or **unstable** "
          "(moves away). A slender compression member can fail by **buckling** (sudden, geometric) before the "
          "material fails. The **critical load P_cr** is the load at neutral equilibrium — find it from equilibrium "
          "in the *displaced* shape, not the original one."),
   ("ex", "Spring–bar model", "Two rigid bars of length L/2 with a lateral spring k: P tanθ balance with the "
          "spring force kLθ/2 for small θ → P_cr = kL/4. Below P_cr stable, above unstable; P_cr is the "
          "**bifurcation point**."),
 ),
 sec("Ideal pin-ended column — Euler load", (6, 11),
   ("md", "Ideal column: perfectly straight, load through the centroid, linear elastic. M = −Pv gives "
          "EI v″ + Pv = 0 (an eigenvalue problem); non-trivial solutions need sin(kL) = 0."),
   ("eq", r"P_{cr} = \frac{\pi^2EI}{L^2}\ (n = 1),\qquad \text{higher modes } P_n = \frac{n^2\pi^2EI}{L^2}"),
   ("eq", r"\sigma_{cr} = \frac{P_{cr}}{A} = \frac{\pi^2E}{(L/r)^2},\qquad r = \sqrt{I/A},\quad L/r = \text{slenderness ratio}"),
   ("md", "Same end conditions both ways → buckles about the **weak axis** (least I). Euler is valid only while "
          "σ_cr ≤ σ_Y (elastic buckling)."),
   ("ex", "Example 1 — W200×46 pin-ended column", "Check σ_cr about y–y against σ_Y = 250 MPa: σ_cr > σ_Y, so the "
          "steel **yields first** and P = σ_Y A governs."),
   ("tip", "Always check both: P_cr (each axis, with its own effective length) and the squash load σ_Y A — "
           "the smallest governs."),
 ),
 sec("End conditions & effective length", (12, 16),
   ("eq", r"P_{cr} = \frac{\pi^2EI}{(KL)^2}"),
   ("md", "| Ends | K | L_e |\n|---|---|---|\n| pinned–pinned | 1.0 | L |\n| fixed–free (cantilever) | 2.0 | 2L |\n"
          "| fixed–pinned | 0.7 | 0.7L |\n| fixed–fixed | 0.5 | 0.5L |\n\nL_e = distance between points of zero "
          "moment (inflection points). Cantilever: P_cr = π²EI/4L²."),
   ("ex", "Example 2 — 8 m column fixed at both ends, braced at mid-height about y–y (E = 200 GPa, σ_Y = 410 MPa)",
    "x–x: K = 0.5, L_e = 4 m → 1653 kN; y–y: fixed bottom, pinned at the brace, L_e = 0.7 × 4 = 2.8 m → **461 kN**; "
    "yield 1255 kN → buckling about y–y governs at 461 kN."),
 ),
 sec("Eccentric load & the secant formula", (17, 24),
   ("md", "A load at eccentricity e ≡ P + moment Pe. The column deflects from the start; the deflection grows "
          "without bound as P → P_cr, so yielding at mid-height usually governs first."),
   ("eq", r"v_{max} = e\left[\sec\left(\sqrt{\frac{P}{EI}}\frac{L}{2}\right) - 1\right]"),
   ("eq", r"\sigma_{max} = \frac{P}{A}\left[1 + \frac{ec}{r^2}\sec\left(\frac{L_e}{2r}\sqrt{\frac{P}{EA}}\right)\right]"),
   ("md", "ec/r² = **eccentricity ratio**; as it → 0 the curve tends to Euler. Solve for P by trial with "
          "σ_max = σ_Y."),
   ("ex", "Example 3 — column fixed at the base, braced in x at the top, e = 200 mm about x–x (σ_Y = 250 MPa)",
    "(1) Weak-axis Euler with fixed–pinned K = 0.7; (2) strong axis: fixed–free (K = 2, L_e = 8 m), secant formula "
    "with c = 105 mm, r_x = 89.9 mm, trial and error → **419 kN** governs."),
   ("tip", "Buckling is geometrically non-linear — superposition does not apply."),
 ),
]}

STUDY[C6] = {"code": "CE102", "title": "CE2155 6 · Material failure", "sections": [
 sec("Ductile materials & yield criteria", (2, 7),
   ("md", "Mild steel in tension: yield → necking → micro-voids coalesce → **cup-and-cone** fracture with ~45° "
          "shear lips. Ductile failure starts with **yielding**, which is shear-controlled. In multi-axial stress, "
          "compare with the uniaxial test via principal stresses σ₁, σ₂ (plane stress)."),
   ("md", "**Tresca (maximum shear stress):** yielding when τ_abs,max = σ_Y/2."),
   ("eq", r"\text{same sign: } |\sigma_1| \le \sigma_Y,\ |\sigma_2| \le \sigma_Y \qquad \text{opposite signs: } |\sigma_1 - \sigma_2| \le \sigma_Y"),
   ("md", "**von Mises (maximum distortion energy):** yielding when the distortion strain-energy density reaches "
          "its uniaxial-yield value."),
   ("eq", r"\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2 \le \sigma_Y^2"),
   ("md", "Tresca's hexagon lies inside the von Mises ellipse → Tresca is more conservative."),
   ("ex", "Example 1 — 5 mm-radius steel shaft, axial load + torque (σ_Y = 360 MPa)",
    "σ from P/A and τ = Tc/J at the surface → principal stresses of opposite sign. Tresca: |σ₁ − σ₂| > 360 → "
    "**fails**; von Mises: < 360² → **does not fail** — the stress point lies between the two criteria."),
 ),
 sec("Brittle materials", (8, 11),
   ("md", "Little or no yielding; sudden fracture governed by flaws. Weak in tension (cast iron, concrete: "
          "f_t ≈ 10 % of f_c)."),
   ("md", "**Maximum normal stress (Rankine):** fracture when the largest principal stress reaches σ_ult."),
   ("eq", r"|\sigma_1| \le \sigma_{ult},\qquad |\sigma_2| \le \sigma_{ult}"),
   ("ex", "Example 2 — cast-iron shaft, T = 400 Nm, σ_ult = 150 MPa", "Pure shear → σ₁ = −σ₂ = τ_max = 2T/(πc³). "
          "Set = 150 MPa → c = 11.9 mm."),
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
