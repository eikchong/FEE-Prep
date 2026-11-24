"""CE2134 Hydraulics study notes.

Part 1 (Dr Yuan Jing's written notes, topics 1–9) → CE105 Fluid Mechanics.
Part 2 (Dr SK Ooi's slides: flow views, real fluids, pipes, machinery) → CE205 Hydraulics.
Tutorial answers come from the official solutions; mistakes in them are flagged with tips.
"""


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


P1 = "CE105/CE2134/"
P2 = "CE205/CE2134/"
D = {
    "H1": P1 + "1 Dimensional homogeneity.pdf", "H2": P1 + "2 Fluid properties.pdf", "H3": P1 + "3 Fluid statics.pdf",
    "H4": P1 + "4 Fluid kinematic.pdf", "H5": P1 + "5 Nature of conservation laws.pdf",
    "H6": P1 + "6 Bernoulli Equation.pdf", "H7": P1 + "7 Reynolds transport theorem.pdf",
    "H8": P1 + "8 Momentum principle.pdf", "H9": P1 + "9 Energy principle.pdf",
    "TQ": P1 + "tutorials/CE2134 Tutorial questions.pdf",
    "SE": P1 + "tutorials/Self_evaluation_questions (solutions).pdf",
    "V1": P2 + "1 Intro and FlowViews1.pdf", "V2": P2 + "1b FlowViews2.pdf", "V3": P2 + "1c FlowViews3.pdf",
    "VX": P2 + "1d FlowViews Examples.pdf", "R1": P2 + "2 RealFluids1.pdf", "R2": P2 + "2b RealFluids2.pdf",
    "RX": P2 + "2c RealFluids Examples Solution.pdf", "Q1": P2 + "3 PipesDucts1.pdf",
    "Q2": P2 + "3b PipesDucts2 corrected.pdf", "QX": P2 + "3c PipesDucts Examples.pdf",
    "M1": P2 + "4 Machinery1.pdf", "HW": P2 + "5 Steps for HW1.pdf",
}
# key, code, page_count, seq, topics
OUTLINE = [("H1", "CE105", 4, 11, ["CE105-07"]), ("H2", "CE105", 7, 12, ["CE105-01"]), ("H3", "CE105", 25, 13, ["CE105-02", "CE105-03"]),
           ("H4", "CE105", 9, 14, ["CE105-04"]), ("H5", "CE105", 5, 15, ["CE105-04"]), ("H6", "CE105", 13, 16, ["CE105-05"]),
           ("H7", "CE105", 6, 17, ["CE105-04", "CE105-06"]), ("H8", "CE105", 13, 18, ["CE105-06"]),
           ("H9", "CE105", 10, 19, ["CE105-05", "CE205-01"]), ("TQ", "CE105", 8, 30, ["CE105-02", "CE105-05", "CE105-06"]),
           ("SE", "CE105", 20, 31, ["CE105-01", "CE105-02", "CE105-05", "CE105-06"]),
           ("V1", "CE205", 8, 1, ["CE205-01"]), ("V2", "CE205", 16, 2, ["CE205-01"]), ("V3", "CE205", 21, 3, ["CE205-01"]),
           ("VX", "CE205", 10, 4, ["CE205-01"]), ("R1", "CE205", 23, 5, ["CE205-01"]), ("R2", "CE205", 18, 6, ["CE205-01"]),
           ("RX", "CE205", 8, 7, ["CE205-01"]), ("Q1", "CE205", 16, 8, ["CE205-01"]), ("Q2", "CE205", 19, 9, ["CE205-01"]),
           ("QX", "CE205", 10, 10, ["CE205-01"]), ("M1", "CE205", 15, 11, ["CE205-02"]), ("HW", "CE205", 7, 12, ["CE205-01"])]

HYD = {}

# ------------------------------------------------------------------ Part 1 → CE105
HYD[D["H1"]] = {"code": "CE105", "title": "Hydraulics 1 · Dimensional homogeneity", "sections": [
 sec("Dimensions & the three rules", (1, 3),
   ("md", "Fundamental dimensions **M, L, T**: [V] = L/T, [a] = L/T², [F] = ML/T². A physical equation must be "
          "dimensionally homogeneous: (A) both sides have the same dimension, (B) every term of a sum has the same "
          "dimension, (C) arguments of exp, log, trig functions are dimensionless (e.g. the log-law u = (u*/κ) ln(z/z₀))."),
 ),
 sec("Working habit", (3, 4),
   ("steps", ["Write symbols (g, ρ), not numbers with units.", "Manipulate symbolically to the end.",
              "Check homogeneity before substituting numbers.", "Always write units with the answer."]),
 ),
]}

