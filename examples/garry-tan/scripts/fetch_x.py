#!/usr/bin/env python3
"""
Fetch Garry Tan's tweets and dump each as a markdown file under data/x/.

Two modes, in order of preference:

1. Twitter archive (ground-truth, no rate limits).
   Set TWEET_ARCHIVE_JS to the path of your downloaded tweets.js from
   https://x.com/settings/download_your_data — requires Garry to have shared
   one, or substitute any public archive host (e.g. archive.org mirrors).

2. X API v2 via user-supplied bearer token (rate-limited, recent tweets only).
   Set X_BEARER_TOKEN.

Output: one file per tweet/thread at data/x/YYYY-MM-DD_<id>.md with frontmatter:
    ---
    id: 123...
    date: 2024-01-15T09:22:03Z
    source: archive|api
    reply_to: null|<id>
    ---
    <tweet text, threads concatenated>
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

HANDLE = "garrytan"
USER_ID = "19301828"  # @garrytan, stable numeric id
OUT = pathlib.Path(__file__).parent.parent / "data" / "x"
OUT.mkdir(parents=True, exist_ok=True)


def _slug(s: str, n: int = 40) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n]


def _write(tweet_id: str, date: str, text: str, source: str, reply_to: str | None) -> None:
    safe_date = date.split("T", 1)[0]
    path = OUT / f"{safe_date}_{tweet_id}.md"
    frontmatter = (
        "---\n"
        f"id: {tweet_id}\n"
        f"date: {date}\n"
        f"source: {source}\n"
        f"reply_to: {reply_to or 'null'}\n"
        "---\n\n"
    )
    path.write_text(frontmatter + text.strip() + "\n", encoding="utf-8")


def from_archive(archive_path: str) -> int:
    raw = pathlib.Path(archive_path).read_text(encoding="utf-8")
    payload = raw.split("=", 1)[1].strip().rstrip(";")
    tweets = json.loads(payload)
    for entry in tweets:
        t = entry.get("tweet", entry)
        _write(
            tweet_id=t["id_str"],
            date=t["created_at"],
            text=t["full_text"],
            source="archive",
            reply_to=t.get("in_reply_to_status_id_str"),
        )
    return len(tweets)


def from_api(bearer: str, max_tweets: int = 3200) -> int:
    n = 0
    pagination: str | None = None
    base = f"https://api.x.com/2/users/{USER_ID}/tweets"
    while n < max_tweets:
        params = {
            "max_results": "100",
            "tweet.fields": "created_at,in_reply_to_user_id,referenced_tweets",
            "exclude": "retweets",
        }
        if pagination:
            params["pagination_token"] = pagination
        req = urllib.request.Request(
            f"{base}?{urllib.parse.urlencode(params)}",
            headers={"Authorization": f"Bearer {bearer}"},
        )
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
        for t in data.get("data", []):
            reply_to = next(
                (r["id"] for r in t.get("referenced_tweets", []) if r["type"] == "replied_to"),
                None,
            )
            _write(
                tweet_id=t["id"],
                date=t["created_at"],
                text=t["text"],
                source="api",
                reply_to=reply_to,
            )
            n += 1
        pagination = data.get("meta", {}).get("next_token")
        if not pagination:
            break
        time.sleep(1)  # conservative pacing
    return n


def main() -> None:
    archive = os.environ.get("TWEET_ARCHIVE_JS")
    bearer = os.environ.get("X_BEARER_TOKEN")
    if archive:
        count = from_archive(archive)
        print(f"wrote {count} tweets from archive → {OUT}")
        return
    if bearer:
        count = from_api(bearer)
        print(f"wrote {count} tweets from X API → {OUT}")
        return
    sys.stderr.write(
        "need TWEET_ARCHIVE_JS=/path/to/tweets.js or X_BEARER_TOKEN=... in env\n"
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
