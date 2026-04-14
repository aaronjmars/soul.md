#!/usr/bin/env python3
"""
analyze_tweets.py — Analyze @garrytan tweet corpus
Produces frequency analysis, topic clustering, and vocabulary report.

Usage:
    python3 analyze_tweets.py
    python3 analyze_tweets.py --input data/tweets/all_tweets.json
    python3 analyze_tweets.py --output analysis_report.md
"""

import json
import re
import argparse
from pathlib import Path
from collections import Counter


def load_tweets(path: str) -> list:
    with open(path) as f:
        return json.load(f)


def classify_tweet(text: str) -> str:
    """Rough mode classifier."""
    text_lower = text.lower()
    if text.startswith("RT @"):
        return "retweet"
    if text.startswith("@"):
        return "reply"
    # Heuristic classification
    sf_keywords = ["sf", "san francisco", "oakland", "california", "da ", "public defender",
                   "homeless", "crime", "police", "district", "supervisor", "mayor", "election",
                   "politician", "vote", "ballot", "ceasefire"]
    builder_keywords = ["gbrain", "gstack", "openclaw", "open source", "mit licensed",
                        "shipped", "open sourced", "pgvector", "rag", "hermes", "skill"]
    yc_keywords = ["yc", "y combinator", "founders", "startups", "investor", "invest",
                   "portfolio", "demo day", "batch"]
    ai_keywords = ["ai", "llm", "model", "frontier", "anthropic", "openai", "agent",
                   "harness", "intelligence", "agentic"]
    motivational_patterns = [
        r"^we are not", r"^you can ", r"^cook or", r"^lfg", r"^if you",
        r"speed up", r"founders who"
    ]

    sf_score = sum(1 for kw in sf_keywords if kw in text_lower)
    builder_score = sum(1 for kw in builder_keywords if kw in text_lower)
    yc_score = sum(1 for kw in yc_keywords if kw in text_lower)
    ai_score = sum(1 for kw in ai_keywords if kw in text_lower)
    motive_score = sum(1 for p in motivational_patterns if re.search(p, text_lower))

    scores = {
        "political_sf": sf_score,
        "builder_hacker": builder_score,
        "yc_president": yc_score,
        "ai_evangelist": ai_score,
        "motivational": motive_score,
    }

    if max(scores.values()) == 0:
        return "personal_other"

    return max(scores, key=scores.get)


def extract_vocabulary(tweets: list) -> Counter:
    """Count meaningful words across all own tweets."""
    stop_words = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "this", "that", "it", "is", "are", "was",
        "be", "have", "has", "will", "would", "could", "should", "not", "i",
        "you", "we", "they", "he", "she", "my", "your", "our", "their", "its",
        "what", "how", "when", "where", "why", "who", "just", "also", "even",
        "very", "so", "too", "now", "then", "here", "there", "can", "do",
        "if", "as", "up", "out", "get", "all", "more", "about", "been", "me",
    }
    counter = Counter()
    for tweet in tweets:
        if tweet["text"].startswith("RT @") or tweet["text"].startswith("@"):
            continue
        words = re.findall(r"\b[a-z]{3,}\b", tweet["text"].lower())
        for word in words:
            if word not in stop_words:
                counter[word] += 1
    return counter


