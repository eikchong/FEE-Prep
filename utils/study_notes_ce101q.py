"""CE101 materials tutorials (CE2155 Part I, Tutorials 1–5) as q blocks, one page per tutorial sheet.
The sheets have no official answers: all answers here were written by Claude from the lecture notes."""
from utils.qblock import q

MT = "CE101/CE2155_Mat_Tutorial_{}.pdf"


def sec(title, pages, *blocks):
    return {"title": title, "pages": list(pages), "blocks": list(blocks)}


def c(set_, question, answer, working="", **kw):
    kw.setdefault("src", "claude")
    return q(set_, question, answer, working, **kw)


MATQ = {}

MATQ[MT.format(1)] = {"code": "CE101", "title": "Materials tutorial 1 · Cement (lecture 2)", "sections": [
 sec("Tutorial 1 — Cement", (1, 1),
   c("CE2155 Mat Tut 1 Q1",
     r"What component is inter-ground with cement clinker in the final stage of manufacture, and why is it needed?",
     r"**Gypsum ($\mathrm{CaSO_4 \cdot 2H_2O}$).** It supplies sulfate so $\mathrm{C_3A}$ forms ettringite instead "
     r"of hydrating at once — this prevents flash set and controls setting.",
     r"The amount rises with the $\mathrm{C_3A}$ content; too much affects setting and causes expansion."),
   c("CE2155 Mat Tut 1 Q2",
     r"What are the four main phases of Portland cement clinker? Which contributes most to strength in the first few "
     r"weeks?",
     r"**$\mathrm{C_3S}$, $\mathrm{C_2S}$, $\mathrm{C_3A}$, $\mathrm{C_4AF}$; $\mathrm{C_3S}$ gives most of the "
     r"early strength** (first 3–4 weeks); $\mathrm{C_2S}$ contributes later."),
   c("CE2155 Mat Tut 1 Q3",
     r"How does Type III (high early strength) cement differ from Type I (ordinary)?",
     r"**More $\mathrm{C_3S}$ (and $\mathrm{C_3A}$) and ground finer** → faster hydration, high early strength and "
     r"more early heat; long-term strength is similar.",
     r"Used for precast work, cold weather and early striking."),
   c("CE2155 Mat Tut 1 Q4",
     r"Describe the two types of porosity in hardened cement paste and where they come from.",
     r"**Gel pores** ($< 10\ \mathrm{nm}$): the spaces within C-S-H itself. **Capillary pores** ($> 10\ "
     r"\mathrm{nm}$): what is left of the original water-filled space between cement grains that hydrates did not "
     r"fill — they grow with w/c and control permeability and strength."),
   c("CE2155 Mat Tut 1 Q5",
     r"Replacing Portland cement with fly ash can help in many ways. List three, and give a case where fly ash is not "
     r"beneficial.",
     r"**Lower heat of hydration, better workability, better long-term strength and durability (also lower cost and "
     r"$\mathrm{CO_2}$). Not beneficial when high early strength is needed** — early striking, cold weather, "
     r"fast-track or precast work.",
     r"Spherical particles cut water demand; the pozzolanic reaction uses CH and refines pores (sulfate and chloride "
     r"resistance); early strength gain is slower."),
   c("CE2155 Mat Tut 1 Q6",
     r"What is the difference between silica fume and Class F fly ash?",
     r"**Silica fume:** by-product of silicon metal, ≥ 90 % amorphous $\mathrm{SiO_2}$, 10–100 nm, very reactive, "
     r"raises water demand and adds early strength. **Class F fly ash:** coal combustion residue, $\mathrm{SiO_2 + "
     r"Al_2O_3 + Fe_2O_3} \ge 70\,\%$, 1–300 µm spheres, slowly pozzolanic, improves flow."),
 ),
]}

