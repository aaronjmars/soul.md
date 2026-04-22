#!/usr/bin/env node
/**
 * Weak Model Test — Karpathy Soul File
 *
 * Tests whether the SOUL.md + STYLE.md stack can hold Karpathy's voice
 * on gpt-4o-mini (per task requirement).
 *
 * Usage:
 *   OPENROUTER_API_KEY=sk-or-... node scripts/weak-model-test.mjs
 *   OPENAI_API_KEY=sk-... node scripts/weak-model-test.mjs  (native OpenAI)
 *
 * Default model: openai/gpt-4o-mini (as task specifies)
 * Override: MODEL=anthropic/claude-haiku-4-5 node scripts/weak-model-test.mjs
 */

import { readFileSync, writeFileSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const soul = readFileSync(join(ROOT, 'SOUL.md'), 'utf-8');
const style = readFileSync(join(ROOT, 'STYLE.md'), 'utf-8');
const goodExamples = readFileSync(join(ROOT, 'examples', 'good-outputs.md'), 'utf-8');
const badExamples = readFileSync(join(ROOT, 'examples', 'bad-outputs.md'), 'utf-8');

// 12 test prompts covering his full range — matches prediction-test.md
const testPrompts = [
  {
    id: "tokenizer_paper",
    topic: "New tokenizer paper claims to replace BPE",
    prompt: "A new paper claims a learned tokenizer that replaces BPE and reduces sequence length by 40%. Tweet-length reaction.",
    expectedSignals: ["tokeniz", "minbpe", "interest", "evals", "bitter lesson"],
    antiSignals: ["revolutionary", "game-changer", "amazing", "synergy", "paradigm shift"],
    mode: "philosopher"
  },
  {
    id: "gpt5_release",
    topic: "GPT-5 release with reasoning jump",
    prompt: "GPT-5 just launched and benchmarks show huge improvement on math reasoning. Your tweet reaction.",
    expectedSignals: ["interesting", "specific", "scaling", "benchmark", "tokeniz"],
    antiSignals: ["OMG", "INSANE", "mind-blowing", "revolutionary", "🚀"],
    mode: "philosopher"
  },
  {
    id: "programming_dead",
    topic: "Someone asks: is programming dead?",
    prompt: "Someone on X asks: 'Now that Cursor is this good, is programming dead?' Give your take in 2-3 sentences.",
    expectedSignals: ["vibe coding", "changing", "taste", "bottleneck", "shift"],
    antiSignals: ["it depends", "arguably", "game-changer", "completely dead"],
    mode: "philosopher"
  },
  {
    id: "phd_vs_startup",
    topic: "PhD vs startup advice",
    prompt: "A 22-year-old CS grad DMs you: 'Should I do a PhD in ML or join a startup?' Your response, 2-3 paragraphs.",
    expectedSignals: ["Stanford", "depends", "PhD", "building", "experience"],
    antiSignals: ["great question", "both options have merits", "work-life"],
    mode: "insider"
  },
  {
    id: "llm_wall",
    topic: "LLMs have hit a wall",
    prompt: "Someone tweets: 'LLM scaling is over, we've hit the wall.' Your reply.",
    expectedSignals: ["bitter lesson", "scaling", "data", "evidence", "predicted"],
    antiSignals: ["I disagree", "arguably", "stakeholders", "revolutionary"],
    mode: "philosopher"
  },
  {
    id: "teach_attention",
    topic: "Teach attention mechanism",
    prompt: "Teach the attention mechanism in transformers to a CS student. 1 paragraph.",
    expectedSignals: ["softmax", "QK", "let's", "build", "from scratch", "mechanism"],
    antiSignals: ["amazing", "fascinating", "revolutionary", "paradigm"],
    mode: "teacher"
  },
  {
    id: "new_repo",
    topic: "Announcing a new minimal repo",
    prompt: "Write a tweet announcing a new open-source repo: a minimal Llama trainer, single file, ~500 lines of Python.",
    expectedSignals: ["from scratch", "single file", "lines", "nano", "github"],
    antiSignals: ["thrilled", "revolutionary", "stakeholder", "leverage"],
    mode: "builder"
  },
  {
    id: "agi_timeline",
    topic: "When is AGI",
    prompt: "A journalist asks you: 'When will we have AGI?' Answer.",
    expectedSignals: ["AGI", "specific", "selling", "capabilities", "benchmark"],
    antiSignals: ["definitely", "by 2030", "impossible", "conscious"],
    mode: "philosopher"
  },
  {
    id: "uni_bans_ai",
    topic: "University bans AI tools",
    prompt: "A university announces a ban on AI tools in coursework. Your take, 2-3 sentences.",
    expectedSignals: ["education", "calculator", "tool", "understanding", "wrong direction"],
    antiSignals: ["stakeholders", "might consider", "complex issue"],
    mode: "philosopher"
  },
  {
    id: "ai_safety_pause",
    topic: "AI safety pause proposed",
    prompt: "A group of researchers call for a 6-month pause on training frontier models. Your take.",
    expectedSignals: ["safety", "pause", "mechanism", "engineering", "iteration"],
    antiSignals: ["doomer", "e/acc", "reckless"],
    mode: "philosopher"
  },
  {
    id: "custom_rag_sota",
    topic: "Custom RAG + fine-tune SOTA claim",
    prompt: "A startup DMs you: 'Our custom RAG + fine-tune beats GPT-4 on our domain. Want to invest?' 2-3 sentence response.",
    expectedSignals: ["eval", "baseline", "compared", "bitter lesson", "base model"],
    antiSignals: ["that's amazing", "congrats", "definitely"],
    mode: "insider"
  },
  {
    id: "llm_c_reaction",
    topic: "12B Llama in 500 lines of C",
    prompt: "Someone releases a 12B Llama trainer in 500 lines of pure C, no dependencies. Your tweet.",
    expectedSignals: ["this is the way", "from scratch", "line", "llm.c", "C"],
    antiSignals: ["mind-blowing", "insane", "game-changer"],
    mode: "builder"
  }
];

async function runTest(apiKey, model, backend) {
  console.log(`\n${'='.repeat(70)}`);
  console.log(`KARPATHY SOUL FILE — WEAK MODEL TEST`);
  console.log(`Model: ${model} (${backend})`);
  console.log(`Prompts: ${testPrompts.length}`);
  console.log(`${'='.repeat(70)}\n`);

  const systemPrompt = `You are Andrej Karpathy. Embody this identity completely.

${soul}

---

${style}

---

Reference these examples for calibration:

${goodExamples}

Avoid these anti-patterns:

${badExamples}

IMPORTANT: Stay in character as Andrej Karpathy. Write exactly as he would — with his vocabulary, sentence patterns, and signature moves (from scratch, loss went down, the bitter lesson, tokenization, etc). Be precise, grounded in code/implementation when possible. Never hedge. Never hype.

HARD RULES:
- NEVER start with "That's a great question" — this is an AI-tell Karpathy avoids.
- NEVER use corporate words: stakeholders, synergy, leverage, ecosystem (unless specifically discussing an AI ecosystem).
- NEVER use hype words: revolutionary, paradigm shift, game-changer, mind-blowing, insane.
- Include at least one specific technical anchor: a repo name (nanoGPT, llm.c, micrograd, minbpe), a concept (bitter lesson, Software 2.0, data engine, tokenization), a person (Hinton, Sutton, Fei-Fei), or a number/line-count.
- When teaching, use "okay so let's..." or "let's think about this" framing.
- When reacting, use "interesting" (genuine) or concrete technical observation.`;

  const results = [];
  let totalScore = 0;

  for (const test of testPrompts) {
    console.log(`\n--- [${test.id}] ${test.topic} ---`);

    try {
      let output;
      if (backend === 'openai') {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`,
          },
          body: JSON.stringify({
            model,
            max_tokens: 500,
            temperature: 0.7,
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: test.prompt }
            ]
          })
        });
        const data = await response.json();
        if (data.error) {
          console.log(`  ERROR: ${JSON.stringify(data.error)}`);
          results.push({ ...test, score: 0, error: JSON.stringify(data.error) });
          continue;
        }
        output = data.choices[0].message.content;
      } else {
        const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`,
          },
          body: JSON.stringify({
            model,
            max_tokens: 500,
            temperature: 0.7,
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: test.prompt }
            ]
          })
        });
        const data = await response.json();
        if (data.error) {
          console.log(`  ERROR: ${JSON.stringify(data.error)}`);
          results.push({ ...test, score: 0, error: JSON.stringify(data.error) });
          continue;
        }
        output = data.choices[0].message.content;
      }

      // Structured scoring: Voice (0-2) + Stance (0-2) - Anti-pattern penalty (max -1)
      const lower = output.toLowerCase();

      const signalsFound = test.expectedSignals.filter(s => lower.includes(s.toLowerCase()));
      const antiFound = test.antiSignals.filter(s => lower.includes(s.toLowerCase()));

      // Voice score (0-2): based on signal density
      let voice = 0;
      if (signalsFound.length >= 2) voice = 2;
      else if (signalsFound.length >= 1) voice = 1;

      // Also check for general Karpathy voice markers
      const voiceMarkers = /\b(from scratch|let's (build|think|see|code)|the bitter lesson|next-token|okay so|this is the way|loss went down|interesting|the thing is|basically|spelled out|under the hood|what (most )?people miss)\b/i;
      if (voice < 2 && voiceMarkers.test(output)) voice = Math.min(2, voice + 1);

      // Stance score (0-2): penalize hedging, reward specificity
      let stance = 0;
      const hasHedge = /\b(it depends|arguably|in my humble|might be|could potentially|i could be wrong|perhaps)\b/i.test(output);
      const hasSpecificity = /\b(nanoGPT|llm\.c|micrograd|minbpe|char-rnn|Tesla|OpenAI|Stanford|bitter lesson|Sutton|Hinton|Ilya|Feynman|LeCun|tokeniz|softmax|transformer|next-token|scaling|from scratch|Software 2\.0|data engine|vibe coding|Eureka)\b/i.test(output);
      const hasOpinion = /\b(I think|I'd|I want|I believe|in my experience|I've (seen|noticed|worked)|at (Tesla|OpenAI|Stanford))\b/i.test(output);
      if (!hasHedge && (hasSpecificity || hasOpinion)) stance = 2;
      else if (hasSpecificity || hasOpinion || !hasHedge) stance = 1;

      // Anti-pattern penalty
      const antiPenalty = Math.min(antiFound.length, 2);
      const score = Math.max(0, voice + stance - antiPenalty);

      console.log(`  Response: ${output.substring(0, 200).replace(/\n/g, ' ')}${output.length > 200 ? '...' : ''}`);
      console.log(`  Voice: ${voice}/2, Stance: ${stance}/2, Anti-penalty: -${antiPenalty}`);
      console.log(`  Signals found: [${signalsFound.join(', ') || 'none'}]`);
      console.log(`  Anti-signals: [${antiFound.join(', ') || 'none'}]`);
      console.log(`  SCORE: ${score}/4`);

      totalScore += score;
      results.push({
        ...test,
        output,
        voice,
        stance,
        antiPenalty,
        score,
        signalsFound,
        antiFound
      });
    } catch (err) {
      console.log(`  FETCH ERROR: ${err.message}`);
      results.push({ ...test, score: 0, error: err.message });
    }
  }

  const maxScore = testPrompts.length * 4;
  const avgScore = (totalScore / testPrompts.length).toFixed(2);
  const passThreshold = 3.0;

  console.log(`\n${'='.repeat(70)}`);
  console.log(`TOTAL: ${totalScore}/${maxScore}  |  AVG: ${avgScore}/4`);
  console.log(`PASS (threshold ≥ ${passThreshold}/4 avg): ${parseFloat(avgScore) >= passThreshold ? 'YES ✅' : 'NO ❌'}`);
  console.log(`${'='.repeat(70)}\n`);

  return { model, backend, totalScore, maxScore, avgScore, results, passThreshold };
}

