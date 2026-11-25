"""First-draft converter: plain-text engineering notation → Markdown with explicit LaTeX ($…$).

Used once by scripts/migrate_math.py; the converted source is then reviewed and fixed by hand.
Finds whole expressions (variables, numbers, operators, units) and puts each in ONE math span:
  "γ_d = 26.5/1.72 = **15.4 kN/m³**"  →  "$\\gamma_d = 26.5/1.72 = \\boldsymbol{15.4\\ \\mathrm{kN/m^3}}$"
"""
from __future__ import annotations

import re

GREEK = {
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta", "ε": r"\varepsilon", "ζ": r"\zeta",
    "η": r"\eta", "θ": r"\theta", "ι": r"\iota", "κ": r"\kappa", "λ": r"\lambda", "μ": r"\mu", "ν": r"\nu",
    "ξ": r"\xi", "π": r"\pi", "ρ": r"\rho", "σ": r"\sigma", "ς": r"\sigma", "τ": r"\tau", "υ": r"\upsilon",
    "φ": r"\phi", "ϕ": r"\phi", "χ": r"\chi", "ψ": r"\psi", "ω": r"\omega", "Γ": r"\Gamma", "Δ": r"\Delta",
    "Θ": r"\Theta", "Λ": r"\Lambda", "Π": r"\Pi", "Σ": r"\sum", "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega",
    "Ξ": r"\Xi", "ℓ": r"\ell", "∂": r"\partial",
}
GR = "α-ωΑ-Ωϕςℓ"
SUBS = dict(zip("₀₁₂₃₄₅₆₇₈₉₊₋ₐₑₒₓₕₖₗₘₙₚₛₜᵢⱼᵣᵤᵥ", "0123456789+-aeoxhklmnpstijruv"))
SUPS = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿⁱᵀ", "0123456789+-niT"))
SUB_RE = "[" + "".join(SUBS) + "]"
SUP_RE = "[" + "".join(SUPS) + "]"
FUNCS = {"sin", "cos", "tan", "cot", "sec", "csc", "ln", "log", "exp", "max", "min", "sinh", "cosh", "tanh",
         "arctan", "arcsin", "arccos", "lim"}
UNIT_RE = re.compile(
    r"(?:(?:k|M|G|m|c|μ|n)?(?:N|Pa|m|g|s|W|J|L|Hz|V)|kNm|Nm|rad|mrad|min|h|hr|day|days|yr|years|t|ha|mg|ppm|kWh|"
    r"veh|pcu|mph|km|mm|cm|kg|kN|MN|kW|MW|MPa|kPa|GPa|kJ|MJ|°C|°|%|‰)"
    r"(?:(?:" + SUP_RE + r")+|\^\{?-?\d+\}?)?"
    r"(?:[/·](?:(?:k|M|G|m|c|μ|n)?(?:N|Pa|m|g|s|W|J|L|Hz)|kNm|Nm|rad|min|h|hr|day|yr|ha|veh|lane|km|mm|cm|kg|kN|m|s)"
    r"(?:(?:" + SUP_RE + r")+|\^\{?-?\d+\}?)?)*$")
STOP = {"is", "in", "at", "of", "to", "be", "as", "or", "if", "the", "and", "for", "on", "by", "an", "it", "so",
        "no", "up", "we", "do", "go", "he", "me", "my", "us", "am", "are", "all", "not", "use", "per", "via",
        "with", "but", "then", "than", "from", "into", "each", "both", "only", "also", "when", "set", "get"}

