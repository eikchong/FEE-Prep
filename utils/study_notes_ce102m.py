"""CE102 lecture decks rewritten in full (CE1101 Mechanics of Materials M1–M5), slide by slide, with every worked
example as a q block carrying the slide's own solution. Homework examples without a solution on the slides are
marked "not provided yet" (src="none")."""
from utils.qblock import q

M1 = "CE102/CE1101_M1_Axial_Force_Members.pdf"


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


MOM = {}

MOM[M1] = {"code": "CE102", "title": "M1 · Introduction & axial force members", "sections": [
 sec("What mechanics of materials adds to statics", (1, 5),
   ("md", "In statics a loaded body is assumed rigid: a bar of length L under axial load P stays length L. Real "
          "bars stretch, and they also get thinner sideways. Mechanics of materials (MOM) describes the **stress** "
          "and **deformation** in a structure through three links:"),
   ("steps", ["**Stress–force** relationship (how internal forces spread over a section) — the criterion used in "
              "design;",
              "**strain–deformation** relationship (how a change of length or angle relates to strain);",
              "**stress–strain** relationship of the material (constitutive law)."]),
   ("md", "Structures covered: bars under axial load (M1), shafts under torsion (M2), beams (M3–M5).\n\n"
          "- **Statically determinate**: FBDs + equilibrium give the forces; the stress–strain law gives the "
          "deformation.\n- **Statically indeterminate**: equilibrium alone is not enough — add a **compatibility** "
          "condition from the geometry of the deformed structure."),
 ),
 sec("Stress: normal, shear and sign convention", (6, 9),
   ("eq", r"\sigma = \lim_{\Delta A \to 0}\frac{\Delta F_n}{\Delta A},\qquad \tau = \lim_{\Delta A \to 0}\frac{\Delta V}{\Delta A}"),
   ("md", r"At a point the state of stress has three normal stresses ($\sigma_{xx}$, $\sigma_{yy}$, $\sigma_{zz}$) "
          r"and shear stresses with $\tau_{xy} = \tau_{yx}$, $\tau_{yz} = \tau_{zy}$, $\tau_{zx} = \tau_{xz}$ — so six "
          r"independent components. In $\tau_{ij}$, i is the face the stress acts on and j its direction."),
   ("md", "**Sign convention:** a stress on a positive face acting in the positive direction is positive; so is a "
          "stress on a negative face acting in the negative direction. Mixed (positive face, negative direction or "
          "the reverse) is negative. Tension is positive."),
   ("eq", r"\sigma_{avg} = \frac{P}{A};\qquad \text{single shear: } \tau_{avg} = \frac{P}{A};\qquad \text{double shear: } \tau_{avg} = \frac{P}{2A}"),
   ("md", "A pin in **double shear** is cut on two planes, so each plane carries half the member force."),
 ),
 sec("Strain, the stress–strain curve and Hooke's law", (10, 13),
   ("eq", r"\varepsilon = \frac{\Delta L}{L}\ \text{(engineering normal strain)},\qquad \gamma_{xy} = \frac{\pi}{2} - \theta'\ \text{(rad)}"),
   ("md", r"Engineering shear strain is the decrease of an originally right angle; $\gamma_{xy}$ is negative if the "
          r"angle opens beyond $\pi/2$."),
   ("md", r"Uniaxial test on mild steel: linear elastic with slope **E** to yield (strain about 0.0012), a perfectly "
          r"plastic plateau to about 0.014, then strain hardening up to the ultimate stress and failure at about 0.25 "
          "strain."),
   ("eq", r"\text{Poisson: } \varepsilon_{yy} = \varepsilon_{zz} = -\nu\varepsilon_{xx} = -\nu\frac{\sigma_{xx}}{E}\quad\text{(uniaxial load in x)}"),
   ("eq", r"\varepsilon_{xx} = \frac{1}{E}\left[\sigma_{xx} - \nu(\sigma_{yy} + \sigma_{zz})\right],\quad \varepsilon_{yy} = \frac{1}{E}\left[\sigma_{yy} - \nu(\sigma_{zz} + \sigma_{xx})\right],\quad \varepsilon_{zz} = \frac{1}{E}\left[\sigma_{zz} - \nu(\sigma_{xx} + \sigma_{yy})\right]"),
   ("eq", r"\gamma_{xy} = \frac{\tau_{xy}}{G},\quad \gamma_{yz} = \frac{\tau_{yz}}{G},\quad \gamma_{zx} = \frac{\tau_{zx}}{G}"),
   ("md", "This **generalised Hooke's law** superposes the strains from each normal stress. Shear stresses cause "
          "only their own shear strain — no normal strain and no shear strain in the other planes."),
 ),
 sec("Allowable stress, factor of safety and pin design", (14, 18),
   ("eq", r"n_s = \frac{\sigma_{failure}}{\sigma_{allowable}} = \frac{P_{failure}}{P_{allowable}} \ge 1"),
   ("md", r"The value of $n_s$ depends on the material and the application. Pins in pin-jointed mechanisms (e.g. a "
          "bike's soft-ride suspension) are sized from the shear force they carry."),
   q("CE1101 M1 Example 1.1",
     r"A mountain-bike suspension is designed for a maximum load $P = 1800\ \mathrm{N}$. Pins B and D are in double "
     r"shear, with ultimate shear stress $\tau_{\mathrm{ult}} = 150\ \mathrm{MPa}$ and a factor of safety of 2. Member "
     r"BC is inclined at 60°; P acts 400 + 100 mm from D, and B is 100 mm from D horizontally and 30 mm vertically. "
     r"Find the minimum diameters of pins B and D.",
     r"**$F_{BC} = 8858\ \mathrm{N}$, $D_x = 4429$, $D_y = 5871\ \mathrm{N}$ → $d_B = 8.67\ \mathrm{mm}$, $d_D = "
     r"7.9\ \mathrm{mm}$.**",
     r"Moments about D on ABD: $P(0.5) - F_{BC}\sin 60^\circ(0.1) - F_{BC}\cos 60^\circ(0.03) = 0$. Then $\sum F_x$, "
     r"$\sum F_y$ give $D_x$, $D_y$; $V_D = \sqrt{D_x^2 + D_y^2} = 7354.5\ \mathrm{N}$. Double shear: $\tau = "
     r"(V/2)/(\pi d^2/4) \le \tau_{\mathrm{ult}}/SF$ → $d = \sqrt{2V \cdot SF/(\pi\tau_{\mathrm{ult}})}$.",
     figure="p. 16: suspension linkage ABD with link BC.")),
 sec("Cast-in anchors: comparing failure modes", (19, 25),
   ("md", "Precast units are lifted on cast-in steel anchors. The anchor can fail by (a) a concrete shear cylinder, "
          "(b) a concrete cone at 45° in tension to two-thirds depth plus a shear cylinder below, (c) a full concrete "
          "tension cone, or (d) tension in the bolt. Work out P for each mode from the failure surface and the "
          "material strength; **the smallest P governs**."),
   ("eq", r"\text{cone (frustum) side area: } A = \pi(r_1 + r_2)s;\qquad \text{cylinder: } A = \pi a h;\qquad P = N\sin 45^\circ + V"),
   q("CE1101 M1 Example 1.2",
     r"A cast-in anchor has $a = 30\ \mathrm{mm}$, embedment $h = 100\ \mathrm{mm}$ and bolt diameter $d = 10\ "
     r"\mathrm{mm}$. Concrete ultimate tensile and shear stresses are 3 and 4.5 MPa; the bolt's ultimate tensile "
     r"stress is 620 MPa. Which of the four failure modes (a)–(d) is most likely?",
     r"**(a) 42.41 kN · (b) 74.8 kN · (c) 173.3 kN · (d) 48.69 kN → (a), concrete shear along the cylinder, governs "
     r"at 42.4 kN.**",
     r"(a) $A = \pi ah = 9424.8\ \mathrm{mm^2}$, $P = 4.5A$. (b) cone to $\tfrac23h$: $A = \pi(a/2 + a/2 + \tfrac23h)"
     r"\sqrt2 \cdot \tfrac23h = 28\,632\ \mathrm{mm^2}$ → $N = 3A$; shear cylinder below: $A = \pi a \cdot h/3 = 3141.6$ "
     r"→ $V = 4.5A$; $P = N\sin 45^\circ + V$. (c) full cone: $A = 57\,757\ \mathrm{mm^2}$; the slide takes $P = 3A = 173.3\ \mathrm{kN}$ (with the 45° "
     r"component, as in (b), it would be 122.5 kN — not governing either way). "
     r"(d) $P = 620 \times \pi \times 10^2/4$.",
     figure="pp. 20–21: the four failure surfaces.")),
 sec("Deformation of axially loaded members", (26, 29),
   ("eq", r"\sigma = \frac{P}{A},\qquad \varepsilon = \frac{\sigma}{E} = \frac{P}{EA},\qquad \delta = \varepsilon L = \frac{PL}{EA}"),
   ("eq", r"\text{stepped bar: } \delta = \sum_{i=1}^{n}\frac{P_iL_i}{A_iE_i};\qquad \text{varying section or load: } \delta = \int_0^L\frac{P(x)}{A(x)E}\,dx"),
   ("md", r"Use the **internal** axial force in each segment, found by cutting the bar and drawing an FBD — not the "
          r"applied loads. Example from the slide: a bar with $P_1$ at the end of part 1 and $P_2$ at the joint has "
          r"$\delta = (P_2 - P_1)a/(E_1A_1) + P_2b/(E_2A_2)$ with the signs of the internal forces."),
 ),
 sec("Indeterminacy and compatibility", (30, 31),
   ("eq", r"\text{degree of indeterminacy} = \text{number of unknowns} - \text{number of equilibrium equations}"),
   ("md", "Examples from the slide: a bar fixed at one end (1 unknown, 1 equation) is determinate; a beam with a "
          "fixed end and a roller (3 unknowns, 2 equations) is indeterminate to the first degree."),
   ("steps", [r"Equilibrium: $\sum F = 0$ (e.g. $R_A + R_B = P$ for a bar between two walls).",
              r"Compatibility: the deformed geometry (e.g. total $\delta_{AB} = 0$ between rigid supports).",
              r"Force–deformation: $\delta = PL/EA$ for each segment; solve the equations together."]),
 ),
 sec("Truss deflections from member deformations", (32, 35),
   ("md", "Truss members only lengthen or shorten, but every member must stay connected at the joints, so the "
          "joints move to fit all the new member lengths. Find each member force, its change of length "
          r"$\delta = FL/AE$, then use the geometry of the displaced joint."),
   q("CE1101 M1 Example 1.3",
     r"A two-member truss (A and B on supports 3 m apart, apex C 2 m above the midpoint) carries $P = 15\ "
     r"\mathrm{kN}$ down at C. Members are steel ($E = 200\ \mathrm{GPa}$) with $A = 100\ \mathrm{mm^2}$. Find the "
     r"vertical displacement of C.",
     r"**$F_{AC} = F_{BC} = 9.375\ \mathrm{kN}$ (compression), each shortens 1.17 mm → $(\delta_C)_V = 1.17/(4/5) = "
     r"1.46\ \mathrm{mm}$ down.**",
     r"$L = \sqrt{2^2 + 1.5^2} = 2.5\ \mathrm{m}$, $\cos\theta = 4/5$ from the vertical. Joint C: $2F\cos\theta = P$. "
     r"$\delta = 9375 \times 2500/(100 \times 200\,000)$. By symmetry C moves straight down, and the member shortening "
     r"is the component of that movement along the member.", figure="p. 33.")),
 sec("Piles with skin friction", (36, 41),
   ("md", "Piles (driven or bored, onshore or offshore) carry load by skin friction along the shaft and end bearing "
          "at the toe. A **pile load test** (kentledge of concrete blocks on a steel beam, hydraulic jacks) checks a "
          "few piles to confirm the calculated capacity. With friction varying along the pile, the internal force "
          "varies too, so integrate for the shortening."),
   q("CE1101 M1 Example 1.4",
     r"Stacked blocks put $P = 2000\ \mathrm{kN}$ on a 300 mm diameter, 12 m bored pile ($E = 30\ \mathrm{GPa}$). "
     r"Skin friction rises linearly from zero at the toe to $p_0$ (kN/m) at the top, and the end bearing is $F = 400\ "
     r"\mathrm{kN}$. Find (a) $p_0$ and (b) the elastic shortening (ignore self-weight).",
     r"**(a) $p_0 = 266.67\ \mathrm{kN/m}$ · (b) $\delta = 5.28\ \mathrm{mm}$.**",
     r"(a) $2000 = 400 + \tfrac12p_0(12)$. With y up from the toe, $p(y) = 22.22y$ kN/m and the internal force "
     r"$P(y) = 400 + 11.11y^2$ kN. (b) $\delta = \int_0^{12}(400 + 11.11y^2) \times 10^3\,dy/[\pi(0.15)^2 \times 30 "
     r"\times 10^9]$.", figure="p. 38."),
   q("CE1101 M1 Example 1.5 (homework)",
     r"A wooden sofa leg is a tapered cylinder (radius $r_1 = 10\ \mathrm{mm}$ at the bottom to $r_2 = 25\ "
     r"\mathrm{mm}$ at the top, $L = 120\ \mathrm{mm}$) loaded by P at the top. (a) Derive its axial deformation. (b) "
     r"Evaluate it for $P = 500\ \mathrm{N}$, $E = 13\ \mathrm{GPa}$ (ignore self-weight).",
     "", src="none", figure="p. 41.")),
 sec("Rigid bars hung on cables", (42, 48),
   ("md", "A rigid bar on two cables plus a pin has more unknowns than equilibrium equations. Add compatibility: "
          "the bar rotates about the pin, so the vertical movements of the cable points are proportional to their "
          r"distances from it; each cable's stretch is the component along the cable, $\delta = \delta_V\cos\theta$."),
   q("CE1101 M1 Example 1.6",
     r"Rigid bar ABD (pinned at A; B at 1 m, D at 3 m) carries 6 kN/m over its 3 m length and hangs from cables BC "
     r"and DC to a point C 2 m above the bar, midway between B and D. Each cable has $A = 140\ \mathrm{mm^2}$, $E = 200\ "
     r"\mathrm{GPa}$. Find the cable forces.",
     r"**$T_{CD} = 3T_{BC}$; $T_{BC} = 3.02\ \mathrm{kN}$, $T_{CD} = 9.06\ \mathrm{kN}$.**",
     r"Moments about A: $T_{BC}(2/\sqrt5)(1) + T_{CD}(2/\sqrt5)(3) = 18 \times 1.5 = 27$. Compatibility: $(\delta_D)_V "
     r"= 3(\delta_B)_V$ and $\cos\theta_B = \cos\theta_D = 2/\sqrt5$, so $\delta_{CD} = 3\delta_{BC}$; equal cable "
     r"lengths and stiffness give $T_{CD} = 3T_{BC}$ → $T_{BC} \times 20/\sqrt5 = 27$.", figure="p. 42."),
   q("CE1101 M1 Example 1.7 (additional)",
     r"For the same bar and loading, find the elongation of cables BC and CD and the rotation of the bar.",
     "", src="none", figure="p. 46."),
   q("CE1101 M1 Example 1.8 (homework)",
     r"A rigid bar ABD carries 20 kN at E and hangs from cables BC and CD (each $140\ \mathrm{mm^2}$, $E = 200\ "
     r"\mathrm{GPa}$) as drawn. Find (a) the cable forces, (b) their elongations and (c) the bar's rotation.",
     "", src="none", figure="p. 47."),
   q("CE1101 M1 Example 1.9 (homework)",
     r"A rigid steel beam (self-weight 3 kN/m, 2.5 m long) rests on three rubber blocks A, B, C at 1.25 m spacing "
     r"($E = 15\ \mathrm{MPa}$, $70 \times 70\ \mathrm{mm}$, 125 mm tall), but B is 5 mm shorter. (a) Does the beam "
     r"touch B? (b) Find the normal stress in each block.",
     "", src="none", figure="p. 48.")),
]}

