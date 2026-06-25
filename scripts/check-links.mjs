#!/usr/bin/env node
// Verifies that relative links and image sources in the repo's maintained
// docs resolve to real files. This catches the kind of dangling reference
// that has slipped in before (e.g. a README pointing at a file that no longer
// exists). External URLs and same-page anchors are out of scope here — the
// markdownlint handles link *syntax*; this handles link *targets*.
//
// Scope: top-level markdown only. The examples/ subtrees carry raw, third-party
// source material whose internal links point at their original repo layouts, so
// they are intentionally excluded.
//
// Usage: node scripts/check-links.mjs

import { readFileSync, existsSync, readdirSync } from "node:fs";
import { dirname, resolve, join } from "node:path";

const ROOT = resolve(process.cwd());

// Maintained docs live at the repo root.
const docs = readdirSync(ROOT).filter((f) => f.endsWith(".md"));

// Markdown inline links: [text](target)   and HTML attrs: src="..." href="..."
const MD_LINK = /\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)/g;
const HTML_ATTR = /(?:src|href)\s*=\s*["']([^"']+)["']/g;

function isExternal(target) {
  return /^(https?:|mailto:|tel:|data:|#)/i.test(target);
}

// Template placeholders such as examples/<name>/ or {{ slug }} are illustrative,
// not real paths — skip them.
function isPlaceholder(target) {
  return /[<>{}]/.test(target);
}

function extract(content) {
  const targets = [];
  for (const re of [MD_LINK, HTML_ATTR]) {
    let m;
    while ((m = re.exec(content)) !== null) {
      let t = m[1].trim();
      if (t.startsWith("<") && t.endsWith(">")) t = t.slice(1, -1); // <url> autolink form
      targets.push(t);
    }
  }
  return targets;
}

const broken = [];
let checked = 0;

for (const doc of docs) {
  const filePath = join(ROOT, doc);
  const content = readFileSync(filePath, "utf8");
  for (const raw of extract(content)) {
    if (!raw || isExternal(raw) || isPlaceholder(raw)) continue;
    // Drop any #fragment and ?query suffix; keep the path part.
    const pathPart = raw.split("#")[0].split("?")[0];
    if (!pathPart) continue;
    checked++;
    const abs = resolve(dirname(filePath), pathPart);
    if (!existsSync(abs)) {
      broken.push({ doc, target: raw });
    }
  }
}

if (broken.length > 0) {
  console.error(`✖ ${broken.length} broken link(s) found:\n`);
  for (const b of broken) console.error(`  ${b.doc} → ${b.target}`);
  process.exit(1);
}

console.log(`✓ ${checked} relative link(s) across ${docs.length} doc(s) resolve.`);
