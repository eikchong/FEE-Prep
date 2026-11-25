"""Smoke-test: every page renders without exceptions (Streamlit AppTest)."""
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
VIEWS = sorted((ROOT / "views").glob("[!_]*.py"))


@pytest.mark.parametrize("view", [v for v in VIEWS if v.name != "library.py"], ids=lambda v: v.stem)
def test_view_renders(view):
    """Each page runs inside the app's navigation (pages use st.page_link, which needs registered pages)."""
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=90).run()
    at.switch_page(f"views/{view.name}").run()
    assert not at.exception, at.exception


def test_app_entry():
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=60).run()
    assert not at.exception, at.exception
    assert any(t.value == "Study" for t in at.title)
    assert "days" in " ".join(m.value for m in at.markdown)


def test_switch_pages():
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=60).run()
    for v in VIEWS:
        if v.name == "library.py":   # hidden when materials/ has no PDFs (as in the test environment)
            continue
        at.switch_page(f"views/{v.name}").run()
        assert not at.exception, (v.name, at.exception)


def test_subject_page_renders_with_questions():
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=90)
    at.query_params["s"] = "CE104"
    at.run()
    assert not at.exception, at.exception
    assert any("CE104" in t.value for t in at.title)
    assert any(e.label == "Show answer" for e in at.expander)