HYD[D["H2"]] = {"code": "CE105", "title": "Hydraulics 2 · Fluid properties", "sections": [
 sec("Fluid vs solid; stress convention", (1, 2),
   ("md", "A fluid cannot resist shear at rest, however small. At rest the stress tensor is isotropic: T_ij = −p δ_ij. "
          "T_ij acts on face i in direction j; positive on a positive face in +j."),
 ),
 sec("Viscosity & no-slip", (2, 4),
   ("eq", r"\tau = \mu\frac{du}{dn},\qquad \nu = \frac{\mu}{\rho}\ [\mathrm{m^2/s}]"),
   ("md", "Newtonian fluids (water, air) have constant μ at a given temperature (μ falls with T for liquids). Real fluids "
          "obey **no-slip** at walls; an ideal fluid has μ = 0 and may slip."),
 ),
 sec("Continuum & compressibility", (4, 7),
   ("eq", r"E_v = -\frac{dp}{dV/V} = \frac{dp}{d\rho/\rho},\qquad Kn = \frac{\lambda_{mfp}}{L} \ll 1"),
   ("md", "Water E_v = 2.15 GPa: 100 MPa (10 km of water) changes density only ~5 % → treat as **incompressible** "
          "(conservation of volume)."),
 ),
]}

HYD[D["H3"]] = {"code": "CE105", "title": "Hydraulics 3 · Fluid statics, forces on surfaces, buoyancy & stability", "sections": [
 sec("Pressure at a point & hydrostatic law", (1, 5),
   ("eq", r"\frac{dp}{dz} = -\rho g\ \Rightarrow\ p + \rho gz = \text{const},\qquad \frac{p}{\rho g} + z = \text{piezometric head},\qquad p_{gauge} = \rho gh"),
   ("md", "Pressure is isotropic (a scalar); pressure force acts normal to and into the surface. Same fluid, same "
          "level → same pressure."),
 ),
 sec("Transmission, piezometer & manometers", (6, 9),
   ("md", "Hydraulic jack: F₂ = F₁A₂/A₁. Piezometer: p_A = ρgh (gauge only). U-tube: step through each fluid with "
          "p + ρgz = const; for a differential manometer between two points of a flowing pipe,"),
   ("eq", r"\left(\frac{p_A}{\rho g} + z_A\right) - \left(\frac{p_F}{\rho g} + z_F\right) = \Delta h\left(\frac{\rho_m}{\rho} - 1\right)"),
 ),
 sec("Plane surfaces", (10, 16),
   ("eq", r"F = p_cA = \rho gh_cA,\qquad y_{cp} = y_c + \frac{I_{xc}}{y_cA}\quad(\text{along the plane};\ \text{for a vertical wall from the surface } h_{cp} = 2H/3)"),
   ("md", "Inclined surface: horizontal component = force on its vertical projection; vertical component = weight of "
          "water above. Submerged gate: split the trapezoid into a uniform block (through centroid) + triangle. "
          "The centre of pressure approaches the centroid as depth increases."),
 ),
 sec("Curved surfaces", (17, 19),
   ("md", "F_H = force on the projection onto a vertical plane (acts at its centre of pressure). F_V = weight of the "
          "(real or imaginary) fluid column above the surface, through its centroid. 2-D resultant passes through the "
          "intersection of the two lines of action."),
 ),
 sec("Buoyancy", (19, 20),
   ("eq", r"F_B = \rho g V_{displaced}\ (\text{acts at the centroid of displaced volume, } B)"),
 ),
 sec("Stability of submerged and floating bodies", (20, 25),
   ("md", "Submerged: stable if **B is above G**. Floating: stable if the **metacentre M is above G**."),
   ("eq", r"BM = \frac{I_{yo}}{V_{sub}},\qquad GM = BM - BG > 0\ \text{(stable)}"),
   ("md", "Wide, shallow hulls (large waterline I) and low G (ballast) improve stability; valid for small angles only."),
 ),
]}

