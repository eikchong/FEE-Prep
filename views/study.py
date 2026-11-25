"""Study: two levels — subjects (home), then one page per subject with every topic on it.

/study            → Study home (countdown, continue reading, subject rows)
/study?s=CE104    → subject page; topic anchors #ce104-05; ?at=<section key> scrolls to a section
"""
from __future__ import annotations

import html
from datetime import date

import streamlit as st

import config
from utils import library, scrollread
from utils.latex_plain import to_plain
from utils.notes_index import index
from utils.qblock import source_line
from utils.reading import (READ_WPM, completed_topics, continue_target, mark_read, mark_topic_unread,
                           overall_stats, section_words, subject_stats, topic_number, topic_sections)
from utils.state import all_mcqs, days_to_exam, init, save
from utils.syllabus import subject_map, subjects

P1, P2 = config.COLOR_P1, config.COLOR_P2
GREEN, ORANGE, GREY, BLUE_TXT, TXT = "#1f7a3a", "#b04716", "#5c5f6b", "#2269bd", "#31333F"
STUDY_PAGE = "views/study.py"

p = init()
read = p.setdefault("read", {})
revisit = p.setdefault("revisit", {})


def _study():
    from utils.study_notes import STUDY
    return STUDY


def part_color(code: str) -> str:
    return P1 if subject_map()[code]["part"] == 1 else P2


def plan_tag(code: str) -> str:
    s = p["settings"]
    n = s.get("part2_core", []).count(code)
    if subject_map()[code]["part"] == 1:
        return ""
    if n:
        return "In plan" + (f" ×{n}" if n > 1 else "")
    return "Backup" if code in s.get("part2_backup", []) else "Not in plan"


def mins(m: float) -> str:
    return f"{max(1, round(m))} min" if m >= 0.5 else "under 1 min"


def bar(pct: float, color: str, h: int = 6, w: str = "100%") -> str:
    return (f'<div style="height:{h}px;background:#e3e6ec;border-radius:{h // 2}px;max-width:{w}">'
            f'<div style="width:{max(0, min(100, pct * 100)):.1f}%;height:{h}px;background:{color};'
            f'border-radius:{h // 2}px"></div></div>')


def anchor(tid: str) -> str:
    return tid.lower()


def mcqs_for(code: str, tid: str | None = None) -> list[dict]:
    return [q for q in all_mcqs() if q["code"] == code and (tid is None or q.get("topic") == tid)]


CSS = """
<style>
.katex-display { overflow-x: auto; overflow-y: hidden; padding: 2px 0; }
.fee-muted { color: #5c5f6b; }
.fee-toc { list-style: none; margin: 0 !important; padding: 0 !important; border-top: 1px solid #e6e8ef; }
.fee-toc li { margin: 0 !important; padding: 0 !important; list-style: none; }
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] a { color: #31333F; text-decoration: none; }
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] a:hover { color: #2269bd; }
.fee-toc a { display: flex; gap: 14px; align-items: center; min-height: 44px; padding: 0 8px;
  border-bottom: 1px solid #e6e8ef; color: #31333F; text-decoration: none; }
.fee-toc a:hover { background: #f7f8fa; }
.fee-toc .n { width: 22px; flex: none; color: #5c5f6b; }
.fee-toc .t { flex: 1 1 auto; }
.fee-toc .s { flex: none; text-align: right; color: #5c5f6b; }
.fee-label { font-size: 14px; font-weight: 600; color: #2269bd; margin: 48px 0 -6px; }
.fee-src { font-size: 13px; color: #5c5f6b; margin: -8px 0 6px; }
.fee-row { display: block; padding: 14px 18px; border: 1px solid #e6e8ef; border-radius: 10px; }
.fee-row.dash { border-style: dashed; border-color: #c9ced8; color: #5c5f6b; }
.fee-qset { font-size: 13px; font-weight: 600; color: #5c5f6b; }
[data-testid="stPageLink"] a { background: transparent !important; padding-left: 0; }
[data-testid="stPageLink"] a span, [data-testid="stPageLink"] a p { white-space: normal !important; overflow: visible !important;
  text-overflow: clip !important; }
section[data-testid="stSidebar"] [data-testid="stPageLink"] a { padding: 4px 8px; }
</style>
"""

SUBJECT_CSS = """
<style>
[data-testid="stMainBlockContainer"] { max-width: 820px; padding-top: 5rem; }
</style>
"""


