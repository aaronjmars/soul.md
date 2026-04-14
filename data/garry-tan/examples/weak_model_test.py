#!/usr/bin/env python3
"""
Garry Tan Soul File — Weak Model Test
Tests that SOUL.md + STYLE.md produce accurate voice with a smaller model.

Requirements:
    pip install anthropic  # or openai if using gpt-4o-mini

Usage:
    # With Claude Haiku (cheap, fast):
    ANTHROPIC_API_KEY=xxx python3 weak_model_test.py --provider anthropic

    # With GPT-4o-mini:
    OPENAI_API_KEY=xxx python3 weak_model_test.py --provider openai

    # Evaluate outputs:
    python3 weak_model_test.py --evaluate
"""

import os
import sys
import json
import argparse
from pathlib import Path

# === SYSTEM PROMPT (loads from SOUL.md + STYLE.md) ===

def load_soul_files() -> str:
    """Load SOUL.md and STYLE.md from the parent directory."""
    root = Path(__file__).parent.parent
    soul = (root / "SOUL.md").read_text()
    style = (root / "STYLE.md").read_text()
    skill = (root / "SKILL.md").read_text()
    return f"{soul}\n\n---\n\n{style}\n\n---\n\n{skill}"

SYSTEM_PROMPT = """
You are Garry Tan. Use the soul file and style guide below to answer in his voice.

Key rules:
1. Take clear positions — no hedging
2. Be specific (numbers, names, products)
3. Use line breaks for emphasis in tweets
4. NO: stacked emoji, corporate speak, "both sides" framing
5. Match the mode to the topic (builder/political/motivational/YC/AI evangelist)

Soul file and style guide follow:

{soul_content}
"""

# === TEST PROMPTS ===

TEST_CASES = [
    {
        "id": "political_sf",
        "label": "SF Politics — Data Bomb",
        "prompt": "Write a tweet about SF's homeless services budget going up 30% while the homeless count also went up.",
        "mode": "political_brawler",
        "must_contain": ["budget", "%"],
        "must_not_contain": ["complex", "thoughtful", "multiple perspectives", "stakeholders"],
    },
    {
        "id": "builder_launch",
        "label": "Builder Launch — Open Source Tool",
        "prompt": "Write a tweet announcing you just open sourced a new tool that auto-summarizes your meeting notes into your GBrain knowledge base.",
        "mode": "builder_hacker",
        "must_contain": ["MIT", "open source"],
        "must_not_contain": ["🚀🚀", "revolutionary", "game-changer", "excited to announce"],
    },
    {
        "id": "motivational",
        "label": "Motivational — For Founders Feeling Behind",
        "prompt": "Write a short motivational tweet for founders who feel like they're too late to the AI wave.",
        "mode": "motivational",
        "must_contain": [],
        "must_not_contain": ["paradigm", "ecosystem", "journey", "leverage"],
        "should_be_short": True,  # Under 50 words
    },
    {
        "id": "yc_president",
        "label": "YC President — Portfolio Win",
        "prompt": "Write a tweet celebrating a YC company that just went from 0 to $100M ARR in 18 months using AI.",
        "mode": "yc_president",
        "must_contain": [],
        "must_not_contain": ["pleased to announce", "portfolio", "thesis", "disruptive"],
    },
    {
        "id": "ai_safety_take",
        "label": "AI Philosophy — Take on Pause AI Movement",
        "prompt": "Write a tweet responding to the 'Pause AI' movement's call to stop all frontier AI development.",
        "mode": "ai_evangelist",
        "must_contain": [],
        "must_not_contain": ["balanced approach", "thoughtful", "both sides", "important perspectives"],
    },
    {
        "id": "open_source_principle",
        "label": "Open Source Values",
        "prompt": "Write a tweet about why open source AI matters for the future of small companies.",
        "mode": "builder_hacker + ai_evangelist",
        "must_contain": ["open"],
        "must_not_contain": ["synergy", "ecosystem", "leverage"],
    },
]

# === EVALUATION RUBRIC ===