TOKEN = re.compile(rf"""
 (?P<skip>\$[^$]*\$|`[^`]*`|https?://\S+|\[[^\]]*\]\([^)]*\))
|(?P<bold>\*\*)
|(?P<gsub>(?:[στεγ][′']?|Σ ?[FM]|∂[uvw])[xyz]{{1,2}}(?![A-Za-z]))
|(?P<chem>(?=(?:[A-Z][a-z]?{SUB_RE}*){{2,}}(?![A-Za-z]))(?=[A-Za-z]*{SUB_RE})(?:[A-Z][a-z]?{SUB_RE}*){{2,}}(?![A-Za-z]))
|(?P<cunit>(?:(?<=[0-9⁰¹²³⁴⁵⁶⁷⁸⁹]\s)|(?<=[0-9]))(?:m|rad)/(?:s|h|day|yr)(?:{SUP_RE}+)?(?![A-Za-z])|(?:kNm|MNm|Nm|k?N|MN|mm|cm|kg|L|veh|kPa|MPa|kW|mg|pcu|rad|m(?={SUP_RE}))(?:{SUP_RE}+)?(?:[/·](?:mm|cm|m|s|h|hr|day|lane|km|ha|yr|kg|g|L|kN|N|veh)(?:{SUP_RE}+)?)+(?![A-Za-z_])|(?:k?N|mm|cm|m|kg){SUP_RE}+(?![A-Za-z_]))
|(?P<num>\d{{1,3}}(?:[ \u202f]\d{{3}})+(?:\.\d+)?(?![\d.])|\d+(?:\.\d+)?(?:[eE][-−]?\d+)?|\.\d+)
|(?P<sym>[Δ∂][A-Za-z](?![A-Za-z_{SUB_RE}])(?:\^(?:\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])|{SUP_RE}+)?
  |(?:[Δ∂](?=[A-Za-z{GR}]))?[A-Za-z{GR}]\u0304?[′″']*
     (?:_(?:\{{[^{{}}$]+\}}|[{GR}]|[A-Za-z0-9]+?(?=[A-Za-z](?:_|{SUB_RE}))|[A-Za-z0-9]+(?:,[A-Za-z0-9]+)*)|{SUB_RE}+)[′″']*
     (?:\^(?:\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])|{SUP_RE}+)?
  |(?:[Δ∂](?=[A-Za-z{GR}]))?[{GR}]\u0304?[′″']*(?:\^(?:\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])|{SUP_RE}+)?
  |[A-Za-z]\u0304?[′″]+(?:\^(?:\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])|{SUP_RE}+)?
  |[A-Za-z]\u0304(?:\^(?:\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])|{SUP_RE}+)?
  |[A-Za-z]{{1,2}}(?:\^(?:\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])|{SUP_RE}+))
|(?P<funcd>(?:sin|cos|tan)(?=\d))
|(?P<label>[A-Za-z]+\d+[A-Za-z0-9]*(?:\.\d+)?)
|(?P<word>(?:[A-Za-z](?![_′″\u0304]|{SUB_RE}))+(?:{SUP_RE}+)?|[A-Za-z])
|(?P<supsub>{SUP_RE}+|{SUB_RE}+|(?<=[)\]])\^(?:\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9]))
|(?P<sep>\s·\s|\s+[—→⇒]\s+|[—→⇒])
|(?P<rel>[=≈≤≥<>≠≡∝])
|(?P<bullet>(?:^|(?<=\n))[ \t]*[-*][ \t])
|(?P<op>[+−×·/±√∞∫∑Σ∂|]|(?<=[ \t\d(])-(?=[\s\d(])|(?<=[\d)])-(?=[A-Za-z(])|–|…|½|¼|¾|⅓|⅔|°C|°|%|‰)
|(?P<open>[(\[{{])
|(?P<close>[)\]}}])
|(?P<ws>\s+)
|(?P<other>.)
""", re.X | re.S)


def _tex_chars(s: str) -> str:
    out = []
    for c in s:
        if c in GREEK:
            out.append(GREEK[c] + " ")
        elif c == "′":
            out.append("'")
        elif c == "″":
            out.append("''")
        elif c == "−":
            out.append("-")
        elif c == "×":
            out.append(r"\times ")
        elif c == "·":
            out.append(r"\cdot ")
        else:
            out.append(c)
    return re.sub(r" +", " ", "".join(out))