HYD[D["H4"]] = {"code": "CE105", "title": "Hydraulics 4 · Fluid kinematics", "sections": [
 sec("Lagrangian vs Eulerian; flow classification", (1, 2),
   ("md", "Eulerian description: fields V(x, y, z, t). Steady (∂/∂t = 0) vs unsteady; uniform vs non-uniform; "
          "1-D/2-D/3-D."),
 ),
 sec("Acceleration field", (3, 5),
   ("eq", r"\mathbf a = \frac{\partial\mathbf V}{\partial t} + (\mathbf V\cdot\nabla)\mathbf V,\qquad a_s = \frac{\partial V}{\partial t} + V\frac{\partial V}{\partial s},\quad a_n = \frac{V^2}{R}"),
   ("md", "Steady flow through a contraction still has **convective** acceleration."),
 ),
 sec("Streamlines, stream tubes", (6, 9),
   ("eq", r"\frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}"),
   ("md", "No flow crosses a streamline; converging streamlines → higher velocity. For steady flow streamlines, "
          "pathlines and streaklines coincide."),
 ),
]}

HYD[D["H5"]] = {"code": "CE105", "title": "Hydraulics 5 · Conservation laws: mass & volume", "sections": [
 sec("Fluxes & the bank-account analogy", (1, 3),
   ("eq", r"Q = \int_A \mathbf V\cdot\mathbf n\,dA = \bar VA,\qquad \dot m = \rho Q"),
   ("md", "Rate of change inside = inflow − outflow (like a bank balance)."),
 ),
 sec("Mass and volume conservation", (3, 5),
   ("eq", r"\frac{dM_{cv}}{dt} = \sum \dot m_{in} - \sum \dot m_{out};\qquad \text{incompressible, steady: } \sum Q_{in} = \sum Q_{out},\ V_1A_1 = V_2A_2"),
 ),
]}

HYD[D["H6"]] = {"code": "CE105", "title": "Hydraulics 6 · Bernoulli equation & applications", "sections": [
 sec("Derivation along and across streamlines", (1, 7),
   ("eq", r"\frac{p}{\rho g} + \frac{V^2}{2g} + z = H\ \text{(along a streamline)},\qquad \frac{\partial}{\partial n}\left(\frac{p}{\rho g} + z\right) = -\frac{V^2}{gR}"),
   ("md", "In a **well-behaved** region (straight, parallel streamlines) the piezometric head is constant across the "
          "flow, so H is the same on all streamlines there."),
 ),
 sec("Restrictions", (8, 8),
   ("md", "Steady, inviscid (no losses), incompressible, along a streamline, no shaft work."),
 ),
 sec("Free jets, orifices, vena contracta", (8, 11),
   ("eq", r"V = \sqrt{2gh}\ (\text{Torricelli}),\qquad Q = C_cA_o\sqrt{2gh}"),
   ("md", "Streamlines contract after a sharp orifice: C_c ≈ 0.61 sharp-edged, ≈ 0.5 re-entrant (Borda), ≈ 1 rounded."),
 ),
 sec("Pitot tube", (12, 13),
   ("eq", r"V = \sqrt{2(p_0 - p)/\rho}\quad(\text{stagnation} - \text{static})"),
 ),
]}

HYD[D["H7"]] = {"code": "CE105", "title": "Hydraulics 7 · Reynolds transport theorem", "sections": [
 sec("System vs control volume", (1, 2),
   ("md", "Laws are written for a **system** (fixed mass); engineering uses a **control volume** (fixed region). "
          "RTT converts one to the other."),
 ),
 sec("RTT and mass/volume conservation", (2, 6),
   ("eq", r"\frac{dB_{sys}}{dt} = \frac{\partial}{\partial t}\int_{CV}\rho b\,dV + \int_{CS}\rho b\,(\mathbf V\cdot\mathbf n)\,dA"),
   ("md", "b = 1 gives mass conservation; b = V gives momentum; b = e gives energy."),
 ),
]}

HYD[D["H8"]] = {"code": "CE105", "title": "Hydraulics 8 · Momentum principle", "sections": [
 sec("Linear momentum for a control volume", (1, 5),
   ("eq", r"\sum\mathbf F = \frac{\partial}{\partial t}\int_{CV}\rho\mathbf V\,dV + \sum_{out}\rho Q K_m\mathbf V - \sum_{in}\rho Q K_m\mathbf V"),
   ("md", "K_m ≈ 1 for turbulent flow (4/3 laminar). Define the **hydraulic thrust** on a flow area, MP = (p + ρV²)A, "
          "always pointing into the CV; at a free jet p = 0."),
 ),
 sec("Steady flow: sum of thrusts + wall force = 0", (6, 7),
   ("eq", r"\sum MP_i + \mathbf F_{wall\to fluid} = 0\quad(\text{gravity added if relevant})"),
 ),
 sec("Applications: jet on plate, bend, Borda mouthpiece", (8, 13),
   ("eq", r"F_{plate} = \rho QV\ (\text{normal jet}),\qquad F_x = (p_1A_1 + \rho QV_1) - (p_2A_2 + \rho QV_2)\cos\theta"),
   ("md", "Borda (re-entrant) mouthpiece: wall pressures are hydrostatic, so momentum gives **C_c = 0.5**."),
 ),
]}

