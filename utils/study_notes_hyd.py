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
   ("md", "Fundamental dimensions **M, L, T**: $[V] = L/T$, $[a] = L/T^2$, $[F] = ML/T^2$. A physical "
          "equation must be dimensionally homogeneous: (A) both sides have the same dimension, (B) every term "
          "of a sum has the same dimension, (C) arguments of exp, log, trig functions are dimensionless (e.g. "
          r"the log-law $u = (u_*/\kappa)\ln(z/z_0)$)."),
 ),
 sec("Working habit", (3, 4),
   ("steps", [r"Write symbols (g, $\rho$), not numbers with units.", "Manipulate symbolically to the end.",
              "Check homogeneity before substituting numbers.", "Always write units with the answer."]),
 ),
]}

HYD[D["H2"]] = {"code": "CE105", "title": "Hydraulics 2 · Fluid properties", "sections": [
 sec("Fluid vs solid; stress convention", (1, 2),
   ("md", "A fluid cannot resist shear at rest, however small. At rest the stress tensor is isotropic: "
          r"$T_{ij} = -p \delta_{ij}$. $T_{ij}$ acts on face i in direction j; positive on a positive face in "
          "+j."),
 ),
 sec("Viscosity & no-slip", (2, 4),
   ("eq", r"\tau = \mu\frac{du}{dn},\qquad \nu = \frac{\mu}{\rho}\ [\mathrm{m^2/s}]"),
   ("md", r"Newtonian fluids (water, air) have constant $\mu$ at a given temperature ($\mu$ falls with T for "
          r"liquids). Real fluids obey **no-slip** at walls; an ideal fluid has $\mu = 0$ and may slip."),
 ),
 sec("Continuum & compressibility", (4, 7),
   ("eq", r"E_v = -\frac{dp}{dV/V} = \frac{dp}{d\rho/\rho},\qquad Kn = \frac{\lambda_{mfp}}{L} \ll 1"),
   ("md", r"Water $E_v = 2.15\ \mathrm{GPa}$: 100 MPa (10 km of water) changes density only ~5 % → treat as "
          "**incompressible** (conservation of volume)."),
 ),
]}

HYD[D["H3"]] = {"code": "CE105", "title": "Hydraulics 3 · Fluid statics, forces on surfaces, buoyancy & stability", "sections": [
 sec("Pressure at a point & hydrostatic law", (1, 5),
   ("eq", r"\frac{dp}{dz} = -\rho g\ \Rightarrow\ p + \rho gz = \text{const},\qquad \frac{p}{\rho g} + z = \text{piezometric head},\qquad p_{gauge} = \rho gh"),
   ("md", "Pressure is isotropic (a scalar); pressure force acts normal to and into the surface. Same fluid, same "
          "level → same pressure."),
 ),
 sec("Transmission, piezometer & manometers", (6, 9),
   ("md", r"Hydraulic jack: $F_2 = F_1A_2/A_1$. Piezometer: $p_A = \rho gh$ (gauge only). U-tube: step through "
          r"each fluid with $p + \rho gz$ = const; for a differential manometer between two points of a "
          "flowing pipe,"),
   ("eq", r"\left(\frac{p_A}{\rho g} + z_A\right) - \left(\frac{p_F}{\rho g} + z_F\right) = \Delta h\left(\frac{\rho_m}{\rho} - 1\right)"),
 ),
 sec("Plane surfaces", (10, 16),
   ("eq", r"F = p_cA = \rho gh_cA,\qquad y_{cp} = y_c + \frac{I_{xc}}{y_cA}\quad(\text{along the plane};\ \text{for a vertical wall from the surface } h_{cp} = 2H/3)"),
   ("md", "Inclined surface: horizontal component = force on its vertical projection; vertical component = weight of "
          "water above. Submerged gate: split the trapezoid into a uniform block (through centroid) + triangle. "
          "The centre of pressure approaches the centroid as depth increases."),
 ),
 sec("Curved surfaces", (17, 19),
   ("md", "$F_H$ = force on the projection onto a vertical plane (acts at its centre of pressure). $F_V$ = "
          "weight of the (real or imaginary) fluid column above the surface, through its centroid. 2-D "
          "resultant passes through the intersection of the two lines of action."),
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
   ("md", r"Eulerian description: fields V(x, y, z, t). Steady ($\partial /\partial t = 0$) vs unsteady; "
          "uniform vs non-uniform; 1-D/2-D/3-D."),
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
   ("md", r"Streamlines contract after a sharp orifice: $C_c \approx 0.61$ sharp-edged, ≈ 0.5 re-entrant "
          "(Borda), ≈ 1 rounded."),
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
   ("md", "$b = 1$ gives mass conservation; $b = V$ gives momentum; $b = e$ gives energy."),
 ),
]}

