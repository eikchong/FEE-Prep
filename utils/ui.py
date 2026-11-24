"""Small shared UI helpers."""
from __future__ import annotations

import time

import streamlit as st

import config
from utils.syllabus import subject_map


def pill(text: str, color: str) -> str:
    return (f"<span style='background:{color}1a;color:{color};border:1px solid {color}55;"
            f"border-radius:999px;padding:2px 10px;margin:2px;display:inline-block;"
            f"font-size:0.85rem;font-weight:600'>{text}</span>")


def part_color(code: str) -> str:
    return config.COLOR_P1 if subject_map()[code]["part"] == 1 else config.COLOR_P2


def fmt_mmss(sec: float) -> str:
    sec = int(max(0, sec))
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def countdown(key: str, total_sec: int, label: str = "Time left") -> None:
    """Live countdown driven by st.session_state[key] = start epoch (or None)."""
    @st.fragment(run_every=1)
    def _tick():
        start = st.session_state.get(key)
        if not start:
            return
        el = time.time() - start
        left = total_sec - el
        if left > 0:
            frac = min(1.0, el / total_sec)
            st.progress(frac, text=f"⏱️ {label}: **{fmt_mmss(left)}** · elapsed {fmt_mmss(el)}")
        else:
            st.error(f"⏰ Time up — {fmt_mmss(-left)} over")
    _tick()


def open_in_library(path: str | None = None, page: int | None = None, topic: str | None = None,
                    code: str | None = None) -> None:
    st.session_state["lib_sel"] = (path, page) if path else st.session_state.get("lib_sel")
    if topic:
        st.session_state["lib_topic"] = topic
        st.session_state["lib_code"] = topic.split("-")[0]
    elif code:
        st.session_state["lib_code"] = code
        st.session_state["lib_topic"] = None
    st.switch_page("views/library.py")


try:
    import inspect as _inspect
    _HAS_ARROW = "delta_arrow" in _inspect.signature(st.metric).parameters
except Exception:  # pragma: no cover
    _HAS_ARROW = False


def metric(col, label, value, sub: str | None = None, help: str | None = None):
    """st.metric with a neutral sub-caption (no coloured arrow) on any Streamlit ≥1.40."""
    kw = {"help": help}
    if sub is not None:
        kw.update(delta=sub, delta_color="off")
        if _HAS_ARROW:
            kw["delta_arrow"] = "off"
    col.metric(label, value, **kw)


def rubric_form(key: str):
    """Part 2 self-marking rubric → (scores dict 0–4, score %)."""
    st.markdown("**Self-mark** (0 = absent · 4 = exam-perfect)")
    scores = {}
    cols = st.columns(len(config.RUBRIC))
    for c, (crit, wt) in zip(cols, config.RUBRIC.items()):
        scores[crit] = c.select_slider(f"{crit} ({wt}%)", options=[0, 1, 2, 3, 4], value=2, key=f"{key}_{crit}")
    pct = sum(scores[k] / 4 * w for k, w in config.RUBRIC.items())
    return scores, pct


def show_pdf_page(abs_path, page_no: int, key: str, height: int = 640) -> None:
    """Render one page of a local PDF (streamlit-pdf-viewer, falling back to a PyMuPDF image)."""
    try:
        from streamlit_pdf_viewer import pdf_viewer
        pdf_viewer(str(abs_path), height=height, pages_to_render=[page_no], key=key)
    except Exception:
        import pymupdf
        with pymupdf.open(abs_path) as d:
            st.image(d[page_no - 1].get_pixmap(dpi=110).tobytes("png"), width="stretch")
