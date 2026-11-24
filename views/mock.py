import random
import time

import pandas as pd
import plotly.express as px
import streamlit as st

import config
from utils.state import all_mcqs, init, now_iso, part2_bank, save
from utils.syllabus import subject_label
from utils.ui import metric, countdown, fmt_mmss

p = init()
st.title("Mock exam")
LETTERS = "ABCD"
SECS = config.PART1["minutes"] * 60

t1, t2, t3 = st.tabs(["Part 1 — 40 MCQ", "Part 2 — 5 of 9", "History"])

# ---------------------------------------------------------------- Part 1
with t1:
    m = st.session_state.get("mock1")
    pool = [q for q in all_mcqs() if q["code"] in config.PART1_CODES]
    if not m:
        n = min(config.PART1["questions"], len(pool))
        st.markdown(f"Random **{n}** questions · **{config.PART1['minutes']} min** countdown "
                    f"(+10 min reading in the real exam).")
        if len(pool) < config.PART1["questions"]:
            st.warning(f"Bank has only {len(pool)} Part 1 questions — add more (MCQ drill → Add my own question) "
                       "for a full 40-question mock.")
        if st.button("▶ Start Part 1 mock", type="primary", disabled=not pool):
            st.session_state["mock1"] = {"qids": [q["id"] for q in random.sample(pool, n)], "result": None}
            st.session_state["mock1_start"] = time.time()
            st.rerun()
    else:
        qmap = {q["id"]: q for q in pool}
        qs = [qmap[i] for i in m["qids"] if i in qmap]
        if m["result"] is None:
            countdown("mock1_start", SECS)
            with st.form("mock1_form"):
                for k, q in enumerate(qs, 1):
                    st.markdown(f"**Q{k}.** {q['q']}")
                    st.radio(f"Q{k}", range(4), format_func=lambda i, q=q: f"{LETTERS[i]}. {q['options'][i]}",
                             index=None, key=f"m1_{q['id']}", label_visibility="collapsed")
                    st.divider()
                sub = st.form_submit_button("Submit paper", type="primary")
            if st.button("Abandon mock"):
                st.session_state["mock1"] = None
                st.rerun()
            if sub:
                el = time.time() - st.session_state["mock1_start"]
                rows = []
                for q in qs:
                    ch = st.session_state.get(f"m1_{q['id']}")
                    ok = ch == q["answer"]
                    rows.append({"qid": q["id"], "code": q["code"], "chosen": ch, "correct": ok})
                    p["mcq_attempts"].append({"ts": now_iso(), "qid": q["id"], "code": q["code"], "chosen": ch,
                                              "correct": ok, "mode": "mock", "seconds": round(el / len(qs), 1)})
                df = pd.DataFrame(rows)
                by = df.groupby("code")["correct"].mean().round(3).to_dict()
                pct = df["correct"].mean() * 100
                p["mock_results"].append({"ts": now_iso(), "part": 1, "score_pct": round(pct, 1),
                                          "by_subject": by, "seconds": round(el), "n": len(qs)})
                save()
                m["result"] = {"rows": rows, "elapsed": el, "pct": pct}
                st.session_state["mock1_start"] = None
                st.rerun()
        else:
            r = m["result"]
            df = pd.DataFrame(r["rows"])
            c = st.columns(3)
            metric(c[0], "Score", f"{df['correct'].sum()}/{len(df)}", f"{r['pct']:.0f}%")
            metric(c[1], "Time", fmt_mmss(r["elapsed"]), "over" if r["elapsed"] > SECS else "within limit")
            c[2].metric("Unanswered", int(df["chosen"].isna().sum()))
            by = df.groupby("code")["correct"].agg(["sum", "count"]).reset_index()
            by["accuracy"] = by["sum"] / by["count"]
            fig = px.bar(by, x="code", y="accuracy", text=by.apply(lambda r: f"{r['sum']}/{r['count']}", axis=1),
                         color_discrete_sequence=[config.COLOR_P1])
            fig.update_layout(height=300, yaxis_tickformat=".0%", yaxis_range=[0, 1.05], margin=dict(t=10, b=0, l=0, r=0))
            st.plotly_chart(fig, width="stretch")
            for k, (q, x) in enumerate(zip(qs, r["rows"]), 1):
                if not x["correct"]:
                    with st.expander(f"❌ Q{k} {q['id']} — {q['q'][:80]}…"):
                        st.write(f"Correct: **{LETTERS[q['answer']]}. {q['options'][q['answer']]}**")
                        st.markdown(q["explain"])
            if st.button("Finish"):
                st.session_state["mock1"] = None
                st.rerun()

