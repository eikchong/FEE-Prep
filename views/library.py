from contextlib import closing
from pathlib import Path

import pandas as pd
import streamlit as st

import config
from utils import library
from utils.state import init, new_id, now_iso, save
from utils.syllabus import subject_label, subjects, topic_label, topic_map

p = init()
st.title("Library")
st.caption("Your lecture notes & references in `materials/`. Search, open at the hit page, and tag pages to sub-topics.")

con = library.connect()

# ---------------------------------------------------------------- toolbar
tb1, tb2 = st.columns([1, 2])
with tb1:
    if st.button("🔄 Re-scan materials", type="primary", use_container_width=True):
        bar = st.progress(0.0, text="Scanning…")
        rep = library.ingest(con=con, progress_cb=lambda f, n: bar.progress(f, text=n))
        bar.empty()
        st.session_state["lib_report"] = rep
    docs = library.documents(con)
    st.caption(f"{len(docs)} files · {sum(d['pages'] for d in docs)} pages indexed")
with tb2:
    with st.expander("⬆️ Add files to materials/"):
        dest = st.selectbox("Folder", [s["code"] for s in subjects()] + ["_general", "_unsorted"],
                            format_func=lambda c: subject_label(c) if c.startswith("CE") else c)
        ups = st.file_uploader("Files", accept_multiple_files=True,
                               type=[e.strip(".") for e in library.SUPPORTED])
        if ups and st.button("Save & re-scan"):
            for u in ups:
                target = config.MATERIALS_DIR / dest / Path(u.name).name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(u.getbuffer())
            st.session_state["lib_report"] = library.ingest(con=con)
            st.rerun()

rep = st.session_state.get("lib_report")
if rep:
    with st.expander(f"Last scan: {rep.summary()} · {len(rep.gaps)} sub-topics with no material", expanded=False):
        for path, err in rep.failed:
            st.error(f"{path}: {err}")
        if rep.ocr_missing:
            st.warning(f"{rep.ocr_missing} scanned page(s) had no extractable text. Install Tesseract "
                       "(`apt install tesseract-ocr` / `brew install tesseract`) and re-scan with rebuild.")
        st.write("**Coverage report — sub-topics with zero linked pages:**")
        st.write(", ".join(f"`{g}`" for g in rep.gaps) or "None 🎉")

counts = library.topic_page_counts(con)

left, centre, right = st.columns([1.1, 1.6, 2.2], gap="medium")

# ---------------------------------------------------------------- left: tree
with left:
    st.subheader("Browse")
    codes = [s["code"] for s in subjects()]
    default_code = st.session_state.get("lib_code")
    code = st.selectbox("Subject", [None] + codes, index=([None] + codes).index(default_code)
                        if default_code in codes else 0,
                        format_func=lambda c: "All subjects" if c is None else subject_label(c))
    st.session_state["lib_code"] = code
    if code:
        s = next(x for x in subjects() if x["code"] == code)
        tdf = pd.DataFrame([{"id": t["id"], "Sub-topic": t["name"],
                             "Pages": counts.get(t["id"], 0)} for t in s["topics"]])
        tdf["Material"] = tdf["Pages"].map(lambda n: f"{n} pages" if n else "no material yet")
        st.dataframe(tdf[["id", "Sub-topic", "Material"]], hide_index=True, use_container_width=True,
                     height=min(420, 36 * (len(tdf) + 1)))
        tids = [None] + tdf["id"].tolist()
        cur = st.session_state.get("lib_topic")
        topic = st.selectbox("Filter by sub-topic", tids, index=tids.index(cur) if cur in tids else 0,
                             format_func=lambda t: "All sub-topics" if t is None else topic_label(t))
    else:
        topic = None
    st.session_state["lib_topic"] = topic

