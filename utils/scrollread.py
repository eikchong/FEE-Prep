"""Scroll-based reading progress (Streamlit inline component, st.components.v2).

Each notes section on a subject page is wrapped in two zero-height markers:
    <div class="fee-rd" data-k=KEY data-w=WORDS data-p="s|e"></div>
A section counts as read when its end marker has been in view AND the section has been on screen for at least
clamp(words / 8, 2, 30) seconds in total, counting only while the tab is visible. Newly read keys go back to
Python in batches (3 s debounce) as a trigger value; only the fragment that hosts the component reruns.

The inline component API runs this JS in the app document itself (no iframe), so `window` IS the app window.
(window.parent would be Streamlit Cloud's wrapper page there.) State is kept on that window so it survives the
component being remounted when the fragment reruns. The thin "now reading" bar is client-side only; if it can't
be injected nothing else is affected.
"""
from __future__ import annotations

import html as _html

import streamlit as st

JS = r"""
export default function (component) {
  const { data, setTriggerValue } = component;
  const W = window;                       // the app document's window (inline component, no iframe)
  const doc = W.document;
  const S = W.__feeRead || (W.__feeRead = {
    sec: {}, read: new Set(), pending: new Set(), screenSecs: 0, seen: new WeakSet(),
    observer: null, ticker: null, flushTimer: null, atDone: {}, bar: null, lastMarkers: 0,
  });
  S.send = setTriggerValue;
  S.data = data || {};
  (S.data.read || []).forEach((k) => S.read.add(k));

  const need = (w) => Math.min(30, Math.max(2, (w || 0) / 8));

  function flush() {
    S.flushTimer = null;
    if (!S.pending.size && S.screenSecs < 30) return;
    const keys = Array.from(S.pending);
    const seconds = Math.round(S.screenSecs);
    try {
      S.send("read", { keys: keys, seconds: seconds, code: S.data.code || null, t: Date.now() });
      S.pending.clear();
      S.screenSecs = 0;
    } catch (e) { /* keep pending; try again on the next flush */ }
  }
  function schedule() {
    if (S.flushTimer) W.clearTimeout(S.flushTimer);
    S.flushTimer = W.setTimeout(flush, 3000);
  }

  function markers() {
    const out = {};
    doc.querySelectorAll(".fee-rd").forEach((el) => {
      const k = el.getAttribute("data-k");
      if (!k) return;
      const o = out[k] || (out[k] = { w: +el.getAttribute("data-w") || 0 });
      if (el.getAttribute("data-p") === "s") o.s = el; else o.e = el;
    });
    return out;
  }

  function observe(ms) {
    if (!S.observer && W.IntersectionObserver) {
      S.observer = new W.IntersectionObserver((entries) => {
        entries.forEach((en) => {
          if (!en.isIntersecting) return;
          const k = en.target.getAttribute("data-k");
          (S.sec[k] || (S.sec[k] = { secs: 0 })).endSeen = true;
        });
      }, { threshold: 0 });
    }
    Object.values(ms).forEach((m) => {
      if (m.e && S.observer && !S.seen.has(m.e)) { S.seen.add(m.e); S.observer.observe(m.e); }
    });
  }

  function bar(ms) {
    try {
      const d = S.data;
      if (!d.code || !Object.keys(ms).length) { if (S.bar) S.bar.style.display = "none"; return; }
      if (!S.bar) {
        const b = doc.createElement("div");
        b.id = "fee-now-reading";
        b.setAttribute("role", "status");
        b.innerHTML = '<span class="fee-nr-text"></span><span class="fee-nr-pct"></span><div class="fee-nr-track"><div class="fee-nr-fill"></div></div>';
        doc.body.appendChild(b);
        S.bar = b;
      }
      const hdr = doc.querySelector('header[data-testid="stHeader"]');
      S.bar.style.top = (hdr ? Math.max(0, hdr.getBoundingClientRect().bottom) : 0) + "px";
      const main = doc.querySelector('[data-testid="stMain"]');
      const bc = doc.querySelector('[data-testid="stMainBlockContainer"]');
      if (main) { const r = main.getBoundingClientRect(); S.bar.style.left = r.left + "px"; S.bar.style.width = r.width + "px"; }
      if (bc && main) {
        const r = bc.getBoundingClientRect(), m = main.getBoundingClientRect();
        const cs = W.getComputedStyle(bc);
        S.bar.style.paddingLeft = (r.left - m.left + parseFloat(cs.paddingLeft || 0)) + "px";
        S.bar.style.paddingRight = (m.right - r.right + parseFloat(cs.paddingRight || 0)) + "px";
      }
      S.bar.style.display = "flex";
      let topic = null;
      doc.querySelectorAll(".fee-topic").forEach((t) => {
        if (t.getBoundingClientRect().top < 140) topic = t.getAttribute("data-name");
      });
      const words = d.words || {};
      let tot = 0, got = 0;
      for (const k in words) { tot += words[k]; if (S.read.has(k)) got += words[k]; }
      const pct = tot ? Math.round(100 * got / tot) : 0;
      S.bar.querySelector(".fee-nr-text").innerHTML =
        "<strong>" + d.code + "</strong>" + (topic ? " · Now reading: " + topic : "");
      S.bar.querySelector(".fee-nr-pct").textContent = pct + "%";
      S.bar.querySelector(".fee-nr-fill").style.width = pct + "%";
      S.bar.querySelector(".fee-nr-fill").style.background = d.color || "#2a78d6";
    } catch (e) { /* the bar is decoration only */ }
  }

  function scrollToAt(ms) {
    const at = S.data.at;
    if (!at || S.atDone[at]) return;
    const m = ms[at];
    if (m && m.s) {
      S.atDone[at] = true;
      const y = m.s.getBoundingClientRect().top + W.scrollY - 110;
      const main = doc.querySelector('[data-testid="stMain"]') || doc.querySelector('section.main');
      if (main && main.scrollHeight > main.clientHeight) main.scrollTo({ top: main.scrollTop + m.s.getBoundingClientRect().top - 110 });
      else W.scrollTo({ top: y });
    }
  }

  function tick() {
    const ms = markers();
    observe(ms);
    scrollToAt(ms);
    bar(ms);
    if (doc.visibilityState !== "visible") return;
    const vh = W.innerHeight || doc.documentElement.clientHeight;
    let any = false;
    for (const k in ms) {
      const m = ms[k];
      if (!m.s || !m.e) continue;
      const top = m.s.getBoundingClientRect().top, bottom = m.e.getBoundingClientRect().bottom;
      if (top < vh && bottom > 0) {
        any = true;
        if (S.read.has(k)) continue;
        const st = S.sec[k] || (S.sec[k] = { secs: 0 });
        st.secs += 0.5;
        if (st.endSeen && st.secs >= need(m.w)) {
          S.read.add(k); S.pending.add(k); schedule();
        }
      }
    }
    if (any) { S.screenSecs += 0.5; if (S.screenSecs >= 60) schedule(); }
  }

  if (!S.ticker) {
    S.ticker = W.setInterval(tick, 500);
    doc.addEventListener("visibilitychange", () => { if (doc.visibilityState === "hidden") flush(); });
  }
  tick();
}
"""