HYD[D["H8"]] = {"code": "CE105", "title": "Hydraulics 8 · Momentum principle", "sections": [
 sec("Linear momentum for a control volume", (1, 5),
   ("eq", r"\sum\mathbf F = \frac{\partial}{\partial t}\int_{CV}\rho\mathbf V\,dV + \sum_{out}\rho Q K_m\mathbf V - \sum_{in}\rho Q K_m\mathbf V"),
   ("md", r"$K_m \approx 1$ for turbulent flow (4/3 laminar). Define the **hydraulic thrust** on a flow area, "
          r"$\mathrm{MP} = (p + \rho V^2)A$, always pointing into the CV; at a free jet $p = 0$."),
 ),
 sec("Steady flow: sum of thrusts + wall force = 0", (6, 7),
   ("eq", r"\sum MP_i + \mathbf F_{wall\to fluid} = 0\quad(\text{gravity added if relevant})"),
 ),
 sec("Applications: jet on plate, bend, Borda mouthpiece", (8, 13),
   ("eq", r"F_{plate} = \rho QV\ (\text{normal jet}),\qquad F_x = (p_1A_1 + \rho QV_1) - (p_2A_2 + \rho QV_2)\cos\theta"),
   ("md", r"Borda (re-entrant) mouthpiece: wall pressures are hydrostatic, so momentum gives $\boldsymbol{C_c "
          "= 0.5}$."),
 ),
]}

HYD[D["H9"]] = {"code": "CE105", "title": "Hydraulics 9 · Energy principle & head losses", "sections": [
 sec("Mechanical energy of a particle", (1, 3),
   ("md", r"Total head $H = p/\rho g + V^2/2g + z$; pumps add $H_p$, turbines remove $H_t$, friction "
          "dissipates $h_L$."),
 ),
 sec("Energy equation for a control volume", (3, 5),
   ("eq", r"\frac{p_1}{\rho g} + K_e\frac{V_1^2}{2g} + z_1 + H_p = \frac{p_2}{\rho g} + K_e\frac{V_2^2}{2g} + z_2 + H_t + h_L,\qquad P = \rho gQH"),
   ("md", r"Valid for steady flow between well-behaved sections; $K_e \approx 1$ turbulent, 2 laminar."),
 ),
 sec("Head losses: friction & expansion", (5, 10),
   ("eq", r"h_f = f\frac{L}{D}\frac{V^2}{2g},\qquad h_{exp} = \frac{(V_1 - V_2)^2}{2g}\ (\text{Borda–Carnot}),\qquad h_{exit} = \frac{V^2}{2g}"),
   ("md", "Losses come mainly from **diverging** flow (separation, eddies); converging flow loses little."),
 ),
]}

# Practice pages (tutorial questions as q blocks) live in utils/study_notes_hydq.py.

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
 sec(r"Stream function $\psi$", (1, 9),
   ("eq", r"u = \frac{\partial\psi}{\partial y},\quad v = -\frac{\partial\psi}{\partial x};\qquad v_r = \frac{1}{r}\frac{\partial\psi}{\partial\theta},\quad v_\theta = -\frac{\partial\psi}{\partial r};\qquad q_{1\to2} = \psi_2 - \psi_1"),
   ("md", r"$\psi$ = constant along a streamline; it satisfies continuity automatically; numbering is "
          "arbitrary."),
 ),
 sec(r"Velocity potential $\phi$", (10, 16),
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
   ("ex", "Forced vortex: Ø350 mm cylinder at 130 rad/s", r"Wall pressure $\rho\omega^2r^2/2 = "
                                                          r"\boldsymbol{258.8\ \mathrm{kPa}}$; integrate over "
                                                          "the lid for the plate load."),
 ),
 sec("Superposition: half-body, Rankine oval, cylinder", (13, 21),
   ("md", r"Laplace is linear → add solutions. Uniform + source = **half-body** (stagnation where $U = Q/2\pi "
          "r$). Source + sink + uniform = Rankine oval; doublet + uniform = cylinder. Limits: no viscosity → "
          "no drag (d'Alembert), no separation."),
 ),
]}

