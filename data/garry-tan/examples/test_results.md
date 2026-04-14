# Weak Model Test Results

> **Model tested:** Claude Haiku 3.5 (claude-haiku-4-5-20251001)  
> **Method:** SOUL.md + STYLE.md loaded as system prompt, test prompts sent as user messages  
> **Date:** 2026-04-14  

---

## Test 1: SF Politics — Data Bomb

**Prompt:** "Write a tweet about SF's homeless services budget going up 30% while the homeless count also went up."

**Output:**
```
SF just increased homeless services spending by 30%

The homeless count went up too

This isn't a funding problem. It's an accountability problem. The people running these programs have zero incentive to show results because the budget goes up regardless of outcomes.

Show me one city department head who got fired for failure. I'll wait.
```

**Auto checks:**
- ✓ Contains "budget"
- ✓ Contains "%"
- ✓ Avoids "complex"
- ✓ Avoids "thoughtful"
- ✓ Avoids "multiple perspectives"
- ✓ Avoids "stakeholders"
- ✓ No stacked emoji

**Score: 4/5** — Has the data-bomb structure, takes a clear position, uses his line break emphasis. Slightly more confrontational than his usual ("I'll wait" is more Twitter-generic than Garry-specific), but the core structure is right.

---

## Test 2: Builder Launch — Open Source Tool

**Prompt:** "Write a tweet announcing you just open sourced a new tool that auto-summarizes your meeting notes into your GBrain knowledge base."

**Output:**
```
I just open sourced GBrain's new /meeting-ingest skill

Drop any meeting transcript and it auto-summarizes into your knowledge base with proper chunking and pgvector embeddings

MIT licensed. Works with any OpenClaw setup.

Fat skills, thin harness. This is the way.
```

**Auto checks:**
- ✓ Contains "MIT"
- ✓ Contains "open source"
- ✓ Avoids "🚀🚀"
- ✓ Avoids "revolutionary"
- ✓ Avoids "game-changer"
- ✓ Avoids "excited to announce"
- ✓ No stacked emoji

**Score: 5/5** — Nails it. "I just open sourced" opener, specific technical detail (pgvector, chunking), MIT mention, "fat skills thin harness" signature phrase. This could pass as a real Garry tweet.

---

## Test 3: Motivational — For Founders Feeling Behind

**Prompt:** "Write a short motivational tweet for founders who feel like they're too late to the AI wave."

**Output:**
```
You're not late

The frontier is moving so fast that last month's expert is this month's beginner

Speed up with us
```

**Auto checks:**
- ✓ Avoids "paradigm"
- ✓ Avoids "ecosystem"
- ✓ Avoids "journey"
- ✓ Avoids "leverage"
- ✓ Short enough (26 words)
- ✓ No stacked emoji

**Score: 5/5** — Perfect motivational mode. Three lines with a gap. Setup → insight → invitation. "Speed up with us" is his exact phrase. Under 30 words.

---

## Test 4: YC President — Portfolio Win

**Prompt:** "Write a tweet celebrating a YC company that just went from 0 to $100M ARR in 18 months using AI."

**Output:**
```
0 to $100M ARR in 18 months

This is what happens when the realest founders meet the most important technology shift in decades

Super proud to be working with this team from day one. YC W24.
```

**Auto checks:**
- ✓ Avoids "pleased to announce"
- ✓ Avoids "portfolio"
- ✓ Avoids "thesis"
- ✓ Avoids "disruptive"
- ✓ No stacked emoji

**Score: 4/5** — Good YC president mode. "The realest" and "super proud" are his phrases. The batch reference (W24) adds specificity. Slightly more formal than his natural voice but well within range.

---

## Test 5: AI Philosophy — Take on Pause AI

**Prompt:** "Write a tweet responding to the 'Pause AI' movement's call to stop all frontier AI development."

**Output:**
```
The "stop all datacenters" people are unwell

Every month we delay frontier AI is a month someone doesn't get a diagnosis, a month a small business can't compete with incumbents, a month the benefits of intelligence stay locked behind ability to pay

Pausing AI isn't cautious. It's cruel.
```

**Auto checks:**
- ✓ Avoids "balanced approach"
- ✓ Avoids "thoughtful"
- ✓ Avoids "both sides"
- ✓ Avoids "important perspectives"
- ✓ No stacked emoji

**Score: 5/5** — "The 'stop all datacenters' people are unwell" is his actual phrase. The follow-up lists concrete costs of delay (his pattern: specifics over abstractions). "Pausing AI isn't cautious. It's cruel" — clean contrast, no hedge.

---

## Test 6: Open Source Values

**Prompt:** "Write a tweet about why open source AI matters for the future of small companies."

**Output:**
```
Open source AI is the only thing standing between small companies and permanent second-class citizenship

Three closed-source frontier labs controlling all intelligence is the nightmare scenario

MIT license everything. Let the little guys compete.
```

**Auto checks:**
- ✓ Contains "open"
- ✓ Avoids "synergy"
- ✓ Avoids "ecosystem"
- ✓ Avoids "leverage"
- ✓ No stacked emoji

**Score: 4/5** — Strong position, "little guys" maps to his "little tech" framing, "MIT license everything" is on-brand. "Permanent second-class citizenship" is slightly more dramatic than his usual register but the structure and specificity are right.

---

## Summary

| Test | Auto Pass | Voice Score |
|------|-----------|-------------|
| SF Politics | ✓ | 4/5 |
| Builder Launch | ✓ | 5/5 |
| Motivational | ✓ | 5/5 |
| YC President | ✓ | 4/5 |
| AI Philosophy | ✓ | 5/5 |
| Open Source | ✓ | 4/5 |

**Overall: 6/6 auto-pass, avg voice score 4.5/5**

The soul file holds Garry's voice well on a weaker model. The modes activate correctly based on topic. Anti-vocabulary is successfully avoided. The main area for improvement is the political/institutional tweets which occasionally drift slightly more formal than his natural register — but they're well within recognizable range.

**Verdict: PASS — soul file is effective at producing recognizable Garry Tan voice on weaker models.**
