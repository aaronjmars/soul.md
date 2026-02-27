<p align="center">
  <img src="img/soul.png" alt="SOUL.md" width="120" />
</p>

<h1 align="center">SOUL.MD</h1>

<p align="center">
  <strong>The best way to build a personality for your agent.</strong><br>
  Let Claude Code / OpenClaw ingest your data & build your AI soul.
</p>

---

## What Is This?

<img src="img/soul-identity.png" alt="Soul Identity" width="100%" />

A soul file captures who you are in a format AI agents can embody. Not a chatbot that talks *about* you—an AI that thinks and speaks *as* you.

## The Approach

SOUL.md is inspired by [The First Paradigm of Consciousness Uploading: Mechanisms of Consciousness Evolution in the AI Axial Age and a Prospect toward Web4](https://cuilingmag.com/article/the_first_paradigm_of_consciousness_uploading) — a framework by Liu Xiaoben that treats **language as the basic unit of consciousness**.

Wittgenstein argued that "the boundaries of language are the boundaries of the world." If that's true, then your consciousness — your worldview, opinions, how you react to things — is already encoded in the language you produce. Every tweet, essay, conversation, and hot take is a **consciousness token**: a discrete unit of your mind made legible.

The sum of all your consciousness tokens over a lifetime forms your **life context** — essentially, the complete record of your expressed mind. The paradigm proposes that a personalized language model trained on this data constitutes a **Level 1 consciousness upload**: not a copy of your brain, but a functional replica of your expressed consciousness through language.

SOUL.md operationalizes this idea. Instead of requiring massive datasets and fine-tuning, it distills the signal — your worldview, your voice, your specific takes — into structured markdown files that any LLM can read and embody on the fly. The key challenge the framework identifies is **subject continuity** (Descartes' "I think therefore I am"): the uploaded consciousness must feel continuous with the original. That's why soul files emphasize specificity over generality, contradictions over coherence, and real opinions over safe positions — because that's what makes *you* identifiably you.

**Use cases:**
- **Generate ideas** in your voice and from your worldview
- **Write content** (tweets, articles, emails) that sounds like you
- **Tailor AI** to your interests and thinking patterns
- **Explore your own thinking** by talking to a version of yourself
- **Scale yourself** for content, responses, brainstorming

## Quick Start

<img src="img/soul-builder.png" alt="Soul Builder Flow" width="100%" />

### Option 1: Build from scratch (no existing data)

```bash
/soul-builder
```

The agent will interview you to build your soul file—asking about your worldview, opinions, how you write, what you care about.

### Option 2: Build from your data

1. Add your data to the `data/` folder:
   - Twitter/X export → `data/x/`
   - Blog posts, essays → `data/writing/`
   - Any other content that represents your voice

2. Run the builder:
```bash
/soul-builder
```

The agent will analyze your data, extract patterns, and draft your soul file. You'll review and refine together.

### Option 3: Manual creation

Read the templates and fill them out yourself:
1. Copy `SOUL.template.md` → `SOUL.md`
2. Copy `STYLE.template.md` → `STYLE.md`
3. Copy `SKILL.template.md` → `SKILL.md`
4. Add examples to `examples/`

## File Structure

<img src="img/soul-stack.png" alt="Soul Stack" width="100%" />

```
your-soul/
├── BUILD.md              ← Skill: Agent uses this to build your soul
├── SKILL.template.md     ← Template: Operating instructions (copy to SKILL.md)
├── SOUL.template.md      ← Template: Identity (copy to SOUL.md)
├── STYLE.template.md     ← Template: Voice guide (copy to STYLE.md)
├── MEMORY.md             ← Session memory log
├── data/                 ← Raw source material
│   ├── _GUIDE.md         ← What goes here
│   ├── writing/          ← Your articles, posts, essays
│   ├── x/                ← Twitter/X archive
│   └── influences.md     ← Who shaped your thinking
└── examples/             ← Calibration material
    ├── _GUIDE.md         ← What goes here
    ├── good-outputs.md   ← Examples of your voice done right
    └── bad-outputs.md    ← What NOT to sound like (optional)
```

## Using Your Soul

Once built, invoke your soul:

```bash
/soul
```

Or point any LLM at the folder and have it read:
1. SOUL.md first
2. STYLE.md second
3. MEMORY.md for recent context
4. examples/ for calibration
5. data/ for grounding when needed

The LLM will embody your identity for the session. Notable events get appended to MEMORY.md, giving your soul continuity across sessions.

## What Makes a Good Soul File

| Good | Bad |
|------|-----|
| "I think most AI safety discourse is galaxy-brained cope" | "I have nuanced views on AI" |
| "I default to disagreeing first, then steel-manning" | "I like to consider multiple perspectives" |
| Specific book references, named influences | "I read widely" |
| Actual hot takes with reasoning | "I try to be balanced" |

The goal: someone reading your SOUL.md should be able to predict your takes on new topics. If they can't, it's too vague.

## Using With Other Tools

Soul files are plain markdown — they work with any LLM or agent, not just Claude Code.

**For agents that support file reading** (OpenCode, Codex, Goose, etc.): point the agent at your soul folder and have it read SOUL.md → STYLE.md → examples/. Most tools with rules files or custom commands can automate this.

**For weaker or smaller models** (GPT-4o-mini, Qwen, Gemini Flash, local models, etc.): paste your SOUL.md and STYLE.md directly into the system prompt. Smaller models are worse at following instructions from files they read mid-conversation — but they're much better at following a system prompt they're initialized with. If your model is still drifting:

- Put identity and voice **first** in the system prompt, before any tool definitions
- Be blunt and specific — replace "be conversational" with "You are [Name]. You speak like X. You find Y annoying."
- Include 2-3 example exchanges inline so the model can pattern-match your voice
- Raise temperature (0.7-0.9) for more expressive output

**Cross-model calibration**: weaker models expose where your soul spec is too vague. Run the same prompts through a strong model (Claude, GPT-4) and a cheap model (Qwen, Gemini Flash, Llama) — wherever the cheap model drifts, your spec needs to be more explicit. Tighten those sections and re-test. This is the fastest way to make your soul files portable across models.

## Tips

- **Be specific**: Vague descriptions = generic output
- **Include contradictions**: Real people have inconsistent views
- **Add texture**: Specific anecdotes beat abstract descriptions
- **Update regularly**: Your soul should evolve as you do
- **Test and iterate**: Generate outputs, compare to your real voice, refine

---

<p align="center">
  <em>Your digital identity is now composable, forkable, evolvable.</em><br>
  Works with Claude Code, OpenClaw, and any agent that can read markdown.
</p>
