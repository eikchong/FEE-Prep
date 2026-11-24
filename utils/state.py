"""Session-state bootstrap + shared sidebar. Every view calls `init()` so pages also run
standalone (handy for tests)."""
from __future__ import annotations

import uuid
from datetime import date, datetime

import streamlit as st

import config
from utils import storage
from utils.syllabus import overall_readiness, subjects


def init() -> dict:
    if "progress" not in st.session_state:
        st.session_state.store = storage.get_storage()
        st.session_state.progress = st.session_state.store.load()
    return st.session_state.progress


def progress() -> dict:
    return init()


def save() -> None:
    st.session_state.store.save(st.session_state.progress)


def new_id() -> str:
    return uuid.uuid4().hex[:10]


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def days_to_exam(today: date | None = None) -> int:
    return (config.EXAM_DATE - (today or date.today())).days


def all_mcqs() -> list[dict]:
    return storage.load_static("mcq_bank.json") + list(progress().get("custom_mcqs", []))


def part2_bank() -> list[dict]:
    return storage.load_static("part2_bank.json")


def sidebar() -> None:
    p = init()
    with st.sidebar:
        d = days_to_exam()
        st.markdown(f"### ⏳ {d} days to go" if d >= 0 else "### Exam done ✅")
        st.caption(f"FEE (Civil) · Wed {config.EXAM_DATE:%d %b %Y}")
        r = overall_readiness(p)
        st.progress(r, text=f"Readiness {r:.0%}")
        with st.expander("➕ Log study time", expanded=False):
            with st.form("log_study", clear_on_submit=True, border=False):
                dt = st.date_input("Date", value=date.today(), max_value=date.today())
                mins = st.number_input("Minutes", 5, 600, 60, step=15)
                codes = ["General"] + [s["code"] for s in subjects()]
                code = st.selectbox("Subject", codes)
                note = st.text_input("Note", placeholder="optional")
                if st.form_submit_button("Log", use_container_width=True):
                    p["study_log"].append({"date": dt.isoformat(), "minutes": int(mins),
                                           "code": code, "note": note})
                    save()
                    st.toast(f"Logged {mins} min")
