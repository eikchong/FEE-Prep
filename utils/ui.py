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
