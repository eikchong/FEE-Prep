"""Hydraulics tutorial questions as q blocks: CE105 (CE2134 Part 1 tutorials and self-evaluation questions) and
CE205 (Part 2 Homework 1). Statements are from the question sheets in materials/CE105 and materials/CE205; answers
from the official solutions unless marked. Numbers are recomputed in tests/test_tutorial_answers.py."""
from utils.qblock import q
from utils.study_notes_hyd import D


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


HYDQ = {}

HYDQ[D["TQ"]] = {"code": "CE105", "title": "Hydraulics practice · Tutorials 1–4 (questions & answers)", "sections": [
 sec("Tut 1 Q1 Micromanometer", (1, 1),
   q("CE2134 Tut 1 Q1",
     r"A micromanometer has two large reservoirs (area $A_r$) filled with liquid of specific weight $\gamma_1$, "
     r"joined by a U-tube (area $A_t$) holding liquid of specific weight $\gamma_2$. A small gas pressure difference "
     r"$p_1 - p_2$ gives a reading h. Find the relation between h and $p_1 - p_2$ when $A_t/A_r$ is small, and show "
     r"that h is magnified by making $\gamma_2 - \gamma_1$ small. Initially ($p_1 = p_2$) the reservoir levels are "
     r"equal.",
     r"**$p_1 - p_2 = (\gamma_2 - \gamma_1)h$, so $h = (p_1 - p_2)/(\gamma_2 - \gamma_1)$ grows as the two specific "
     r"weights approach each other.**",
     r"With $A_t/A_r$ small the reservoir levels barely move, so their difference can be neglected; walk the "
     r"hydrostatic equation from one side to the other.", figure="p. 1, Figure 1.")),
 sec(r"Tut 1 Q2 Oil-spill boom ($\rho_{\mathrm{oil}}$ 873, $\rho_{\mathrm{sw}}$ 1030; L 150 m, draft 0.30 m)", (2, 2),
   q("CE2134 Tut 1 Q2",
     r"A tanker carrying 500 000 barrels of crude ($\rho = 873\ \mathrm{kg/m^3}$) spills oil into seawater ($\rho = "
     r"1030\ \mathrm{kg/m^3}$). A 150 m boom (five 30 m sections) forms a semicircle off the ship; its 45 × 10 cm "
     r"section has a 30 cm draft $h_D$ and 15 cm freeboard. (a) What is the largest oil volume it can hold before oil "
     r"leaks underneath, and what percentage of the cargo is that? (b) What minimum freeboard-to-draft ratio prevents "
     r"leakage, and why might the boom be built with 1 : 2? (c) How much lead must be added to each 30 m section per "
     r"extra centimetre of draft?",
     r"**(a) $V_{\max} = 1267\ \mathrm{m^3}$ (1.6 % of 500 000 bbl) · (b) $h_f/h_D = \rho_w/\rho_o - 1 = 0.18$ (≈ "
     r"1 : 5.6); the extra freeboard allows for waves and wind · (c) $1030 \times 0.01 \times 0.10 \times 30 = 30.9\ "
     r"\mathrm{kg}$.**",
     r"Equal pressure under the boom: oil depth $= (\rho_w/\rho_o)h_D$. Semicircle radius $R = 150/\pi$, area $\pi "
     r"R^2/2$. The solution prints the volume unit as square metres and mentions a 40 cm draft while using 30 cm — read "
     r"it as cubic metres and 30 cm.", figure="p. 2, Figure 2.")),
 sec("Tut 2 Q1 Thin gate holding oil against seawater", (3, 3),
   q("CE2134 Tut 2 Q1",
     r"A thin, weightless plane gate ABCDE is submerged in seawater ($\rho = 1025\ \mathrm{kg/m^3}$, $z = 0$ at its "
     r"surface). On its right it holds back oil ($\rho = 854\ \mathrm{kg/m^3}$) to a depth $h = -z_D = 1.0\ "
     r"\mathrm{m}$. A counterweight W hangs at E ($h_E > h$) and a horizontal wire holds A, 0.50 m above the seawater. "
     r"(a) Find the oil surface level $z_B$. (b) Sketch the pressures on both sides from A to D. (c) Argue that the "
     r"pressures on D–E cancel. (d) Find the net pressure forces, the wire tension $T_A$ and W. (e) What length A–E "
     r"keeps the gate in equilibrium?",
     r"**(a) $z_B = +0.2\ \mathrm{m}$ · (b) $p_D = 10\ \mathrm{kPa}$ on both sides · (c) below D both sides are "
     r"seawater at equal depth · (d) net normal force $8.5 - 7.1 = 1.4\ \mathrm{kN/m}$ → $T_A = W \approx 1.0\ "
     r"\mathrm{kN/m}$ · (e) moments about A → $z_E = -1.0\ \mathrm{m}$.**",
     r"(a) Same pressure at D: $854(z_B + 1.0) = 1025 \times 1.0$.", figure="p. 3, Figure 1.")),
 sec(r"Tut 2 Q2 Rectangular dam (B 10 m, H 36 m, $\mu = 1$)", (4, 4),
   q("CE2134 Tut 2 Q2",
     r"A long rectangular concrete dam ($\rho_c = 2400\ \mathrm{kg/m^3}$) is $B_0 = 10\ \mathrm{m}$ wide and holds "
     r"water to its full height $H = 36\ \mathrm{m}$. Its base is cemented to rock (no uplift) and base friction has "
     r"$\mu = 1$. (a) Find the horizontal water force per metre and its line of action. (b) Show it does not slide. (c) "
     r"Show it overturns. (d) Find the minimum width for overturning stability.",
     r"**(a) $F_H = 6350\ \mathrm{kN/m}$ at 24 m depth · (b) friction 8467 > 6350 ✓ · (c) overturning 76 200 > "
     r"restoring 42 335 kNm/m → overturns · (d) $B_{\min} = 13.4\ \mathrm{m}$.**",
     r"$g = 9.8$. $F_H = \tfrac12\rho gH^2$; $W = \rho_cgB_0H$; overturning $F_HH/3$ vs $WB_0/2$; $B_{\min} = "
     r"\sqrt{F_H(H/3)/(\tfrac12\rho_cgH)}$.", figure="p. 4, Figure 2.")),
 sec("Tut 3 Q1 Sluice gate ($h_1$ 6 m, $h_2$ 3 m)", (5, 5),
   ("eq", r"q = h_1h_2\sqrt{\frac{2g}{h_1 + h_2}}"),
   q("CE2134 Tut 3 Q1",
     r"Steady 2-D flow passes under a sluice gate, from a uniform depth $h_1 = 6\ \mathrm{m}$ upstream to $h_2 = 3\ "
     r"\mathrm{m}$ downstream. Find the discharge per unit width.",
     r"**$q = 18\sqrt{19.6/9} = 26.6\ \mathrm{m^2/s}$.**",
     r"Bernoulli along the free surface plus continuity $q = V_1h_1 = V_2h_2$.", figure="p. 5, Figure 1.")),
 sec("Tut 3 Q2 Venturi insecticide mixer", (6, 6),
   q("CE2134 Tut 3 Q2",
     r"A hose device draws insecticide from an open tank A into water: $Q_A = 0.02\ \mathrm{gal/min}$, $Q = 1\ "
     r"\mathrm{gal/min}$, nozzle diameter $d_h = 0.1\ \mathrm{in}$, feed-line diameter $d_A = 0.015\ \mathrm{in}$, "
     r"hose centre 6 in above the liquid in A, nozzle exit (3) at atmospheric pressure; same density for both liquids. "
     r"(a) Find the pressure at (1) from the streamline out of tank A. (b) Find the velocity at (1) from the streamline "
     r"(1)–(3). (c) Find the device diameter D at (1). (d) Show the ratio $Q_A/Q$ stays constant for large Q.",
     r"**(a) feed-line velocity 11.07 m/s → $p_1 = -62.7\ \mathrm{kPa}$ (gauge) · (b) nozzle $V_3 = 12.7$ → $V_1 = "
     r"16.9\ \mathrm{m/s}$ · (c) $D = 2.2\ \mathrm{mm}$ · (d) for large Q, $p_1 \propto Q^2$ on both branches, so "
     r"$Q_A/Q \to$ constant (0.02).**",
     r"$Q = 6.31 \times 10^{-5}$, $Q_A = 1.26 \times 10^{-6}\ \mathrm{m^3/s}$. The solution writes $d_h = 2.5 "
     r"\times 10^{-4}\ \mathrm{m}$ and '$Q = 5Q_A$', but its working uses $d_h = 2.54\ \mathrm{mm}$ and $Q = 50Q_A$.",
     figure="p. 6, Figure 2.")),
 sec("Tut 4 Q1 Plane jet splitting on a floor", (7, 7),
   q("CE2134 Tut 4 Q1",
     r"A plane jet (speed $U_0$, thickness $h_0$) falls over a brink and strikes a horizontal floor at angle "
     r"$\beta$, splitting into two jets. Neglecting gravity: (a) find the vertical force on the floor; (b) find the "
     r"thicknesses $h_l$ and $h_r$. (c) With $U_0 = 14\ \mathrm{m/s}$, how large can the vertical scale be before "
     r"neglecting gravity gives a 5 % error in the jet speeds?",
     r"**(a) $\rho U_0^2h_0\sin\beta$ · (b) speeds unchanged; $h_r = \tfrac12h_0(1 + \cos\beta)$, $h_l = "
     r"\tfrac12h_0(1 - \cos\beta)$ · (c) about 1 m.**",
     r"(b) Horizontal momentum with no floor friction plus continuity. (c) Bernoulli with gravity: $U^2 = U_0^2 + "
     r"2gl_v$; a 5 % change needs $2gl_v \approx 0.1U_0^2$.", figure="p. 7, Figure 1.")),
 sec(r"Tut 4 Q2 Semi-circular gate, $q = 10\ \mathrm{m^2/s}$", (8, 8),
   q("CE2134 Tut 4 Q2",
     r"A semicircular gate across a wide river is raised to leave a 1.3 m gap; just downstream the depth is $h_2 = 1\ "
     r"\mathrm{m}$, upstream $h_1 = 6\ \mathrm{m}$, and $q = 10\ \mathrm{m^2/s}$. (a) Find the contraction coefficient; "
     r"is it sensible compared with 0.6 for a vertical plane gate? (b) Find the horizontal force on the gate per metre. "
     r"(c) If the gap is closed by a wall, what is the horizontal force then?",
     r"**(a) $C_c = 1.0/1.3 = 0.77$ — higher than 0.6 because the curved lip turns the flow less · (b) $F = 193 - 105 "
     r"= 88\ \mathrm{kN/m}$ · (c) hydrostatic on the wetted 4.7 m: 108 kN/m — larger, because moving water lowers the "
     r"pressure near the lip.**",
     r"(b) Momentum between 1 and 2: $\tfrac12\rho gh_1^2 - \tfrac12\rho gh_2^2 - F = \rho q(V_2 - V_1)$.",
     figure="p. 8, Figure 2.")),
]}

