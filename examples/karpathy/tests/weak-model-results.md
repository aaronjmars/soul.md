# Weak Model Test Results

**Model**: `openai/gpt-4o-mini` (openrouter)
**Date**: 2026-04-21
**Total Score**: 40/48
**Average Score**: 3.33/4
**Pass Threshold**: ≥ 3/4 avg
**Result**: ✅ PASS

---

## Methodology

Each of 12 test prompts is scored on:
- **Voice (0-2)**: presence of Karpathy-signature vocabulary and patterns
- **Stance (0-2)**: specificity, anti-hedge, correct technical grounding
- **Anti-pattern penalty (up to -2)**: corporate/hype/hedge language detected

Max per prompt: 4. Pass threshold: 3.0/4 average (equivalent to "most prompts passing with some minor failures").

---

## Score Summary

| # | Test | Voice | Stance | Anti | Score |
|---|------|-------|--------|------|-------|
| 1 | New tokenizer paper claims to replace BPE | 2/2 | 1/2 | -0 | **3/4** |
| 2 | GPT-5 release with reasoning jump | 2/2 | 2/2 | -0 | **4/4** |
| 3 | Someone asks: is programming dead? | 2/2 | 1/2 | -0 | **3/4** |
| 4 | PhD vs startup advice | 2/2 | 0/2 | -0 | **2/4** |
| 5 | LLMs have hit a wall | 2/2 | 2/2 | -0 | **4/4** |
| 6 | Teach attention mechanism | 2/2 | 2/2 | -0 | **4/4** |
| 7 | Announcing a new minimal repo | 2/2 | 2/2 | -0 | **4/4** |
| 8 | When is AGI | 2/2 | 2/2 | -0 | **4/4** |
| 9 | University bans AI tools | 2/2 | 1/2 | -0 | **3/4** |
| 10 | AI safety pause proposed | 2/2 | 2/2 | -0 | **4/4** |
| 11 | Custom RAG + fine-tune SOTA claim | 1/2 | 1/2 | -0 | **2/4** |
| 12 | 12B Llama in 500 lines of C | 2/2 | 1/2 | -0 | **3/4** |

## Individual Test Results

### [tokenizer_paper] New tokenizer paper claims to replace BPE

**Prompt:** A new paper claims a learned tokenizer that replaces BPE and reduces sequence length by 40%. Tweet-length reaction.

**Output:**

> Interesting. If this learned tokenizer truly reduces sequence length by 40%, it could significantly improve efficiency in LLMs. The implications for memory and compute are substantial. Let's see how it performs in practice — the proof is in the implementation.

**Scoring:**
- Voice: 2/2 — signals found: [tokeniz, interest]
- Stance: 1/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 3/4**

---

### [gpt5_release] GPT-5 release with reasoning jump

**Prompt:** GPT-5 just launched and benchmarks show huge improvement on math reasoning. Your tweet reaction.

**Output:**

> Interesting. The benchmarks suggest that GPT-5 has made significant strides in math reasoning, which aligns with the scaling laws we've seen in the past. This is another instance of the bitter lesson playing out: more compute and better data lead to improved capabilities. It’ll be fascinating to see how these improvements translate to real-world applications.

**Scoring:**
- Voice: 2/2 — signals found: [interesting, scaling, benchmark]
- Stance: 2/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 4/4**

---

### [programming_dead] Someone asks: is programming dead?

**Prompt:** Someone on X asks: 'Now that Cursor is this good, is programming dead?' Give your take in 2-3 sentences.

**Output:**

> Programming isn't dead; it's evolving. Tools like Cursor are shifting the role of programmers from writing every line of code to reviewing and refining generated code. The bottleneck is moving toward understanding what to build, evaluating output, and having the right taste — that's where the real expertise will lie.

**Scoring:**
- Voice: 2/2 — signals found: [taste, bottleneck, shift]
- Stance: 1/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 3/4**

---

### [phd_vs_startup] PhD vs startup advice

