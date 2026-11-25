"""Formula & code-sheet content built from the lecture notes, in lecture order.

Every entry cites (doc, page) — page = PDF page of the file in materials/. Notes predate the
Eurocodes in places: superseded British/SS standards are flagged; methods that are not acceptable
in FEE 2027 are marked legacy=True (kept out of the sheet, listed separately).
"""
from utils.formulas import F

D101 = "CE101/CE101_Mechanics_of_Materials.pdf"


def S(title, doc, page, items):
    return {"title": title, "src": {"doc": doc, "page": page}, "items": items}


CE101 = [
 S("1 · Strength, stiffness & deformability", D101, 2, [
   F("Theoretical cohesive strength", r"\sigma_{th} = \sqrt{\frac{E\gamma_s}{r_0}} \approx \frac{E}{10}",
     note=r"$\gamma_s$ surface energy, $r_0$ atomic spacing; real strengths 2–3 orders lower because of flaws", src=(D101, 2)),
   F("Griffith fracture strength", r"\sigma_f = \sqrt{\frac{2E\gamma_s}{\pi c}}",
     note=r"c = half crack length → $\sigma_f \propto 1/\sqrt{c}$; steel $E \approx 200\ \mathrm{GPa}$, "
          r"$\mathrm{UTS} \approx 500\ \mathrm{MPa}$; concrete E 20–40 GPa, $f_c$ 20–60, $f_t$ 2–6 MPa",
     src=(D101, 2)),
   F("Hooke's law; stiffness vs deformability", r"\sigma = E\varepsilon",
     note="stiffness ∝ E; deformability = elastic + plastic strain to fracture; strain energy/vol = area "
          r"under $\sigma\text{–}\varepsilon$; hysteresis loop = energy not recovered", src=(D101, 3)),
   F("Poisson's ratio & volume change", r"\nu = -\frac{\varepsilon_{lat}}{\varepsilon_{ax}},\quad \frac{\Delta V}{V} \approx \varepsilon(1 - 2\nu)",
     note=r"$\nu \approx 0.15$ concrete/wood, 0.33 metals, 0.5 rubber; size effect: larger specimens → lower "
          "fracture strength",
     src=(D101, 4)),
 ]),
 S("2 · Ductile–brittle behaviour, creep & relaxation", D101, 5, [
   F("Ductile–brittle transition",
     note="Brittle favoured by low temperature, high loading rate and triaxiality (yield stress rises faster than "
          "fracture stress); ductile materials absorb more fracture energy", src=(D101, 5)),
   F("Creep stages",
     note="Primary (decreasing rate) → secondary (steady) → tertiary → rupture; metals: dislocation movement; "
          "concrete: movement of gel water; drying + loading together > sum of the two (drying creep)",
     src=(D101, 6)),
   F("Creep vs relaxation",
     note="Creep = strain ↑ under constant stress; relaxation = stress ↓ under constant strain (e.g. PSC tendons)",
     src=(D101, 6)),
 ]),
 S("3 · Fatigue", D101, 7, [
   F("Fatigue cycle parameters",
     r"\sigma_m = \frac{\sigma_{max} + \sigma_{min}}{2},\quad \sigma_a = \frac{\sigma_{max} - \sigma_{min}}{2},\quad \Delta\sigma = 2\sigma_a,\quad R = \frac{\sigma_{min}}{\sigma_{max}}",
     note="initiation at stress raisers → propagation (tension/shear, not compression)", src=(D101, 7)),
   F("Factors affecting fatigue",
     note="Amplitude dominates; tensile mean stress lowers life; frequency minor below ~1000 cps; cumulative "
          "damage; notches/surface finish. No fatigue limit for concrete (modified Goodman diagram, $10^7$ "
          "cycles)",
     src=(D101, 8)),
 ]),
 S("4 · Steel metallurgy", D101, 10, [
   F("Composition",
     note="Structural steel < 0.30 % C (max 2 % in steel); Mn raises strength, lowers ductility; low-alloy: "
          "Ni, Cr, Mo < 8 %",
     src=(D101, 11)),
   F(r"$\mathrm{Fe}\text{–}\mathrm{Fe_3C}$ phase diagram",
     note="Eutectoid 727 °C / 0.80 % C. Slow cooling → ferrite + pearlite; quenching → martensite (hard, "
          r"brittle) → temper. Carbon solubility: austenite 2.0 %, $\delta$-iron 0.10 %, ferrite 0.025 %; "
          r"cementite $\mathrm{Fe_3C}$ 6.7 % C",
     src=(D101, 12)),
   F("Allotropy of iron", note=r"$\delta$-iron (BCC) → austenite $\gamma$ (FCC, larger interstices) → ferrite "
                               r"$\alpha$ (BCC)", src=(D101, 13)),
 ]),
 S("5 · Strengthening & weldability", D101, 14, [
   F("Strengthening mechanisms",
     note="Alloying (interstitial/substitutional), grain refinement (heat treatment), strain hardening (cold work — "
          "lost on heating, e.g. welding); all reduce ductility", src=(D101, 14)),
   F("Carbon equivalent", r"CE = C + \frac{Mn}{6} + \frac{Cr + Mo + V}{5} + \frac{Cu + Ni}{15}",
     note="higher CE → harder HAZ, hydrogen cracking risk, more preheat; HAZ properties depend on parent "
          "composition, grain size and cooling rate", src=(D101, 14)),
   F("Weldability limit — check", src=("CE103/CE103_Structural_Analysis.pdf", 11), verify=True,
     note=r"Your handwritten '$\mathrm{CE} < 0.25\,\%$' is likely the carbon-content limit; the bar spec on p. "
          r"17 gives $\mathrm{CE} \le 0.42\text{–}0.51$"),
   F("Steel specifications", note="Notes cite BS 4360 (now SS EN 10025) and BS 5950 (now SS EN 1993) — use the EN standards",
     src=(D101, 15)),
 ]),
 S("6 · Reinforcement & prestressing steel", D101, 16, [
   F("Effective area & nominal diameter of a deformed bar",
     r"A = \frac{M}{0.00785L}\ \mathrm{mm^2},\quad \phi = \sqrt{\frac{4A}{\pi}}",
     note=r"M = mass (kg), L = length (m, ≥ 0.5 m); steel density $7850\ \mathrm{kg/m^3}$", src=(D101, 16)),
   F("Reinforcement grade today",
     note=r"Notes give BS 4449 G250/G460 and $\mathrm{CE} \le 0.42/0.51$ — superseded: FEE 2027 uses B500 (SS "
          r"560 / EN 10080, $f_{\mathrm{yk}} = 500\ \mathrm{N/mm^2}$)", src=(D101, 17), verify=True),
   F("Steel at high temperature", note="Strength drops markedly above ~300 °C; cold-worked bars lose strength faster",
     src=(D101, 17)),
 ]),
 S("7 · Corrosion", D101, 18, [
   F("Passivation", note=r"$\mathrm{pH} > 12$ pore solution keeps the oxide film; lost by carbonation or "
                         "chloride ingress",
     src=(D101, 18)),
   F("Forms of corrosion", note="General, pitting (chlorides), galvanic, stress corrosion (PSC tendons), crevice",
     src=(D101, 18)),
   F("Corrosion control",
     note="Coatings (paint, epoxy); galvanising (barrier + sacrificial zinc); cathodic protection (impressed current); "
          "weathering steels (Cu, P, Cr, Ni, Si self-healing oxide)", src=(D101, 19)),
 ]),
 S("8 · Concrete vs steel — engineering properties", D101, 21, [
   F("Key values",
     note=r"Density 2000–2400 (normal), 300–1850 (LW), 3000–5600 (HW) vs $7830\ \mathrm{kg/m^3}$; $\alpha "
          r"\approx 10$ vs $12 \times 10^{-6}\ \mathrm{K^{-1}}$; E 20–60 vs 180–200 GPa; $\nu$ 0.15–0.20 vs "
          r"0.30; $\varepsilon_{\mathrm{cu}}$ 0.0035, $\varepsilon_{\mathrm{ct}}$ 0.0002", src=(D101, 21)),
   F("Concrete as a composite",
     note="Cement-paste matrix + aggregate; interfacial transition zone is the weakest link; bond cracks arrested by "
          "aggregate → quasi-ductile behaviour", src=(D101, 22)),
 ]),
 S("9 · Cement & hydration", D101, 23, [
   F("Cement types",
     note="OPC, RHPC (Type III), LHPC (IV), SRPC (V), blastfurnace & PFA blends; strength classes L/N/R. "
          "BS 12 / SS 26 superseded by SS EN 197-1 (CEM I–V, 32.5/42.5/52.5)", src=(D101, 24)),
   F("Hydration water", note=r"Full hydration needs $w/c \approx 0.20\text{–}0.24$; capillary pores persist if "
                             r"$w/c > 0.36\text{–}0.38$",
     src=(D101, 26)),
   F("Rate of hydration", note=r"$\mathrm{C_3S}$ fast (early strength); $\mathrm{C_2S}$ slow (later); "
                               "pfa/silica fume pozzolanic; ggbs latent hydraulic",
     src=(D101, 27)),
   F("Alkali content", r"Na_2O_{eq} = Na_2O + 0.658K_2O",
     note="< 0.60 % for low-alkali cement (ASR control); > 70 °C curing → delayed ettringite formation", src=(D101, 25)),
   F("Hydration stops when", note=r"$T < -10^\circ\mathrm{C}$, RH < ~80 % (negligible < 30 %), $w/c < "
                                  r"0.20\text{–}0.25$ → need for curing",
     src=(D101, 29)),
   F("SCM replacement for low heat", note="25–30 % pfa or 60–70 % ggbs; slower strength gain, ≥ 7 days moist curing",
     src=(D101, 30)),
 ]),
 S("10 · Water", D101, 34, [
   F("Roles of water",
     note="Chemical w/c 0.20–0.25; physical space ~0.36; workability > 0.36; excess → capillary pores, permeability, "
          "shrinkage", src=(D101, 35)),
   F("Mixing-water quality", note="Potable water OK (dissolved solids < 2000 ppm); no sulfates in curing water",
     src=(D101, 36)),
 ]),
 S("11 · Aggregates", D101, 37, [
   F("Classification", note="Fine/coarse split at 5 mm; 60–80 % of concrete volume; LW / normal / HW",
     src=(D101, 38)),
   F("Moisture states", note="Oven-dry → air-dry → SSD (absorption) → wet (free water). Total = free + absorbed",
     src=(D101, 40)),
   F("Fineness modulus", r"FM = \frac{\sum \%\ \mathrm{cumulative\ retained}\ (150\,\mu m \to D_{max})}{100}",
     note=r"$\Delta FM$ of 0.2 can change water demand noticeably", src=(D101, 44)),
   F("Tests", note="ACV, 10 % fines, AIV, abrasion, Los Angeles; alkali–silica/carbonate reactivity; chlorides, sulfates",
     src=(D101, 39)),
 ]),
 S("12 · Chemical admixtures", D101, 46, [
   F("Three ways to use a plasticiser",
     note="Plasticising (same w/c, higher slump); water-reducing (same slump, lower w/c, higher strength); "
          "cement-saving (same w/c & slump, less cement)", src=(D101, 48)),
   F("Acceptance (normal water reducer)",
     note="≥ 8 % water reduction, strength ≥ 110 % of control; retarders delay stiffening ≥ 1 h. "
          "SS 320 / BS 5075 → SS EN 934-2", src=(D101, 49)),
   F("Efficiency", note=r"Reduced by finer cement, higher alkali and $\mathrm{C_3A}$ content, and higher "
                        "concrete temperature",
     src=(D101, 50)),
 ]),
 S("13 · Mix design & strength", D101, 51, [
   F("k-value (efficiency) concept", r"\left(\frac{w}{c}\right)_{eff} = \frac{W}{C + kA}",
     note=r"silica fume $k \approx 3$ (OPC, 28 d); EN 206 $k = 2.0$ for silica fume; ggbs/pfa $k < 1$ to 28 d", src=(D101, 52)),
   F("Target mean strength", r"f_m = f_{ck} + 1.64\,s",
     note="5 % defectives; e.g. Grade 35, $s = 5$ → margin 8.2 MPa", src=(D101, 53)),
   F("Absolute volume (yield) equation",
     r"\frac{M_C}{D_C} + \frac{M_W}{D_W} + \frac{M_S}{D_S} + \frac{M_G}{D_G} = 1 - V_A",
     note=r"masses per $\mathrm{m^3}$; $V_A$ = air content", src=(D101, 54)),
   F("Curing & maturity", note=r"Hydration datum ≈ −10 °C; maturity = $\sum(T + 10)\Delta t$", src=(D101, 53)),
 ]),
 S("14 · Fresh concrete & workability tests", D101, 54, [
   F("Workability tests & ranges",
     note="Vebe (very low), compacting factor (low–medium), slump 50–100 (medium–high), flow table > 150. "
          "BS 1881 → SS EN 12350-2/-3/-4/-5", src=(D101, 55)),
   F("Slump forms", note="True, shear, collapse; same slump ≠ same water if grading/cement/admixture change",
     src=(D101, 55)),
   F("SCC", note="Slump flow 600–700 mm, T500; VSI 0–3 (ASTM C1611)", src=(D101, 57)),
   F("Density & yield", r"Y = \frac{W_t}{D}", note="$W_t$ total batch mass, D compacted fresh density", src=(D101, 58)),
 ]),
 S("15 · Hardened concrete — strength testing & conformity", D101, 59, [
   F("Specimens", note=r"150 mm cubes (SG/UK) or 150×300 cylinders; min dimension ≥ $4 \times "
                       r"D_{\mathrm{max}}$; pair repeatability 10 % of mean", src=(D101, 59)),
   F("Characteristic strength", note=r"5 % of results expected below $f_{\mathrm{ck}}$ (28 d standard curing)", src=(D101, 53)),
   F("Conformity (today)",
     note="Notes use BS 5328 / SS 289 tables — superseded. SS EN 206 initial production ($n = 3$): mean ≥ "
          r"$f_{\mathrm{ck}} + 4$, each ≥ $f_{\mathrm{ck}} - 4$; continuous ($n \ge 15$): mean ≥ "
          r"$f_{\mathrm{ck}} + 1.48\sigma$", clause="SS EN 206 8.2.1", src=(D101, 60)),
   F("Tensile splitting", r"f_{ct,sp} = \frac{2F}{\pi L d}", note="repeatability 18 %", src=(D101, 63)),
   F("Flexural strength (4-point, prism)", r"f_{cf} = \frac{F\,l}{d_1 d_2^2}", note="report to 0.1 MPa",
     src=(D101, 63)),
   F("Investigation of non-conformity", note="Cores, NDT correlations or load tests; core ≠ cube strength",
     src=(D101, 62)),
 ]),
 S("16 · Non-destructive testing", D101, 65, [
   F("Rebound hammer", r"\bar{R}\ \mathrm{within}\ \pm\frac{15}{\sqrt{n}}\ \%\ (95\%)",
     note="≥ 10–12 readings, 20 mm apart & from edges; affected by carbonation (↑), moisture, surface, angle; "
          "anvil ≈ 80", src=(D101, 66)),
   F("Ultrasonic pulse velocity", r"f_c = A e^{BV}",
     note="direct / semi-direct / indirect; affected by aggregate E, moisture (water raises V), cracks, coupling",
     src=(D101, 68)),
 ]),
 S("17 · Stress–strain & time-dependent behaviour", D101, 69, [
   F("Cracking stages under compression",
     note="< 25 % fc stable bond cracks; > 50 % matrix cracks start; > 75 % cracks link (unstable); "
          "sustained > ~80 % → creep failure", src=(D101, 69)),
   F("Creep + shrinkage", note="Combined > sum; restrained shrinkage → tensile cracking; not fully recoverable",
     src=(D101, 70)),
 ]),
 S("18 · Quality control, durability & special concrete", D101, 71, [
   F("Quality control", note="Hardest to control: effective water content (sand moisture); slump drift may also "
                             "reflect cement/grading changes", src=(D101, 72)),
   F("High-performance concrete", note="> 60–140 MPa, SCC, extreme durability, LW/HW; fibres for tensile ductility",
     src=(D101, 73)),
   F("Mass pour (raft) strategy",
     note=r"$350\text{–}400\ \mathrm{kg/m^3}$ low-heat binder (70 % ggbs or 30 % pfa + 5–7 % csf), water "
          r"$150\text{–}160\ \mathrm{kg/m^3}$, plasticiser + retarder, chilled water; conformity at 56 d", src=(D101, 74)),
   F("Sulfate attack", note=r"Ettringite ($\mathrm{C_3A} \cdot 3C\bar{S} \cdot H_{32}$) expansion; internal "
                            "(DEF) if cured > 70 °C; use SRPC / SCMs",
     src=(D101, 75)),
 ]),
]