MATQ[MT.format(2)] = {"code": "CE101", "title": "Materials tutorial 2 · Aggregate & admixtures (lectures 3–4)", "sections": [
 sec("Tutorial 2 — Aggregate & admixtures", (1, 1),
   c("CE2155 Mat Tut 2 Q1", r"How does the maximum aggregate size affect the amount of paste in concrete?",
     r"**A larger, well-graded maximum size lowers the total surface area and voids, so less water and paste are "
     r"needed for the same workability** (limited by member size and bar spacing)."),
   c("CE2155 Mat Tut 2 Q2",
     r"A sand has an absorption capacity of 1.5 % and the pile's total moisture is 5 %. What is its free moisture?",
     r"**$5 - 1.5 = 3.5\,\%$** of the oven-dry mass — reduce the mixing water by this amount.", "", checked=True),
   c("CE2155 Mat Tut 2 Q3",
     r"Why are plasticising admixtures called water reducers? How does ASTM C494 distinguish normal from high-range "
     r"water reducers?",
     r"**They disperse flocculated cement, so the same slump needs less water. Type A (normal) reduces water by at "
     r"least 5 %; Type F (high-range, superplasticiser) by at least 12 %.**"),
   c("CE2155 Mat Tut 2 Q4",
     r"How do the surfactants for air entrainment and for water reduction differ in composition and action?",
     r"**Air-entraining:** hydrophilic head with a hydrophobic tail, acting at the air–water interface to stabilise "
     r"small bubbles. **Water-reducing:** anionic polymers that adsorb at the cement–water interface and disperse "
     r"particles by electrostatic repulsion or steric hindrance."),
   c("CE2155 Mat Tut 2 Q5",
     r"A mix needs 300 kg of water. With a water reducer of 15 % reducing ability, how much water is needed?",
     r"**$300 \times (1 - 0.15) = 255\ \mathrm{kg}$.**", "", checked=True),
   c("CE2155 Mat Tut 2 Q6",
     r"With suitable curves, show how accelerating and retarding admixtures affect setting time.",
     r"**Plot penetration resistance against time: an accelerator shifts the curve left (earlier initial set at 3.5 "
     r"MPa and final set at 27.6 MPa), a retarder shifts it right; the plain mix lies between.**"),
   c("CE2155 Mat Tut 2 Q7",
     r"Discuss how temperature affects setting time, and list three good ways to lower the temperature of fresh "
     r"concrete.",
     r"**Higher temperature speeds hydration → shorter setting time and faster slump loss. Cool it with chilled water "
     r"or ice, shaded or chilled aggregate, and casting at night or in the coolest part of the day** (also low-heat "
     r"binders or a retarder)."),
 ),
]}