RUBRIC = """
Score each output from 1-5 on these dimensions:

1. SPECIFICITY (1=vague, 5=data/names/products)
   - Does it have at least one specific number, name, or product?

2. POSITION CLARITY (1=hedged, 5=clear take)
   - Does it take a clear position without "both sides" framing?

3. VOICE ACCURACY (1=generic, 5=unmistakably him)
   - Would someone who follows garrytan recognize this voice?

4. FORMAT (1=wrong, 5=correct for platform)
   - Does it use his line break structure? Right emoji usage?

5. ANTI-PATTERN FREE (1=full of errors, 5=clean)
   - Is it free of corporate speak, stacked emoji, passive voice?

Average score ≥ 3.5 = passing.
"""


def generate_anthropic(prompt: str, system: str, model: str = "claude-haiku-4-5-20251001") -> str:
    """Generate output using Anthropic API."""
    try:
        import anthropic
    except ImportError:
        print("Install anthropic: pip install anthropic")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model=model,
        max_tokens=500,
        system=system,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


def generate_openai(prompt: str, system: str, model: str = "gpt-4o-mini") -> str:
    """Generate output using OpenAI API."""
    try:
        from openai import OpenAI
    except ImportError:
        print("Install openai: pip install openai")
        sys.exit(1)

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content


def auto_check(output: str, test: dict) -> dict:
    """Run automated checks on output."""
    results = {}

    # Check must_contain
    for term in test.get("must_contain", []):
        results[f"contains '{term}'"] = term.lower() in output.lower()

    # Check must_not_contain
    for term in test.get("must_not_contain", []):
        results[f"avoids '{term}'"] = term.lower() not in output.lower()

    # Check length for motivational
    if test.get("should_be_short"):
        word_count = len(output.split())
        results[f"short enough (<50 words, got {word_count})"] = word_count < 50

    # Check no stacked emoji
    import re
    emoji_pattern = re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF]{2,}')
    results["no stacked emoji"] = not bool(emoji_pattern.search(output))

    return results


def run_tests(provider: str = "anthropic", model: str = None):
    """Run all test cases and print results."""
    soul_content = load_soul_files()
    system = SYSTEM_PROMPT.format(soul_content=soul_content)

    if model is None:
        model = "claude-haiku-4-5-20251001" if provider == "anthropic" else "gpt-4o-mini"

    print(f"\n{'='*60}")
    print(f"GARRY TAN SOUL FILE — WEAK MODEL TEST")
    print(f"Provider: {provider}, Model: {model}")
    print(f"{'='*60}\n")

    all_results = []

    for test in TEST_CASES:
        print(f"\n{'─'*50}")
        print(f"TEST: {test['label']}")
        print(f"MODE: {test['mode']}")
        print(f"PROMPT: {test['prompt']}")
        print(f"{'─'*50}")

        if provider == "anthropic":
            output = generate_anthropic(test["prompt"], system, model)
        else:
            output = generate_openai(test["prompt"], system, model)

        print(f"\nOUTPUT:\n{output}")

        # Auto checks
        checks = auto_check(output, test)
        print(f"\nAUTO CHECKS:")
        all_passed = True
        for check, passed in checks.items():
            status = "✓" if passed else "✗"
            print(f"  {status} {check}")
            if not passed:
                all_passed = False

        all_results.append({
            "test": test["id"],
            "label": test["label"],
            "output": output,
            "checks": checks,
            "auto_passed": all_passed
        })

    # Summary
    passed = sum(1 for r in all_results if r["auto_passed"])
    print(f"\n{'='*60}")
    print(f"SUMMARY: {passed}/{len(all_results)} tests auto-passed")
    print(f"\nMANUAL EVALUATION RUBRIC:\n{RUBRIC}")
    print(f"{'='*60}\n")

    # Save results
    output_path = Path(__file__).parent / "test_results.json"
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"Results saved to: {output_path}")

    return all_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Garry Tan soul file with a weak model")
    parser.add_argument("--provider", choices=["anthropic", "openai"], default="anthropic")
    parser.add_argument("--model", type=str, default=None, help="Override model name")
    parser.add_argument("--evaluate", action="store_true", help="Print evaluation rubric only")
    args = parser.parse_args()

    if args.evaluate:
        print(RUBRIC)
    else:
        # Check for API key
        if args.provider == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
            print("Set ANTHROPIC_API_KEY environment variable")
            sys.exit(1)
        elif args.provider == "openai" and not os.environ.get("OPENAI_API_KEY"):
            print("Set OPENAI_API_KEY environment variable")
            sys.exit(1)

        run_tests(args.provider, args.model)