D102 = "CE102/CE102_Structural_Mechanics.pdf"
M1 = "CE102/CE1101_M1_Axial_Force_Members.pdf"
M2 = "CE102/CE1101_M2_Torsional_Members.pdf"
M3 = "CE102/CE1101_M3_Flexural_Members.pdf"
M4 = "CE102/CE1101_M4_Stress_Strain_Bending.pdf"
M5 = "CE102/CE1101_M5_Deflection_of_Beams.pdf"
S1 = "CE102/CE1101_S1_Equilibrium_of_Particles.pdf"
S2_ = "CE102/CE1101_S2_Equilibrium_of_Rigid_Bodies.pdf"
S3 = "CE102/CE1101_S3_Truss_Structures.pdf"
S4 = "CE102/CE1101_S4_Frame_and_Cable_Structures.pdf"

CE102 = [
 S("1 · Fundamental principles & laws", D102, 2, [
   F("Parallelogram law, transmissibility, Newton's laws",
     note="A force may slide along its line of action; action = reaction", src=(D102, 2)),
   F("Newton's 2nd law · work–energy · impulse–momentum",
     r"\sum F = ma,\quad U_{1\to2} = \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2,\quad \int F\,dt = mv_2 - mv_1",
     src=(D102, 3)),
 ]),
 S("2 · Equilibrium of particles", D102, 4, [
   F("Resultant of concurrent forces", r"R_x = \sum F_x,\quad R_y = \sum F_y,\quad R = \sqrt{R_x^2 + R_y^2}",
     note="particle in equilibrium: $R = 0$", src=(D102, 4)),
   F("Parallelogram law: sine & cosine rules (S1)", r"R^2 = a^2 + b^2 + 2ab\cos\theta,\quad \frac{a}{\sin\alpha} = \frac{b}{\sin\beta} = \frac{R}{\sin\gamma}",
     note=r"$\theta$ = angle between the two forces; for > 2 forces use Cartesian components", src=(S1, 18)),
   F("Free-body diagram (S1)", note="Isolate completely; show all external forces (weights, reactions, cable tensions); "
     "internal forces appear only where a member is cut; frictionless pulley → equal tension both sides",
     src=(S1, 5)),
 ]),
 S("3 · Moments & equilibrium of rigid bodies", D102, 5, [
   F("Moment of a force about a point", r"\mathbf{M}_O = \mathbf{r} \times \mathbf{F}",
     note="evaluate as a 3×3 determinant of i, j, k / r / F", src=(D102, 5)),
   F("Moment about an axis AL", r"M_{AL} = \boldsymbol{\lambda} \cdot (\mathbf{r}_{A} \times \mathbf{F})",
     note=r"$\lambda$ = unit vector along the axis; r from any point on the axis", src=(D102, 6)),
   F("Equivalent force–couple system", r"\mathbf{R} = \sum \mathbf{F}_i,\quad \mathbf{M}_O^R = \sum \mathbf{r}_i \times \mathbf{F}_i",
     src=(D102, 7)),
   F("2-D equilibrium", r"\sum F_x = 0,\quad \sum F_y = 0,\quad \sum M_O = 0",
     note=r"3 equations, 3 unknowns; alternatively $\sum F_x$ + two moment equations, or three moment "
          "equations about non-collinear points", src=(D102, 8)),
   F("Couple; force–couple equivalence (S2)", r"M = Fd\ \ \mathrm{(same\ about\ every\ point)},\quad F\ \mathrm{at}\ e \equiv F + M = Fe",
     src=(S2_, 8)),
   F("Support reactions (S2)", note="A support exerts a force in each direction it prevents translation and a moment if it "
     "prevents rotation: roller 1, pin 2, fixed 3", src=(S2_, 19)),
 ]),
 S("4 · Free-body diagrams; two- & three-force members", D102, 9, [
   F("Two-force member", note="Forces equal, opposite and collinear (along the line joining the two points)",
     src=(D102, 10)),
   F("Three-force member", note="The three forces must be concurrent (or parallel) — use the force triangle",
     src=(D102, 12)),
 ]),
 S("5 · Pin-jointed structures: trusses & frames", D102, 12, [
   F("Categories", note="Trusses (two-force members), frames (≥ 1 multi-force member), machines (transmit/modify forces)",
     src=(D102, 12)),
   F("Truss assumptions", note="Pinned joints, loads at joints, straight members → axial forces only",
     src=(D102, 14)),
   F("Method of joints", r"\sum F_x = 0,\quad \sum F_y = 0\ \mathrm{at\ each\ joint}",
     note="start at a joint with ≤ 2 unknowns; assume tension", src=(D102, 15)),
   F("Zero-force members & special joints",
     note="Two non-collinear members, no load → both zero; three members, two collinear, no load → third is zero; "
          "X-joints → opposite members equal", src=(D102, 16)),
   F("Method of sections", note="Cut ≤ 3 members with unknown forces; take moments about the intersection of "
                                "two",
     src=(D102, 18)),
   F("Frames", note="Dismember; identify two-force members first; pins carry forces between parts", src=(D102, 21)),
   F("Special joints (S3)", note="Unloaded L-joint → both zero; unloaded T-joint → stem zero; collinear pair + load along "
     "third → third = P", src=(S3, 6)),
   F("Truss solution strategy (S3)", note="FBD of whole truss → reactions → mark special joints → joints or sections; "
     "a truss behaves like a beam (top chord compression, bottom chord tension under gravity)", src=(S3, 20)),
   F("Truss vs frame vs machine (S4)", note="Frames: ≥ 1 multi-force member, loads anywhere, rigid (reactions from overall "
     "equilibrium); machines: non-rigid, transmit/modify forces, need dismembering for reactions", src=(S4, 3)),
   F("Frame solution steps (S4)", note="Whole FBD → reactions → dismember → two-force members first → moments about the "
     "point where all but one unknown intersect", src=(S4, 5)),
 ]),
 S("5a · Cables under concentrated loads (S4)", S4, 26, [
   F("Cable segments", note="Straight between loads (two-force segments); 4 support unknowns → need one extra fact: "
     "position of a point, tension/slope at a point, or total length", src=(S4, 27)),
   F("Horizontal tension constant", r"\sum M_{cut} = 0:\ T_x\,y_D = \sum M\ \mathrm{(loads\ and\ reactions\ about\ D)}",
     note=r"$T_x$ is the same throughout (no horizontal loads); $T_{\mathrm{max}}$ at the steepest segment", src=(S4, 31)),
   F("Given cable length", r"L_c = \sum_i \sqrt{(x_i - x_{i-1})^2 + (y_i - y_{i-1})^2}", src=(S4, 34)),
 ]),
 S("6 · Stress, strain & Hooke's law", D102, 24, [
   F("State of stress", note=r"Six independent components ($\sigma_x$, $\sigma_y$, $\sigma_z$, $\tau_{xy}$, "
                             r"$\tau_{yz}$, $\tau_{zx}$)", src=(D102, 25)),
   F("Generalised Hooke's law", r"\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right],\quad \gamma_{xy} = \frac{\tau_{xy}}{G},\quad G = \frac{E}{2(1+\nu)}",
     src=(D102, 26)),
   F("Average normal & shear stress (M1)", r"\sigma = \frac{P}{A},\quad \tau_{avg} = \frac{V}{A},\quad V = \frac{P}{2}\ \mathrm{(double\ shear)}",
     src=(M1, 9)),
   F("Factor of safety (M1)", r"n_s = \frac{P_{failure}}{P_{allowable}} = \frac{\sigma_{failure}}{\sigma_{allowable}} \geq 1", src=(M1, 14)),
 ]),
 S("7 · Axially loaded members", D102, 27, [
   F("Elongation of a stepped bar", r"\delta = \sum_i \frac{P_i L_i}{E_i A_i}", src=(D102, 29)),
   F("Statically indeterminate bar (superposition)",
     r"\delta_L + \delta_R = 0 \Rightarrow R_B",
     note=r"remove redundant support, find free deflection $\delta_L$, add $\delta_R$ from $R_B$, enforce "
          r"compatibility. Notes' example: $1125/E = 1.95R_B/E$ → $R_B = 577\ \mathrm{kN}$", src=(D102, 28)),
   F("Varying section and load (M1)", r"\delta = \int_0^L \frac{P(x)}{E\,A(x)}dx", src=(M1, 29)),
   F("Degree of indeterminacy (M1)", note="unknowns − equations; solve with equilibrium + compatibility + "
     "force–displacement", src=(M1, 30)),
   F("Truss deflection by geometry (M1)", note=r"member elongations $\delta = NL/EA$ must stay compatible at "
                                               "the joints — Williot-type sketch", src=(M1, 32)),
 ]),
 S("8 · Torsion of circular shafts", D102, 30, [
   F("Torsion formula & twist", r"\tau = \frac{T\rho}{J},\quad \tau_{max} = \frac{Tc}{J},\quad \phi = \frac{TL}{GJ}",
     src=(D102, 31)),
   F("Polar second moment", r"J_{solid} = \frac{\pi c^4}{2} = \frac{\pi d^4}{32},\quad J_{hollow} = \frac{\pi}{2}(c_2^4 - c_1^4)",
     src=(D102, 32)),
   F("Indeterminate shaft fixed at both ends", r"T_A + T_B = T,\quad \phi_{AC} = \phi_{CB}",
     src=(D102, 33)),
   F("Varying section/torque (M2)", r"\phi = \int_0^L\frac{T(x)}{G\,J(x)}dx,\quad \phi = \sum\frac{T_iL_i}{G_iJ_i}", src=(M2, 11)),
   F("Axial ↔ torsion analogy (M2)", r"\delta = \frac{FL}{EA} \leftrightarrow \theta = \frac{TL}{GJ},\quad \sigma = \frac{F}{A} \leftrightarrow \tau = \frac{Tr}{J}",
     note="circular, linear-elastic only; ignores stress concentrations; right-hand rule sign convention", src=(M2, 12)),
   F("Power transmission (M2)", r"P = T\omega,\quad \omega = \frac{2\pi N}{60}", src=(M2, 27)),
   F("Bolted shaft coupling (M2)", note=r"bolts on the pitch circle carry shear: $n \cdot F \cdot r_b = T$", src=(M2, 20)),
 ]),
 S("9 · Flexural members: internal forces, SFD & BMD", D102, 34, [
   F("Sign convention", note="Deformation sign convention: +V clockwise on element, +M sagging; tension +ve",
     src=(D102, 35)),
   F("Load–shear–moment relations", r"\frac{dV}{dx} = -q,\quad \frac{dM}{dx} = V,\quad M_B - M_A = \int_A^B V\,dx",
     note="point load → jump in V; applied couple → jump in M; M is max where $V = 0$", src=(D102, 37)),
   F("Drawing diagrams", note="Reactions → segment by segment left to right; V jumps at point loads, M slope = V",
     src=(D102, 38)),
   F("Jumps at concentrated actions (M3)", note="Point load P: V drops by P, M unchanged (slope changes); "
                                                "clockwise couple $M_0$: M jumps, V unchanged", src=(M3, 10)),
 ]),
 S("10 · Bending (normal) stresses", D102, 42, [
   F("Flexure formula", r"\sigma_x = -\frac{My}{I},\quad \sigma_{max} = \frac{M}{S},\quad S = \frac{I}{c}",
     note="neutral axis through the centroid (linear elastic, no axial force); rectangle $S = bh^2/6$", src=(D102, 44)),
   F("Parallel-axis theorem", r"I = I_c + Ad^2", note="composite areas: sum about common axis", src=(D102, 46)),
   F("Moment–curvature (M4)", r"\kappa = \frac{1}{\rho} = \frac{M}{EI},\quad \varepsilon_x = -\kappa y", src=(M4, 11)),
   F("I by superposition (M4)", note="About an axis of symmetry, add/subtract rectangles directly (e.g. I-section = "
     "outer box − two voids)", src=(M4, 16)),
   F("Transformed section (M4)", r"n = \frac{E_2}{E_1},\quad b^* = nb,\quad \sigma_1 = -\frac{My}{I_t},\quad \sigma_2 = -n\frac{My}{I_t}",
     note="scale widths only; N.A. at centroid of transformed section", src=(M4, 18)),
 ]),
 S("11 · Shear stresses in beams", D102, 50, [
   F("Shear formula", r"\tau = \frac{VQ}{Ib}", note="Q = first moment of area beyond the level considered",
     src=(D102, 51)),
   F("Rectangular section", r"\tau_{max} = \frac{3V}{2A}", note="parabolic; max at neutral axis", src=(D102, 52)),
   F("Flanged sections", note=r"Web carries most of the shear; check $\tau$ at web–flange junction with $b = "
                              "t_w$",
     src=(D102, 54)),
 ]),
 S("12 · Deflection — elastic curve & Macaulay", D102, 55, [
   F("Elastic curve", r"EI\frac{d^2y}{dx^2} = M,\quad \frac{1}{\rho} = \frac{M}{EI}", src=(D102, 56)),
   F("Macaulay (singularity) functions", r"\langle x - a\rangle^n = 0\ (x < a),\ (x - a)^n\ (x \geq a)",
     note="one equation for the whole beam; integrate twice, constants from supports", src=(D102, 57)),
   F("Direct integration & continuity (M5)", note="Piecewise M(x) → integrate each segment; boundary "
                                                  "conditions at supports plus continuity of y and $y'$ at "
                                                  "segment joins", src=(M5, 11)),
   F("Superposition (M5)", note="Linear ODE → add deflections from standard cases", src=(M5, 14)),
 ]),
 S("13 · Moment-area method", D102, 60, [
   F("1st theorem", r"\theta_{B/A} = \int_A^B \frac{M}{EI}\,dx", note="change in slope = area of M/EI diagram",
     src=(D102, 60)),
   F("2nd theorem", r"t_{B/A} = \int_A^B \frac{M}{EI}\,\bar{x}_B\,dx",
     note="tangential deviation of B from tangent at A = first moment of M/EI area about B", src=(D102, 61)),
   F("Area & centroid of typical shapes (M5)", r"\mathrm{rectangle}:\ bh,\ \frac{b}{2};\quad \mathrm{triangle}:\ \frac{bh}{2},\ \frac{b}{3};\quad \mathrm{parabolic\ spandrel}:\ \frac{bh}{3},\ \frac{b}{4}",
     note=r"$\bar{x}$ measured from the end with zero ordinate's opposite (see sketch on p. 21); nth-degree "
          "spandrel: bh/(n+1)",
     src=(M5, 21)),
   F("Not covered", note="Kinetics of particles and plane motion of rigid bodies are listed in the syllabus but not in "
                         "these slides — revise from Hibbeler/Beer", src=(D102, 1)),
 ]),
]

