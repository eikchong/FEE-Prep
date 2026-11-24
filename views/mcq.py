import random
import time

import pandas as pd
import streamlit as st

import config
from utils.state import all_mcqs, init, new_id, now_iso, save
from utils.syllabus import subject_label, subject_map, topic_label
from utils.ui import metric, countdown, fmt_mmss, open_in_library

p = init()
st.title("Part 1 MCQ drill")
bank = all_mcqs()
LETTERS = "ABCD"

codes = st.multiselect("Subjects", config.PART1_CODES, default=config.PART1_CODES, format_func=subject_label)
pool = [q for q in bank if q["code"] in codes]
st.caption(f"{len(pool)} questions in pool · {len(bank)} in bank · pace {config.PART1['pace_min']} min/question")


def record(q, chosen, mode, seconds):
    p["mcq_attempts"].append({"ts": now_iso(), "qid": q["id"], "code": q["code"], "chosen": chosen,
                              "correct": chosen == q["answer"], "mode": mode, "seconds": round(seconds, 1)})


def source_button(q, key):
    src = q.get("source") or {}
    if src.get("doc"):
        if st.button(f"📖 Review source ({src['doc']}, p. {src.get('page', 1)})", key=key):
            open_in_library(src["doc"], int(src.get("page", 1)))


def pick_next(pool):
    """Prefer unseen, then previously-wrong questions."""
    hist = {}
    for a in p["mcq_attempts"]:
        hist[a["qid"]] = a["correct"]
    unseen = [q for q in pool if q["id"] not in hist]
    wrong = [q for q in pool if hist.get(q["id"]) is False]
    return random.choice(unseen or wrong or pool)


tab_p, tab_t, tab_add, tab_bank = st.tabs(["Practice", "Timed set", "➕ Add my own question", "Question bank"])

# ---------------------------------------------------------------- practice
with tab_p:
    if not pool:
        st.info("Select at least one subject with questions.")
    else:
        cur = st.session_state.get("prac_q")
        if not cur or cur not in {q["id"] for q in pool}:
            st.session_state["prac_q"] = pick_next(pool)["id"]
            st.session_state["prac_start"] = time.time()
            st.session_state["prac_done"] = None
        q = next(x for x in pool if x["id"] == st.session_state["prac_q"])
        with st.container(border=True):
            st.caption(f"{subject_label(q['code'])} · {topic_label(q['topic']) if q.get('topic') else ''} · `{q['id']}`")
            st.markdown(f"**{q['q']}**")
            done = st.session_state.get("prac_done")
            choice = st.radio("Answer", range(4), format_func=lambda i: f"{LETTERS[i]}. {q['options'][i]}",
                              index=None, key=f"prac_choice_{q['id']}", disabled=done is not None,
                              label_visibility="collapsed")
            b1, b2 = st.columns([1, 1])
            if done is None and b1.button("Check", type="primary", disabled=choice is None):
                el = time.time() - st.session_state["prac_start"]
                record(q, choice, "practice", el)
                save()
                st.session_state["prac_done"] = {"choice": choice, "secs": el}
                st.rerun()
            if done is not None:
                ok = done["choice"] == q["answer"]
                (st.success if ok else st.error)(
                    f"{'✅ Correct' if ok else '❌ Incorrect'} — answer **{LETTERS[q['answer']]}. "
                    f"{q['options'][q['answer']]}** · {fmt_mmss(done['secs'])} "
                    f"({'within' if done['secs'] <= config.PART1['pace_min'] * 60 else 'over'} pace)")
                st.markdown(f"**Explanation.** {q['explain']}")
                source_button(q, f"src_p_{q['id']}")
                if not ok and st.button("Add to error log"):
                    p["errors"].append({"id": new_id(), "ts": now_iso(), "code": q["code"], "source": f"MCQ {q['id']}",
                                        "what": f"Chose {LETTERS[done['choice']]} — {q['q'][:120]}",
                                        "fix": q["explain"][:300], "resolved": False,
                                        "source_doc": (q.get("source") or {}).get("doc"),
                                        "source_page": (q.get("source") or {}).get("page")})
                    save()
                    st.toast("Added to error log")
            if b2.button("Next question ➜"):
                st.session_state["prac_q"] = pick_next([x for x in pool if x["id"] != q["id"]] or pool)["id"]
                st.session_state["prac_start"] = time.time()
                st.session_state["prac_done"] = None
                st.rerun()

