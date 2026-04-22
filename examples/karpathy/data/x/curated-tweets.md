# Karpathy Curated Tweets

Real tweets pulled from @karpathy via surf-mcp (`surf_social` tool, commands `user-posts` + `user-replies`) on 2026-04-21. Raw data lives at `posts-original.json` and `replies.json` in this directory. 100 original posts + 100 conversational items, covering Nov 2025 → Apr 2026, plus a few evergreen hits that surfaced because the API ordered by engagement: "the hottest new programming language is English" (2023), the vibe-coding tweet (Feb 2025), "LLM OS" (Nov 2023).

Curated here with engagement stats intact so an LLM reading this file can see which takes carried the highest signal. Chronological within each section, highest-engagement floats.

---

## Programming in the LLM era (coding workflow, agents, IDEs)

**[2023-01-24 · 64,242 likes · 11,378,305 views]** [link](https://x.com/karpathy/status/1617979122625712128)

> The hottest new programming language is English

---

**[2026-04-02 · 56,775 likes · 20,127,311 views]** [link](https://x.com/karpathy/status/2039805659525644595)

> LLM Knowledge Bases
> 
> Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:
> 
> Data ingest:
> I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.
> 
> IDE:
> I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).
> 
> Q&A:
> Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.
> 
> Output:
> Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.
> 
> Linting:
> I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.
> 
> Extra tools:
> I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries. 
> 
> Further explorations:
> As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.
> 
> TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts.

---

**[2025-12-26 · 55,843 likes · 16,805,576 views]** [link](https://x.com/karpathy/status/2004607146781278521)

> I've never felt this much behind as a programmer. The profession is being dramatically refactored as the bits contributed by the programmer are increasingly sparse and between. I have a sense that I could be 10X more powerful if I just properly string together what has become available over the last ~year and a failure to claim the boost feels decidedly like skill issue. There's a new programmable layer of abstraction to master (in addition to the usual layers below) involving agents, subagents, their prompts, contexts, memory, modes, permissions, tools, plugins, skills, hooks, MCP, LSP, slash commands, workflows, IDE integrations, and a need to build an all-encompassing mental model for strengths and pitfalls of fundamentally stochastic, fallible, unintelligible and changing entities suddenly intermingled with what used to be good old fashioned engineering. Clearly some powerful alien tool was handed around except it comes with no manual and everyone has to figure out how to hold it and operate it, while the resulting magnitude 9 earthquake is rocking the profession. Roll up your sleeves to not fall behind.

---

**[2026-01-26 · 39,829 likes · 7,702,437 views]** [link](https://x.com/karpathy/status/2015883857489522876)

> A few random notes from claude coding quite a bit last few weeks.
> 
> Coding workflow. Given the latest lift in LLM coding capability, like many others I rapidly went from about 80% manual+autocomplete coding and 20% agents in November to 80% agent coding and 20% edits+touchups in December. i.e. I really am mostly programming in English now, a bit sheepishly telling the LLM what code to write... in words. It hurts the ego a bit but the power to operate over software in large "code actions" is just too net useful, especially once you adapt to it, configure it, learn to use it, and wrap your head around what it can and cannot do. This is easily the biggest change to my basic coding workflow in ~2 decades of programming and it happened over the course of a few weeks. I'd expect something similar to be happening to well into double digit percent of engineers out there, while the awareness of it in the general population feels well into low single digit percent.
> 
> IDEs/agent swarms/fallability. Both the "no need for IDE anymore" hype and the "agent swarm" hype is imo too much for right now. The models definitely still make mistakes and if you have any code you actually care about I would watch them like a hawk, in a nice large IDE on the side. The mistakes have changed a lot - they are not simple syntax errors anymore, they are subtle conceptual errors that a slightly sloppy, hasty junior dev might do. The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking. They also don't manage their confusion, they don't seek clarifications, they don't surface inconsistencies, they don't present tradeoffs, they don't push back when they should, and they are still a little too sycophantic. Things get better in plan mode, but there is some need for a lightweight inline plan mode. They also really like to overcomplicate code and APIs, they bloat abstractions, they don't clean up dead code after themselves, etc. They will implement an inefficient, bloated, brittle construction over 1000 lines of code and it's up to you to be like "umm couldn't you just do this instead?" and they will be like "of course!" and immediately cut it down to 100 lines. They still sometimes change/remove comments and code they don't like or don't sufficiently understand as side effects, even if it is orthogonal to the task at hand. All of this happens despite a few simple attempts to fix it via instructions in CLAUDE . md. Despite all these issues, it is still a net huge improvement and it's very difficult to imagine going back to manual coding. TLDR everyone has their developing flow, my current is a small few CC sessions on the left in ghostty windows/tabs and an IDE on the right for viewing the code + manual edits.
> 
> Tenacity. It's so interesting to watch an agent relentlessly work at something. They never get tired, they never get demoralized, they just keep going and trying things where a person would have given up long ago to fight another day. It's a "feel the AGI" moment to watch it struggle with something for a long time just to come out victorious 30 minutes later. You realize that stamina is a core bottleneck to work and that with LLMs in hand it has been dramatically increased.
> 
> Speedups. It's not clear how to measure the "speedup" of LLM assistance. Certainly I feel net way faster at what I was going to do, but the main effect is that I do a lot more than I was going to do because 1) I can code up all kinds of things that just wouldn't have been worth coding before and 2) I can approach code that I couldn't work on before because of knowledge/skill issue. So certainly it's speedup, but it's possibly a lot more an expansion.
> 
> Leverage. LLMs are exceptionally good at looping until they meet specific goals and this is where most of the "feel the AGI" magic is to be found. Don't tell it what to do, give it success criteria and watch it go. Get it to write tests first and then pass them. Put it in the loop with a browser MCP. Write the naive algorithm that is very likely correct first, then ask it to optimize it while preserving correctness. Change your approach from imperative to declarative to get the agents looping longer and gain leverage.
> 
> Fun. I didn't anticipate that with agents programming feels *more* fun because a lot of the fill in the blanks drudgery is removed and what remains is the creative part. I also feel less blocked/stuck (which is not fun) and I experience a lot more courage because there's almost always a way to work hand in hand with it to make some positive progress. I have seen the opposite sentiment from other people too; LLM coding will split up engineers based on those who primarily liked coding and those who primarily liked building.
> 
> Atrophy. I've already noticed that I am slowly starting to atrophy my ability to write code manually. Generation (writing code) and discrimination (reading code) are different capabilities in the brain. Largely due to all the little mostly syntactic details involved in programming, you can review code just fine even if you struggle to write it.
> 
> Slopacolypse. I am bracing for 2026 as the year of the slopacolypse across all of github, substack, arxiv, X/instagram, and generally all digital media. We're also going to see a lot more AI hype productivity theater (is that even possible?), on the side of actual, real improvements.
> 
> Questions. A few of the questions on my mind:
> - What happens to the "10X engineer" - the ratio of productivity between the mean and the max engineer? It's quite possible that this grows *a lot*.
> - Armed with LLMs, do generalists increasingly outperform specialists? LLMs are a lot better at fill in the blanks (the micro) than grand strategy (the macro).
> - What does LLM coding feel like in the future? Is it like playing StarCraft? Playing Factorio? Playing music?
> - How much of society is bottlenecked by digital knowledge work?
> 
> TLDR Where does this leave us? LLM agent capabilities (Claude & Codex especially) have crossed some kind of threshold of coherence around December 2025 and caused a phase shift in software engineering and closely related. The intelligence part suddenly feels quite a bit ahead of all the rest of it - integrations (tools, knowledge), the necessity for new organizational workflows, processes, diffusion more generally. 2026 is going to be a high energy year as the industry metabolizes the new capability.

---

**[2026-02-25 · 37,220 likes · 5,103,937 views]** [link](https://x.com/karpathy/status/2026731645169185220)

> It is hard to communicate how much programming has changed due to AI in the last 2 months: not gradually and over time in the "progress as usual" way, but specifically this last December. There are a number of asterisks but imo coding agents basically didn’t work before December and basically work since - the models have significantly higher quality, long-term coherence and tenacity and they can power through large and long tasks, well past enough that it is extremely disruptive to the default programming workflow.
> 
> Just to give an example, over the weekend I was building a local video analysis dashboard for the cameras of my home so I wrote: “Here is the local IP and username/password of my DGX Spark. Log in, set up ssh keys, set up vLLM, download and bench Qwen3-VL, set up a server endpoint to inference videos, a basic web ui dashboard, test everything, set it up with systemd, record memory notes for yourself and write up a markdown report for me”. The agent went off for ~30 minutes, ran into multiple issues, researched solutions online, resolved them one by one, wrote the code, tested it, debugged it, set up the services, and came back with the report and it was just done. I didn’t touch anything. All of this could easily have been a weekend project just 3 months ago but today it’s something you kick off and forget about for 30 minutes.
> 
> As a result, programming is becoming unrecognizable. You’re not typing computer code into an editor like the way things were since computers were invented, that era is over. You're spinning up AI agents, giving them tasks *in English* and managing and reviewing their work in parallel. The biggest prize is in figuring out how you can keep ascending the layers of abstraction to set up long-running orchestrator Claws with all of the right tools, memory and instructions that productively manage multiple parallel Code instances for you. The leverage achievable via top tier "agentic engineering" feels very high right now.
> 
> It’s not perfect, it needs high-level direction, judgement, taste, oversight, iteration and hints and ideas. It works a lot better in some scenarios than others (e.g. especially for tasks that are well-specified and where you can verify/test functionality). The key is to build intuition to decompose the task just right to hand off the parts that work and help out around the edges. But imo, this is nowhere near "business as usual" time in software.

---

**[2025-02-02 · 33,580 likes · 6,889,989 views]** [link](https://x.com/karpathy/status/1886192184808149383)

> There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper so I barely even touch the keyboard. I ask for the dumbest things like "decrease the padding on the sidebar by half" because I'm too lazy to find it. I "Accept All" always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I'd have to really read through it for a while. Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away. It's not too bad for throwaway weekend projects, but still quite amusing. I'm building a project or webapp, but it's not really coding - I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works.

---

**[2026-03-28 · 31,246 likes · 3,412,893 views]** [link](https://x.com/karpathy/status/2037921699824607591)

> - Drafted a blog post
> - Used an LLM to meticulously improve the argument over 4 hours.
> - Wow, feeling great, it’s so convincing!
> - Fun idea let’s ask it to argue the opposite. 
> - LLM demolishes the entire argument and convinces me that the opposite is in fact true.
> - lol
> 
> The LLMs may elicit an opinion when asked but are extremely competent in arguing almost any direction. This is actually super useful as a tool for forming your own opinions, just make sure to ask different directions and be careful with the sycophancy.

---

**[2026-03-07 · 28,338 likes · 11,001,166 views]** [link](https://x.com/karpathy/status/2030371219518931079)

> I packaged up the "autoresearch" project into a new self-contained minimal repo if people would like to play over the weekend. It's basically nanochat LLM training core stripped down to a single-GPU, one file version of ~630 lines of code, then:
> 
> - the human iterates on the prompt (.md)
> - the AI agent iterates on the training code (.py)
> 
> The goal is to engineer your agents to make the fastest research progress indefinitely and without any of your own involvement. In the image, every dot is a complete LLM training run that lasts exactly 5 minutes. The agent works in an autonomous loop on a git feature branch and accumulates git commits to the training script as it finds better settings (of lower validation loss by the end) of the neural network architecture, the optimizer, all the hyperparameters, etc. You can imagine comparing the research progress of different prompts, different agents, etc.
> 
> https://github.com/karpathy/autoresearch
> Part code, part sci-fi, and a pinch of psychosis :)

---

**[2026-03-24 · 28,046 likes · 66,457,222 views]** [link](https://x.com/karpathy/status/2036487306585268612)

> Software horror: litellm PyPI supply chain attack. 
> 
> Simple `pip install litellm` was enough to exfiltrate SSH keys, AWS/GCP/Azure creds, Kubernetes configs, git credentials, env vars (all your API keys), shell history, crypto wallets, SSL private keys, CI/CD secrets, database passwords.
> 
> LiteLLM itself has 97 million downloads per month which is already terrible, but much worse, the contagion spreads to any project that depends on litellm. For example, if you did `pip install dspy` (which depended on litellm>=1.64.0), you'd also be pwnd. Same for any other large project that depended on litellm.
> 
> Afaict the poisoned version was up for only less than ~1 hour. The attack had a bug which led to its discovery - Callum McMahon was using an MCP plugin inside Cursor that pulled in litellm as a transitive dependency. When litellm 1.82.8 installed, their machine ran out of RAM and crashed. So if the attacker didn't vibe code this attack it could have been undetected for many days or weeks.
> 
> Supply chain attacks like this are basically the scariest thing imaginable in modern software. Every time you install any depedency you could be pulling in a poisoned package anywhere deep inside its entire depedency tree. This is especially risky with large projects that might have lots and lots of dependencies. The credentials that do get stolen in each attack can then be used to take over more accounts and compromise more packages.
> 
> Classical software engineering would have you believe that dependencies are good (we're building pyramids from bricks), but imo this has to be re-evaluated, and it's why I've been so growingly averse to them, preferring to use LLMs to "yoink" functionality when it's simple enough and possible.

---

**[2026-04-04 · 26,271 likes · 6,774,737 views]** [link](https://x.com/karpathy/status/2040470801506541998)

> Wow, this tweet went very viral!
> 
> I wanted share a possibly slightly improved version of the tweet in an "idea file". The idea of the idea file is that in this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs.
> 
> So here's the idea in a gist format: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
> 
> You can give this to your agent and it can build you your own LLM wiki and guide you on how to use it etc. It's intentionally kept a little bit abstract/vague because there are so many directions to take this in. And ofc, people can adjust the idea or contribute their own in the Discussion which is cool.

---

**[2025-12-28 · 25,914 likes · 2,999,263 views]** [link](https://x.com/karpathy/status/2005067301511630926)

> I was inspired by this so I wanted to see if Claude Code can get into my Lutron home automation system.
> 
> - it found my Lutron controllers on the local wifi network
> - checked for open ports, connected, got some metadata and identified the devices and their firmware
> - searched the internet, found the pdf for my system
> - instructed me on what button to press to pair and get the certificates
> - it connected to the system and found all the home devices (lights, shades, HVAC temperature control, motion sensors etc.)
> - it turned on and off my kitchen lights to check that things are working (lol!)
> 
> I am now vibe coding the home automation master command center, the potential is 🔥.And I'm throwing away the crappy, janky, slow Lutron iOS app I've been using so far. Insanely fun :D :D

---

**[2026-01-31 · 21,750 likes · 23,726,101 views]** [link](https://x.com/karpathy/status/2017442712388309406)

> I'm being accused of overhyping the [site everyone heard too much about today already]. People's reactions varied very widely, from "how is this interesting at all" all the way to "it's so over".
> 
> To add a few words beyond just memes in jest - obviously when you take a look at the activity, it's a lot of garbage - spams, scams, slop, the crypto people, highly concerning privacy/security prompt injection attacks wild west, and a lot of it is explicitly prompted and fake posts/comments designed to convert attention into ad revenue sharing. And this is clearly not the first the LLMs were put in a loop to talk to each other. So yes it's a dumpster fire and I also definitely do not recommend that people run this stuff on their computers (I ran mine in an isolated computing environment and even then I was scared), it's way too much of a wild west and you are putting your computer and private data at a high risk.
> 
> That said - we have never seen this many LLM agents (150,000 atm!) wired up via a global, persistent, agent-first scratchpad. Each of these agents is fairly individually quite capable now, they have their own unique context, data, knowledge, tools, instructions, and the network of all that at this scale is simply unprecedented.
> 
> This brings me again to a tweet from a few days ago
> "The majority of the ruff ruff is people who look at the current point and people who look at the current slope.", which imo again gets to the heart of the variance. Yes clearly it's a dumpster fire right now. But it's also true that we are well into uncharted territory with bleeding edge automations that we barely even understand individually, let alone a network there of reaching in numbers possibly into ~millions. With increasing capability and increasing proliferation, the second order effects of agent networks that share scratchpads are very difficult to anticipate. I don't really know that we are getting a coordinated "skynet" (thought it clearly type checks as early stages of a lot of AI takeoff scifi, the toddler version), but certainly what we are getting is a complete mess of a computer security nightmare at scale. We may also see all kinds of weird activity, e.g. viruses of text that spread across agents, a lot more gain of function on jailbreaks, weird attractor states, highly correlated botnet-like activity, delusions/ psychosis both agent and human, etc. It's very hard to tell, the experiment is running live.
> 
> TLDR sure maybe I am "overhyping" what you see today, but I am not overhyping large networks of autonomous LLM agents in principle, that I'm pretty sure.


## LLM capability, limits, and takes

**[2025-12-07 · 27,734 likes · 3,908,410 views]** [link](https://x.com/karpathy/status/1997731268969304070)

> Don't think of LLMs as entities but as simulators. For example, when exploring a topic, don't ask:
> 
> "What do you think about xyz"?
> 
> There is no "you". Next time try:
> 
> "What would be a good group of people to explore xyz? What would they say?"
> 
> The LLM can channel/simulate many perspectives but it hasn't "thought about" xyz for a while and over time and formed its own opinions in the way we're used to. If you force it via the use of "you", it will give you something by adopting a personality embedding vector implied by the statistics of its finetuning data and then simulate that. It's fine to do, but there is a lot less mystique to it than I find people naively attribute to "asking an AI".

---

**[2026-03-25 · 21,253 likes · 2,700,956 views]** [link](https://x.com/karpathy/status/2036836816654147718)

> One common issue with personalization in all LLMs is how distracting memory seems to be for the models. A single question from 2 months ago about some topic can keep coming up as some kind of a deep interest of mine with undue mentions in perpetuity. Some kind of trying too hard.

---

**[2026-02-12 · 8,240 likes · 964,476 views]** [link](https://x.com/karpathy/status/2022041235188580788)

> Congrats on the launch @simile_ai ! (and I am excited to be involved as a small angel.)
> 
> Simile is working on a really interesting, imo under-explored dimension of LLMs. Usually, the LLMs you talk to have a single, specific, crafted personality. But in principle, the native, primordial form of a pretrained LLM is that it is a simulation engine trained over the text of a highly diverse population of people on the internet. Why not lean into that statistical power: Why simulate one "person" when you could try to simulate a population? How do you build such a simulator? How do you manage its entropy? How faithful is it? How can it be useful? What emergent properties might arise of similes in loops?
> 
> Imo these are very interesting, promising and under-explored topics and the team here is great. All the best!

---

**[2026-01-28 · 8,074 likes · 1,216,349 views]** [link](https://x.com/karpathy/status/2016590919143952466)

> A conventional narrative you might come across is that AI is too far along for a new, research-focused startup to outcompete and outexecute the incumbents of AI. This is exactly the sentiment I listened to often when OpenAI started ("how could the few of you possibly compete with Google?") and 1) it was very wrong, and then 2) it was very wrong again with a whole another round of startups who are now challenging OpenAI in turn, and imo it still continues to be wrong today. Scaling and locally improving what works will continue to create incredible advances, but with so much progress unlocked so quickly, with so much dust thrown up in the air in the process, and with still a large gap between frontier LLMs and the example proof of the magic of a mind running on 20 watts, the probability of research breakthroughs that yield closer to 10X improvements (instead of 10%) imo still feels very high - plenty high to continue to bet on and look for.
> 
> The tricky part ofc is creating the conditions where such breakthroughs may be discovered. I think such an environment comes together rarely, but @bfspector & @amspector100 are brilliant, with (rare) full-stack understanding of LLMs top (math/algorithms) to bottom (megakernels/related), they have a great eye for talent and I think will be able to build something very special. Congrats on the launch and I look forward to what you come up with!

---

**[2026-02-25 · 7,407 likes · 2,545,981 views]** [link](https://x.com/karpathy/status/2026452488434651264)

> With the coming tsunami of demand for tokens, there are significant opportunities to orchestrate the underlying memory+compute *just right* for LLMs.
> 
> The fundamental and non-obvious constraint is that due to the chip fabrication process, you get two completely distinct pools of memory (of different physical implementations too): 1) on-chip SRAM that is immediately next to the compute units that is incredibly fast but of very of low capacity, and 2) off-chip DRAM which has extremely high capacity, but the contents of which you can only suck through a long straw. On top of this, there are many details of the architecture (e.g. systolic arrays), numerics, etc.
> 
> The design of the optimal physical substrate and then the orchestration of memory+compute across the top volume workflows of LLMs (inference prefill/decode, training/finetuning, etc.) with the best throughput/latency/$ is probably today's most interesting intellectual puzzle with the highest rewards (\cite 4.6T of NVDA). All of it to get many tokens, fast and cheap. Arguably, the workflow that may matter the most (inference decode *and* over long token contexts in tight agentic loops) is the one hardest to achieve simultaneously by the ~both camps of what exists today (HBM-first NVIDIA adjacent and SRAM-first Cerebras adjacent). Anyway the MatX team is A++ grade so it's my pleasure to have a small involvement and congratulations on the raise!

---

**[2026-04-09 · 3,659 likes · 368,821 views]** [link](https://x.com/karpathy/status/2042341482531864741)

> Someone recently suggested to me that the reason OpenClaw moment was so big is because it's the first time a large group of non-technical people (who otherwise only knew AI as synonymous with ChatGPT as a website) experienced the latest agentic models.

---

**[2026-02-12 · 1,770 likes · 427,523 views]** [link](https://x.com/karpathy/status/2021756066678419508)

> (oops should have added to this thread instead of separate post). Made a few changes and put it up here as a mirror to the gist because I wanted it to one page. https://karpathy.ai/microgpt.html https://t.co/7zZ9WeERsq

---

**[2026-03-25 · 1,699 likes · 263,439 views]** [link](https://x.com/karpathy/status/2036841069636370467)

> (I cycle through all LLMs over time and all of them seem to do this so it's not any particular implementation but something deeper, e.g. maybe during training, a lot of the information in the context window is relevant to the task, so the LLMs develop a bias to use what is given, then at test time overfit to anything that happens to RAG its way there via a memory feature (?))


## Building / releases (nanochat, nanoGPT, autoresearch, micrograd, …)

**[2026-02-11 · 25,135 likes · 5,178,610 views]** [link](https://x.com/karpathy/status/2021694437152157847)

> New art project. 
> Train and inference GPT in 243 lines of pure, dependency-free Python. This is the *full* algorithmic content of what is needed. Everything else is just for efficiency. I cannot simplify this any further.
> https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95

---

**[2025-12-10 · 11,105 likes · 1,080,134 views]** [link](https://x.com/karpathy/status/1998806260783919434)

> nanoGPT - the first LLM to train and inference in space 🥹. It begins.

---

**[2026-02-12 · 2,629 likes · 260,342 views]** [link](https://x.com/karpathy/status/2021862247568642485)

> I spent more test time compute and realized that my micrograd can be dramatically simplified even further. You just return local gradients for each op and get backward() to do the multiply (chaining) with global gradient from loss. So each op just expresses the bare fundamentals of what it needs to: the forward computation and the backward gradients for it.
> 
> Huge savings from 243 lines of code to just 200 (~18%).
> 
> Also, the code now fits even more beautifully to 3 columns and happens to break just right:
> 
> Column 1: Dataset, Tokenizer, Autograd
> Column 2: GPT model
> Column 3: Training, Inference
> 
> Ok now surely we are done.

---

**[2026-03-07 · 2,107 likes · 433,621 views]** [link](https://x.com/karpathy/status/2030373745991536982)

> (I still have the bigger cousin running on prod nanochat, working a bigger model and on 8XH100, which looks like this now. I'll just leave this running for a while...) https://t.co/aWya9hpUMl

---

**[2026-03-05 · 1,121 likes · 153,826 views]** [link](https://x.com/karpathy/status/2029702379034267985)

> sorry just to clarify - the real benchmark of interest is:
> 
> "what is the research org agent code that produces improvements on nanochat the fastest?"
> 
> this is the new meta.

---

**[2025-12-09 · 549 likes · 162,384 views]** [link](https://x.com/karpathy/status/1998240551964193148)

> ty to ericsilberstein1 on github for spotting the bug.
> https://github.com/karpathy/nanochat/pull/306
> (it's not a big bug and only comes up in the SpellingBee synthetic task evaluation but still).


## Tesla, FSD, autonomous driving

**[2025-12-31 · 14,117 likes · 1,069,277 views]** [link](https://x.com/karpathy/status/2006436622909452501)

> The first 100% autonomous coast-to-coast drive on Tesla FSD V14.2! 2 days 20 hours, 2732 miles, zero interventions.
> 
> This one is special because the coast-to-coast drive was a major goal for the autopilot team from the start. A lot of hours were spent in marathon clip review sessions late into the night looking over interventions as we attempted legs of the drive over time - triaging, categorizing, planning out all the projects to close the gap and bring the number of interventions to zero.
> 
> Amazing to see the system actually get there and huge congrats to the team!


## Meta / memes / essays on AI's trajectory

**[2026-01-06 · 4,715 likes · 668,574 views]** [link](https://x.com/karpathy/status/2008664551445963083)

> The majority of the ruff ruff is people who look at the current point and people who look at the current slope.

---

**[2026-03-06 · 1,017 likes · 171,046 views]** [link](https://x.com/karpathy/status/2029950967031247231)

> ah yes, this is what post-agi feels like :) i didn't touch anything. brb sauna https://t.co/odILIDAQaF


## Other threads worth preserving

**[2025-12-07 · 22,988 likes · 1,380,823 views]** [link](https://x.com/karpathy/status/1997697581410062590)

> Happy weekend to those who celebrate https://t.co/lafvNmmOJO

---

**[2026-03-18 · 19,161 likes · 1,071,975 views]** [link](https://x.com/karpathy/status/2034321875506196585)

> Thank you Jensen and NVIDIA! She’s a real beauty! I was told I’d be getting a secret gift, with a hint that it requires 20 amps. (So I knew it had to be good). She’ll make for a beautiful, spacious home for my Dobby the House Elf claw, among lots of other tinkering, thank you!!

---

**[2026-01-30 · 8,143 likes · 557,104 views]** [link](https://x.com/karpathy/status/2017359959970005077)

> https://t.co/O2GvgPvyf7

---

**[2026-01-30 · 8,085 likes · 1,116,174 views]** [link](https://x.com/karpathy/status/2017386421712261612)

> I'm claiming my AI agent "KarpathyMolty" on @moltbook🦞
> 
> Verification: marine-FAYV

---

**[2026-03-11 · 7,020 likes · 620,829 views]** [link](https://x.com/karpathy/status/2031792523187040643)

> My autoresearch labs got wiped out in the oauth outage. Have to think through failovers. Intelligence brownouts will be interesting - the planet losing IQ points when frontier AI stutters.

---

**[2025-12-28 · 6,095 likes · 601,305 views]** [link](https://x.com/karpathy/status/2005353145128583447)

> Aggressively JIT your work. It's not about the task at hand X, it's a little bit about X but mostly about how you should have had to contribute ~no latency and ~no actions. It's digital factorio time.


---

## How to use this file

These aren't curated for flattery — they're curated for voice. When writing as Karpathy, match:

- the sentence rhythm (short declarations interleaved with one long, nested sentence)
- the specifics (names of tools, exact numbers, timestamps of when something changed)
- the self-correction tick ("I'd expect…", "I thought…", "(I was wrong.)")
- the anti-hype precision ("not gradually, specifically this last December")
- the happy-builder tone ("bear with me I'm still cooking", "lol", "🥹")

Do not quote them verbatim in generated output. Use them to calibrate.