def _script(raw: str) -> str:
    inner = raw[1:-1] if raw.startswith("{") else raw
    parts = inner.split(",")
    if all(re.fullmatch(r"[ijkxyzn]{1,2}", p) for p in parts):
        return ",".join(parts)
    if any(re.fullmatch(r"[A-Za-z]{2,}\d*|[A-Z]\d+|\d+[A-Za-z]{2,}", p) for p in parts) and \
            all(re.fullmatch(r"[A-Za-z0-9]+", p) for p in parts):
        return r"\mathrm{" + ",".join(parts) + "}"
    return _tex_chars(inner).strip()


def _sym(tok: str) -> str:
    m = re.fullmatch(rf"(?P<d>[Δ∂]?)(?P<b>[A-Za-z{GR}]{{1,2}})(?P<bar>\u0304?)(?P<p>[′″']*)"
                     rf"(?:_(?P<s>\{{[^{{}}$]+\}}|[{GR}]|[A-Za-z0-9]+(?:,[A-Za-z0-9]+)*)|(?P<us>{SUB_RE}+))?"
                     rf"(?P<p2>[′″']*)"
                     rf"(?:\^(?P<sup>\{{[^{{}}$]+\}}|[-−]?[A-Za-z0-9.]*[A-Za-z0-9])|(?P<usup>{SUP_RE}+))?", tok)
    if not m:
        return _tex_chars(tok)
    b = m["b"]
    if len(b) == 2 and b[0] not in GREEK:           # wL² → w L^2 (implicit product)
        pre, b = b[0], b[1]
    else:
        pre = ""
    base = _tex_chars(b).strip()
    if m["bar"]:
        base = r"\bar{" + base + "}"
    out = pre + (_tex_chars(m["d"]).strip() + " " if m["d"] else "") + base + _tex_chars(m["p"])
    if m["s"]:
        out += "_{" + _script(m["s"]) + "}"
    elif m["us"]:
        out += "_{" + "".join(SUBS[c] for c in m["us"]) + "}"
    out += _tex_chars(m["p2"] or "")
    if m["sup"]:
        out += "^{" + _script(m["sup"]) + "}"
    elif m["usup"]:
        out += "^{" + "".join(SUPS[c] for c in m["usup"]) + "}"
    return out.replace("_{", "_{").replace("{ ", "{")


def _unit(u: str) -> str:
    u = u.replace("°C", r"^\circ\mathrm{C}") if u.startswith("°C") else u
    if u == "°":
        return r"^\circ"
    if u == "%":
        return r"\,\%"
    if u == "‰":
        return r"\,\text{‰}"
    def sup(m):
        return "^{" + "".join(SUPS[c] for c in m.group(0)) + "}"
    body = re.sub(SUP_RE + "+", sup, u).replace("·", r"\cdot ").replace("μ", r"\mu ")
    return r"\ \mathrm{" + body + "}"


def _tokens(text: str):
    for m in TOKEN.finditer(text):
        kind = m.lastgroup
        yield kind, m.group(0)


