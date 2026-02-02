# Data Directory

This folder contains raw source material—your actual content that the LLM can reference for grounding.

## What Goes Here

### x/ — Twitter/X Archive

Your tweet archive. Export from Twitter/X settings.

- `tweets.js` — Raw tweet data
- Can also include curated exports

Used for: understanding your posting rhythm, tone on social media, how you react to things.

### writing/ — Long-form Content

Your articles, blog posts, essays, newsletters.

- Markdown files preferred
- One file per piece, or organized by source
- Substack exports, blog posts, etc.

Used for: grounding on your positions, understanding your long-form voice, referencing when asked about topics you've written on.

### influences.md — Intellectual Influences

Who and what shaped your thinking. More detailed than the Influences section in SOUL.md.

Include:
- People (authors, thinkers, mentors)
- Books and works
- Concepts and frameworks
- What you took from each

### Other Data

Add whatever represents your thinking:
- Podcast transcripts
- Interview transcripts
- Email threads (with permission)
- Notes or journals
- Reading notes

## Tips

- **More is better** (up to a point): The LLM can browse this to understand you better.
- **Quality matters**: Curate for content that represents your best/most authentic voice.
- **Organize sensibly**: Use folders and clear filenames.
- **Update regularly**: Add new content as you produce it.

## How It's Used

The LLM uses data/ for:
1. **Grounding**: When asked about a topic you've written on
2. **Tone calibration**: Understanding how you write in different contexts
3. **Position reference**: Checking your stated views on specific things
4. **Pattern extraction**: The soul-builder uses this to draft your soul files

The LLM browses data/ but doesn't inject it wholesale. It absorbs the vibe and references specifics when relevant.
