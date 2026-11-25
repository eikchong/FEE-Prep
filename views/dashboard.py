from datetime import date, timedelta

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import config
from utils import library
from utils.latex_plain import to_plain
from utils.reading import overall_stats
from utils.state import days_to_exam, init, log_study_time_form
from utils.syllabus import (chosen_part2, focus_codes, mcq_accuracy, readiness_by_subject, subject_map, subjects,
                            topic_map, topic_mcq_accuracy)
from utils.ui import metric, part_color, pill

p = init()
settings = p["settings"]

st.title("Dashboard")
st.caption(f"Wed {config.EXAM_DATE:%d %B %Y} · results {config.RESULTS}")

# ---------------------------------------------------------------- metrics
ov = overall_stats(p)
att = p["mcq_attempts"]
acc = (sum(a["correct"] for a in att) / len(att)) if att else None
week_ago = (date.today() - timedelta(days=6)).isoformat()
hrs7 = sum(l["minutes"] for l in p["study_log"] if l["date"] >= week_ago) / 60
counts = library.safe_counts()
focus_ids = [t["id"] for c in focus_codes(settings) for t in subject_map()[c]["topics"]]

c = st.columns(6)
c[0].metric("Days to exam", days_to_exam())
metric(c[1], "Notes read", f"{ov['pct']:.0%}", f"{ov['n_topics_read']}/{ov['n_topics_with_notes']} topics")
metric(c[2], "Readiness", f"{sum(readiness_by_subject(p)[x] for x in focus_codes(settings)) / len(focus_codes(settings)):.0%}",
       "read % + MCQ accuracy")
metric(c[3], "MCQ accuracy", f"{acc:.0%}" if acc is not None else "—", f"{len(att)} attempts")
c[4].metric("Study hrs (7 d)", f"{hrs7:.1f}")
metric(c[5], "Revisit flags", len(p.get("revisit", {})), "topics flagged")

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
    accs = mcq_accuracy(p)
    codes = [s["code"] for s in subjects()][::-1]
    fig = go.Figure(go.Bar(
        x=[rb[c] for c in codes], y=codes, orientation="h",
        marker_color=[part_color(c) for c in codes],
        text=[f"{rb[c]:.0%}" for c in codes], textposition="outside",
        hovertext=[f"{subject_map()[c]['name']} · read {ov['subjects'][c]['pct']:.0%}"
                   + (f" · MCQ {accs[c]:.0%}" if accs[c] is not None else "") for c in codes]))
    fig.update_layout(height=380, margin=dict(l=0, r=30, t=10, b=0),
                      xaxis=dict(range=[0, 1.1], tickformat=".0%", title="read % of notes, averaged with MCQ accuracy"),
                      plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, width="stretch")
    st.caption(f"<span style='color:{config.COLOR_P1}'>■</span> Part 1 &nbsp; "
               f"<span style='color:{config.COLOR_P2}'>■</span> Part 2", unsafe_allow_html=True)

with right:
    st.subheader("Focus next")
    tacc = topic_mcq_accuracy(p)
    plan_codes = set(focus_codes(settings))
    rows = []
    for tid, d in p.get("revisit", {}).items():
        if tid in topic_map():
            rows.append((0, tid, f"Flagged to revisit ({d})"))
    for tid, a in sorted(tacc.items(), key=lambda x: x[1]):
        if a < 0.6 and tid in topic_map() and tid not in p.get("revisit", {}):
            rows.append((1, tid, f"MCQ accuracy {a:.0%}"))
    seen = {r[1] for r in rows}
    for tid in focus_ids:
        if tid in seen or topic_map()[tid]["code"] not in plan_codes:
            continue
        ts = ov["subjects"][topic_map()[tid]["code"]]["topics"][tid]
        if ts["words"] and ts["status"] != "read":
            rows.append((2, tid, "Unread" if ts["status"] == "not_started" else f"{ts['pct']:.0%} read"))
    df = pd.DataFrame([{"Topic": f"{tid} {to_plain(topic_map()[tid]['name'])}", "Why": why} for _, tid, why in rows[:10]])
    if df.empty:
        st.success("Nothing flagged — keep reading.")
    else:
        st.dataframe(df, hide_index=True, width="stretch")
    st.caption("Revisit flags first, then topics with MCQ accuracy below 60 %, then unread topics in your plan "
               "subjects (" + ", ".join(chosen_part2(settings)) + " and Part 1).")

log_study_time_form()
st.info(f"**Codes rule:** {config.CODES_RULE}  \n**{config.OPEN_BOOK}**", icon="📘")
