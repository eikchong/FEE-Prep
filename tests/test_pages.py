"""Smoke-test: every page renders without exceptions (Streamlit AppTest)."""
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
VIEWS = sorted((ROOT / "views").glob("[!_]*.py"))


@pytest.mark.parametrize("view", VIEWS, ids=[v.stem for v in VIEWS])
def test_view_renders(view):
    at = AppTest.from_file(str(view), default_timeout=60).run()
    assert not at.exception, at.exception


def test_app_entry():
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=60).run()
    assert not at.exception, at.exception
    assert "days to go" in " ".join(m.value for m in at.sidebar.markdown)


def test_switch_pages():
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=60).run()
    for v in VIEWS:
        at.switch_page(f"views/{v.name}").run()
        assert not at.exception, (v.name, at.exception)
