from datetime import date, timedelta

import config
from utils.planner import generate_plan, subject_weights, topic_weights
from utils.syllabus import all_topics

S = dict(config.DEFAULT_SETTINGS)


def test_never_on_or_after_exam():
    blocks = generate_plan(all_topics(), {}, S, start=date(2026, 11, 24))
    assert blocks
    assert max(b.day for b in blocks) == config.EXAM_DATE - timedelta(days=1)
    assert all(b.day < config.EXAM_DATE for b in blocks)


def test_start_after_exam_gives_empty():
    assert generate_plan(all_topics(), {}, S, start=config.EXAM_DATE) == []
    assert generate_plan(all_topics(), {}, S, start=config.EXAM_DATE + timedelta(days=3)) == []


def test_last_seven_days_are_mocks_and_review():
    blocks = generate_plan(all_topics(), {}, S, start=date(2026, 11, 24))
    last7 = {config.EXAM_DATE - timedelta(days=i) for i in range(1, 8)}
    for b in blocks:
        if b.day in last7:
            assert b.kind in ("Mock", "Review")
        else:
            assert b.kind in ("Study", "MCQ")
    assert any(b.kind == "Mock" for b in blocks)


def test_daily_mcq_block_rotates():
    blocks = generate_plan(all_topics(), {}, S, start=date(2026, 11, 24))
    mcq = [b for b in blocks if b.kind == "MCQ"]
    study_days = {b.day for b in blocks if b.kind in ("Study", "MCQ")}
    assert len(mcq) == len(study_days)
    assert all(b.minutes == 30 for b in mcq)
    assert [b.code for b in mcq[:5]] == config.PART1_CODES


def test_unchosen_part2_zero_weight():
    w = subject_weights(S)
    assert w["CE204"] == w["CE205"] == w["CE206"] == 0
    assert w["CE201"] == 2 and w["CE203"] == 1.5
    blocks = generate_plan(all_topics(), {}, S, start=date(2026, 11, 24))
    assert not any(b.code in ("CE204", "CE205", "CE206") for b in blocks)


def test_confidence_weighting_and_floor():
    tw = topic_weights([{"id": "CE101-01", "code": "CE101"}, {"id": "CE101-02", "code": "CE101"}],
                       {"CE101-01": 5, "CE101-02": 0}, S)
    assert tw["CE101-01"] == config.CONFIDENCE_FLOOR
    assert tw["CE101-02"] == 1.0


def test_daily_minutes_respected():
    s = dict(S, weekday_hours=2, weekend_hours=5)
    blocks = generate_plan(all_topics(), {}, s, start=date(2026, 11, 24))
    by = {}
    for b in blocks:
        by[b.day] = by.get(b.day, 0) + b.minutes
    for d, m in by.items():
        assert m == (300 if d.weekday() >= 5 else 120)


def test_subjects_interleave_from_week_one():
    blocks = generate_plan(all_topics(), {}, S, start=date(2026, 11, 24))
    first14 = {b.code for b in blocks if b.kind == "Study" and b.day < date(2026, 12, 8)}
    assert set(config.PART1_CODES) | {"CE201", "CE202", "CE203"} <= first14
