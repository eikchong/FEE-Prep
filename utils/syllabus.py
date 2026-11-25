"""Syllabus lookups shared by all pages."""
from __future__ import annotations

from functools import lru_cache

import config
from utils.storage import load_static


@lru_cache(maxsize=1)
def syllabus() -> dict:
    return load_static("syllabus.json")


def subjects(part: int | None = None) -> list[dict]:
    return [s for s in syllabus()["subjects"] if part is None or s["part"] == part]


@lru_cache(maxsize=1)
def subject_map() -> dict[str, dict]:
    return {s["code"]: s for s in syllabus()["subjects"]}


@lru_cache(maxsize=1)
def topic_map() -> dict[str, dict]:
    out = {}
    for s in syllabus()["subjects"]:
        for t in s["topics"]:
            out[t["id"]] = {**t, "code": s["code"], "part": s["part"], "subject": s["name"]}
    return out


def all_topics() -> list[dict]:
    return list(topic_map().values())


def subject_label(code: str) -> str:
    s = subject_map().get(code)
    return f"{code} {s['name']}" if s else code


def topic_label(tid: str) -> str:
    t = topic_map().get(tid)
    return f"{tid} · {t['name']}" if t else tid


def chosen_part2(settings: dict) -> list[str]:
    return sorted(set(settings.get("part2_core", [])) | set(settings.get("part2_backup", [])))


def focus_codes(settings: dict) -> list[str]:
    """Part 1 subjects + Part 2 subjects the candidate intends to answer."""
    return config.PART1_CODES + chosen_part2(settings)


def mcq_accuracy(progress: dict) -> dict[str, float | None]:
    """Subject → share of MCQ attempts answered correctly (None when not attempted)."""
    out: dict[str, list[int]] = {}
    for a in progress.get("mcq_attempts", []):
        out.setdefault(a["code"], []).append(1 if a["correct"] else 0)
    return {s["code"]: (sum(out[s["code"]]) / len(out[s["code"]]) if out.get(s["code"]) else None) for s in subjects()}


def topic_mcq_accuracy(progress: dict) -> dict[str, float]:
    from utils.storage import load_static
    topic_of = {q["id"]: q.get("topic") for q in load_static("mcq_bank.json") + progress.get("custom_mcqs", [])}
    agg: dict[str, list[int]] = {}
    for a in progress.get("mcq_attempts", []):
        t = topic_of.get(a["qid"])
        if t:
            agg.setdefault(t, []).append(1 if a["correct"] else 0)
    return {t: sum(v) / len(v) for t, v in agg.items()}


def readiness_by_subject(progress: dict) -> dict[str, float]:
    """Readiness = read % of the notes, averaged with MCQ accuracy where the subject has attempts."""
    from utils.reading import subject_stats
    acc = mcq_accuracy(progress)
    out = {}
    for s in subjects():
        r = subject_stats(progress, s["code"])["pct"]
        a = acc[s["code"]]
        out[s["code"]] = r if a is None else (r + a) / 2
    return out


def overall_readiness(progress: dict) -> float:
    rb = readiness_by_subject(progress)
    codes = focus_codes(progress["settings"])
    return sum(rb[c] for c in codes) / len(codes) if codes else 0.0
