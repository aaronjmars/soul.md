<p align="center">
  <img src="img/soul.jpg" alt="SOUL.md" width="120" />
</p>

<h1 align="center">SOUL.MD</h1>

<p align="center">
  <strong>The best way to build a personality for your agent.</strong><br>
  Let Claude Code / OpenClaw ingest your data & build your AI soul.<br>
  Best used with <a href="https://github.com/aaronjmars/aeon">Aeon</a> — background intelligence that evolves with you.
</p>

---

## What Is This?

<img src="img/soul-identity.jpg" alt="Soul Identity" width="100%" />

A soul file captures who you are in a format AI agents can embody. Not a chatbot that *talks about you* — an AI that *thinks and speaks as you*.

Dump your tweets, essays, and posts into a folder. The agent reads everything, extracts your worldview and voice, and builds a set of markdown files any LLM can load to write as you.

The goal: someone reading your `SOUL.md` should be able to predict your takes on new topics. If they can't, it's too vague.

**Use cases:**
- Generate ideas from your worldview
- Write content (tweets, articles, emails) that sounds like you
- Tailor AI to your interests and thinking patterns
- Scale yourself for content, responses, brainstorming

---

## Quick Start

<img src="img/soul-builder.jpg" alt="Soul Builder Flow" width="100%" />

**Option 1 — Build from scratch**
```
/soul-builder
```
The agent interviews you: worldview, opinions, how you write, what you care about.

**Option 2 — Build from your data**

Drop your content into `data/`:
```
data/x/          ← Twitter/X export
data/writing/    ← Blog posts, essays
```
Then run `/soul-builder`. It analyzes your data, extracts patterns, and drafts your soul file. You review and refine together.

**Option 3 — Manual**

Copy the templates and fill them in:
```
SOUL.template.md  → SOUL.md
STYLE.template.md → STYLE.md
SKILL.template.md → SKILL.md
```

---

## Best Used With Aeon

<img src="img/soul-sources.jpg" alt="Soul + Aeon" width="100%" />

