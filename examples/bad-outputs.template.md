# Bad Outputs — [Your Name]

<!--
Anti-patterns. What "sounding wrong" looks like for you specifically.
This file is what catches AI drift before it ships.

Generic anti-patterns (corporate voice, emoji spam, hedging) belong in
STYLE.md. This file is for the *person-specific* failure modes — the
drifts that look fine in isolation but feel wrong coming from you.

Aim for 8–12 examples. Each one: the bad output, a diagnosis of *why*
it's wrong, and ideally a rewrite showing how you'd actually say it.

The rewrites are the most useful part — they teach the model the
correction, not just the rejection.
-->

[One-sentence summary of what this file catches: how many anti-patterns,
what failure modes they cover.]

---

## 1. [Failure-mode name — e.g. Generic thought-leader voice]

**Bad:**
> [Example of the wrong voice. Make it specific. AI failure modes are
> usually a cluster of small tells, not one obvious flag.]

**Why it's wrong:** [Diagnose the tells — specific phrases, structural
moves, tonal choices. "Every word on the never-use list" beats "feels
off." Then show how you'd actually say it: "You'd say: [rewrite]."]

---

## 2. [Failure-mode name — e.g. Wrong register for the topic]

**Bad:**
> [Example.]

**Why it's wrong:** [Diagnosis + rewrite.]

---

## 3. [Failure-mode name — e.g. Over-hedged]

**Bad:**
> [Example.]

**Why it's wrong:** [Diagnosis + rewrite.]

---

## 4. [Failure-mode name — e.g. Right voice, wrong opinion]

<!--
Worth including: outputs where the voice is plausible but the *position*
is wrong for you. The LLM nailing your style while putting words in your
mouth is a distinctive failure mode worth flagging.
-->

**Bad:**
> [Example.]

**Why it's wrong:** [Diagnosis + rewrite.]

---

## 5. [Failure-mode name]

**Bad:**
> [Example.]

**Why it's wrong:** [Diagnosis + rewrite.]

---

<!--
QUALITY CHECK:
- Does each example catch a *distinct* failure mode? Two examples of the
  same drift = one wasted slot.
- Are the diagnoses pointing at specific tells, or just saying "feels off"?
- Do the rewrites show the correction clearly? If not, the model learns
  what to avoid but not what to do.
- Are you catching person-specific drifts, or just listing generic AI
  failure modes? Generic ones belong in STYLE.md.
-->