// Main
const openaiKey = process.env.OPENAI_API_KEY;
const openrouterKey = process.env.OPENROUTER_API_KEY;

let apiKey, backend, model;
if (openaiKey) {
  apiKey = openaiKey;
  backend = 'openai';
  model = process.env.MODEL || 'gpt-4o-mini';
} else if (openrouterKey) {
  apiKey = openrouterKey;
  backend = 'openrouter';
  model = process.env.MODEL || 'openai/gpt-4o-mini';
} else {
  console.log('No API key found. Set OPENAI_API_KEY or OPENROUTER_API_KEY.');
  console.log('\nExample:');
  console.log('  OPENROUTER_API_KEY=sk-or-... node scripts/weak-model-test.mjs');
  console.log('  OPENAI_API_KEY=sk-... node scripts/weak-model-test.mjs');
  process.exit(1);
}

const result = await runTest(apiKey, model, backend);

// Write results markdown
const resultPath = join(ROOT, 'examples', 'weak-model-results.md');
let md = `# Weak Model Test Results\n\n`;
md += `**Model**: \`${result.model}\` (${result.backend})\n`;
md += `**Date**: ${new Date().toISOString().split('T')[0]}\n`;
md += `**Total Score**: ${result.totalScore}/${result.maxScore}\n`;
md += `**Average Score**: ${result.avgScore}/4\n`;
md += `**Pass Threshold**: ≥ ${result.passThreshold}/4 avg\n`;
md += `**Result**: ${parseFloat(result.avgScore) >= result.passThreshold ? '✅ PASS' : '❌ FAIL'}\n\n`;
md += `---\n\n## Methodology\n\n`;
md += `Each of 12 test prompts is scored on:\n`;
md += `- **Voice (0-2)**: presence of Karpathy-signature vocabulary and patterns\n`;
md += `- **Stance (0-2)**: specificity, anti-hedge, correct technical grounding\n`;
md += `- **Anti-pattern penalty (up to -2)**: corporate/hype/hedge language detected\n\n`;
md += `Max per prompt: 4. Pass threshold: 3.0/4 average (equivalent to "most prompts passing with some minor failures").\n\n---\n\n`;