M2 = "CE102/CE1101_M2_Torsional_Members.pdf"

MOM[M2] = {"code": "CE102", "title": "M2 · Torsional members", "sections": [
 sec("Torsion in circular shafts: assumptions", (2, 5),
   ("md", "Torsion appears in screwdrivers, soil augers, drive shafts and couplings. For a circular shaft under "
          "torque: the axis stays straight and does not stretch; each cross-section stays plane and perpendicular "
          "to the axis; radial lines stay straight and radial as the section rotates."),
   ("eq", r"\gamma = \frac{r\,d\phi}{dx},\qquad \gamma_{max} = \frac{c\,d\phi}{dx}\ \Rightarrow\ \gamma = \frac{r}{c}\gamma_{max}"),
   ("md", "Shear strain is zero on the axis and grows linearly to a maximum at the surface (radius c)."),
 ),
 sec("The torsion formula and polar moment of area", (6, 9),
   ("eq", r"T = \int_A r\tau\,dA = G\frac{d\phi}{dx}\int_A r^2dA = GJ\frac{d\phi}{dx}\qquad\Rightarrow\qquad \tau = \frac{Tr}{J},\ \ \tau_{max} = \frac{Tc}{J}"),
   ("eq", r"J_{solid} = \frac{\pi c^4}{2} = \frac{\pi D^4}{32},\qquad J_{tube} = \frac{\pi}{2}(R_2^4 - R_1^4) = \frac{\pi}{32}(D_2^4 - D_1^4)"),
   ("md", "Shear stress varies linearly from zero at the centre to its maximum at the outer surface."),
 ),
 sec("Angle of twist", (10, 14),
   ("eq", r"\phi = \frac{TL}{GJ};\qquad \phi = \sum_i\frac{T_iL_i}{G_iJ_i};\qquad \phi = \int_0^L\frac{T(x)}{GJ(x)}dx"),
   ("md", r"Analogy with axial members: $\phi = TL/GJ \leftrightarrow \delta = FL/EA$; $\tau = T/(J/r) "
          r"\leftrightarrow \sigma = F/A$.\n\n**Limits:** circular sections only, linear-elastic material, and no "
          "stress concentrations at abrupt changes of section. **Sign convention:** right-hand rule — a torque "
          "vector pointing out of the cut face is positive."),
 ),
 sec("Statically determinate shafts", (15, 19),
   ("steps", ["Draw the shaft with torque vectors (right-hand rule).",
              "Cut each segment and find the internal torque by $\\sum M_x = 0$, assuming it positive.",
              r"Largest |T| gives $\tau_{\max} = Tc/J$; add $T_iL_i/GJ$ segment by segment for the twist."]),
   q("CE1101 M2 Example 2.1",
     r"A 35 mm solid shaft ($G = 80\ \mathrm{GPa}$) carries balanced torques of 30, 25, 40, 65 and 80 Nm at A, B, C, "
     r"D, E (segments AB 0.3 m, BC 0.2 m, CD 0.3 m, DE 0.15 m). Find the absolute maximum shear stress and the twist "
     r"of A relative to E.",
     r"**Internal torques −30, −55, −15, −80 Nm → $\tau_{\max} = 9.503\ \mathrm{MPa}$ (in DE) · $\phi_{A/E} = "
     r"-0.0031\ \mathrm{rad}$.**",
     r"$J = \pi \times 35^4/32 = 147\,323.5\ \mathrm{mm^4}$; $\tau = 80 \times 10^3 \times 17.5/J$. $\phi = "
     r"[(-30)(300) + (-55)(200) + (-15)(300) + (-80)(150)] \times 10^3/(147\,323.5 \times 80 \times 10^3)$.",
     figure="p. 16.")),
 sec("Bolted shaft couplings", (20, 23),
   ("md", "A flange coupling transfers torque through bolts in shear: each of n bolts at radius R carries $F = "
          "T/(nR)$. Good practice: the connection should be stronger than the members it joins, so the shaft fails "
          "first (a ductile, visible failure rather than a sudden one at the joint)."),
   q("CE1101 M2 Example 2.2",
     r"A bolted coupling joins two solid shafts of radius $r = 30\ \mathrm{mm}$; bolts of $d = 10\ \mathrm{mm}$ sit at "
     r"$R = 75\ \mathrm{mm}$. Shaft and bolts share $\tau_{\mathrm{ult}} = 60\ \mathrm{MPa}$. How many bolts make "
     r"the shaft fail first? (Assume uniform bolt shear.)",
     r"**$n \ge 2r^3/(Rd^2) = 7.2$ → at least 8 bolts.**",
     r"Shaft: $\tau = 2T/(\pi r^3)$; bolt: $\tau = 4T/(nR\pi d^2)$. Require $\tau_{\mathrm{shaft}} \ge "
     r"\tau_{\mathrm{bolt}}$.", figure="p. 21.")),
 sec("Varying torque: drill pipe", (24, 26),
   q("CE1101 M2 Example 2.3",
     r"A drill pipe (outer radius $r_o$, inner $r_i$, shear modulus G, length L) meets a resisting torque $T_A$ at "
     r"its deep end A, and soil friction adds a torque per unit length rising linearly from 0 at the surface B to "
     r"$t_0$ at A. Find the drive torque $T_B$ and the twist of one end relative to the other as it starts to turn.",
     r"**$T_B = T_A + t_0L/2$ · $\phi = -\dfrac{2L(t_0L + 3T_A)}{3\pi G(r_o^4 - r_i^4)}$.**",
     r"Cut at x from B: $T_x = t_0x^2/(2L) - (T_A + t_0L/2)$; $\phi = \int_0^L T_x\,dx/(JG)$ with $J = \tfrac{\pi}{2}"
     r"(r_o^4 - r_i^4)$.", figure="p. 24.")),
 sec("Power transmission", (27, 31),
   ("eq", r"P = T\omega,\qquad \omega = 2\pi f = \frac{2\pi N}{60}\ \text{rad/s},\qquad 1\ \mathrm{hp} = 0.745\ \mathrm{kW}"),
   q("CE1101 M2 Example 2.4",
     r"A car drive shaft is a thin-walled tube, outer diameter 55 mm, carrying 180 hp at 1500 rev/min. With "
     r"$\tau_{\mathrm{ult}} = 120\ \mathrm{MPa}$ and a factor of safety of 2.5, find the minimum wall thickness.",
     r"**$T = 853.6\ \mathrm{Nm}$, $\tau_{\mathrm{allow}} = 48\ \mathrm{MPa}$ → $d_i \le 45.2\ \mathrm{mm}$ → $t = "
     r"4.9\ \mathrm{mm}$.**",
     r"$\omega = 157.1\ \mathrm{rad/s}$, $P = 134.1\ \mathrm{kW}$. $d_i = \sqrt[4]{d_o^4 - 16d_oT/(\pi\tau_{\mathrm{allow}})}$. "
     r"(The slide also asks whether this keeps the twist under 0.2 rad over 2.8 m with $G = 15\ \mathrm{GPa}$ — "
     r"not answered there.)", figure="p. 28."),
   q("CE1101 M2 Example 2.5 (homework)",
     r"A helicopter engine delivers 600 hp to rotor shaft AB (600 mm long, steel $G = 70\ \mathrm{GPa}$) at 1200 "
     r"rev/min. Find the shaft diameter for $\tau_{\mathrm{allow}} = 55\ \mathrm{MPa}$ and a twist limit of 0.05 rad.",
     "", src="none", figure="p. 31.")),
 sec("Statically indeterminate shafts", (32, 37),
   ("steps", ["Equilibrium of the whole shaft: the support torques plus applied torques sum to zero.",
              "Check whether a gap or free rotation closes; if not, the problem is determinate.",
              r"Compatibility: total twist between the supports equals the gap (often 0); write each segment's "
              r"internal torque in terms of the unknown reaction and solve."]),
   q("CE1101 M2 Example 2.6",
     r"A stainless-steel shower-curtain rail ($G = 74\ \mathrm{GPa}$, outer diameter 30 mm, wall 1.5 mm) should be "
     r"fixed at both ends, but end A can rotate 0.005 rad before it locks. Torques of 40 Nm at C and 20 Nm at D "
     r"(segments AC, CD, DB each 0.4 m) are applied. Find (a) the support torques and (b) the maximum shear stress.",
     r"**Free twist would be 0.012 rad > 0.005, so A locks: (a) $T_A = -11.57\ \mathrm{Nm}$, $T_B = -8.43\ "
     r"\mathrm{Nm}$ · (b) $\tau_{\max} = 15.59\ \mathrm{MPa}$ in CD ($T = 28.43\ \mathrm{Nm}$).**",
     r"$J = \tfrac{\pi}{2}(0.015^4 - 0.0135^4)$. Compatibility: $[T_A + (T_A + 40) + (T_A + 20)] \times 0.4/(JG) = "
     r"0.005$. Equilibrium: $T_A + 40 - 20 + T_B = 0$.", figure="p. 33.")),
 sec("Rubber torsion spring", (38, 40),
   q("CE1101 M2 Example 2.7",
     r"A rubber annulus (inner radius $r_i$, outer $r_o$, thickness h, shear modulus G) is bonded between a rigid "
     r"shaft and a fixed rigid ring. For a torque T on the shaft, find (a) the maximum shear stress in the rubber and "
     r"(b) the shaft's rotation.",
     r"**(a) $\tau_{\max} = \dfrac{T}{2\pi r_i^2h}$ at the inner face · (b) $\phi = \dfrac{T}{4\pi hG}\left(\dfrac{1}"
     r"{r_i^2} - \dfrac{1}{r_o^2}\right)$.**",
     r"At radius r the shear force $\tau(2\pi rh)$ times r must equal T, so $\tau = T/(2\pi r^2h)$. With $\gamma\,dr "
     r"= r\,d\phi$: $d\phi = T\,dr/(2\pi hGr^3)$; integrate from $r_i$ to $r_o$.", figure="p. 38.")),
]}