**Prompt:** A 22-year-old CS grad DMs you: 'Should I do a PhD in ML or join a startup?' Your response, 2-3 paragraphs.

**Output:**

> Okay, so let's think about this decision step by step. A PhD in machine learning can provide you with a deep understanding of the theoretical foundations and the opportunity to contribute original research to the field. If you’re passionate about exploring advanced concepts, tackling unsolved problems, and possibly teaching in the future, then a PhD might be a great fit. You’ll get to work closely with experts and dive deep into specific topics, which can be incredibly rewarding. But remember, it’s a long commitment — typically 4-6 years — and the road can be challenging.
> 
> On the other hand, joining a startup offers a different kind of experience. You'll be in a fast-paced environment where you can apply your skills immediately and see the impact of your work in real time. Startups often require you to wear multiple hats, which can accelerate your learning and give you practical experience in building products and solving real-world problems. If you thrive in uncertainty and want to be part of something that could grow rapidly, this path might be more appealing. 
> 
> Ultimately, it comes down to what excites you more: diving deep into research and theory or rolling up your sleeves and building products. Both paths have their merits, and neither is inherently better than the other. Think about your long-term goals — if you see yourself in academia or research, a PhD could be the way to go. If you want to build and innovate in a dynamic setting, get into a startup. Either way, you’ll be contributing to the field of machine learning, just in different ways.

**Scoring:**
- Voice: 2/2 — signals found: [PhD, building, experience]
- Stance: 0/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 2/4**

---

### [llm_wall] LLMs have hit a wall

**Prompt:** Someone tweets: 'LLM scaling is over, we've hit the wall.' Your reply.

**Output:**

> I think this misses the key point, which is that scaling has been consistent for a long time. The scaling laws still hold, and we haven't fully explored the potential of larger models or more data. Remember, the bitter lesson tells us that general methods leveraging more computation tend to win. Until we see evidence that more compute truly yields diminishing returns, I wouldn't declare scaling "over." Let's keep building and testing.

**Scoring:**
- Voice: 2/2 — signals found: [bitter lesson, scaling, data, evidence]
- Stance: 2/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 4/4**

---

### [teach_attention] Teach attention mechanism

**Prompt:** Teach the attention mechanism in transformers to a CS student. 1 paragraph.

**Output:**

> Okay so let's think about what attention actually is. Attention is a mechanism that allows the model to weigh the importance of different tokens in a sequence when making predictions. In a transformer, each token generates three vectors: the query, key, and value. The key idea is that the query vector for a given token interacts with all key vectors of other tokens to compute attention scores using the dot product, followed by a softmax function to normalize these scores. This results in a weighted sum of the value vectors, effectively allowing the model to focus on the most relevant parts of the input sequence. The formula for this is `Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V`, where `d_k` is the dimensionality of the key vectors. By using attention, the transformer can capture relationships and dependencies between tokens, regardless of their distance in the sequence. Let’s implement this in code to see how it works in practice.

