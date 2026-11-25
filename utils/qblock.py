"""Tutorial-question blocks: ("q", {...}).

A question is shown in full; its answer stays hidden until the reader opens "Show answer".

Fields: id, set (label such as "CSC A Q1"), question, answer (final answers first, in bold), working (steps),
figure (page reference + one-line description, if the question needs a figure), source {doc, page},
answer_source ("official" | "mine" | "claude" | "none"), checked (numbers recomputed in
tests/test_tutorial_answers.py). "none" = no answer yet (shown as "not provided yet", to be solved later).
"""
from __future__ import annotations

import re

SOURCE_LINE = {
    "official": "Answer from the tutorial solutions",
    "mine": "My solution",
    "claude": "Worked by Claude — numbers checked, please review",
    "claude_unchecked": "Worked by Claude — please review",
    "none": "Answer not provided yet — to be solved later",
}


def q(set_: str, question: str, answer: str, working: str = "", *, figure: str | None = None,
      page: int | None = None, src: str = "official", checked: bool = True, id: str | None = None) -> tuple:
    assert src in ("official", "mine", "claude", "none"), src
    if src == "none":
        answer, working = "", ""
    else:
        assert answer.strip(), f"{set_}: give an answer or src='none'"
    return ("q", {"id": id, "set": set_, "question": question, "answer": answer, "working": working,
                  "figure": figure, "source": {"doc": None, "page": page}, "answer_source": src,
                  "checked": checked})


def source_line(qd: dict) -> str:
    src = qd["answer_source"]
    if src == "claude" and not qd.get("checked"):
        src = "claude_unchecked"
    return SOURCE_LINE[src]


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def fill_sources(study: dict) -> None:
    """Fill each q block's source doc/page from the section it sits in, and give it a stable id."""
    for doc, d in study.items():
        stem = _slug(doc.rsplit("/", 1)[-1].rsplit(".", 1)[0])
        for s in d["sections"]:
            for b in s["blocks"]:
                if b[0] != "q":
                    continue
                qd = b[1]
                qd["source"]["doc"] = qd["source"]["doc"] or doc
                qd["source"]["page"] = qd["source"]["page"] or s["pages"][0]
                qd["id"] = qd["id"] or f"{stem}:{_slug(qd['set'])}"


def all_questions(study: dict):
    for doc, d in study.items():
        for i, s in enumerate(d["sections"]):
            for b in s["blocks"]:
                if b[0] == "q":
                    yield doc, i, b[1]