HYD[D["H9"]] = {"code": "CE105", "title": "Hydraulics 9 · Energy principle & head losses", "sections": [
 sec("Mechanical energy of a particle", (1, 3),
   ("md", "Total head H = p/ρg + V²/2g + z; pumps add H_p, turbines remove H_t, friction dissipates h_L."),
 ),
 sec("Energy equation for a control volume", (3, 5),
   ("eq", r"\frac{p_1}{\rho g} + K_e\frac{V_1^2}{2g} + z_1 + H_p = \frac{p_2}{\rho g} + K_e\frac{V_2^2}{2g} + z_2 + H_t + h_L,\qquad P = \rho gQH"),
   ("md", "Valid for steady flow between well-behaved sections; K_e ≈ 1 turbulent, 2 laminar."),
 ),
 sec("Head losses: friction & expansion", (5, 10),
   ("eq", r"h_f = f\frac{L}{D}\frac{V^2}{2g},\qquad h_{exp} = \frac{(V_1 - V_2)^2}{2g}\ (\text{Borda–Carnot}),\qquad h_{exit} = \frac{V^2}{2g}"),
   ("md", "Losses come mainly from **diverging** flow (separation, eddies); converging flow loses little."),
 ),
]}

HYD[D["TQ"]] = {"code": "CE105", "title": "Hydraulics practice · Tutorials 1–4 (questions & answers)", "sections": [
 sec("Tut 1 Q1 Micromanometer", (1, 1),
   ("ex", "Answer", "Reservoir levels stay equal (A_t/A_r small) → **p₁ − p₂ = (γ₂ − γ₁)h**, so h = Δp/(γ₂ − γ₁) is "
          "magnified when the two specific weights are close."),
 ),
 sec("Tut 1 Q2 Oil-spill boom (ρ_oil 873, ρ_sw 1030; L 150 m, draft 0.30 m)", (2, 2),
   ("ex", "Answers", "Equal pressure under the boom: oil depth = (ρ_w/ρ_o)h_D → V_max = (ρ_w/ρ_o)h_DL²/2π = "
          "**1267 m³** (1.6 % of 500 000 bbl) · minimum freeboard/draft = ρ_w/ρ_o − 1 = **0.18** (≈ 1 : 5.6, i.e. "
          "5.4 cm for the 30 cm draft — the extra freeboard covers waves and wind) · lead per extra cm on a 30 m section "
          "= 1030 × 0.01 × 0.10 × 30 = **30.9 kg**."),
   ("tip", "The solution prints the volume as 'm²' and says 'for a 40 cm draft' while using 30 cm — read it as m³ and 30 cm."),
 ),
 sec("Tut 2 Q1 Thin gate holding oil against seawater", (3, 3),
   ("ex", "Answers", "Oil surface z_B = **+0.2 m** · p_D = 10 kPa both sides · below D the seawater pressures cancel · net "
          "normal force 8.5 − 7.1 = 1.4 kN/m → **T_A = W ≈ 1.0 kN/m** · moments about A → z_E = −1.0 m."),
 ),
 sec("Tut 2 Q2 Rectangular dam (B 10 m, H 36 m, μ = 1)", (4, 4),
   ("ex", "Answers", "F_H = ½ρgH² = **6350 kN/m** at 24 m depth · friction 8467 kN/m > F_H → no sliding · overturning "
          "moment 76 200 > restoring 42 335 kNm/m → **overturns** · B_min = √(F_H(H/3)/(½ρ_cgH)) = **13.4 m**."),
 ),
 sec("Tut 3 Q1 Sluice gate (h₁ 6 m, h₂ 3 m)", (5, 5),
   ("eq", r"q = h_1h_2\sqrt{\frac{2g}{h_1 + h_2}}"),
   ("ex", "Answer", "q = 18√(19.6/9) = **26.6 m²/s**."),
 ),
 sec("Tut 3 Q2 Venturi insecticide mixer", (6, 6),
   ("ex", "Answers (Q = 1 gpm = 6.31 × 10⁻⁵ m³/s, Q_A = 1.26 × 10⁻⁶ m³/s)", "Feed-line velocity 11.07 m/s → p₁ = "
          "**−62.7 kPa** (gauge) · nozzle V₃ = 12.7 m/s → V₁ = 16.9 m/s → throat D = **2.2 mm** · for large Q, p₁ ∝ Q² on "
          "both branches, so Q_A/Q → constant (0.02)."),
   ("tip", "The solution writes d_h = 2.5 × 10⁻⁴ m and 'Q = 5Q_A'; the working actually uses d_h = 2.54 mm and Q = 50Q_A."),
 ),
 sec("Tut 4 Q1 Plane jet splitting on a floor", (7, 7),
   ("ex", "Answers", "Vertical force **ρu₀²h₀ sin β** · speeds unchanged (Bernoulli, no gravity) · split "
          "h_R = ½h₀(1 + cos β), h_L = ½h₀(1 − cos β) · gravity error < 5 % for drops up to **≈ 1 m** at 14 m/s."),
 ),
 sec("Tut 4 Q2 Semi-circular gate, q = 10 m²/s", (8, 8),
   ("ex", "Answers", "C_c = 1.0/1.3 = **0.77** (> 0.6 for a sharp vertical gate — the curved lip turns the flow less) · "
          "momentum: F = 193 − 105 = **88 kN/m** · if blocked, hydrostatic on the wetted 4.7 m: **108 kN/m** — larger "
          "because flowing water lowers the pressure near the gate lip."),
 ),
]}

