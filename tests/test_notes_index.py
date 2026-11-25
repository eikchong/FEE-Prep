import json
from pathlib import Path

from utils.notes_index import OUT_PATH, build, section_keys
from utils.study_notes import STUDY

ROOT = Path(__file__).resolve().parents[1]


def _build():
    return build(STUDY, json.loads((ROOT / "data/lecture_outlines.json").read_text()),
                 json.loads((ROOT / "data/syllabus.json").read_text()))


def test_every_section_placed_or_excluded():
    idx = _build()
    placed, excl = set(idx["sections"]), {e["key"] for e in idx["excluded"]}
    assert not placed & excl
    for d, doc in STUDY.items():
        for k in section_keys(d, doc["sections"]):
            assert k in placed or k in excl, k
    # only course-info and wood are left out; nothing is silently unplaced
    assert not [e for e in idx["excluded"] if e["reason"].startswith("unplaced")]


def test_each_section_once_and_keys_stable():
    idx = _build()
    seen = [k for t in idx["topics"].values() for k in t["lecture"] + t["practice"]]
    assert len(seen) == len(set(seen)) == len(idx["sections"])


def test_generated_file_is_current():
    assert json.loads(OUT_PATH.read_text()) == json.loads(json.dumps(_build())), \
        "run python scripts/build_notes_by_topic.py"


def test_covered_in_and_practice_group():
    idx = _build()
    assert idx["topics"]["CE104-09"]["covered_in"] == ["CE104-06", "CE104-08"]
    shear = idx["topics"]["CE104-05"]
    assert shear["lecture"] and shear["practice"]
    assert all(idx["sections"][k]["kind"] == "practice" for k in shear["practice"])
