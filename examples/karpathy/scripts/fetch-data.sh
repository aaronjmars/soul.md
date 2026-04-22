#!/usr/bin/env bash
# =============================================================================
# Karpathy Soul File — Data Pipeline
# =============================================================================
# Reproducible script to fetch Andrej Karpathy's public writing, transcripts,
# and GitHub data. Idempotent — skips already-cached files.
#
# Usage: bash scripts/fetch-data.sh
# Dependencies: curl, yt-dlp (optional, for YouTube transcripts)
# =============================================================================

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data"

mkdir -p "$DATA/writing" "$DATA/transcripts" "$DATA/x" "$DATA/github"

echo "=== Karpathy Data Pipeline ==="
echo "Output: $DATA"
echo ""

# -----------------------------------------------------------------------------
# 1. Blog posts from karpathy.github.io
# -----------------------------------------------------------------------------
echo "--- Fetching blog posts ---"

BLOG_SLUGS="state-of-cv rnn-effectiveness ai-short-peek rl phd medium software-2.0 recipe biohacking-lite forward-pass blockchain lecun1989 microgpt"
BLOG_URLS="https://karpathy.github.io/2012/10/22/state-of-computer-vision/ https://karpathy.github.io/2015/05/21/rnn-effectiveness/ https://karpathy.github.io/2015/11/14/ai/ https://karpathy.github.io/2016/05/31/rl/ https://karpathy.github.io/2016/09/07/phd/ https://karpathy.github.io/2018/01/20/medium/ https://karpathy.github.io/2017/01/25/software-2.0/ https://karpathy.github.io/2019/04/25/recipe/ https://karpathy.github.io/2020/06/11/biohacking-lite/ https://karpathy.github.io/2021/03/27/forward-pass/ https://karpathy.github.io/2021/06/21/blockchain/ https://karpathy.github.io/2022/03/14/lecun1989/ https://karpathy.github.io/2026/02/12/microgpt/"

set -- $BLOG_URLS
for slug in $BLOG_SLUGS; do
  url="$1"; shift
  outfile="$DATA/writing/${slug}.html"
  if [ -f "$outfile" ]; then
    echo "  [cached] $slug"
  else
    echo "  [fetch]  $slug"
    curl -sL "$url" -o "$outfile" || echo "  [WARN] Failed to fetch $slug"
    sleep 0.5
  fi
done

echo ""

# -----------------------------------------------------------------------------
# 2. YouTube transcripts (Zero to Hero series)
# -----------------------------------------------------------------------------
echo "--- Fetching YouTube transcripts ---"

# Karpathy's Neural Networks: Zero to Hero playlist
YOUTUBE_VIDEOS=(
  "VMj-3S1tku0"  # The spelled-out intro to neural networks and backpropagation
  "PaCmpygFfXo"  # Building micrograd
  "TCH_1BHY58I"  # Building makemore Part 1
  "q8SA3rM6ckI"  # Building makemore Part 2: MLP
  "P6sfmUTpUmc"  # Building makemore Part 3: Activations & Gradients, BatchNorm
  "t3YJ5hKiMQ0"  # Building makemore Part 4: Becoming a Backprop Ninja
  "kCc8FmEb1nY"  # Let's build GPT: from scratch, in code, spelled out
  "zduSFxRajkE"  # Let's build the GPT Tokenizer
  "l8pRSuU81PU"  # Let's reproduce GPT-2 (124M)
  "7xTGNNLPyMI"  # Deep Dive into LLMs like ChatGPT (2025)
  # Podcast appearances
  "hM_h0UA7upI"  # No Priors × Karpathy
  "c3b-JASoPi0"  # Karpathy talk (conference)
)

if command -v yt-dlp &>/dev/null; then
  for vid in "${YOUTUBE_VIDEOS[@]}"; do
    outfile="$DATA/transcripts/${vid}.vtt"
    if [ -f "$outfile" ] || [ -f "$DATA/transcripts/${vid}.en.vtt" ]; then
      echo "  [cached] $vid"
    else
      echo "  [fetch]  $vid"
      yt-dlp --write-auto-sub --sub-lang en --skip-download \
        --output "$DATA/transcripts/${vid}" \
        "https://www.youtube.com/watch?v=${vid}" 2>/dev/null || echo "  [WARN] No subs for $vid"
      sleep 1
    fi
  done

  # Convert VTT to plain text
  echo "  Converting VTT to plaintext..."
  for vtt in "$DATA/transcripts"/*.vtt; do
    [ -f "$vtt" ] || continue
    txt="${vtt%.vtt}.txt"
    if [ ! -f "$txt" ]; then
      sed '/^$/d; /^[0-9]/d; /-->/d; /WEBVTT/d; /Kind:/d; /Language:/d' "$vtt" \
        | sed 's/<[^>]*>//g' | awk '!seen[$0]++' > "$txt"
    fi
  done
else
  echo "  [SKIP] yt-dlp not found. Install: pip install yt-dlp"
  echo "  YouTube video IDs saved to $DATA/transcripts/SOURCES.md"
fi

echo ""

# -----------------------------------------------------------------------------
# 3. GitHub READMEs
# -----------------------------------------------------------------------------
echo "--- Fetching GitHub READMEs ---"

REPOS=(
  "karpathy/nanoGPT"
  "karpathy/llm.c"
  "karpathy/micrograd"
  "karpathy/minbpe"
  "karpathy/char-rnn"
  "karpathy/arxiv-sanity-preserver"
  "karpathy/nn-zero-to-hero"
  "karpathy/LLM101n"
)

for repo in "${REPOS[@]}"; do
  slug="${repo//\//_}"
  outfile="$DATA/github/${slug}_README.md"
  if [ -f "$outfile" ]; then
    echo "  [cached] $repo"
  else
    echo "  [fetch]  $repo"
    curl -sL "https://raw.githubusercontent.com/${repo}/master/README.md" -o "$outfile" 2>/dev/null \
      || curl -sL "https://raw.githubusercontent.com/${repo}/main/README.md" -o "$outfile" 2>/dev/null \
      || echo "  [WARN] Failed to fetch README for $repo"
    sleep 0.3
  fi
done

echo ""

# -----------------------------------------------------------------------------
# 4. Twitter/X data
# -----------------------------------------------------------------------------
echo "--- Twitter/X data ---"
if [ ! -f "$DATA/x/curated-tweets.md" ]; then
  echo "  [INFO] Curated tweets file will be created manually."
  echo "  See data/x/README.md for Twitter archive export instructions."
else
  echo "  [cached] curated-tweets.md exists"
fi

cat > "$DATA/x/README.md" << 'XREADME'
# Twitter/X Data — @karpathy

## How to get the full archive

1. Go to https://x.com/settings/download_data
2. Request "Your archive"
3. Wait for email (can take 24-48 hours)
4. Download and unzip
5. Copy `data/tweets.js` to this directory

## What we have without the archive

- `curated-tweets.md` — Hand-curated collection of Karpathy's most notable
  tweets, organized by theme. Sourced from public archives, screenshots,
  and news coverage.

## Notable accounts to cross-reference

- @karpathy (main)
- Replies to @lexfridman, @ylecun, @ilonamusk, @sama
XREADME

echo ""

# -----------------------------------------------------------------------------
# 5. Summary
# -----------------------------------------------------------------------------
echo "=== Pipeline Complete ==="
echo ""
find "$DATA" -type f | wc -l | xargs -I{} echo "Total files: {}"
echo ""
echo "Directory structure:"
find "$DATA" -type f | head -30 | sed "s|$DATA/||"