HYDQ[D["SE"]] = {"code": "CE105", "title": "Hydraulics practice · Self-evaluation questions (worked)", "sections": [
 sec("1 Viscosity", (1, 3),
   q("CE2134 Self-evaluation 1-1",
     r"Water flows down an inclined surface with the velocity profile shown. Find the magnitude and direction of the "
     r"shear stress on the surface for $U = 2\ \mathrm{m/s}$, $h = 1\ \mathrm{m}$.",
     r"**$\tau_{\mathrm{wall}} = 2\mu U/h = 4 \times 10^{-3}\ \mathrm{Pa}$, acting down the slope.**",
     r"Differentiate the given profile at the wall; $\mu \approx 10^{-3}\ \mathrm{Pa\,s}$."),
   q("CE2134 Self-evaluation 1-2",
     r"A computer disc spins at 10 000 rpm with the reader head 0.0005 in above it. Estimate the shear force on the "
     r"head from the air between them.",
     r"**$V = R\omega = 532\ \mathrm{m/s}$ → $F = \mu VA/h \approx 0.15\ \mathrm{N}$.**", ""),
   q("CE2134 Self-evaluation 1-3",
     r"A 25 mm shaft is pulled at 3 m/s through a bearing; the 0.3 mm gap holds oil with $\nu = 8 \times 10^{-4}\ "
     r"\mathrm{m^2/s}$ and $\rho = 910\ \mathrm{kg/m^3}$. With a linear velocity profile, find the pull P.",
     r"**$P = \rho\nu(U/\delta)\pi Dl = 286\ \mathrm{N}$** (for the bearing length in the figure).", "")),
 sec("2 Manometers", (4, 5),
   q("CE2134 Self-evaluation 2-1",
     r"A closed water tank with a hemispherical dome connects to an inverted piping system; the top of the pipes holds "
     r"liquid of SG 0.8, the rest water. With gauge A reading 60 kPa, find (a) the pressure in pipe B and (b) the "
     r"pressure head at the dome top C in mm of mercury.",
     r"**(a) $p_B = 60 + 0.8 \times 9.8 \times 3 + 9.8 \times 2 = 103.1\ \mathrm{kPa}$ · (b) $p_C = 60 - 9.8 \times 3 = "
     r"30.6\ \mathrm{kPa}$ = 229.5 mm Hg.**", ""),
   q("CE2134 Self-evaluation 2-2",
     r"An inverted U-tube manometer holds oil and water; $p_A - p_B = -5\ \mathrm{kPa}$. Find the reading h.",
     r"**$h = 0.45\ \mathrm{m}$.**",
     r"A→C→D→B: $p_A - p_B = \rho gH - \rho_mgh$ with $H = 0.2 - 0.3 = -0.1\ \mathrm{m}$.")),
 sec("3 Forces on gates & dams", (6, 8),
   q("CE2134 Self-evaluation 3-1",
     r"A structure on the ocean floor has a 2 m hatch in an inclined wall, hinged on one edge. Find the minimum air "
     r"pressure $p_1$ inside that opens it (ignore hatch weight and hinge friction).",
     r"**$p_1 = p_A + \tfrac23(p_B - p_A) = 1000 \times 9.8 \times (10 + \tfrac23) = 104.5\ \mathrm{kPa}$.**",
     r"Split the outside pressure into a uniform part $p_A$ and a triangle; moments about the hinge."),
   q("CE2134 Self-evaluation 3-2",
     r"Water stands behind a concrete dam (80 ft high, base width $l = 60\ \mathrm{ft}$, $150\ \mathrm{lb/ft^3}$) with "
     r"10 ft of tailwater; leakage gives the uplift pressure shown. Find the maximum water depth h before the dam "
     r"topples about its toe A.",
     r"**Even at $h = H$ the overturning moment (5304) is less than the resisting moment (6539; both divided by $\gamma$, in "
     r"$\mathrm{m^3}$) → always stable; the maximum depth is the full 80 ft.**",
     r"Forces: weight, water on the upstream face, tailwater on the sloping face, uplift (uniform $p_A$ + triangle).")),
 sec("4 Kinematics & continuity", (9, 11),
   q("CE2134 Self-evaluation 4-1",
     r"As a valve opens, the centreline velocity in a diffuser is $V = V_0(1 - x/l)(1 - e^{-ct})$. Find the "
     r"acceleration. For $V_0 = 10\ \mathrm{m/s}$, $l = 5\ \mathrm{m}$, what c (other than 0) makes it zero for all x at "
     r"$t = 1\ \mathrm{s}$? How can it be zero while the flow is increasing?",
     r"**$a = V_0(1 - x/l)[ce^{-ct} - (V_0/l)(1 - e^{-ct})^2]$ → $c = 0.49\ \mathrm{s^{-1}}$; the local (unsteady) "
     r"and convective terms cancel.**", ""),
   q("CE2134 Self-evaluation 4-2",
     r"A wing-tip vortex is approximated by $u = -Ky/(x^2 + y^2)$, $v = Kx/(x^2 + y^2)$. Show that the speed is "
     r"$K/\sqrt{x^2 + y^2}$ and that the streamlines are circles.",
     r"**$|V| = K/r$; $dy/dx = v/u = -x/y$ → $x^2 + y^2 = $ constant.**", ""),
   q("CE2134 Self-evaluation 4-3",
     r"Water at $0.1\ \mathrm{m^3/s}$ and alcohol (SG 0.8) at $0.3\ \mathrm{m^3/s}$ mix in a Y-duct. Find the mixture "
     r"density.",
     r"**$\rho = (0.1 \times 1000 + 0.3 \times 800)/0.4 = 850\ \mathrm{kg/m^3}$.**", "")),
 sec("5 Bernoulli", (12, 15),
   q("CE2134 Self-evaluation 5-1",
     r"Water flows from a large tank through a pipe that splits into two smaller pipes. Ignoring viscosity, find the "
     r"flow rate from the tank and the pressure at point 1.",
     r"**$V_B = 7.67$, $V_D = 11.71\ \mathrm{m/s}$, $Q = 9.1\ \mathrm{L/s}$, $p_1 = 57.8\ \mathrm{kPa}$.**", ""),
   q("CE2134 Self-evaluation 5-2",
     r"A free water jet from a pipe strikes a circular flat plate (axisymmetric flow). Find the flow rate and the "
     r"manometer reading H.",
     r"**$V = 1.59\ \mathrm{m/s}$, $Q = 0.2\ \mathrm{L/s}$, $H = 0.134\ \mathrm{m}$.**", ""),
   q("CE2134 Self-evaluation 5-3",
     r"A conical plug regulates air flow from a pipe; the air leaves the cone edge in a 0.02 m thick sheet. With no "
     r"viscous effects and $Q = 0.5\ \mathrm{m^3/s}$, find the pressure in the pipe.",
     r"**$p = 154\ \mathrm{Pa}$ (gauge).**", ""),
   q("CE2134 Self-evaluation 5-4",
     r"Water flows down a ramp, uniform at sections 1 and 2. Show that Bernoulli and continuity give three solutions "
     r"for the downstream depth, only two of them realistic, and find them.",
     r"**0.032 m and 5.2 m; the third root is negative.**", "")),
 sec("6 Momentum", (16, 18),
   q("CE2134 Self-evaluation 6-1",
     r"Water enters a device vertically and leaves horizontally through a 0.2 m slit as a sheet whose speed rises "
     r"linearly from 0 to 10 m/s along the slit. Find the vertical anchoring force.",
     r"**66.7 N.**", ""),
   q("CE2134 Self-evaluation 6-2",
     r"A hydraulic dredge sucks a sand–water mixture (SG 1.2) from a river bed. Estimate the propeller thrust needed "
     r"to hold the boat still.",
     r"**About 25.4 kN.**", ""),
   q("CE2134 Self-evaluation 6-3",
     r"Water flows at 15 m/s through a horizontal 180° bend of constant area $9000\ \mathrm{mm^2}$; inlet and outlet "
     r"pressures are 210 and 165 kPa. Find the x and y anchoring forces.",
     r"**$F_x = (2\rho V^2 + p_1 + p_2)A = 7.4\ \mathrm{kN}$, $F_y = 0$.**",
     r"$(2 \times 1000 \times 225 + 210\,000 + 165\,000) \times 0.009$.")),
 sec("7 Energy", (19, 20),
   q("CE2134 Self-evaluation 7-1",
     r"A 3 in siphon has a friction loss of $0.8V^2/2$ between A and B. Find the flow rate.",
     r"**$V = \sqrt{2g \times 2.44/1.8} = 5.16\ \mathrm{m/s}$ → $Q = 23.4\ \mathrm{L/s}$.**", ""),
   q("CE2134 Self-evaluation 7-2",
     r"A 100 ft wide river carrying $2400\ \mathrm{ft^3/s}$ flows over a rock pile. Find the flow direction and the "
     r"head loss.",
     r"**$H_1 = 1.39 > H_2 = 1.29\ \mathrm{m}$ → flows from 1 to 2, $h_L = 0.10\ \mathrm{m}$.**", "")),
]}

