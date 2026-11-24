"""CE103 Structural Analysis — CE3155 (Part 1 Elliot Law: classical methods; Part 2 Poh Leong Hien: stiffness
method & influence lines). Tutorial answers from the official answer sheets."""


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


A = "CE103/CE3155/"
T = A + "tutorials/"
D = {
    "P0": A + "P1-0 SFD and BMD.pdf", "P2a": A + "P1-2a Determinacy.pdf", "P2b": A + "P1-2b Stability.pdf",
    "P3": A + "P1-3 Virtual work.pdf", "P4": A + "P1-4 Force method.pdf", "P5": A + "P1-5 Slope-deflection.pdf",
    "P6": A + "P1-6 Plastic analysis of continuous beams.pdf",
    "Q0": A + "P2-0 Introduction.pdf", "Q1": A + "P2-1 Truss analysis.pdf", "Q2": A + "P2-2 Beam analysis.pdf",
    "Q3": A + "P2-3 Frame analysis.pdf", "Q4": A + "P2-4 Influence lines.pdf", "Q5": A + "P2-5 Influence lines II.pdf",
    "T1": T + "Tut 1.pdf", "T2": T + "Tut 2.pdf", "T3": T + "Tut 3.pdf", "T4": T + "Tut 4.pdf", "T5": T + "Tut 5.pdf",
}
OUTLINE = [("P0", 71, 1, ["CE103-07"]), ("P2a", 29, 2, ["CE103-02"]), ("P2b", 37, 3, ["CE103-02"]),
           ("P3", 95, 4, ["CE103-01"]), ("P4", 61, 5, ["CE103-02"]), ("P5", 118, 6, ["CE103-04"]),
           ("P6", 66, 7, ["CE103-06"]), ("Q0", 22, 8, ["CE103-02", "CE103-07"]), ("Q1", 58, 9, ["CE103-08"]),
           ("Q2", 34, 10, ["CE103-08"]), ("Q3", 48, 11, ["CE103-08"]), ("Q4", 28, 12, ["CE103-03"]),
           ("Q5", 28, 13, ["CE103-03"]), ("T1", 2, 21, ["CE103-08"]), ("T2", 2, 22, ["CE103-08"]),
           ("T3", 2, 23, ["CE103-08"]), ("T4", 2, 24, ["CE103-03"]), ("T5", 2, 25, ["CE103-03"])]

ANA = {}

ANA[D["P0"]] = {"code": "CE103", "title": "Analysis 0 · Shear force & bending moment diagrams", "sections": [
 sec("Internal forces & sign convention", (1, 22),
   ("md", "Cut the member, draw the free body, solve N, V, M by equilibrium. Positive convention: sagging M, shear "
          "that rotates the segment clockwise."),
 ),
 sec("Load–shear–moment relations", (23, 42),
   ("eq", r"\frac{dV}{dx} = -w(x),\qquad \frac{dM}{dx} = V,\qquad \Delta V = -\int w\,dx,\quad \Delta M = \int V\,dx"),
   ("md", "M is maximum where V = 0; point loads jump V; point moments jump M; UDL → parabolic M."),
 ),
 sec("Frames", (43, 71),
   ("md", "Draw BMD on the tension side member by member; at rigid joints moments balance."),
 ),
]}

ANA[D["P2a"]] = {"code": "CE103", "title": "Analysis 1 · Determinacy", "sections": [
 sec("Trusses", (4, 10),
   ("eq", r"\text{planar truss: } i = m + r - 2j\quad(i = 0 \text{ determinate},\ i > 0 \text{ indeterminate to degree } i)"),
 ),
 sec("Beams & frames", (11, 29),
   ("eq", r"\text{beams/frames: } i = 3m + r - 3j - c\quad(c = \text{conditions released at internal hinges})"),
   ("md", "Alternative: cut back to a stable determinate tree and count released restraints. Indeterminate "
          "structures need compatibility (force or displacement methods)."),
 ),
]}

ANA[D["P2b"]] = {"code": "CE103", "title": "Analysis 2 · Stability", "sections": [
 sec("Internal & external stability", (4, 8),
   ("md", "A structure is unstable if it can move as a mechanism without deforming. Counting (r < 3 or i < 0) is "
          "necessary but not sufficient."),
 ),
 sec("Classes of instability", (9, 23),
   ("md", "**Partial constraint** (too few reactions); **improper constraint** (reactions all concurrent or all "
          "parallel); **collapse mechanism** (internal hinges aligned). Check geometry, not only counts."),
 ),
 sec("Determinacy vs stability & exercises", (24, 37),
   ("md", "Unknowns < equations → unstable; unknowns ≥ equations is stable only if constraints are proper."),
 ),
]}

