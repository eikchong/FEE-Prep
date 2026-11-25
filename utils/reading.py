"""Reading progress: word-weighted, built on data/notes_by_topic.json.

progress["read"]    = {section_key: "YYYY-MM-DD"}   (added by scrolling; never removed by scrolling)
progress["revisit"] = {topic_id: "YYYY-MM-DD"}

Topic % = read words / topic words; a topic is "Read" at >= 95 %. Subject and overall % are word-weighted
the same way (only topics that have notes count). Tutorial questions count by their question text only — a
hidden answer never counts and opening it marks nothing.
"""
from __future__ import annotations

from datetime import date
from functools import lru_cache

from utils.latex_plain import to_plain
from utils.notes_index import index, section_keys
from utils.syllabus import subject_map, subjects

READ_WPM = 120
READ_AT = 0.95
EQ_WORDS = 6


def block_words(b) -> int:
    k = b[0]
    if k in ("md", "tip"):
        return len(to_plain(b[1]).split())
    if k == "ex":
        return len(to_plain(b[1]).split()) + len(to_plain(b[2]).split())
    if k == "steps":
        return sum(len(to_plain(t).split()) for t in b[1])
    if k == "eq":
        return EQ_WORDS
    if k == "q":
        return len(to_plain(b[1]["question"]).split()) + 3
    return 0


@lru_cache(maxsize=1)
def _study():
    from utils.study_notes import STUDY
    return STUDY


@lru_cache(maxsize=1)
def section_words() -> dict[str, int]:
    out = {}
    for key, s in index()["sections"].items():
        sec = _study()[s["doc"]]["sections"][s["idx"]]
        out[key] = max(1, sum(block_words(b) for b in sec["blocks"]))
    return out


def topic_sections(tid: str) -> list[str]:
    t = index()["topics"].get(tid, {})
    return list(t.get("lecture", [])) + list(t.get("practice", []))


def topic_words(tid: str) -> int:
    w = section_words()
    return sum(w[k] for k in topic_sections(tid))


def read_words(progress: dict, keys) -> int:
    read, w = progress.get("read", {}), section_words()
    return sum(w[k] for k in keys if k in read)


def topic_stats(progress: dict, tid: str) -> dict:
    keys = topic_sections(tid)
    total = sum(section_words()[k] for k in keys)
    done = read_words(progress, keys)
    t = index()["topics"].get(tid, {})
    pct = done / total if total else 0.0
    if not keys:
        status = "covered" if t.get("covered_in") else "none"
    elif pct >= READ_AT:
        status = "read"
    elif done:
        status = "reading"
    else:
        status = "not_started"
    dates = [progress["read"][k] for k in keys if k in progress.get("read", {})]
    return {"words": total, "read_words": done, "pct": pct, "status": status,
            "minutes": total / READ_WPM, "minutes_left": max(0, total - done) / READ_WPM,
            "n_lecture": len(t.get("lecture", [])), "n_practice": len(t.get("practice", [])),
            "covered_in": t.get("covered_in", []), "revisit": tid in progress.get("revisit", {}),
            "last_read": max(dates) if dates else None}


def subject_stats(progress: dict, code: str) -> dict:
    tids = [t["id"] for t in subject_map()[code]["topics"]]
    ts = {tid: topic_stats(progress, tid) for tid in tids}
    with_notes = [t for t in tids if ts[t]["words"]]
    total = sum(ts[t]["words"] for t in with_notes)
    done = sum(ts[t]["read_words"] for t in with_notes)
    dates = [ts[t]["last_read"] for t in tids if ts[t]["last_read"]]
    return {"topics": ts, "n_topics": len(tids), "n_with_notes": len(with_notes),
            "n_read": sum(ts[t]["status"] == "read" for t in with_notes),
            "n_no_notes": sum(ts[t]["status"] == "none" for t in tids),
            "words": total, "read_words": done, "pct": done / total if total else 0.0,
            "minutes": total / READ_WPM, "minutes_left": max(0, total - done) / READ_WPM,
            "last_read": max(dates) if dates else None, "has_notes": bool(with_notes)}


def overall_stats(progress: dict) -> dict:
    ss = {s["code"]: subject_stats(progress, s["code"]) for s in subjects()}
    total = sum(v["words"] for v in ss.values())
    done = sum(v["read_words"] for v in ss.values())
    return {"subjects": ss, "pct": done / total if total else 0.0,
            "n_topics_with_notes": sum(v["n_with_notes"] for v in ss.values()),
            "n_topics_read": sum(v["n_read"] for v in ss.values()),
            "n_without_notes": sum(not v["has_notes"] for v in ss.values())}


def continue_target(progress: dict, code: str | None = None) -> tuple[str, str, str] | None:
    """(code, topic id, first unread section key) — most recently read subject when code is None."""
    if code is None:
        best = None
        for s in subjects():
            st_ = subject_stats(progress, s["code"])
            if st_["last_read"] and (best is None or st_["last_read"] > best[1]):
                best = (s["code"], st_["last_read"])
        code = best[0] if best else next((s["code"] for s in subjects() if subject_stats(progress, s["code"])["has_notes"]), None)
        if code is None:
            return None
    read = progress.get("read", {})
    for t in subject_map()[code]["topics"]:
        keys = topic_sections(t["id"])
        if not keys or topic_stats(progress, t["id"])["status"] == "read":
            continue
        k = next((k for k in keys if k not in read), keys[0])
        return code, t["id"], k
    return None


def topic_number(tid: str) -> int:
    return int(tid.split("-")[1])


def mark_read(progress: dict, keys, today: str | None = None) -> list[str]:
    """Add keys (never removes). Returns the keys that were new."""
    today = today or date.today().isoformat()
    read = progress.setdefault("read", {})
    valid = section_words()
    new = [k for k in keys if k in valid and k not in read]
    for k in new:
        read[k] = today
    return new


def mark_topic_unread(progress: dict, tid: str) -> None:
    read = progress.setdefault("read", {})
    for k in topic_sections(tid):
        read.pop(k, None)


def completed_topics(progress: dict, before: dict, keys) -> list[str]:
    """Topics that crossed the 95 % line because of `keys` (before = read dict prior to the update)."""
    tids = {index()["sections"][k]["topic"] for k in keys if k in index()["sections"]}
    out = []
    for tid in tids:
        total = topic_words(tid)
        prev = sum(section_words()[k] for k in topic_sections(tid) if k in before)
        now = read_words(progress, topic_sections(tid))
        if total and prev / total < READ_AT <= now / total:
            out.append(tid)
    return out


def migrate_notes_read(progress: dict) -> bool:
    """Old per-doc section indices → stable read keys (once)."""
    old = progress.get("notes_read") or {}
    if not old or progress.get("_migrated_notes_read"):
        return False
    today = date.today().isoformat()
    read = progress.setdefault("read", {})
    for doc, idxs in old.items():
        d = _study().get(doc)
        if not d:
            continue
        keys = section_keys(doc, d["sections"])
        for i in idxs:
            if 0 <= i < len(keys) and keys[i] in section_words():
                read.setdefault(keys[i], today)
    progress["_migrated_notes_read"] = True
    return True
