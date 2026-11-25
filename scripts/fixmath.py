"""Apply hand-review fixes to display strings: [(old_substring, new_substring), …] across the notes, formula
files and JSON banks. Each old substring must occur in at least one display string (else it is reported).

    from scripts.fixmath import apply;  apply([("…", "…")])
"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from migrate_math import FORMULA_FILES, NOTE_FILES, _literal  # noqa: E402

JSONS = ["mcq_bank.json", "part2_bank.json", "past_papers.json"]


def _walk_json(obj, fn):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str):
                obj[k] = fn(v)
            else:
                _walk_json(v, fn)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str):
                obj[i] = fn(v)
            else:
                _walk_json(v, fn)


def apply(fixes: list[tuple[str, str]], verbose: bool = True) -> dict:
    hits = {o: 0 for o, _ in fixes}

    def fix(v: str) -> str:
        for o, n in fixes:
            if o in v:
                hits[o] += v.count(o)
                v = v.replace(o, n)
        return v

    for path in NOTE_FILES + FORMULA_FILES:
        src = path.read_text(encoding="utf-8")
        lines = src.splitlines(keepends=True)
        offs = [0]
        for ln in lines:
            offs.append(offs[-1] + len(ln))
        edits = []
        for node in ast.walk(ast.parse(src)):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                new = fix(node.value)
                if new != node.value:
                    ca = len(lines[node.lineno - 1].encode()[:node.col_offset].decode())
                    cb = len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())
                    edits.append((offs[node.lineno - 1] + ca, offs[node.end_lineno - 1] + cb, _literal(new, ca)))
        for a, b, lit in sorted(edits, reverse=True):
            src = src[:a] + lit + src[b:]
        if edits:
            path.write_text(src, encoding="utf-8")
    for name in JSONS:
        p = ROOT / "data" / name
        data = json.loads(p.read_text(encoding="utf-8"))
        before = json.dumps(data, ensure_ascii=False)
        _walk_json(data, fix)
        if json.dumps(data, ensure_ascii=False) != before:
            p.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    missing = [o for o, c in hits.items() if not c]
    if verbose and missing:
        print("NOT FOUND:", *missing, sep="\n  ")
    return hits
