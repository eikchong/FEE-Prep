import time
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import config
from utils import library, pastpapers as pp
from utils.state import init, new_id, now_iso, save
from utils.syllabus import subject_label, subjects, topic_label
from utils.ui import countdown, fmt_mmss, part_color, rubric_form, show_pdf_page

p = init()
st.title("Past papers")
st.caption("Official PEB Annex A questions (2017, 2020, 2026) and a candidate's 2019 recollection, indexed by "
           "subject and sub-topic. Attempt them against the original PDF page. The PDFs stay local in "
           "`materials/_past_papers/` (not in the public repo).")
LET = pp.LETTERS

# ---------------------------------------------------------------- source files
missing = [d for d in pp.docs() if not pp.doc_available(d)]
with st.expander(f"📂 Source PDFs — {len(pp.docs()) - len(missing)}/{len(pp.docs())} available",
                 expanded=bool(missing)):
    for doc, meta in pp.docs().items():
        ok = pp.doc_available(doc)
        c1, c2 = st.columns([3, 2])
        c1.markdown(f"{'✅' if ok else '⬜'} **{meta['label']}**  \n<small>`materials/{doc}` · "
                    f"{meta['kind']}</small>", unsafe_allow_html=True)
        if not ok:
            up = c2.file_uploader(f"Upload {meta['upload_hint']}", type=["pdf"], key=f"up_{doc}")
            if up is not None:
                target = config.MATERIALS_DIR / doc
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(up.getbuffer())
                library.ingest()
                st.rerun()
    if missing:
        st.caption("On Streamlit Cloud uploads are lost on restart — re-upload when needed.")

# ---------------------------------------------------------------- helpers
att = pd.DataFrame(p["mcq_attempts"])
p2att = pd.DataFrame(p["part2_attempts"])


def appearance_text(q):
    return ", ".join(f"{a['year']}" + (f" Q{a['q']}" if a.get("q") else "") for a in q["appearances"])


def pdf_panel(q, key):
    pages = q["appearances"]
    if len(pages) > 1:
        i = st.radio("Source", range(len(pages)), horizontal=True, key=f"src_{key}",
                     format_func=lambda i: f"{pages[i]['year']} p.{pages[i]['page']}")
    else:
        i = 0
    a = pages[i]
    path = config.MATERIALS_DIR / a["doc"]
    if path.exists():
        show_pdf_page(path, a["page"], key=f"pp_{key}_{i}")
        nxt = st.checkbox("Show next page too (figures / continuation)", key=f"nx_{key}_{i}")
        if nxt:
            show_pdf_page(path, a["page"] + 1, key=f"pp_{key}_{i}_n")
    else:
        st.info(f"Upload **{pp.docs()[a['doc']]['label']}** above to see the question (PDF page {a['page']}).")


def badges(q):
    b = [f"`{q['id']}`", subject_label(q["code"]), f"seen {appearance_text(q)}"]
    if len({a['year'] for a in q["appearances"]}) > 1:
        b.append("🔁 **in several sources**")
    if q.get("legacy"):
        b.append(":red[legacy BS code]")
    if pp.docs()[q["appearances"][0]["doc"]]["kind"] == "recollection":
        b.append(":orange[recollection]")
    return " · ".join(b)


tab_f, tab_1, tab_2 = st.tabs(["📊 What gets asked", "Part 1 MCQs", "Part 2 questions"])

# ---------------------------------------------------------------- frequency
with tab_f:
    st.markdown("Each bar counts **question-years** — a question printed in the 2017, 2020 and 2026 brochures counts 3. "
                "PEB reprints its sample questions, so repeats show what PEB treats as representative "
                "(not proof the same question was re-set); the 2019 recollection reflects an actual sitting.")
    c1, c2 = st.columns(2)
    for col, part in ((c1, 1), (c2, 2)):
        f = pp.frequency(part)
        codes = [s["code"] for s in subjects() if f.get(s["code"])]
        fig = go.Figure(go.Bar(x=codes, y=[f[c] for c in codes], marker_color=[part_color(c) for c in codes],
                               text=[f[c] for c in codes], textposition="outside"))
        fig.update_layout(title=f"Part {part}", height=300, margin=dict(l=0, r=0, t=40, b=0),
                          yaxis_title="question-years")
        col.plotly_chart(fig, width="stretch")
    rep = [q for q in pp.items() if len({a["year"] for a in q["appearances"]}) > 1]
    st.subheader(f"🔁 Questions in more than one source ({len(rep)})")
    st.dataframe(pd.DataFrame([{"Part": q["part"], "Subject": q["code"], "Question": q["title"],
                                "Years": appearance_text(q)} for q in rep]),
                 hide_index=True, width="stretch")
    tf = pp.topic_frequency()
    st.subheader("Most-tested sub-topics")
    st.dataframe(pd.DataFrame([{"Sub-topic": topic_label(t), "Question-years": n} for t, n in tf.most_common(15)]),
                 hide_index=True, width="stretch")

