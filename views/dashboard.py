from datetime import date, timedelta

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import config
from utils import library
from utils.state import days_to_exam, init
from utils.syllabus import (chosen_part2, focus_codes, readiness_by_subject, subject_map, subjects,
                            topic_map, topic_state)
from utils.ui import metric, part_color, pill

p = init()
settings = p["settings"]

st.title("FEE 2027 (Civil) — Dashboard")
st.caption(f"Wed {config.EXAM_DATE:%d %B %Y} · results {config.RESULTS}")

# ---------------------------------------------------------------- metrics
all_ids = list(topic_map())
states = {t: topic_state(p, t) for t in all_ids}
started = sum(s["status"] != "Not started" for s in states.values())
ready = sum(s["status"] == "Exam-ready" for s in states.values())
att = p["mcq_attempts"]
acc = (sum(a["correct"] for a in att) / len(att)) if att else None
week_ago = (date.today() - timedelta(days=6)).isoformat()
hrs7 = sum(l["minutes"] for l in p["study_log"] if l["date"] >= week_ago) / 60
counts = library.safe_counts()
focus_ids = [t["id"] for c in focus_codes(settings) for t in subject_map()[c]["topics"]]
gaps = [t for t in focus_ids if counts.get(t, 0) == 0]

c = st.columns(6)
c[0].metric("Days to exam", days_to_exam())
metric(c[1], "Topics started", f"{started / len(all_ids):.0%}", f"{started}/{len(all_ids)}")
c[2].metric("Exam-ready", ready)
metric(c[3], "MCQ accuracy", f"{acc:.0%}" if acc is not None else "—", f"{len(att)} attempts")
c[4].metric("Study hrs (7 d)", f"{hrs7:.1f}")
metric(c[5], "Material gaps", len(gaps), "focus sub-topics with no notes",
            help="Sub-topics (Part 1 + your chosen Part 2 subjects) with no linked pages in the Library")

# ---------------------------------------------------------------- format cards
a, b = st.columns(2)
with a.container(border=True):
    st.markdown(f"#### <span style='color:{config.COLOR_P1}'>●</span> {config.PART1['name']}", unsafe_allow_html=True)
    st.markdown(f"**{config.PART1['start']:%H:%M}–{config.PART1['end']:%H:%M}** · {config.PART1['duration']}  \n"
                f"{config.PART1['questions']} MCQ, answer all · **≈ {config.PART1['pace_min']} min / question**")
    st.markdown(" ".join(pill(f"{s['code']} {s['name']}", config.COLOR_P1) for s in subjects(1)),
                unsafe_allow_html=True)
with b.container(border=True):
    st.markdown(f"#### <span style='color:{config.COLOR_P2}'>●</span> {config.PART2['name']}", unsafe_allow_html=True)
    st.markdown(f"**{config.PART2['start']:%H:%M}–{config.PART2['end']:%H:%M}** · {config.PART2['duration']}  \n"
                f"Answer 5 of 9 · **≈ {config.PART2['pace_min']} min / question**")
    core = settings["part2_core"]
    alloc = pd.DataFrame([{"Subject": f"{c} {subject_map()[c]['name']}", "Questions": n,
                           "My core slots": core.count(c),
                           "Backup": "✓" if c in settings["part2_backup"] else ""}
                          for c, n in config.PART2_ALLOCATION.items()])
    st.dataframe(alloc, hide_index=True, width="stretch")

# ---------------------------------------------------------------- readiness + focus
left, right = st.columns([1, 1])
with left:
    st.subheader("Readiness by subject")
    rb = readiness_by_subject(p)
    codes = [s["code"] for s in subjects()][::-1]
    fig = go.Figure(go.Bar(
        x=[rb[c] for c in codes], y=[f"{c}" for c in codes], orientation="h",
        marker_color=[part_color(c) for c in codes],
        text=[f"{rb[c]:.0%}" for c in codes], textposition="outside",
        hovertext=[subject_map()[c]["name"] for c in codes]))
    fig.update_layout(height=380, margin=dict(l=0, r=30, t=10, b=0),
                      xaxis=dict(range=[0, 1.1], tickformat=".0%", title="avg confidence ÷ 5"),
                      plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, width="stretch")
    st.caption(f"<span style='color:{config.COLOR_P1}'>■</span> Part 1 &nbsp; "
               f"<span style='color:{config.COLOR_P2}'>■</span> Part 2", unsafe_allow_html=True)

with right:
    st.subheader("Focus next")
    rows = []
    for tid in focus_ids:
        t, s = topic_map()[tid], states[tid]
        rows.append({"Sub-topic": f"{tid} {t['name']}", "Status": s["status"], "Conf.": s["confidence"],
                     "Notes": "✓" if counts.get(tid) else "—"})
    df = pd.DataFrame(rows).sort_values(["Conf.", "Sub-topic"]).head(8)
    st.dataframe(df, hide_index=True, width="stretch",
                 column_config={"Conf.": st.column_config.ProgressColumn(min_value=0, max_value=5, format="%d")})
    st.caption("Lowest-confidence sub-topics across Part 1 and your chosen Part 2 subjects ("
               + ", ".join(chosen_part2(settings)) + ").")
    if gaps:
        with st.expander(f"📭 Material gaps — {len(gaps)} focus sub-topics without linked notes"):
            st.write(", ".join(f"`{g}`" for g in gaps[:60]) + (" …" if len(gaps) > 60 else ""))
            if st.button("📚 Open Library"):
                st.switch_page("views/library.py")

st.info(f"**Codes rule:** {config.CODES_RULE}  \n**{config.OPEN_BOOK}**", icon="📘")
