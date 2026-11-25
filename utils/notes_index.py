"""Notes → syllabus topics.

Each STUDY section is placed once, under its *primary* topic: the topic of the lecture-outline section (same
doc) it overlaps most by page range (first listed on ties). Sections from tutorial/practice docs go into the
topic's "Tutorial questions" group. `build()` is pure (STUDY + outlines → dict) so the build script, the app
and the tests share it; the app reads the generated data/notes_by_topic.json.
"""
from __future__ import annotations

import json
import re
from functools import lru_cache

import config
from utils.latex_plain import to_plain

PRACTICE_RE = re.compile(r"Practice|Tut|Exam|Quiz|Assignment|Homework|Self-evaluation", re.I)
COURSE_DOC_RE = re.compile(r"course map|course outline|course information|\boutline\b", re.I)
COURSE_SEC_RE = re.compile(r"^(scope|part ii scope|scope of part 2|scope & references|parts & order|"
                           r"where .* fits|arrangements|syllabus & reading|course map)\b", re.I)
EXCLUDED_DOC_PARTS = ("12_wood",)
OUT_PATH = config.STATIC_DATA_DIR / "notes_by_topic.json"


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", to_plain(text).lower()).strip("-")
    return s[:60] or "section"


def section_keys(doc: str, sections: list[dict]) -> list[str]:
    """Stable keys f"{doc}::{slug(title)}"; a repeated title in one doc gets -2, -3 …"""
    seen: dict[str, int] = {}
    out = []
    for s in sections:
        base = slug(s["title"])
        seen[base] = seen.get(base, 0) + 1
        out.append(f"{doc}::{base}" + (f"-{seen[base]}" if seen[base] > 1 else ""))
    return out


def _overlap(a: list[int], b: list[int]) -> int:
    return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)


def is_practice(doc_title: str) -> bool:
    return bool(PRACTICE_RE.search(doc_title))


def build(study: dict, outlines: dict, syllabus: dict) -> dict:
    topic_ids = {t["id"]: (s["code"], i + 1) for s in syllabus["subjects"] for i, t in enumerate(s["topics"])}
    sections: dict[str, dict] = {}
    excluded: list[dict] = []
    docs = sorted(study, key=lambda d: (study[d]["code"], outlines.get(d, {}).get("seq", 999), d))
    for d in docs:
        doc = study[d]
        ol = outlines.get(d, {}).get("sections", [])
        for i, (key, s) in enumerate(zip(section_keys(d, doc["sections"]), doc["sections"])):
            base = {"doc": d, "idx": i, "title": s["title"], "pages": list(s["pages"])}
            if any(p in d for p in EXCLUDED_DOC_PARTS):
                excluded.append({"key": key, **base, "reason": "not examined (wood)"})
                continue
            if COURSE_DOC_RE.search(doc["title"]) and COURSE_SEC_RE.search(s["title"]):
                excluded.append({"key": key, **base, "reason": "course map / outline / course info"})
                continue
            best, best_ov, overlaps = None, 0, []
            for o in ol:
                ov = _overlap(s["pages"], o["pages"])
                if ov <= 0:
                    continue
                for t in o["topics"]:
                    if t in topic_ids and t not in overlaps:
                        overlaps.append(t)
                first = next((t for t in o["topics"] if t in topic_ids), None)
                if first and ov > best_ov:
                    best, best_ov = first, ov
            if best is None:
                excluded.append({"key": key, **base, "reason": "unplaced: no overlapping outline topic"})
                continue
            sections[key] = {**base, "topic": best, "overlaps": overlaps,
                             "kind": "practice" if is_practice(doc["title"]) else "lecture"}
    topics: dict[str, dict] = {}
    for s in syllabus["subjects"]:
        for t in s["topics"]:
            topics[t["id"]] = {"lecture": [], "practice": [], "covered_in": []}
    for key, s in sections.items():           # dict order = course order (docs sorted by seq)
        topics[s["topic"]][s["kind"]].append(key)
    for tid, tv in topics.items():
        if tv["lecture"] or tv["practice"]:
            continue
        hosts = []
        for s in sections.values():
            if tid in s["overlaps"] and s["topic"] != tid and s["topic"] not in hosts:
                hosts.append(s["topic"])
        tv["covered_in"] = sorted(hosts, key=lambda h: topic_ids[h][1])
    return {"sections": sections, "topics": topics, "excluded": excluded}


@lru_cache(maxsize=1)
def index() -> dict:
    return json.loads(OUT_PATH.read_text(encoding="utf-8"))


def topic_number(tid: str) -> int:
    return int(tid.split("-")[1])