D103 = "CE103/CE103_Structural_Analysis.pdf"

CE103 = [
 S("1 · Stability & determinacy", D103, 15, [
   F("Beams", r"r \gtrless c + 3", note="r reactions, c conditions from internal hinges/releases; < unstable, = determinate, "
     "> indeterminate (degree r − c − 3) — check geometric instability", src=(D103, 15)),
   F("Trusses", r"m + r \gtrless 2j", src=(D103, 16)),
   F("Rigid frames", r"3m + r \gtrless 3j + c",
     note="your worked example (p. 3): 4 members, 5 joints, $r = 5$ → $17 - 15 = 2$ degrees indeterminate", src=(D103, 17)),
 ]),
 S("2 · Trusses, beams & frames (statically determinate)", D103, 18, [
   F("Same methods as CE102", note="Joints, sections, SFD/BMD; frames: break into members and draw each",
     src=(D103, 34)),
 ]),
 S("3 · Deflections — elastic curve & moment-area", D103, 36, [
   F("Curvature & Macaulay", r"\kappa = \frac{1}{\rho} = \frac{M}{EI},\quad EIy'' = M", src=(D103, 37)),
   F("Moment-area theorems", r"\theta_{B/A} = \int_A^B \frac{M}{EI}dx,\quad t_{B/A} = \int_A^B \frac{M}{EI}\bar{x}_B\,dx",
     src=(D103, 41)),
 ]),
 S("4 · Energy methods & virtual work", D103, 47, [
   F("External work & strain energy", r"U_e = \frac{1}{2}P\Delta,\quad U_i = \sum\frac{N^2L}{2AE} + \int\frac{M^2}{2EI}dx",
     src=(D103, 47)),
   F("Virtual work — trusses", r"1\cdot\Delta = \sum\frac{nNL}{AE},\quad 1\cdot\Delta = \sum n\,\alpha\,\Delta T\,L,\quad 1\cdot\Delta = \sum n\,\delta L",
     note=r"n = member force from a unit virtual load at the point/direction of $\Delta$; temperature and "
          "fabrication errors",
     src=(D103, 51)),
   F("Virtual work — beams & frames", r"1\cdot\Delta = \int\frac{mM}{EI}dx,\quad 1\cdot\theta = \int\frac{m_\theta M}{EI}dx",
     note="unit couple for slopes; integrate member by member", src=(D103, 52)),
 ]),
 S("5 · Influence lines", D103, 55, [
   F("Simply supported beam ordinates", r"IL_{R_A}(x) = 1 - \frac{x}{L},\quad IL_{M_C}^{max} = \frac{ab}{L}",
     note="C at a from A, b from B", src=(D103, 56)),
   F("Using influence lines", r"E = \sum P_i y_i\ (\mathrm{point\ loads}),\quad E = w\times\mathrm{area\ under\ IL}\ (\mathrm{UDL})",
     note="UDL only over the positive (or negative) part for the extreme value", src=(D103, 59)),
   F("Müller-Breslau principle",
     note="IL = deflected shape when the restraint for that action is removed and a unit displacement (or "
          "rotation / relative slide) is imposed", src=(D103, 61)),
 ]),
 S("6 · Force method (consistent deformation)", D103, 64, [
   F("Compatibility with one redundant", r"\Delta_{B0} + f_{BB}R_B = 0",
     note="e.g. propped cantilever, central P: $5PL^3/(48EI) = R_BL^3/(3EI)$ → $R_B = 5P/16$; UDL: $R_B = "
          "3wL/8$",
     src=(D103, 65)),
 ]),
 S("7 · Castigliano & least work", D103, 66, [
   F("Castigliano's 2nd theorem", r"\Delta_j = \frac{\partial U}{\partial P_j} = \int\frac{M}{EI}\frac{\partial M}{\partial P_j}dx",
     src=(D103, 67)),
   F("Least work", r"\frac{\partial U}{\partial R} = 0", note="redundant R takes the value minimising strain energy",
     src=(D103, 66)),
 ]),
 S("8 · Slope-deflection method", D103, 70, [
   F("Slope-deflection equation", r"M_{AB} = \frac{2EI}{L}\left(2\theta_A + \theta_B - 3\psi\right) + FEM_{AB},\quad \psi = \frac{\Delta}{L}",
     note=r"clockwise moments and rotations positive; joint equilibrium $\sum M = 0$; sway → shear equation", src=(D103, 71)),
   F("Fixed-end moments", r"FEM = \mp\frac{wL^2}{12}\ (\mathrm{UDL}),\quad \mp\frac{PL}{8}\ (\mathrm{central\ P}),\quad \mp\frac{Pab^2}{L^2},\ \pm\frac{Pa^2b}{L^2}",
     src=(D103, 72)),
 ]),
 S("9 · Moment distribution", D103, 76, [
   F("Stiffness & distribution factor", r"k = \frac{4EI}{L}\ (\mathrm{far\ fixed}),\quad k = \frac{3EI}{L}\ (\mathrm{far\ pinned}),\quad DF = \frac{k}{\sum k}",
     src=(D103, 77)),
   F("Carry-over factor", note=r"$\tfrac12$ to a fixed far end, 0 to a pinned end; balance → carry over → "
                               "repeat",
     src=(D103, 79)),
 ]),
 S("10 · Direct stiffness method", D103, 80, [
   F("Truss element (local)", r"[k'] = \frac{EA}{L}\,[\,1\ \ -1\ ;\ -1\ \ 1\,]", src=(D103, 80)),
   F("Global stiffness", r"[k] = [T]^T[k'][T],\quad k_{11} = \frac{EA}{L}\lambda_x^2,\ k_{12} = \frac{EA}{L}\lambda_x\lambda_y",
     note=r"$\lambda_x = \cos\theta_x$, $\lambda_y = \cos\theta_y$; assemble, apply supports, solve $\{Q\} = "
          r"[K]\{D\}$", src=(D103, 82)),
   F("Beam element terms", r"\frac{12EI}{L^3},\ \frac{6EI}{L^2},\ \frac{4EI}{L},\ \frac{2EI}{L}",
     note="member loads → equivalent joint loads (fixed-end actions reversed)", src=(D103, 87)),
   F("Not covered in these slides", note="Plastic analysis and elastic stability of frames are in the syllabus but not "
     "in these notes — see West & Geschwindner / the CE103 formula sheet quick reference", src=(D103, 12)),
 ]),
]

