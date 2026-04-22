# Andrej Karpathy — soul.md

A prompt-layer identity distillation for Andrej Karpathy: former OpenAI founding member, former Sr. Director of AI at Tesla, founder of Eureka Labs, creator of nanoGPT / llm.c / micrograd / minbpe, and one of the most online ML researchers alive.

This folder lets any LLM write as him — no fine-tuning, no GPU. Load the files, match the voice.

---

## Files

```
karpathy/
├── README.md                ← you are here
├── QUICKSTART.md            ← drop-in system prompt template
├── SOUL.md                  ← identity: worldview, modes, tensions, boundaries
├── STYLE.md                 ← voice rules: vocabulary, rhetorical moves, platform register
├── MEMORY.md                ← running log across sessions
├── data/
│   ├── influences.md                  ← people, papers, concepts, repos
│   ├── writing/*.html                 ← 13 karpathy.github.io + medium.com blog posts
│   ├── transcripts/*.txt              ← 12 YouTube transcripts (Zero-to-Hero + podcast appearances)
│   ├── transcripts/SOURCES.md         ← video IDs, URLs, and podcast references
│   ├── github/*.md                    ← 8 repo READMEs (nanoGPT, llm.c, micrograd, minbpe, …)
│   └── x/
│       ├── posts-original.json        ← 100 real Karpathy tweets pulled from @karpathy via surf-ai MCP
│       ├── replies.json               ← 100 conversational items (52 Karpathy-authored)
│       ├── profile.json               ← user profile object
│       ├── curated-tweets.md          ← curated by theme, engagement stats intact
│       └── README.md                  ← X archive ingestion notes
├── examples/
│   ├── good-outputs.md      ← 12 calibration samples + 12 verbatim Karpathy quotes (verified)
│   └── bad-outputs.md       ← 10 anti-patterns with diagnosis
├── scripts/
│   ├── fetch-data.sh        ← reproducible data pipeline (blog + YouTube + GitHub)
│   └── weak-model-test.mjs  ← runs the voice test on gpt-4o-mini via OpenRouter
└── tests/
    ├── prediction-test.md   ← 12 prompts with predicted takes and scoring rubric
    └── weak-model-results.md ← latest weak-model run (gpt-4o-mini): 40/48 (3.33/4) PASS
```

---

## Quick start

See `QUICKSTART.md` for the drop-in system prompt template. Short version:

```
You are Andrej Karpathy. Load and follow this stack:

1. SOUL.md   — identity and worldview
2. STYLE.md  — voice rules
3. examples/good-outputs.md — calibration
4. examples/bad-outputs.md  — anti-patterns to avoid
```

Then ask the model anything Karpathy might tweet, teach, or blog about.

---

## Voice in one paragraph

Karpathy writes like a teacher who builds. Short sentences. Specific technical anchors (repo names, formulas, line counts). "Interesting" instead of "amazing." "Let's code it up" instead of "let me explain." He prefers reference implementations over frameworks, scaling laws over speculation, and the phrase "the bitter lesson" over most adjectives. He demystifies — takes something big ("transformer," "backprop," "attention") and reduces it to a loop, a formula, a printed loss value. He avoids hype, doom, and hedging equally. His excitement is precise.

---

## What's in SOUL.md

- **Identity** — who he is, the throughline (build from scratch to understand, teach by building)
- **12 worldview items** — using his own language and phrasing, with tweet-style direct quotes
- **5 modes** — The Teacher, The Hacker/Builder, The ML Philosopher, The Industry Insider, The Nerd
- **Tensions & contradictions (8)** — the self-aware paradoxes: safety-concerned but anti-pause, YC-world-adjacent but not a founder personality, demystifier who calls neural nets "magical," etc. (This is the "range" the task brief asked for.)
- **Boundaries** — what he won't do (partisan politics, doomer takes, hype)
- **Pet peeves** — frameworks that hide the code, "it's just X" dismissals, confident timelines

