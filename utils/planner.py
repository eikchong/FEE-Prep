"""Day-by-day study plan generator (pure, unit-tested).

Rules (brief §5.3):
* plan runs from start date to the day before the exam (never on/after exam day)
* sub-topic weight = subject weight × max(floor, 1 − confidence/5)
* Part 2 subjects not in core/backup get zero weight
* final MOCK_DAYS days = mocks + error-log review
* every day has a 30-min Part 1 MCQ block rotating CE101–CE105
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, asdict
from datetime import date, timedelta

import config

MOCK_SEQUENCE = [
    ("Mock", "Part 1 mock (40 MCQ, timed)"),
    ("Review", "Error-log review + formula binder tabbing"),
    ("Mock", "Part 2 mock (5 of 9, timed)"),
    ("Review", "Error-log review — re-attempt failed questions"),
    ("Mock", "Full mock day: Part 1 AM + Part 2 PM"),
    ("Review", "Weak-topic sweep from mock results"),
    ("Review", "Light review: binder check, codes & calculator ready, rest"),
]


@dataclass
class Block:
    day: date
    kind: str          # Study | MCQ | Mock | Review
    code: str
    topic_id: str | None
    label: str
    minutes: int

    def as_dict(self):
        d = asdict(self)
        d["day"] = self.day.isoformat()
        return d


def subject_weights(settings: dict) -> dict[str, float]:
    w = {c: config.PART1_SUBJECT_WEIGHT for c in config.PART1_CODES}
    core = Counter(settings.get("part2_core", []))
    backup = set(settings.get("part2_backup", []))
    for c in config.PART2_CODES:
        w[c] = core.get(c, 0) * config.PART2_SLOT_WEIGHT + (config.PART2_BACKUP_WEIGHT if c in backup else 0)
    return w


def topic_weights(topics: list[dict], confidence: dict[str, int], settings: dict) -> dict[str, float]:
    """topics: [{id, code}], confidence: id -> 0..5"""
    sw = subject_weights(settings)
    out = {}
    for t in topics:
        s = sw.get(t["code"], 0.0)
        if s <= 0:
            continue
        c = confidence.get(t["id"], 0)
        out[t["id"]] = s * max(config.CONFIDENCE_FLOOR, 1 - c / 5)
    return out


def day_minutes(d: date, weekday_hours: float, weekend_hours: float) -> int:
    return int(round((weekend_hours if d.weekday() >= 5 else weekday_hours) * 60))


def generate_plan(topics: list[dict], confidence: dict[str, int], settings: dict,
                  start: date, exam: date = config.EXAM_DATE, block_min: int = 60,
                  topic_names: dict[str, str] | None = None) -> list[Block]:
    topic_names = topic_names or {}
    code_of = {t["id"]: t["code"] for t in topics}
    end = exam - timedelta(days=1)            # last plannable day
    if start > end:
        return []
    days = [start + timedelta(days=i) for i in range((end - start).days + 1)]
    mock_days = days[-config.MOCK_DAYS:] if len(days) > config.MOCK_DAYS else days[-1:]
    study_days = [d for d in days if d not in mock_days]

    wd, we = float(settings.get("weekday_hours", 2.5)), float(settings.get("weekend_hours", 6))
    weights = topic_weights(topics, confidence, settings)
    total_w = sum(weights.values()) or 1.0

    # total study capacity (excluding the daily MCQ block) → target minutes per topic
    capacity = sum(max(0, day_minutes(d, wd, we) - config.MCQ_BLOCK_MIN) for d in study_days)
    target = {tid: capacity * w / total_w for tid, w in weights.items()}
    assigned = Counter()
    sub_target: dict[str, float] = Counter()
    for tid, tgt in target.items():
        sub_target[code_of[tid]] += tgt
    sub_assigned = Counter()

    blocks: list[Block] = []
    for i, d in enumerate(study_days):
        avail = day_minutes(d, wd, we)
        mcq_code = config.PART1_CODES[i % len(config.PART1_CODES)]
        mcq = min(config.MCQ_BLOCK_MIN, avail)
        if mcq > 0:
            blocks.append(Block(d, "MCQ", mcq_code, None, f"{mcq_code} MCQ drill", mcq))
        remaining = avail - mcq
        used_today: set[str] = set()
        while remaining >= 15 and weights:
            length = min(block_min, remaining)
            # 1) subject furthest behind (fraction of its target), not the previous block's subject
            #    → every subject progresses in parallel and blocks interleave
            # 2) within it, the sub-topic with the lowest fraction done (weakest first on ties)
            prev_code = blocks[-1].code if blocks and blocks[-1].day == d and blocks[-1].kind == "Study" else None
            open_ = [t for t in weights if t not in used_today] or list(weights)
            subs = sorted({code_of[t] for t in open_},
                          key=lambda c: (c == prev_code, sub_assigned[c] / sub_target[c], -sub_target[c], c))
            code = subs[0]
            tid = min((t for t in open_ if code_of[t] == code),
                      key=lambda t: (assigned[t] / target[t], -target[t], t))
            blocks.append(Block(d, "Study", code_of[tid], tid, topic_names.get(tid, tid), length))
            assigned[tid] += length
            sub_assigned[code] += length
            used_today.add(tid)
            remaining -= length

    for j, d in enumerate(mock_days):
        kind, label = MOCK_SEQUENCE[min(j + (len(MOCK_SEQUENCE) - len(mock_days)), len(MOCK_SEQUENCE) - 1)]
        blocks.append(Block(d, kind, "ALL", None, label, day_minutes(d, wd, we)))
    return blocks
