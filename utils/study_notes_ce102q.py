"""CE102 tutorial questions as q blocks.

CE1101 T2L Tutorials 1–4 (statics and mechanics of materials) have no answer sheets: every answer there was
worked by Claude (src="claude"). CE2155 Tutorials 1–5 print their answers on the sheet (src="official"); where you
handed in your own solution (materials/CE102/*_my_solution.pdf) the answer is marked as yours (src="mine").
Numbers are recomputed in tests/test_tutorial_answers.py."""
from utils.qblock import q

T = "CE102/CE1101_T2L_Tutorial_{}.pdf"
TT = "CE102/CE2155_Tutorial_{}.pdf"


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


def c(set_, question, answer, working="", **kw):
    kw.setdefault("src", "claude")
    return q(set_, question, answer, working, **kw)


MECHQ = {}

# ======================================================================== CE1101 T2L statics
MECHQ[T.format(1)] = {"code": "CE102", "title": "Statics practice · T2L Tutorial 1 (Q1–Q3: cables, jib crane, tower truss)", "sections": [
 sec("Q1 Scoreboard on cable ABC", (1, 1),
   c("CE1101 T2L Q1",
     r"A 9 kN scoreboard is hung from a cable ABC whose ends A and C are hinged 3 m apart. At first it hangs from the "
     r"cable's midpoint B by two short cords to its top corners (0.5 m each side of B). The cable may carry at most 20 "
     r"kN, and B may drop no more than 0.30 m below line AC. Can these limits be met? If so, give the cable length "
     r"and $\theta$; if not, design the alternative with two hanging points $B_1$, $B_2$ a distance x apart.",
     r"**Single point fails: $T \le 20\ \mathrm{kN}$ needs $\sin\theta \ge 0.225$ ($\theta \ge 13.0^\circ$), so $d "
     r"\ge 1.5\tan 13.0^\circ = 0.346\ \mathrm{m} > 0.30$. Two points at the board's corners ($x = 1.0\ \mathrm{m}$) "
     r"work: take the cable 3.08 m long → $\theta \approx 15.9^\circ$, $d \approx 0.29\ \mathrm{m}$, $T \approx 16.4\ "
     r"\mathrm{kN}$** (any length from 3.053 to 3.088 m satisfies both limits).",
     r"One point: $2T\sin\theta = 9$. Two points: each carries 4.5 kN and the middle segment is horizontal, so "
     r"$T\sin\theta = 4.5$; with 1.0 m horizontal on each side, $d = \tan\theta$. $T \le 20$ → $d \ge 0.231$; $d \le "
     r"0.30$. Length $= 1 + 2\sqrt{1 + d^2}$. Any $x \ge 0.40\ \mathrm{m}$ can work in principle; hanging at the corners "
     r"also keeps the board level.", figure="p. 1: both hanging arrangements.")),
 sec("Q2 Jib crane", (2, 2),
   c("CE1101 T2L Q2",
     r"Design a jib crane for 6 kN truck engines: a beam (0.3 kN/m, length 5.5–6.5 m) pinned to a column and held by "
     r"a tie rod from height h ($\le 4\ \mathrm{m}$) on the column to a point b along the beam; the hoist travels to "
     r"within 0.3 m of the free end. The tie rod must resist 2.5 times the engine's static effect. Choose a, b and h "
     r"to minimise the tie-rod force, and suggest improvements.",
     r"**Beam 5.5 m, tie rod to the beam end ($b = 5.5\ \mathrm{m}$) from $h = 4\ \mathrm{m}$, hoist reach $a = 5.2\ "
     r"\mathrm{m}$ → $T = 11.0\ \mathrm{kN}$ static, 25.5 kN with the 2.5 factor on the engine.**",
     r"Moments about the pin: $T \cdot hb/\sqrt{h^2 + b^2} = 6a + 0.3l^2/2$. For fixed h the factor $\sqrt{h^2 + "
     r"b^2}/(hb)$ falls as b grows, so attach at the end; take h at its 4 m limit; a shorter beam lowers the moment "
     r"($l = 6.5\ \mathrm{m}$ gives 12.8 kN, against 11.0 for 5.5 m). Design: $(2.5 \times 6 \times 5.2 + 0.15 \times 5.5^2) \times \sqrt{16 + "
     r"30.25}/22$. Improvements: a taller column (larger h), end stops for the trolley, a counterweight or back-stay, "
     r"a lighter beam.", figure="p. 2: jib crane.")),
 sec("Q3 Water-tank tower under wind", (3, 3),
   c("CE1101 T2L Q3",
     r"A full 2 m water tank ($\rho = 1000\ \mathrm{kg/m^3}$, $g = 9.81$) sits on a tower 6 m tall (three 2 m panels; "
     r"legs from 3.0 m apart at the base to 2 m at the deck) and takes a 3.0 kPa wind pressure, its resultant 1.4 m "
     r"above the deck. Find a bracing layout with the fewest members for stability that also minimises the force in "
     r"the critical main leg (GH), and report all main-leg forces.",
     r"**Per frame: horizontals BG and CF plus one diagonal per panel, each running down towards the leeward leg "
     r"(B–H, C–G, D–F) — 12 members. Leeward legs: GH 31.9, FG 28.5, EF 23.9 kN; windward legs: AB 4.8, BC 7.5, CD "
     r"10.9 kN — all compression.**",
     r"Stability: $m + r = 2j$ → $m = 2 \times 8 - 4 = 12$. Loads per frame (front and back frames share): weight $8 "
     r"\times 9.81/2 = 39.24\ \mathrm{kN}$, wind $3 \times 4/2 = 6\ \mathrm{kN}$ with moment $6 \times 1.4$ → deck "
     r"loads 15.42 (D) and 23.82 kN (E) plus 6 kN horizontal. Method of sections about the joint where the cut "
     r"diagonal meets the other leg: GH about B gives 31.9 kN; a diagonal A–G instead gives 34.5 kN. Wind can reverse, "
     r"so a real tower needs bracing for both directions.", figure="p. 3: front and side views.", checked=False)),
]}