HYD[D["SE"]] = {"code": "CE105", "title": "Hydraulics practice · Self-evaluation questions (worked)", "sections": [
 sec("1 Viscosity", (1, 3),
   ("ex", "1-1 to 1-3", "Film on an incline: τ_wall = 2μU/h = **4 × 10⁻³ Pa** · disc drive head: V = Rω = 532 m/s, "
          "F = μVA/h = **0.15 N** · shaft in bearing: F = ρνU/δ · πDl = **286 N**."),
 ),
 sec("2 Manometers", (4, 5),
   ("ex", "2-1, 2-2", "Pipe B: 60 + 0.8(9.8)(3) + 9.8(2) = **103.1 kPa**; dome C: 30.6 kPa = **229.5 mm Hg** · inverted "
          "U-tube: step A→C→D→B, h from p_A − p_B = −5 kPa."),
 ),
 sec("3 Forces on gates & dams", (6, 8),
   ("ex", "3-1 hinged hatch / 3-2 dam with uplift", "Air pressure to open the hatch p₁ = p_A + ⅔(p_B − p_A) = "
          "**104.5 kPa** · dam: with uplift and h = H the overturning side (5304) < resisting (6539) → always stable."),
 ),
 sec("4 Kinematics & continuity", (9, 11),
   ("ex", "4-1 to 4-3", "Diffuser: a = V₀(1 − x/l)[ce^{−ct} − (V₀/l)(1 − e^{−ct})²] → zero at t = 1 s for **c = 0.49 s⁻¹** "
          "(local and convective terms cancel) · swirl: |V| = K/r, circular streamlines · mixing: ρ = (0.1 + 0.24)/0.4 → "
          "**850 kg/m³**."),
 ),
 sec("5 Bernoulli", (12, 15),
   ("ex", "5-1 to 5-4", "Tank with two outlets: V_B = 7.67, V_D = 11.71 m/s, **Q = 9.1 L/s**, p₁ = 57.8 kPa · jet on plate: "
          "V = 1.59 m/s, Q = 0.2 L/s, H = 0.134 m · conical plug: **p = 154 Pa** · ramp: two physical depths 0.032 m and "
          "5.2 m (third root negative)."),
 ),
 sec("6 Momentum", (16, 18),
   ("ex", "6-1 to 6-3", "Slit device: anchoring **66.7 N** · dredge: thrust ≈ **25.4 kN** · 180° bend: F_x = (2ρV² + p₁ + p₂)A "
          "= **7.4 kN**, F_y = 0."),
 ),
 sec("7 Energy", (19, 20),
   ("ex", "7-1, 7-2", "Siphon: V = √(2g·2.44/1.8) = 5.16 m/s → **Q = 23.4 L/s** · river over rock pile: H₁ 1.39 > H₂ 1.29 m → "
          "flows 1 → 2, **h_L = 0.10 m**."),
 ),
]}

