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


def topic_state(progress: dict, tid: str) -> dict:
    st = progress["topics"].get(tid, {})
    return {"status": st.get("status", config.STATUSES[0]),
            "confidence": int(st.get("confidence", 0) or 0),
            "notes": st.get("notes", "") or ""}


def chosen_part2(settings: dict) -> list[str]:
    return sorted(set(settings.get("part2_core", [])) | set(settings.get("part2_backup", [])))


def focus_codes(settings: dict) -> list[str]:
    """Part 1 subjects + Part 2 subjects the candidate intends to answer."""
    return config.PART1_CODES + chosen_part2(settings)


def readiness_by_subject(progress: dict) -> dict[str, float]:
    out = {}
    for s in subjects():
        confs = [topic_state(progress, t["id"])["confidence"] for t in s["topics"]]
        out[s["code"]] = (sum(confs) / len(confs) / 5) if confs else 0.0
    return out


def overall_readiness(progress: dict) -> float:
    codes = focus_codes(progress["settings"])
    confs = [topic_state(progress, t["id"])["confidence"]
             for c in codes for t in subject_map()[c]["topics"]]
    return sum(confs) / len(confs) / 5 if confs else 0.0
