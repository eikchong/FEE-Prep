"""CE103 tutorial questions (CE3155 Part 2, Tut 1–5: stiffness method and influence lines) as q blocks.
Statements are from the tutorial sheets in materials/CE103; answers from the official answer sheets unless marked.
Numbers are recomputed in tests/test_tutorial_answers.py."""
from utils.qblock import q
from utils.study_notes_ce103 import D


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


ANAQ = {}

ANAQ[D["T1"]] = {"code": "CE103", "title": "Analysis practice · Tut 1 Truss stiffness method", "sections": [
 sec("Q1–Q2", (1, 2),
   q("CE3155 Tut 1 Q1",
     r"A truss has a pin at A and rollers at B and C; AB is 2 m long with $\angle CAB = \angle CBA = 45^\circ$, and a "
     r"horizontal 1 kN load acts at C. All members have the same EA. (a) Using the stiffness method, find the reaction "
     r"at B. (b) Find the reactions at A and C without the stiffness method.",
     r"**(a) $Q_3 = 0$ — no reaction at B · (b) $V_C = 1\ \mathrm{kN}$, $V_A = -1\ \mathrm{kN}$, $H_A = -1\ "
     r"\mathrm{kN}$.**",
     r"Assemble $K$ from the three members ($EA/\sqrt2$ for the inclined ones, $EA/2$ for AB), partition into "
     r"$K_{uu}$, $K_{ku}$, solve $D_u$, then $Q_k = K_{ku}D_u$. Check by statics: moments about A give $V_C$.",
     figure="p. 1: truss with element numbers.")),
 sec("Q2 Six-member truss", (1, 2),
   q("CE3155 Tut 1 Q2",
     r"A truss is pinned at nodes a and c and roller supported at b, d and f; loads P act at d, e and f. All members "
     r"have the same EA; ae and ce are $\sqrt2\ \mathrm{m}$ long, the others 1 m. Find the reactions at node a.",
     r"**Horizontal 0.207P (to the right), vertical 1.207P (upwards).**",
     r"Number the free dofs first; use a spreadsheet for the matrix solve.", figure="p. 2: truss.")),
]}

ANAQ[D["T2"]] = {"code": "CE103", "title": "Analysis practice · Tut 2 Beam stiffness method", "sections": [
 sec("Q1 Two-span beam, 15 kN/m (two FEM choices)", (1, 2),
   q("CE3155 Tut 2 Q1",
     r"A two-span beam (constant EI) under 15 kN/m has a pin at node 1 and rollers at nodes 2 and 3. (a) Using the "
     r"first set of fixed-end moments given, draw the deformed shape and find the reaction at node 2. (b) Repeat with "
     r"the second set of fixed-end moments. How do the solutions differ?",
     r"**Both give the reaction at node 2 = 34.5 kN (3 + 31.5 in (a), −1.5 + 36 in (b)); rotations $EI^{-1}[-47.6,\ "
     r"41.1,\ -20.6]$ vs $EI^{-1}[-20.6,\ 41.1,\ -20.6]$ — in (b) the true rotation at node 1 is not known.**",
     r"In (b) the fixed-end system fixes node 2 only, so $D_1$ is not the real rotation of node 1.",
     figure="p. 1: beam and the two fixed-end moment sets.")),
 sec(r"Q2 3 m fixed–fixed beam with roller at 1 m, deflection limit 0.01 m at $x = 2\ \mathrm{m}$", (1, 2),
   q("CE3155 Tut 2 Q2",
     r"A 3 m beam (constant EI) is fixed at both ends and rests on a roller at $x = 1\ \mathrm{m}$. It carries 12 kN/m "
     r"over $0 \le x \le 1$ and a point load P at $x = 2.5\ \mathrm{m}$. A column sits under $x = 2\ \mathrm{m}$, so the "
     r"downward deflection there must stay below 0.01 m. With nodes at $x = 0, 1, 2, 3\ \mathrm{m}$, find the largest "
     r"allowable P.",
     r"**$P_{\max} = 0.4EI + 1.68\ \mathrm{kN}$** ($EI$ in $\mathrm{kNm^2}$).",
     r"Unlocked system with $D_3 = -0.01$: $\begin{bmatrix} -P/8 \\ 1 \\ -P/2 \end{bmatrix} = EI\begin{bmatrix} 8 & "
     r"2 & 0 \\ 2 & 8 & -6 \\ 0 & -6 & 24 \end{bmatrix}\begin{bmatrix} D_1 \\ D_2 \\ -0.01 \end{bmatrix}$; eliminate "
     r"$D_1$, $D_2$.")),
]}

