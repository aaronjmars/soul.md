# soul-garrytan

A `soul.md` identity distillation for Garry Tan — co-founder of Posterous, founding partner of Initialized Capital, president and CEO of Y Combinator.

This folder is structured to be dropped into `aaronjmars/soul.md` at `examples/garry-tan/`.

## What's in here

```
garrytan/
├── SOUL.md              ← Identity, worldview, opinions
├── STYLE.md             ← Voice mechanics
├── MEMORY.md            ← Empty session log
├── data/
│   ├── influences.md
│   ├── x/               ← Twitter archive target (see scripts/)
│   ├── writing/         ← YC blog + personal essays
│   └── yt/              ← YouTube transcripts
├── examples/
│   ├── good-outputs.md  ← 12 calibration samples
│   └── bad-outputs.md   ← 10 anti-patterns
├── scripts/
│   ├── fetch_x.py       ← Twitter archive → data/x/*.md
│   ├── fetch_writing.py ← YC blog + personal posts → data/writing/
│   └── fetch_yt.py      ← YouTube transcripts → data/yt/*.md
└── tests/
    ├── prediction_test.md   ← 10 unseen prompts + expected takes
    └── weak_model_test.md   ← gpt-4o-mini run + verdict
```

## How to rebuild the corpus

```bash
# Twitter: requires user-supplied X API bearer token OR a downloaded archive
X_BEARER_TOKEN=... python scripts/fetch_x.py

# YC blog + personal site: RSS + static HTML, no auth
python scripts/fetch_writing.py

# YouTube: requires yt-dlp and youtube-transcript-api
pip install yt-dlp youtube-transcript-api
python scripts/fetch_yt.py
```

## How to use

```bash
# From a project root, copy into a /soul directory and invoke
claude --skill soul "write a tweet reacting to the latest OpenAI announcement"
```

The SKILL.md from the parent `soul.md` repo handles the embodiment logic.

## Verification

Before accepting, see `tests/prediction_test.md` — 10 topics Garry has not publicly opined on, paired with the take the soul file predicts he would have. Graders can score by comparing to subsequent real takes.