def _classify(toks):
    """Return list of (kind, text, role); role in M (math), V (lone latin letter), U (unit), B (bold),
    W (whitespace), X (prose boundary)."""
    out = []
    for i, (k, t) in enumerate(toks):
        if k == "skip":
            out.append((k, t, "X"))
        elif k == "bold":
            out.append((k, t, "B"))
        elif k == "ws":
            out.append((k, t, "W"))
        elif k in ("num", "sym", "rel", "supsub", "open", "close"):
            out.append((k, t, "M"))
        elif k == "op":
            out.append((k, t, "U" if t in ("°", "°C", "%", "‰") else "M"))
        elif k == "funcd":
            out.append(("func", t, "M"))
        elif k == "gsub":
            out.append(("sym", t, "M"))
        elif k == "bullet":
            out.append((k, t, "X"))
        elif k == "word" and re.fullmatch(r"[IVX]{2,4}", t):
            out.append((k, t, "X"))
        elif k == "word" and t in ("max", "min", "lim") and not (i + 1 < len(toks) and toks[i + 1][1][:1] in "(_{^"):
            out.append((k, t, "X"))
        elif k == "cunit":
            out.append((k, t, "U?"))
        elif k == "chem":
            out.append((k, t, "M"))
        elif k == "word":
            base = re.sub(SUP_RE + "+$", "", t)
            if base.lower() in FUNCS:
                out.append(("func", t, "M"))
            elif len(t) == 1:
                out.append((k, t, "V"))
            elif UNIT_RE.match(t):
                out.append((k, t, "U?"))
            elif re.search(SUP_RE, t):
                out.append(("chem", t, "M"))
            else:
                out.append((k, t, "X?"))
        else:
            out.append((k, t, "X"))
    for i, (k, t, r) in enumerate(out):
        if (r == "V" and t in "mshNgt") or (k == "sym" and re.fullmatch(r"[mshN]" + SUP_RE + "+", t)):
            if i >= 2 and out[i - 1][2] == "W" and out[i - 2][0] in ("num", "supsub"):
                out[i] = ("unit1", t, "U")
    if any(re.fullmatch(r"[IVX]{2,4}", t) for k, t, r in out):
        out = [(k, t, "X") if (r == "V" and t in "IVX") else (k, t, r) for k, t, r in out]
    # resolve units: only directly after a number (ignoring spaces) or ° / %
    for i, (k, t, r) in enumerate(out):
        if r == "U?":
            j = i - 1
            while j >= 0 and out[j][2] == "W":
                j -= 1
            if j >= 0 and (out[j][0] in ("num", "supsub") or out[j][1] in ("°",)):
                out[i] = (k, t, "U")
            elif re.search(SUP_RE, t):
                out[i] = ("unitalone", t, "M")
            elif len(t) <= 2 and t not in STOP and t.lower() not in STOP:
                out[i] = (k, t, "X?")
            else:
                out[i] = (k, t, "X?")
    KNOWN = {"FoS", "Fr", "Re", "pH", "FS", "SF", "OCR", "PI", "LL", "PL", "LI", "RC", "CBR", "RQD", "SPT"}
    for i, (k, t, r) in enumerate(out):
        if r != "X?" or k != "word" or not t.isalpha():
            continue
        nx = next((o for o in out[i + 1:] if o[2] != "W"), None)
        pv = next((o for o in reversed(out[:i]) if o[2] != "W"), None)
        glued_l = i > 0 and out[i - 1][2] == "M" and out[i - 1][0] != "rel"
        glued_r = i + 1 < len(out) and out[i + 1][2] == "M" and out[i + 1][0] != "rel"
        near_rel = (nx and nx[0] == "rel") or (pv and pv[0] == "rel")
        caps = t.isupper() or t in KNOWN
        mixed = not t.islower() and not t.isupper()
        if t in KNOWN and 2 <= len(t) <= 4 and near_rel:
            out[i] = ("acro", t, "M")
        elif caps and 2 <= len(t) <= 4 and near_rel and t.lower() not in STOP:
            out[i] = ("acro", t, "M")
        elif 2 <= len(t) <= 3 and (mixed or t.isupper()) and (glued_l or glued_r):
            out[i] = ("prod", t, "M")
        elif len(t) == 2 and t.islower() and t not in STOP and (glued_l or glued_r or near_rel):
            out[i] = ("prod", t, "M")
        elif mixed and len(t) <= 3 and near_rel:
            out[i] = ("prod", t, "M")
        else:
            out[i] = (k, t, "X")
    return out


ANCHOR_KINDS = {"sym", "supsub", "func", "chem", "unitalone", "acro"}


def _has_anchor(run) -> bool:
    kinds = [k for k, t, r in run]
    if any(k in ANCHOR_KINDS for k in kinds):
        return True
    if any(r == "U" and re.search(SUP_RE, t) for k, t, r in run):
        return True
    if any(t in ("√", "∑", "Σ", "∫", "∞", "½", "¼", "¾", "⅓", "⅔") for k, t, r in run):
        return True
    # a relation with math on both sides
    for i, (k, t, r) in enumerate(run):
        if k == "rel":
            left = any(x[2] in ("M", "V") and x[0] not in ("rel",) for x in run[:i])
            right = any(x[2] in ("M", "V", "U") and x[0] != "rel" for x in run[i + 1:])
            if left and right:
                return True
    return False