HYDQ[D["HW"]] = {"code": "CE205", "title": "Hydraulics II practice · Homework 1", "sections": [
 sec("HW1 Q1–Q2 Statics (Part 1)", (1, 7),
   q("CE2134 HW1 Q1",
     r"A long submerged concrete bar with trapezoidal section ABCD sits in a diving pool, its top 2 m below the "
     r"surface: AB = 1.5 m (horizontal, top), AD = 1.2 m (vertical), DC = 2.4 m (bottom, cemented to the pool floor). "
     r"$g = 9.8$, $\rho = 1000\ \mathrm{kg/m^3}$. Find per unit width (1) the force on AB, (2) the force on AD, (3) the "
     r"total pressure force on the block — is it the buoyancy?",
     r"**(1) 29.4 kN/m · (2) 30.6 kN/m · (3) 52.3 kN/m downward — not the buoyancy: no water reaches the cemented "
     r"base, so nothing pushes up.**",
     r"(1) $9.8 \times 2 \times 1.5$. (2) mean depth 2.6 m: $9.8 \times 2.6 \times 1.2$. (3) Horizontal forces on AD "
     r"and BC cancel (same vertical projection). Vertical: AB 29.4 plus the water above BC, $9.8 \times 0.9 \times (2 "
     r"+ 3.2)/2 = 22.9$, both downward.", figure="Homework 1 sheet, p. 1.", src="claude"),
   q("CE2134 HW1 Q2",
     r"Find $p_A - p_B$ for the manometer chain in the figure: benzene at A, a mercury U-tube, kerosene over the top, "
     r"a water U-tube and air at B (densities: benzene 881, mercury 13 600, kerosene 809, water 998, air 1.2 "
     r"$\mathrm{kg/m^3}$; vertical distances 20, 8, 40, 14 and 9 cm as drawn).",
     r"**$p_A - p_B \approx 8.9\ \mathrm{kPa}$.**",
     r"Levels from the left mercury surface: A +20, right mercury top +8, kerosene–water interface +40, water top in "
     r"the last leg +14, B +23 cm. $p_A - p_B = g(-881 \times 0.20 + 13\,600 \times 0.08 + 809 \times 0.32 - 998 \times "
     r"0.26 + 1.2 \times 0.09)$. Check the levels against the figure.", figure="Homework 1 sheet, p. 2.",
     src="claude", checked=False)),
 sec("HW1 Q9–Q12 (Part 2)", (1, 7),
   q("CE2134 HW1 Q9",
     r"A uniform flow of 30 m/s is combined with a source of strength $60\ \mathrm{m^3/s}$ (per unit depth). Locate "
     r"the stagnation point.",
     r"**$r = 60/(2\pi \times 30) = 0.318\ \mathrm{m}$ upstream of the source.**", ""),
   q("CE2134 HW1 Q10–Q11",
     r"Water ($\mu = 1.14 \times 10^{-3}\ \mathrm{Pa\,s}$, $\rho = 998\ \mathrm{kg/m^3}$): (Q10) find the Reynolds "
     r"number for $V = 0.5\ \mathrm{m/s}$ with length scale $h = 0.1\ \mathrm{m}$; (Q11) find it for flow at 4.5 m/s in a "
     r"50 mm pipe. Laminar or turbulent?",
     r"**Q10: $Re = 43\,771$ · Q11: $Re = 196\,974$ → both turbulent.**",
     r"$Re = \rho VL/\mu$. (Statements reconstructed from the steps sheet — the Part 2 question sheet isn't in the "
     r"materials.)"),
   q("CE2134 HW1 Q12",
     r"Water ($\mu = 1.2 \times 10^{-3}$, $\rho = 998$) flows at 12 m/s past a flat plate with a turbulent boundary "
     r"layer. Find the total skin-friction force on the plate.",
     r"**$F_s \approx 82.5\ \mathrm{N}$.**",
     r"Write $Re_\delta = 9.98 \times 10^6\delta$, then $\delta = 0.0148x^{0.8}$ and $\tau_0 = 165x^{-0.2}$; integrate "
     r"$\tau_0$ over the plate.")),
]}
