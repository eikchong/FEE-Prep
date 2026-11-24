import streamlit as st

from utils import library
from utils.notes import clean_text, documents_for
from utils.state import init, save
from utils.syllabus import subject_label, subjects
from utils.ui import show_pdf_page

p = init()
st.title("Study notes")
st.caption("Your lecture notes in lecture order — cleaned text beside the original page. "
           "Read from `materials/` on this machine (not stored in the repo).")

con = library.connect()
docs_db = library.documents(con)
read = p.setdefault("notes_read", {})          # path -> [section indices studied]

codes = [s["code"] for s in subjects()]
avail = {c: documents_for(c, docs_db) for c in codes}
with_notes = [c for c in codes if avail[c]]
if not with_notes:
    st.info("No notes indexed yet. Put PDFs in `materials/<subject>/` and click **Re-scan** in the Library.")
    st.stop()

c1, c2, c3 = st.columns([2, 3, 1])
code = c1.selectbox("Subject", with_notes, format_func=subject_label, key="nt_code")
docs = avail[code]
dlabels = [f"{i + 1}. {d['title']}" for i, d in enumerate(docs)]
di = c2.selectbox("Document", range(len(docs)), format_func=lambda i: dlabels[i], key=f"nt_doc_{code}")
doc = docs[di]
mode = c3.radio("Show", ["Text + page", "Text", "Page"], key="nt_mode",
                index=0)

secs = doc["sections"]
done = set(read.get(doc["path"], []))
st.progress(len(done & set(range(len(secs)))) / len(secs),
            text=f"{len(done & set(range(len(secs))))}/{len(secs)} sections studied")

skey = f"nt_sec_{doc['path']}"
cur = st.session_state.get(skey, next((i for i in range(len(secs)) if i not in done), 0))
cur = min(cur, len(secs) - 1)

with st.sidebar:
    st.markdown(f"**Sections — {doc['title'][:40]}**")
    for i, s in enumerate(secs):
        mark = "✅" if i in done else ("▶️" if i == cur else "·")
        if st.button(f"{mark} {s['title'][:48]}", key=f"nt_toc_{doc['path']}_{i}", width="stretch"):
            st.session_state[skey] = i
            st.rerun()

sec = secs[cur]
a, b = sec["pages"]
st.subheader(f"{cur + 1}. {sec['title']}")
st.caption(f"{doc['path'].split('/')[-1]} · pages {a}–{b}")

nav = st.columns([1, 1, 2, 1, 1])
if nav[0].button("◀ Previous", disabled=cur == 0, width="stretch", key="nt_prev"):
    st.session_state[skey] = cur - 1
    st.rerun()
studied = nav[2].toggle("Studied ✓", value=cur in done, key=f"nt_done_{doc['path']}_{cur}")
if studied != (cur in done):
    s_ = set(read.get(doc["path"], []))
    s_.symmetric_difference_update({cur})
    read[doc["path"]] = sorted(s_)
    save()
    st.rerun()
if nav[4].button("Next ▶", disabled=cur >= len(secs) - 1, width="stretch", key="nt_next"):
    st.session_state[skey] = cur + 1
    st.rerun()

fp = library.abs_path(doc["path"])
for pg in range(a, b + 1):
    text = clean_text(library.page_text(con, doc["path"], pg))
    st.markdown(f"##### Page {pg}")
    if mode == "Text + page":
        t, im = st.columns([1, 1])
    else:
        t = im = st.container()
    if mode in ("Text + page", "Text"):
        with t:
            st.markdown(text.replace("\n", "  \n") if text.strip() else "_(no text on this page — see the image)_")
    if mode in ("Text + page", "Page") and fp.exists():
        with im:
            show_pdf_page(fp, pg, key=f"nt_pdf_{doc['path']}_{pg}", height=560)
    st.divider()

if cur < len(secs) - 1 and st.button("Next section ▶", key="nt_next_bottom", type="primary"):
    if cur not in done:
        read[doc["path"]] = sorted(done | {cur})
        save()
    st.session_state[skey] = cur + 1
    st.rerun()
con.close()