# ------------------------------------------------------------------ Part 2 → CE205
HYD[D["V1"]] = {"code": "CE205", "title": "Hydraulics II-1 · Course map & ways to view flow", "sections": [
 sec("Scope of Part 2", (1, 4),
   ("md", "Tools to view flows; steady pressurised flow in single pipes; elementary pump/turbine performance; "
          "dimensional analysis. Leads to pipe networks, hydrology and open-channel modelling."),
 ),
 sec("Integral vs differential views; real vs ideal", (5, 8),
   ("md", "Flow equations can be written integral/differential and conservative/non-conservative. The full real-fluid "
          "differential equations have more unknowns than equations, so we simplify: **ideal** (inviscid, "
          "incompressible, irrotational) flow → potential flow and flow nets."),
 ),
]}

HYD[D["V2"]] = {"code": "CE205", "title": "Hydraulics II-2 · Stream function & velocity potential", "sections": [
 sec("Stream function ψ", (1, 9),
   ("eq", r"u = \frac{\partial\psi}{\partial y},\quad v = -\frac{\partial\psi}{\partial x};\qquad v_r = \frac{1}{r}\frac{\partial\psi}{\partial\theta},\quad v_\theta = -\frac{\partial\psi}{\partial r};\qquad q_{1\to2} = \psi_2 - \psi_1"),
   ("md", "ψ = constant along a streamline; it satisfies continuity automatically; numbering is arbitrary."),
 ),
 sec("Velocity potential φ", (10, 16),
   ("eq", r"u = \frac{\partial\phi}{\partial x},\quad v = \frac{\partial\phi}{\partial y},\qquad \nabla^2\phi = 0,\ \nabla^2\psi = 0\ (\text{irrotational})"),
   ("md", "Equipotentials are orthogonal to streamlines → **flow nets** (also used for seepage)."),
 ),
]}

HYD[D["V3"]] = {"code": "CE205", "title": "Hydraulics II-3 · Elementary flows, vortices & superposition", "sections": [
 sec("Uniform flow, sources & sinks", (1, 6),
   ("eq", r"\text{uniform: } \psi = Uy - Vx;\qquad \text{source: } \psi = \frac{Q}{2\pi}\theta,\ \phi = \frac{Q}{2\pi}\ln r,\ v_r = \frac{Q}{2\pi r}"),
 ),
 sec("Curved flow; free & forced vortices", (7, 12),
   ("eq", r"\frac{dp}{dr} = \frac{\rho V^2}{r};\qquad \text{free: } V = \frac{C}{r}\ (\text{irrotational}),\qquad \text{forced: } V = \omega r,\ p = \frac{\rho\omega^2r^2}{2}"),
   ("ex", "Forced vortex: Ø350 mm cylinder at 130 rad/s", "Wall pressure ρω²r²/2 = **258.8 kPa**; integrate over the lid "
          "for the plate load."),
 ),
 sec("Superposition: half-body, Rankine oval, cylinder", (13, 21),
   ("md", "Laplace is linear → add solutions. Uniform + source = **half-body** (stagnation where U = Q/2πr). "
          "Source + sink + uniform = Rankine oval; doublet + uniform = cylinder. Limits: no viscosity → no drag "
          "(d'Alembert), no separation."),
 ),
]}

HYD[D["VX"]] = {"code": "CE205", "title": "Hydraulics II-3a · Flow-view examples", "sections": [
 sec("Worked examples", (1, 10),
   ("ex", "Uniform + source (U 60 m/s in −x, Q_s 160 m³/s)", "Stagnation where U = Q_s/2πr → r = 160/(2π × 60) = "
          "**0.424 m**; ψ = 0 traces the half-body surface."),
   ("tip", "The slide text says '106 m³/s' but the working (160θ/2π, r = 0.424 m) uses 160 m³/s."),
   ("ex", "Uniform 5 m/s in +x plus 5 m/s in −y", "ψ = 5y + 5x."),
 ),
]}

HYD[D["R1"]] = {"code": "CE205", "title": "Hydraulics II-4 · Viscosity, laminar & turbulent flow", "sections": [
 sec("Limits of potential flow", (1, 6),
   ("md", "Potential flow gives velocities everywhere and Bernoulli applies across streamlines, but it cannot "
          "produce drag, wakes or losses."),
 ),
 sec("Viscosity & laminar flow", (7, 12),
   ("eq", r"\tau = \mu\frac{du}{dy},\qquad Re = \frac{\rho VL}{\mu} = \frac{VL}{\nu}"),
 ),
 sec("Transition & turbulence", (13, 23),
   ("md", "Disturbances grow when inertia beats viscosity. Pipes: **laminar Re < 2000**, transitional to ~4000, "
          "turbulent above. Turbulence: random fluctuations u = ū + u′, extra Reynolds stress −ρu′v′, flatter mean "
          "profile, much higher mixing and losses; eddy-viscosity and mixing-length models (FYI)."),
 ),
]}

