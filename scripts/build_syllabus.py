"""Regenerate data/syllabus.json from the lists below (ids are stable: order matters!).

Only ever APPEND new sub-topics to the end of a subject list, otherwise ids shift and
saved progress / tags will point at the wrong sub-topic.
"""
import json
from pathlib import Path

S = [
 ("CE101", "Mechanics of Materials", 1, [
   ("Mechanics of materials", ["Strength, stiffness & deformability", "Stress–strain behaviour",
     "Ductility & brittle fracture", "Creep, creep rupture & relaxation", "Cyclic loading & fatigue"]),
   ("Concrete technology", ["Concrete materials (cement, aggregates, admixtures)", "Fresh & hardened concrete properties",
     "Mixing, placing & curing", "Mix design", "Destructive & non-destructive testing",
     "Quality control", "Durability of concrete", "Special concretes"]),
   ("Steel", ["Basic metallurgy of steel", "Mechanical properties & applications of steel", "Welding", "Corrosion of steel"]),
 ]),
 ("CE102", "Structural Mechanics", 1, [("", [
   "Statics & kinetics of particles", "Rigid-body equilibrium", "Kinematics & plane motion of rigid bodies",
   "Simple trusses & beams", "Compound & complex trusses", "Tension & compression members", "Torsion",
   "Bending", "BM, SF & axial force in beams & frames"])]),
 ("CE103", "Structural Analysis", 1, [("", [
   "Virtual work & energy theorems", "Analysis of indeterminate structures", "Influence lines",
   "Slope-deflection method", "Moment distribution", "Plastic analysis",
   "Equilibrium, compatibility & force–displacement", "Direct stiffness method (trusses, beams, frames)",
   "Elastic stability of frames"])]),
 ("CE104", "Soil Mechanics", 1, [("", [
   "Basic geology", "Unified Soil Classification System (USCS)", "Mechanical properties & phase relations",
   "Effective stress", "Shear strength & Mohr–Coulomb (drained/undrained)", "Compressibility",
   "Seepage", "Consolidation & Terzaghi rate theory", "Settlement"])]),
 ("CE105", "Fluid Mechanics", 1, [("", [
   "Fluid properties", "Hydrostatic pressure & thrust", "Buoyancy & floating stability", "Continuity",
   "Bernoulli equation", "Linear momentum", "Dimensional analysis", "Hydraulic models & similitude"])]),
 ("CE201", "Reinforced & Prestressed Concrete Design", 2, [
   ("Reinforced concrete", ["Members & loads", "Bending", "Shear", "Torsion", "Bond & anchorage", "Corbels",
     "Serviceability (deflection & cracking)", "Durability & cover", "Short columns", "Slender columns",
     "Slab systems", "Punching shear", "Foundations", "Retaining walls", "Detailing"]),
   ("Prestressed concrete", ["PSC concepts, materials & systems", "Prestress losses & time-dependent deformation",
     "PSC flexure", "PSC shear", "PSC combined axial + bending"]),
 ]),
 ("CE202", "Structural Steel Design", 2, [("", [
   "Limit state design & material response", "Local buckling & cross-section classification",
   "Laterally restrained beams", "Shear buckling & plate girders", "Web bearing, buckling & stiffeners",
   "Lateral-torsional buckling", "Tension members", "Compression members", "Members with end moments (combined)",
   "Connections (bolted & welded)", "Plastic design of portal frames", "Continuous multi-storey frames"])]),
 ("CE203", "Geotechnical Engineering", 2, [("", [
   "Slopes & embankments", "Active & passive earth pressure", "Retaining structures", "Deep excavations",
   "Site investigation & soil report interpretation", "Shallow foundations", "Piles", "Foundation selection",
   "Settlement of foundations"])]),
 ("CE204", "Transportation Engineering", 2, [("", [
   "Transport systems, planning & management", "Geometric design of roads & intersections",
   "Flexible pavement design", "Rigid pavement design", "Traffic flow studies", "Traffic management",
   "Highway & intersection capacity", "Traffic signal control", "Parking"])]),
 ("CE205", "Hydraulics & Hydrology", 2, [("", [
   "Pipe friction & minor losses", "Pipe–pump systems", "Pipe networks", "Manning & uniform flow",
   "Critical flow", "Energy, momentum & hydraulic jumps", "Gradually varied flow & backwater",
   "Hydrologic cycle & rainfall", "Evaporation & infiltration", "Runoff", "Streamflow measurement",
   "Hydrographs & unit hydrographs", "Frequency analysis", "Flood routing", "Urban drainage & flood peaks"])]),
 ("CE206", "Environmental Engineering", 2, [("", [
   "Water quality parameters", "Water treatment design", "Water distribution systems",
   "Wastewater collection & pumping", "Pretreatment & primary treatment",
   "Secondary treatment (activated sludge)", "Tertiary treatment", "Anaerobic digestion"])]),
]

THEMES = {
 "CE201": ["Precast beam M_Rd incl. construction stage", "Short column: N then N + M"],
 "CE202": ["Platform beam SFD/BMD + LTB (S355) + remedies"],
 "CE203": ["Strip footing EC7 DA1 + CPT/Schmertmann settlement"],
 "CE204": ["Shockwave + sight/stopping distance"],
 "CE205": ["Trapezoidal Manning, critical depth, slope classification"],
 "CE206": ["Primary clarifier, activated sludge volume, F/M, SRT"],
}

def build():
    subjects = []
    for code, name, part, groups in S:
        topics, n = [], 0
        for group, names in groups:
            for t in names:
                n += 1
                topics.append({"id": f"{code}-{n:02d}", "name": t, "group": group})
        subjects.append({"code": code, "name": name, "part": part,
                         "themes": THEMES.get(code, []), "topics": topics})
    out = Path(__file__).resolve().parents[1] / "data" / "syllabus.json"
    out.write_text(json.dumps({"subjects": subjects}, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out} ({sum(len(s['topics']) for s in subjects)} sub-topics)")

if __name__ == "__main__":
    build()
