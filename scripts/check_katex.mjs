// Render every math span with KaTeX (throwOnError). Input: JSON file [{where, tex, display}].
// Usage: node scripts/check_katex.mjs spans.json   → prints failures, exit 1 if any.
import fs from "node:fs";
import katex from "katex";

const spans = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
let bad = 0;
for (const s of spans) {
  try {
    katex.renderToString(s.tex, { throwOnError: true, displayMode: !!s.display, strict: "ignore" });
  } catch (e) {
    bad++;
    console.log(`${s.where}\n  ${s.tex}\n  → ${e.message}`);
  }
}
console.log(`${spans.length} spans checked, ${bad} failed`);
process.exit(bad ? 1 : 0);
