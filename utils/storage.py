"""Persistence layer.

All app state lives in a single JSON document (data/progress.json). The `Storage`
interface is deliberately tiny (load/save) so it can be swapped for SQLite/Supabase
later (e.g. for Streamlit Cloud) without touching the views.
"""
from __future__ import annotations

import copy
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Protocol

import config

EMPTY_PROGRESS: dict[str, Any] = {
    "topics": {},          # id -> {status, confidence, notes}
    "mcq_attempts": [],    # {ts, qid, code, chosen, correct, mode, seconds}
    "part2_attempts": [],  # {ts, qid, code, scores{}, score_pct, seconds, notes, mock}
    "errors": [],          # {id, ts, code, source, what, fix, resolved, source_doc, source_page}
    "study_log": [],       # {date, minutes, code, note}
    "mock_results": [],    # {ts, part, score_pct, by_subject{}, seconds}
    "custom_mcqs": [],     # user-added MCQs, same schema as mcq_bank
    "pins": [],            # {id, code, topic_id, doc, page, excerpt, ts}
    "formula_notes": {},   # code -> markdown
    "notes_read": {},      # notes path -> [studied section indices]
    "settings": copy.deepcopy(config.DEFAULT_SETTINGS),
}


class Storage(Protocol):
    def load(self) -> dict: ...
    def save(self, data: dict) -> None: ...


class JsonStorage:
    def __init__(self, path: Path | None = None):
        self.path = Path(path or config.DATA_DIR / "progress.json")

    def load(self) -> dict:
        data = {}
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                # keep a copy of the corrupt file rather than silently overwriting it
                self.path.rename(self.path.with_suffix(".corrupt.json"))
                data = {}
        return merge_defaults(data)

    def save(self, data: dict) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=self.path.parent, prefix=".progress-", suffix=".json")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=1, ensure_ascii=False, default=str)
        os.replace(tmp, self.path)  # atomic on POSIX & Windows


def merge_defaults(data: dict) -> dict:
    out = copy.deepcopy(EMPTY_PROGRESS)
    for k, v in (data or {}).items():
        if k == "settings" and isinstance(v, dict):
            out["settings"].update(v)
        else:
            out[k] = v
    return out


def get_storage() -> Storage:
    return JsonStorage()


def load_static(name: str) -> Any:
    return json.loads((config.STATIC_DATA_DIR / name).read_text(encoding="utf-8"))