ANA[D["P3"]] = {"code": "CE103", "title": "Analysis 3 · Virtual work (unit load method)", "sections": [
 sec("Work & energy", (6, 14),
   ("md", "External work ½PΔ = internal strain energy (real work, one load only)."),
 ),
 sec("Principle of virtual work", (15, 30),
   ("eq", r"1\cdot\Delta = \sum\frac{nNL}{AE}\ (\text{trusses}),\qquad 1\cdot\Delta = \int\frac{mM}{EI}dx,\qquad 1\cdot\theta = \int\frac{m_\theta M}{EI}dx"),
   ("md", "Apply a virtual unit load (or moment) at the point and in the direction of the wanted displacement; "
          "n, m are internal forces from it, N, M from the real loads."),
 ),
 sec("Trusses, beams & frames", (31, 95),
   ("md", "Trusses: tabulate n, N, L per member (temperature: Δ = Σnα ΔT L; fabrication error: Σn ΔL). Beams/frames: "
          "use the product-integral table (e.g. ∫ rectangle × triangle = ½ab L, triangle × triangle same sign = ⅓abL, "
          "parabola etc.)."),
 ),
]}

ANA[D["P4"]] = {"code": "CE103", "title": "Analysis 4 · Force (flexibility) method", "sections": [
 sec("Principle", (4, 10),
   ("eq", r"\Delta_{1P} + f_{11}X_1 + f_{12}X_2 + \dots = 0,\qquad f_{ij} = \int\frac{m_im_j}{EI}dx\ (\text{Maxwell: } f_{ij} = f_{ji})"),
   ("md", "Release redundants to get a determinate primary structure, compute displacements there, enforce "
          "compatibility to solve for the redundants, superpose."),
 ),
 sec("Beams, frames, trusses", (11, 61),
   ("md", "Choose redundants that keep the primary structure stable and the integrals easy. Trusses use "
          "f = ΣnnL/AE. Supports settlement: right-hand side equals the known displacement."),
 ),
]}

ANA[D["P5"]] = {"code": "CE103", "title": "Analysis 5 · Slope-deflection method", "sections": [
 sec("Deflected shapes", (6, 25),
   ("md", "Sketch the deflected shape first: rotations at joints, sway in unbraced frames, inflection points."),
 ),
 sec("Slope-deflection equations & fixed-end moments", (26, 41),
   ("eq", r"M_{AB} = \frac{2EI}{L}\left(2\theta_A + \theta_B - 3\psi\right) + FEM_{AB},\qquad \psi = \frac{\Delta}{L}"),
   ("eq", r"\text{Pin at far end: } M_{AB} = \frac{3EI}{L}(\theta_A - \psi) + FEM'_{AB};\qquad FEM_{UDL} = \frac{wL^2}{12},\ FEM_{P,mid} = \frac{PL}{8}"),
 ),
 sec("Beams", (42, 61),
   ("md", "Unknowns: joint rotations; equations: ΣM = 0 at each joint. Then end moments → shears → BMD."),
 ),
 sec("Frames without and with sidesway", (62, 118),
   ("md", "Sway frames add Δ as an unknown and a **shear (storey) equation**: Σ column shears = applied horizontal "
          "load, column shear V = −(M_top + M_bot)/h."),
 ),
]}

ANA[D["P6"]] = {"code": "CE103", "title": "Analysis 6 · Plastic analysis of continuous beams", "sections": [
 sec("Plastic hinge & section properties", (6, 34),
   ("eq", r"M_p = f_yW_{pl},\qquad f = \frac{W_{pl}}{W_{el}}\ (\text{rectangle } 1.5,\ \text{I-section} \approx 1.12)"),
 ),
 sec("Kinematic (mechanism) method", (35, 51),
   ("md", "Assume hinge positions, give a virtual rotation θ, equate external work Σ P δ to internal work Σ M_p θ_i. "
          "The upper-bound theorem: the true collapse load is the **lowest** of all mechanism loads."),
   ("eq", r"\text{fixed-ended beam, UDL: } w_c = \frac{16M_p}{L^2};\qquad \text{propped cantilever, UDL: } w_c \approx \frac{11.66M_p}{L^2}"),
 ),
 sec("Continuous beams", (52, 66),
   ("md", "Check a beam mechanism in each span (hinges at supports and under/near the loads); the governing span gives "
          "the collapse load. Then check M ≤ M_p everywhere (equilibrium check)."),
 ),
]}

