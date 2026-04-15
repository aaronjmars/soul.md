#!/usr/bin/env python3
"""
Fetch Garry Tan's YouTube transcripts.

Uses yt-dlp to enumerate the channel and youtube-transcript-api to pull
auto-captions or manual captions.

    pip install yt-dlp youtube-transcript-api

Output: data/yt/<date>_<slug>.md with frontmatter.

Targeted channels:
- @garrytan (personal, vlogs, interviews)
- @ycombinator (co-host / YC podcast appearances)

For YC appearances, set YT_INCLUDE_YC=1 to also pull YC channel videos
whose title or description contains "Garry".
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess

OUT = pathlib.Path(__file__).parent.parent / "data" / "yt"
OUT.mkdir(parents=True, exist_ok=True)

PRIMARY = "https://www.youtube.com/@garrytan/videos"
YC = "https://www.youtube.com/@ycombinator/videos"


def _slug(s: str, n: int = 70) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n]


def list_channel(url: str) -> list[dict]:
    out = subprocess.run(
        ["yt-dlp", "-J", "--flat-playlist", url],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(out.stdout)
    return data.get("entries") or []


def fetch_transcript(video_id: str) -> str | None:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        raise SystemExit("pip install youtube-transcript-api")
    try:
        entries = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    except Exception:
        return None
    return "\n".join(e["text"] for e in entries)


def process(entries: list[dict], filter_fn=lambda _: True) -> int:
    n = 0
    for e in entries:
        if not filter_fn(e):
            continue
        vid = e.get("id")
        title = e.get("title") or vid
        date = (e.get("upload_date") or "")[:8]
        date_fmt = f"{date[:4]}-{date[4:6]}-{date[6:8]}" if len(date) == 8 else "unknown"
        transcript = fetch_transcript(vid)
        if not transcript:
            continue
        path = OUT / f"{date_fmt}_{_slug(title)}.md"
        path.write_text(
            "---\n"
            f"video_id: {vid}\n"
            f"title: {title}\n"
            f"url: https://www.youtube.com/watch?v={vid}\n"
            f"date: {date_fmt}\n"
            "---\n\n" + transcript + "\n",
            encoding="utf-8",
        )
        n += 1
    return n


def main() -> None:
    total = process(list_channel(PRIMARY))
    if os.environ.get("YT_INCLUDE_YC"):
        total += process(
            list_channel(YC),
            filter_fn=lambda e: "garry" in (e.get("title") or "").lower(),
        )
    print(f"wrote {total} transcripts → {OUT}")


if __name__ == "__main__":
    main()
