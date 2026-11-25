"""Lint for explicit-LaTeX text fields (used by tests/test_math.py and the migration).

Outside $…$ a text field may not contain: Greek letters, Unicode sub/superscripts, `_` or `^` touching a
letter or digit, or an odd number of unescaped $.
"""
from __future__ import annotations

import re

GREEK_RE = re.compile(r"[α-ωΑ-Ωϕϑϵς]")
UNI_SCRIPT_RE = re.compile(r"[₀-₉₊₋ₐ-ₜᵢⱼᵣᵤᵥ⁰¹²³⁴-⁹⁺⁻ⁿⁱ]")
SCRIPT_RE = re.compile(r"[A-Za-z0-9][_^]|[_^][A-Za-z0-9{]")
DOLLAR_RE = re.compile(r"(?<!\\)\$")
MATH_SPAN_RE = re.compile(r"(?<!\\)\$(.+?)(?<!\\)\$", re.S)
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)|`[^`]*`|https?://\S+")


def outside_math(text: str) -> str:
    return MATH_SPAN_RE.sub(" ", text)


def math_spans(text: str) -> list[str]:
    return MATH_SPAN_RE.findall(text)


def problems(text: str) -> list[str]:
    if not isinstance(text, str) or not text:
        return []
    out = []
    if len(DOLLAR_RE.findall(text)) % 2:
        out.append("odd number of $")
    rest = LINK_RE.sub(" ", outside_math(text))
    if m := GREEK_RE.search(rest):
        out.append(f"Greek outside math: {m.group(0)!r}")
    if m := UNI_SCRIPT_RE.search(rest):
        out.append(f"Unicode sub/superscript outside math: {m.group(0)!r}")
    if m := SCRIPT_RE.search(rest):
        out.append(f"_ or ^ outside math: {rest[max(0, m.start() - 8):m.end() + 8]!r}")
    return out
