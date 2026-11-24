import streamlit as st

import config
from utils import export
from utils.formulas import LEGACY_NOTE, codes as formula_codes, legacy_items, sections
from utils.export import cite
from utils.state import init, save
from utils.syllabus import subjects
from utils.ui import open_in_library

p = init()
st.title("Formula & code sheet")
st.caption(f"{config.CODES_RULE} {LEGACY_NOTE}")

# ---------------------------------------------------------------- export
with st.container(border=True):
    st.markdown("**🖨️ Export for the open-book binder**")
    e1, e2, e3 = st.columns([2, 1, 1])
    codes = e1.multiselect("Subjects", formula_codes(), default=formula_codes(),
                           label_visibility="collapsed")
    with_index = e1.checkbox("Include binder index (subject → sub-topic → file & page)", value=True)
    idx = export.binder_index() if with_index else {}
    md = export.to_markdown(codes, p["formula_notes"], p["pins"], idx)
    e2.download_button("⬇️ Markdown", md, "fee2027_formula_sheet.md", "text/markdown", width="stretch")
    if e3.button("Build PDF", width="stretch"):
        with st.spinner("Rendering formulas…"):
            st.session_state["sheet_pdf"] = export.to_pdf(codes, p["formula_notes"], p["pins"], idx)
    if st.session_state.get("sheet_pdf"):
        e3.download_button("⬇️ PDF", st.session_state["sheet_pdf"], "fee2027_formula_sheet.pdf",
                           "application/pdf", width="stretch", type="primary")

# ---------------------------------------------------------------- tabs
subs = subjects()
tabs = st.tabs([s["code"] for s in subs])
for tab, s in zip(tabs, subs):
    with tab:
        st.subheader(f"{s['code']} {s['name']}")
        for si, sec in enumerate(sections(s["code"])):
            if sec["title"]:
                h1, h2 = st.columns([4, 1])
                h1.markdown(f"#### {sec['title']}")
                if sec.get("src") and h2.button(f"📖 p. {sec['src']['page']}", key=f"sec_{s['code']}_{si}",
                                                 help=cite(sec["src"])):
                    open_in_library(sec["src"]["doc"], sec["src"]["page"])
            for fi, f in enumerate(sec["items"]):
                with st.container(border=True):
                    head = f"**{f['title']}**"
                    if f["clause"]:
                        head += f" · `{f['clause']}`"
                    if f["verify"]:
                        head += " · :orange[⚠ verify against Singapore NA]"
                    st.markdown(head)
                    if f["latex"]:
                        st.latex(f["latex"])
                    if f["note"] or f.get("src"):
                        st.caption(" · ".join(x for x in [f["note"], cite(f.get("src"))] if x))
        leg = legacy_items(s["code"])
        if leg:
            with st.expander(f"🚫 Legacy methods in the notes ({len(leg)}) — not acceptable in FEE 2027"):
                for f in leg:
                    st.markdown(f"- **{f['title']}** — {f['note']} {cite(f.get('src'))}")
        pins = [x for x in p["pins"] if x.get("code") == s["code"]]
        if pins:
            st.markdown("#### 📌 Pinned excerpts")
            for x in pins:
                with st.container(border=True):
                    st.markdown(f"{x['excerpt']}")
                    c1, c2, c3 = st.columns([3, 1, 1])
                    c1.caption(f"{x['topic_id']} · ({x['doc']}, p. {x['page']})")
                    if c2.button("Open", key=f"pin_open_{x['id']}"):
                        open_in_library(x["doc"], x["page"])
                    if c3.button("Unpin", key=f"pin_del_{x['id']}"):
                        p["pins"] = [y for y in p["pins"] if y["id"] != x["id"]]
                        save()
                        st.rerun()
        st.markdown("#### ✍️ My notes")
        cur = p["formula_notes"].get(s["code"], "")
        txt = st.text_area("Markdown notes (included in export)", cur, height=160, key=f"fn_{s['code']}",
                           label_visibility="collapsed",
                           placeholder="e.g. NA values you confirmed, design-chart page refs, traps…")
        if txt != cur:
            p["formula_notes"][s["code"]] = txt
            save()
            st.toast("Notes saved")