ANA[D["Q0"]] = {"code": "CE103", "title": "Analysis 7 · Part 2 introduction: idealisation & determinacy", "sections": [
 sec("Idealisation, determinacy, stability", (1, 22),
   ("md", "Pin-jointed trusses, rigid frames; supports (pin 2, roller 1, fixed 3 reactions). Statically "
          "indeterminate → use the stiffness (displacement) method in matrix form."),
 ),
]}

ANA[D["Q1"]] = {"code": "CE103", "title": "Analysis 8 · Truss analysis by the stiffness method", "sections": [
 sec("Member stiffness & transformation", (18, 34),
   ("eq", r"\mathbf k' = \frac{AE}{L}\begin{bmatrix}1 & -1\\ -1 & 1\end{bmatrix},\qquad \mathbf k = \mathbf T^T\mathbf k'\mathbf T = \frac{AE}{L}\begin{bmatrix}\lambda_x^2 & \lambda_x\lambda_y & -\lambda_x^2 & -\lambda_x\lambda_y\\ & \lambda_y^2 & -\lambda_x\lambda_y & -\lambda_y^2\\ & & \lambda_x^2 & \lambda_x\lambda_y\\ \text{sym} & & & \lambda_y^2\end{bmatrix}"),
   ("md", "λ_x = cos θ_x, λ_y = cos θ_y from the near to the far node."),
 ),
 sec("Assembly & solution", (35, 58),
   ("eq", r"\begin{bmatrix}\mathbf Q_k\\ \mathbf Q_u\end{bmatrix} = \begin{bmatrix}\mathbf K_{11} & \mathbf K_{12}\\ \mathbf K_{21} & \mathbf K_{22}\end{bmatrix}\begin{bmatrix}\mathbf D_u\\ \mathbf D_k\end{bmatrix}\ \Rightarrow\ \mathbf D_u = \mathbf K_{11}^{-1}(\mathbf Q_k - \mathbf K_{12}\mathbf D_k),\quad \mathbf Q_u = \mathbf K_{21}\mathbf D_u + \mathbf K_{22}\mathbf D_k"),
   ("md", "Number unknown dofs first. Member force q = (AE/L)[−λ_x −λ_y λ_x λ_y]·D."),
 ),
]}

ANA[D["Q2"]] = {"code": "CE103", "title": "Analysis 9 · Beam analysis by the stiffness method", "sections": [
 sec("Beam member stiffness", (1, 20),
   ("eq", r"\mathbf k = \frac{EI}{L^3}\begin{bmatrix}12 & 6L & -12 & 6L\\ 6L & 4L^2 & -6L & 2L^2\\ -12 & -6L & 12 & -6L\\ 6L & 2L^2 & -6L & 4L^2\end{bmatrix}\quad(\text{dofs } v_1, \theta_1, v_2, \theta_2)"),
 ),
 sec("Intermediate loads (fixed-end forces)", (21, 34),
   ("md", "Superpose: (a) fixed-end system with FEMs/FEFs, (b) unlocked system with equivalent nodal loads = −(fixed-end "
          "reactions). Final member forces = (a) + (b)."),
 ),
]}

ANA[D["Q3"]] = {"code": "CE103", "title": "Analysis 10 · Plane frame analysis by the stiffness method", "sections": [
 sec("Frame member (6 dofs) & transformation", (1, 16),
   ("md", "Combine the axial (AE/L) and flexural (12EI/L³, 6EI/L², 4EI/L, 2EI/L) terms in local axes, then rotate "
          "with T (λ_x, λ_y). Watch units (kN, m, kNm)."),
 ),
 sec("Worked examples & internal forces", (17, 48),
   ("md", "Solve D_u, reactions Q_u, then member end forces q = k′TD (+ fixed-end forces). Check with FBDs."),
 ),
]}