HYD[D["R2"]] = {"code": "CE205", "title": "Hydraulics II-5 · Boundary layers, drag, cavitation", "sections": [
 sec("Boundary layer thicknesses", (1, 6),
   ("eq", r"\delta^* = \int_0^\delta\left(1 - \frac{u}{U}\right)dy,\qquad \theta = \int_0^\delta\frac{u}{U}\left(1 - \frac{u}{U}\right)dy"),
   ("md", "δ = where u = 0.99U. Re_x = Ux/ν; laminar to ~5 × 10⁵ on a flat plate."),
 ),
 sec("Momentum integral (von Kármán)", (7, 10),
   ("eq", r"\tau_0 = \rho U^2\frac{d\theta}{dx}"),
   ("md", "Pick a velocity profile → θ(δ) → τ₀ → δ(x) → integrate τ₀ for the plate drag."),
 ),
 sec("Bluff bodies, roughness, drag & vibration", (11, 14),
   ("eq", r"F_D = C_D\,\tfrac{1}{2}\rho U^2A"),
   ("md", "Adverse pressure gradient → separation → wake (pressure drag dominates). Vortex shedding can excite "
          "structures (St = fD/U ≈ 0.2 for cylinders)."),
 ),
 sec("Bounded flows; cavitation & surface tension", (15, 18),
   ("md", "In pipes the boundary layers meet → **fully developed** flow after the entrance length. Cavitation when local "
          "p falls to vapour pressure (pump suctions, valves) — damages surfaces."),
 ),
]}

HYD[D["RX"]] = {"code": "CE205", "title": "Hydraulics II-5a · Real-fluid examples (solutions)", "sections": [
 sec("Example 1 1/7-power boundary layer in a channel", (1, 4),
   ("ex", "Depth 0.5 m, surface 2 m/s, δ = 0.2 m", "Re = 1000 × 2 × 0.5/1.14 × 10⁻³ = 8.8 × 10⁵ → turbulent · "
          "δ* = δ/8 = **0.025 m** · θ = 7δ/72 = **0.0194 m**."),
 ),
 sec("Example 2 plate drag", (5, 8),
   ("md", "Momentum-integral method: assume the profile, get θ(δ), substitute an empirical τ₀(Re_δ), solve for δ(x) "
          "and integrate τ₀ along the plate for the drag — same steps as HW1 Q12."),
 ),
]}

HYD[D["Q1"]] = {"code": "CE205", "title": "Hydraulics II-6 · Pipe flow: momentum & laminar flow", "sections": [
 sec("Insight from mass, energy & momentum", (5, 10),
   ("eq", r"\tau_0 = \frac{\rho g h_f D}{4L},\qquad \tau(r) = -\frac{r}{2}\frac{dp^*}{dx}\ (\text{linear in } r),\quad p^* = p + \rho gz"),
 ),
 sec("Laminar (Hagen–Poiseuille)", (11, 15),
   ("eq", r"u(r) = \frac{-dp^*/dx}{4\mu}(R^2 - r^2),\quad u_{max} = 2V,\quad h_f = \frac{32\mu LV}{\rho gD^2},\quad f = \frac{64}{Re}"),
 ),
 sec("Example: oil in a Ø25 mm pipe at 0.3 m/s", (16, 16),
   ("ex", "ρ 800, μ 0.048, L 45 m", "Re = 125 (laminar) · h_f = **4.23 m** of oil (Δp = 33.2 kPa) · u_max = **0.6 m/s**, "
          "u at 5 mm from wall = 0.6(1 − 0.6²) = **0.384 m/s**."),
 ),
]}