# ---------------------------------------------------------------- Part 1
with tab_1:
    qs = pp.items(1)
    f1, f2, f3 = st.columns(3)
    fc = f1.multiselect("Subject", sorted({q["code"] for q in qs}), key="pp1_code")
    fy = f2.multiselect("Year", sorted({y for q in qs for y in pp.years(q)}), key="pp1_year")
    only_keyed = f3.toggle("Only questions with full options", value=False)
    view = [q for q in qs if (not fc or q["code"] in fc) and (not fy or set(fy) & set(pp.years(q)))
            and (not only_keyed or (q.get("answer") is not None and not q.get("options_missing")))]
    acc = att.groupby("qid")["correct"].agg(["count", "mean"]) if not att.empty else pd.DataFrame()
    st.caption(f"{len(view)} questions")
    labels = {f"{q['code']} · {q['title']} ({appearance_text(q)})" + (" ✓" if q["id"] in acc.index else ""): q["id"]
              for q in view}
    pick = st.selectbox("Question", list(labels), key="pp1_sel")
    sel = labels.get(pick)
    if sel:
        q = next(x for x in view if x["id"] == sel)
        st.markdown(badges(q))
        left, right = st.columns([3, 2])
        with left:
            pdf_panel(q, sel)
        with right:
            st.markdown("**Your answer**")
            done = st.session_state.get(f"pp1_done_{sel}")
            if q.get("answer") is not None and not q.get("options_missing"):
                if f"pp1_t_{sel}" not in st.session_state:
                    st.session_state[f"pp1_t_{sel}"] = time.time()
                ch = st.radio("Answer", range(4), format_func=lambda i: f"({LET[i]})", horizontal=True,
                              index=None, key=f"pp1_ch_{sel}", disabled=done is not None,
                              label_visibility="collapsed")
                if done is None and st.button("Check", type="primary", disabled=ch is None):
                    el = time.time() - st.session_state[f"pp1_t_{sel}"]
                    ok = ch == q["answer"]
                    p["mcq_attempts"].append({"ts": now_iso(), "qid": sel, "code": q["code"], "chosen": ch,
                                              "correct": ok, "mode": "past", "seconds": round(el, 1)})
                    save()
                    st.session_state[f"pp1_done_{sel}"] = {"ch": ch, "el": el}
                    st.rerun()
                if done is not None:
                    ok = done["ch"] == q["answer"]
                    (st.success if ok else st.error)(f"{'✅ Correct' if ok else '❌ Incorrect'} — key **({LET[q['answer']]})** "
                                                     f"· {fmt_mmss(done['el'])} (pace {config.PART1['pace_min']} min)")
                    if not ok and st.button("Add to error log", key=f"pp1_err_{sel}"):
                        a0 = q["appearances"][0]
                        p["errors"].append({"id": new_id(), "ts": now_iso(), "code": q["code"],
                                            "source": f"Past paper {appearance_text(q)} — {q['title']}",
                                            "what": f"Chose ({LET[done['ch']]})", "fix": q["explain"][:300],
                                            "resolved": False, "source_doc": a0["doc"], "source_page": a0["page"]})
                        save()
                        st.toast("Added to error log")
                    if st.button("↺ Try again", key=f"pp1_re_{sel}"):
                        for k in (f"pp1_done_{sel}", f"pp1_t_{sel}", f"pp1_ch_{sel}"):
                            st.session_state.pop(k, None)
                        st.rerun()
                show = done is not None
            else:
                st.caption("Options/answer not fully recalled — work it, then reveal the worked solution.")
                show = st.toggle("Reveal worked solution", key=f"pp1_rev_{sel}")
            if show:
                src = {"computed": "computed & unit-tested", "reasoned": "reasoned",
                       "candidate": "candidate's key (unverified)"}[q["answer_source"]]
                st.markdown(f"**Worked solution** <small>({src})</small>", unsafe_allow_html=True)
                st.markdown(q["explain"])
                if q.get("verify"):
                    st.warning("⚠ " + q["verify"])
            st.caption("Sub-topics: " + ", ".join(topic_label(t) for t in q["topics"]))
            if sel in acc.index:
                st.caption(f"Your record: {int(acc.loc[sel, 'count'])} attempts · {acc.loc[sel, 'mean']:.0%} correct")