MECHQ[T.format(2)] = {"code": "CE102", "title": "Statics practice · T2L Tutorial 2 (Q4–Q6: frame, cable, stacked blocks)", "sections": [
 sec("Q4 Pin-connected structure, best position of D", (1, 1),
   c("CE1101 T2L Q4",
     r"(a) A frame has a horizontal member AB pinned to a wall at A, a horizontal member EC pinned at E (1.5 m below "
     r"A, length 6 m), a member BC joining their ends with an arm carrying an upward 10 kN load 0.5 m beyond C, and a "
     r"rod BD from B to D on EC at 30°. Find the rod tension and the forces on each member. (b) D may sit anywhere "
     r"along CE: find the best position.",
     r"**(a) $T_{BD} = 46.2\ \mathrm{kN}$; AB 43.3 kN compression; E: 43.3 kN outward (EC in tension) and 10 kN; pin "
     r"C: $(3.33, 13.1)\ \mathrm{kN}$ · (b) the horizontal part of T is always 40 kN, so $T = 40/\cos\phi$ falls as D "
     r"moves towards E: at E, $T = 41.2\ \mathrm{kN}$, CE carries no bending and the pin forces are smallest → put D at "
     r"or near E (subject to rod length and clearance).**",
     r"Whole frame, moments about E: $1.5A_x = 6.5 \times 10$ → $A_x = 43.3$. Member BC, moments about C: $1.5(43.3 - "
     r"T\cos\phi) = 0.5 \times 10$ → $T\cos\phi = 40.0$. Vertical force from the rod on CE: $T\sin\phi = 60/(6 - x)$, "
     r"so bending in CE grows quickly as D approaches C.", figure="p. 1: frame.")),
 sec("Q5 Traffic-light cable", (2, 2),
   c("CE1101 T2L Q5",
     r"Traffic lights of 15, 30 and 15 kg hang at B, C, D on a cable between A and E at the same level (spacings 1.5, "
     r"3.0, 3.0, 1.5 m; $g = 10$). The mid-span sag $y_2$ must be under 1.0 m and the cable tension under 1000 N. Find "
     r"the minimum cable length and the sags at each light.",
     r"**$H = 954\ \mathrm{N}$ (tension limit) → $y_1 = 0.472\ \mathrm{m}$ at B and D, $y_2 = 0.943\ \mathrm{m}$ at C, "
     r"length 9.22 m; $T_{\max} = 1000\ \mathrm{N}$ in AB and DE.**",
     r"Support reactions 300 N each; constant horizontal tension H. AB: $y_1/1.5 = 300/H$; BC: $(y_2 - y_1)/3 = 150/H$ "
     r"→ $y_2 = 2y_1$. A shorter cable means less sag and more tension: $\sqrt{H^2 + 300^2} = 1000$. Length $= "
     r"2[\sqrt{1.5^2 + y_1^2} + \sqrt{3^2 + (y_2 - y_1)^2}]$.", figure="p. 2: cable and lights.")),
 sec("Q6 Stack of blocks", (3, 3),
   c("CE1101 T2L Q6",
     r"Four blocks of equal length l are stacked (I on top, IV on the table); $W_I = W_{III} = W_{IV} = w$, $W_{II} = "
     r"2w$. Find the largest overhang x of the top block beyond block IV before the stack topples.",
     r"**$x = l/2 + l/3 + l/8 = 23l/24 \approx 0.96l$.**",
     r"Work down from the top: I may overhang II by $l/2$; the centre of gravity of I + II (3w) must sit over III's "
     r"edge → II overhangs III by $l/3$; that of I + II + III (4w) over IV's edge → III overhangs IV by $l/8$.",
     figure="p. 3: the stack.")),
]}

