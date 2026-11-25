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
import time
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
    "notes_read": {},      # legacy: notes path -> [studied section indices] (migrated to "read")
    "read": {},            # section key -> date first read (from scroll tracking; never removed by scrolling)
    "revisit": {},         # topic id -> date flagged "Revisit later"
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

    def save(self, data: dict, force: bool = False) -> None:
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


class GistStorage:
    """Keep progress.json in a private GitHub gist (Streamlit Cloud wipes the container disk on reboot/redeploy).

    Writes are throttled to one per `min_interval` seconds; a write that arrives sooner is kept and sent by a
    timer when the interval has passed. `save(data, force=True)` writes at once (used when a topic completes).
    """
    FILE = "progress.json"

    def __init__(self, gist_id: str, token: str, min_interval: float = 20.0, timeout: float = 10.0):
        import threading
        self.gist_id, self.token, self.min_interval, self.timeout = gist_id, token, min_interval, timeout
        self._last = 0.0
        self._pending: dict | None = None
        self._timer = None
        self._lock = threading.Lock()

    def _req(self, method: str, body: dict | None = None) -> dict:
        import urllib.request
        req = urllib.request.Request(
            f"https://api.github.com/gists/{self.gist_id}", method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={"Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json",
                     "User-Agent": "fee-prep-app", "X-GitHub-Api-Version": "2022-11-28",
                     **({"Content-Type": "application/json"} if body is not None else {})})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read().decode())

    def load(self) -> dict:
        try:
            g = self._req("GET")
            f = (g.get("files") or {}).get(self.FILE)
            if not f:
                return merge_defaults({})
            content = f.get("content", "")
            if f.get("truncated") and f.get("raw_url"):
                import urllib.request
                with urllib.request.urlopen(f["raw_url"], timeout=self.timeout) as r:
                    content = r.read().decode()
            return merge_defaults(json.loads(content) if content.strip() else {})
        except Exception:
            # never lose the user's data by overwriting it with defaults: fall back to a local copy
            return JsonStorage().load()

    def _write(self, data: dict) -> None:
        body = {"files": {self.FILE: {"content": json.dumps(data, indent=1, ensure_ascii=False, default=str)}}}
        self._req("PATCH", body)
        self._last = time.monotonic()

    def _flush(self) -> None:
        with self._lock:
            data, self._pending, self._timer = self._pending, None, None
        if data is not None:
            try:
                self._write(data)
            except Exception:
                JsonStorage().save(data)

    def save(self, data: dict, force: bool = False) -> None:
        import threading
        JsonStorage().save(data)                     # local copy, also a fallback if GitHub is unreachable
        wait = self.min_interval - (time.monotonic() - self._last)
        with self._lock:
            self._pending = copy.deepcopy(data)
            if force or wait <= 0:
                if self._timer:
                    self._timer.cancel()
                    self._timer = None
                go_now = True
            else:
                go_now = False
                if not self._timer:
                    self._timer = threading.Timer(wait, self._flush)
                    self._timer.daemon = True
                    self._timer.start()
        if go_now:
            self._flush()


def _secret(name: str):
    try:
        import streamlit as st
        return st.secrets.get(name)
    except Exception:
        return None


def get_storage() -> Storage:
    gid, tok = _secret("GIST_ID"), _secret("GITHUB_TOKEN")
    if gid and tok:
        return GistStorage(str(gid), str(tok))
    return JsonStorage()


def load_static(name: str) -> Any:
    return json.loads((config.STATIC_DATA_DIR / name).read_text(encoding="utf-8"))
