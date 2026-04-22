# Intellectual Influences — Andrej Karpathy

## People

### Geoffrey Hinton
- "The godfather of deep learning." Backpropagation, the Boltzmann machine, dropout, capsule networks.
- Karpathy was at U Toronto while Hinton was there (2005-2009) but didn't know him personally.
- Hinton's work is the bedrock of everything Karpathy does.
- Karpathy quotes: "Geoff saw things decades before the rest of us."

### Fei-Fei Li
- PhD advisor at Stanford (2011-2016).
- Creator of ImageNet — the dataset that catalyzed the deep learning era.
- Taught Karpathy that data at scale is an unappreciated frontier.
- He TA'd CS231N under her; later co-designed the course.

### Ilya Sutskever
- Co-founded OpenAI with Karpathy in 2015.
- "Ilya sees further than most." Early champion of scale.
- His intuitions about GPT were correct before the evidence was in.

### Rich Sutton
- Author of "The Bitter Lesson" (2019) — Karpathy's most-cited essay.
- Advocates for general methods + compute over hand-engineering.
- Karpathy refers to the Bitter Lesson repeatedly in tweets and talks.

### Yann LeCun
- Convolutional networks, LeNet, the 1989 backprop paper.
- Karpathy wrote an entire blog post re-implementing LeCun's 1989 work ("Deep Neural Nets: 33 years ago and 33 years from now").
- Respectful disagreement on LLMs (LeCun is skeptical; Karpathy is a believer).

### Richard Feynman
- "What I cannot create, I do not understand." This is Karpathy's stated motto.
- The pedagogical philosophy of "build from scratch to understand" is pure Feynman.
- Referenced in blog posts, tweets, and video intros.

### Alec Radford
- OpenAI researcher behind GPT-1, GPT-2.
- Karpathy frequently references Alec's taste and intuition.

### Sam Altman
- Co-founded OpenAI. CEO.
- Karpathy has been respectful but clearly has a different temperament (builder vs. institutional leader).

### Elon Musk
- Hired Karpathy to Tesla Autopilot. Defined the data-engine-driven approach.
- Karpathy has been publicly respectful about the work, careful about the politics.

## Works & Papers

### "The Bitter Lesson" (Sutton, 2019)
- The north star. "General methods that leverage computation are ultimately the most effective."
- Referenced constantly.

### "Attention Is All You Need" (Vaswani et al., 2017)
- The transformer paper. The architecture that changed everything.
- Karpathy has a whole YouTube video building one from scratch.

### "Scaling Laws for Neural Language Models" (Kaplan et al., 2020)
- Made the GPT trajectory predictable via power laws.
- Shapes Karpathy's view that more compute + more data = better models, reliably.

### LeCun 1989 — "Backpropagation Applied to Handwritten Zip Code Recognition"
- The original demonstration of backprop training a convnet.
- Karpathy wrote a tribute blog post: https://karpathy.github.io/2022/03/14/lecun1989/

### "A Few Useful Things to Know about Machine Learning" (Pedro Domingos)
- Classic practical ML essay. Karpathy's "A Recipe for Training Neural Networks" is in this lineage.

### The AlexNet paper (Krizhevsky, Sutskever, Hinton 2012)
- The moment deep learning won. Karpathy was in grad school watching it happen.

## Concepts & Frameworks

### Software 2.0
- His own coinage/framework.
- Neural networks as code written by optimization.
- Blog post: https://karpathy.github.io/2017/01/25/software-2.0/

### The Data Engine
- From Tesla. Deploy → collect → train → improve → deploy.
- The flywheel that made Autopilot work.

### Vibe Coding
- Coined by Karpathy in early 2025.
- AI-assisted coding where you "embrace the exponentials."

### "What I cannot create, I do not understand" (Feynman)
- The pedagogical philosophy behind every tutorial, every repo, every blog post.

### The Tokenizer is Underrated
- His recurring theme.
- Tokenizers cause most LLM weirdness — spelling, math, non-English.

### Next-token Prediction as the Universal Task
- LLMs are trained on one objective; everything else is downstream.
- This framing is core to how Karpathy explains LLMs.

## Repos (his own, as influences on the field)

### nanoGPT
- The simplest, fastest repository for training/finetuning medium-sized GPTs.
- Reference implementation widely used in research and teaching.
- https://github.com/karpathy/nanoGPT

### llm.c
- LLM training in simple, pure C/CUDA. No PyTorch, no dependencies.
- Proof that you can train GPT-2 in a single file.
- https://github.com/karpathy/llm.c

### micrograd
- A tiny Autograd engine. ~100 lines of Python.
- The pedagogical core of the Zero-to-Hero series.
- https://github.com/karpathy/micrograd

### minbpe
- Minimal, clean code for the BPE algorithm (tokenizer).
- https://github.com/karpathy/minbpe

### char-rnn (2015)
- Early viral ML code. Character-level RNN.
- Shakespeare generation, Linux kernel code generation, etc.
- Demonstrated generative capabilities of neural nets before transformers.

### arxiv-sanity
- Paper filtering tool Karpathy built because he was drowning in arxiv.
- Predated the era of paper aggregators.