# ======================================================================== CE1101 T2L mechanics of materials
MECHQ[T.format(3)] = {"code": "CE102", "title": "Mechanics practice · T2L Tutorial 3 (Q1–Q3: axial members)", "sections": [
 sec("Q1 Connecting rod; biaxial fabric", (1, 1),
   c("CE1101 T2L Q1 (MoM)",
     r"(a) A piston pushes with constant force P on a connecting rod AB (area A, length L) whose end B turns on a crank "
     r"of radius R. (i) Find $P_{\mathrm{allow}}$ for an allowable compressive stress $\sigma_c$ in the rod. (ii) "
     r"Evaluate it for $\sigma_c = 150\ \mathrm{MPa}$, $A = 63.62\ \mathrm{mm^2}$, $R = 0.28L$. (b) A fabric (E = 87 "
     r"GPa, $\nu = 0.34$) carries $\sigma_x = 120$ and $\sigma_z = 160\ \mathrm{MPa}$. Find the change in length of "
     r"side AB (100 mm, along x), side BC (75 mm, along z) and diagonal AC.",
     r"**(a) $P_{\mathrm{allow}} = \sigma_cA\sqrt{1 - (R/L)^2} = 9.16\ \mathrm{kN}$ · (b) AB 0.0754 mm, BC 0.103 mm, "
     r"AC 0.122 mm.**",
     r"(a) The rod force is $P/\cos\alpha$, largest when the crank is perpendicular to the cylinder axis, $\sin\alpha "
     r"= R/L$. (b) $\varepsilon_x = (120 - 0.34 \times 160)/87\,000$, $\varepsilon_z = (160 - 0.34 \times 120)/87\,000$; "
     r"diagonal $\delta_{AC} = (100\delta_{AB} + 75\delta_{BC})/125$.", figure="p. 1.")),
 sec("Q2 Tapered plate; mine-shaft cable", (2, 2),
   c("CE1101 T2L Q2 (MoM)",
     r"(a) A plate of thickness t tapers linearly in width from a to 2a over length L under axial load P. (i) Find "
     r"its elongation. (ii) Evaluate for $P = 50\ \mathrm{kN}$, $a = 25\ \mathrm{mm}$, $L = 5\ \mathrm{m}$, $t = 10\ "
     r"\mathrm{mm}$, $E = 80\ \mathrm{GPa}$. (b) A 450 m steel cable ($w = 6.1\ \mathrm{N/m}$) hangs in a mine shaft "
     r"with $P = 22.0\ \mathrm{kN}$ at its lower end; the strain at mid-height is 0.00223. Find the strain at the top and "
     r"bottom and the cable's elongation.",
     r"**(a) $\delta = PL\ln 2/(Eta) = 8.66\ \mathrm{mm}$ · (b) $\varepsilon_A = 0.00236$, $\varepsilon_B = "
     r"0.00210$, $\delta = 1.00\ \mathrm{m}$.**",
     r"(a) $\int_0^L P\,dx/[Et\,a(1 + x/L)]$. (b) Strain is proportional to the axial force $P + wx$ (x up from B), "
     r"which is linear, so the mid-height strain is the average: $\delta = 0.00223 \times 450$.", figure="p. 2.")),
 sec("Q3 Minimum-weight two-bar truss; rigid bar on two rods", (3, 3),
   c("CE1101 T2L Q3 (MoM)",
     r"(a) Bars AC (inclined at $\alpha$) and BC (horizontal, fixed length L) carry a vertical load P at C with the "
     r"same allowable stress in tension and compression. Find $\alpha$ for minimum weight. (b) A rigid member ABCD is "
     r"pinned at B and hung from a brass rod AE ($E = 105\ \mathrm{GPa}$) at A and an aluminium rod CF ($E = 70\ "
     r"\mathrm{GPa}$) at C, both 0.15 m long with area $500\ \mathrm{mm^2}$; AB = 0.2, BC = 0.15, CD = 0.25 m. Find "
     r"the displacement of D under 40 kN.",
     r"**(a) $\cos^2\alpha = 1/3$ → $\alpha = 54.7^\circ$ (volume $2\sqrt2\,PL/\sigma$) · (b) $\delta_D = 0.333\ "
     r"\mathrm{mm}$ downward.**",
     r"(a) $V = (PL/\sigma)(1 + \cos^2\alpha)/(\sin\alpha\cos\alpha)$; set $dV/d\alpha = 0$. (b) Rotation $\theta$ "
     r"about B: rod forces $k_b(0.2\theta)$ and $k_a(0.15\theta)$ with $k = EA/L$; moments about B: $40 \times 0.4 = "
     r"(350 \times 0.04 + 233.3 \times 0.0225) \times 10^6\theta$ → $\theta = 8.31 \times 10^{-4}$; $\delta_D = "
     r"0.4\theta$.", figure="p. 3.")),
]}