# ---------------------------------------------------------------- centre: search
with centre:
    st.subheader("Search")
    q = st.text_input("Full-text search", placeholder='e.g. "lateral torsional" or Schmertmann',
                      key="lib_q")
    fpaths = [None] + [d["path"] for d in docs]
    fpath = st.selectbox("File", fpaths, format_func=lambda x: "All files" if x is None else x)
    results = library.search(con, q, code=code, topic_id=topic, path=fpath, limit=60) if docs else []
    if not docs:
        st.info("No materials indexed yet. Drop files into `materials/CE2xx/` (or upload above) and click **Re-scan**.")
    elif not results:
        st.write("No matching pages.")
    for i, r in enumerate(results):
        with st.container(border=True):
            st.markdown(f"**{r['title']}** · p. {r['page_no']}" + (" · _OCR_" if r["ocr"] else "")
                        + f"  \n<small>{r['path']}</small>", unsafe_allow_html=True)
            st.markdown(f"<small>…{r['snippet']}…</small>" if not q else r["snippet"].replace("\n", " "),
                        unsafe_allow_html=True)
            if st.button("Open", key=f"open_{i}_{r['path']}_{r['page_no']}"):
                st.session_state["lib_sel"] = (r["path"], r["page_no"])

# ---------------------------------------------------------------- right: viewer
with right:
    sel = st.session_state.get("lib_sel")
    if not sel and results:
        sel = (results[0]["path"], results[0]["page_no"])
    if not sel or not any(d["path"] == sel[0] for d in docs):
        st.subheader("Viewer")
        st.caption("Open a search result to view it here.")
    else:
        path, page_no = sel
        doc = next(d for d in docs if d["path"] == path)
        st.subheader(f"{doc['title']}")
        nav1, nav2, nav3 = st.columns([1, 2, 1])
        if nav1.button("◀", disabled=page_no <= 1, use_container_width=True):
            st.session_state["lib_sel"] = (path, page_no - 1)
            st.rerun()
        nav2.markdown(f"<div style='text-align:center'>page <b>{page_no}</b> / {doc['pages']}</div>",
                      unsafe_allow_html=True)
        if nav3.button("▶", disabled=page_no >= doc["pages"], use_container_width=True):
            st.session_state["lib_sel"] = (path, page_no + 1)
            st.rerun()

        fp = library.abs_path(path)
        ext = fp.suffix.lower()
        if ext == ".pdf" and fp.exists():
            try:
                from streamlit_pdf_viewer import pdf_viewer
                pdf_viewer(str(fp), height=620, pages_to_render=[page_no], key=f"pdf_{path}_{page_no}")
            except Exception:
                import pymupdf
                with pymupdf.open(fp) as d:
                    st.image(d[page_no - 1].get_pixmap(dpi=110).tobytes("png"), use_container_width=True)
        elif ext in (".png", ".jpg", ".jpeg") and fp.exists():
            st.image(str(fp), use_container_width=True)
        text = library.page_text(con, path, page_no)
        with st.expander("Extracted text", expanded=ext not in (".pdf", ".png", ".jpg", ".jpeg")):
            st.text(text[:6000] or "(no text)")

        # tag editor
        st.markdown("**Sub-topic tags** (manual edits override auto-tags)")
        tags = library.page_tags(con, path, page_no)
        cur_ids = [t["topic_id"] for t in tags]
        new_ids = st.multiselect("Tags", list(topic_map()), default=cur_ids, format_func=topic_label,
                                 key=f"tags_{path}_{page_no}", label_visibility="collapsed")
        if tags:
            def _src(t):
                return "manual" if t["manual"] else "auto {:.0%}".format(t["confidence"])
            st.caption(" · ".join(f"{t['topic_id']} ({_src(t)})" for t in tags))
        if sorted(new_ids) != sorted(cur_ids):
            library.set_page_tags(con, path, page_no, new_ids)
            st.toast("Tags saved")
            st.rerun()

        # actions
        a1, a2 = st.columns(2)
        with a1.popover("📌 Pin to formula sheet", use_container_width=True):
            pin_topic = st.selectbox("Sub-topic", cur_ids or list(topic_map()), format_func=topic_label,
                                     key="pin_topic")
            excerpt = st.text_area("Excerpt", value=text.strip()[:400], height=150, key="pin_ex")
            if st.button("Pin", key="pin_go"):
                p["pins"].append({"id": new_id(), "code": pin_topic.split("-")[0], "topic_id": pin_topic,
                                  "doc": path, "page": page_no, "excerpt": excerpt, "ts": now_iso()})
                save()
                st.toast("Pinned to formula sheet")
        if a2.button("❓ Make a question from this page", use_container_width=True):
            st.session_state["new_q_source"] = {"doc": path, "page": page_no,
                                                "topic": cur_ids[0] if cur_ids else None}
            st.switch_page("views/mcq.py")

con.close()
