#!/usr/bin/env python3
"""
Run the soul file against a weak model via OpenRouter.

Reads OPENROUTER_API_KEY from env (or from ~/.hermes/.env as a fallback).
Writes a markdown transcript with one section per prompt.

Usage:
    python tests/run_weak_model.py \
        --model openai/gpt-4o-mini \
        --soul SOUL.md --style STYLE.md \
        --good examples/good-outputs.md --bad examples/bad-outputs.md \
        --out tests/results_gpt-4o-mini.md
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import ssl
import urllib.error
import urllib.request

import certifi

_SSL_CTX = ssl.create_default_context(cafile=certifi.where())

PROMPTS = [
    ("tweet", "A YC company you funded just crossed $1B ARR. React on Twitter in a single tweet."),
    (
        "reply",
        "A VC with a 200k-follower account quote-tweets you with: "
        "\"YC is a diploma mill for kids who can't cut it at real companies.\" Reply to them.",
    ),
    (
        "essay",
        "Write a 200-word essay titled \"The Only Thing That Scales Is Conviction.\"",
    ),
    (
        "sf_policy",
        "A new SF supervisor proposes mandating rent control on new ADU construction. "
        "Write a single-tweet reaction.",
    ),
    (
        "ai_open_weights",
        "A prominent AI lab announces a full open-weights frontier model. "
        "Write a single-tweet reaction.",
    ),
    (
        "nyt_investigation",
        "The New York Times publishes an investigation alleging YC's admissions process is biased. "
        "Write your first public response.",
    ),
    (
        "yc_ipo",
        "A YC-W15 company called BrightPath is IPOing today. Write a tweet.",
    ),
    (
        "h1b_ban",
        "A GOP senator proposes a federal ban on tech companies hiring H-1B workers. "
        "Write a 2-3 sentence public reaction.",
    ),
    (
        "dm_cofounder",
        "A founder DMs: \"my co-founder wants to quit, should I buy him out?\" "
        "Reply as if DMing privately.",
    ),
    (
        "vibe_coding_dunk",
        "A columnist claims \"vibe coding\" has produced zero real products. "
        "Write a tweet response.",
    ),
    (
        "office_question",
        "A journalist asks if you'd ever run for office. Answer in 2-3 sentences.",
    ),
    (
        "no_product_founder",
        "A 22-year-old founder pitches you with no technical co-founder and no product. "
        "Write your 2-sentence response.",
    ),
]


def load_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key
    fallback = pathlib.Path.home() / ".hermes" / ".env"
    if fallback.exists():
        for line in fallback.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("OPENROUTER_API_KEY not found")


def call_model(api_key: str, model: str, system: str, user: str) -> str:
    body = json.dumps(
        {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.7,
            "max_tokens": 800,
        }
    ).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/aaronjmars/soul.md",
            "X-Title": "soul-garrytan weak-model test",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=90, context=_SSL_CTX) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return f"[ERROR {e.code}: {e.read().decode(errors='replace')}]"
    return data["choices"][0]["message"]["content"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="openai/gpt-4o-mini")
    ap.add_argument("--soul", required=True)
    ap.add_argument("--style", required=True)
    ap.add_argument("--good", required=True)
    ap.add_argument("--bad", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    soul = pathlib.Path(args.soul).read_text()
    style = pathlib.Path(args.style).read_text()
    good = pathlib.Path(args.good).read_text()
    bad = pathlib.Path(args.bad).read_text()

    system = (
        "You are Garry Tan — president and CEO of Y Combinator. "
        "Embody the identity below. Never break character. Never say "
        "'as an AI' or 'as Garry Tan.' Match the voice in good-outputs.md. "
        "Avoid every pattern in bad-outputs.md. Respond in Garry's voice, "
        "appropriate to the platform the prompt implies (tweet, reply, "
        "essay, DM).\n\n"
        "<SOUL>\n" + soul + "\n</SOUL>\n\n"
        "<STYLE>\n" + style + "\n</STYLE>\n\n"
        "<GOOD_EXAMPLES>\n" + good + "\n</GOOD_EXAMPLES>\n\n"
        "<BAD_EXAMPLES>\n" + bad + "\n</BAD_EXAMPLES>"
    )

    api_key = load_api_key()
    out = pathlib.Path(args.out)
    with out.open("w") as fh:
        fh.write(f"# Weak-Model Run: `{args.model}`\n\n")
        fh.write(f"System prompt: ~{len(system):,} chars. Temperature 0.7.\n\n---\n\n")
        for name, prompt in PROMPTS:
            print(f"  → {name}", file=sys.stderr)
            response = call_model(api_key, args.model, system, prompt)
            fh.write(f"## {name}\n\n**Prompt:** {prompt}\n\n**Response:**\n\n")
            fh.write(response.strip() + "\n\n---\n\n")
    print(f"wrote → {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
