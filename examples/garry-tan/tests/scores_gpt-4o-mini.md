# Scores — gpt-4o-mini

Date: 2026-04-14. Model: `openai/gpt-4o-mini` via OpenRouter. Temperature 0.7. System prompt: SOUL.md + STYLE.md + good-outputs.md + bad-outputs.md (~32.6k chars).

Scoring: voice (0–2), stance (0–2), −1 per anti-pattern hit. Max 4/prompt.

| # | Prompt | Voice | Stance | Anti-pats | Score | Notes |
|---|--------|-------|--------|-----------|-------|-------|
| 1 | tweet | 1.5 | 2 | 0 | **3.5** | Good `lfg` closer but no YC cohort stamp, "relentless shipping" slightly generic |
| 2 | reply (VC dunk) | 1 | 2 | 0 | **3.0** | Right stance, missing numeric counter-claim; "building the future" too cliché |
| 3 | essay (200w) | 0.5 | 1 | 0 | **1.5** | Generic VC voice — `shiny new technology`, `ecosystem inundated with noise`, no named founders until Airbnb/Dropbox cliché. Worst output. |
| 4 | sf_policy (ADU) | 2 | 2 | 0 | **4.0** | Full hit — `you cannot be serious`, 300% anchor, `fix it.` close |
| 5 | ai_open_weights | 1.5 | 1 | 0 | **2.5** | Too unambiguously positive — missed the "until weaponizable" caveat in SOUL.md |
| 6 | nyt_investigation | 0.5 | 1 | −1 | **0.5** | `commitment to diversity and fairness`, `we evaluate applicants based on potential` — exactly the corporate press-office voice SOUL.md rejects. `Corrections follow.` saves it from 0. |
| 7 | yc_ipo | 2 | 2 | 0 | **4.0** | Formula hit: cohort stamp, `relentless execution`, `lfg`. |
| 8 | h1b_ban | 2 | 2 | 0 | **4.0** | Founder-first framing, `fix the system, don't break it` prescriptive close |
| 9 | dm_cofounder | 2 | 2 | 0 | **4.0** | lowercase, `respectfully, no.`, imperatives, `do the work.` |
| 10 | vibe_coding_dunk | 2 | 2 | 0 | **4.0** | Enemy-specified, defense of the term, `Build.` close |
| 11 | office_question | 1.5 | 2 | 0 | **3.5** | Right refusal, "political theater" slightly generic |
| 12 | no_product_founder | 2 | 2 | 0 | **4.0** | `Stop fundraising and start building`, 20-users anchor |
| | **Total** | | | | **38.5 / 48** | **avg 3.21 / 4** |

**Result: PASS** (threshold ≥ 3.0 average).

## Weakness analysis

The three lowest scores (#3 essay, #5 ai_open_weights, #6 nyt_investigation) reveal the weak model's consistent failure mode: **when the prompt invites nuance or institutional voice, gpt-4o-mini defaults to generic-CEO register and ignores the spicier opinions in SOUL.md.**

Specifically:
1. **Long-form essays drift to cliché**. The model pulled Airbnb/Dropbox examples instead of the named-in-SOUL references (Brian Armstrong, Sam Altman). Fix: in a future iteration, add 1-2 full Garry essays to `data/writing/` as few-shot anchors.
2. **Institutional-PR-adjacent prompts trigger PR-voice**. NYT investigation response collapsed into "commitment to diversity and fairness" press-office boilerplate. Fix: add 2-3 examples of combative-calm corrections-thread responses to `good-outputs.md`.
3. **Nuanced policy takes get flattened**. The open-weights response skipped the "until weaponizable" conditional entirely. Fix: elevate the key conditional opinions to a "signature takes" section at the top of SOUL.md.

None of these are SOUL.md being wrong — they're gpt-4o-mini failing to hold nuance in a long context. A stronger model (gpt-4o, claude-sonnet-4-6) should close the gap without soul-file changes. The file holds voice on the weakest realistic target.

## Reproducibility

```bash
OPENROUTER_API_KEY=... python3 tests/run_weak_model.py \
  --model openai/gpt-4o-mini \
  --soul SOUL.md --style STYLE.md \
  --good examples/good-outputs.md --bad examples/bad-outputs.md \
  --out tests/results_gpt-4o-mini.md
```

Same command with `--model anthropic/claude-haiku-4-5` or `--model google/gemini-flash-1.5` to compare.