M3 = "CE102/CE1101_M3_Flexural_Members.pdf"

MOM[M3] = {"code": "CE102", "title": "M3 · Flexural members: shear force & bending moment", "sections": [
 sec("Internal forces and sign convention", (2, 6),
   ("md", "A cut through a member exposes an axial force F, a shear force V and a bending moment M, equal and "
          "opposite on the two faces. Equilibrium must hold for the whole structure, for every member and for any "
          "part cut from a member."),
   ("md", "**Deformation sign convention** (for stress resultants): positive shear tends to rotate the element "
          "clockwise; positive (sagging) moment compresses the top fibres; tension is positive. The **static** sign "
          "convention (forces positive in a chosen direction) is used only when writing equilibrium equations."),
   ("md", "The shear-force diagram (SFD) and bending-moment diagram (BMD) plot V and M along the beam so the "
          "maximum and minimum values for design can be read off."),
 ),
 sec("Relations between load, shear and moment", (7, 11),
   ("eq", r"\frac{dV}{dx} = -q,\qquad V_B - V_A = -\int_A^B q\,dx;\qquad \frac{dM}{dx} = V,\qquad M_B - M_A = \int_A^B V\,dx"),
   ("md", "Loads q and P are positive downwards; an applied couple is positive anticlockwise.\n\n"
          "- No distributed load → V constant, M linear.\n- Uniform load → V linear, M parabolic.\n"
          "- Where V = 0, M has a maximum or minimum.\n- A **point load P** makes V drop by P (left to right); M "
          "does not jump.\n- A **couple** $M_0$ (anticlockwise) makes M drop by $M_0$; V does not change."),
 ),
 sec("Sketching procedure", (12, 12),
   ("steps", ["Draw the free-body (load) diagram with dimensions.",
              "Find the support reactions from equilibrium.",
              "Draw vertical construction lines at every point load, couple, support, and start/end of distributed load.",
              "Sketch the SFD segment by segment from left to right using $dV/dx = -q$ and the jumps at point loads.",
              "Sketch the BMD segment by segment using $dM/dx = V$ (area under the SFD) and the jumps at couples."]),
 ),
 sec("Examples: balance beam and engine crane", (13, 19),
   q("CE1101 M3 Example 3.1",
     r"A gymnast of weight P does a handstand on a 5 m simply supported balance beam, 1.5 m from A. Draw the SFD and "
     r"BMD. Then, for an arbitrary distance x from A, find the maximum moment and the most critical position.",
     r"**$R_A = 0.7P$, $R_B = 0.3P$; V = +0.7P (A–C), −0.3P (C–B); $M_C = 1.05P$ · general: $M_{\max} = Px(5 - "
     r"x)/5$, largest at mid-span ($x = 2.5\ \mathrm{m}$, $M = 1.25P$).**",
     r"$\sum M_B$: $5R_A = 3.5P$. The BMD rises linearly over A–C (positive constant V) and falls over C–B.",
     figure="p. 13."),
   q("CE1101 M3 Example 3.2",
     r"An engine crane lifts 5 kN at the tip C of a horizontal boom ABC (pinned at A; hydraulic cylinder BD at "
     r"68.2° to the boom at B, 0.4 m from A; C a further 0.9 m). Draw the SFD and BMD of the boom.",
     r"**$R_B = 17.5\ \mathrm{kN}$ (two-force cylinder), $A_y = 11.25\ \mathrm{kN}$ down, $A_x = 6.5\ \mathrm{kN}$ · V "
     r"= −11.25 kN on AB, +5 kN on BC · $M_B = -4.5\ \mathrm{kNm}$ (hogging), zero at A and C.**",
     r"$\sum M_A$: $R_B\sin 68.2^\circ(0.4) = 5(1.3)$. Vertical component of $R_B$ is 16.25 kN.", figure="p. 17.")),
 sec("Example: chair frame", (20, 22),
   q("CE1101 M3 chair (in class)",
     r"Members ABC and BD of a chair are rigidly joined at B; the chair is pinned at A and runs in a smooth vertical "
     r"slot at D. A person (550 N) sits at C. Draw the SFD and BMD of ABC.",
     r"**Reactions from the slide: $D_x = 1100\ \mathrm{N}$, $A_y = 550\ \mathrm{N}$, $A_x = 1100\ \mathrm{N}$; the "
     r"collar force acts on ABC as 1100 N axial plus a 495 Nm couple at B.** (The diagrams are left blank on the "
     "student copy.)",
     r"Move the collar force from D to B as an equal force plus a couple $1100 \times 0.45 = 495\ \mathrm{Nm}$.",
     figure="pp. 20–22.")),
 sec("Example: bridge pier cap", (23, 27),
   ("md", "Stringers bring point loads onto the pier cap, and the cap's own weight is a uniform load."),
   q("CE1101 M3 Example 3.3",
     r"A concrete pier cap (overhangs D–A and B–E of 2 m, span A–B of 5 m with C at mid-span) carries 60 kN at D and "
     r"E, 45 kN at A, C and B, and 8 kN/m self-weight. Piers A and B give vertical reactions only. Draw the SFD and "
     r"BMD.",
     r"**$A_y = B_y = 163.5\ \mathrm{kN}$ · V: −60 → −76 (A left), +42.5 → +22.5 (C left), −22.5 → −42.5 (B left), "
     r"+76 → +60 · M: 0 (D), −136 (A), −54.75 (C), −136 (B), 0 (E) kNm.**",
     r"Symmetry: $2A_y = 2(60) + 3(45) + 8(9)$. Moments from areas of the SFD: $M_A = -(60 + 76)/2 \times 2$; $M_C = "
     r"-136 + (42.5 + 22.5)/2 \times 2.5$.", figure="p. 24."),
   q("CE1101 M3 Example 3.4 (homework)",
     r"A basement retaining wall, fixed at A, 6 m high, carries soil pressure rising linearly with depth (8.5h kN/m "
     r"at depth h). Draw its SFD and BMD.",
     "", src="none", figure="p. 28.")),
 sec("Example: spliced beam", (29, 32),
   q("CE1101 M3 spliced beam (in class)",
     r"A spliced timber beam (span A–B 4 m, overhang B–C 2 m) carries 8 kN/m. Find the largest sagging moment and "
     r"where it occurs, and the best place for the splice within A–B.",
     r"**Reactions 12 kN (A) and 36 kN (B); V = 0 at 1.5 m → $M_{\max} = 9\ \mathrm{kNm}$ · splice where M = 0, 3 m "
     r"from A.**",
     r"$\sum M_B$: $4R_A = 8 \times 4 \times 2 - 8 \times 2 \times 1 = 48$ → $R_A = 12$, $R_B = 48 - 12 = 36$. $M = 12x - 4x^2$ is zero at $x = 3$.",
     figure="p. 29."),
   q("CE1101 M3 Example 3.5 (homework)",
     r"Find the position a of the roller support on a beam of length L under w kN/m so that the largest sagging "
     r"moment equals the largest hogging moment, and draw the SFD and BMD.",
     "", src="none", figure="p. 33.")),
 sec("Example: ski on snow", (34, 36),
   q("CE1101 M3 ski (in class)",
     r"A ski carries the man's 0.8 kN at its centre; the snow pushes back with a trapezoidal load (rising over 0.5 m "
     r"to w, constant over the middle 1 m, falling over the last 0.5 m). Find w and draw the SFD and BMD.",
     r"**$w = 0.533\ \mathrm{kN/m}$.** (The SFD and BMD are left blank on the student copy.)",
     r"$0.8 = \tfrac12w(0.5) + \tfrac12w(0.5) + w(1)$.", figure="p. 34.")),
]}

