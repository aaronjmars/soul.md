# Reproducible Data Pipeline

This is the intended reproducible build for improving the steipete soul file.

## 1. Collect public writing

```bash
mkdir -p data/raw/{blog,github,x,transcripts}

# Blog posts: use the GitHub edit links on steipete.me or clone the site repo if public.
# Recommended seed URLs:
# - https://steipete.me/posts/just-talk-to-it
# - https://steipete.me/posts/2025/optimal-ai-development-workflow
# - https://steipete.me/posts/2025/essential-reading-july-2025
# - https://steipete.me/posts/2025/essential-reading-august-2025

# GitHub repos
for repo in \
  openclaw/openclaw openclaw/lobster \
  steipete/poltergeist steipete/peekaboo steipete/codexbar steipete/claude-code-mcp; do
  git clone --depth 1 https://github.com/$repo data/raw/github/${repo#*/} || true
done

find data/raw/github -name 'README.md' -o -name 'VISION.md' -o -name 'AGENTS.md' > data/github-files.txt
```

## 2. Add social/archive data

Export or scrape only public/permitted sources:

- X/Twitter archive for `@steipete` and `@openclaw`, preserving threads and timestamps.
- Public podcast/talk transcripts: Pragmatic Engineer, Claude Code Anonymous, conference appearances.
- Public OpenClaw showcase/shoutout pages and docs.

Normalize to JSONL:

```json
{"source":"blog","url":"...","date":"2025-10-14","text":"..."}
{"source":"x","url":"...","date":"...","thread_id":"...","text":"..."}
{"source":"github","repo":"steipete/poltergeist","path":"AGENTS.md","text":"..."}
```

## 3. Segment and label

Split into chunks by natural unit:

- post section
- tweet/thread item
- README section
- podcast answer

Add labels:

- topic: `openclaw`, `agentic-engineering`, `apple`, `tooling`, `startup`, `workflow`
- mode: `short-take`, `essay`, `docs`, `reply`, `rant`, `tutorial`
- strength: `high-voice`, `medium-voice`, `reference-only`

## 4. Build soul

Run the soul builder over high/medium voice material:

```bash
soul-builder build data/normalized.jsonl --out examples/steipete
```

Then manually edit for:

- factual accuracy
- avoiding private/unverified claims
- separating identity from style
- keeping examples synthetic unless licensing permits direct quotes

## 5. Evaluate

Use prompts:

1. “Write Peter’s take on a new OpenClaw skill that wraps Playwright.”
2. “Write a short post about Claude Code plugins.”
3. “Explain OpenClaw to a skeptical iOS developer.”
4. “Compare MCP vs CLI for agent workflows.”
5. “React to a screenshot-based bugfix workflow.”

Score 1-5 on:

- specificity
- tool/workflow realism
- voice match
- absence of corporate AI language
- predictive usefulness

## 6. Weak-model gate

Load only `SOUL.md`, `STYLE.md`, and examples into a cheap model such as gpt-4o-mini. The voice passes if at least 4/5 evaluation prompts score 4+ without becoming generic AI slop.