D105 = "CE105/CE105_Pressure_and_Fluid_Statics.pdf"   # compilation: fluids + hydraulics + hydrology

CE105 = [
 S("1 · Fluids, viscosity & pressure", D105, 2, [
   F("Fluid definition", note="Deforms continuously under any shear stress; solid → constant shear angle, fluid → "
                              "constant rate of shear", src=(D105, 2)),
   F("Absolute, gauge & vacuum pressure", r"P_{gage} = P_{abs} - P_{atm},\quad P_{vac} = P_{atm} - P_{abs}",
     note="pressure at a point acts equally in all directions (Pascal)", src=(D105, 4)),
 ]),
 S("2 · Hydrostatics, manometers & barometer", D105, 6, [
   F("Pressure variation with depth", r"P = P_0 + \rho g h", note="independent of container shape", src=(D105, 7)),
   F("Manometer rule", r"\Delta P = \rho g h", note="+ going down, − going up; same level in a continuous fluid = same "
                                                "pressure", src=(D105, 9)),
   F("Barometer", r"P_{atm} = \rho_{Hg} g h", note="standard atmosphere = 760 mmHg = 101.325 kPa", src=(D105, 11)),
 ]),
 S("3 · Forces on plane surfaces", D105, 14, [
   F("Resultant force", r"F_R = (P_0 + \rho g y_C\sin\theta)A = P_C A",
     note="y measured along the plate from the free surface; acts below the centroid", src=(D105, 15)),
   F("Centre of pressure", r"y_P = y_C + \frac{I_{xx,C}}{y_C A}\ \ (P_0 = 0)", src=(D105, 16)),
   F("Centroidal second moments", r"I_{rect} = \frac{ab^3}{12},\quad I_{circle} = \frac{\pi R^4}{4},\quad I_{tri} = \frac{ab^3}{36}",
     src=(D105, 17)),
 ]),
 S("4 · Forces on curved surfaces", D105, 19, [
   F("Components", r"F_H = F_{x,\,projection},\quad F_V = F_y + W,\quad F_R = \sqrt{F_H^2 + F_V^2},\quad \alpha = \tan^{-1}\frac{F_V}{F_H}",
     note="$F_H$ = force on the vertical projection; $F_V$ = weight of fluid above (real or imaginary)", src=(D105, 19)),
 ]),
 S("5 · Buoyancy & stability", D105, 20, [
   F("Archimedes", r"F_B = \rho_f g V_{sub}", note="acts through the centroid of displaced volume (centre of buoyancy)",
     src=(D105, 21)),
   F("Stability", r"GM = \frac{I}{V_{sub}} - BG",
     note=r"immersed bodies: G below B; floating bodies: metacentre M above G ($\mathrm{GM} > 0$); I = "
          "waterplane second moment about the tilt axis", src=(D105, 29)),
 ]),
 S("6 · Fluids in rigid-body motion", D105, 30, [
   F("Linear acceleration", r"\tan\theta = \frac{a_x}{g + a_z},\quad P_2 - P_1 = -\rho a_x(x_2 - x_1) - \rho(g + a_z)(z_2 - z_1)",
     src=(D105, 32)),
   F("Rotation about a vertical axis", r"z_s = h_0 - \frac{\omega^2}{4g}(R^2 - 2r^2),\quad \Delta z_{max} = \frac{\omega^2R^2}{2g}",
     note=r"$P = P_1 + \rho\omega^2r^2/2 - \rho gz$", src=(D105, 34)),
 ]),
 S("7 · Conservation laws in pipe flow", D105, 118, [
   F("Continuity", r"Q = A_1v_1 = A_2v_2", src=(D105, 121)),
   F("Momentum (pipe thrust)", r"\sum F = \rho Q(v_2 - v_1)",
     note="bend: include $p_1A_1$, $p_2A_2$, fluid weight; anchor force F from the momentum balance per "
          "direction",
     src=(D105, 123)),
   F("Bernoulli / energy", r"z_1 + \frac{p_1}{\rho g} + \frac{v_1^2}{2g} = z_2 + \frac{p_2}{\rho g} + \frac{v_2^2}{2g} + \Delta E",
     note=r"$\mathrm{HGL} = z + p/\rho g$; $\mathrm{EGL} = \mathrm{HGL} + v^2/2g$", src=(D105, 127)),
 ]),
]

