"""Every user-visible text field that may carry math, for the lint test and the KaTeX check.

text_fields() → (where, markdown text with $…$ math)
display_fields() → (where, LaTeX for st.latex)
"""
from __future__ import annotations

import json
from typing import Iterator

import config


def block_text_fields(b) -> list[tuple[str, str]]:
    k = b[0]
    if k in ("md", "tip", "tut"):
        return [(k, b[1])]
    if k == "ex":
        return [("ex.title", b[1]), ("ex.body", b[2])]
    if k == "steps":
        return [(f"steps.{i}", t) for i, t in enumerate(b[1])]
    if k == "q":
        q = b[1]
        out = [(f"q.{f}", q.get(f) or "") for f in ("set", "question", "answer", "working", "figure")]
        return [(w, t) for w, t in out if t]
    return []


def _study():
    from utils.study_notes import STUDY
    return STUDY


def text_fields() -> Iterator[tuple[str, str]]:
    for d, doc in _study().items():
        for i, s in enumerate(doc["sections"]):
            yield f"{d} §{i} title", s["title"]
            for j, b in enumerate(s["blocks"]):
                for w, t in block_text_fields(b):
                    yield f"{d} §{i}.{j} {w}", t
    from utils.formulas import FORMULAS
    from utils.formulas_notes import NOTES_LEGACY, NOTES_SECTIONS
    for code, items in FORMULAS.items():
        for f in items:
            yield f"formulas {code} {f['title']}", f["title"]
            yield f"formulas {code} {f['title']} note", f["note"]
    for code, secs in NOTES_SECTIONS.items():
        for s in secs:
            yield f"formulas_notes {code} section", s["title"]
            for f in s["items"]:
                yield f"formulas_notes {code} {f['title']}", f["title"]
                yield f"formulas_notes {code} {f['title']} note", f["note"]
    for code, items in NOTES_LEGACY.items():
        for f in items:
            yield f"formulas_notes legacy {code}", f["title"]
            yield f"formulas_notes legacy {code} note", f["note"]
    for name, rows in _banks():
        for where, t in rows:
            yield f"{name} {where}", t


def _banks():
    def load(n):
        return json.loads((config.STATIC_DATA_DIR / n).read_text(encoding="utf-8"))
    mcq = load("mcq_bank.json")
    yield "mcq_bank", [(f"{q['id']}.{k}", q[k]) for q in mcq for k in ("q", "explain")] + \
        [(f"{q['id']}.opt{i}", o) for q in mcq for i, o in enumerate(q["options"])]
    p2 = load("part2_bank.json")
    yield "part2_bank", [(f"{q['id']}.{k}", q[k]) for q in p2 for k in ("title", "prompt") if k in q] + \
        [(f"{q['id']}.approach{i}", a) for q in p2 for i, a in enumerate(q.get("approach", []))]
    pp = load("past_papers.json")
    rows = []
    for part in ("part1", "part2"):
        for q in pp[part]:
            for k in ("title", "explain", "prompt", "q"):
                if isinstance(q.get(k), str):
                    rows.append((f"{q['id']}.{k}", q[k]))
            rows += [(f"{q['id']}.approach{i}", a) for i, a in enumerate(q.get("approach", []))]
            rows += [(f"{q['id']}.opt{i}", o) for i, o in enumerate(q.get("options", []))]
    yield "past_papers", rows


def display_fields() -> Iterator[tuple[str, str]]:
    for d, doc in _study().items():
        for i, s in enumerate(doc["sections"]):
            for j, b in enumerate(s["blocks"]):
                if b[0] == "eq":
                    yield f"{d} §{i}.{j} eq", b[1]
    from utils.formulas import FORMULAS
    from utils.formulas_notes import NOTES_LEGACY, NOTES_SECTIONS
    items = [f for v in FORMULAS.values() for f in v] + \
        [f for secs in NOTES_SECTIONS.values() for s in secs for f in s["items"]] + \
        [f for v in NOTES_LEGACY.values() for f in v]
    for f in items:
        if f.get("latex"):
            yield f"formula {f['title']}", f["latex"]
