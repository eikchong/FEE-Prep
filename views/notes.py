import streamlit as st

from utils import library
from utils.state import init, save
from utils.study_notes import STUDY, TUTORIALS
from utils.syllabus import subject_label
from utils.ui import open_in_library, show_pdf_page

p = init()
st.title("Study notes")
st.caption("Condensed notes from your CE1101 text notes, in the same order as the notes. "
           "Read here; open the original page only if you need a figure.")

read = p.setdefault("notes_read", {})          # doc path -> [studied section indices]
ol = library.outlines()
docs = sorted(STUDY, key=lambda d: (STUDY[d]["code"], ol.get(d, {}).get("seq", 99), d))
codes = list(dict.fromkeys(STUDY[d]["code"] for d in docs))

c1, c2 = st.columns([1, 3])
code = c1.selectbox("Subject", codes, format_func=subject_label, key="sn_code")
cdocs = [d for d in docs if STUDY[d]["code"] == code]


def doc_label(d):
    n = len(STUDY[d]["sections"])
    k = len(set(read.get(d, [])) & set(range(n)))
    return f"{STUDY[d]['title']}  ({k}/{n} ✓)"


doc = c2.selectbox("Notes", cdocs, format_func=doc_label, key=f"sn_doc_{code}")
secs = STUDY[doc]["sections"]
done = set(read.get(doc, []))
st.progress(len(done & set(range(len(secs)))) / len(secs),
            text=f"{len(done & set(range(len(secs))))}/{len(secs)} sections studied")

skey = f"sn_sec_{doc}"
cur = min(st.session_state.get(skey, next((i for i in range(len(secs)) if i not in done), 0)), len(secs) - 1)

with st.sidebar:
    st.markdown(f"**{STUDY[doc]['title']}**")
    for i, s in enumerate(secs):
        mark = "✅" if i in done else ("▶️" if i == cur else "·")
        if st.button(f"{mark} {s['title']}", key=f"sn_toc_{doc}_{i}", width="stretch"):
            st.session_state[skey] = i
            st.rerun()


def render(block):
    kind = block[0]
    if kind == "md":
        st.markdown(block[1])
    elif kind == "eq":
        st.latex(block[1])
    elif kind == "steps":
        st.markdown("\n".join(f"{i}. {t}" for i, t in enumerate(block[1], 1)))
    elif kind == "ex":
        with st.container(border=True):
            st.markdown(f"**📘 {block[1]}**  \n{block[2]}")
    elif kind == "tip":
        st.info(block[1], icon="💡")
    elif kind == "tut":
        st.markdown(f"✏️ **Practice:** {block[1]}")


sec = secs[cur]
st.subheader(f"{cur + 1}. {sec['title']}")
for b in sec["blocks"]:
    render(b)

a, z = sec["pages"]
fp = library.abs_path(doc)
with st.expander(f"📄 Original pages {a}–{z}" + ("" if fp.exists() else " (file not on this machine)")):
    if fp.exists():
        pg = st.number_input("Page", a, z, a, key=f"sn_pg_{doc}_{cur}")
        show_pdf_page(fp, int(pg), key=f"sn_pdf_{doc}_{pg}", height=600)
        if st.button("Open in Library", key=f"sn_lib_{doc}_{cur}"):
            open_in_library(doc, int(pg))
    else:
        st.caption("Add the PDF to materials/ (or upload in the Library) to view the original slides.")

st.divider()
n1, n2, n3 = st.columns([1, 2, 1])
if n1.button("◀ Previous", disabled=cur == 0, width="stretch", key="sn_prev"):
    st.session_state[skey] = cur - 1
    st.rerun()
studied = n2.toggle("Studied ✓", value=cur in done, key=f"sn_done_{doc}_{cur}")
if studied != (cur in done):
    read[doc] = sorted(done ^ {cur})
    save()
    st.rerun()
if n3.button("Next ▶", disabled=cur >= len(secs) - 1, width="stretch", key="sn_next", type="primary"):
    if cur not in done:
        read[doc] = sorted(done | {cur})
        save()
    st.session_state[skey] = cur + 1
    st.rerun()

tuts = [t for t in TUTORIALS if t[3] == doc]
if tuts:
    with st.expander(f"✏️ Tutorial questions for this module ({len(tuts)})"):
        for tdoc, page, title, _ in tuts:
            c, b = st.columns([4, 1])
            c.markdown(f"**{tdoc.split('_T2L_')[-1].replace('.pdf', '').replace('_', ' ')}** — {title}")
            if library.abs_path(tdoc).exists() and b.button("Open", key=f"sn_t_{tdoc}_{page}"):
                open_in_library(tdoc, page)
