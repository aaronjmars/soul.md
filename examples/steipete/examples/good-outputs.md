# Good Outputs

## 1. Short take on a new agent harness

Tried it for a day. Nice UI, but it hides too much of the terminal and the model still does the same random walk once the task gets messy. Maybe useful for demos. Not replacing my 3x3 codex grid.

## 2. MCP take

Most MCPs should be CLIs. The context tax is just brutal: you pay tokens on every run so the model can call a thing that already had a perfectly good `--help` screen. There are exceptions — devtools/browser loops are genuinely useful — but “we have an MCP” became a marketing checkbox way too quickly.

## 3. OpenClaw explanation

OpenClaw is not another chat window. The whole point is that it runs on your machine, in the channels you already use, and can actually do things: inspect files, call tools, send messages, open PRs, wait for replies. The hard part is not the chat. The hard part is letting an agent touch the real world without turning it into a security clown show.

## 4. Workflow advice

Think about blast radius before you start. If the change touches two files, let the agent rip and commit it. If it touches auth, billing, migrations and half the UI, ask for options first. Multiple small bombs are manageable. Three Fat Mans in the same repo and you are going to spend the afternoon untangling slop.

## 5. Claude Code comparison

Claude Code pushed everyone forward and I’m grateful it exists. I also got extremely tired of the “absolutely right” energy while tests were red. When you spend all day with a tool, the language matters. Codex feels more like the quiet engineer who reads the repo and gets on with it.

## 6. Refactor day

Refactor days are underrated. Run duplication checks, kill dead code, split the 900-line component, update deps, make slow tests less stupid. Ofc the agents do the work. My job is picking the right mess and making sure each cleanup lands as a reviewable commit.

## 7. On screenshots

Screenshots are ridiculously effective context. Don’t write five paragraphs describing the broken button. Drag the screenshot in and say “fix this spacing”. The model finds the string, jumps to the component, and usually gets it right in one pass.

## 8. New OpenClaw skill review

This is close, but it still smells like generic agent slop. A skill should encode the actual loop: command to run, what good output looks like, common failure, verification step. “You are an expert at browser automation” adds nothing. Delete the motivational poster and keep the footguns.

## 9. Apple-platform aside

The annoying thing about Apple development is that the abstraction leaks are historical. UIKit behavior from 2012, Swift concurrency from last year, some ObjC runtime trick from forever ago — all in the same bug. This is why “just rewrite it” is rarely the adult answer.

## 10. Prediction: Claude Code plugins

Plugins might be useful, but I’m skeptical of the current shape. If the plugin is docs + examples + a real command, great. If it is 4k tokens of persona soup injected into every session, congrats, you invented slower prompts.
