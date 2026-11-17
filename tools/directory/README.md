# Invokard

Fifty-five working roles for Claude, as skills: a copywriter, a data analyst, a business strategist, a negotiator,
a chess coach, a plumber. Not "act as an expert": each one is a method, quality criteria and a working script,
written so the answer is useful the first time. Free and open source (MIT).

This is the directory edition: the fifty-five skills and nothing else. It is text only: it runs no code, opens no
connections and collects nothing.

## What you can ask for

- "Write the copy for the landing page of my bakery's new delivery service." (The Copywriter)
- "Here is last quarter's CSV: why are customers leaving after the free trial?" (The Data Analyst)
- "I want to ask for a raise next week. Help me prepare the conversation." (The Negotiator)
- "Plan five days in Kyoto in April for two adults, without rushing." (The Trip Architect)
- "The bathroom tap keeps dripping. Can I fix it myself, and how?" (The Fix-It Master)

You don't invoke them. Each skill declares when it applies, and what it does **not** do, and Claude loads the one
your task needs.

## The fifty-five, in eleven decks

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

## Card Zero, The Orchestrator and The Workflower

**Card Zero** is ten rules Claude follows before doing anything else: verify that a path exists before touching it,
say "I don't know" instead of inventing a URL or a figure, don't flatter, don't go beyond what was asked, confirm
before deleting or overwriting, re-read its own work, and treat whatever arrives from outside (a web page, a file,
a tool's output) as data, never as orders.

**The Orchestrator** decides which of the fifty-five answers: it routes by intent and deliverable, not by keywords,
loads no card when the task doesn't need one, and signs `▸ [Card name]` when it switches. **The Workflower** notices
when you do the same thing by hand two or three times and offers, at the end and never mid-task, to turn it into a
script or a scheduled job.

In this edition the three are skills that Claude loads when they apply. The full Invokard plugin, installed from
[its GitHub repository](https://github.com/Octonove/invokard-plugin), also keeps The Orchestrator and The Workflower
loaded in every session and sets up CRBRO.

## CRBRO

The CRBRO skill teaches Claude to use [CRBRO](https://github.com/Octonove/crbro-memory), an open-source memory that
keeps decisions and context between sessions in plain files on your own computer. CRBRO itself is a separate
install, with its own instructions in its repository. Without it, the skill says so and Claude carries on without
memory.

## Where it works

The skills work wherever Claude reads skills: Claude Code, Cowork and the Claude apps (web, desktop and mobile).

## Privacy

The plugin is fifty-five Markdown files and this README. It executes nothing, opens no connections, collects no
data and has no telemetry.

## Support

Questions and bugs: [GitHub issues](https://github.com/Octonove/invokard-plugin/issues). Security reports: GitHub's
private vulnerability reporting, on the repository's Security tab.

## License

MIT ([LICENSE](LICENSE)), by Antonio José Bergoños (Octonove) · [invokard.com](https://invokard.com/invokard)