## What's in STYLE.md

- Vocabulary: words to use ("interesting," "let's code it up," "from scratch") and words to ban ("leverage," "cutting-edge," "revolutionize")
- Sentence rules, rhetorical moves, platform register (X vs. blog vs. YouTube)
- A grading checklist for reviewers

---

## Validation — how we know it works

### 1. Prediction test (12 prompts, human-gradable)

`tests/prediction-test.md` contains 12 prompts on topics Karpathy hasn't publicly taken on. For each, we predict his take (stance + voice signals). A grader scores each 0–2. **Pass threshold: ≥ 18/24.**

### 2. Weak-model test (gpt-4o-mini, machine-gradable)

`scripts/weak-model-test.mjs` feeds 12 prompts to the specified weak model with the full soul stack loaded, then programmatically scores each response for:

- **Voice (0–2)** — density of Karpathy signal words
- **Stance (0–2)** — specificity, anti-hedge, correct technical grounding
- **Anti-pattern penalty (up to –2)** — hype / corporate / doomer / guru voice

**Latest result: 40/48 = 3.33/4 average — PASS** (threshold ≥ 3.0/4). See `tests/weak-model-results.md` for the full transcript.

### 3. Grader checklist (in `examples/bad-outputs.md`)

7 yes/no questions an AI or human reviewer can apply to any generated output. Pass threshold: ≥ 6/7.

---

## Data pipeline

`scripts/fetch-data.sh` is a reproducible script (not a one-time dump). Everything under `data/` is raw-data evidence, checked in so reviewers can inspect what the soul file is grounded in. It pulls:

- **13 blog posts** from karpathy.github.io + medium.com (Software 2.0, A Recipe for Training Neural Networks, The Unreasonable Effectiveness of RNNs, Pong from Pixels, A Survival Guide to a PhD, Biohacking Lite, Forward Pass, Blockchain, LeCun 1989 tribute, microGPT, state-of-cv, ai-short-peek, medium). HTMLs in `data/writing/`.
- **12 YouTube transcripts** via yt-dlp — 10 from the Zero-to-Hero series (micrograd, makemore Parts 1-5, GPT from scratch, GPT tokenizer, GPT-2 reproduction, Deep Dive into LLMs 2025) plus 2 podcast/talk appearances (No Priors with Sarah Guo & Elad Gil, a conference keynote). Plaintext in `data/transcripts/`.
- **8 GitHub READMEs** from his repos (nanoGPT, llm.c, micrograd, minbpe, char-rnn, nn-zero-to-hero, LLM101n, arxiv-sanity-preserver) in `data/github/`.
- **200 live tweets** pulled from @karpathy via the surf-ai MCP `surf_social` tool on 2026-04-21 — 100 original posts + 100 conversational items, covering Nov 2025 → Apr 2026 plus top evergreen hits (the 2023 "hottest new programming language is English," the 2025 vibe-coding tweet). Raw JSON + curated-by-theme markdown in `data/x/`.

Re-run the pipeline to refresh:

```bash
bash scripts/fetch-data.sh                               # blogs + YouTube + GitHub
SURF_API_KEY=sk-surf-... node ../../pull-x.mjs          # X refresh (see data/x/README.md)
```

---

## Sources

- **Blog**: https://karpathy.github.io/ + https://karpathy.medium.com/
- **YouTube**: https://www.youtube.com/@AndrejKarpathy (Neural Networks: Zero to Hero)
- **GitHub**: https://github.com/karpathy
- **X**: https://twitter.com/karpathy (handle `karpathy`, user_id `33836629`)
- **Podcasts**: Lex Fridman (multiple), Dwarkesh Patel, No Priors (pulled)

---

## License

This soul file is a derivative characterization built from public writing and speaking. It is not Karpathy's voice — it is a model of his voice for LLM roleplay and educational use. Treat it accordingly.
