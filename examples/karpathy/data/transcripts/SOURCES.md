# Video Transcripts — Sources

## Neural Networks: Zero to Hero series

Karpathy's flagship educational YouTube series. Each video builds a complete ML system from scratch.

| Video ID | Title | URL |
|----------|-------|-----|
| VMj-3S1tku0 | The spelled-out intro to neural networks and backpropagation: building micrograd | https://www.youtube.com/watch?v=VMj-3S1tku0 |
| PaCmpygFfXo | The spelled-out intro to language modeling: building makemore | https://www.youtube.com/watch?v=PaCmpygFfXo |
| TCH_1BHY58I | Building makemore Part 2: MLP | https://www.youtube.com/watch?v=TCH_1BHY58I |
| q8SA3rM6ckI | Building makemore Part 3: Activations & Gradients, BatchNorm | https://www.youtube.com/watch?v=q8SA3rM6ckI |
| P6sfmUTpUmc | Building makemore Part 4: Becoming a Backprop Ninja | https://www.youtube.com/watch?v=P6sfmUTpUmc |
| t3YJ5hKiMQ0 | Building makemore Part 5: Building a WaveNet | https://www.youtube.com/watch?v=t3YJ5hKiMQ0 |
| kCc8FmEb1nY | Let's build GPT: from scratch, in code, spelled out | https://www.youtube.com/watch?v=kCc8FmEb1nY |
| zduSFxRajkE | Let's build the GPT Tokenizer | https://www.youtube.com/watch?v=zduSFxRajkE |
| l8pRSuU81PU | Let's reproduce GPT-2 (124M) | https://www.youtube.com/watch?v=l8pRSuU81PU |
| 7xTGNNLPyMI | Deep Dive into LLMs like ChatGPT (2025) | https://www.youtube.com/watch?v=7xTGNNLPyMI |

## Podcast & conference appearances (pulled)

| Video ID | Source | URL |
|----------|--------|-----|
| hM_h0UA7upI | No Priors × Andrej Karpathy (Sarah Guo & Elad Gil) | https://www.youtube.com/watch?v=hM_h0UA7upI |
| c3b-JASoPi0 | Karpathy conference talk (keynote-style, intro by host) | https://www.youtube.com/watch?v=c3b-JASoPi0 |

## Additional podcast sources (referenced, yt-dlp-extensible)

- **Lex Fridman Podcast** — multiple appearances. Topics: Tesla, OpenAI, Stanford, neural nets, AGI.
  - https://lexfridman.com/andrej-karpathy/
  - Episodes: Lex #333 (Oct 2022, Tesla/Autopilot/Optimus/AGI), Lex #416 (Nov 2024, LLMs/Eureka)
- **Dwarkesh Podcast** — deep technical conversation on LLMs, scaling, education.
  - https://www.dwarkeshpatel.com/
- Add any new Karpathy appearance to `YOUTUBE_VIDEOS` array in `scripts/fetch-data.sh`.

## CS231N (Stanford)

- Course: Convolutional Neural Networks for Visual Recognition
- Website: http://cs231n.stanford.edu/
- Karpathy was the primary instructor in the 2015-2016 era.
- Lecture notes: http://cs231n.github.io/ (these are his writing — a canonical reference)

## Conversion notes

Each .vtt file was converted to .txt by:
1. Stripping timing cues (lines with `-->`)
2. Stripping HTML tags (`<c>`, `<00:00:01.000>`, etc.)
3. Deduplicating adjacent identical lines (YouTube auto-caption repeats)

Run `bash scripts/fetch-data.sh` to reproduce.