ANAQ[D["T3"]] = {"code": "CE103", "title": "Analysis practice · Tut 3 Frame stiffness method", "sections": [
 sec("Q1 Two-member frame fixed at A and C", (1, 2),
   q("CE3155 Tut 3 Q1",
     r"A two-member frame is fixed at A and C and loaded as shown; for both members $AE/L = 200 \times 10^3\ "
     r"\mathrm{kN/m}$, $12EI/L^3 = 2 \times 10^3\ \mathrm{kN/m}$, $6EI/L^2 = 6 \times 10^3\ \mathrm{kN}$, $4EI/L = 24 "
     r"\times 10^3$ and $2EI/L = 12 \times 10^3\ \mathrm{kNm}$; member 2's global stiffness matrix is given. (a) Find "
     r"the unknown dofs at B. (b) Find the horizontal reaction at C. (c) Sketch the deformed shape.",
     r"**(a) $D_B = [7.02 \times 10^{-5}\ \mathrm{m},\ -2.53 \times 10^{-5}\ \mathrm{m},\ -1.56 \times 10^{-4}\ "
     r"\mathrm{rad}]$ · (b) $-60.8\ \mathrm{kN}$ · (c) joint B moves right and down and rotates clockwise, keeping the "
     r"135° angle between the members.**",
     r"$K_{uu} = 10^3\begin{bmatrix} 103 & 99 & -1.76 \\ 99 & 301 & -4.24 \\ -1.76 & -4.24 & 48 \end{bmatrix}$; (b) "
     r"$Q_C = 10^3[-2\ \ 0\ \ 6]\,D_u$ + the fixed-end reaction.", figure="p. 1: frame and member data.")),
 sec("Q2 Triangular welded frame using symmetry", (1, 2),
   q("CE3155 Tut 3 Q2",
     r"A triangular frame has AB = AD = 2 m, BC = CD = 1 m and $\angle ABC = \angle ADC = 45^\circ$; joints A, B and D "
     r"are welded. A distributed load w acts normal to AB and AD; B and D are pinned, C is on a roller; EA and EI are "
     r"the same for all members. Using the stiffness method without extra nodes: (a) find the nodal loads of the "
     r"unlocked system by fixed-end moments; (b) use symmetry to reduce the problem — give $Q_u$, $D_u$, $D_k$ and the "
     r"needed part of K; (c) with $EA = 1.2 \times 10^9\ \mathrm{N}$, $EI = 10^6\ \mathrm{Nm^2}$, $w = 1\ "
     r"\mathrm{kN/m}$, solve $D_u$ and sketch the deformed shape; (d) find the vertical reaction at D.",
     r"**(a) fixed-end loads $w/2$ (force) and $w/6$ (moment) at the joints · (b) unknowns $D_1$ (vertical movement "
     r"at A) and $D_2$ (rotation at D) · (c) $D_u = [-1.3 \times 10^{-6}\ \mathrm{m},\ 2.48 \times 10^{-5}\ "
     r"\mathrm{rad}]$ · (d) reaction at D = 851.6 (the sheet says kN; with $w = 1\ \mathrm{kN/m}$ it must be N, "
     r"≈ 0.85 kN).**",
     r"$K = \begin{bmatrix} \dfrac{AE}{2\sqrt2} + \dfrac{3EI}{\sqrt2} & \dfrac{3EI}{\sqrt2} \\ \dfrac{3EI}{\sqrt2} "
     r"& \dfrac{4EI}{\sqrt2} + 4EI \end{bmatrix}$. Symmetry halves the stiffness matrix.",
     figure="p. 2: triangular frame.")),
]}