MECHQ[T.format(4)] = {"code": "CE102", "title": "Mechanics practice · T2L Tutorial 4 (Q4–Q6: torsion, bending, deflection)", "sections": [
 sec("Q4 Geared shafts; rod with distributed torque", (1, 1),
   c("CE1101 T2L Q4 (MoM)",
     r"(a) Steel shafts ($G = 80\ \mathrm{GPa}$) are linked by gears: shaft AB ($d_1 = 40\ \mathrm{mm}$, 1 m, fixed at "
     r"A) carries a 300 mm gear; shaft CD ($d_2 = 30\ \mathrm{mm}$, 1.5 m) carries a 200 mm gear, and $T = 400\ "
     r"\mathrm{N\,m}$ acts at D. Find the rotation at D and the maximum shear stress in each shaft. (b) A rod ABC of "
     r"radius c is embedded over its length C–B (L/2) in a material whose torque reaction rises linearly from 0 at C to "
     r"$t_0$ at B; a lever at A carries a couple Pd. Find $t_0$ and the twist of end A (shear modulus G).",
     r"**(a) $\phi_D = 0.139\ \mathrm{rad} = 7.97^\circ$; $\tau_{\max}$ 47.7 MPa (AB, $T = 600\ \mathrm{N\,m}$) and "
     r"75.5 MPa (CD) · (b) $t_0 = 4Pd/L$, $\phi_A = 4PdL/(3\pi c^4G)$.**",
     r"(a) Contact force $400/0.1 = 4000\ \mathrm{N}$ → $T_{AB} = 4000 \times 0.15 = 600$. $\phi_B = 600 \times "
     r"1/(GJ_1) = 0.0298$; gears: $\phi_C = 1.5\phi_B$; $\phi_D = \phi_C + 400 \times 1.5/(GJ_2)$. (b) $\tfrac12t_0(L/2) "
     r"= Pd$; twist = $Pd(L/2)/(GJ) + \int_0^{L/2}(t_0x^2/L)\,dx/(GJ)$ with $J = \pi c^4/2$.", figure="p. 1.")),
 sec("Q5 SFD/BMD: bracket cantilever; aircraft wing", (2, 2),
   c("CE1101 T2L Q5 (MoM)",
     r"(a) A 0.9 m cantilever (fixed at the left) has a 0.4 m post at 0.2 m carrying 5 kN horizontally at its top, a "
     r"0.2 m hanger at 0.6 m carrying 20 kN horizontally at its bottom, and 10 kN down at the free end. Draw the shear "
     r"and moment diagrams, give the maxima and sketch the deflected shape. (b) A wing (tapered cantilever, fixed at "
     r"A on the fuselage) carries a dead load rising linearly from 0 at the tip C to 3.75 kN/m at A over 3.9 m, an "
     r"engine of 15 kN at B (2.4 m from C) and a 75 kN landing-gear reaction up at D (3.0 m from C). Find the reactions "
     r"at A and the maximum shear and moment.",
     r"**(a) $V = 10\ \mathrm{kN}$ throughout; M: −7 at the wall, −5 / −3 either side of the post, −3 / +1 either "
     r"side of the hanger, 0 at the tip → $M_{\max} = 7\ \mathrm{kNm}$ (hogging) at the wall; axial tension 25 kN then "
     r"20 kN · (b) $A_y = 52.7\ \mathrm{kN}$ down, $M_A = 35.5\ \mathrm{kNm}$; $V_{\max} = 55.7\ \mathrm{kN}$ between D "
     r"and A; $M_{\max} = 35.5\ \mathrm{kNm}$ at A (−13.3 kNm at D).**",
     r"(a) The offset horizontal loads add couples: $5 \times 0.4 = 2$ (clockwise) and $20 \times 0.2 = 4\ "
     r"\mathrm{kNm}$ (anticlockwise). From the tip: $M = -10a$, +4 past the hanger, −2 past the post. A short sagging "
     r"stretch between 0.5 and 0.6 m; otherwise it curves downwards. (b) Load total $\tfrac12 \times 3.9 \times 3.75 = "
     r"7.31\ \mathrm{kN}$ at 1.3 m from A; $M_A = 7.31 \times 1.3 + 15 \times 1.5 - 75 \times 0.9$.",
     figure="p. 2.")),
 sec("Q6 Combined stress; maximum deflection", (3, 3),
   c("CE1101 T2L Q6 (MoM)",
     r"(a) A 1.8 m beam AB (I-section 220 mm deep, $I = 70 \times 10^{-6}\ \mathrm{m^4}$, $A = 1800 \times 10^{-6}\ "
     r"\mathrm{m^2}$) is pinned at A and held at B by a cable to C, 1.17 m above A; 45 kN acts 0.45 m from B. Find the "
     r"largest normal stress at section D (mid-span). (b) A simply supported beam of span 3L carries $P = q_0L/2$ at L "
     r"from A and $q_0$ over the last third. Find the maximum deflection and where it occurs.",
     r"**(a) $\sigma_{\max} = 44.8\ \mathrm{MPa}$ compression (top of D) · (b) $\delta_{\max} = 0.500q_0L^4/EI$ at $x "
     r"= 1.528L$ from A.**",
     r"(a) Moments about A: $T_y \times 1.8 = 45 \times 1.35$ → $T_y = 33.75$, $T_x = 33.75 \times 1.8/1.17 = 51.9\ "
     r"\mathrm{kN}$ (compression in AB). $M_D = 33.75 \times 0.9 - 45 \times 0.45 = 10.1\ \mathrm{kNm}$; $\sigma = "
     r"-51.9/1800 - 10.1 \times 0.11/70$ (kN, mm, MPa). (b) $R_A = q_0L/2$; integrate with Macaulay terms; $C_1 = "
     r"-0.514q_0L^3$; the slope is zero at $x = 55L/36$.", figure="p. 3.")),
]}