# ======================================================================== sidebar (subject list)
def sidebar(current: str | None, ov: dict) -> None:
    with st.sidebar:
        st.page_link(STUDY_PAGE, label="All subjects", icon=":material/arrow_back:")
        for part in (1, 2):
            st.caption(f"**Part {part}**")
            for s in subjects(part):
                code, ss = s["code"], ov["subjects"][s["code"]]
                pct = f"{ss['pct']:.0%}" if ss["has_notes"] else "no notes"
                if code != current:
                    st.page_link(STUDY_PAGE, label=f"**{code}** {s['name']} · {pct}", query_params={"s": code})
                    continue
                with st.container(border=True):
                    st.markdown(f"**{code}** {s['name']} · **{pct}**")
                    st.html(bar(ss["pct"], part_color(code), 4))
                    lines = []
                    for t in s["topics"]:
                        ts = ss["topics"][t["id"]]
                        icon = {"read": ":green[:material/check_circle:]", "reading": ":blue[:material/clock_loader_40:]",
                                "not_started": ":gray[:material/radio_button_unchecked:]",
                                "covered": ":gray[:material/remove:]", "none": ":gray[:material/remove:]"}[ts["status"]]
                        if ts["revisit"]:
                            icon = ":orange[:material/flag:]"
                        lines.append(f"{icon} [{to_plain(t['name'])}](#{anchor(t['id'])})")
                    st.markdown("  \n".join(lines))


# ======================================================================== home
def home() -> None:
    ov = overall_stats(p)
    sidebar(None, ov)
    st.html(CSS)
    d = days_to_exam()
    st.title("Study")
    st.caption("Pick a subject and scroll. Progress saves as you read.")
    st.markdown(
        f"**{d} days** to go · Wed {config.EXAM_DATE:%-d %b %Y} &nbsp;·&nbsp; **Part 1** "
        f"{config.PART1['start']:%H:%M}–{config.PART1['end']:%H:%M} · 40 MCQs, answer all &nbsp;·&nbsp; "
        f"**Part 2** {config.PART2['start']:%H:%M}–{config.PART2['end']:%H:%M} · answer 5 of 9 &nbsp;·&nbsp; "
        "Eurocodes + Singapore NAs only · AASHTO for transport")

    tgt = continue_target(p)
    if tgt:
        code, tid, key = tgt
        ts = ov["subjects"][code]["topics"][tid]
        s = subject_map()[code]
        n = len(s["topics"])
        with st.container(border=True):
            c1, c2 = st.columns([4, 1], vertical_alignment="center")
            with c1:
                st.caption("**Continue reading**")
                st.markdown(f"#### {next(t['name'] for t in s['topics'] if t['id'] == tid)}")
                st.caption(f"{code} {s['name']} · topic {topic_number(tid)} of {n} · {ts['pct']:.0%} read · "
                           f"about {mins(ts['minutes_left'])} left in this topic")
                st.html(bar(ts["pct"], part_color(code), 6, "420px"))
            c2.page_link(STUDY_PAGE, label="Continue", icon=":material/arrow_forward:",
                         query_params={"s": code, "at": key}, width="stretch")

    st.markdown(f"**{ov['pct']:.0%}** of all notes read · {ov['n_topics_read']} of {ov['n_topics_with_notes']} "
                f"topics with notes read · {ov['n_without_notes']} subjects still need notes")

    cols = st.columns(2, gap="large")
    plan = p["settings"]
    for part, col in ((1, cols[0]), (2, cols[1])):
        with col:
            st.subheader(f"Part {part} · {'Breadth' if part == 1 else 'Depth'}")
            if part == 1:
                st.caption("All five subjects are examined in the 40 MCQs")
            else:
                core = ", ".join(f"{c}" + (f" ×{plan['part2_core'].count(c)}" if plan["part2_core"].count(c) > 1 else "")
                                 for c in dict.fromkeys(plan.get("part2_core", [])))
                st.caption(f"Your plan: {core}" + (f" · backup {', '.join(plan.get('part2_backup', []))}"
                                                   if plan.get("part2_backup") else ""))
            for s in subjects(part):
                subject_row(s, ov["subjects"][s["code"]])


