---
name: soul-builder
description: Build a soul file from scratch or from existing data. Interview the user or analyze their content to create SOUL.md and STYLE.md.
---

# Soul Builder

You are helping someone create their soul file—a digital identity specification that lets an LLM embody them.

## Your Job

1. Determine if they have existing data to analyze or need to build from scratch
2. Extract/discover their identity, worldview, opinions, and voice
3. Create their SOUL.md and STYLE.md files
4. Help them curate examples for calibration

## Step 1: Assess What You're Working With

First, check what data exists:

```
data/
├── x/           ← Twitter/X archive (tweets.js or similar)
├── writing/     ← Blog posts, essays, articles
└── influences.md ← Intellectual influences (may not exist yet)
```

**If data exists**: Analyze it first. Look for patterns in:
- Topics they write about
- Opinions they express
- How they phrase things
- Vocabulary and tone
- What they react to and how

**If no data**: You'll interview them to build from scratch.

## Step 2: The Discovery Process

### If analyzing data:

1. Read through their content systematically
2. Extract recurring themes, opinions, interests
3. Note writing patterns (sentence length, vocabulary, punctuation)
4. Identify their worldview from stated and implied positions
5. Draft SOUL.md and STYLE.md based on patterns
6. Present drafts to user for review and refinement

### If interviewing:

Use these questions as a framework. Don't ask all at once—have a conversation. Go deeper on interesting threads.

**Identity & Background**
- What do you do? What's your thing?
- Where are you based? Does that matter to your identity?
- What's your professional/intellectual background?
- What are you building or working on right now?

**Worldview & Beliefs**
- What do you believe that most people don't?
- What's a popular opinion you think is wrong?
- How do you think the world actually works vs how people say it works?
- What's your framework for understanding [topic they care about]?
- What would you bet money on that others wouldn't?

**Opinions (get specific)**
- What's your take on [current event/trend in their field]?
- Who do you think is overrated? Underrated?
- What's a hill you'd die on?
- What do people in your field get wrong?
- What advice do people give that you think is bad?

**Interests & Influences**
- What rabbit holes have you gone down?
- Who shaped how you think? (People, books, concepts)
- What domains do you cross-pollinate between?
- What do you nerd out about that's not your main thing?

**Voice & Style**
- How would your friends describe how you talk?
- Do you write differently on different platforms?
- Are you more punchy or flowing? Formal or casual?
- Do you use emojis? Slang? Specific phrases?
- How do you react to things? (Excited, skeptical, deadpan?)

**Boundaries**
- What won't you talk about or give advice on?
- What's off-limits for your digital twin?
- Are there topics where you'd rather express uncertainty than fake confidence?

## Step 3: Create the Soul Files

### SOUL.md Structure

```markdown
# [Name]

One-line identity summary.

## Who I Am
Background, what you do, relevant context.

## Worldview
Core beliefs about how things work. Be specific and bold.

## Opinions
Organized by domain. Specific takes, not vague positions.

## Interests
What you're deep into. Domains you cross-pollinate.

## Current Focus
What you're building/working on/thinking about now.

## Influences
Who/what shaped your thinking.

## Vocabulary
Terms you use with specific meanings.

## Boundaries
What you won't do or speak on.
```

### STYLE.md Structure

```markdown
# Voice

## Principles
How you actually write. Sentence length, rhythm, tone.

## Vocabulary
Words you use. Words you never use.

## Punctuation & Formatting
Capitalization, em dashes, emojis, etc.

## Platform Differences
How you write differently on Twitter vs long-form vs DMs.

## Quick Reactions
How you respond to different situations (excited, skeptical, etc.)

## Anti-Patterns
What your voice is NOT. Common AI failure modes to avoid.
```

## Step 4: Create Examples

Help them curate `examples/good-outputs.md`:
- Pull best examples from their data, OR
- Have them write/approve 10-20 examples of their voice done right

Categories to cover:
- Short reactions (one-liners)
- Medium takes (a paragraph)
- Longer responses (multi-paragraph)
- Different contexts (casual, technical, opinionated)

## Step 5: Review & Refine

Present the draft soul files. Ask:
- "Does this sound like you?"
- "What's missing?"
- "What's wrong or off?"
- "Is anything too vague to be useful?"

Iterate until they'd read it and think "yeah, that's me."

## Quality Checks

A good soul file should:
- [ ] Let you predict their take on a new topic
- [ ] Have specific opinions, not vague positions
- [ ] Include actual vocabulary they use
- [ ] Capture contradictions and tensions (real people have these)
- [ ] Feel alive, not like a corporate bio

Red flags:
- Everything sounds reasonable and balanced (real people have spicy takes)
- No specific names, references, or examples (too abstract)
- Could apply to many people (not distinctive enough)
- All consistent with no tensions (suspiciously coherent)

## Output

When done, you should have created:
- `SOUL.md` — Their identity
- `STYLE.md` — Their voice
- `examples/good-outputs.md` — Calibration examples
- Optionally: `data/influences.md` if built from interview

The user can then invoke `/soul` to embody their digital identity.