CE205 = [
 S("1 · Specific energy & critical flow", D105, 38, [
   F("Normal depth, wide rectangular channel", r"R \approx h,\quad h_n = \left(\frac{nq}{\sqrt{S_0}}\right)^{3/5}",
     note="general sections: iterate Manning", src=(D105, 40)),
   F("Specific energy", r"E = h + \frac{Q^2}{2gA^2}", src=(D105, 40)),
   F("Critical flow", r"\frac{dE}{dh} = 1 - Fr^2 = 0,\quad Fr = \frac{v}{\sqrt{gA/B}},\quad h_c = \left(\frac{q^2}{g}\right)^{1/3},\quad E_{min} = \frac{3}{2}h_c",
     note=r"at critical: E minimum for Q, Q maximum for E; sub-critical $\mathrm{Fr} < 1$, super-critical "
          r"$\mathrm{Fr} > 1$", src=(D105, 44)),
 ]),
 S("2 · Hydraulic jump", D105, 48, [
   F("Sequent depths (rectangular)", r"\frac{h_2}{h_1} = \frac{1}{2}\left(\sqrt{1 + 8\mathrm{Fr}_1^2} - "
                                     r"1\right)",
     note=r"general section: momentum function $F + M = \rho g A \bar{y} + \rho Q^2/A$ equal on both sides", src=(D105, 49)),
   F("Energy loss & length", r"\Delta E = \frac{(h_2 - h_1)^3}{4h_1h_2},\quad L_j \approx 5\ \mathrm{to}\ 7\,(h_2 - h_1)",
     src=(D105, 50)),
 ]),
 S("3 · Gradually varied flow & surface profiles", D105, 52, [
   F("GVF equation", r"\frac{dh}{dx} = \frac{S_0 - S_f}{1 - Fr^2}", src=(D105, 60)),
   F("Slope classes", note="M ($h_n > h_c$), S ($h_n < h_c$), C ($h_n = h_c$), H ($S_0 = 0$), A ($S_0 < 0$); "
                           "zones 1–3; sketch from control points (critical depth at free overfall, gates, "
                           "weirs)", src=(D105, 55)),
   F("Computation", note=r"Direct step ($\Delta x$ from $\Delta h$) for prismatic channels; standard step for "
                         "natural channels",
     src=(D105, 62)),
 ]),
 S("4 · Uniform flow & channel capacity", D105, 65, [
   F("Uniform flow", r"\tau_0 = \rho g R S_0", note=r"laminar $\mathrm{Re} < 500$, turbulent $\mathrm{Re} > "
                                                    "1000$ (log velocity profile)",
     src=(D105, 69)),
   F("Chézy", r"v = C\sqrt{RS_0}", src=(D105, 76)),
   F("Manning", r"v = \frac{1}{n}R^{2/3}S_0^{1/2},\quad Q = \frac{1}{n}AR^{2/3}S_0^{1/2},\quad C = \frac{R^{1/6}}{n}",
     note="conveyance $K = AR^{2/3}/n$", src=(D105, 77)),
   F("Part-full circular pipe", note=r"$Q_{\mathrm{max}} \approx 1.08 Q_{\mathrm{full}}$ at $h/D \approx "
                                     r"0.94$; half-full $Q = 0.5 Q_{\mathrm{full}}$", src=(D105, 80)),
 ]),
 S("5 · Weirs & gates", D105, 82, [
   F("Rectangular thin-plate weir", r"Q = C_d\frac{2}{3}\sqrt{2g}\,B\,h^{3/2}", note=r"$C_d \approx 0.6$ "
                                                                                     "(contraction, "
                                                                                     "non-atmospheric "
                                                                                     "pressure, approach "
                                                                                     "velocity)", src=(D105, 87)),
   F("V-notch weir", r"Q = C_d\frac{8}{15}\sqrt{2g}\tan\frac{\theta}{2}\,h^{5/2}", note="typical $C_d = 0.59$",
     src=(D105, 89)),
   F("Broad-crested weir", r"Q = C_d\left(\frac{2}{3}\right)^{3/2}\sqrt{g}\,B\,h^{3/2},\quad C_d \approx 0.88",
     note="critical depth on crest ($L > 2h$, free discharge)", src=(D105, 92)),
   F("Sluice gate", r"Q = C_d\,b\,a\sqrt{2gh_1}", note="a = gate opening", src=(D105, 100)),
 ]),
 S("6 · Pipe friction & minor losses", D105, 101, [
   F("Darcy–Weisbach", r"h_f = f\frac{L}{D}\frac{v^2}{2g} = \frac{8fLQ^2}{\pi^2gD^5}", src=(D105, 102)),
   F("Colebrook–White", r"\frac{1}{\sqrt{f}} = -2\log_{10}\left(\frac{k}{3.7D} + \frac{2.51}{Re\sqrt{f}}\right)",
     note=r"laminar ($\mathrm{Re} < 2000$) $f = 64/\mathrm{Re}$; transitional 2000–4000; Moody diagram", src=(D105, 103)),
   F("Hazen–Williams", r"h_f = \frac{10.67LQ^{1.852}}{C^{1.852}D^{4.87}}", note=r"$C \approx 120\text{–}150$ "
                                                                                "(table p. 106)",
     src=(D105, 106)),
   F("Manning (pipes)", r"h_f = \frac{10.29n^2LQ^2}{D^{16/3}}", note=r"$n \approx 0.008\text{–}0.017$ (table "
                                                                     "p. 107)",
     src=(D105, 107)),
   F("Minor losses", r"h_m = \xi\frac{v^2}{2g}", note="entrance 0.5, exit 1.0, bends, valves; v downstream",
     src=(D105, 113)),
 ]),
 S("7 · Pipe systems & networks", D105, 132, [
   F("Branched networks", note="Flows from nodal demands by continuity, then head losses → piezometric heads",
     src=(D105, 133)),
   F("Pipes in series / parallel", r"\mathrm{series:}\ Q_i = Q,\ \sum h_{f,i} = H;\quad \mathrm{parallel:}\ h_{f,i} = H,\ \sum Q_i = Q",
     note="equivalent diameter replaces the combination", src=(D105, 155)),
   F("Single-pipe design", note="Maximum capacity for available head; optimal (minimum) diameter for residual "
                                "pressure; allow for pipe ageing (roughness ↑)", src=(D105, 141)),
 ]),
 S("8 · Gravity & pumped systems", D105, 159, [
   F("Operating point", r"H_{pump}(Q) = H_{static} + \sum kQ^2",
     note=r"parallel pumps add Q at same H; series pumps add H at same Q; variable speed: $Q \propto N$, $H "
          r"\propto N^2$",
     src=(D105, 172)),
   F("Combined systems", note="Tank–pump–network, booster stations, zoned supply, water towers balancing demand",
     src=(D105, 184)),
 ]),
 S("9 · Hydrology: frequency analysis & rainfall", D105, 191, [
   F("Return period & risk", r"T = \frac{1}{p},\quad P(\geq 1\ \mathrm{in}\ n\ \mathrm{yr}) = 1 - \left(1 - \frac{1}{T}\right)^n",
     src=(D105, 193)),
   F("Chow's frequency equation", r"x_T = \bar{x} + K_T s", src=(D105, 193)),
   F("Gumbel (large n)", r"K_T = -\frac{\sqrt{6}}{\pi}\left[0.5772 + \ln\ln\frac{T}{T - 1}\right]",
     note=r"small n: $K_T = (y_T - \bar{y}_n)/s_n$ from tables", src=(D105, 194)),
   F("Areal rainfall", note="Arithmetic mean, Thiessen polygons, isohyets; design storm; PMP", src=(D105, 196)),
 ]),
 S("10 · Losses, infiltration & hydrographs", D105, 199, [
   F("Losses", note=r"Interception, depression storage, evapotranspiration ($\mathrm{AET} \le \mathrm{PET}$), "
                    "infiltration", src=(D105, 200)),
   F(r"$\phi$-index & W-index", r"\phi:\ \sum (i - \phi)\Delta t = R,\quad W = \frac{P - R - S_d}{t_e}",
     note=r"$\phi$ = rate above which rainfall volume equals runoff volume", src=(D105, 202)),
   F("Base-flow separation & ERH", note="Separate base flow → DRH; effective rainfall hyetograph from "
                                        r"$\phi$-index",
     src=(D105, 203)),
 ]),
 S("11 · Unit hydrograph", D105, 205, [
   F("Unit hydrograph", r"Q_n = \sum_{m=1}^{n} P_m U_{n-m+1}",
     note="DRH from 1 unit of excess rain in duration D; assumes linearity & time invariance", src=(D105, 205)),
   F("S-hydrograph", r"UH_{D'} = \frac{D}{D'}\left[S(t) - S(t - D')\right]", note=r"IUH = $dS/dt$ as $D' \to "
                                                                                  "0$",
     src=(D105, 207)),
   F("Synthetic UH & design flood", note="Snyder/SCS for ungauged catchments; PMF from UH + PMP", src=(D105, 208)),
   F("Stage–discharge", note="Rating curve $Q = C(h - a)^n$; weirs/flumes for direct measurement; hysteresis "
                             "correction for unsteady flow", src=(D105, 210)),
 ]),
 S("12 · Flood routing & reservoirs", D105, 213, [
   F("Muskingum", r"O_2 = C_0I_2 + C_1I_1 + C_2O_1",
     note=r"$C_0 = (-KX + 0.5\Delta t)/D$, $C_1 = (KX + 0.5\Delta t)/D$, $C_2 = (K - KX - 0.5\Delta t)/D$, $D "
          r"= K - KX + 0.5\Delta t$; $\sum C = 1$; $2KX < \Delta t < K$", src=(D105, 215)),
   F("Reservoir (level-pool) routing", r"\frac{2S_2}{\Delta t} + O_2 = I_1 + I_2 + \frac{2S_1}{\Delta t} - O_1",
     src=(D105, 217)),
   F("Reservoir design", note="Mass curve / sequent peak for storage; sediment trap efficiency", src=(D105, 219)),
 ]),
 S("13 · Groundwater & wells", D105, 221, [
   F("Darcy", r"q = -K\frac{dh}{dx},\quad K = \frac{k\rho g}{\mu}", src=(D105, 221)),
   F("Dupuit (unconfined, 1-D)", r"q = \frac{K}{2L}(h_1^2 - h_2^2)", src=(D105, 221)),
   F("Wells (steady)", r"\mathrm{confined:}\ Q = \frac{2\pi Kb(h_2 - h_1)}{\ln(r_2/r_1)},\quad \mathrm{unconfined:}\ Q = \frac{\pi K(h_2^2 - h_1^2)}{\ln(r_2/r_1)}",
     note="unsteady: Theis/Jacob; interference by superposition of drawdowns", src=(D105, 223)),
 ]),
]

