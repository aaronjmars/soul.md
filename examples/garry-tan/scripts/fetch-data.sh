#!/usr/bin/env bash
# Garry Tan Soul File — Reproducible Data Pipeline
# Fetches public content from blog, YouTube, and X/Twitter
# Usage: bash scripts/fetch-data.sh
# Dependencies: curl, yt-dlp (optional, for YouTube transcripts)

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data"

echo "=== Garry Tan Data Pipeline ==="
echo "Output: $DATA"
echo ""

# ──────────────────────────────────────────────
# 1. BLOG POSTS (blog.garrytan.com / Posthaven)
# ──────────────────────────────────────────────
echo "[1/4] Fetching blog posts..."
mkdir -p "$DATA/writing"

BLOG_URLS=(
  "https://blog.garrytan.com/deprogramming-corporatism"
  "https://blog.garrytan.com/working-for-microsoft-cost-me-200-dollars-million"
  "https://blog.garrytan.com/how-founders-can-build-trust-and-safety-teams"
  "https://blog.garrytan.com/micromanagement-is-toxic"
  "https://blog.garrytan.com/sell-die-no-grow-profitably"
  "https://blog.garrytan.com/roll-your-way-to-a-billion-dollar-startup"
  "https://blog.garrytan.com/what-instacart-taught-us"
  "https://blog.garrytan.com/crusty-engineers-unite"
  "https://blog.garrytan.com/to-soften-our-view-of-others"
  "https://blog.garrytan.com/metaprogram-your-own-mind"
  "https://blog.garrytan.com/six-skills-for-startup-success"
  "https://blog.garrytan.com/changing-the-world-can-make-you-insane"
)

for url in "${BLOG_URLS[@]}"; do
  slug=$(echo "$url" | sed 's|.*/||')
  outfile="$DATA/writing/${slug}.html"
  if [ ! -f "$outfile" ]; then
    echo "  -> $slug"
    curl -sL "$url" -o "$outfile" || echo "  [WARN] Failed: $url"
    sleep 0.5
  else
    echo "  -> $slug (cached)"
  fi
done

echo "  Blog posts: $(ls "$DATA/writing/"*.html 2>/dev/null | wc -l) files"

# ──────────────────────────────────────────────
# 2. YOUTUBE TRANSCRIPTS (via yt-dlp)
# ──────────────────────────────────────────────
echo ""
echo "[2/4] Fetching YouTube transcripts..."
mkdir -p "$DATA/transcripts"

YT_VIDEOS=(
  "https://www.youtube.com/watch?v=yP176MBG9TU"  # One Decision Cost Me $200M
  "https://www.youtube.com/watch?v=mmBKMnQ7kLQ"  # 6 Skills for Startup Success
  "https://www.youtube.com/watch?v=AZP8dJJ2BRQ"  # How to Get Into YC
)

if command -v yt-dlp &>/dev/null; then
  for url in "${YT_VIDEOS[@]}"; do
    vid=$(echo "$url" | sed 's|.*v=||')
    outfile="$DATA/transcripts/${vid}.txt"
    if [ ! -f "$outfile" ]; then
      echo "  -> $vid"
      yt-dlp --write-auto-sub --sub-lang en --skip-download \
        --sub-format vtt -o "$DATA/transcripts/${vid}" "$url" 2>/dev/null || \
        echo "  [WARN] No subtitles for $vid"
      # Convert VTT to plain text if exists
      vtt="$DATA/transcripts/${vid}.en.vtt"
      if [ -f "$vtt" ]; then
        grep -v "^[0-9]" "$vtt" | grep -v "^$" | grep -v "WEBVTT" | grep -v "-->.*" | sort -u > "$outfile"
        rm -f "$vtt"
      fi
    else
      echo "  -> $vid (cached)"
    fi
  done
else
  echo "  [SKIP] yt-dlp not installed. Install with: pip install yt-dlp"
  echo "  YouTube transcripts can also be fetched manually."
fi

echo "  Transcripts: $(ls "$DATA/transcripts/"*.txt 2>/dev/null | wc -l) files"

# ──────────────────────────────────────────────
# 3. X/TWITTER DATA (public profile info)
# ──────────────────────────────────────────────
echo ""
echo "[3/4] X/Twitter data..."
mkdir -p "$DATA/x"

# Note: Full tweet archive requires Twitter/X data export or API access.
# This script documents the process; manual export is required for full data.
cat > "$DATA/x/README.md" << 'XREADME'
# Twitter/X Data for Garry Tan (@garrytan)

## How to Get Full Tweet Archive

1. **Twitter Data Export** (recommended):
   - Go to Settings > Your Account > Download an archive of your data
   - This provides tweets.js with full tweet history
   - Only available to the account owner

2. **Community Notes / Public Archives**:
   - https://web.archive.org/web/*/https://twitter.com/garrytan*
   - Various tweet archiving services

3. **Manual Curation** (used here):
   - Key tweets curated from public sources
   - Organized by theme and date

## Account Stats (as of 2024)
- Handle: @garrytan
- Followers: 400,000+
- Posts: Very active, multiple daily
- Topics: startups, AI, SF politics, motivation, tech industry
XREADME

echo "  X data directory created with README"

# ──────────────────────────────────────────────
# 4. PODCAST/INTERVIEW SOURCES
# ──────────────────────────────────────────────
echo ""
echo "[4/4] Interview source references..."

cat > "$DATA/transcripts/SOURCES.md" << 'SOURCES'
# Interview & Podcast Sources

## Full Episodes (transcripts available)
1. **Acquired Podcast** — "How YC Rewrote the Seed Playbook with Garry Tan"
   - URL: https://www.acquired.fm/episodes/how-yc-rewrote-the-seed-playbook-with-garry-tan
   - Topics: YC history, seed investing, cult of startups

2. **Mixergy** — "Y Combinator Startups Growing 5X Faster"
   - URL: https://mixergy.com/interviews/garry-tan-y-combinator-startups-growing-5x-faster-heres-what-changed/
   - Topics: AI growth, vibe coding, founder advice

3. **The Knowledge Project #226** — "Billion-Dollar Misfits"
   - URL: https://fs.blog/knowledge-project-podcast/garry-tan/
   - Topics: Earnestness, founder selection, YC formula

4. **Vanta Frameworks for Growth** — "Why The Next Unicorns Are Built By AI"
   - URL: https://www.vanta.com/resources/why-the-next-unicorns-are-built-by-ai
   - Topics: AI unicorns, vibe coding, company scaling

5. **The Hustle Q&A** — Interview with Trung Phan
   - URL: https://thehustle.co/garry-tan-q-and-a-trung-phan
   - Topics: YouTube content, VC democratization, personal background

6. **Investor Operator Podcast** — "How YC's Garry Tan Evaluates Startups"
   - URL: https://www.investoroperator.io/how-ycs-garry-tan-evaluates-startups-episode-3-of-the-investor-operator-podcast/
   - Topics: Startup evaluation, pattern matching

## Key Blog Posts
- https://blog.garrytan.com/deprogramming-corporatism
- https://blog.garrytan.com/working-for-microsoft-cost-me-200-dollars-million
- https://blog.garrytan.com/what-instacart-taught-us
- https://blog.garrytan.com/crusty-engineers-unite
- https://blog.garrytan.com/roll-your-way-to-a-billion-dollar-startup
SOURCES

echo "  Sources file created"
echo ""
echo "=== Pipeline complete ==="
echo "Data directory: $DATA"
echo "Files: $(find "$DATA" -type f | wc -l) total"
