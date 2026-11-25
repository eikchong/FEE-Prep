"""Session-state bootstrap + shared sidebar. Every view calls `init()` so pages also run
standalone (handy for tests)."""
from __future__ import annotations

import uuid
from datetime import date, datetime

import streamlit as st

import config
from utils import storage
from utils.syllabus import subjects


def init() -> dict:
    if "progress" not in st.session_state:
        st.session_state.store = storage.get_storage()
        st.session_state.progress = st.session_state.store.load()
        try:
            from utils.reading import migrate_notes_read
            if migrate_notes_read(st.session_state.progress):
                save()
        except Exception:
            pass
    return st.session_state.progress


def progress() -> dict:
    return init()


def save(force: bool = False) -> None:
    st.session_state.store.save(st.session_state.progress, force=force)


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


def log_study_time_form() -> None:
    """Manual study-time entry (reading time on Study pages is logged automatically)."""
    p = init()
    with st.form("log_study", clear_on_submit=True, border=True):
        st.markdown("**Log study time**")
        c1, c2, c3 = st.columns([1, 1, 1])
        dt = c1.date_input("Date", value=date.today(), max_value=date.today())
        mins = c2.number_input("Minutes", 5, 600, 60, step=15)
        codes = ["General"] + [s["code"] for s in subjects()]
        code = c3.selectbox("Subject", codes)
        note = st.text_input("Note", placeholder="optional")
        if st.form_submit_button("Log", width="stretch"):
            p["study_log"].append({"date": dt.isoformat(), "minutes": int(mins), "code": code, "note": note})
            save()
            st.toast(f"Logged {mins} min")