HYD[D["Q2"]] = {"code": "CE205", "title": "Hydraulics II-7 · Turbulent pipe friction & minor losses", "sections": [
 sec("Darcy–Weisbach & friction factor", (1, 8),
   ("eq", r"h_f = f\frac{L}{D}\frac{V^2}{2g},\qquad \frac{1}{\sqrt f} = -2\log_{10}\left(\frac{k_s/D}{3.7} + \frac{2.51}{Re\sqrt f}\right)\ (\text{Colebrook–White})"),
   ("eq", r"\text{Haaland: } \frac{1}{\sqrt f} = -1.8\log_{10}\left[\left(\frac{k_s/D}{3.7}\right)^{1.11} + \frac{6.9}{Re}\right]"),
   ("md", "Nikuradse: laminar, smooth turbulent (Blasius f = 0.316Re^{-1/4}), transitional, fully rough "
          "(f depends only on k_s/D). Moody chart combines them; typical k_s: glass/Perspex ~0, new steel 0.045 mm, "
          "concrete 0.3–3 mm."),
 ),
 sec("Three problem types", (9, 14),
   ("steps", ["Type 1 — find h_f (or pump pressure) given Q, D: direct (Re, k/D → f → h_f).",
              "Type 2 — find Q given h_f, D: iterate on f, or use the explicit Swamee–Jain form for V.",
              "Type 3 — find D given Q, h_f: iterate (guess D → f → h_f) until it matches."]),
   ("ex", "Type 1: 0.01 m³/s through 75 mm smooth pipe, 100 m, into a 10 m reservoir", "V = 2.26 m/s, Re 1.7 × 10⁵, "
          "f ≈ 0.0164 → p₁/ρg ≈ **15.3 m** → p₁ ≈ 153 kPa (g = 10)."),
 ),
 sec("Hazen–Williams (practical)", (15, 15),
   ("eq", r"V = 0.849\,C\,R^{0.63}S^{0.54}\quad(\text{SI},\ R = D/4)"),
 ),
 sec("Minor (local) losses", (16, 19),
   ("eq", r"h_m = K\frac{V^2}{2g},\qquad K_{exp} = \left(1 - \frac{A_1}{A_2}\right)^2,\qquad K_{contr} = \left(\frac{1}{C_c} - 1\right)^2"),
   ("md", "Entrance sharp 0.5, rounded ≈ 0.05; exit 1.0; bends, valves from tables."),
 ),
]}

HYD[D["QX"]] = {"code": "CE205", "title": "Hydraulics II-7a · Pipe-flow worked examples", "sections": [
 sec("Laminar & Type 1", (1, 6),
   ("ex", "See II-6 (oil) and II-7 (pump pressure 15.3 m)", "Use the Moody chart or Colebrook; check Re first."),
 ),
 sec("Type 2 and Type 3 iterations", (7, 10),
   ("md", "Type 2 (oil ρ 950, ν 2 × 10⁻⁵): unknown V → guess f, compute V and Re, update f until stable. Type 3 "
          "(Q = 0.34 m³/s): guess D → V, Re, k/D → f → h_f; repeat until h_f matches the allowed value."),
 ),
]}

HYD[D["M1"]] = {"code": "CE205", "title": "Hydraulics II-8 · Pumps & turbines", "sections": [
 sec("Types of machinery", (1, 7),
   ("md", "Turbines extract energy, pumps add it. **Positive displacement** (small Q, large H; reciprocating, screw) vs "
          "**rotodynamic** (centrifugal/radial for high H, mixed and axial for large Q, low H; need priming)."),
 ),
 sec("Radial pump: velocity triangles & Euler head", (8, 13),
   ("eq", r"T = \rho Q(r_2V_{t2} - r_1V_{t1}),\qquad H_{ideal} = \frac{u_2V_{t2} - u_1V_{t1}}{g},\qquad u = r\omega"),
   ("md", "Real head < ideal: impeller and volute friction, shock at off-design, leakage/recirculation. Efficiency "
          "η = ρgQH/P_shaft. Cavitation risk if suction pressure is too low (check NPSH available > required)."),
 ),
 sec("Other rotodynamic pumps; example", (14, 15),
   ("md", "Mixed- and axial-flow pumps for drainage and large flows. Select the pump so the operating point (pump "
          "H–Q curve ∩ system curve H = Δz + kQ²) lies near peak efficiency."),
 ),
]}

HYD[D["HW"]] = {"code": "CE205", "title": "Hydraulics II practice · Homework 1 steps", "sections": [
 sec("HW1 Q9–Q12", (1, 7),
   ("ex", "Key results", "Q9 uniform 30 m/s + source 60 m³/s → stagnation at r = 60/(2π·30) = **0.318 m** · Q10–11 "
          "Reynolds-number checks · Q12 turbulent plate drag: Re_δ = 9.98 × 10⁶δ, δ = 0.0148x^{0.8}, "
          "τ₀ = 165x^{−0.2} → integrate → **F_s ≈ 82.5 N**."),
   ("md", "HW1 Q1–Q2 (Part 1): forces on a submerged trapezoidal block and a multi-fluid manometer — work them with "
          "the fluid-statics rules."),
 ),
]}