# ---------------------------------------------------------------- Part 2
with tab_2:
    qs = pp.items(2)
    f1, f2 = st.columns(2)
    fc = f1.multiselect("Subject", sorted({q["code"] for q in qs}), key="pp2_code",
                        default=[c for c in sorted({q["code"] for q in qs})
                                 if c in set(p["settings"]["part2_core"]) | set(p["settings"]["part2_backup"])])
    fy = f2.multiselect("Year", sorted({y for q in qs for y in pp.years(q)}), key="pp2_year")
    view = [q for q in qs if (not fc or q["code"] in fc) and (not fy or set(fy) & set(pp.years(q)))]
    done_ids = set(p2att["qid"]) if not p2att.empty else set()
    if not view:
        st.info("No questions for this filter.")
        st.stop()
    labels = {f"{q['code']} · {q['title']} ({appearance_text(q)})" + (" ✓" if q["id"] in done_ids else ""): q["id"]
              for q in view}
    sel = labels[st.selectbox("Question", list(labels), key="pp2_sel")]
    q = next(x for x in view if x["id"] == sel)
    st.markdown(badges(q))
    if q.get("legacy"):
        st.error("Set in BS 8110 terms — legacy, not acceptable in FEE 2027. Practise it in Eurocode terms.")
    SECS = int(config.PART2["pace_min"] * 60)
    ws = st.session_state.setdefault("pp2", {})
    state = ws.get(sel, {"phase": "ready"})
    left, right = st.columns([3, 2])
    with left:
        pdf_panel(q, sel)
    with right:
        if state["phase"] == "ready":
            if st.button("▶ Start 36-min attempt", type="primary", key=f"pp2_go_{sel}"):
                ws[sel] = {"phase": "running"}
                st.session_state[f"pp2start_{sel}"] = time.time()
                st.rerun()
            st.caption("The approach outline is revealed after your attempt.")
        elif state["phase"] == "running":
            countdown(f"pp2start_{sel}", SECS)
            if st.button("⏹ Finish & self-mark", type="primary", key=f"pp2_stop_{sel}"):
                ws[sel] = {"phase": "mark", "elapsed": time.time() - st.session_state[f"pp2start_{sel}"]}
                st.session_state[f"pp2start_{sel}"] = None
                st.rerun()
        else:
            el = state["elapsed"]
            (st.success if el <= SECS else st.warning)(f"Time taken {fmt_mmss(el)} (target {fmt_mmss(SECS)})")
            st.markdown("#### Approach outline")
            for s in q["approach"]:
                st.markdown(f"- {s}")
            kr = {k: v for k, v in (q.get("key_results") or {}).items() if k != "note"}
            if kr:
                st.caption("Key results (unit-tested): " + " · ".join(f"{k} = {v}" for k, v in kr.items()))
            if state["phase"] == "mark":
                scores, pct = rubric_form(f"pp2r_{sel}")
                notes = st.text_area("Notes — what to fix next time", key=f"pp2n_{sel}")
                st.metric("Score", f"{pct:.0f}%")
                if st.button("💾 Save attempt", type="primary", key=f"pp2_save_{sel}"):
                    p["part2_attempts"].append({"ts": now_iso(), "qid": sel, "code": q["code"], "scores": scores,
                                                "score_pct": round(pct, 1), "seconds": round(el), "notes": notes,
                                                "mock": False, "past": True})
                    if pct < 60 and notes.strip():
                        a0 = q["appearances"][0]
                        p["errors"].append({"id": new_id(), "ts": now_iso(), "code": q["code"],
                                            "source": f"Past paper {appearance_text(q)}", "what": notes.strip(),
                                            "fix": "", "resolved": False, "source_doc": a0["doc"],
                                            "source_page": a0["page"]})
                    save()
                    ws[sel] = {"phase": "saved", "elapsed": el}
                    st.rerun()
            else:
                st.success("Attempt saved.")
                if st.button("↺ Attempt again", key=f"pp2_again_{sel}"):
                    ws[sel] = {"phase": "ready"}
                    st.rerun()
        st.caption("Sub-topics: " + ", ".join(topic_label(t) for t in q["topics"]))