HYD[D["VX"]] = {"code": "CE205", "title": "Hydraulics II-3a · Flow-view examples", "sections": [
 sec("Worked examples", (1, 10),
   ("ex", r"Uniform + source (U 60 m/s in −x, $Q_s = 160\ \mathrm{m^3/s}$)", r"Stagnation where $U = Q_s/2\pi r$ → $r = "
                                                             r"160/(2\pi \times 60) = \boldsymbol{0.424\ "
                                                             r"\mathrm{m}}$; $\psi = 0$ traces the half-body "
                                                             "surface."),
   ("tip", r"The slide text says '$106\ \mathrm{m^3/s}$' but the working ($160\theta/2\pi$, $r = 0.424\ "
           r"\mathrm{m}$) uses $160\ \mathrm{m^3/s}$."),
   ("ex", "Uniform 5 m/s in +x plus 5 m/s in −y", r"$\psi = 5y + 5x$."),
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
   ("md", r"Disturbances grow when inertia beats viscosity. Pipes: **laminar $\mathrm{Re} < 2000$**, "
          r"transitional to ~4000, turbulent above. Turbulence: random fluctuations $u = \bar{u} + u'$, extra "
          r"Reynolds stress $-\rho u'v'$, flatter mean profile, much higher mixing and losses; eddy-viscosity "
          "and mixing-length models (FYI)."),
 ),
]}

HYD[D["R2"]] = {"code": "CE205", "title": "Hydraulics II-5 · Boundary layers, drag, cavitation", "sections": [
 sec("Boundary layer thicknesses", (1, 6),
   ("eq", r"\delta^* = \int_0^\delta\left(1 - \frac{u}{U}\right)dy,\qquad \theta = \int_0^\delta\frac{u}{U}\left(1 - \frac{u}{U}\right)dy"),
   ("md", r"$\delta$ = where $u = 0.99U$. $Re_x = Ux/\nu$; laminar to ~$5 \times 10^5$ on a flat plate."),
 ),
 sec("Momentum integral (von Kármán)", (7, 10),
   ("eq", r"\tau_0 = \rho U^2\frac{d\theta}{dx}"),
   ("md", r"Pick a velocity profile → $\theta(\delta)$ → $\tau_0$ → $\delta(x)$ → integrate $\tau_0$ for the "
          "plate drag."),
 ),
 sec("Bluff bodies, roughness, drag & vibration", (11, 14),
   ("eq", r"F_D = C_D\,\tfrac{1}{2}\rho U^2A"),
   ("md", "Adverse pressure gradient → separation → wake (pressure drag dominates). Vortex shedding can "
          r"excite structures ($St = fD/U \approx 0.2$ for cylinders)."),
 ),
 sec("Bounded flows; cavitation & surface tension", (15, 18),
   ("md", "In pipes the boundary layers meet → **fully developed** flow after the entrance length. Cavitation when local "
          "p falls to vapour pressure (pump suctions, valves) — damages surfaces."),
 ),
]}

HYD[D["RX"]] = {"code": "CE205", "title": "Hydraulics II-5a · Real-fluid examples (solutions)", "sections": [
 sec("Example 1 1/7-power boundary layer in a channel", (1, 4),
   ("ex", r"Depth 0.5 m, surface 2 m/s, $\delta = 0.2\ \mathrm{m}$", r"$\mathrm{Re} = 1000 \times 2 \times "
                                                                     r"0.5/1.14 \times 10^{-3} = 8.8 \times "
                                                                     r"10^5$ → turbulent · $\delta^* = "
                                                                     r"\delta/8 = \boldsymbol{0.025\ "
                                                                     r"\mathrm{m}}$ · $\theta = 7\delta/72 = "
                                                                     r"\boldsymbol{0.0194\ \mathrm{m}}$."),
 ),
 sec("Example 2 plate drag", (5, 8),
   ("md", r"Momentum-integral method: assume the profile, get $\theta(\delta)$, substitute an empirical "
          r"$\tau_0(Re_{\delta})$, solve for $\delta(x)$ and integrate $\tau_0$ along the plate for the drag — "
          "same steps as HW1 Q12."),
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
   ("ex", r"$\rho$ 800, $\mu$ 0.048, L 45 m", r"$\mathrm{Re} = 125$ (laminar) · $h_f = \boldsymbol{4.23\ \mathrm{m}}$ of "
                                    r"oil ($\Delta p = 33.2\ \mathrm{kPa}$) · $u_{\mathrm{max}} = "
                                    r"\boldsymbol{0.6\ \mathrm{m/s}}$, u at 5 mm from wall = $0.6(1 - 0.6^2) = "
                                    r"\boldsymbol{0.384\ \mathrm{m/s}}$."),
 ),
]}

