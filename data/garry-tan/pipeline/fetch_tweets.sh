#!/bin/bash
# fetch_tweets.sh — Fetch @garrytan tweets via Twitter API v2
#
# Usage:
#   TWITTER_BEARER_TOKEN=xxx ./fetch_tweets.sh
#   OR: source ~/.env.twitter && ./fetch_tweets.sh
#
# Output: garry-tan/data/tweets/all_tweets.json
# Dependencies: curl, python3

set -euo pipefail

BEARER="${TWITTER_BEARER_TOKEN:-}"
if [ -z "$BEARER" ]; then
    # Try loading from default env file
    if [ -f "$HOME/.env.twitter" ]; then
        export $(grep -v '^#' "$HOME/.env.twitter" | xargs)
        BEARER="$TWITTER_BEARER_TOKEN"
    else
        echo "ERROR: TWITTER_BEARER_TOKEN not set and ~/.env.twitter not found"
        exit 1
    fi
fi

USERNAME="garrytan"
OUTPUT_DIR="$(dirname "$0")/../data/tweets"
mkdir -p "$OUTPUT_DIR"

echo "Fetching user ID for @${USERNAME}..."
USER_RESPONSE=$(curl -s "https://api.x.com/2/users/by/username/${USERNAME}" \
    -H "Authorization: Bearer ${BEARER}")
USER_ID=$(echo "$USER_RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['id'])")
echo "User ID: $USER_ID"

# Fetch tweets via search (more permissive on free tier than timeline)
echo "Fetching tweets..."
PAGE=1
NEXT_TOKEN=""
ALL_TWEETS="[]"

while true; do
    echo "  Fetching page $PAGE..."

    URL="https://api.x.com/2/tweets/search/recent?query=from%3A${USERNAME}&max_results=100&tweet.fields=created_at,text,public_metrics"
    if [ -n "$NEXT_TOKEN" ]; then
        URL="${URL}&next_token=${NEXT_TOKEN}"
    fi

    RESPONSE=$(curl -s "$URL" -H "Authorization: Bearer ${BEARER}")

    # Check for errors
    if echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if 'data' in d else 1)" 2>/dev/null; then
        COUNT=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('data',[])))")
        echo "    Got $COUNT tweets"

        # Accumulate tweets
        ALL_TWEETS=$(echo "$ALL_TWEETS" "$RESPONSE" | python3 -c "
import sys, json
parts = sys.stdin.read().strip().split('\n', 1)
existing = json.loads(parts[0])
new_resp = json.loads(parts[1])
existing.extend(new_resp.get('data', []))
print(json.dumps(existing))
")

        # Get next token
        NEXT_TOKEN=$(echo "$RESPONSE" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print(d.get('meta', {}).get('next_token', ''))
" 2>/dev/null || echo "")

        if [ -z "$NEXT_TOKEN" ]; then
            echo "  No more pages."
            break
        fi
        PAGE=$((PAGE + 1))

        # Rate limit: 1 req/sec on free tier
        sleep 1
    else
        echo "  Error or no more data. Stopping."
        break
    fi
done

# Deduplicate and sort
echo "$ALL_TWEETS" | python3 -c "
import sys, json
tweets = json.load(sys.stdin)
seen = set()
unique = []
for t in tweets:
    if t['id'] not in seen:
        seen.add(t['id'])
        unique.append(t)
unique.sort(key=lambda x: x['id'])
print(json.dumps(unique, indent=2))
" > "$OUTPUT_DIR/all_tweets.json"

TOTAL=$(python3 -c "import json; print(len(json.load(open('$OUTPUT_DIR/all_tweets.json'))))")
echo ""
echo "Done. Total unique tweets: $TOTAL"
echo "Saved to: $OUTPUT_DIR/all_tweets.json"