def subject_row(s: dict, ss: dict) -> None:
    code = s["code"]
    tag = plan_tag(code)
    color = part_color(code)
    if not ss["has_notes"]:
        st.html(f'<div class="fee-row dash"><div style="display:flex;gap:10px;align-items:baseline">'
                f'<b>{code}</b><span style="flex:1 1 auto;font-weight:600;font-size:17px">{html.escape(s["name"])}</span>'
                f'<span style="font-size:13px;font-weight:600">{tag}</span></div>'
                f'<div style="margin-top:6px;font-size:14px">No notes yet · {ss["n_topics"]} topics</div></div>')
        return
    with st.container(border=True):
        pct = f"{ss['pct']:.0%}" if ss["read_words"] else "Not started"
        st.page_link(STUDY_PAGE, label=f"**{code}** · {s['name']} · {pct}" + (f" · {tag}" if tag else ""),
                     query_params={"s": code}, width="stretch")
        st.html(bar(ss["pct"], color))
        bits = []
        if ss["read_words"]:
            bits.append(f"{ss['n_read']} of {ss['n_with_notes']} topics read")
            bits.append(f"about {mins(ss['minutes_left'])} left")
        else:
            bits.append(f"{ss['n_with_notes']} topics · about {mins(ss['minutes'])} of notes")
        if ss["n_no_notes"]:
            bits.append(f"{ss['n_no_notes']} topic{'s have' if ss['n_no_notes'] != 1 else ' has'} no notes yet")
        if ss["last_read"] == date.today().isoformat():
            bits.append("last read today")
        st.caption(" · ".join(bits))


# ======================================================================== subject page
def on_read(ev: dict, code: str) -> None:
    keys = [k for k in (ev.get("keys") or []) if isinstance(k, str)]
    before = dict(read)
    new = mark_read(p, keys)
    secs = int(ev.get("seconds") or 0)
    if secs > 0:
        today = date.today().isoformat()
        log = p.setdefault("study_log", [])
        e = next((x for x in log if x.get("date") == today and x.get("code") == code
                  and x.get("note") == "auto · reading"), None)
        if e is None:
            e = {"date": today, "minutes": 0, "code": code, "note": "auto · reading", "seconds": 0}
            log.append(e)
        e["seconds"] = int(e.get("seconds", 0)) + secs
        e["minutes"] = round(e["seconds"] / 60)
    done = completed_topics(p, before, new) if new else []
    if new or secs:
        save(force=bool(done))
    for tid in done:
        st.toast(f"Topic read: {to_plain(next(t['name'] for s in subjects() for t in s['topics'] if t['id'] == tid))}",
                 icon=":material/check_circle:")


@st.fragment
def tracker(code: str, at: str | None) -> None:
    words = {k: w for k, w in section_words().items() if index()["sections"][k]["topic"].startswith(code + "-")}
    payload = {"code": code, "color": part_color(code), "words": words,
               "read": [k for k in words if k in read], "at": at}
    scrollread.mount(payload, lambda ev: on_read(ev, code))


def source_caption(doc: str, a: int, b: int, first: bool) -> None:
    d = _study()[doc]
    title = to_plain(d["title"])
    short = title.split(" · ")[0]
    label = f"{title if first else short} · {'slide' if a == b else 'slides'} {a}" + ("" if a == b else f"–{b}")
    fp = library.abs_path(doc)
    if fp.exists():
        c1, c2 = st.columns([5, 1], vertical_alignment="center")
        c1.html(f'<div class="fee-src">{html.escape(label)}</div>')
        c2.page_link("views/library.py", label="Open slides", query_params={"doc": doc, "page": str(a)})
    else:
        st.html(f'<div class="fee-src">{html.escape(label)}</div>')


def render_block(b, key: str) -> None:
    k = b[0]
    if k == "md":
        st.markdown(b[1])
    elif k == "eq":
        st.latex(b[1])
    elif k == "steps":
        st.markdown("\n".join(f"{i}. {t}" for i, t in enumerate(b[1], 1)))
    elif k == "ex":
        with st.container(border=True):
            st.markdown(f"**{b[1]}**  \n{b[2]}")
    elif k == "tip":
        st.info(b[1], icon=":material/lightbulb:")
    elif k == "q":
        render_q(b[1], key)


def render_q(qd: dict, key: str) -> None:
    with st.container(border=True):
        st.html(f'<div class="fee-qset">{html.escape(to_plain(qd["set"]))}</div>')
        st.markdown(qd["question"])
        if qd.get("figure"):
            st.caption(f"Figure: {qd['figure']}")
        with st.expander("Show answer"):
            st.markdown(qd["answer"])
            if qd.get("working"):
                st.markdown(qd["working"])
            st.caption(source_line(qd))