# ---------------------------------------------------------------- Part 2
with t2:
    m = st.session_state.get("mock2")
    bank = part2_bank()
    if not m:
        st.markdown(f"Draws one question per slot (**9**: CE201×2, CE202×2, CE203×2, CE204, CE205, CE206). "
                    f"Choose **5**, **{config.PART2['minutes']} min** countdown, then self-mark.")
        if st.button("▶ Start Part 2 mock", type="primary"):
            paper, reused = [], False
            for code, n in config.PART2_ALLOCATION.items():
                cands = [q["id"] for q in bank if q["code"] == code]
                random.shuffle(cands)
                for i in range(n):
                    if not cands:
                        break
                    if i >= len(cands):
                        reused = True
                    paper.append(cands[i % len(cands)])
            st.session_state["mock2"] = {"paper": paper, "chosen": [], "phase": "choose", "reused": reused}
            st.rerun()
    else:
        qmap = {q["id"]: q for q in bank}
        if m["reused"]:
            st.caption("Some subjects have fewer bank questions than slots — a question was repeated.")
        labels = {f"Q{i + 1}": qid for i, qid in enumerate(m["paper"])}
        if m["phase"] == "choose":
            for lab, qid in labels.items():
                q = qmap[qid]
                with st.expander(f"{lab} · {q['code']} — {q['title']}"):
                    st.markdown(q["prompt"])
            chosen = st.multiselect("Choose 5 questions", list(labels), max_selections=5,
                                    default=[k for k, v in labels.items() if qmap[v]["code"] in p["settings"]["part2_core"]][:5])
            if st.button("▶ Start 180-min clock", type="primary", disabled=len(chosen) != 5):
                m["chosen"] = chosen
                m["phase"] = "running"
                st.session_state["mock2_start"] = time.time()
                st.rerun()
        elif m["phase"] == "running":
            countdown("mock2_start", SECS)
            for lab in m["chosen"]:
                q = qmap[labels[lab]]
                with st.expander(f"{lab} · {q['code']} — {q['title']}", expanded=False):
                    st.markdown(q["prompt"])
            if st.button("⏹ Stop clock & self-mark", type="primary"):
                m["elapsed"] = time.time() - st.session_state["mock2_start"]
                m["phase"] = "mark"
                st.session_state["mock2_start"] = None
                st.rerun()
        else:
            st.info(f"Time used {fmt_mmss(m['elapsed'])} of {fmt_mmss(SECS)}")
            totals = {}
            for lab in m["chosen"]:
                q = qmap[labels[lab]]
                with st.container(border=True):
                    st.markdown(f"**{lab} · {q['id']} — {q['title']}**")
                    with st.expander("Approach outline"):
                        for s in q["approach"]:
                            st.markdown(f"- {s}")
                    cols = st.columns(len(config.RUBRIC))
                    sc = {crit: c.select_slider(f"{crit} ({w}%)", [0, 1, 2, 3, 4], 2, key=f"m2_{lab}_{crit}")
                          for c, (crit, w) in zip(cols, config.RUBRIC.items())}
                    totals[lab] = (q, sc, sum(sc[k] / 4 * w for k, w in config.RUBRIC.items()))
            avg = sum(t[2] for t in totals.values()) / len(totals)
            st.metric("Paper score (avg of 5)", f"{avg:.0f}%")
            if st.button("💾 Save mock", type="primary"):
                for lab, (q, sc, pct) in totals.items():
                    p["part2_attempts"].append({"ts": now_iso(), "qid": q["id"], "code": q["code"], "scores": sc,
                                                "score_pct": round(pct, 1), "seconds": round(m["elapsed"] / 5),
                                                "notes": "", "mock": True})
                p["mock_results"].append({"ts": now_iso(), "part": 2, "score_pct": round(avg, 1),
                                          "by_subject": {t[0]["code"]: round(t[2], 1) for t in totals.values()},
                                          "seconds": round(m["elapsed"]), "n": 5})
                save()
                st.session_state["mock2"] = None
                st.success("Mock saved.")
                st.rerun()

# ---------------------------------------------------------------- history
with t3:
    mr = pd.DataFrame(p["mock_results"])
    if mr.empty:
        st.caption("No mocks yet.")
    else:
        mr["Part"] = mr["part"].map({1: "Part 1", 2: "Part 2"})
        mr["time"] = mr["seconds"].map(fmt_mmss)
        st.dataframe(mr[["ts", "Part", "score_pct", "n", "time"]].iloc[::-1], hide_index=True, width="stretch")