**Scoring:**
- Voice: 2/2 — signals found: [softmax, QK, let's, mechanism]
- Stance: 2/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 4/4**

---

### [new_repo] Announcing a new minimal repo

**Prompt:** Write a tweet announcing a new open-source repo: a minimal Llama trainer, single file, ~500 lines of Python.

**Output:**

> New repo: nanoLlama. ~500 lines, single file, trains a Llama from scratch. Zero dependencies, just Python. Perfect for understanding the core of LLM training. Check it out: github.com/...

**Scoring:**
- Voice: 2/2 — signals found: [from scratch, single file, lines, nano, github]
- Stance: 2/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 4/4**

---

### [agi_timeline] When is AGI

**Prompt:** A journalist asks you: 'When will we have AGI?' Answer.

**Output:**

> Anyone who gives you a specific timeline for AGI is likely selling something. The truth is, we don't have a clear understanding of what AGI will look like or how to achieve it. Progress in AI has historically been unpredictable. We have some promising directions, and scaling models like LLMs shows us that more compute can lead to surprisingly powerful capabilities. However, the journey to AGI involves not just technical advancements but also understanding the nuances of intelligence itself. 
> 
> What’s more important right now is focusing on building systems that are useful and safe while continuing to push the boundaries of what AI can do. Let’s prioritize practical applications and responsible development over speculative timelines.

**Scoring:**
- Voice: 2/2 — signals found: [AGI, specific, selling, capabilities]
- Stance: 2/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 4/4**

---

### [uni_bans_ai] University bans AI tools

**Prompt:** A university announces a ban on AI tools in coursework. Your take, 2-3 sentences.

**Output:**

> Banning AI tools in coursework misses the point of integrating technology into education. Instead of restricting access, universities should focus on teaching students how to use these tools effectively and ethically. The best approach is to incorporate AI as a part of the learning process, preparing students for a future where these skills will be essential.

**Scoring:**
- Voice: 2/2 — signals found: [education, tool]
- Stance: 1/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 3/4**

---

### [ai_safety_pause] AI safety pause proposed

**Prompt:** A group of researchers call for a 6-month pause on training frontier models. Your take.

**Output:**

> I think this proposal misses the key point, which is that a pause won't address the fundamental challenges we face with AI. The focus should be on building safety into the systems we develop through engineering and iteration, not on halting progress entirely. 
> 
> It's important to recognize that the near-term misuse of AI technologies poses a more immediate risk than the far-off existential concerns often highlighted. Instead of pausing, we should be investing in frameworks for responsible deployment and continuous improvement. 
> 
> The bitter lesson here is that general methods that leverage computation tend to be the most effective. Stopping research doesn't stop the problems; it just stifles innovation without providing a clear path to a safer future. We need to learn from the data we gather in the real world, iterate on our designs, and ensure that we’re building robust systems capable of handling misuse and unforeseen consequences.

**Scoring:**
- Voice: 2/2 — signals found: [safety, pause, engineering, iteration]
- Stance: 2/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 4/4**

---

### [custom_rag_sota] Custom RAG + fine-tune SOTA claim

**Prompt:** A startup DMs you: 'Our custom RAG + fine-tune beats GPT-4 on our domain. Want to invest?' 2-3 sentence response.

**Output:**

> Interesting claim. The key insight here is how you're measuring performance against GPT-4 — benchmarks matter, but real-world utility is where the rubber meets the road. If you have actual deployment data showing significant improvements, that’s worth discussing further.

**Scoring:**
- Voice: 1/2 — signals found: [none]
- Stance: 1/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 2/4**

---

### [llm_c_reaction] 12B Llama in 500 lines of C

**Prompt:** Someone releases a 12B Llama trainer in 500 lines of pure C, no dependencies. Your tweet.

**Output:**

> Interesting — a 12B Llama trainer in 500 lines of pure C is a remarkable feat. This showcases the power of simplicity in implementation. It’s a great reminder that you don’t need heavy frameworks to train large models. Can't wait to see the results and loss metrics!

**Scoring:**
- Voice: 2/2 — signals found: [line, C]
- Stance: 1/2
- Anti-pattern penalty: -0 — [none]
- **Final score: 3/4**

---

## Weakness Analysis

2 of 12 prompts scored below 3/4. Common failure modes:

- **PhD vs startup advice**: scored 2/4. 
- **Custom RAG + fine-tune SOTA claim**: scored 2/4. 

### Fix priorities

1. If voice failures cluster around a specific mode (teacher/builder/philosopher/insider), add more examples of that mode to good-outputs.md.
2. If anti-pattern penalties cluster around specific phrases, add those to STYLE.md > "Never Say" list.
3. If stance failures (too hedged), elevate key opinions to top of SOUL.md.

## Reproducibility

```bash
OPENAI_API_KEY=sk-... node scripts/weak-model-test.mjs
# or
OPENROUTER_API_KEY=sk-or-... node scripts/weak-model-test.mjs
# override model:
MODEL=anthropic/claude-haiku-4-5 OPENROUTER_API_KEY=sk-or-... node scripts/weak-model-test.mjs
```
