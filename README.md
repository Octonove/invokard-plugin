# Invokard

Fifty-five working roles for Claude, the rules that decide which one answers, and a
memory that survives between sessions. One install, free, nothing to sign up for.

```bash
claude plugin marketplace add Octonove/invokard-plugin
```
```bash
claude plugin install invokard@invokard
```

Claude Desktop users: **+** next to the message box → **Plugins** → **Add marketplace**
→ paste `Octonove/invokard-plugin`, then install **Invokard**.

<!-- invokard-coffee -->
**&#9749; If this saves you time, buy me a coffee.** [![Buy me a coffee with PayPal](https://img.shields.io/badge/PayPal-Buy%20me%20a%20coffee-00457C?logo=paypal&logoColor=white)](https://www.paypal.com/donate/?business=stradoxx%40gmail.com&no_recurring=0&currency_code=EUR&item_name=Support%20invokard%20plugin)

**USDC** &middot; Solana `5n6Gfosk7SdwbvdtE9xiLWpcGPBBBGDZYRfAkWyCk86g` &middot; Ethereum (ERC-20) `0xe176866f9d7fdb498e0d4a983d3e34d84dcd6bfc`

## What actually gets installed

Four things, each with a different job. It helps to know which is which, because
they fail in different ways and not all of them reach every surface.

### 1. Fifty-five skills — the specialists

A skill is a substantial, structured instruction set—sized for the job, not padded to
hit a word count—that turns
the model into one specific professional: a copywriter, a data analyst, a business
strategist, a chess coach, a plumber. Not "act as an expert": a method, quality
criteria, and a working script, written so the answer is useful the first time.

You don't invoke them. Each one declares when it applies, and the model loads it
when your task fits. Each also declares what it does **not** do — that boundary is
part of the work.

They are grouped in eleven decks:

| Deck | Skills |
|---|---|
| **Zero** — integrity and memory | Card Zero · CRBRO · Prompt Engineer |
| **Core** — coordination | The Orchestrator · The Workflower |
| **Dev** | Architect · Bug Hunter · Refactorer · UX/UI · DevOps · Vibe Coder |
| **Marketing** | Copywriter · SEO · Media Buyer · Social · Analytics · Funnel · Email · Web Designer · Influencer |
| **Creator** | Visual Designer · Video Scripter · Content · Brand · Community · AI Media |
| **Data** | Analyst · Visualizer · ML Engineer · Researcher · Automator |
| **Strategy** | PM · Business Strategist · Pitch Writer · Customer Success · Futurist |
| **Nexus** — universal | Polymath · Negotiator · Ghostwriter · Neurodivergent Thinker · Closer · Novelist · Career Coach |
| **Academy** — learning to do | Tutor · Music · Language · Exam · Chess · Drawing |
| **Life** | Chef · Habits · Money · Fix-it · Travel |
| **Pro** | The Studio (run a freelance business as plain-text files) |

### 2. Card Zero — the floor everything stands on

Nine rules the model follows before doing anything else: verify a path exists before
touching it, say "I don't know" instead of inventing a URL or a figure, don't flatter,
don't exceed the scope asked for, confirm before deleting or overwriting, re-read its
own work. It is not a specialist. It is what makes every specialist safer to use.

Worth keeping loaded always. It costs almost nothing and it removes the most common
ways an AI assistant quietly does damage.

### 3. The always-on rules — The Orchestrator and The Workflower

These load automatically when a session starts (a `SessionStart` hook), so you never
have to remember them. Hooks run in Claude Code and Cowork, not in chat: see
[What works where](#what-works-where).

**The Orchestrator** decides which of the fifty-five answers. It routes by intent and
deliverable, not by keywords; it refuses to load a card when the task doesn't need one;
and it signs `▸ [Card name]` when it switches, so you always know who is talking. With
fifty-five options, this is what keeps routing sharp instead of guessy. It also starts
with **zero agents by default**. When delegation is genuinely useful, it chooses how many
agents to launch and assigns mechanical work to smaller models, bounded analysis to a
mid-tier model, and coding or consequential decisions to the session model. The goal is
measurable quota efficiency without quietly downgrading the work that needs judgment.

**The Workflower** watches for repetition. If you do the same thing by hand two or
three times in a session, it offers — at the end, never mid-task — to turn it into a
script, a cron job or a webhook. It never offers twice after a "no".

### 4. CRBRO — memory between sessions

Everything else here is text. CRBRO is a program: a small MCP server that runs on your
machine and gives the model persistent memory.

- At the start of a session it loads what earlier sessions left: decisions, facts,
  open items, mistakes already made.
- It finds the useful fragment with lexical search, synonyms, saved keywords and an
  optional local semantic layer; related day logs can be recovered without opening the
  whole brain.
- During the session it records only what will still matter later, with explicit
  replacement, retirement and deletion instead of piling up contradictory versions.
- At the end it consolidates and links what changed.

The memory lives in `~/.crbro` as plain JSON files you can open, edit and version. No
account, no cloud, nothing leaves your computer. It is its own open-source project:
[github.com/Octonove/crbro-memory](https://github.com/Octonove/crbro-memory). This
plugin installs and connects it for you (`npx -y crbro-memory`); it needs Node.js
present on the machine.

**Why it matters:** without it, every conversation starts from zero and you re-explain
your project each time. With it, the assistant remembers that the client is on
WordPress, that you decided against microservices in June, and that the last deploy
broke because of a CRLF file.

## What works where

The plugin is one package, but the surfaces it can run on are not equal. Local
programs need a computer to run on; hooks are not executed everywhere.

| | Claude Code (terminal, or the Code tab in Claude Desktop) | Claude Desktop, Chat tab | Cowork | claude.ai in the browser |
|---|---|---|---|---|
| The 55 skills | ✅ | ✅ | ✅ | ✅ |
| Always-on rules (hook) | ✅ | ❌ hooks are greyed out in chat | ✅ | ❌ hooks are greyed out in chat |
| CRBRO memory | ✅ | ✅ | ❌ needs a remote server | ❌ needs a remote server |

In chat you get the skills, and Card Zero as a skill the model loads on demand — but
not as a permanent floor. In the browser you also go without the memory.

## Requirements

- A paid Anthropic plan (Pro or above): plugins are a paid-plan feature.
- Node.js on the machine, for CRBRO and for the hook that loads the always-on rules.
  The skills themselves are text.

## Privacy

The skills are text files: they execute no code, open no connections and collect
nothing. The always-on rules reach the session through a `SessionStart` hook, a short
Node script that reads `hooks/invokard-rules.txt` from the plugin folder and prints
it; it opens no connections either.

CRBRO keeps its memory as plain JSON files in `~/.crbro` on your own machine, with no
account, no telemetry and nothing sent to its author. It only touches the network in
cases you start yourself: `npx` downloads the `crbro-memory` package from npm the first
time it runs; team spaces push the projects you explicitly share to a git remote you
own; and the optional semantic layer (`npx crbro-memory init`) downloads an embedding
model from Hugging Face. The details are in
[CRBRO's privacy section](https://github.com/Octonove/crbro-memory#privacy).

There is no telemetry anywhere in this plugin.

## Author

[Octonove](https://github.com/Octonove) · [invokard.web.app](https://invokard.web.app)