def end_card(code: str, tid: str, name: str, n: int) -> None:
    @st.fragment
    def card():
        from utils.reading import topic_stats
        ts = topic_stats(p, tid)
        flagged = tid in revisit
        plain = to_plain(name)
        nq = len(mcqs_for(code, tid))
        with st.container(border=True):
            if flagged:
                c1, c2 = st.columns([3, 1], vertical_alignment="center")
                c1.markdown(f":orange[:material/flag:] **{plain} — flagged to revisit**  \n"
                            ":gray[Shows in “Focus next” on Progress]")
                if c2.button("Clear flag", key=f"clr_{tid}", width="stretch"):
                    revisit.pop(tid, None)
                    save()
                    st.rerun(scope="fragment")
            elif ts["status"] == "read":
                c1, c2 = st.columns([3, 1], vertical_alignment="center")
                when = f" · finished {date.fromisoformat(ts['last_read']):%-d %b}" if ts["last_read"] else ""
                c1.markdown(f":green[:material/check_circle:] **{plain} — read**  \n"
                            f":gray[{ts['n_lecture'] + ts['n_practice']} sections{when}]")
                if c2.button("Revisit later", key=f"rev_{tid}", width="stretch"):
                    revisit[tid] = date.today().isoformat()
                    save()
                    st.rerun(scope="fragment")
                ck = f"unread_confirm_{tid}"
                lbl = "Click again to confirm" if st.session_state.get(ck) else "Mark topic unread"
                if c2.button(lbl, key=f"unr_{tid}", width="stretch", type="tertiary"):
                    if st.session_state.get(ck):
                        mark_topic_unread(p, tid)
                        st.session_state[ck] = False
                        save()
                    else:
                        st.session_state[ck] = True
                    st.rerun(scope="fragment")
            else:
                c1, c2 = st.columns([3, 1], vertical_alignment="center")
                c1.markdown(f"**{plain} — {ts['pct']:.0%} read**  \n"
                            ":gray[Keep scrolling: each section counts once it has been on screen for a few seconds.]")
                if c2.button("Revisit later", key=f"rev_{tid}", width="stretch"):
                    revisit[tid] = date.today().isoformat()
                    save()
                    st.rerun(scope="fragment")
                st.html(bar(ts["pct"], part_color(code)))
            if nq:
                st.page_link("views/mcq.py", label=f"{nq} practice question{'s' if nq != 1 else ''}",
                             icon=":material/quiz:", query_params={"s": code, "t": tid})
    card()