# ---------------------------------------------------------------- timed
with tab_t:
    ts = st.session_state.get("timed")
    if not ts:
        n = st.number_input("Number of questions", 1, max(1, len(pool)), min(10, max(1, len(pool))))
        st.caption(f"Time allowed: {n * config.PART1['pace_min']:.1f} min")
        if st.button("Start timed set", type="primary", disabled=not pool):
            qs = random.sample(pool, int(n))
            st.session_state["timed"] = {"qids": [q["id"] for q in qs], "secs": int(n * config.PART1["pace_min"] * 60),
                                         "result": None}
            st.session_state["timed_start"] = time.time()
            st.rerun()
    else:
        qmap = {q["id"]: q for q in bank}
        qs = [qmap[i] for i in ts["qids"] if i in qmap]
        if ts["result"] is None:
            countdown("timed_start", ts["secs"])
            with st.form("timed_form"):
                for k, q in enumerate(qs, 1):
                    st.markdown(f"**Q{k}.** {q['q']}")
                    st.radio(f"Q{k}", range(4), format_func=lambda i, q=q: f"{LETTERS[i]}. {q['options'][i]}",
                             index=None, key=f"t_{q['id']}", label_visibility="collapsed")
                    st.divider()
                sub = st.form_submit_button("Submit set", type="primary")
            if sub:
                el = time.time() - st.session_state["timed_start"]
                res = []
                for q in qs:
                    ch = st.session_state.get(f"t_{q['id']}")
                    record(q, ch, "timed", el / len(qs))
                    res.append({"id": q["id"], "code": q["code"], "chosen": ch, "correct": ch == q["answer"]})
                save()
                ts["result"] = {"rows": res, "elapsed": el}
                st.session_state["timed_start"] = None
                st.rerun()
        else:
            r = ts["result"]
            score = sum(x["correct"] for x in r["rows"])
            metric(st, "Score", f"{score}/{len(r['rows'])}", f"{score / len(r['rows']):.0%} · {fmt_mmss(r['elapsed'])}")
            if r["elapsed"] > ts["secs"]:
                st.warning(f"Over time by {fmt_mmss(r['elapsed'] - ts['secs'])}")
            for k, (q, x) in enumerate(zip(qs, r["rows"]), 1):
                icon = "✅" if x["correct"] else "❌"
                with st.expander(f"{icon} Q{k} {q['id']} — {q['q'][:80]}…"):
                    ch = x["chosen"]
                    st.write(f"Your answer: {LETTERS[ch] + '. ' + q['options'][ch] if ch is not None else '—'}")
                    st.write(f"Correct: **{LETTERS[q['answer']]}. {q['options'][q['answer']]}**")
                    st.markdown(q["explain"])
                    source_button(q, f"src_t_{q['id']}")
            if st.button("New set"):
                st.session_state["timed"] = None
                st.rerun()

# ---------------------------------------------------------------- add
with tab_add:
    src = st.session_state.get("new_q_source") or {}
    if src:
        st.info(f"Source prefilled from Library: **{src['doc']}**, p. {src['page']}")
    with st.form("add_q", clear_on_submit=True):
        c1, c2 = st.columns(2)
        dcode = (src.get("topic") or "CE101").split("-")[0]
        code = c1.selectbox("Subject", list(subject_map()), index=list(subject_map()).index(dcode),
                            format_func=subject_label)
        topics = [t["id"] for t in subject_map()[code]["topics"]]
        topic = c2.selectbox("Sub-topic (optional)", [None] + topics, format_func=lambda t: "—" if t is None else topic_label(t),
                             index=(topics.index(src["topic"]) + 1) if src.get("topic") in topics else 0)
        qtext = st.text_area("Question")
        opts = [st.text_input(f"Option {LETTERS[i]}") for i in range(4)]
        ans = st.radio("Correct option", range(4), format_func=lambda i: LETTERS[i], horizontal=True)
        explain = st.text_area("Explanation / working")
        s1, s2 = st.columns([3, 1])
        sdoc = s1.text_input("Source file (materials/ relative path)", value=src.get("doc", ""))
        spage = s2.number_input("Page", 1, 5000, int(src.get("page", 1)))
        if st.form_submit_button("Save question", type="primary"):
            if not qtext.strip() or any(not o.strip() for o in opts):
                st.error("Question and all four options are required.")
            else:
                p["custom_mcqs"].append({"id": f"U-{code}-{new_id()[:6]}", "code": code, "topic": topic,
                                         "q": qtext.strip(), "options": [o.strip() for o in opts], "answer": ans,
                                         "explain": explain.strip(),
                                         "source": {"doc": sdoc, "page": int(spage)} if sdoc.strip() else None})
                save()
                st.session_state["new_q_source"] = None
                st.success("Saved.")
    if code not in config.PART1_CODES:
        st.caption("Note: drills use Part 1 subjects; Part 2 MCQs are stored but not drilled.")

# ---------------------------------------------------------------- bank
with tab_bank:
    att = pd.DataFrame(p["mcq_attempts"])
    stats = att.groupby("qid")["correct"].agg(["count", "mean"]) if not att.empty else pd.DataFrame()
    rows = []
    for q in bank:
        s = stats.loc[q["id"]] if q["id"] in stats.index else None
        rows.append({"id": q["id"], "code": q["code"], "question": q["q"][:110],
                     "attempts": int(s["count"]) if s is not None else 0,
                     "accuracy": float(s["mean"]) if s is not None else None,
                     "source": (q.get("source") or {}).get("doc") or ""})
    st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True,
                 column_config={"accuracy": st.column_config.ProgressColumn(min_value=0, max_value=1, format="percent")})
    mine = p["custom_mcqs"]
    if mine:
        rm = st.selectbox("Delete one of my questions", [None] + [q["id"] for q in mine])
        if rm and st.button("Delete"):
            p["custom_mcqs"] = [q for q in mine if q["id"] != rm]
            save()
            st.rerun()