M4 = "CE102/CE1101_M4_Stress_Strain_Bending.pdf"

MOM[M4] = {"code": "CE102", "title": "M4 · Stresses and strains in bending", "sections": [
 sec("Curvature and bending strain", (2, 7),
   ("eq", r"\kappa = \frac{1}{\rho} = \frac{d\theta}{ds} \approx \frac{d\theta}{dx},\qquad \varepsilon_x = -\kappa y"),
   ("md", "Deflections are small, so $ds \\approx dx$. Curvature takes the sign of the bending moment: a sagging "
          "(positive) moment bends the beam concave upward. In pure bending, plane sections stay plane and normal "
          "to the axis; fibres below the neutral axis lengthen (tension), fibres above shorten (compression), and "
          "the strain varies linearly with the distance y from the neutral axis."),
 ),
 sec("Neutral axis, moment–curvature and the flexure formula", (8, 12),
   ("eq", r"\sigma_x = E\varepsilon_x = -E\kappa y;\qquad \int_A\sigma_x\,dA = 0 \Rightarrow \int_A y\,dA = 0"),
   ("md", "With no axial force and a linear-elastic material, the neutral axis passes through the **centroid** "
          "of the section."),
   ("eq", r"M = -\int_A y\sigma_x\,dA = \kappa EI\ \Rightarrow\ \kappa = \frac{1}{\rho} = \frac{M}{EI};\qquad \sigma_x = -\frac{My}{I},\qquad \sigma_{max} = \frac{Mc}{I} = \frac{M}{S}"),
   ("md", "EI is the flexural rigidity and $S = I/c$ the section modulus. For a positive moment, stress is tensile "
          "below the neutral axis and compressive above; it varies linearly with y."),
 ),
 sec("Centroid and second moment of area", (13, 16),
   ("eq", r"c_1 = \frac{\sum A_ky_k}{\sum A_k};\qquad I_z = \sum_k\left[\frac{b_kh_k^3}{12} + A_k(c_1 - y_k)^2\right]\ \ \text{(parallel-axis theorem)}"),
   ("md", "**Superposition:** about an axis of symmetry you may subtract areas, e.g. a hollow box $I = "
          r"\tfrac{1}{12}(BH^3 - bh^3)$. This is not valid about an axis that is not a symmetry axis of the section."),
 ),
 sec("Composite beams: transformed section", (17, 20),
   ("eq", r"n = \frac{E_2}{E_1},\quad b^* = nb;\qquad (\sigma_x)_1 = -\frac{My}{I},\quad (\sigma_x)_2 = -n\frac{My}{I}"),
   ("md", "Replace material 2 by an equivalent width of material 1, scaling **only the width** (never the depth, "
          "since the moment arm y must be kept). Find the centroid and I of the transformed section, then convert "
          "stresses back with n. Examples: steel plates on timber ($n = E_s/E_w$), a concrete slab on a steel I-beam "
          "transformed to steel ($n = E_c/E_s$)."),
 ),
 sec("Examples: hollow box and plank sections", (21, 29),
   q("CE1101 M4 Example 4.1",
     r"Four 20 mm boards form a 140 × 140 mm hollow box (100 mm clear inside). For a moment M, what share of M is "
     r"carried by the top and bottom boards?",
     r"**$I = 2.368 \times 10^{-5}\ \mathrm{m^4}$; stresses 2956M (outer face) and 2111.5M Pa (inner face); force "
     r"in each flange $F = 7.10M$, lever arm $L = 121\ \mathrm{mm}$ → $M' = 0.859M$: 85.9 %.**",
     r"$I = \tfrac{1}{12}(0.14^4 - 0.1 \times 0.1^3)$. $F = \tfrac12(\sigma_C + \sigma_D)(0.02)(0.14)$. The trapezoid's "
     r"centroid is 10.5 mm from the inner face, so $L = 100 + 2 \times 10.5$. (The slide then asks what happens with "
     r"one central web instead of two side boards — not answered there.)", figure="p. 21."),
   q("CE1101 M4 plank sections (in class)",
     r"Two beams are built from 15 mm boards, both 300 mm deep and 200 mm wide but arranged differently (a) and (b). "
     r"Which carries 150 kNm about z with the lower bending stress, and what is that stress?",
     r"**Section (b) — it has the larger section modulus.** (The values of I, S and the stress are left blank on the student "
     "copy.)", r"$\sigma = M/S$; find each I by subtracting rectangles about the symmetry axis.", figure="pp. 27–29.")),
 sec("Example: diving board", (30, 34),
   q("CE1101 M4 Example 4.2",
     r"An 80 kg man stands at the end C of a diving board (pin A, roller B 1.5 m from A, overhang 2.5 m). The section "
     r"is a 400 × 20 mm plank with three 10 × 20 mm ribs below. Find the maximum bending stresses.",
     r"**$M_{\max} = -1962\ \mathrm{Nm}$ at B; $c_1 = 11.4$, $c_2 = 28.6\ \mathrm{mm}$, $I = 5.1 \times 10^5\ "
     r"\mathrm{mm^4}$ → tension 43.86 MPa (top), compression −110.0 MPa (bottom of the ribs).**",
     r"Reactions 1308 N (A, down) and 2092.8 N (B). $c_1 = (10 \times 8000 + 3 \times 30 \times 200)/8600$. $I = "
     r"2.82 \times 10^5 + 3 \times 7.59 \times 10^4$.", figure="p. 30.")),
 sec("Example: railway sleeper", (35, 37),
   q("CE1101 M4 Example 4.3",
     r"A 400 mm wide timber sleeper (2.3 m long) carries two 70 kN rail loads 1.5 m apart, 0.4 m from each end; the "
     r"ballast reaction is uniform. With $\sigma_{\mathrm{allow}} = 19\ \mathrm{MPa}$, find the minimum thickness.",
     r"**$w = 60.87\ \mathrm{kN/m}$, $M_{\max} = -12.25\ \mathrm{kNm}$ at mid-span → $S = 0.645 \times 10^6\ "
     r"\mathrm{mm^3}$ → $t = 98.4\ \mathrm{mm}$.**",
     r"$w = 140/2.3$. Moment at the rail: $4.87\ \mathrm{kNm}$; at mid-span $-12.25$. $S = bt^2/6 = 200t^2/3$.",
     figure="p. 35.")),
 sec("Truss girders and castellated beams", (38, 42),
   ("md", "Aluminium stage girders: continuous chords with welded diagonals; for bending, take I of the four chords "
          "about the centroid with the parallel-axis theorem. Castellated beams are cut along a zig-zag, offset and "
          "re-welded: deeper, stiffer and stronger for the same steel."),
   q("CE1101 M4 Example 4.4 (homework)",
     r"A stage truss girder (four 50 mm tubes, 3 mm wall, at the corners of a 400 × 400 mm square; span 9 m) carries "
     r"1 kN/m over its middle 3 m. Ignoring the diagonals, find the maximum bending stress.",
     "", src="none", figure="p. 39."),
   q("CE1101 M4 Example 4.5 (homework)",
     r"Beam (b) is made by cutting and re-welding I-beam (a). With $\sigma_{\mathrm{allow}} = 180\ \mathrm{MPa}$, find "
     r"(1) the ratio of moment capacities of (b) at section b-b and (a); (2) the ratio between sections b-b and c-c "
     r"of beam (b).",
     "", src="none", figure="p. 42.")),
 sec("Example: steel–concrete composite beam", (43, 47),
   q("CE1101 M4 composite beam (in class)",
     r"A 1000 × 100 mm concrete slab sits on a steel I-beam (200 × 15 mm flanges, 370 × 15 mm web, 400 mm deep). "
     r"$\sigma_{\mathrm{allow}}$ = 15 MPa (concrete) and 165 MPa (steel); $E_c = 22$, $E_s = 200\ \mathrm{GPa}$. "
     r"Find the allowable moment and the stresses and strains through the depth.",
     r"**$n = 0.11$, $b^* = 110\ \mathrm{mm}$; $c_1 = 177.33$, $c_2 = 322.67\ \mathrm{mm}$, $I = 6.471 \times 10^8\ "
     r"\mathrm{mm^4}$ → steel governs: $M_{\max} = 330.9\ \mathrm{kNm}$ · concrete top −9.97 MPa, concrete and steel "
     r"at the interface −4.35 / −39.54 MPa, steel bottom +165 MPa ($\varepsilon = 8.25 \times 10^{-4}$).**",
     r"Concrete limit: $15 = nMc_1/I$; steel limit: $165 = Mc_2/I$; take the smaller M.", figure="p. 44.")),
]}