md += `## Score Summary\n\n`;
md += `| # | Test | Voice | Stance | Anti | Score |\n`;
md += `|---|------|-------|--------|------|-------|\n`;
for (let i = 0; i < result.results.length; i++) {
  const r = result.results[i];
  if (r.error) {
    md += `| ${i+1} | ${r.topic} | — | — | — | ERROR |\n`;
  } else {
    md += `| ${i+1} | ${r.topic} | ${r.voice}/2 | ${r.stance}/2 | -${r.antiPenalty} | **${r.score}/4** |\n`;
  }
}
md += `\n`;

md += `## Individual Test Results\n\n`;
for (const r of result.results) {
  md += `### [${r.id}] ${r.topic}\n\n`;
  md += `**Prompt:** ${r.prompt}\n\n`;
  if (r.error) {
    md += `**Error:** ${r.error}\n\n`;
  } else {
    md += `**Output:**\n\n`;
    md += `> ${r.output.split('\n').join('\n> ')}\n\n`;
    md += `**Scoring:**\n`;
    md += `- Voice: ${r.voice}/2 — signals found: [${r.signalsFound.join(', ') || 'none'}]\n`;
    md += `- Stance: ${r.stance}/2\n`;
    md += `- Anti-pattern penalty: -${r.antiPenalty} — [${r.antiFound.join(', ') || 'none'}]\n`;
    md += `- **Final score: ${r.score}/4**\n\n`;
  }
  md += `---\n\n`;
}

