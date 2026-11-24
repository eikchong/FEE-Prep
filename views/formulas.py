import streamlit as st

import config
from utils import export
from utils.formulas import FORMULAS, LEGACY_NOTE
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
    codes = e1.multiselect("Subjects", list(FORMULAS), default=list(FORMULAS),
                           label_visibility="collapsed")
    with_index = e1.checkbox("Include binder index (subject → sub-topic → file & page)", value=True)
    idx = export.binder_index() if with_index else {}
    md = export.to_markdown(codes, p["formula_notes"], p["pins"], idx)
    e2.download_button("⬇️ Markdown", md, "fee2027_formula_sheet.md", "text/markdown", use_container_width=True)
    if e3.button("Build PDF", use_container_width=True):
        with st.spinner("Rendering formulas…"):
            st.session_state["sheet_pdf"] = export.to_pdf(codes, p["formula_notes"], p["pins"], idx)
    if st.session_state.get("sheet_pdf"):
        e3.download_button("⬇️ PDF", st.session_state["sheet_pdf"], "fee2027_formula_sheet.pdf",
                           "application/pdf", use_container_width=True, type="primary")

# ---------------------------------------------------------------- tabs
subs = subjects()
tabs = st.tabs([s["code"] for s in subs])
for tab, s in zip(tabs, subs):
    with tab:
        st.subheader(f"{s['code']} {s['name']}")
        for f in FORMULAS.get(s["code"], []):
            with st.container(border=True):
                head = f"**{f['title']}**"
                if f["clause"]:
                    head += f" · `{f['clause']}`"
                if f["verify"]:
                    head += " · :orange[⚠ verify against Singapore NA]"
                st.markdown(head)
                st.latex(f["latex"])
                if f["note"]:
                    st.caption(f["note"])
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
