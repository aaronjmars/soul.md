# LLM101n: Let's build a Storyteller

---

**!!! NOTE: this course does not yet exist. It is current being developed by [Eureka Labs](https://eurekalabs.ai). Until it is ready I am archiving this repo !!!**

---

![LLM101n header image](llm101n.jpg)

>  What I cannot create, I do not understand. -Richard Feynman

In this course we will build a Storyteller AI Large Language Model (LLM). Hand in hand, you'll be able to create, refine and illustrate little [stories](https://huggingface.co/datasets/roneneldan/TinyStories) with the AI. We are going to build everything end-to-end from basics to a functioning web app similar to ChatGPT, from scratch in Python, C and CUDA, and with minimal computer science prerequisites. By the end you should have a relatively deep understanding of AI, LLMs, and deep learning more generally.

**Syllabus**

- Chapter 01 **Bigram Language Model** (language modeling)
- Chapter 02 **Micrograd** (machine learning, backpropagation)
- Chapter 03 **N-gram model** (multi-layer perceptron, matmul, gelu)
- Chapter 04 **Attention** (attention, softmax, positional encoder)
- Chapter 05 **Transformer** (transformer, residual, layernorm, GPT-2)
- Chapter 06 **Tokenization** (minBPE, byte pair encoding)
- Chapter 07 **Optimization** (initialization, optimization, AdamW)
- Chapter 08 **Need for Speed I: Device** (device, CPU, GPU, ...)
- Chapter 09 **Need for Speed II: Precision** (mixed precision training, fp16, bf16, fp8, ...)
- Chapter 10 **Need for Speed III: Distributed** (distributed optimization, DDP, ZeRO)
- Chapter 11 **Datasets** (datasets, data loading, synthetic data generation)
- Chapter 12 **Inference I: kv-cache** (kv-cache)
- Chapter 13 **Inference II: Quantization** (quantization)
- Chapter 14 **Finetuning I: SFT** (supervised finetuning SFT, PEFT, LoRA, chat)
- Chapter 15 **Finetuning II: RL** (reinforcement learning, RLHF, PPO, DPO)
- Chapter 16 **Deployment** (API, web app)
- Chapter 17 **Multimodal** (VQVAE, diffusion transformer)

**Appendix**

Further topics to work into the progression above:

- Programming languages: Assembly, C, Python
- Data types: Integer, Float, String (ASCII, Unicode, UTF-8)
- Tensor: shapes, views, strides, contiguous, ...
- Deep Learning frameworks: PyTorch, JAX
- Neural Net Architecture: GPT (1,2,3,4), Llama (RoPE, RMSNorm, GQA), MoE, ...
- Multimodal: Images, Audio, Video, VQVAE, VQGAN, diffusion
