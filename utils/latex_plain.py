"""to_plain(): Markdown-with-LaTeX → readable Unicode, for places KaTeX can't render (tab titles, toasts, the
injected progress bar, widget labels, slugs, PDF export).  "$\\sigma'_v$ = 50 kPa" → "σ′v = 50 kPa"."""
from __future__ import annotations

import re

_CMDS = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε", "varepsilon": "ε", "zeta": "ζ",
    "eta": "η", "theta": "θ", "vartheta": "θ", "iota": "ι", "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν",
    "xi": "ξ", "pi": "π", "rho": "ρ", "sigma": "σ", "tau": "τ", "upsilon": "υ", "phi": "φ", "varphi": "φ",
    "chi": "χ", "psi": "ψ", "omega": "ω", "Gamma": "Γ", "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Xi": "Ξ",
    "Pi": "Π", "Sigma": "Σ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω", "ell": "ℓ",
    "times": "×", "cdot": "·", "approx": "≈", "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "neq": "≠",
    "ne": "≠", "pm": "±", "mp": "∓", "infty": "∞", "sum": "Σ", "int": "∫", "partial": "∂", "ldots": "…",
    "cdots": "⋯", "dots": "…", "to": "→", "rightarrow": "→", "Rightarrow": "⇒", "leftarrow": "←", "propto": "∝",
    "equiv": "≡", "circ": "°", "degree": "°", "%": "%", "$": "$", "nabla": "∇", "sim": "~", "ll": "≪",
    "gg": "≫", "quad": "  ", "qquad": "   ", ",": " ", ";": " ", "!": "", " ": " ", "prime": "′", "lt": "<",
    "gt": ">", "min": "min", "max": "max", "sin": "sin", "cos": "cos", "tan": "tan", "cot": "cot", "ln": "ln",
    "log": "log", "exp": "exp", "sinh": "sinh", "cosh": "cosh", "tanh": "tanh", "lim": "lim", "in": "∈",
    "therefore": "∴", "angle": "∠", "perp": "⊥", "parallel": "∥", "Delta_": "Δ",
}
_SUP = dict(zip("0123456789+-−=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿ"))
_FRAC = {("1", "2"): "½", ("1", "3"): "⅓", ("2", "3"): "⅔", ("1", "4"): "¼", ("3", "4"): "¾"}
_GROUP = r"\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}"


def _sup(s: str) -> str:
    s = s.strip()
    if s in ("\\circ", "°"):
        return "°"
    if s and all(c in _SUP for c in s):
        return "".join(_SUP[c] for c in s)
    return "^(" + s + ")" if len(s) > 1 else "^" + s


def latex_to_plain(s: str) -> str:
    for _ in range(4):
        s = re.sub(r"\\(?:mathrm|mathbf|mathit|boldsymbol|text|textbf|textrm|operatorname|bm|mathsf)\s*" + _GROUP,
                   r"\1", s)
    s = re.sub(r"\\[dt]?frac\s*(\d)\s*(\d)", lambda m: _FRAC.get((m[1], m[2]), f"{m[1]}/{m[2]}"), s)
    for _ in range(3):
        s = re.sub(r"\\[dt]?frac\s*" + _GROUP + r"\s*" + _GROUP,
                   lambda m: _FRAC.get((m[1], m[2])) or (f"{_wrap(m[1])}/{_wrap(m[2])}"), s)
        s = re.sub(r"\\sqrt\s*" + _GROUP, lambda m: "√" + _wrap(m[1], always=len(m[1]) > 1), s)
        s = re.sub(r"\\(?:bar|overline)\s*" + _GROUP, lambda m: m[1] + "\u0304", s)
        s = re.sub(r"\\(?:hat)\s*" + _GROUP, lambda m: m[1] + "\u0302", s)
        s = re.sub(r"\\(?:dot)\s*" + _GROUP, lambda m: m[1] + "\u0307", s)
        s = re.sub(r"\\(?:vec)\s*" + _GROUP, lambda m: m[1] + "\u20d7", s)
    s = re.sub(r"\\(?:left|right|big|Big|bigg|Bigg)\s*([()\[\]|.]|\\[{}])", lambda m: "" if m[1] == "." else m[1], s)
    s = re.sub(r"\^\s*\\circ", "°", s)
    s = re.sub(r"\\([A-Za-z]+)(?![A-Za-z])", lambda m: _CMDS.get(m[1], "\\" + m[1]), s)
    s = re.sub(r"\^\s*" + _GROUP, lambda m: _sup(latex_to_plain(m[1])), s)
    s = re.sub(r"\^\s*(\\?[A-Za-z0-9])", lambda m: _sup(m[1]), s)
    s = re.sub(r"_\s*" + _GROUP, lambda m: latex_to_plain(m[1]).replace(" ", ""), s)
    s = re.sub(r"_\s*(\\[A-Za-z]+|[A-Za-z0-9])", lambda m: m[1], s)
    s = re.sub(r"\\([A-Za-z]+|[%$, ;!])", lambda m: _CMDS.get(m[1], m[1]), s)
    s = s.replace("{", "").replace("}", "").replace("''", "″").replace("'", "′").replace("~", " ")
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.strip()


def _wrap(s: str, always: bool = False) -> str:
    s = latex_to_plain(s)
    return f"({s})" if always or re.search(r"[\s+\-−/·×]", s) else s


def to_plain(text: str) -> str:
    """Markdown text with $…$ math → plain Unicode (math converted; Markdown bold markers removed)."""
    if not isinstance(text, str):
        return text
    out = re.sub(r"(?<!\\)\$(.+?)(?<!\\)\$", lambda m: latex_to_plain(m[1]), text, flags=re.S)
    out = out.replace("\\$", "$").replace("**", "")
    return out