CSS_GLOBAL = """
<style>
.st-key-fee_scroll_read, .st-key-fee_scroll_read * { height: 0 !important; min-height: 0 !important; margin: 0 !important; }
.fee-rd { height: 0; margin: 0; padding: 0; }
div[data-testid="stElementContainer"]:has(> div > .fee-rd), div[data-testid="stElementContainer"]:has(.fee-rd) { margin: 0 !important; }
#fee-now-reading { position: fixed; left: 0; width: 100%; box-sizing: border-box; z-index: 999990; display: none;
  align-items: center; gap: 16px; padding: 6px 16px; background: #ffffffee; backdrop-filter: blur(4px);
  border-bottom: 1px solid #e6e8ef; font: 14px 'Source Sans 3', 'Source Sans Pro', sans-serif; color: #5c5f6b; }
#fee-now-reading strong { color: #31333F; }
#fee-now-reading .fee-nr-text { flex: 1 1 auto; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
#fee-now-reading .fee-nr-pct { font-weight: 600; color: #31333F; }
#fee-now-reading .fee-nr-track { position: absolute; left: 0; right: 0; bottom: -1px; height: 3px; background: #e3e6ec; }
#fee-now-reading .fee-nr-fill { height: 3px; width: 0; }
</style>
"""

_COMPONENT = None


def _component():
    global _COMPONENT
    if _COMPONENT is None:
        _COMPONENT = st.components.v2.component("fee_scroll_read", js=JS, isolate_styles=False)
    return _COMPONENT


def marker(key: str, words: int, pos: str) -> None:
    st.html(f'<div class="fee-rd" data-k="{_html.escape(key)}" data-w="{int(words)}" data-p="{pos}"></div>')


def topic_marker(name: str) -> None:
    st.html(f'<div class="fee-topic" data-name="{_html.escape(name)}"></div>')


def mount(payload: dict, on_event) -> None:
    """Render the tracker once (height 0). on_event(dict) runs when a batch of read keys arrives."""
    res = _component()(data=payload, key="fee_scroll_read", on_read_change=lambda: None)
    ev = getattr(res, "read", None) if res is not None else None
    if ev:
        on_event(ev)
