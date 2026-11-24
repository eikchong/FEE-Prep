import pandas as pd
import streamlit as st

import config
from utils import library
from utils.state import init, save
from utils.syllabus import subjects, topic_state
from utils.ui import open_in_library

p = init()
st.title("Syllabus tracker")
st.caption("Edits save automatically. Confidence 0 = never seen · 5 = could teach it under exam time.")

f1, f2 = st.columns([2, 1])
query = f1.text_input("Search sub-topics", placeholder="e.g. buckling, Manning, consolidation").strip().lower()
status_filter = f2.multiselect("Status", config.STATUSES, placeholder="All statuses")
counts = library.safe_counts()


def subject_editor(s: dict):
    rows = []
    for t in s["topics"]:
        stt = topic_state(p, t["id"])
        rows.append({"id": t["id"], "Sub-topic": t["name"], "Group": t["group"], "Status": stt["status"],
                     "Confidence": stt["confidence"], "Notes": stt["notes"], "Materials": counts.get(t["id"], 0)})
    df = pd.DataFrame(rows)
    n_ready = int((df["Status"] == "Exam-ready").sum())
    view = df
    if query:
        view = view[view["Sub-topic"].str.lower().str.contains(query, regex=False)
                    | view["Notes"].str.lower().str.contains(query, regex=False)]
    if status_filter:
        view = view[view["Status"].isin(status_filter)]
    if (query or status_filter) and view.empty:
        return
    avg = df["Confidence"].mean() / 5
    header = f"**{s['code']} {s['name']}** — {n_ready}/{len(df)} exam-ready · readiness {avg:.0%}"
    with st.expander(header, expanded=bool(query or status_filter)):
        if s["themes"]:
            st.caption("Past-paper themes: " + " · ".join(s["themes"]))
        cols = ["id", "Sub-topic", "Status", "Confidence", "Notes", "Materials"]
        if df["Group"].nunique() > 1:
            cols.insert(2, "Group")
        edited = st.data_editor(
            view[cols], key=f"ed_{s['code']}", hide_index=True, use_container_width=True,
            disabled=["id", "Sub-topic", "Group", "Materials"],
            column_config={
                "id": st.column_config.TextColumn(width="small"),
                "Sub-topic": st.column_config.TextColumn(width="large"),
                "Status": st.column_config.SelectboxColumn(options=config.STATUSES, required=True),
                "Confidence": st.column_config.NumberColumn(min_value=0, max_value=5, step=1, format="%d ⭐"),
                "Notes": st.column_config.TextColumn(width="large"),
                "Materials": st.column_config.NumberColumn(help="Linked pages in the Library", format="%d 📄"),
            })
        changed = False
        for _, r in edited.iterrows():
            cur = topic_state(p, r["id"])
            new = {"status": r["Status"] or config.STATUSES[0],
                   "confidence": int(r["Confidence"] if pd.notna(r["Confidence"]) else 0),
                   "notes": r["Notes"] if isinstance(r["Notes"], str) else ""}
            if new != cur:
                p["topics"][r["id"]] = new
                changed = True
        if changed:
            save()
            st.toast(f"Saved {s['code']}")
        c1, c2 = st.columns([3, 1])
        pick = c1.selectbox("Materials for", view["id"].tolist(), key=f"mat_{s['code']}",
                            format_func=lambda i: f"{i} · {df.set_index('id').at[i, 'Sub-topic']} "
                                                  f"({df.set_index('id').at[i, 'Materials']} pages)",
                            label_visibility="collapsed")
        if c2.button("📚 Open in Library", key=f"open_{s['code']}", use_container_width=True):
            open_in_library(topic=pick)


t1, t2 = st.tabs(["Part 1 — Breadth", "Part 2 — Depth"])
with t1:
    for s in subjects(1):
        subject_editor(s)
with t2:
    st.caption("Your chosen Part 2 subjects are set in the Study planner. All are listed here.")
    for s in subjects(2):
        subject_editor(s)
