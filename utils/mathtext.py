"""Turn plain-text engineering symbols in study notes into inline KaTeX for st.markdown.

Notes are written in readable plain text ("γ_d = 15.2", "f_ck^{2/3}", "σ′_v0", "M_c,Rd"); this converts each
subscripted/superscripted symbol into `$...$` so Streamlit renders proper sub/superscripts. Greek letters
and Unicode super/subscripts that already render well outside symbols are left alone.
"""
import re

GREEK = {
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta", "ε": r"\varepsilon", "ζ": r"\zeta",
    "η": r"\eta", "θ": r"\theta", "ι": r"\iota", "κ": r"\kappa", "λ": r"\lambda", "μ": r"\mu", "ν": r"\nu",
    "ξ": r"\xi", "π": r"\pi", "ρ": r"\rho", "σ": r"\sigma", "τ": r"\tau", "υ": r"\upsilon", "φ": r"\phi",
    "ϕ": r"\phi", "χ": r"\chi", "ψ": r"\psi", "ω": r"\omega", "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta",
    "Λ": r"\Lambda", "Π": r"\Pi", "Σ": r"\Sigma", "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega",
}
GR = "α-ωΑ-Ωϕ"
_SUBDIGITS = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
_SUPDIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")

_BASE = rf"(?P<base>[A-Za-z{GR}])(?P<bar>̄?)(?P<prime>[′″']*)"
_SUB = rf"_(?P<sub>\{{[^{{}}$]+\}}|[{GR}]|[A-Za-z0-9]+(?:,[A-Za-z0-9]+)*)(?P<sprime>[′']*)"
_SUP = r"(?:\^(?P<sup>\{[^{}$]+\}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9]))?"
TOKEN = re.compile(_BASE + _SUB + _SUP)
POWER = re.compile(r"\^(\{[^{}$]+\}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])")
_U = r"(?:k?N|M?Pa|kPa|mm|cm|m|s|kg|hr|yr|day|rad|kNm)"
UNIT = rf"(?<![A-Za-z]){_U}[²³]?(?:[/·]{_U}[²³]?)+(?![A-Za-z])|(?<![A-Za-z])L/s(?![A-Za-z])"
SKIP = re.compile(r"(\$[^$]*\$|`[^`]*`|https?://\S+|\[[^\]]*\]\([^)]*\)|" + UNIT + ")")


def _tex(s):
    s = re.sub("(.)\u0304", lambda m: r"\bar{" + m[1] + "}", s)
    s = s.replace("′", "'").replace("″", "''").replace("−", "-").replace("×", r"\times ").replace("·", r"\cdot ")
    s = s.translate(_SUBDIGITS).translate(_SUPDIGITS)
    return "".join(GREEK[c] + " " if c in GREEK else c for c in s).replace("  ", " ")


def _script(raw):
    inner = raw[1:-1] if raw.startswith("{") else raw
    parts = inner.split(",")
    if all(re.fullmatch(r"[A-Za-z]{2,}|[A-Za-z]{2,}\d*|\d+[A-Za-z]*|[A-Za-z]", p) for p in parts) and \
            any(re.fullmatch(r"[A-Za-z]{2,}\d*", p) for p in parts):
        return r"\mathrm{" + ",".join(parts) + "}"
    return _tex(inner)


def _token(m):
    base = _tex(m["base"]).strip()
    if m["bar"]:
        base = r"\bar{" + base + "}"
    out = base + _tex(m["prime"]) + "_{" + _script(m["sub"]) + "}" + _tex(m["sprime"] or "")
    if m["sup"]:
        out += "^{" + _script(m["sup"]) + "}"
    return "$" + out + "$"


GREEK_VAR = re.compile(rf"(?<![A-Za-z0-9{GR}$\\])(Δ[A-Za-z][′″]*|Δ?[{GR}]\u0304?[′″]*)(?![A-Za-z0-9{GR}])")
LATIN_VAR = re.compile(r"(?<![A-Za-z0-9₀-₉$\\.])([A-Za-z])([′″]*)(?![A-Za-z0-9$])")
_OPS = "=<>≤≥≈+−×·/()^"


def _is_formula_var(text, m):
    """A lone latin letter counts as a variable only when it sits in a formula (next to an operator)."""
    if m.prime:
        return True
    if text[m.start():m.end()] in "IVX" and re.search(r"\b(?:II|III|IV|VI)\b", text):   # Type III > I > II
        return False
    nxt, prv = text[m.end():m.end() + 2], text[max(0, m.start() - 1):m.start()]
    if prv == "(" and nxt[:1] == ")":                      # list label (a)
        return False
    if re.match(r"\.[A-Za-z]|[₀-₉]", nxt):                 # e.g., i.e., C₃A
        return False
    if re.search(r"\d\s$", text[:m.start()]):              # 0.3 m) — a unit after a number
        return False
    if text[m.end():m.end() + 1] == "·" or text[m.start() - 1:m.start()] == "·":   # tight product k·i·A
        return True
    after = text[m.end():].lstrip(" ")
    before = text[:m.start()].rstrip(" ")
    if re.search(r"\$,$", before) or re.match(r",\s*\$", after):   # symbol lists: γ_d, e, n, S_r
        return True
    if after[:1] and after[:1] in _OPS.replace("(", "").replace("·", "") or after[:1] == "$":
        if after[:1] == "/" and re.match(r"/\s*[A-Za-z]{2,}", after):   # unit like m/s
            return False
        return True
    if before[-1:] and before[-1:] in _OPS.replace(")", "").replace("·", "") or before[-1:] == "$":
        if before[-1:] == "/" and re.search(r"[A-Za-z]{2,}\s*/$", before):  # kN/m
            return False
        return True
    return False


def _vars(text):
    text = GREEK_VAR.sub(lambda m: "$" + _tex(m[1]).strip() + "$", text)
    parts = re.split(r"(\$[^$]*\$)", text)
    out = []
    for i, p in enumerate(parts):
        if p.startswith("$"):
            out.append(p)
            continue
        whole = "".join(out) + "".join(parts[i:])
        off = len("".join(out))
        res, last = [], 0
        for m in LATIN_VAR.finditer(p):
            if _is_formula_var(whole, type("M", (), {"start": lambda s, a=m.start() + off: a,
                                                      "end": lambda s, b=m.end() + off: b,
                                                      "prime": bool(m[2])})()):
                res.append(p[last:m.start()] + "$" + m[1] + _tex(m[2]) + "$")
                last = m.end()
        res.append(p[last:])
        out.append("".join(res))
    return "".join(out)


def _plain(text):
    text = TOKEN.sub(_token, text)
    # leftover powers like 30^{2/3}, )^0.5 — only outside the $…$ just produced
    parts = re.split(r"(\$[^$]*\$)", text)
    text = "".join(p if p.startswith("$") else POWER.sub(lambda m: "$^{" + _script(m[1]) + "}$", p) for p in parts)
    text = _vars(text)
    return text.replace("$$", " ")   # merge adjacent symbols (G_sγ_w) into one span; never leave a $$ delimiter


def mathify(text):
    if not isinstance(text, str):
        return text
    parts = SKIP.split(text)
    return "".join(p if i % 2 else _plain(p) for i, p in enumerate(parts))