# ======================================================================== CE2155 (answers printed on the sheets)
MECHQ[TT.format(1)] = {"code": "CE102", "title": "Mechanics practice · CE2155 Tutorial 1 (revision)", "sections": [
 sec("Stress, strain, torsion, beams", (1, 2),
   q("CE2155 Tut 1 (Hibbeler 1-54)",
     r"A 2 Mg concrete pipe hangs from cables AB and AC at 30° and 45° to the vertical (diameters 12 and 10 mm). Find "
     r"the average normal stress in each cable.",
     r"**127 MPa (AB) and 129 MPa (AC).**",
     r"$T_{AB}\sin 30^\circ = T_{AC}\sin 45^\circ$, $T_{AB}\cos 30^\circ + T_{AC}\cos 45^\circ = 19.62\ \mathrm{kN}$ → "
     r"14.36 and 10.16 kN."),
   q("CE2155 Tut 1 (Hibbeler 2-21)",
     r"A 400 × 300 mm plate deforms as shown (dashed). Find the average normal strain along diagonal AC and the shear "
     r"strain at corner A.",
     r"**0.0168 mm/mm and 0.0116 rad.**", "", figure="p. 1."),
   q("CE2155 Tut 1 (Hibbeler 5-25)",
     r"A 25 mm bent rod weighing 225 N/m (segments as shown) — find the maximum torsional stress at section B due to "
     r"its own weight.",
     r"**52.8 MPa** ($T_B = 162\ \mathrm{N\,m}$).", "", figure="p. 1."),
   q("CE2155 Tut 1 (Hibbeler 6-38)",
     r"A compound beam is fixed at A, pinned at B and on a roller at C (2 + 2 + 2 m), with 600 N at 2 m and 400 N/m on "
     r"B–C. Draw the shear and moment diagrams.",
     r"**V: 1000 N (A–2 m), 400 N (2–4 m), then falling to −400 N at C · M: −2800 at A, −800 at 2 m, 0 at B, +200 "
     r"N·m at 5 m, 0 at C.**", r"B–C alone: reactions 400 N each; the 400 N at B loads the cantilever A–B.",
     figure="p. 2."),
   q("CE2155 Tut 1 (Hibbeler 6-99)",
     r"A built-up timber beam (4 m span plus 2 m overhang, 8 kN/m, 12 kN at the tip; section as shown) has $\sigma_"
     r"{\mathrm{allow}} = 6\ \mathrm{MPa}$. Find the minimum depth d to the nearest mm.",
     r"**$d = 410\ \mathrm{mm}$.**", "", figure="p. 2.")),
]}

