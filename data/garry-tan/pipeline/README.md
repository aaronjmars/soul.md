# Data Pipeline — @garrytan

Reproducible scripts for collecting and analyzing Garry Tan's public content.

## Prerequisites

```bash
# Twitter API (free tier)
export TWITTER_BEARER_TOKEN="your_bearer_token"
# OR: put in ~/.env.twitter as TWITTER_BEARER_TOKEN=xxx

# Python packages
pip3 install yt-dlp  # for YouTube

# Optional: for weak model test
pip3 install anthropic  # or openai
```

## Scripts

### 1. Fetch Tweets

```bash
./pipeline/fetch_tweets.sh
```

Fetches all available @garrytan tweets via Twitter API v2 search.  
Output: `data/tweets/all_tweets.json`  
Notes:
- Uses search endpoint (more permissive than timeline on free tier)
- Paginates until API returns no more results
- Deduplicates and sorts by tweet ID
- Free tier: ~500 tweets from recent 7 days

### 2. Fetch YouTube Transcripts

```bash
./pipeline/fetch_youtube.sh [count]
# Default: first 20 videos
./pipeline/fetch_youtube.sh 50  # first 50 videos
```

Downloads auto-generated subtitles from https://www.youtube.com/@garrytan  
Output: `data/youtube/*.vtt` and `data/youtube/*.txt`  
Notes:
- Requires yt-dlp (installed automatically if missing)
- Auto-captions may be missing for some videos (YouTube SABR streaming restriction)
- VTT files converted to plain text automatically

### 3. Analyze Tweets

```bash
python3 pipeline/analyze_tweets.py
# Custom input/output:
python3 pipeline/analyze_tweets.py --input data/tweets/all_tweets.json --output report.md
```

Produces:
- Mode distribution (builder vs political vs motivational etc.)
- Top vocabulary
- Signature phrase frequency
- Most amplified accounts
- Emoji usage

Output: `data/tweets/analysis.md`

### 4. Weak Model Test

```bash
# Using Anthropic Haiku (cheap)
ANTHROPIC_API_KEY=xxx python3 examples/weak_model_test.py --provider anthropic

# Using OpenAI GPT-4o-mini
OPENAI_API_KEY=xxx python3 examples/weak_model_test.py --provider openai

# Just print the evaluation rubric
python3 examples/weak_model_test.py --evaluate
```

Runs 6 test scenarios against the soul file, with automated checks.

## Data Sources

| Source | Method | Coverage |
|--------|--------|----------|
| Twitter/X @garrytan | API v2 search | ~500 recent tweets |
| garrytan.com | (requires JS rendering) | Manual + known quotes |
| YouTube @garrytan | yt-dlp subtitles | 158 videos available |
| Podcast/interviews | Known quotes compiled manually | See data/interviews/ |

## Notes on Twitter API Tier

The free tier of Twitter API v2 gives access to ~7 days of tweets via recent search.  
For deeper historical coverage, the Basic or Pro tier is needed.  
This pipeline uses the search endpoint which tends to return more results than the timeline endpoint on free tier.