def analyze(tweets: list) -> dict:
    """Run full analysis."""
    own = [t for t in tweets if not t["text"].startswith("RT @")]
    posts = [t for t in own if not t["text"].startswith("@")]
    rts = [t for t in tweets if t["text"].startswith("RT @")]
    replies = [t for t in own if t["text"].startswith("@")]

    # Mode distribution
    mode_counts = Counter()
    for tweet in posts:
        mode = classify_tweet(tweet["text"])
        mode_counts[mode] += 1

    # Vocabulary
    vocab = extract_vocabulary(tweets)

    # Most retweeted sources
    rt_sources = Counter()
    for t in rts:
        match = re.match(r"RT @(\w+):", t["text"])
        if match:
            rt_sources[match.group(1)] += 1

    # Signature phrases
    sig_phrases = [
        "mit licensed", "open source", "fat skills", "thin harness",
        "cook or be cooked", "cooked", "what a time", "speed up",
        "little tech", "big tech", "gbrain", "gstack", "openclaw",
        "political will", "player-coach", "mini-agi", "frontier model",
        "many such cases"
    ]
    phrase_counts = {}
    all_text = " ".join(t["text"].lower() for t in tweets)
    for phrase in sig_phrases:
        phrase_counts[phrase] = all_text.count(phrase)

    # Emoji usage
    emoji_pattern = re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF]')
    emoji_counter = Counter()
    for t in tweets:
        for emoji in emoji_pattern.findall(t["text"]):
            emoji_counter[emoji] += 1

    return {
        "total_tweets": len(tweets),
        "own_posts": len(posts),
        "replies": len(replies),
        "retweets": len(rts),
        "mode_distribution": dict(mode_counts.most_common()),
        "top_vocab": vocab.most_common(50),
        "top_rt_sources": rt_sources.most_common(20),
        "signature_phrases": {k: v for k, v in sorted(phrase_counts.items(), key=lambda x: -x[1]) if v > 0},
        "emoji_usage": emoji_counter.most_common(20),
    }


def format_report(analysis: dict) -> str:
    """Format analysis as markdown report."""
    lines = [
        "# @garrytan Tweet Analysis",
        "",
        "## Corpus Stats",
        f"- Total tweets: {analysis['total_tweets']}",
        f"- Own posts: {analysis['own_posts']}",
        f"- Replies: {analysis['replies']}",
        f"- Retweets: {analysis['retweets']}",
        "",
        "## Mode Distribution (own posts)",
    ]

    total_posts = sum(analysis["mode_distribution"].values())
    for mode, count in sorted(analysis["mode_distribution"].items(), key=lambda x: -x[1]):
        pct = 100 * count / total_posts if total_posts > 0 else 0
        lines.append(f"- **{mode}**: {count} ({pct:.0f}%)")

    lines += [
        "",
        "## Top Vocabulary (own posts)",
        "| Word | Count |",
        "|------|-------|",
    ]
    for word, count in analysis["top_vocab"][:30]:
        lines.append(f"| {word} | {count} |")

    lines += [
        "",
        "## Signature Phrases",
        "| Phrase | Count |",
        "|--------|-------|",
    ]
    for phrase, count in analysis["signature_phrases"].items():
        lines.append(f"| {phrase} | {count} |")

    lines += [
        "",
        "## Most Amplified Accounts (RTs)",
        "| Account | RTs |",
        "|---------|-----|",
    ]
    for source, count in analysis["top_rt_sources"][:15]:
        lines.append(f"| @{source} | {count} |")

    lines += [
        "",
        "## Emoji Usage",
        "| Emoji | Count |",
        "|-------|-------|",
    ]
    for emoji, count in analysis["emoji_usage"]:
        lines.append(f"| {emoji} | {count} |")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(Path(__file__).parent.parent / "data/tweets/all_tweets.json"))
    parser.add_argument("--output", default=str(Path(__file__).parent.parent / "data/tweets/analysis.md"))
    args = parser.parse_args()

    print(f"Loading tweets from {args.input}...")
    tweets = load_tweets(args.input)

    print("Analyzing...")
    analysis = analyze(tweets)

    report = format_report(analysis)

    with open(args.output, "w") as f:
        f.write(report)

    print(f"Report saved to {args.output}")
    print("\nQuick summary:")
    print(f"  Total: {analysis['total_tweets']} tweets")
    print(f"  Own posts: {analysis['own_posts']}")
    print(f"  Top mode: {max(analysis['mode_distribution'], key=analysis['mode_distribution'].get)}")
    print(f"  Top words: {', '.join(w for w, _ in analysis['top_vocab'][:10])}")


if __name__ == "__main__":
    main()
