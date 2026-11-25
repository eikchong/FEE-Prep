"""Math in the notes and banks is explicit LaTeX: lint outside $…$, and render every span with KaTeX."""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from utils.mathfields import display_fields, text_fields
from utils.mathlint import math_spans, problems

ROOT = Path(__file__).resolve().parents[1]


def test_no_plain_text_math_outside_dollars():
    bad = [f"{w}: {p} ← {t[:120]!r}" for w, t in text_fields() for p in problems(t)]
    assert not bad, f"{len(bad)} problems:\n" + "\n".join(bad[:40])


def _spans():
    out = [{"where": w, "tex": s} for w, t in text_fields() for s in math_spans(t)]
    out += [{"where": w, "tex": t, "display": True} for w, t in display_fields()]
    return out


def test_katex_renders_every_span(tmp_path):
    node = shutil.which("node")
    if not node or not (ROOT / "node_modules/katex").exists():
        pytest.skip("node + katex not installed (npm install)")
    f = tmp_path / "spans.json"
    f.write_text(json.dumps(_spans(), ensure_ascii=False))
    r = subprocess.run([node, str(ROOT / "scripts/check_katex.mjs"), str(f)], capture_output=True, text=True,
                       cwd=ROOT, timeout=300)
    assert r.returncode == 0, r.stdout[-6000:]