[**Aeon**](https://github.com/aaronjmars/aeon) is an autonomous agent on GitHub Actions, powered by Claude Code. 68 skills across research, dev tooling, crypto monitoring, and productivity — all running in the background on a cron schedule.

Soul files slot directly into Aeon. Copy your soul into `soul/` in your Aeon repo, add a few lines to `CLAUDE.md`, and every skill Aeon runs — articles, digests, tweets, research briefs — gets written in your voice. No per-skill config. Identity propagates automatically.

Why this pairing works:
- **Aeon handles the when and what** — scheduling, research, monitoring, content generation
- **Soul files handle the who** — voice, worldview, opinions, style
- Together you get a background agent that doesn't just work for you — it *sounds* like you

Setup takes 2 minutes. See Aeon's [Soul section](https://github.com/aaronjmars/aeon#soul-optional) for details.

---

## Data Sources

Feed the builder anything you've written. The more signal, the sharper the output.

| Category | Platforms |
|----------|-----------|
| **Social** | Twitter/X, Bluesky, Farcaster, Mastodon, Threads, LinkedIn, Reddit |
| **Writing** | Substack, Medium, Ghost, WordPress, Mirror.xyz, Paragraph.xyz |
| **Messaging** | Discord, Telegram, Slack, iMessage exports |
| **Notes** | Notion, Obsidian, Roam Research, Logseq, Apple Notes |
| **Video/Audio** | YouTube transcripts, podcast transcripts, Loom recordings |
| **Code/Dev** | GitHub activity, Hacker News comments, Stack Overflow answers |
| **Other** | PDFs, plain text, CSV/JSON, RSS feeds, GDPR data exports |

No existing data? Option 1 (interview mode) still builds a solid soul file from scratch.

---

## Compatible Frameworks

Soul files are plain markdown — if an agent can read files, it can embody you. Tested with:

| Framework | Language | Stars |
|-----------|----------|-------|
| [Aeon](https://github.com/aaronjmars/aeon) | YAML/Markdown | — |
| [OpenClaw](https://github.com/openclaw/openclaw) | TypeScript | 322k |
| [Nanobot](https://github.com/HKUDS/nanobot) | Python | 34.6k |
| [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | Rust | 27.8k |
| [PicoClaw](https://github.com/sipeed/picoclaw) | Go | 25.3k |
| [NanoClaw](https://github.com/qwibitai/nanoclaw) | TypeScript | 24k |
| [OpenFang](https://github.com/RightNow-AI/openfang) | Rust | 14.9k |
| [IronClaw](https://github.com/nearai/ironclaw) | Rust | 10.4k |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Python | 8.7k |
| Claude Code · OpenCode · Codex · Goose | various | — |

Also works with any model via system prompt — see [Using With Other Tools](#using-with-other-tools).

---

## File Structure

<img src="img/soul-stack.jpg" alt="Soul Stack" width="100%" />

```
your-soul/
├── SOUL.md           ← Who you are (identity, worldview, opinions)
├── STYLE.md          ← How you write (voice, syntax, patterns)
├── SKILL.md          ← Operating modes (tweet, essay, chat, etc.)
├── MEMORY.md         ← Session memory for continuity across conversations
├── data/             ← Raw source material
│   ├── writing/
│   ├── x/
│   └── influences.md
└── examples/
    ├── good-outputs.md
    └── bad-outputs.md
```

---

## What Makes a Good Soul File

| Good | Bad |
|------|-----|
| "I think most AI safety discourse is galaxy-brained cope" | "I have nuanced views on AI" |
| "I default to disagreeing first, then steel-manning" | "I like to consider multiple perspectives" |
| Specific book references, named influences | "I read widely" |
| Actual hot takes with reasoning | "I try to be balanced" |

Real people have inconsistent views. Include contradictions — they're what make you identifiably you.

---

## Using Your Soul

Once built, invoke your soul:
```
/soul
```

Or point any LLM at your folder and have it read:
1. `SOUL.md` — identity
2. `STYLE.md` — voice
3. `MEMORY.md` — recent context
4. `examples/` — calibration
5. `data/` — grounding when needed

Notable events get appended to `MEMORY.md`, giving your soul continuity across sessions.

For always-on operation, pair with [Aeon](https://github.com/aaronjmars/aeon) — your soul files feed into every skill automatically, so background tasks (digests, articles, tweets, monitoring alerts) all carry your voice without any extra prompting.

---

## Using With Other Tools

Soul files are plain markdown — they work with any LLM or agent.

**For agents that support file reading** (OpenCode, Codex, Goose, etc.): point the agent at your soul folder and have it read `SOUL.md` → `STYLE.md` → `examples/`.

**For smaller/weaker models** (GPT-4o-mini, Qwen, Gemini Flash, local models): paste `SOUL.md` and `STYLE.md` directly into the system prompt. Tips if the model still drifts:
- Put identity and voice *before* tool definitions
- Be blunt: replace "be conversational" with "You are [Name]. You speak like X. You find Y annoying."
- Include 2–3 inline example exchanges for pattern-matching
- Raise temperature (0.7–0.9) for more expressive output

**Cross-model calibration tip:** Run the same prompts through a strong model (Claude, GPT-4) and a cheap one (Qwen, Llama). Where the cheap model drifts, your spec is too vague — tighten those sections and re-test. This is the fastest way to make your soul files portable.

---

## Examples

Real soul files built with this framework.

### @aaronjmars
Builder, writer, and researcher at the intersection of crypto, AI, and consciousness. Toronto-based. Active on Substack and X.

A taste of the soul spec: worldview cross-pollinates CCRU accelerationism, mechanism design, and neurotech. Voice: short sentences, lowercase, em dashes, state opinion first. Key vocabulary: hyperstition, reflexivity, templexity, vectoralism.

→ [View soul files](https://github.com/aaronjmars/soul-aaronjmars)

---

## Contribute Your Soul

Fork this repo, build your soul using the templates, host it publicly, and open a PR adding yourself to the Examples section — one paragraph bio + link + a few lines on what makes your soul spec distinctive.

What makes a contribution worth including: real opinions (not placeholders), a `STYLE.md` someone could actually calibrate from, and at least some examples.

[Open a PR →](https://github.com/aaronjmars/soul.md/pulls)

---

## Aeon Token

SOUL.md is affiliated with the [Aeon](https://github.com/aaronjmars/aeon) project and the AEON token.

Contract: [`0xbf8e8f0e8866a7052f948c16508644347c57aba3`](https://bankr.bot/agents/0xbf8e8f0e8866a7052f948c16508644347c57aba3)

---

## The Theory (Optional Background)

SOUL.md is inspired by *The First Paradigm of Consciousness Uploading* by Liu Xiaoben — a framework that treats language as the basic unit of consciousness. Wittgenstein argued that the boundaries of language are the boundaries of the world. If that's true, your consciousness is already encoded in the language you produce.

The paradigm proposes that a model trained on a lifetime of your language output constitutes a Level 1 consciousness upload — not a copy of your brain, but a functional replica of your expressed consciousness. SOUL.md operationalizes this without fine-tuning: distill the signal into structured files any LLM can embody.

The key challenge is *subject continuity*: the uploaded consciousness must feel continuous with the original. That's why soul files emphasize specificity over generality, contradictions over coherence, and real opinions over safe positions.

<p align="center">
  <em>Your identity is now composable. Forkable. Evolvable.</em><br>
  Works with <a href="https://github.com/aaronjmars/aeon">Aeon</a>, Claude Code, OpenClaw, and any agent that can read markdown.
</p>