MECHQ[TT.format(2)] = {"code": "CE102", "title": "Mechanics practice · CE2155 Tutorial 2 (shear stress & shear flow)", "sections": [
 sec("Shear stress and shear flow", (1, 2),
   q("CE2155 Tut 2 (Hibbeler 7-6)",
     r"A hollow timber box beam (200 mm deep, walls as shown) has $\tau_{\mathrm{allow}} = 7\ \mathrm{MPa}$. Find the "
     r"largest shear force V.",
     r"**$V = 100\ \mathrm{kN}$.**", "", figure="p. 1."),
   q("CE2155 Tut 2 (Hibbeler 7-15)",
     r"Find the maximum shear stress in the T-beam (150 × 30 flange, 150 × 30 web) at the section of maximum shear, "
     r"for the loading shown.",
     r"**7.33 MPa.**", "", figure="p. 1."),
   q("CE2155 Tut 2 (Hibbeler 7-50 and 7-50A)",
     r"A built-up section carries $V = 25\ \mathrm{kN}$. Find the shear flow at A and B (interfaces), first exactly, "
     r"then with the thin-walled (centreline) approximation at E and F.",
     r"**Exact 65.1 and 43.6 kN/m; thin-walled 62.4 and 44.8 kN/m.**", "", figure="pp. 1–2."),
   q("CE2155 Tut 2 (Hibbeler R7-4)",
     r"Four boards glued at their seams form a beam: two 12 mm side boards 249 mm deep and two 100 × 12 mm inner "
     r"boards 75 mm from the top and bottom. If the glue resists 15 kN/m, find the largest vertical shear V.",
     r"**$V \approx 20.4\ \mathrm{kN}$.**",
     r"$I = 35.4 \times 10^6\ \mathrm{mm^4}$; each inner board: $Q = 1200 \times 43.5 = 52\,200\ \mathrm{mm^3}$, held "
     r"by two seams → $V = 2 \times 15 \times I/Q$. (From your own solution sheet for R7-4.)",
     figure="p. 2.", src="mine")),
]}