M5 = "CE102/CE1101_M5_Deflection_of_Beams.pdf"

MOM[M5] = {"code": "CE102", "title": "M5 · Deflection of beams", "sections": [
 sec("Differential equation of the elastic curve", (2, 4),
   ("eq", r"\theta \approx \tan\theta = \frac{dy}{dx},\qquad \kappa = \frac{d\theta}{dx} = \frac{d^2y}{dx^2} = \frac{M}{EI}"),
   ("md", "Small slopes, so $ds \\approx dx$. Deflection y is positive upward and rotation $\\theta$ positive "
          "anticlockwise."),
 ),
 sec("Direct integration", (5, 13),
   ("eq", r"EIy'' = M,\qquad EIy''' = V,\qquad EIy'''' = -q"),
   ("md", "Integrate the moment equation twice (or the shear three times, the load four times) and fix the "
          "constants from **boundary conditions** (zero deflection at supports, zero slope at a fixed end) and "
          "**continuity** of slope and deflection where one moment function hands over to the next. Each segment "
          "with a different moment expression needs its own function and coordinate."),
   q("CE1101 M5 Example 5.1",
     r"Two people of weight P sit at the ends of a garden bench with overhangs a and span b between legs A and B "
     r"(vertical reactions only). Find (1) the slope at A, (2) the mid-span deflection, (3) the deflection of the free "
     r"ends.",
     r"**$\theta_A = \dfrac{Pab}{2EI}$ · $\delta_{\mathrm{mid}} = \dfrac{Pab^2}{8EI}$ (upward) · $\delta_{\mathrm{end}} "
     r"= -\dfrac{Pa^2}{6EI}(2a + 3b)$ (downward).**",
     r"Overhang: $M = -Px_1$; span: $M = -Pa$ (constant). Conditions: $y_1(a) = 0$, $y_2(0) = y_2(b) = 0$, "
     r"$y_1'(a) = y_2'(0)$ → $C_3 = Pab/2$, $C_4 = 0$, $C_1 = \tfrac{Pa}{2}(a + b)$, $C_2 = -\tfrac{Pa^2}{6}(2a + 3b)$.",
     figure="p. 7."),
   q("CE1101 M5 Example 5.2 (homework)",
     r"Redo Example 5.1 with $x_2$ running from right to left (positive slope clockwise for $x_2$).",
     "", src="none", figure="p. 13.")),
 sec("Superposition", (14, 14),
   ("md", "The deflection equation is linear, so deflections and slopes from separate loads add."),
   ("eq", r"\text{simply supported, UDL: } \delta_C = \frac{5qL^4}{384EI},\ \theta_A = \frac{qL^3}{24EI};\qquad \text{central point load: } \delta_C = \frac{PL^3}{48EI},\ \theta_A = \frac{PL^2}{16EI}"),
 ),
 sec("Moment-area method", (15, 19),
   ("eq", r"\theta_{B/A} = \theta_B - \theta_A = \int_A^B\frac{M}{EI}dx\qquad(\text{area of the } M/EI \text{ diagram})"),
   ("eq", r"t_{B/A} = \int_A^B x_1\frac{M}{EI}dx = \bar x\cdot\text{area}\qquad(\text{first moment of the } M/EI \text{ area about B})"),
   ("md", r"First theorem: the angle between the tangents at A and B equals the area of the M/EI diagram between "
          r"them. Second theorem: the deviation of B from the tangent at A equals the moment of that area about B "
          r"(positive when B lies above the tangent). Useful relations: $t_{A/B} + t_{B/A} = \theta_{B/A}L_{B/A}$; "
          "best for slopes and deflections at particular points."),
 ),
 sec("Moment diagrams by parts and area properties", (20, 23),
   ("md", "Draw the M diagram as separate parts, one per load measured from a convenient point, so each part is a "
          "simple shape. Spandrel $y = kx^n$: area $bh/(n + 1)$, centroid $b/(n + 2)$ from the vertex (rectangle n = "
          "0, triangle n = 1, parabola n = 2: area $bh/3$, centroid $b/4$). A parabolic segment under a UDL "
          r"between zero-slope and end has area $2bh/3$ with centroid $3b/8$."),
 ),
 sec("Application: pipeline support spacing", (24, 30),
   ("md", "A pipeline on regular supports is a continuous beam; analysing one span as simply supported "
          "over-estimates deflection, so it is conservative. Design limits: bending stress and sag ≤ L/600."),
   q("CE1101 M5 pipeline (in class)",
     r"A 15 km pipeline of stainless steel pipe (outer diameter 330 mm, wall 6 mm, $E = 200\ \mathrm{GPa}$) carries "
     r"1.4 kN/m. With sag ≤ L/600 and simply supported spans, find the largest span and the number of supports.",
     "", src="none", figure="pp. 26–30 (steps given, values blank).")),
 sec("Example: four-point bend test", (31, 35),
   q("CE1101 M5 Example 5.3",
     r"A fibre-reinforced concrete beam (span L, second moment I) is tested with two loads P at distance a from each "
     r"support. The mid-span deflection is $\delta$. Find the elastic modulus E.",
     r"**$\delta = \dfrac{Pa}{24EI}(3L^2 - 4a^2)$ → $E = \dfrac{Pa}{24I\delta}(3L^2 - 4a^2)$.**",
     r"M/EI diagram: triangles of height $Pa/EI$ over each end a, rectangle between. $\delta = \tfrac12t_{D/A} - "
     r"t_{E/A}$ by similar triangles.", figure="p. 31.")),
 sec("Example: retaining wall", (36, 39),
   q("CE1101 M5 Example 5.4",
     r"A 6 m RC basement wall (600 mm thick, $E = 16\ \mathrm{GPa}$) is fixed at the base B and carries soil "
     r"pressure 8.5h kPa at depth h. Per metre of wall, find the slope and deflection at the top A.",
     r"**Base shear 153 kN, moment 306 kNm; $\theta_A = 1.59 \times 10^{-3}\ \mathrm{rad}$, $\delta_A = 7.65\ "
     r"\mathrm{mm}$.**",
     r"$I = 1 \times 0.6^3/12 = 1.8 \times 10^{-2}\ \mathrm{m^4}$. Cubic M/EI: area $= 6 \times 306/(4EI) = "
     r"459/EI$, centroid $6/5$ m from A. $\theta_A = -\theta_{B/A}$; $\delta_A = A_1(6 - 6/5)$ i.e. $2203.2/EI$.",
     figure="p. 36.")),
 sec("Example: overhanging beam, matching deflections", (40, 50),
   q("CE1101 M5 overhang (in class)",
     r"A beam AB of length a (pin A, roller B) overhangs to C (total length L) with a load P at C. Find a so that "
     r"the deflection at C equals the largest deflection within AB (EI constant).",
     r"**$\delta_C = \dfrac{(L - a)^2}{3}\dfrac{PL}{EI}$, $\delta_D = \dfrac{3a^2(L - a)}{27L}\dfrac{PL}{EI}$ at $x = "
     r"a/\sqrt3$; equal when $3a^2 + 9aL - 9L^2 = 0$ → $a = \dfrac{-3 + \sqrt{21}}{2}L \approx 0.791L$.**",
     r"Moment-area with the M/EI diagram by parts; zero slope at D gives $x = a/\sqrt3$.", figure="p. 40.")),
]}
