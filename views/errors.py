import pandas as pd
import plotly.express as px
import streamlit as st

import config
from utils.state import init, new_id, now_iso, save
from utils.syllabus import subject_label, subject_map
from utils.ui import open_in_library

p = init()
st.title("Error log & analytics")

tab_log, tab_an = st.tabs(["Error log", "Analytics"])

with tab_log:
    with st.expander("➕ Add mistake", expanded=not p["errors"]):
        with st.form("add_err", clear_on_submit=True):
            c1, c2 = st.columns(2)
            code = c1.selectbox("Subject", list(subject_map()), format_func=subject_label)
            source = c2.text_input("Source", placeholder="e.g. Mock 1 Q12, textbook ex 5.3")
            what = st.text_area("What went wrong")
            fix = st.text_area("Fix / rule to remember")
            s1, s2 = st.columns([3, 1])
            sdoc = s1.text_input("Source page that fixes it (materials/ path, optional)")
            spage = s2.number_input("Page", 1, 5000, 1)
            if st.form_submit_button("Add", type="primary") and what.strip():
                p["errors"].append({"id": new_id(), "ts": now_iso(), "code": code, "source": source, "what": what,
                                    "fix": fix, "resolved": False, "source_doc": sdoc or None,
                                    "source_page": int(spage) if sdoc else None})
                save()
                st.toast("Added")

    if not p["errors"]:
        st.caption("No mistakes logged yet. Wrong MCQs and low-scoring Part 2 attempts can be sent here.")
    else:
        df = pd.DataFrame(p["errors"])
        for col in ("source_doc", "source_page"):
            if col not in df:
                df[col] = None
        show_resolved = st.toggle("Show resolved", value=False)
        view = df if show_resolved else df[~df["resolved"].astype(bool)]
        edited = st.data_editor(
            view[["id", "ts", "code", "source", "what", "fix", "resolved", "source_doc", "source_page"]],
            hide_index=True, use_container_width=True, key="err_ed", disabled=["id", "ts"],
            column_config={"id": None, "ts": st.column_config.TextColumn("logged", width="small"),
                           "code": st.column_config.SelectboxColumn(options=list(subject_map()), width="small"),
                           "what": st.column_config.TextColumn(width="large"),
                           "fix": st.column_config.TextColumn(width="large"),
                           "resolved": st.column_config.CheckboxColumn(),
                           "source_page": st.column_config.NumberColumn(format="%d")})
        changed = False
        byid = {e["id"]: e for e in p["errors"]}
        for _, r in edited.iterrows():
            e = byid.get(r["id"])
            if not e:
                continue
            for k in ("code", "source", "what", "fix", "resolved", "source_doc", "source_page"):
                v = r[k]
                v = None if (not isinstance(v, (str, bool)) and pd.isna(v)) else v
                if k == "resolved":
                    v = bool(v)
                if k == "source_page" and v is not None:
                    v = int(v)
                if e.get(k) != v:
                    e[k] = v
                    changed = True
        if changed:
            save()
            st.toast("Saved")
        linked = [e for e in p["errors"] if e.get("source_doc") and (show_resolved or not e["resolved"])]
        if linked:
            c1, c2 = st.columns([3, 1])
            pick = c1.selectbox("Open source page for", [e["id"] for e in linked],
                                format_func=lambda i: f"{byid[i]['code']} — {byid[i]['what'][:60]} "
                                                      f"({byid[i]['source_doc']}, p. {byid[i]['source_page'] or 1})")
            if c2.button("📖 Open in Library", use_container_width=True):
                e = byid[pick]
                open_in_library(e["source_doc"], int(e["source_page"] or 1))
        st.caption(f"{int((~df['resolved'].astype(bool)).sum())} open · {int(df['resolved'].astype(bool).sum())} resolved")

with tab_an:
    a, b = st.columns(2)
    with a:
        st.subheader("MCQ accuracy by subject")
        att = pd.DataFrame(p["mcq_attempts"])
        if att.empty:
            st.caption("No MCQ attempts yet.")
        else:
            g = att.groupby("code")["correct"].agg(["mean", "count"]).reset_index()
            fig = px.bar(g, x="code", y="mean", text=g["count"].map(lambda n: f"n={n}"),
                         color_discrete_sequence=[config.COLOR_P1])
            fig.update_layout(height=320, yaxis_tickformat=".0%", yaxis_range=[0, 1.05], yaxis_title="accuracy",
                              margin=dict(t=10, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
    with b:
        st.subheader("Part 2 score trend")
        pa = pd.DataFrame(p["part2_attempts"])
        if pa.empty:
            st.caption("No Part 2 attempts yet.")
        else:
            pa["ts"] = pd.to_datetime(pa["ts"])
            fig = px.line(pa.sort_values("ts"), x="ts", y="score_pct", color="code", markers=True)
            fig.add_hline(y=50, line_dash="dot", annotation_text="50%")
            fig.update_layout(height=320, yaxis_range=[0, 100], margin=dict(t=10, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
    st.subheader("Minutes studied per week")
    log = pd.DataFrame(p["study_log"])
    if log.empty:
        st.caption("No study time logged yet.")
    else:
        log["date"] = pd.to_datetime(log["date"])
        log["week"] = log["date"].dt.to_period("W-SUN").dt.start_time
        wk = log.groupby(["week", "code"], as_index=False)["minutes"].sum()
        fig = px.bar(wk, x="week", y="minutes", color="code")
        fig.update_layout(height=320, margin=dict(t=10, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