ANAQ[D["T4"]] = {"code": "CE103", "title": "Analysis practice · Tut 4 Influence lines (qualitative)", "sections": [
 sec("Q1–Q2 Influence-line shapes", (1, 2),
   q("CE3155 Tut 4 Q1",
     r"A beam is pinned at A, with a roller at B 6 m away and an overhang of 3 m beyond B; C is midway between A and "
     r"B. Draw the influence lines for (a) the moment at C, (b) the reaction at B, (c) the shear at C.",
     r"**(a) $M_C$: 0 at A → +1.5 at C → 0 at B → −1.5 at the free end · (b) $R_B$: straight line from 0 at A through "
     r"1 at B to 1.5 at the free end · (c) $V_C$: 0 at A → −0.5 just left of C, jumps to +0.5 just right of C → 0 at "
     r"B → −0.5 at the free end.**",
     r"Müller-Breslau: release the action and give a unit displacement; the deflected shape is the influence line.",
     figure="p. 1: beam A–C–B with overhang.")),
 sec("Q2 Beam with an internal hinge (see Tut 5 Q1 for ordinates)", (1, 2),
   q("CE3155 Tut 4 Q2",
     r"A beam A–B–C–D–E–F–G (2 m spacings) has a roller at B, an internal hinge at D, a roller at E and a pin at G. "
     r"Draw the influence lines for the shear and moment at C and the shear at hinge D.",
     r"**A–D behaves as a beam on B and the hinge, so all three lines are zero beyond D · $V_C$: +0.5 at A, 0 at B, "
     r"−0.5 at $C^-$ / +0.5 at $C^+$, 0 at D · $M_C$: −1 at A, 0 at B, +1 at C, 0 at D · $V_D$: +0.5 at A, 0 at B, −0.5 at C, "
     r"−1 at D.**",
     r"D–G stands on its own (E and G), so a load right of D never reaches C.", figure="p. 1: beam A–G.")),
 sec("Q3 Critical load arrangements", (2, 2),
   q("CE3155 Tut 4 Q3",
     r"A beam is pinned at A, with a pin at B 8 m away, an internal hinge E 4 m beyond B and a pin at D 4 m further; "
     r"C is 4 m from A. It carries a dead load of 0.8 kN/m, a live load of 4 kN/m and a 20 kN live point load. Find "
     r"the quantitative influence lines for (a) the reaction at B, (b) the moment at C and (c) the maximum negative "
     r"shear at C, and the load arrangement that is most critical for each.",
     r"**(a) $R_{B,\max} = 87.6\ \mathrm{kN}$ (live load everywhere, point load at E) · (b) $M_{C,\max} = 72\ "
     r"\mathrm{kNm}$ (live load on A–B, point load at C) · (c) $V_{C,\min} = -23.6\ \mathrm{kN}$ (live load on A–C and "
     r"B–D, point load at $C^-$ or E).**",
     r"ILs: $R_B$ 0 → 1 (B) → 1.5 (E) → 0 (D), area 12 · $M_C$ 0 → 2 (C) → 0 (B) → −2 (E) → 0 (D), net area 0 · "
     r"$V_C$ 0 → −0.5 ($C^-$) | +0.5 ($C^+$) → 0 (B) → −0.5 (E) → 0 (D), net area −2. (a) $0.8 \times 12 + 4 \times 12 + 20 "
     r"\times 1.5$ · (b) $0 + 4 \times 8 + 20 \times 2$ · (c) $0.8 \times (-2) + 4 \times (-3) + 20 \times (-0.5)$. "
     r"Dead load acts everywhere; live load only where the IL has the sign you want.",
     figure="p. 2: beam A–C–B–E–D.", src="claude")),
]}

ANAQ[D["T5"]] = {"code": "CE103", "title": "Analysis practice · Tut 5 Influence lines (quantitative)", "sections": [
 sec("Q1–Q3", (1, 2),
   q("CE3155 Tut 5 Q1",
     r"For the hinged beam of Tutorial 4 Q2, find the ordinates of the influence lines for the shear and moment at C "
     r"and the shear at hinge D.",
     r"**$V_C$: 0.5, 0, −0.5 | 0.5, 0 at A, B, C, D · $M_C$: −1, 0, 1, 0 · $V_D$: 0.5, 0, −0.5, −1; all zero beyond "
     r"D.**",
     r"With x from A: $R_B = (6 - x)/4$ on A–D; $V_C = R_B - 1$ left of C, $R_B$ right of C."),
   q("CE3155 Tut 5 Q2",
     r"A simply supported 15 m beam AB with C 6 m from A is crossed by moving loads 9, 18, 27 and 9 kN at spacings of "
     r"0.9, 1.2 and 0.9 m. Find the maximum moment at C.",
     r"**$M_{C,\max} = 201\ \mathrm{kNm}$, with the 18 kN load at C.**",
     r"IL peak $6 \times 9/15 = 3.6$. 18 kN at C: $18 \times 3.6 + 27 \times 3.12 + 9 \times 2.76 + 9 \times 3.06 = "
     r"201.4$; 27 kN at C gives only 199.3.", figure="p. 1: beam and load train."),
   q("CE3155 Tut 5 Q3",
     r"A beam A–B–C–D–E (1 m spacings) is fixed at A, has an internal hinge at C and a roller at D. (a) Draw the "
     r"influence line for the positive moment at A by Müller-Breslau and find the maximum positive $M_A$ for 5 kN/m "
     r"live, 1 kN/m dead and a 2 kN live point load. (b) Draw the influence line for the reaction at D and find the "
     r"maximum $R_D$ for a dead load of x kN/m (x measured from A) and a 2 kN live point load.",
     r"**(a) IL: 0 at A, −2 at C, 0 at D, +2 at E → $M_{A,\max} = 7\ \mathrm{kNm}$ · (b) IL: 0 on A–C, 1 at D, 2 at E "
     r"→ $R_{D,\max} = 10.667\ \mathrm{kN}$.**",
     r"(a) Dead load everywhere: net IL area $-2 - 1 + 1 = -2$ → −2; live 5 kN/m on D–E (area 1) → 5; 2 kN at E → 4; "
     r"total 7. (b) The dead load varies linearly ($w = x$): $\int_2^4 x(x - 2)\,dx = 6.667$, plus $2 \times 2 = 4$.",
     figure="p. 2: beam A–E.")),
]}
