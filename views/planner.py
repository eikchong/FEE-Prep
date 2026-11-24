from datetime import date, timedelta

import pandas as pd
import plotly.express as px
import streamlit as st

import config
from utils.planner import generate_plan, subject_weights
from utils.state import init, save
from utils.syllabus import all_topics, subject_label, topic_map, topic_state

p = init()
s = p["settings"]
st.title("Study planner")

# ---------------------------------------------------------------- strategy
with st.container(border=True):
    st.subheader("Part 2 strategy")
    st.caption("Pick the 5 question slots you intend to answer, plus backups. "
               "Unchosen Part 2 subjects get zero study weight.")
    slot_opts = [c for c, n in config.PART2_ALLOCATION.items() for _ in range(n)]
    cols = st.columns(5)
    core = []
    for i in range(5):
        default = s["part2_core"][i] if i < len(s["part2_core"]) else slot_opts[0]
        core.append(cols[i].selectbox(f"Slot {i + 1}", list(config.PART2_ALLOCATION), key=f"core{i}",
                                      index=list(config.PART2_ALLOCATION).index(default)))
    over = [c for c in set(core) if core.count(c) > config.PART2_ALLOCATION[c]]
    if over:
        st.error("Only " + ", ".join(f"{config.PART2_ALLOCATION[c]} × {c}" for c in over)
                 + " question(s) appear in the paper — adjust your slots.")
    backup = st.multiselect("Backup subjects", list(config.PART2_ALLOCATION), default=s["part2_backup"],
                            format_func=subject_label)
    c1, c2, c3 = st.columns(3)
    wd = c1.number_input("Weekday hours", 0.0, 12.0, float(s["weekday_hours"]), 0.5)
    we = c2.number_input("Weekend hours", 0.0, 16.0, float(s["weekend_hours"]), 0.5)
    start_default = date.fromisoformat(s["plan_start"]) if s.get("plan_start") else date.today()
    start = c3.date_input("Plan start", value=min(max(start_default, date.today()), config.EXAM_DATE - timedelta(days=1)),
                          max_value=config.EXAM_DATE - timedelta(days=1))
    new = {"part2_core": core, "part2_backup": backup, "weekday_hours": wd, "weekend_hours": we,
           "plan_start": start.isoformat()}
    if any(s.get(k) != v for k, v in new.items()) and not over:
        s.update(new)
        save()

sw = subject_weights(s)
st.caption("Subject weights → " + " · ".join(f"{c} {w:g}" for c, w in sw.items() if w))

# ---------------------------------------------------------------- plan
conf = {t: topic_state(p, t)["confidence"] for t in topic_map()}
names = {t: f"{t} {v['name']}" for t, v in topic_map().items()}
blocks = generate_plan(all_topics(), conf, s, start=start, topic_names=names)
if not blocks:
    st.warning("Nothing to plan — the start date is on or after the exam.")
    st.stop()
df = pd.DataFrame([b.as_dict() for b in blocks])
df["day"] = pd.to_datetime(df["day"])
df["Part"] = df["code"].map(lambda c: "Part 1" if c in config.PART1_CODES else ("Part 2" if c in config.PART2_CODES else "Mock / review"))
total_h = df["minutes"].sum() / 60
st.markdown(f"**{df['day'].nunique()} days** from {start:%d %b} to {df['day'].max():%a %d %b %Y} "
            f"(exam {config.EXAM_DATE:%a %d %b}) · **{total_h:.0f} h** planned · "
            f"last {config.MOCK_DAYS} days = mocks + error-log review")

tab_g, tab_t, tab_s, tab_log = st.tabs(["Timeline", "Day-by-day", "Hours by subject", "Study log"])
with tab_g:
    g = df.groupby(["day", "code", "Part"], as_index=False)["minutes"].sum()
    g["end"] = g["day"] + pd.Timedelta(days=1)
    g["hours"] = (g["minutes"] / 60).round(1)
    fig = px.timeline(g, x_start="day", x_end="end", y="code", color="Part", hover_data={"hours": True, "end": False},
                      color_discrete_map={"Part 1": config.COLOR_P1, "Part 2": config.COLOR_P2,
                                          "Mock / review": "#7a7a7a"})
    fig.update_yaxes(categoryorder="array", categoryarray=sorted(g["code"].unique(), reverse=True))
    fig.add_vline(x=pd.Timestamp(config.EXAM_DATE).timestamp() * 1000, line_dash="dash", line_color="red",
                  annotation_text="Exam")
    fig.update_layout(height=420, margin=dict(l=0, r=0, t=30, b=0), legend_orientation="h")
    st.plotly_chart(fig, use_container_width=True)
with tab_t:
    week = st.select_slider("Week starting", options=sorted({(d - pd.Timedelta(days=d.weekday())).date()
                                                              for d in df["day"]}),
                            format_func=lambda d: d.strftime("%d %b"))
    wk = df[(df["day"].dt.date >= week) & (df["day"].dt.date < week + timedelta(days=7))]
    for day, grp in wk.groupby("day"):
        with st.container(border=True):
            st.markdown(f"**{day:%a %d %b}** · {grp['minutes'].sum() / 60:.1f} h")
            for _, b in grp.iterrows():
                icon = {"MCQ": "🎯", "Study": "📖", "Mock": "⏱️", "Review": "🔁"}[b["kind"]]
                st.markdown(f"{icon} {b['minutes']} min — {b['label']}")
    st.download_button("⬇️ Download full plan (CSV)", df.assign(day=df["day"].dt.date).to_csv(index=False),
                       "fee2027_plan.csv", "text/csv")
with tab_s:
    h = df[df["kind"].isin(["Study", "MCQ"])].groupby(["code", "Part"], as_index=False)["minutes"].sum()
    h["hours"] = h["minutes"] / 60
    fig = px.bar(h, x="code", y="hours", color="Part",
                 color_discrete_map={"Part 1": config.COLOR_P1, "Part 2": config.COLOR_P2})
    fig.update_layout(height=340, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)
with tab_log:
    log = pd.DataFrame(p["study_log"])
    if log.empty:
        st.info("No study time logged yet — use **Log study time** in the sidebar.")
    else:
        log["date"] = pd.to_datetime(log["date"])
        daily = log.groupby(["date", "code"], as_index=False)["minutes"].sum()
        fig = px.bar(daily, x="date", y="minutes", color="code")
        fig.update_layout(height=320, margin=dict(l=0, r=0, t=10, b=0))
        st.plotly_chart(fig, use_container_width=True)
        st.caption(f"Logged {log['minutes'].sum() / 60:.1f} h in total.")
