"""FEE 2027 (Civil) prep — entry point.  Run:  streamlit run app.py"""
import streamlit as st

import config
from utils.state import init

st.set_page_config(page_title="FEE 2027 Civil Prep", page_icon=":material/school:", layout="wide",
                   initial_sidebar_state="auto")

init()


def has_materials() -> bool:
    """The Library only makes sense where the PDFs are (hidden on the deployed site with an empty materials/)."""
    d = config.MATERIALS_DIR
    return d.exists() and any(d.rglob("*.pdf"))


tools = [
    st.Page("views/formulas.py", title="Formula & code sheet", icon=":material/function:", url_path="formulas"),
    st.Page("views/calculators.py", title="Calculators", icon=":material/calculate:", url_path="calculators"),
]
if has_materials():
    tools.append(st.Page("views/library.py", title="Library", icon=":material/local_library:", url_path="library"))
tools.append(st.Page("views/info.py", title="Exam info", icon=":material/info:", url_path="info"))

study = st.Page("views/study.py", title="Study", icon=":material/menu_book:", url_path="study")


def _root():
    """/ forwards to /study (keeping ?s=… etc.) so /study?s=CE104 is the one deep-linkable URL."""
    st.switch_page(study, query_params=dict(st.query_params))


pages = {
    "": [st.Page(_root, title="Home", url_path="home", default=True, visibility="hidden"), study],
    "Practice": [
        st.Page("views/mcq.py", title="MCQ drill", icon=":material/quiz:", url_path="mcq"),
        st.Page("views/part2.py", title="Part 2 workbook", icon=":material/edit_note:", url_path="part2"),
        st.Page("views/past_papers.py", title="Past papers", icon=":material/history_edu:", url_path="past-papers"),
        st.Page("views/mock.py", title="Mock exam", icon=":material/timer:", url_path="mock"),
    ],
    "Progress": [
        st.Page("views/dashboard.py", title="Dashboard", icon=":material/dashboard:", url_path="dashboard"),
        st.Page("views/planner.py", title="Study planner", icon=":material/calendar_month:", url_path="planner"),
        st.Page("views/errors.py", title="Error log", icon=":material/report:", url_path="errors"),
    ],
    "Tools": tools,
}

nav = st.navigation(pages, position="top")
nav.run()
