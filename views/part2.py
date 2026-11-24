import time

import pandas as pd
import streamlit as st

import config
from utils.state import init, new_id, now_iso, part2_bank, save
from utils.syllabus import subject_label, topic_label
from utils.ui import countdown, fmt_mmss, open_in_library, rubric_form

p = init()
st.title("Part 2 workbook")
bank = part2_bank()
SECS = int(config.PART2["pace_min"] * 60)


codes = st.multiselect("Subjects", config.PART2_CODES, default=sorted(set(p["settings"]["part2_core"])),
                       format_func=subject_label)
qs = [q for q in bank if q["code"] in codes] or bank
attempts = pd.DataFrame(p["part2_attempts"])
done_ids = set(attempts["qid"]) if not attempts.empty else set()

qid = st.selectbox("Question", [q["id"] for q in qs],
                   format_func=lambda i: next(f"{'✓ ' if q['id'] in done_ids else ''}{q['id']} — {q['title']}"
                                              for q in qs if q["id"] == i))
q = next(x for x in qs if x["id"] == qid)
ws = st.session_state.setdefault("p2", {})
state = ws.get(qid, {"phase": "ready"})

with st.container(border=True):
    st.caption(f"{subject_label(q['code'])} · " + " · ".join(topic_label(t) for t in q.get("topics", [])))
    st.subheader(q["title"])
    if state["phase"] == "ready":
        st.info(f"Read the question and start the {config.PART2['pace_min']}-min timer when ready.")
        st.markdown(q["prompt"])
        if st.button("▶ Start 36-min attempt", type="primary"):
            ws[qid] = {"phase": "running"}
            st.session_state[f"p2start_{qid}"] = time.time()
            st.rerun()
    elif state["phase"] == "running":
        countdown(f"p2start_{qid}", SECS)
        st.markdown(q["prompt"])
        st.caption("Work on paper. Cite clauses, keep units, sketch where useful.")
        if st.button("⏹ Finish & self-mark", type="primary"):
            el = time.time() - st.session_state[f"p2start_{qid}"]
            ws[qid] = {"phase": "mark", "elapsed": el}
            st.session_state[f"p2start_{qid}"] = None
            st.rerun()
    else:
        el = state["elapsed"]
        (st.success if el <= SECS else st.warning)(f"Time taken {fmt_mmss(el)} (target {fmt_mmss(SECS)})")
        with st.expander("Question", expanded=False):
            st.markdown(q["prompt"])
        st.markdown("#### Approach outline")
        for step in q["approach"]:
            st.markdown(f"- {step}")
        if q.get("key_results"):
            st.caption("Key results: " + " · ".join(f"{k} = {v}" for k, v in q["key_results"].items()))
        src = q.get("source") or {}
        if src.get("doc") and st.button(f"📖 Review source ({src['doc']}, p. {src.get('page', 1)})"):
            open_in_library(src["doc"], int(src.get("page", 1)))
        if state["phase"] == "mark":
            scores, pct = rubric_form(f"r_{qid}")
            notes = st.text_area("Notes — what to fix next time")
            c1, c2 = st.columns(2)
            c1.metric("Score", f"{pct:.0f}%")
            if c2.button("💾 Save attempt", type="primary"):
                p["part2_attempts"].append({"ts": now_iso(), "qid": qid, "code": q["code"], "scores": scores,
                                            "score_pct": round(pct, 1), "seconds": round(el), "notes": notes,
                                            "mock": False})
                if pct < 60 and notes.strip():
                    p["errors"].append({"id": new_id(), "ts": now_iso(), "code": q["code"],
                                        "source": f"Part 2 {qid}", "what": notes.strip(), "fix": "",
                                        "resolved": False, "source_doc": src.get("doc"),
                                        "source_page": src.get("page")})
                save()
                ws[qid] = {"phase": "saved", "elapsed": el}
                st.rerun()
        else:
            st.success("Attempt saved. (Scores under 60% with notes are also added to the error log.)")
            if st.button("↺ Attempt again"):
                ws[qid] = {"phase": "ready"}
                st.rerun()

st.subheader("History")
if attempts.empty:
    st.caption("No attempts yet.")
else:
    a = attempts.copy()
    a["time"] = a["seconds"].map(fmt_mmss)
    st.dataframe(a[["ts", "qid", "code", "score_pct", "time", "mock", "notes"]].iloc[::-1], hide_index=True,
                 width="stretch",
                 column_config={"score_pct": st.column_config.ProgressColumn("score", min_value=0, max_value=100,
                                                                              format="%.0f%%")})
