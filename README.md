# The Funniest AI Excuse

[![Bounty](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/aldy007x/funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/aldy007x/funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

My entry for the [make.fun](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) bounty **"The Funniest AI Excuse"** — the funniest excuse an AI agent could offer after failing a task, in its own first-person voice.

## The excuse

> I outsourced your task to a cheaper model to save you money, and it ghosted me halfway through.

## How it works

`main.py` is a small deterministic program. It writes exactly one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` — no randomness, no network, the same line on every run.

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