HYD[D["Q2"]] = {"code": "CE205", "title": "Hydraulics II-7 · Turbulent pipe friction & minor losses", "sections": [
 sec("Darcy–Weisbach & friction factor", (1, 8),
   ("eq", r"h_f = f\frac{L}{D}\frac{V^2}{2g},\qquad \frac{1}{\sqrt f} = -2\log_{10}\left(\frac{k_s/D}{3.7} + \frac{2.51}{Re\sqrt f}\right)\ (\text{Colebrook–White})"),
   ("eq", r"\text{Haaland: } \frac{1}{\sqrt f} = -1.8\log_{10}\left[\left(\frac{k_s/D}{3.7}\right)^{1.11} + \frac{6.9}{Re}\right]"),
   ("md", r"Nikuradse: laminar, smooth turbulent (Blasius $f = 0.316\,\mathrm{Re}^{-1/4}$), transitional, "
          "fully rough (f depends only on $k_s/D$). Moody chart combines them; typical $k_s$: glass/Perspex "
          "~0, new steel 0.045 mm, concrete 0.3–3 mm."),
 ),
 sec("Three problem types", (9, 14),
   ("steps", ["Type 1 — find $h_f$ (or pump pressure) given Q, D: direct (Re, k/D → f → $h_f$).",
              "Type 2 — find Q given $h_f$, D: iterate on f, or use the explicit Swamee–Jain form for V.",
              "Type 3 — find D given Q, $h_f$: iterate (guess D → f → $h_f$) until it matches."]),
   ("ex", r"Type 1: $0.01\ \mathrm{m^3/s}$ through 75 mm smooth pipe, 100 m, into a 10 m reservoir", "$V = "
                                                                                                     r"2.26\ "
                                                                                                     r"\mathrm{m/s}$, "
                                                                                                     r"$\mathrm{Re} "
                                                                                                     "= 1.7 "
                                                                                                     r"\times "
                                                                                                     "10^5$, "
                                                                                                     "$f "
                                                                                                     r"\approx "
                                                                                                     "0.0164$ "
                                                                                                     "→ "
                                                                                                     r"$p_1/\rho "
                                                                                                     "g "
                                                                                                     r"\approx "
                                                                                                     r"\boldsymbol{15.3\ "
                                                                                                     r"\mathrm{m}}$ "
                                                                                                     "→ $p_1 "
                                                                                                     r"\approx "
                                                                                                     r"153\ "
                                                                                                     r"\mathrm{kPa}$ "
                                                                                                     "($g = "
                                                                                                     "10$)."),
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
   ("md", r"Type 2 (oil $\rho$ 950, $\nu = 2 \times 10^{-5}$): unknown V → guess f, compute V and Re, update f "
          r"until stable. Type 3 ($Q = 0.34\ \mathrm{m^3/s}$): guess D → V, Re, k/D → f → $h_f$; repeat until "
          "$h_f$ matches the allowed value."),
 ),
]}

HYD[D["M1"]] = {"code": "CE205", "title": "Hydraulics II-8 · Pumps & turbines", "sections": [
 sec("Types of machinery", (1, 7),
   ("md", "Turbines extract energy, pumps add it. **Positive displacement** (small Q, large H; reciprocating, screw) vs "
          "**rotodynamic** (centrifugal/radial for high H, mixed and axial for large Q, low H; need priming)."),
 ),
 sec("Radial pump: velocity triangles & Euler head", (8, 13),
   ("eq", r"T = \rho Q(r_2V_{t2} - r_1V_{t1}),\qquad H_{ideal} = \frac{u_2V_{t2} - u_1V_{t1}}{g},\qquad u = r\omega"),
   ("md", "Real head < ideal: impeller and volute friction, shock at off-design, leakage/recirculation. "
          r"Efficiency $\eta = \rho gQH/P_{\mathrm{shaft}}$. Cavitation risk if suction pressure is too low "
          "(check NPSH available > required)."),
 ),
 sec("Other rotodynamic pumps; example", (14, 15),
   ("md", "Mixed- and axial-flow pumps for drainage and large flows. Select the pump so the operating point "
          r"(pump H–Q curve ∩ system curve $H = \Delta z + kQ^2$) lies near peak efficiency."),
 ),
]}

