import pandas as pd
import streamlit as st

import config
from utils.state import days_to_exam, init
from utils.storage import load_static
from utils.syllabus import subject_label, subjects

init()
st.title("Exam info & reading list")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Format")
    fmt = pd.DataFrame([
        {"": "Session", "Part 1 — Breadth": f"{config.PART1['start']:%H:%M}–{config.PART1['end']:%H:%M}",
         "Part 2 — Depth": f"{config.PART2['start']:%H:%M}–{config.PART2['end']:%H:%M}"},
        {"": "Duration", "Part 1 — Breadth": config.PART1["duration"], "Part 2 — Depth": config.PART2["duration"]},
        {"": "Questions", "Part 1 — Breadth": config.PART1["fmt"], "Part 2 — Depth": config.PART2["fmt"]},
        {"": "Pace", "Part 1 — Breadth": f"≈ {config.PART1['pace_min']} min / question",
         "Part 2 — Depth": f"≈ {config.PART2['pace_min']} min / question"},
        {"": "Subjects", "Part 1 — Breadth": ", ".join(config.PART1_CODES),
         "Part 2 — Depth": ", ".join(f"{c}×{n}" for c, n in config.PART2_ALLOCATION.items())},
    ])
    st.dataframe(fmt, hide_index=True, use_container_width=True)
with c2:
    st.subheader("Key dates")
    st.markdown(f"- **Exam:** Wednesday {config.EXAM_DATE:%d %B %Y} ({days_to_exam()} days)\n"
                f"- **Results:** {config.RESULTS}")
    st.subheader("Rules")
    st.markdown(f"- {config.CODES_RULE}\n- {config.OPEN_BOOK}\n"
                "- Legacy BS 8110 / BS 5950 methods are **not** acceptable.")
    st.markdown(f"[📄 FEE 2027 brochure]({config.BROCHURE_URL}) · [🏛️ PEB website]({config.PEB_URL})")

st.subheader("Syllabus at a glance")
for part in (1, 2):
    st.markdown(f"**Part {part}**")
    st.markdown("\n".join(f"- **{s['code']} {s['name']}** — {len(s['topics'])} sub-topics"
                          + (f" · themes: {'; '.join(s['themes'])}" if s["themes"] else "") for s in subjects(part)))

st.subheader("Reading list")
rl = pd.DataFrame(load_static("reading_list.json"))
code = st.selectbox("Filter", [None] + [s["code"] for s in subjects()],
                    format_func=lambda c: "All subjects" if c is None else subject_label(c))
if code:
    rl = rl[rl["codes"].map(lambda cs: code in cs)]
rl["codes"] = rl["codes"].map(", ".join)
st.dataframe(rl.rename(columns={"codes": "Subject", "title": "Title", "authors": "Authors", "edition": "Ed."}),
             hide_index=True, use_container_width=True)
