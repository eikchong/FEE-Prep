"""Past-paper index (data/past_papers.json) helpers.

The PEB papers themselves live in materials/_past_papers/ (git-ignored — the repo is public).
The index only holds metadata, page pointers, answer keys and our own worked solutions.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache

import config
from utils.storage import load_static

LETTERS = "abcd"


@lru_cache(maxsize=1)
def index() -> dict:
    return load_static("past_papers.json")


def docs() -> dict[str, dict]:
    return index()["docs"]


def items(part: int | None = None) -> list[dict]:
    out = []
    for p in (1, 2):
        if part in (None, p):
            out += [{**q, "part": p} for q in index()[f"part{p}"]]
    return out


def doc_available(doc: str) -> bool:
    return (config.MATERIALS_DIR / doc).exists()


def years(q: dict) -> list[int]:
    return sorted({a["year"] for a in q["appearances"]})


def frequency(part: int | None = None) -> Counter:
    """Appearances per subject code (each year a question appears counts once)."""
    c = Counter()
    for q in items(part):
        c[q["code"]] += len({a["year"] for a in q["appearances"]})
    return c


def topic_frequency() -> Counter:
    c = Counter()
    for q in items():
        n = len({a["year"] for a in q["appearances"]})
        for t in q["topics"]:
            c[t] += n
    return c
