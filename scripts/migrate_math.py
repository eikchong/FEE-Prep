"""One-off migration: plain-text notation → explicit LaTeX in the source data (first draft, reviewed by hand).

  python scripts/migrate_math.py --dry   # print before → after for every changed string
  python scripts/migrate_math.py         # rewrite the sources

Python sources are rewritten in place via the AST (only string literals whose value is a display string
are touched, so paths/ids/keys stay as they are). JSON banks are re-dumped with the same formatting.
"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from mathconv import convert  # noqa: E402

NOTE_FILES = sorted((ROOT / "utils").glob("study_notes*.py"))
FORMULA_FILES = [ROOT / "utils/formulas_notes.py", ROOT / "utils/formulas.py"]


# ------------------------------------------------------------------ which strings are display text
def study_strings() -> list[str]:
    from utils.study_notes import STUDY
    out = []
    for doc in STUDY.values():
        for s in doc["sections"]:
            out.append(s["title"])
            for b in s["blocks"]:
                out += block_texts(b)
    return out


def block_texts(b) -> list[str]:
    k = b[0]
    if k in ("md", "tip", "tut"):
        return [b[1]]
    if k == "ex":
        return [b[1], b[2]]
    if k == "steps":
        return list(b[1])
    if k == "q":
        q = b[1]
        return [q.get("question", ""), q.get("answer", ""), q.get("working", ""), q.get("figure", "") or ""] + \
            list(q.get("steps", []) or [])
    return []


def formula_strings() -> list[str]:
    from utils.formulas import FORMULAS
    from utils.formulas_notes import NOTES_LEGACY, NOTES_SECTIONS
    out = []
    for items in FORMULAS.values():
        out += [f["note"] for f in items] + [f["title"] for f in items]
    for secs in NOTES_SECTIONS.values():
        for s in secs:
            out.append(s["title"])
            out += [f["note"] for f in s["items"]] + [f["title"] for f in s["items"]]
    for items in (NOTES_LEGACY.values() if isinstance(NOTES_LEGACY, dict) else [NOTES_LEGACY]):
        for f in items:
            out += [f["note"], f["title"]]
    return [x for x in out if isinstance(x, str) and x]


JSON_FIELDS = {
    "mcq_bank.json": lambda d: [(q, k) for q in d for k in ("q", "explain")] +
                               [(q["options"], i) for q in d for i in range(len(q["options"]))],
    "part2_bank.json": lambda d: [(q, k) for q in d for k in ("title", "prompt") if k in q] +
                                 [(q["approach"], i) for q in d for i in range(len(q.get("approach", [])))],
    "past_papers.json": lambda d: [(q, k) for part in ("part1", "part2") for q in d[part]
                                   for k in ("title", "explain", "prompt", "q") if isinstance(q.get(k), str)] +
                                  [(q["approach"], i) for q in d["part2"] for i in range(len(q.get("approach", [])))] +
                                  [(q["options"], i) for q in d["part1"] for i in range(len(q.get("options", [])))],
}


# ------------------------------------------------------------------ rewriting
def _literal(value: str, indent: int, width: int = 112) -> str:
    """Python literal for value; long strings are split into implicitly-concatenated chunks."""
    def one(chunk: str) -> str:
        if "\\" in chunk and '"' not in chunk and "\n" not in chunk and not chunk.endswith("\\"):
            return 'r"' + chunk + '"'
        return json.dumps(chunk, ensure_ascii=False)
    if len(value) + indent + 4 <= width:
        return one(value)
    chunks, cur = [], ""
    for word in value.split(" "):
        cand = (cur + " " + word) if cur else word
        if len(cand) + indent + 4 > width and cur:
            chunks.append(cur + " ")
            cur = word
        else:
            cur = cand
    chunks.append(cur)
    return ("\n" + " " * indent).join(one(c) for c in chunks)


def rewrite_py(path: Path, mapping: dict[str, str], dry: bool) -> int:
    src = path.read_text(encoding="utf-8")
    lines = src.splitlines(keepends=True)
    offs = [0]
    for ln in lines:
        offs.append(offs[-1] + len(ln))
    tree = ast.parse(src)
    edits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            new = mapping.get(node.value)
            if new is not None and new != node.value:
                ca = len(lines[node.lineno - 1].encode()[:node.col_offset].decode())
                cb = len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())
                a = offs[node.lineno - 1] + ca
                b = offs[node.end_lineno - 1] + cb
                edits.append((a, b, _literal(new, ca), node.value, new))
    if dry:
        for _, _, _, old, new in edits:
            print(f"--- {path.name}\n  {old}\n→ {new}")
    else:
        for a, b, lit, _, _ in sorted(edits, reverse=True):
            src = src[:a] + lit + src[b:]
        path.write_text(src, encoding="utf-8")
    return len(edits)


def migrate(dry: bool) -> None:
    strings = set(study_strings()) | set(formula_strings())
    mapping = {s: convert(s) for s in strings}
    n = 0
    for f in NOTE_FILES + FORMULA_FILES:
        n += rewrite_py(f, mapping, dry)
    for name, fields in JSON_FIELDS.items():
        p = ROOT / "data" / name
        data = json.loads(p.read_text(encoding="utf-8"))
        for obj, key in fields(data):
            old = obj[key]
            new = convert(old)
            if new != old:
                n += 1
                if dry:
                    print(f"--- {name}\n  {old}\n→ {new}")
                obj[key] = new
        if not dry:
            p.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{n} strings changed", file=sys.stderr)


if __name__ == "__main__":
    migrate("--dry" in sys.argv)