D_HW = D103  # pp. 1–11 are handwritten cross-subject summary notes bound into the CE103 file
NOTES_LEGACY = {
 "CE201": [
   F("BS 8110 singly/doubly reinforced beam", legacy=True, src=(D_HW, 4),
     note=r"$f_{\mathrm{cu}}$, $0.45f_{\mathrm{cu}}$ block, $z = d[0.5 + \sqrt{0.25 - K/0.9}]$, $K' = 0.156$ — "
          r"use EC2: $f_{\mathrm{ck}}$, $z = d[0.5 + \sqrt{0.25 - K/1.134}]$, $K'$ per NA (0.167 for $\delta = "
          "1$)"),
   F("BS 8110 column capacity", legacy=True, src=(D_HW, 4),
     note=r"$N = 0.45f_{\mathrm{cu}} A_c + 0.87f_y A_s$ (BS $0.4f_{\mathrm{cu}}$ with nominal e) — use EC2 "
          r"$0.567f_{\mathrm{ck}} A_c + \sigma_s A_s$, $e_0 = \max(h/30,\ 20\ \mathrm{mm})$"),
   F(r"BS 8110 biaxial bending ($\beta$ table)", legacy=True, src=(D_HW, 4),
     note=r"EC2 5.8.9: $(M_{\mathrm{Edz}}/M_{\mathrm{Rdz}})^a + (M_{\mathrm{Edy}}/M_{\mathrm{Rdy}})^a \le 1$"),
   F(r"BS 8110 slender column ($\beta_a = (l_e/b)^2/2000$, $K = (N_{\mathrm{uz}} - N)/(N_{\mathrm{uz}} - "
     r"N_{\mathrm{bal}})$)", legacy=True, src=(D_HW, 5),
     note=r"EC2 5.8: $\lambda$ vs $\lambda_{\mathrm{lim}} = 20ABC/\sqrt{n}$; nominal curvature $e_2 = "
          "(1/r)l_0^2/c$"),
 ],
 "CE202": [
   F("BS 5950 section classes (plastic / compact / semi-compact / slender)", legacy=True, src=(D_HW, 11),
     note=r"EC3 Table 5.2 Class 1–4 with $\varepsilon = \sqrt{235/f_y}$; concept similar, limits differ"),
 ],
}

NOTES_SECTIONS = {"CE101": CE101, "CE102": CE102, "CE103": CE103, "CE105": CE105, "CE205": CE205}
