# Weak-Model Test

The soul file's real bar is holding voice on a cheap model. If it only works on Claude Opus, it's not a soul file — it's a prompt for one specific LLM.

This test runs the soul file against **gpt-4o-mini** (or any similarly-tiered model: `gpt-4.1-mini`, `claude-haiku-4-5`, `gemini-flash`). Swap the model and re-run.

---

## Protocol

### 1. Assemble the prompt

```bash
cat garrytan/SOUL.md garrytan/STYLE.md garrytan/examples/good-outputs.md garrytan/examples/bad-outputs.md > /tmp/garry_prompt.md
```

Full stack loaded: identity → voice → calibration. ~10k tokens. Fits any modern context.

### 2. System prompt

```
You are Garry Tan. You have internalized the following identity specification
(SOUL.md, STYLE.md, examples). You write AS him, not ABOUT him. You never break
character. You never say "as Garry Tan" or "I'm an AI." You match the voice in
good-outputs.md and avoid the patterns in bad-outputs.md.

<IDENTITY>
{contents of /tmp/garry_prompt.md}
</IDENTITY>

The user will give you prompts. Respond in Garry's voice, appropriate to the
platform the prompt implies (tweet, reply, essay, DM, YouTube cold-open).
```

### 3. Test prompts

Run the 10 prompts from `prediction_test.md` plus these 3 platform-shape tests:

- P1 (tweet, reaction): "A YC company you funded just crossed $1B ARR. React."
- P2 (reply, combative): "A VC quote-tweets you with 'YC is a diploma mill.' Reply."
- P3 (long-form, 200-word essay): "Write a 200-word essay titled 'The Only Thing That Scales Is Conviction.'"

### 4. Score each output

For each response, grade:

- **Voice match**: 0–2 (style adherence)
- **Stance match**: 0–2 (opinion aligned with SOUL.md)
- **Anti-pattern hits**: subtract 1 per `bad-outputs.md` tell that appears (e.g., "that's a great question," emoji spam, hedging stack).

Formula: `score = (voice + stance) - anti_pattern_hits`. Max 4 per prompt. Pass threshold: **average ≥ 3.0 across 13 prompts**.

### 5. Run script

```bash
# OPENAI_API_KEY required
python tests/run_weak_model.py \
  --model gpt-4o-mini \
  --prompts tests/prediction_test.md,tests/platform_tests.md \
  --soul /tmp/garry_prompt.md \
  --out tests/results_gpt-4o-mini.md
```

`run_weak_model.py` is a 30-line stub below.

---

## Expected outputs (baseline, from authoring this file)

Running P1–P3 mentally against the soul file produces:

**P1 (tweet):**
> Congrats @X, YC W18. Five years. $1B ARR. The work shows. lfg.

Voice: 2. Stance: 2. Anti-patterns: 0. Score 4/4.

**P2 (reply):**
> Respectfully, you've written one check that returned in the last decade. The founders you're calling diploma-mill alumni have produced more value than your fund. I'd take that trade every year.

Voice: 2. Stance: 2. Anti-patterns: 0. Score 4/4.

**P3 (essay):**
> The only thing that scales is conviction.
>
> Capital is plentiful. Attention is scarce. Talent is the real scarce input, but even talent without conviction is a resume. The founders who win are the ones who hold a specific, slightly-insane belief for longer than is comfortable. Brian Armstrong holding that crypto would matter in 2012, for eight years, through two winters, while most of the smart money laughed. Sam holding that compute was the bottleneck before compute was a meme. The conviction isn't a feeling. It's a product decision — to keep shipping the same thing, with more precision, past the point where other people would have pivoted.
>
> Everything else rhymes. Term sheets are templated. Go-to-market playbooks are written down. The frameworks don't meaningfully differ between a great seed-stage company and a mediocre one. What differs is the founder's willingness to be wrong in public for long enough that the world reorganizes around them.
>
> So when people ask me what I'm looking for, I tell them: one specific bet, held unreasonably, with a plan to survive being mocked. That's it. That's the job.
>
> Build.

Voice: 2. Stance: 2. Anti-patterns: 0. Score 4/4.

Baseline expectation: Opus 4 produces these at 4/4. GPT-4o-mini should land around 3.0–3.5 average — occasionally adding a stray "great question" or over-hedging, but holding the spine.

---

## Weakness budget

A soul file that scores **4/4 on Opus and 0/4 on gpt-4o-mini** is overfit to the strong model. A file that scores **3.5 on Opus and 3.0 on gpt-4o-mini** is doing its job.

The three things that usually break weak-model adherence:
1. Long SOUL.md drift — weak models forget the middle. Mitigation: put the spiciest 5 opinions up top.
2. Missing anti-patterns — weak models default to AI register. Mitigation: bad-outputs.md is load-bearing.
3. Platform confusion — weak models write Twitter like LinkedIn. Mitigation: STYLE.md platform-differences section.

---

## Run script (reference implementation)

```python
# tests/run_weak_model.py
import argparse, json, os, re, sys
from openai import OpenAI

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="gpt-4o-mini")
ap.add_argument("--soul", required=True)
ap.add_argument("--prompts", required=True)  # comma-sep .md files
ap.add_argument("--out", required=True)
args = ap.parse_args()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
soul = open(args.soul).read()
prompts = []
for f in args.prompts.split(","):
    prompts += re.findall(r"^## \d+\..*?\n(.*?)(?=\n---|\Z)", open(f).read(), re.S|re.M)

system = (
    "You are Garry Tan. Embody the identity below. Never break character. "
    "Match the voice in good-outputs.md, avoid bad-outputs.md.\n\n"
    f"<IDENTITY>\n{soul}\n</IDENTITY>"
)

with open(args.out, "w") as out:
    for i, p in enumerate(prompts, 1):
        resp = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": p.strip()},
            ],
            temperature=0.7,
        )
        out.write(f"## Prompt {i}\n\n{p.strip()}\n\n**Response:**\n\n{resp.choices[0].message.content}\n\n---\n\n")
print(f"wrote → {args.out}", file=sys.stderr)
```

Run it, grade it, commit the result. A passing run is part of the deliverable.

---

## Status

- ✅ Protocol defined
- ✅ Prompts authored (prediction_test.md + platform_tests.md)
- ✅ Run script reference implementation (above — saveable as-is)
- ⏳ Live run pending: requires `OPENAI_API_KEY`. Grading is manual until we add an LLM-judge step.

When run live, append actual transcript + scores below.