MATQ[MT.format(3)] = {"code": "CE101", "title": "Materials tutorial 3 · Hardened concrete (lecture 6)", "sections": [
 sec("Tutorial 3 — Hardened concrete", (1, 1),
   c("CE2155 Mat Tut 3 Q1", r"How are strength and porosity related?",
     r"**Strength falls roughly exponentially as porosity rises**; capillary porosity is set by w/c and the degree of "
     r"hydration."),
   c("CE2155 Mat Tut 3 Q2",
     r"What is the dominant factor in concrete strength? Name two other factors.",
     r"**The water–cement ratio.** Others: age and degree of hydration, curing (moisture, temperature), cement type, "
     r"aggregate, air content, test conditions."),
   c("CE2155 Mat Tut 3 Q3",
     r"At a given w/c, would Types I, III and V cement differ in early-age strength? In long-term strength? Explain.",
     r"**Early: III > I > V** ($\mathrm{C_3S}$ content and fineness). **Long term: about the same**, because the "
     r"degree of hydration converges by about 90 days."),
   c("CE2155 Mat Tut 3 Q4", r"What is curing, and why does it matter?",
     r"**Keeping concrete moist and at a suitable temperature after placing so hydration continues** (it stops below "
     r"about 80 % internal RH) — giving strength, low permeability and durability, and less plastic and drying "
     r"shrinkage cracking."),
   c("CE2155 Mat Tut 3 Q5",
     r"Which option gives the higher measured 28-day strength? (a) w/c 0.5 or 0.4; (b) moist curing at 25 °C or "
     r"10 °C; (c) a 150 × 300 or 75 × 150 mm cylinder; (d) loading at 3 or 0.3 MPa/s; (e) testing saturated or "
     r"air-dry.",
     r"**(a) 0.4 · (b) 25 °C · (c) 75 × 150 mm (size effect) · (d) 3 MPa/s · (e) air-dry.**",
     r"(b) 10 °C is slower at 28 days; only a very high early temperature lowers the ultimate strength. (e) Saturated "
     r"specimens read lower — the opposite of the effect on E."),
   c("CE2155 Mat Tut 3 Q6",
     r"What is a truly elastic material? Is concrete truly elastic? Describe the stages of micro-cracking as a "
     r"specimen is loaded to failure.",
     r"**No — concrete is non-linear and inelastic** (ITZ micro-cracks, creep, residual strain on unloading). "
     r"Below about $30\,\%f_c$: stable ITZ cracks · 30–50 %: ITZ cracks grow · above 50 %: matrix cracks start · "
     r"above 75 %: cracks link up and become unstable → failure.",
     r"A truly elastic material returns all strain on unloading along the same path."),
   c("CE2155 Mat Tut 3 Q7",
     r"All else equal, a mortar loses strength and impermeability as coarser aggregate is added. Why?",
     r"**Bigger particles create a thicker, more porous interfacial transition zone, with more bleed water and "
     r"micro-cracking under them — weak, connected paths.**"),
 ),
]}

MATQ[MT.format(4)] = {"code": "CE101", "title": "Materials tutorial 4 · Dimensional stability & durability (lectures 8–9)", "sections": [
 sec("Tutorial 4 — Shrinkage, creep & durability", (1, 1),
   c("CE2155 Mat Tut 4 Q1",
     r"Why is heat of hydration important for dams and foundations but less so for slabs and columns?",
     r"**Mass concrete cannot lose heat (low surface-to-volume), so large internal temperature differences and "
     r"restraint cause thermal cracking; thin slabs and columns lose heat quickly.**"),
   c("CE2155 Mat Tut 4 Q2",
     r"List the main factors affecting drying shrinkage and creep, and say where their effects are similar or "
     r"opposite.",
     r"**Both rise with paste volume (w/c, cement content) and with softer aggregate — similar. Stress level affects "
     r"creep only. Drier air and thinner members increase both drying shrinkage and drying creep.**",
     r"Check lecture 8 p. 15 for the creep trends shown in class."),
   c("CE2155 Mat Tut 4 Q3",
     r"What is durability, and how much weight should it get in design and construction?",
     r"**The ability to resist weathering, chemical attack, abrasion and other deterioration over the design life — "
     r"as important as strength; most repair spending comes from durability failures.**"),
   c("CE2155 Mat Tut 4 Q4",
     r"How does aggregate size affect the permeability of concrete? What else controls permeability?",
     r"**Larger aggregate → more porous ITZ and micro-cracks → higher permeability.** Others: w/c, degree of "
     r"hydration and curing, SCMs, compaction, cracking, air voids."),
   c("CE2155 Mat Tut 4 Q5", r"What measures control corrosion of embedded steel?",
     r"**Adequate cover; low w/c, SCMs and good curing (low permeability); limits on chlorides in the materials; crack "
     r"control; coatings or sealers; epoxy-coated, galvanised or stainless bars; corrosion inhibitors; cathodic "
     r"protection.**"),
   c("CE2155 Mat Tut 4 Q6",
     r"What reactions are involved in sulfate attack, and how do they degrade concrete?",
     r"**Sulfate + CH → gypsum (expansion, softening); sulfate + monosulfate (AFm) / $\mathrm{C_3A}$ hydrates → "
     r"ettringite (expansive) → cracking, spalling and loss of strength.**"),
   c("CE2155 Mat Tut 4 Q7",
     r"Assign each of the photos (a)–(d) to a degradation mechanism.",
     r"**Map cracking with white gel → ASR · scaling and pop-outs in a cold climate → frost · rust staining and "
     r"spalling over bars → corrosion · soft, expanded, spalled surface against soil or seawater → sulfate attack.**",
     r"Match these descriptions to the sheet's four photos.", figure="Tutorial 4 sheet: photos (a)–(d).",
     checked=False),
 ),
]}