def _trim(run):
    changed = True
    while changed and run:
        changed = False
        # whitespace
        if run and run[0][2] == "W":
            run = run[1:]; changed = True; continue
        if run and run[-1][2] == "W":
            run = run[:-1]; changed = True; continue
        # trailing/leading dangling operators or relation
        if run and run[-1][0] in ("op", "rel") and run[-1][1] not in ("|", "°", "°C", "%", "‰", "…", "½", "¼", "¾", "⅓", "⅔", "∞"):
            run = run[:-1]; changed = True; continue
        if run and run[0][0] == "rel":
            run = run[1:]; changed = True; continue
        if run and run[0][0] == "op" and run[0][1] in ("/", "×", "·", "–", "+", "="):
            run = run[1:]; changed = True; continue
        # unbalanced brackets at the ends
        txt = [t for k, t, r in run]
        opens = sum(t in "([{" for t in txt)
        closes = sum(t in ")]}" for t in txt)
        if run and run[0][0] == "open" and opens > closes:
            run = run[1:]; changed = True; continue
        if run and run[-1][0] == "close" and closes > opens:
            run = run[:-1]; changed = True; continue
        # bold markers must pair inside the run
        nb = sum(r == "B" for k, t, r in run)
        if nb % 2:
            if run[0][2] == "B":
                run = run[1:]
            elif run[-1][2] == "B":
                run = run[:-1]
            else:
                return []
            changed = True; continue
        # lone latin letters at the ends need an operator neighbour
        for end in (0, -1):
            if run and run[end][2] == "V":
                nb_ = run[1:] if end == 0 else run[:-1]
                nb_ = [x for x in (nb_ if end == 0 else reversed(nb_)) if x[2] != "W"]
                if not nb_ or nb_[0][0] not in ("rel", "op", "open", "close", "sym", "num"):
                    run = run[1:] if end == 0 else run[:-1]
                    changed = True
                    break
    return run