MECHQ[TT.format(3)] = {"code": "CE102", "title": "Mechanics practice · CE2155 Tutorial 3 (combined loading)", "sections": [
 sec("Combined loading", (1, 1),
   q("CE2155 Tut 3 (Hibbeler 8-26)",
     r"A column of two glued 150 × 300 mm boards carries P = 50 kN at the eccentric point shown. Find the maximum normal "
     r"stress.",
     r"**$\sigma_{\max} = 2.34\ \mathrm{MPa}$ (compression).**", "", figure="p. 1."),
   q("CE2155 Tut 3 (Hibbeler 8-31)",
     r"A drill jammed in a wall has 20 N·m torque and a 150 N force on the handle. Find the state of stress at A on "
     r"section a–a of the 5 mm bit.",
     r"**215 MPa normal and 102 MPa shear at A** (see the element on the sheet).", "", figure="p. 1."),
   q("CE2155 Tut 3 (Hibbeler 8-63)",
     r"A 2 × 1 m sign under 1.5 kPa wind sits on a 100 mm post. Find the stresses at A and B on the post.",
     r"**A: 107 MPa normal, 15.3 MPa shear · B: 14.8 MPa shear.**", "", figure="p. 1.")),
 sec("Q4 Bent pipe: reactions and stresses at C", (2, 2),
   q("CE2155 Tut 3 Q4",
     r"A pipe (outer radius R, thickness t) rises a from its fixed end D, then runs horizontally b to its free end B, "
     r"where P acts in −x and F in +y. (a) Find the fixed-end reactions, including torsion. (b) Which of them cause "
     r"stress at C = (0, R, 0), and in which directions?",
     r"**(a) Forces P (x) and F (y); moments $M_x = Fa$, $M_y = Pa$ (bending) and $M_z = Fb$ (torsion) · (b) at C: "
     r"normal stress $\sigma_z$ from $M_x$ (C is an extreme fibre for it; compression on the +y side), shear "
     r"$\tau_{zx}$ from the torsion $Fb$ and from the shear force P; $M_y$ and F give nothing at C (C lies on the "
     r"neutral axis of $M_y$ and at a free edge for F's shear flow).**",
     r"From your own solution sheet for Q4. Check: $M = r_B \times F$ with $r_B = (-b, 0, a)$.",
     figure="p. 2, Figures a–c.", src="mine")),
]}

MECHQ[TT.format(4)] = {"code": "CE102", "title": "Mechanics practice · CE2155 Tutorial 4 (stress & strain transformation)", "sections": [
 sec("Stress transformation", (1, 2),
   q("CE2155 Tut 4 (Hibbeler 9-14)",
     r"At a point $\sigma_x = -30\ \mathrm{MPa}$, $\sigma_y = 0$, $\tau = 12\ \mathrm{MPa}$. Find (a) the principal "
     r"stresses and (b) the maximum in-plane shear and average normal stress, with orientations.",
     r"**(a) 4.21 and −34.2 MPa (principal planes at 19.3°) · (b) 19.2 MPa with −15 MPa average (planes at "
     r"25.7°).**",
     r"Centre −15, radius $\sqrt{15^2 + 12^2} = 19.2$.", figure="p. 1."),
   q("CE2155 Tut 4 (Hibbeler 9-44)",
     r"Find the principal stresses at A, at the bottom of the web of the cantilever I-beam under the triangular load "
     r"shown.",
     r"**6.53 MPa and −21.6 MPa (at 61.2°).**", "", figure="p. 1."),
   q("CE2155 Tut 4 (Hibbeler 9-72)",
     r"Find the normal and shear stresses at D, perpendicular and parallel to grain at 30°, just left of the 10 kN load "
     r"on the timber frame.",
     r"**470 kPa normal and 592 kPa parallel to the grain.**", "", figure="p. 2."),
   q("CE2155 Tut 4 (Hibbeler 10-28)",
     r"A 45° rosette reads $\varepsilon_a = 650$, $\varepsilon_b = -300$, $\varepsilon_c = 480\ (\times 10^{-6})$. Find "
     r"(a) the principal strains and (b) the maximum in-plane shear strain and average normal strain.",
     r"**(a) $1434 \times 10^{-6}$ and $-304 \times 10^{-6}$ · (b) $1738 \times 10^{-6}$ with $565 \times 10^{-6}$.**",
     r"$\varepsilon_x = 650$, $\varepsilon_y = 480$, $\gamma_{xy} = 2\varepsilon_b - (\varepsilon_a + \varepsilon_c) = "
     r"-1730$.", figure="p. 2.")),
 sec("Q5 Strain gauge on a shaft", (3, 3),
   q("CE2155 Tut 4 Q5",
     r"A solid 50 mm radius shaft ($E = 200\ \mathrm{GPa}$, $\nu = 0.25$) under torque T has a strain gauge at 15° to "
     r"its axis reading $-180 \times 10^{-6}$. Using Mohr's circle, find (a) T and (b) the principal stresses and their "
     r"orientation.",
     r"**(a) $T = 11.3\ \mathrm{kN\,m}$ · (b) $\pm 57.6\ \mathrm{MPa}$ at 45° to the axis (pure shear).**",
     r"$G = E/[2(1 + \nu)] = 80\ \mathrm{GPa}$; $\varepsilon_{15^\circ} = (\gamma/2)\sin 30^\circ$ → $\gamma = 720 \times "
     r"10^{-6}$, $\tau = 57.6\ \mathrm{MPa}$; $T = \tau J/c$. From your own solution sheet for Q5.",
     figure="p. 3.", src="mine")),
]}