ANA[D["Q4"]] = {"code": "CE103", "title": "Analysis 11 · Influence lines (determinate beams)", "sections": [
 sec("Construction", (1, 14),
   ("md", "Influence line = value of a response (reaction, V or M at a point) as a **unit load** moves across. "
          "Tabulate or write equations; for determinate beams the IL is piecewise linear."),
 ),
 sec("Using influence lines", (15, 19),
   ("md", "Point load: P × ordinate. UDL: w × area under the IL over the loaded length (load only the positive or "
          "negative region for the max)."),
 ),
 sec("Müller-Breslau (qualitative)", (20, 28),
   ("md", "Remove the restraint corresponding to the response and impose a unit displacement in its positive "
          "direction — the deflected shape is the influence line (to scale for determinate structures)."),
 ),
]}

ANA[D["Q5"]] = {"code": "CE103", "title": "Analysis 12 · Influence lines II: moving load series", "sections": [
 sec("Maximum effect of a series of loads", (1, 28),
   ("md", "Trial positions with one load at the peak ordinate, or use the change rules: move the group until ΔV or "
          "ΔM changes sign — for moment, ΔM = Σ(P × slope change × distance). The position giving the largest value "
          "is critical."),
 ),
]}

# ------------------------------------------------------------------ tutorials (official answer sheets)
ANA[D["T1"]] = {"code": "CE103", "title": "Analysis practice · Tut 1 Truss stiffness method", "sections": [
 sec("Q1–Q2", (1, 2),
   ("ex", "Answers", "Q1 (three-member truss, 1 kN at C): stiffness solution → Q₃ = 0 at B; by statics V_C = 1 kN, "
          "V_A = −1 kN, H_A = −1 kN · Q2 (six-member truss, loads P at d, e, f): reaction at node a: horizontal "
          "**0.207P** (right), vertical **1.207P** (up)."),
 ),
]}

ANA[D["T2"]] = {"code": "CE103", "title": "Analysis practice · Tut 2 Beam stiffness method", "sections": [
 sec("Q1 Two-span beam, 15 kN/m (two FEM choices)", (1, 2),
   ("ex", "Answers", "Both fixed-end systems give the same **reaction at node 2 = 34.5 kN** (3 + 31.5 or −1.5 + 36); "
          "rotations D = EI⁻¹[−47.6, 41.1, −20.6] vs [−20.6, 41.1, −20.6] — the second system leaves node 1's true "
          "rotation unknown."),
 ),
 sec("Q2 3 m fixed–fixed beam with roller at 1 m, deflection limit 0.01 m at x = 2 m", (1, 2),
   ("ex", "Answer", "Set D₃ = −0.01 m in the unlocked system → **P_max = 0.4EI + 1.68 kN**."),
 ),
]}

ANA[D["T3"]] = {"code": "CE103", "title": "Analysis practice · Tut 3 Frame stiffness method", "sections": [
 sec("Q1 Two-member frame fixed at A and C", (1, 2),
   ("ex", "Answers", "D_B = [7.02 × 10⁻⁵ m, −2.53 × 10⁻⁵ m, −1.56 × 10⁻⁴ rad] · horizontal reaction at C = **−60.8 kN**."),
 ),
 sec("Q2 Triangular welded frame using symmetry", (1, 2),
   ("ex", "Answers", "Unknowns D₁, D₂ only; D_u = [−1.3 × 10⁻⁶ m, 2.48 × 10⁻⁵ rad]; reaction at D = **851.6 kN** (for the "
          "given w). Use symmetry to halve the stiffness matrix."),
 ),
]}

ANA[D["T4"]] = {"code": "CE103", "title": "Analysis practice · Tut 4 Influence lines (qualitative)", "sections": [
 sec("Q1–Q3", (1, 2),
   ("md", "Draw ILs for M_C, R_B, V_C on an overhanging beam; V_C, M_C and V at an internal hinge D; then for a beam "
          "with dead 0.8 kN/m, live 4 kN/m and a 20 kN live point load find the critical arrangements (live load only "
          "on regions of the same sign). Answers are sketches — see the answer sheet."),
 ),
]}

ANA[D["T5"]] = {"code": "CE103", "title": "Analysis practice · Tut 5 Influence lines (quantitative)", "sections": [
 sec("Q1–Q3", (1, 2),
   ("ex", "Answers", "Q2 moving loads: **M_C,max = 201 kNm** · Q3 (fixed at A, hinge at C, roller at D; Müller-Breslau): "
          "**M_A,max = 7 kNm** (5 kN/m live + 1 kN/m dead + 2 kN live) · **R_D,max = 10.667 kN**."),
 ),
]}