def _render(run) -> str:
    out = []
    i = 0
    toks = list(run)
    while i < len(toks):
        k, t, r = toks[i]
        if r == "B":
            # find matching closing bold
            j = next(j for j in range(i + 1, len(toks)) if toks[j][2] == "B")
            out.append(r"\boldsymbol{" + _render(toks[i + 1:j]).strip() + "}")
            i = j + 1
            continue
        if k == "num":
            out.append(re.sub(r"(\d)[ \u202f](\d{3})", r"\1\\,\2", re.sub(r"(\d)[ \u202f](\d{3})", r"\1\\,\2", t))
                       .replace("−", "-"))
        elif k == "sym" and re.fullmatch(r"(?:[στεγ][′']?|Σ ?[FM]|∂[uvw])[xyz]{1,2}", t):
            m = re.fullmatch(r"([στεγ][′']?|Σ ?[FM]|∂[uvw])([xyz]{1,2})", t)
            out.append(_tex_chars(m[1].replace("Σ", "Σ ")).strip().replace("\\sum", "\\sum ").replace("  ", " ")
                       + "_{" + m[2] + "}")
        elif k == "sym":
            out.append(_sym(t))
        elif k == "func":
            base = re.sub(SUP_RE + "+$", "", t)
            sup = t[len(base):]
            out.append("\\" + base.lower() + ("^{" + "".join(SUPS[c] for c in sup) + "}" if sup else "") + " ")
        elif k == "prod":
            out.append(t)
        elif k == "acro":
            out.append(r"\mathrm{" + t + "}")
        elif k in ("chem", "unitalone"):
            body = re.sub(SUP_RE + "+", lambda m: "^{" + "".join(SUPS[c] for c in m.group(0)) + "}", t)
            body = re.sub(SUB_RE + "+", lambda m: "_{" + "".join(SUBS[c] for c in m.group(0)) + "}", body)
            out.append(r"\mathrm{" + body.replace("·", r"\cdot ") + "}")
        elif r == "U":
            out.append(_unit(t))
        elif k == "supsub":
            if t[0] == "^":
                out.append("^{" + _script(t[1:]) + "}")
            elif t[0] in SUPS:
                out.append("^{" + "".join(SUPS[c] for c in t) + "}")
            else:
                out.append("_{" + "".join(SUBS[c] for c in t) + "}")
        elif k == "rel":
            out.append({"=": " = ", "≈": r" \approx ", "≤": r" \le ", "≥": r" \ge ", "<": " < ", ">": " > ",
                        "≠": r" \neq ", "≡": r" \equiv ", "∝": r" \propto "}[t])
        elif k == "op":
            out.append({"+": " + ", "−": " - ", "-": " - ", "×": r" \times ", "·": r" \cdot ", "/": "/",
                        "±": r" \pm ", "∞": r"\infty ", "∫": r"\int ", "∑": r"\sum ", "Σ": r"\sum ",
                        "∂": r"\partial ", "|": "|", "–": r"\text{–}", "…": r"\ldots ", "½": r"\tfrac12 ",
                        "¼": r"\tfrac14 ", "¾": r"\tfrac34 ", "⅓": r"\tfrac13 ", "⅔": r"\tfrac23 ",
                        "√": r"\sqrt "}.get(t, t))
        elif k in ("open", "close"):
            out.append({"{": r"\{", "}": r"\}"}.get(t, t))
        elif r == "V":
            out.append(t)
        elif r == "W":
            out.append(" ")
        else:
            out.append(_tex_chars(t))
        i += 1
    s = ""
    for piece in out:
        if re.search(r"\\[a-zA-Z]+$", s) and piece[:1].isalpha():
            s += " "
        s += piece
    # √(…) → \sqrt{…}
    for _ in range(3):
        s = re.sub(r"\\sqrt *\(([^()]*(?:\([^()]*\)[^()]*)*)\)", r"\\sqrt{\1}", s)
    s = re.sub(r"\\sqrt *((?:[A-Za-z]|\\[a-z]+)(?:_\{[^}]*\}|_[A-Za-z0-9])?|[0-9.]+)", r"\\sqrt{\1}", s)
    s = re.sub(r" {2,}", " ", s).strip()
    s = s.replace("{ ", "{").replace(" }", "}").replace("( ", "(").replace(" )", ")")
    return s


def convert(text: str) -> str:
    if not isinstance(text, str) or not text:
        return text
    if re.search(r"(?m)^\|", text):
        lines = []
        for line in text.split("\n"):
            if line.startswith("|") and not re.fullmatch(r"[|\-: ]+", line):
                cells = line.split("|")
                lines.append("|".join(_convert_inline(c) if c.strip() else c for c in cells))
            elif line.startswith("|"):
                lines.append(line)
            else:
                lines.append(_convert_inline(line))
        return "\n".join(lines)
    return _convert_inline(text)