MECHQ[TT.format(5)] = {"code": "CE102", "title": "Mechanics practice · CE2155 Tutorial 5 (column buckling)", "sections": [
 sec("Buckling", (1, 2),
   q("CE2155 Tut 5 (Hibbeler 13-26)",
     r"A pin-jointed truss (3 m deep, 4 m panels) carries two loads P; member AG is a 50 mm A-36 steel rod ($E = 200\ "
     r"\mathrm{GPa}$). Find the largest P without AG buckling.",
     r"**$P = 14.5\ \mathrm{kN}$.**", "", figure="p. 1."),
   q("CE2155 Tut 5 (Hibbeler 13-27)",
     r"Member AB (30 × 20 mm steel, 2 m; pinned for x–x and fixed for y–y buckling; $E = 200\ \mathrm{GPa}$, $\sigma_Y = "
     r"360\ \mathrm{MPa}$) props beam BC, which carries w over 1.5 m plus a 0.5 m overhang. With a factor of safety of 3, "
     r"find the largest w.",
     r"**$w = 5.55\ \mathrm{kN/m}$.**", "", figure="p. 1."),
   q("CE2155 Tut 5 (Hibbeler 13-47)",
     r"A W360 × 39 column (6 m, fixed at the top, pinned at the bottom; $A = 4960\ \mathrm{mm^2}$, $I_x = 102 \times "
     r"10^6$, $I_y = 3.75 \times 10^6\ \mathrm{mm^4}$) carries 75 kN at 250 mm eccentricity. Find the maximum stress.",
     r"**48.0 MPa.**", "", figure="p. 2."),
   c("CE2155 Tut 5 (Hibbeler 13-64)",
     r"A W310 × 74 column (7.5 m, fixed at the bottom, pinned at the top by cables; $A = 9480\ \mathrm{mm^2}$, $I_x = "
     r"165 \times 10^6$, $I_y = 23.4 \times 10^6\ \mathrm{mm^4}$, $d = 310\ \mathrm{mm}$, $E = 200\ \mathrm{GPa}$, "
     r"$\sigma_Y = 250\ \mathrm{MPa}$) carries P at 50 mm eccentricity. Find the P that causes failure by buckling or "
     r"yielding. (Self-practice; no answer on the sheet.)",
     r"**$P \approx 1.55\ \mathrm{MN}$ — yielding by the secant formula (eccentricity in the web plane) governs over "
     r"weak-axis buckling at 1.68 MN.**",
     r"$K = 0.7$, $L_e = 5.25\ \mathrm{m}$. Buckling about y: $\pi^2EI_y/L_e^2 = 1676\ \mathrm{kN}$ ($\sigma = 177 < "
     r"250$, elastic). Secant about x: $r_x = 131.9$, $ec/r^2 = 50 \times 155/131.9^2 = 0.445$; solve $250 = (P/A)[1 + "
     r"0.445\sec(\tfrac{L_e}{2r_x}\sqrt{P/EA})]$ → 1550 kN. If the 50 mm were about the weak axis the answer would drop "
     r"to about 550 kN.", figure="p. 2.", checked=False)),
]}
