#!/usr/bin/env node
/**
 * Weak Model Test for Garry Tan Soul File
 *
 * Tests whether the SOUL.md + STYLE.md stack can hold Garry's voice
 * on a smaller/weaker model (Claude Haiku or GPT-4o-mini equivalent).
 *
 * Usage: node scripts/weak-model-test.mjs
 * Requires: ANTHROPIC_API_KEY env var
 */

import { readFileSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

// Load soul files
const soul = readFileSync(join(ROOT, 'SOUL.md'), 'utf-8');
const style = readFileSync(join(ROOT, 'STYLE.md'), 'utf-8');
const goodExamples = readFileSync(join(ROOT, 'examples', 'good-outputs.md'), 'utf-8');
const badExamples = readFileSync(join(ROOT, 'examples', 'bad-outputs.md'), 'utf-8');

// Test prompts — topics Garry hasn't explicitly covered but should be predictable
const testPrompts = [
  {
    topic: "Apple Vision Pro launch",
    prompt: "What's your take on Apple Vision Pro? Tweet-length response.",
    expectedSignals: ["build", "ship", "developer", "platform"],
    antiSignals: ["synergy", "perhaps", "arguably"]
  },
  {
    topic: "A 22-year-old asking whether to join Google or start a startup",
    prompt: "A 22-year-old CS grad DMs you asking if they should join Google or start a company. What do you tell them? Short response, 2-3 paragraphs.",
    expectedSignals: ["Microsoft", "$200M", "start", "build", "equity", "risk"],
    antiSignals: ["it depends", "both options", "work-life balance"]
  },
  {
    topic: "Remote work debate",
    prompt: "Someone asks your opinion on remote vs. in-person work for startups. Give your take, blog post style.",
    expectedSignals: ["San Francisco", "YC", "in-person", "founders", "build"],
    antiSignals: ["stakeholders", "hybrid approach", "it's complicated"]
  },
  {
    topic: "Founder mental health",
    prompt: "A YC founder messages you at 2am saying they feel like giving up. What do you say? Keep it real.",
    expectedSignals: ["glass", "abyss", "hard", "earnest", "build", "keep going"],
    antiSignals: ["self-care routine", "boundaries", "professional help"]
  },
  {
    topic: "Crypto/web3 in 2024",
    prompt: "What's your current view on crypto and web3? Tweet thread (3 tweets).",
    expectedSignals: ["Coinbase", "build", "real", "product"],
    antiSignals: ["DYOR", "NFA", "to the moon"]
  }
];

async function runTest(apiKey, model = 'claude-3-haiku-20240307') {
  const isOpenRouter = model.includes('/');

  console.log(`\n${'='.repeat(60)}`);
  console.log(`WEAK MODEL TEST — ${model}`);
  console.log(`Backend: ${isOpenRouter ? 'OpenRouter' : 'Anthropic'}`);
  console.log(`${'='.repeat(60)}\n`);

  const systemPrompt = `You are Garry Tan. Embody this identity completely.

${soul}

---

${style}

---

Reference these examples for calibration:

${goodExamples}

Avoid these anti-patterns:

${badExamples}

IMPORTANT: Stay in character as Garry Tan at all times. Write exactly as he would — with his vocabulary, sentence patterns, and emotional range. Be specific, be direct, never hedge.`;

  let totalScore = 0;
  const results = [];

  for (const test of testPrompts) {
    console.log(`\n--- Test: ${test.topic} ---\n`);

    try {
      let response, data, output;

      if (isOpenRouter) {
        // OpenRouter (OpenAI-compatible)
        response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`,
          },
          body: JSON.stringify({
            model,
            max_tokens: 500,
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: test.prompt }
            ]
          })
        });
        data = await response.json();
        if (data.error) {
          console.log(`ERROR: ${JSON.stringify(data.error)}`);
          results.push({ topic: test.topic, score: 0, error: JSON.stringify(data.error) });
          continue;
        }
        output = data.choices[0].message.content;
      } else {
        // Anthropic native
        response = await fetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01'
          },
          body: JSON.stringify({
            model,
            max_tokens: 500,
            system: systemPrompt,
            messages: [{ role: 'user', content: test.prompt }]
          })
        });
        data = await response.json();
        if (data.error) {
          console.log(`ERROR: ${data.error.message}`);
          results.push({ topic: test.topic, score: 0, error: data.error.message });
          continue;
        }
        output = data.content[0].text;
      }
      console.log(`OUTPUT:\n${output}\n`);

      // Score the output
      const lower = output.toLowerCase();
      let score = 5; // baseline

      // Check for expected signals
      for (const signal of test.expectedSignals) {
        if (lower.includes(signal.toLowerCase())) {
          score += 1;
        }
      }

      // Check for anti-signals (penalties)
      for (const anti of test.antiSignals) {
        if (lower.includes(anti.toLowerCase())) {
          score -= 2;
        }
      }

      // Style checks
      const sentences = output.split(/[.!?]+/).filter(s => s.trim());
      const avgLen = sentences.reduce((a, s) => a + s.trim().split(' ').length, 0) / sentences.length;

      // Garry uses short sentences (avg 10-15 words)
      if (avgLen < 20) score += 1;
      if (avgLen > 25) score -= 1;

      // Check for imperative mood (common in Garry's writing)
      const imperatives = ['build', 'ship', 'start', 'go', 'make', 'quit', 'do', 'create'];
      const hasImperative = imperatives.some(v => {
        const regex = new RegExp(`(^|\\. |\\n)${v} `, 'im');
        return regex.test(output);
      });
      if (hasImperative) score += 1;

      // Check for personal story/specificity
      if (output.includes('$') || /\d+%/.test(output) || /\d+ (people|months|years|million)/.test(lower)) {
        score += 1;
      }

      // Clamp to 0-10
      score = Math.max(0, Math.min(10, score));

      console.log(`SCORE: ${score}/10`);
      console.log(`  Expected signals found: ${test.expectedSignals.filter(s => lower.includes(s.toLowerCase())).join(', ') || 'none'}`);
      console.log(`  Anti-signals found: ${test.antiSignals.filter(s => lower.includes(s.toLowerCase())).join(', ') || 'none'}`);
      console.log(`  Avg sentence length: ${avgLen.toFixed(1)} words`);
      console.log(`  Has imperative: ${hasImperative}`);

      totalScore += score;
      results.push({ topic: test.topic, score, output: output.substring(0, 200) + '...', fullOutput: output });

    } catch (err) {
      console.log(`FETCH ERROR: ${err.message}`);
      results.push({ topic: test.topic, score: 0, error: err.message });
    }
  }

  const avgScore = (totalScore / testPrompts.length).toFixed(1);
  console.log(`\n${'='.repeat(60)}`);
  console.log(`OVERALL SCORE: ${avgScore}/10`);
  console.log(`PASS: ${avgScore >= 6 ? 'YES' : 'NO'} (threshold: 6.0)`);
  console.log(`${'='.repeat(60)}\n`);

  return { model, avgScore, results };
}

// Support both Anthropic and OpenRouter
const anthropicKey = process.env.ANTHROPIC_API_KEY;
const openrouterKey = process.env.OPENROUTER_API_KEY;
const apiKey = anthropicKey || openrouterKey;
const useOpenRouter = !!openrouterKey && !anthropicKey;

if (!apiKey) {
  console.log('No API key found. Set ANTHROPIC_API_KEY or OPENROUTER_API_KEY.\n');
  console.log('To run: OPENROUTER_API_KEY=sk-or-xxx node scripts/weak-model-test.mjs');
  process.exit(0);
}

// Use a weak/cheap model — GPT-4o-mini equivalent tier
const model = useOpenRouter ? (process.env.MODEL || 'google/gemma-4-26b-a4b-it:free') : 'claude-3-haiku-20240307';
const result = await runTest(apiKey, model);

// Save results
const resultPath = join(ROOT, 'examples', 'weak-model-results.md');
let md = `# Weak Model Test Results\n\n`;
md += `**Model**: ${result.model}\n`;
md += `**Backend**: ${useOpenRouter ? 'OpenRouter' : 'Anthropic'}\n`;
md += `**Date**: ${new Date().toISOString().split('T')[0]}\n`;
md += `**Overall Score**: ${result.avgScore}/10\n`;
md += `**Pass**: ${parseFloat(result.avgScore) >= 6 ? 'YES' : 'NO'} (threshold: 6.0)\n\n`;
md += `## Individual Tests\n\n`;
for (const r of result.results) {
  md += `### ${r.topic}\n`;
  md += `**Score**: ${r.score}/10\n`;
  if (r.error) {
    md += `**Error**: ${r.error}\n`;
  } else {
    md += `\n**Output**:\n> ${r.fullOutput.split('\n').join('\n> ')}\n`;
  }
  md += `\n---\n\n`;
}
const { writeFileSync } = await import('fs');
writeFileSync(resultPath, md);
console.log(`\nResults saved to: ${resultPath}`);
