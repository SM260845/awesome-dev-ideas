# Awesome Dev Ideas

[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Ideas](https://img.shields.io/badge/ideas-1152-brightgreen.svg)](#categories)
[![Lint](https://github.com/SM260845/awesome-dev-ideas/actions/workflows/lint.yml/badge.svg)](https://github.com/SM260845/awesome-dev-ideas/actions/workflows/lint.yml)
[![Links](https://github.com/SM260845/awesome-dev-ideas/actions/workflows/links.yml/badge.svg)](https://github.com/SM260845/awesome-dev-ideas/actions/workflows/links.yml)

A curated list of specific, buildable developer ideas: tools, products, forks and learning projects, with a one-line pitch, who it helps, a suggested stack and a difficulty for each. Every category has at least 50 entries, every link is verified, and duplicates are rejected by CI.

## Contents

- [How to use this list](#how-to-use-this-list)
- [Categories](#categories)
- [Entry format and legend](#entry-format-and-legend)
- [Contributing](#contributing)
- [License](#license)

## How to use this list

- **Looking for something to build this weekend?** Filter by 🟢 Beginner or 🟡 Intermediate in any category, or start with [Learning Projects](ideas/learning-projects.md).
- **Looking for a startup or serious portfolio piece?** Start with [Project Inspiration](ideas/project-inspiration.md) and [Micro-SaaS & Indie Apps](ideas/micro-saas-indie.md).
- **Want a head start?** [Fork Suggestions](ideas/fork-suggestions.md) lists real, licensed repos with a concrete idea for each fork.
- **Following 2026 trends?** Agent harnesses, MCP servers, skills, local models and AI security are covered in [AI, Agents & MCP](ideas/ai-agents-mcp.md) and [Security & Privacy](ideas/security-privacy.md).
- **Prior art** links point to an existing, related project worth studying first. Check what already exists before you build; the best ideas here fill a gap next to a proven one.

## Categories

The three core categories come first: **Dev Ideas**, **Project Inspiration** and **Fork Suggestions**. Each category has a one-line scope so ideas don't repeat across files.

<!-- counts:start -->
| Category | Ideas | Scope |
| --- | ---: | --- |
| [Dev Ideas](ideas/dev-ideas.md) | 107 | Things you import, embed or apply inside a codebase: libraries, testing, code quality, API and data-layer patterns, frontend engineering, observability and docs. |
| [Project Inspiration](ideas/project-inspiration.md) | 102 | Ambitious multi-week builds (platforms, engines, AI-native products, civic and science tools) worth a serious portfolio piece or a startup. |
| [Fork Suggestions](ideas/fork-suggestions.md) | 73 | Real, licensed open-source repos worth forking, each with a specific change: a new niche, a missing feature, a port or a revival. |
| [AI, Agents & MCP](ideas/ai-agents-mcp.md) | 74 | Agent harnesses, MCP servers, skills, memory, evals, local models and RAG. AI security lives in Security & Privacy. |
| [Developer Tools & CLIs](ideas/developer-tools-clis.md) | 92 | Tools developers run: CLIs, TUIs, editor extensions, local environments, API clients, profilers and build tooling. |
| [GitHub & Open Source Ecosystem](ideas/github-open-source.md) | 87 | GitHub Actions and Apps, maintainer and contributor tooling, repo health, community and OSS sustainability. |
| [Micro-SaaS & Indie Apps](ideas/micro-saas-indie.md) | 97 | Small web or mobile products a solo developer can ship and charge for: developer SaaS, niche AI tools, local-business and vertical apps. |
| [Automation & Workflows](ideas/automation-workflows.md) | 90 | Glue that connects existing services: personal and business automations, workflow engines, browser automation, bots and sync. |
| [Data & Analytics](ideas/data-analytics.md) | 82 | Pipelines, data quality, BI, product analytics, datasets, visualisation, notebooks and observability data. |
| [Security & Privacy](ideas/security-privacy.md) | 70 | AI and agent security, supply chain, secrets, AppSec, cloud hardening, privacy tools and detection. |
| [Games & Creative Coding](ideas/games-creative-coding.md) | 100 | Games, game tooling, generative art, music and audio, interactive experiments, retro and creative tools. |
| [Hardware, IoT & Self-hosting](ideas/hardware-iot-self-hosting.md) | 66 | Microcontrollers, home automation, local AI hardware, self-hosted services, networking, radio, backups and homelabs. |
| [Learning Projects: Beginner to Advanced](ideas/learning-projects.md) | 112 | Classic builds with a twist, grouped by level, each chosen to teach a specific concept. |
| **Total** | **1152** | |
<!-- counts:end -->

## Entry format and legend

Idea entries:

```markdown
- **Title**: One-line pitch.
  - **Why:** Why it's valuable and who needs it.
  - **Stack:** Suggested stack · **Difficulty:** 🟡 Intermediate · **Prior art:** [owner/repo](https://github.com/owner/repo)
```

Fork entries replace the stack with the fork idea, the licence and the star count from the GitHub API (with the date checked).

| Difficulty | Meaning |
| --- | --- |
| 🟢 Beginner | A weekend or two; common libraries; little infrastructure. |
| 🟡 Intermediate | A few weeks; several moving parts, some design decisions, real users possible. |
| 🔴 Advanced | Months, or deep expertise in systems, security, ML or hardware. |

**Prior art** is optional and only included when the link was verified to exist and match. It points to an existing, related project, not necessarily a competitor.

## Contributing

Suggestions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format, the quality bar, the no-duplicates rule and how links are verified, then [suggest an idea](https://github.com/SM260845/awesome-dev-ideas/issues/new?template=suggest-an-idea.yml) or open a pull request. Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

Local checks:

```bash
python3 scripts/count_entries.py --write   # update README counts, fail if a category has < 50
python3 scripts/check_duplicates.py        # reject duplicate or near-duplicate ideas
npx markdownlint-cli2 "**/*.md"            # markdown lint
lychee --config lychee.toml "**/*.md"      # link check
```

## License

To the extent possible under law, the contributors have waived all copyright and related rights to this list under [CC0 1.0 Universal](LICENSE). Linked projects keep their own licences.