MATQ[MT.format(5)] = {"code": "CE101", "title": "Materials tutorial 5 · Steel (lectures 10–11)", "sections": [
 sec("Tutorial 5 — Steel", (1, 1),
   c("CE2155 Mat Tut 5 Q1", r"Give everyday examples of objects made of brittle and of ductile materials.",
     r"**Brittle:** glass, ceramic mugs, chalk, concrete, cast iron. **Ductile:** paper clips, aluminium foil, copper "
     r"wire, mild-steel rebar."),
   c("CE2155 Mat Tut 5 Q2", r"List three cases where concrete is a better construction material than steel.",
     r"**Compression-dominated mass structures (foundations, dams); fire resistance; corrosive or marine exposure "
     r"with good cover** — also mouldability, low cost with local materials, and mass for stability or acoustics."),
   c("CE2155 Mat Tut 5 Q3",
     r"A metal has a total strain of 0.213 at 600 MPa and a permanent strain of 0.210 after unloading. Find its "
     r"elastic modulus.",
     r"**Elastic strain $0.213 - 0.210 = 0.003$ → $E = 600/0.003 = 200\ \mathrm{GPa}$.**", "", checked=True),
   c("CE2155 Mat Tut 5 Q4",
     r"Gold is FCC with a unit-cell edge of 0.408 nm. Find the atomic radius.",
     r"**$r = \sqrt2a/4 = 0.144\ \mathrm{nm}$.**", r"Atoms touch along the face diagonal: $\sqrt2a = 4r$.",
     checked=True),
   c("CE2155 Mat Tut 5 Q5",
     r"A steel just below 723 °C contains 75 % pro-eutectoid cementite ($\mathrm{Fe_3C}$). (a) Is it hypo- or "
     r"hyper-eutectoid? Find the percentage of (b) pearlite, (c) eutectoid ferrite, (d) eutectoid cementite.",
     r"**(a) Hyper-eutectoid (pro-eutectoid cementite). As printed, 75 % would need 5.2 % C — a cast iron, not a "
     r"steel; it was probably meant to be 7.5 %: $C_0 = 1.24\,\%$, (b) pearlite 92.5 %, (c) eutectoid ferrite 81.8 %, "
     r"(d) eutectoid cementite 10.7 %.**",
     r"Lever rule with 0.025 / 0.8 / 6.7 % C. 7.5 %: $C_0 = 0.8 + 0.075 \times 5.9$; eutectoid ferrite $= 0.925 "
     r"\times 5.9/6.675$. As printed (75 %): pearlite 25 %, eutectoid ferrite 22.1 %, eutectoid cementite 2.9 %. Steel "
     r"holds at most about 2 % C, so pro-eutectoid cementite can't exceed about 20 %.", checked=True),
   c("CE2155 Mat Tut 5 Q6",
     r"Why do carbon and other alloying elements raise the ultimate strength of iron?",
     r"**Interstitial and substitutional atoms distort the lattice and pin dislocations (solid-solution "
     r"strengthening); carbon forms hard $\mathrm{Fe_3C}$ / pearlite; alloys refine grains and raise hardenability** "
     r"— at the cost of ductility and weldability."),
 ),
]}