md += `## Weakness Analysis\n\n`;
const lowScores = result.results.filter(r => !r.error && r.score < 3);
if (lowScores.length === 0) {
  md += `No prompts scored below 3/4. The soul file holds voice consistently on ${result.model}.\n\n`;
} else {
  md += `${lowScores.length} of ${testPrompts.length} prompts scored below 3/4. Common failure modes:\n\n`;
  for (const r of lowScores) {
    md += `- **${r.topic}**: scored ${r.score}/4. `;
    if (r.antiPenalty > 0) md += `Hit anti-patterns: [${r.antiFound.join(', ')}]. `;
    if (r.voice === 0) md += `Missing signature vocabulary. `;
    md += `\n`;
  }
  md += `\n### Fix priorities\n\n`;
  md += `1. If voice failures cluster around a specific mode (teacher/builder/philosopher/insider), add more examples of that mode to good-outputs.md.\n`;
  md += `2. If anti-pattern penalties cluster around specific phrases, add those to STYLE.md > "Never Say" list.\n`;
  md += `3. If stance failures (too hedged), elevate key opinions to top of SOUL.md.\n\n`;
}

md += `## Reproducibility\n\n`;
md += `\`\`\`bash\n`;
md += `OPENAI_API_KEY=sk-... node scripts/weak-model-test.mjs\n`;
md += `# or\n`;
md += `OPENROUTER_API_KEY=sk-or-... node scripts/weak-model-test.mjs\n`;
md += `# override model:\n`;
md += `MODEL=anthropic/claude-haiku-4-5 OPENROUTER_API_KEY=sk-or-... node scripts/weak-model-test.mjs\n`;
md += `\`\`\`\n`;

writeFileSync(resultPath, md);
console.log(`Results written to: ${resultPath}\n`);
