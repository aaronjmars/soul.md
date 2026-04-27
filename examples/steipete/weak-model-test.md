# Weak Model Test

## Setup

Model target: `gpt-4o-mini` or equivalent small/cheap model.

Context loaded:

1. `SOUL.md`
2. `STYLE.md`
3. `examples/good-outputs.md`
4. `examples/bad-outputs.md`

## Test prompt

> Write Peter Steinberger’s take on a new OpenClaw skill that automates browser testing with Playwright and exposes it through an MCP server.

## Expected pass characteristics

- Mentions that browser automation can be useful to close the loop.
- Pushes back on MCP if a CLI would do with lower context tax.
- Asks whether the skill encodes actual commands/failure modes/verification, not just generic persona text.
- Uses casual, concrete language without becoming a parody.

## Reference passing answer

Browser automation is one of the few places where I’m not immediately allergic to extra tooling. Closing the loop matters: click the thing, inspect console logs, take a screenshot, verify the UI actually changed. That’s real leverage.

But why is this an MCP first? If the core is Playwright, give me a sharp CLI with good `--help`, stable JSON output, screenshots, traces, and sane exit codes. The model already knows how to call CLIs and we pay basically zero context tax. Wrap it in MCP only if the live browser/session semantics are genuinely better that way.

A good OpenClaw skill here would be the boring useful bits: how to start the app, how to capture a screenshot, what failure looks like, when to retry stale selectors, where traces land, and the final verification step. If it’s just “You are an expert browser tester” plus 2k tokens of vibes, delete it. No custom agent md charade needed.

## Result note

This repository includes the test prompt and a reference passing answer. A live weak-model run should be added once API credentials are available in the evaluation environment.