def _convert_inline(text: str) -> str:
    if not text:
        return text
    if "$" in text and not re.search(r"\$[^$]+\$", text):
        text = text.replace("$", r"\$")
    text = (text.replace("ȳ", "y\u0304").replace("ā", "a\u0304").replace("Ū", "U\u0304").replace("ū", "u\u0304")
            .replace("x̄", "x\u0304"))
    toks = _classify(list(_tokens(text)))
    bpos = [i for i, t in enumerate(toks) if t[2] == "B"]
    partner = {}
    for a, b in zip(bpos[0::2], bpos[1::2]):
        partner[a], partner[b] = b, a
    res, i = [], 0
    n = len(toks)
    while i < n:
        if toks[i][2] == "X" or toks[i][0] == "sep":
            res.append(toks[i][1]); i += 1; continue
        j = i
        while j < n and toks[j][2] != "X" and toks[j][0] != "sep":
            j += 1
        idx = list(range(i, j))
        # split points: bold markers whose partner lies outside; "f_y 265"-style value lists
        cuts = set()
        for x in idx:
            if toks[x][2] == "B" and partner.get(x, -1) not in idx:
                cuts.add(x)
            if toks[x][2] == "W" and x - 1 >= i and x + 1 < j and toks[x - 1][2] in ("M", "V") and \
                    toks[x - 1][0] in ("sym", "prod", "acro", "word") and (
                        toks[x + 1][0] == "num" or (toks[x + 1][2] == "B" and x + 2 < j and toks[x + 2][0] == "num")):
                cuts.add(x)
        piece = []
        for x in idx:
            if x in cuts:
                if piece:
                    for pc in _split_unmatched(piece):
                        res.append(_convert_seg(pc))
                    piece = []
                res.append(toks[x][1])
            else:
                piece.append(toks[x])
        if piece:
            for pc in _split_unmatched(piece):
                res.append(_convert_seg(pc))
        i = j
    out = "".join(res)
    out = re.sub(r"\$([^$]+)\$", lambda m: "$" + _tidy(m.group(1)) + "$", out)
    for _ in range(3):   # lone letters in a list of symbols: w, γ, γ_d, e, n, S_r
        out = re.sub(r"(?<=\$, )([A-Za-z])(?=, |$|\.)", r"$\1$", out)
        out = re.sub(r"(?:(?<=^)|(?<=, ))([A-Za-z])(?=, \$)", r"$\1$", out)
    return out


def _split_unmatched(seg):
    """Split a token run at brackets that have no partner inside it; those brackets stay as text."""
    stack, bad = [], set()
    pairs = {")": "(", "]": "[", "}": "{"}
    for idx, (k, t, r) in enumerate(seg):
        if k == "open":
            stack.append((idx, t))
        elif k == "close":
            if stack and stack[-1][1] == pairs[t]:
                stack.pop()
            else:
                bad.add(idx)
    bad |= {idx for idx, _ in stack}
    pieces, cur = [], []
    for idx, tok in enumerate(seg):
        if idx in bad:
            if cur:
                pieces.append(cur)
            pieces.append([("plain", tok[1], "X")])
            cur = []
        else:
            cur.append(tok)
    if cur:
        pieces.append(cur)
    return pieces


def _convert_seg(seg) -> str:
    if len(seg) == 1 and seg[0][2] == "X":
        return seg[0][1]
    core = _trim(seg)
    if not (core and _has_anchor(core)):
        return "".join(t for k, t, r in seg)
    a = next(x for x in range(len(seg)) if seg[x:x + len(core)] == core)
    pre, post = seg[:a], seg[a + len(core):]
    if core[0][1] == "(" and core[-1][1] == ")" and _balanced_whole(core):
        mid = "($" + _render(core[1:-1]) + "$)"
    else:
        mid = "$" + _render(core) + "$"
    return "".join(t for k, t, r in pre) + mid + "".join(t for k, t, r in post)


def _tidy(s: str) -> str:
    s = re.sub(r" +(\\[ ,])", r"\1", s)
    s = re.sub(r"(^|[=(,]|\\le|\\ge|\\approx|\\times|\{) *- (?=[\d\\A-Za-z])", r"\1 -", s).strip()
    s = re.sub(r"\{ -", "{-", s)
    s = re.sub(r" +'", "'", s)
    s = re.sub(r"\b([fF])'c\b", r"\1'_c", s)
    s = re.sub(r"\^\{(\w)\}", r"^\1", s)
    s = re.sub(r"_\{(\w)\}", r"_\1", s)
    s = re.sub(r"(\\(?:sin|cos|tan|cot|sec|ln|log|exp|max|min|sqrt|sinh|cosh|tanh|sum|int)) +(?=[{(\[\\^_'])",
               r"\1", s)   # \tan (… → \tan(…
    s = re.sub(r"(\\[a-zA-Z]+) +(?=[A-Za-z])", r"\1 ", s)
    return s


def _balanced_whole(core) -> bool:
    depth = 0
    for idx, (k, t, r) in enumerate(core):
        if t == "(":
            depth += 1
        elif t == ")":
            depth -= 1
            if depth == 0 and idx != len(core) - 1:
                return False
    return depth == 0