def subject(code: str) -> None:
    s = subject_map()[code]
    ov = overall_stats(p)
    ss = ov["subjects"][code]
    sidebar(code, ov)
    st.html(CSS + SUBJECT_CSS)
    at = st.query_params.get("at")
    tracker(code, at)

    color = part_color(code)
    n = len(s["topics"])
    nq_all = len(mcqs_for(code))
    st.page_link(STUDY_PAGE, label=f"Study / Part {s['part']} · {'Breadth' if s['part'] == 1 else 'Depth'}",
                 icon=":material/arrow_back:")
    st.title(f"{code} {s['name']}")
    st.caption(f"{n} topics · about {mins(ss['minutes'])} of notes · {nq_all} practice question"
               f"{'s' if nq_all != 1 else ''}")
    st.html(bar(ss["pct"], color, 8))
    st.markdown(f"**{ss['pct']:.0%} read** · {ss['n_read']} of {ss['n_with_notes']} topics with notes read · "
                f"about {mins(ss['minutes_left'])} left")
    tgt = continue_target(p, code)
    c1, c2 = st.columns([1, 1])
    if tgt:
        _, tid, key = tgt
        tname = to_plain(next(t["name"] for t in s["topics"] if t["id"] == tid))
        c1.page_link(STUDY_PAGE, label=f"Continue: {tname}", icon=":material/arrow_forward:",
                     query_params={"s": code, "at": key})
    if nq_all:
        c2.page_link("views/mcq.py", label=f"Practise {code} ({nq_all} questions)", icon=":material/quiz:",
                     query_params={"s": code})

    extra = []
    if s.get("themes"):
        extra.append("**Past-paper themes:** " + "; ".join(s["themes"]) + ".")
    reading = [r for r in library_reading() if code in r.get("codes", [])]
    if reading:
        extra.append("**Reading:** " + "; ".join(
            f"{r['authors']}, *{r['title']}*" + (f", {r['edition']}" if r.get("edition") else "") for r in reading) + ".")
    if extra:
        st.markdown(" ".join(extra))

    # contents
    st.markdown("#### In this subject")
    rows = []
    for i, t in enumerate(s["topics"], 1):
        ts = ss["topics"][t["id"]]
        if ts["revisit"]:
            right = f'<span style="color:{ORANGE};font-weight:600">Revisit</span>'
        elif ts["status"] == "read":
            right = f'<span style="color:{GREEN};font-weight:600">Read</span>'
        elif ts["status"] == "reading":
            right = f'<span style="color:{BLUE_TXT}">{ts["pct"]:.0%}</span>'
        elif ts["status"] == "not_started":
            right = mins(ts["minutes"])
        elif ts["status"] == "covered":
            right = "Covered in " + " and ".join(str(topic_number(c)) for c in ts["covered_in"])
        else:
            right = "No notes yet"
        muted = ' style="color:#5c5f6b"' if ts["status"] in ("covered", "none") else ""
        rows.append(f'<li><a href="#{anchor(t["id"])}"{muted}><span class="n">{i}</span>'
                    f'<span class="t">{html.escape(to_plain(t["name"]))}</span><span class="s">{right}</span></a></li>')
    st.html(f'<ol class="fee-toc">{"".join(rows)}</ol>')

    secs_idx = index()["sections"]
    for i, t in enumerate(s["topics"], 1):
        tid = t["id"]
        ts = ss["topics"][tid]
        st.html(f'<div class="fee-label">Topic {i} of {n}</div>')
        scrollread.topic_marker(to_plain(t["name"]))
        st.subheader(t["name"], anchor=anchor(tid))
        if ts["status"] in ("covered", "none"):
            if ts["covered_in"]:
                links = " and ".join(f"[{topic_number(c)}](#{anchor(c)})" for c in ts["covered_in"])
                st.caption(f"Covered in topics {links} — its notes sit there.")
            else:
                st.caption("No notes yet.")
            continue
        nq = sum(1 for k in topic_sections(tid) if secs_idx[k]["kind"] == "practice"
                 for b in _study()[secs_idx[k]["doc"]]["sections"][secs_idx[k]["idx"]]["blocks"] if b[0] == "q")
        meta = [f"{ts['n_lecture']} lecture section{'s' if ts['n_lecture'] != 1 else ''}"]
        if nq:
            meta.append(f"{nq} tutorial question{'s' if nq != 1 else ''}")
        meta += [f"about {mins(ts['minutes'])}", f"{ts['pct']:.0%} read"]
        st.caption(" · ".join(meta))

        lecture = index()["topics"][tid]["lecture"]
        practice = index()["topics"][tid]["practice"]
        prev_doc = None
        for k in lecture:
            sx = secs_idx[k]
            sec = _study()[sx["doc"]]["sections"][sx["idx"]]
            w = section_words()[k]
            scrollread.marker(k, w, "s")
            st.markdown(f"### {sec['title']}")
            source_caption(sx["doc"], *sec["pages"], first=sx["doc"] != prev_doc)
            prev_doc = sx["doc"]
            for j, b in enumerate(sec["blocks"]):
                render_block(b, f"{k}:{j}")
            scrollread.marker(k, w, "e")
        if practice:
            st.markdown("### Tutorial questions")
            sets = list(dict.fromkeys(to_plain(_study()[secs_idx[k]["doc"]]["title"]).split(" · ", 1)[-1]
                                      for k in practice))
            nq_t = sum(1 for k in practice for b in _study()[secs_idx[k]["doc"]]["sections"][secs_idx[k]["idx"]]["blocks"]
                       if b[0] == "q")
            st.html(f'<div class="fee-src">{html.escape("; ".join(sets))} · {nq_t} question{"s" if nq_t != 1 else ""}'
                    f' · answers stay hidden until you open them</div>')
            for k in practice:
                sx = secs_idx[k]
                sec = _study()[sx["doc"]]["sections"][sx["idx"]]
                w = section_words()[k]
                scrollread.marker(k, w, "s")
                if not any(b[0] == "q" for b in sec["blocks"]):
                    st.markdown(f"**{sec['title']}**")
                for j, b in enumerate(sec["blocks"]):
                    render_block(b, f"{k}:{j}")
                scrollread.marker(k, w, "e")
        end_card(code, tid, t["name"], n)


def library_reading() -> list[dict]:
    from utils.storage import load_static
    try:
        return load_static("reading_list.json")
    except Exception:
        return []


st.html(scrollread.CSS_GLOBAL)
code = st.query_params.get("s")
if code and code in subject_map():
    subject(code)
else:
    home()
