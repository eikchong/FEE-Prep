"""FEE 2027 (Civil) prep — entry point.  Run:  streamlit run app.py"""
import streamlit as st

from utils.state import init, sidebar

st.set_page_config(page_title="FEE 2027 Civil Prep", page_icon="📐", layout="wide",
                   initial_sidebar_state="auto")

init()

pages = {
    "Overview": [
        st.Page("views/dashboard.py", title="Dashboard", icon="🏠", default=True),
    ],
    "Study": [
        st.Page("views/syllabus.py", title="Syllabus tracker", icon="✅", url_path="syllabus"),
        st.Page("views/notes.py", title="Study notes", icon="📖", url_path="notes"),
        st.Page("views/library.py", title="Library", icon="📚", url_path="library"),
        st.Page("views/planner.py", title="Study planner", icon="🗓️", url_path="planner"),
        st.Page("views/formulas.py", title="Formula & code sheet", icon="📐", url_path="formulas"),
        st.Page("views/calculators.py", title="Quick calculators", icon="🧮", url_path="calculators"),
    ],
    "Practice": [
        st.Page("views/mcq.py", title="Part 1 MCQ drill", icon="🎯", url_path="mcq"),
        st.Page("views/part2.py", title="Part 2 workbook", icon="📝", url_path="part2"),
        st.Page("views/past_papers.py", title="Past papers", icon="🗂️", url_path="past-papers"),
        st.Page("views/mock.py", title="Mock exam", icon="⏱️", url_path="mock"),
    ],
    "Review": [
        st.Page("views/errors.py", title="Error log & analytics", icon="📈", url_path="errors"),
        st.Page("views/info.py", title="Exam info & reading list", icon="ℹ️", url_path="info"),
    ],
}

nav = st.navigation(pages)
sidebar()
nav.run()
