"""Progress maths: word-weighted, 95 % rule, never decreases by scrolling, migration from notes_read."""
import copy

from utils.notes_index import index, section_keys
from utils.reading import (READ_AT, completed_topics, mark_read, mark_topic_unread, migrate_notes_read, section_words,
                           subject_stats, topic_sections, topic_stats)
from utils.storage import merge_defaults
from utils.study_notes import STUDY


def fresh():
    return merge_defaults({})


def test_topic_pct_is_word_weighted():
    p = fresh()
    keys = topic_sections("CE104-05")
    w = section_words()
    big = max(keys, key=lambda k: w[k])
    mark_read(p, [big])
    ts = topic_stats(p, "CE104-05")
    assert abs(ts["pct"] - w[big] / sum(w[k] for k in keys)) < 1e-9
    assert ts["status"] == "reading"


def test_read_at_95_percent():
    p = fresh()
    keys = topic_sections("CE104-05")
    w = section_words()
    total = sum(w[k] for k in keys)
    # read everything except the smallest sections while staying >= 95 %
    order = sorted(keys, key=lambda k: w[k])
    skipped, acc = [], 0
    for k in order:
        if (acc + w[k]) / total <= 1 - READ_AT:
            skipped.append(k)
            acc += w[k]
    mark_read(p, [k for k in keys if k not in skipped])
    assert topic_stats(p, "CE104-05")["status"] == "read"
    p2 = fresh()
    mark_read(p2, keys[:-1] if w[keys[-1]] / total > 0.05 else keys[:len(keys) // 2])
    assert topic_stats(p2, "CE104-05")["pct"] < READ_AT
    assert topic_stats(p2, "CE104-05")["status"] == "reading"


def test_progress_never_decreases_from_scrolling():
    p = fresh()
    keys = topic_sections("CE104-07")
    mark_read(p, keys[:3], today="2026-11-01")
    before = subject_stats(p, "CE104")["pct"]
    new = mark_read(p, keys[:3] + keys[3:5], today="2026-11-02")
    assert new == keys[3:5]
    assert p["read"][keys[0]] == "2026-11-01"           # first-read date kept
    assert subject_stats(p, "CE104")["pct"] >= before
    mark_read(p, ["not-a-key"])
    assert "not-a-key" not in p["read"]


def test_subject_pct_word_weighted_over_topics_with_notes():
    p = fresh()
    keys = topic_sections("CE104-03")
    mark_read(p, keys)
    ss = subject_stats(p, "CE104")
    w = section_words()
    allk = [k for t in ss["topics"] for k in topic_sections(t)]
    assert abs(ss["pct"] - sum(w[k] for k in keys) / sum(w[k] for k in allk)) < 1e-9
    assert ss["topics"]["CE104-09"]["status"] == "covered"


def test_completed_topic_detected_and_unread():
    p = fresh()
    keys = topic_sections("CE104-04")
    before = copy.deepcopy(p["read"])
    new = mark_read(p, keys)
    assert "CE104-04" in completed_topics(p, before, new)
    mark_topic_unread(p, "CE104-04")
    assert topic_stats(p, "CE104-04")["read_words"] == 0


def test_migrate_notes_read():
    doc = next(d for d in STUDY if STUDY[d]["code"] == "CE104" and len(STUDY[d]["sections"]) > 2
               and all(k in index()["sections"] for k in section_keys(d, STUDY[d]["sections"])[:2]))
    p = merge_defaults({"notes_read": {doc: [0, 1]}})
    assert migrate_notes_read(p)
    ks = section_keys(doc, STUDY[doc]["sections"])
    assert ks[0] in p["read"] and ks[1] in p["read"]
    assert not migrate_notes_read(p)


def test_question_answer_does_not_count():
    from utils.reading import block_words
    b = ("q", {"question": "One two three", "answer": "a " * 500, "working": "w " * 500})
    assert block_words(b) == 3 + 3
