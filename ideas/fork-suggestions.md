# Fork Suggestions

> **Scope:** Real, licensed open-source repos worth forking, each with a specific change: a new niche, a missing feature, a port or a revival.

Every repo below was checked via the GitHub API on 2026-09-28: it exists, has a licence and is not archived (unless the idea is to revive it). Star counts are rounded API values from that date. Check the licence yourself before forking; copyleft licences (GPL/AGPL) carry obligations.

57 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [AI & agents](#ai--agents)
- [Developer tools](#developer-tools)
- [GitHub & open source](#github--open-source)
- [Self-hosting & productivity](#self-hosting--productivity)
- [Security & privacy](#security--privacy)
- [Media & creative](#media--creative)
- [Learning resources](#learning-resources)

## AI & agents

- **[openai/codex](https://github.com/openai/codex)**: OpenAI's open-source coding agent CLI.
  - **Fork idea:** A local-model-first variant tuned for small context windows: aggressive repo maps, smaller tool schemas and Ollama/llama.cpp defaults.
  - **Why:** Many developers want an agent harness that works well offline, not just technically supports it.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~126.8k · **Difficulty:** 🔴 Advanced

- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)**: Google's open-source terminal AI agent.
  - **Fork idea:** A domain-specific agent CLI for infrastructure operations, with read-only cloud tools by default and a plan/apply approval flow.
  - **Why:** Ops teams want agent help but fear write access; a narrow fork can ship safer defaults.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~107.2k · **Difficulty:** 🔴 Advanced

- **[modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)**: Visual testing tool for MCP servers.
  - **Fork idea:** Add an authorization debugging mode that walks through the MCP OAuth flow step by step with token and scope inspection.
  - **Why:** Auth is where remote MCP servers most often fail, and it's hard to see what went wrong.
  - **Licence:** MIT → Apache-2.0 (transition, per LICENSE) · **Stars (2026-09-28):** ~11k · **Difficulty:** 🟡 Intermediate

- **[ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram)**: Turns any GitHub repo into an interactive architecture diagram.
  - **Fork idea:** A fully local fork for private repos: local model, no external API calls, output committed to the repo.
  - **Why:** Companies can't send private code to hosted services.
  - **Licence:** MIT · **Stars (2026-09-28):** ~17.2k · **Difficulty:** 🟡 Intermediate

- **[microsoft/graphrag](https://github.com/microsoft/graphrag)**: Graph-based retrieval-augmented generation pipeline.
  - **Fork idea:** A lightweight, cost-capped fork that runs end to end on local models with incremental indexing.
  - **Why:** GraphRAG indexing costs are a common complaint; a local, incremental version widens adoption.
  - **Licence:** MIT · **Stars (2026-09-28):** ~36.1k · **Difficulty:** 🔴 Advanced

- **[mem0ai/mem0](https://github.com/mem0ai/mem0)**: Memory layer for AI agents and assistants.
  - **Fork idea:** A single-binary, SQLite-backed edition with no external vector database, for desktop apps and CLIs.
  - **Why:** Local tools want memory without running extra services.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~66.1k · **Difficulty:** 🟡 Intermediate

- **[jina-ai/reader](https://github.com/jina-ai/reader)**: Converts URLs into LLM-friendly text.
  - **Fork idea:** A self-hosted edition with a local headless browser pool, caching and robots.txt respect by default.
  - **Why:** Teams want reader-style extraction without sending URLs to a hosted API.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~12.1k · **Difficulty:** 🟡 Intermediate

- **[LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)**: Self-hosted multi-model chat UI.
  - **Fork idea:** A small-business edition with pre-configured MCP tools (calendar, invoices, docs) and simple role permissions.
  - **Why:** SMBs want a private assistant but can't configure MCP themselves.
  - **Licence:** MIT · **Stars (2026-09-28):** ~45k · **Difficulty:** 🟡 Intermediate

- **[Aider-AI/aider](https://github.com/Aider-AI/aider)**: AI pair programming in the terminal.
  - **Fork idea:** Add first-class MCP client support and SKILL.md loading while keeping aider's git-native workflow.
  - **Why:** Aider's git-centric UX is loved; modern tool ecosystems would extend its life.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~49.2k · **Difficulty:** 🟡 Intermediate

- **[microsoft/markitdown](https://github.com/microsoft/markitdown)**: Converts Office files and PDFs to Markdown for LLMs.
  - **Fork idea:** Port to TypeScript for edge runtimes and browsers, keeping the converter plugin model.
  - **Why:** JavaScript-only stacks (edge functions, extensions) can't run the Python version.
  - **Licence:** MIT · **Stars (2026-09-28):** ~187.4k · **Difficulty:** 🟡 Intermediate

## Developer tools

- **[jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)**: Terminal UI for git.
  - **Fork idea:** A worktree dashboard mode for parallel coding agents: one pane per worktree with diff, test status and merge actions.
  - **Why:** Running several agents in parallel worktrees is common and hard to supervise from a plain git UI.
  - **Licence:** MIT · **Stars (2026-09-28):** ~82.7k · **Difficulty:** 🟡 Intermediate

- **[jgraph/drawio](https://github.com/jgraph/drawio)**: The draw.io diagramming app.
  - **Fork idea:** Two-way sync between draw.io files and Mermaid or D2 text so diagrams can be reviewed as code.
  - **Why:** Upstream states it does not accept pull requests, so extensions like this need a fork.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~8.4k · **Difficulty:** 🔴 Advanced

- **[Wilfred/difftastic](https://github.com/Wilfred/difftastic)**: Structural diff tool that understands syntax.
  - **Fork idea:** A web viewer and GitHub PR integration that renders difftastic output in review.
  - **Why:** Structural diffs are most valuable during code review, where they're currently unavailable.
  - **Licence:** MIT · **Stars (2026-09-28):** ~25.9k · **Difficulty:** 🟡 Intermediate

- **[jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker)**: Terminal UI for Docker and Compose.
  - **Fork idea:** Add first-class Podman and Kubernetes (kind/k3s) contexts in the same UI.
  - **Why:** Many developers moved to Podman or local Kubernetes and lost this workflow.
  - **Licence:** MIT · **Stars (2026-09-28):** ~53k · **Difficulty:** 🟡 Intermediate

- **[tsl0922/ttyd](https://github.com/tsl0922/ttyd)**: Share a terminal over the web.
  - **Fork idea:** Multi-user sessions with per-user control handoff, recording to asciicast and SSO.
  - **Why:** Pairing and incident response need shared terminals with auditability.
  - **Licence:** MIT · **Stars (2026-09-28):** ~12.4k · **Difficulty:** 🟡 Intermediate

- **[sharkdp/hyperfine](https://github.com/sharkdp/hyperfine)**: Command-line benchmarking tool.
  - **Fork idea:** Add peak memory and I/O measurement (RSS, bytes read and written) alongside timing results.
  - **Why:** Performance work often trades time for memory; seeing both avoids surprises.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~28.9k · **Difficulty:** 🟡 Intermediate

- **[antirez/kilo](https://github.com/antirez/kilo)**: A text editor in under 1,000 lines of C.
  - **Fork idea:** A teaching fork that adds UTF-8, multiple buffers and undo, one commit per feature with notes.
  - **Why:** A readable step-by-step history turns it into a great systems programming course.
  - **Licence:** BSD-2-Clause · **Stars (2026-09-28):** ~9.1k · **Difficulty:** 🟡 Intermediate

- **[usebruno/bruno](https://github.com/usebruno/bruno)**: Offline, git-friendly API client.
  - **Fork idea:** Add MCP server testing: list tools, call them with forms and snapshot responses.
  - **Why:** MCP developers lack a friendly client comparable to REST tooling.
  - **Licence:** MIT · **Stars (2026-09-28):** ~47.2k · **Difficulty:** 🟡 Intermediate

- **[gchq/CyberChef](https://github.com/gchq/CyberChef)**: Web app for encoding, decoding and data analysis.
  - **Fork idea:** A desktop edition with a shareable recipe library and an "explain this blob" helper using a local model.
  - **Why:** Analysts reuse recipes constantly but share them as URLs in chat.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~36k · **Difficulty:** 🟡 Intermediate

- **[mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)**: Interactive HTTPS proxy.
  - **Fork idea:** An LLM-traffic edition that decodes provider APIs to show prompts, tool calls, tokens and cost per request.
  - **Why:** Developers debugging agents need to see exactly what's sent to model APIs.
  - **Licence:** MIT · **Stars (2026-09-28):** ~45.2k · **Difficulty:** 🟡 Intermediate

- **[wagoodman/dive](https://github.com/wagoodman/dive)**: Tool for exploring Docker image layers.
  - **Fork idea:** Add side-by-side comparison of two image tags and multi-arch index support.
  - **Why:** Knowing what changed between two releases of an image is a common question.
  - **Licence:** MIT · **Stars (2026-09-28):** ~54.6k · **Difficulty:** 🟡 Intermediate

- **[louislam/dockge](https://github.com/louislam/dockge)**: Self-hosted docker-compose stack manager.
  - **Fork idea:** Add git sync so stacks are stored in a repo and changes arrive as commits.
  - **Why:** GitOps for small homelabs without Kubernetes.
  - **Licence:** MIT · **Stars (2026-09-28):** ~24.5k · **Difficulty:** 🟡 Intermediate

## GitHub & open source

- **[mitchellh/vouch](https://github.com/mitchellh/vouch)**: Lets maintainers vouch for trusted contributors.
  - **Fork idea:** Federated vouch lists shared across projects, with revocation and an audit trail.
  - **Why:** Trust earned in one project should carry to related projects.
  - **Licence:** MIT · **Stars (2026-09-28):** ~5.1k · **Difficulty:** 🟡 Intermediate

- **[ctrf-io/github-test-reporter](https://github.com/ctrf-io/github-test-reporter)**: GitHub Action that reports test results in PRs.
  - **Fork idea:** Add a GitHub Pages dashboard of test history: slowest tests, failure trends per file and suite duration over time.
  - **Why:** PR comments show one run; maintainers need trends to prioritise test work.
  - **Licence:** MIT · **Stars (2026-09-28):** ~376 · **Difficulty:** 🟡 Intermediate

- **[sindresorhus/awesome-lint](https://github.com/sindresorhus/awesome-lint)**: Linter for awesome lists.
  - **Fork idea:** A variant for structured idea/resource lists: entry schema checks, duplicate detection and verified links.
  - **Why:** Curated lists grow messy without schema-level validation.
  - **Licence:** MIT · **Stars (2026-09-28):** ~831 · **Difficulty:** 🟢 Beginner

- **[anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats)**: Dynamic GitHub stats cards for READMEs.
  - **Fork idea:** Add GitLab, Codeberg and Forgejo support in one card.
  - **Why:** Developers increasingly split work across forges.
  - **Licence:** MIT · **Stars (2026-09-28):** ~79.8k · **Difficulty:** 🟡 Intermediate

- **[probot/probot](https://github.com/probot/probot)**: Framework for building GitHub Apps.
  - **Fork idea:** A modern fork with first-class GitHub Actions deployment, typed webhooks and an agent-tool (MCP) interface.
  - **Why:** Many bots still use Probot; a modern runtime would lower hosting friction.
  - **Licence:** ISC · **Stars (2026-09-28):** ~9.6k · **Difficulty:** 🟡 Intermediate

- **[public-apis/public-apis](https://github.com/public-apis/public-apis)**: Curated list of free public APIs.
  - **Fork idea:** A live directory that health-checks every API daily and shows uptime, auth type and CORS support.
  - **Why:** Many listed APIs are dead or changed; live status saves developers time.
  - **Licence:** MIT · **Stars (2026-09-28):** ~483.9k · **Difficulty:** 🟡 Intermediate

## Self-hosting & productivity

- **[usememos/memos](https://github.com/usememos/memos)**: Lightweight self-hosted notes.
  - **Fork idea:** Add an MCP server so agents can read and write personal notes with scoped permissions.
  - **Why:** Personal notes become useful agent memory without a vendor lock-in.
  - **Licence:** MIT · **Stars (2026-09-28):** ~63.4k · **Difficulty:** 🟡 Intermediate

- **[paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)**: Document management with OCR.
  - **Fork idea:** A small-business edition focused on invoices and receipts with accounting-software export.
  - **Why:** SMBs need bookkeeping flows more than a general archive.
  - **Licence:** GPL-3.0 · **Stars (2026-09-28):** ~46.1k · **Difficulty:** 🟡 Intermediate

- **[actualbudget/actual](https://github.com/actualbudget/actual)**: Local-first personal finance app.
  - **Fork idea:** Add importers for more national bank export formats and a local transaction categoriser.
  - **Why:** Bank import coverage is the main blocker for non-US users.
  - **Licence:** MIT · **Stars (2026-09-28):** ~29.2k · **Difficulty:** 🟡 Intermediate

- **[mealie-recipes/mealie](https://github.com/mealie-recipes/mealie)**: Self-hosted recipe manager and meal planner.
  - **Fork idea:** Add nutrition data and dietary-restriction planning (allergies, diabetes).
  - **Why:** Families with dietary needs are underserved by generic planners.
  - **Licence:** AGPL-3.0 · **Stars (2026-09-28):** ~13.4k · **Difficulty:** 🟡 Intermediate

- **[dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io)**: Website change monitoring.
  - **Fork idea:** A vertical edition for government tenders and grants with keyword scoring.
  - **Why:** Small businesses miss tenders because portals are hard to monitor.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~34.6k · **Difficulty:** 🟡 Intermediate

- **[miniflux/v2](https://github.com/miniflux/v2)**: Minimalist feed reader.
  - **Fork idea:** Add story clustering and deduplication across feeds with a daily digest.
  - **Why:** Heavy feed readers drown in duplicate coverage of the same story.
  - **Licence:** Apache-2.0 · **Stars (2026-09-28):** ~9.7k · **Difficulty:** 🟡 Intermediate

- **[knadh/listmonk](https://github.com/knadh/listmonk)**: Self-hosted newsletter and mailing list manager.
  - **Fork idea:** Add paid subscriptions and gated posts for independent writers.
  - **Why:** Writers want Substack-style monetisation on their own infrastructure.
  - **Licence:** AGPL-3.0 · **Stars (2026-09-28):** ~23.6k · **Difficulty:** 🔴 Advanced

- **[documenso/documenso](https://github.com/documenso/documenso)**: Open-source document signing.
  - **Fork idea:** Pre-built templates and field rules for one country's real estate or rental forms.
  - **Why:** Vertical templates are what small agencies actually pay for.
  - **Licence:** AGPL-3.0 · **Stars (2026-09-28):** ~15.2k · **Difficulty:** 🟡 Intermediate

- **[pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)**: Backend in one file: database, auth, files and realtime.
  - **Fork idea:** Add a built-in MCP endpoint so agents can query and modify collections under PocketBase's rules.
  - **Why:** A one-binary backend that agents can safely operate is attractive for prototypes.
  - **Licence:** MIT · **Stars (2026-09-28):** ~61.2k · **Difficulty:** 🟡 Intermediate

- **[BookStackApp/BookStack](https://github.com/BookStackApp/BookStack)**: Self-hosted wiki platform.
  - **Fork idea:** Two-way sync between BookStack pages and Markdown files in a git repo.
  - **Why:** Teams want wiki editing for non-developers and docs-as-code for engineers.
  - **Licence:** MIT · **Stars (2026-09-28):** ~19.1k · **Difficulty:** 🟡 Intermediate

- **[huginn/huginn](https://github.com/huginn/huginn)**: Self-hosted agents that monitor and act on your behalf.
  - **Fork idea:** Modernise the UI and add LLM-powered agent types while keeping its event-driven model.
  - **Why:** Huginn's design predates LLMs; a refresh fits current automation demand.
  - **Licence:** MIT · **Stars (2026-09-28):** ~50k · **Difficulty:** 🟡 Intermediate

- **[monicahq/monica](https://github.com/monicahq/monica)**: Personal relationship manager.
  - **Fork idea:** A local-first mobile edition that syncs with the self-hosted server.
  - **Why:** Personal CRM is used on the go; a mobile-first client fits real usage.
  - **Licence:** AGPL-3.0 · **Stars (2026-09-28):** ~25.4k · **Difficulty:** 🔴 Advanced

- **[kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools)**: Tools for serving offline Wikipedia and other ZIM archives.
  - **Fork idea:** Add delta updates and peer-to-peer sync so remote sites can share ZIM updates over a LAN or USB drive.
  - **Why:** Downloading full archives again is impractical on slow or no internet.
  - **Licence:** GPL-3.0 · **Stars (2026-09-28):** ~957 · **Difficulty:** 🔴 Advanced

## Security & privacy

- **[OWASP/pytm](https://github.com/OWASP/pytm)**: Pythonic threat modelling framework.
  - **Fork idea:** Add threat patterns for LLM apps and agents: prompt injection, tool abuse, MCP trust boundaries.
  - **Why:** Threat modelling tools haven't caught up with agent architectures.
  - **Licence:** MIT (per LICENSE) · **Stars (2026-09-28):** ~1.2k · **Difficulty:** 🟡 Intermediate

- **[sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)**: Finds usernames across social networks.
  - **Fork idea:** A privacy edition that finds your own old accounts and links to each site's deletion page.
  - **Why:** Reducing your digital footprint starts with knowing where you're registered.
  - **Licence:** MIT · **Stars (2026-09-28):** ~92.9k · **Difficulty:** 🟢 Beginner

- **[cowrie/cowrie](https://github.com/cowrie/cowrie)**: SSH and Telnet honeypot.
  - **Fork idea:** Add LLM-generated shell responses for higher-interaction deception, with safety limits.
  - **Why:** Richer interaction reveals more attacker behaviour.
  - **Licence:** BSD-3-Clause (per LICENSE) · **Stars (2026-09-28):** ~6.6k · **Difficulty:** 🔴 Advanced

## Media & creative

- **[excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)**: Virtual hand-drawn style whiteboard.
  - **Fork idea:** A desktop edition with git-backed storage and diagram-from-text using a local model.
  - **Why:** Engineers want diagrams versioned with code and offline.
  - **Licence:** MIT · **Stars (2026-09-28):** ~133.1k · **Difficulty:** 🟡 Intermediate

- **[motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas)**: Library for programmatic animated videos.
  - **Fork idea:** A code-explainer toolkit: animated diffs, file trees and call graphs from a repo.
  - **Why:** Developer education videos need code-aware primitives.
  - **Licence:** MIT · **Stars (2026-09-28):** ~19.2k · **Difficulty:** 🟡 Intermediate

- **[mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)**: Bitmap and tilemap generation algorithm.
  - **Fork idea:** A Godot plugin with an editor UI for rules and live previews.
  - **Why:** Game developers want WFC inside their engine, not as a separate tool.
  - **Licence:** MIT (per LICENSE) · **Stars (2026-09-28):** ~25.3k · **Difficulty:** 🟡 Intermediate

- **[boardgameio/boardgame.io](https://github.com/boardgameio/boardgame.io)**: State management and multiplayer for turn-based games.
  - **Fork idea:** Add a serverless peer-to-peer (WebRTC) transport and a static-hosted lobby template.
  - **Why:** Casual game makers want to share a link without running a game server.
  - **Licence:** MIT · **Stars (2026-09-28):** ~12.4k · **Difficulty:** 🟡 Intermediate

- **[ManimCommunity/manim](https://github.com/ManimCommunity/manim)**: Animation engine for explanatory maths videos.
  - **Fork idea:** A browser-based live editor with instant previews for teaching.
  - **Why:** Install friction stops teachers from trying Manim.
  - **Licence:** MIT · **Stars (2026-09-28):** ~41.1k · **Difficulty:** 🔴 Advanced

- **[wulkano/Kap](https://github.com/wulkano/Kap)**: Open-source screen recorder for macOS.
  - **Fork idea:** Revive it on current macOS capture APIs and add a cross-platform build.
  - **Why:** A simple, open screen recorder is still in demand; the last release was v3.6.0 in Oct 2022.
  - **Licence:** MIT · **Stars (2026-09-28):** ~19.4k · **Difficulty:** 🔴 Advanced

- **[marktext/marktext](https://github.com/marktext/marktext)**: Simple, elegant Markdown editor.
  - **Fork idea:** A writer's edition with git-backed sync and one-click publishing to static-site generators.
  - **Why:** Writers want a distraction-free editor that also handles versioning and publishing.
  - **Licence:** MIT · **Stars (2026-09-28):** ~61.9k · **Difficulty:** 🟡 Intermediate

## Learning resources

- **[cstack/db_tutorial](https://github.com/cstack/db_tutorial)**: Build a simple SQLite clone from scratch in C.
  - **Fork idea:** Continue the series with deletes, transactions and a write-ahead log in the same step-by-step style.
  - **Why:** A popular tutorial whose last commit was in March 2024; readers finish it wanting these parts.
  - **Licence:** MIT · **Stars (2026-09-28):** ~10.5k · **Difficulty:** 🔴 Advanced

- **[karpathy/micrograd](https://github.com/karpathy/micrograd)**: A tiny autograd engine with a neural network library.
  - **Fork idea:** An interactive web version that visualises the computation graph and gradients as you train.
  - **Why:** Seeing backprop step by step makes it click for more learners.
  - **Licence:** MIT · **Stars (2026-09-28):** ~17.7k · **Difficulty:** 🟡 Intermediate

- **[jamiebuilds/the-super-tiny-compiler](https://github.com/jamiebuilds/the-super-tiny-compiler)**: A tiny, heavily commented compiler in JavaScript.
  - **Fork idea:** Extend with a type-checking chapter and a WebAssembly backend in the same annotated style.
  - **Why:** Readers finish it wanting the next step.
  - **Licence:** CC-BY-4.0 · **Stars (2026-09-28):** ~28.6k · **Difficulty:** 🟡 Intermediate

- **[rui314/chibicc](https://github.com/rui314/chibicc)**: A small C compiler.
  - **Fork idea:** Add a RISC-V or WebAssembly backend as a learning exercise with commit-by-commit notes.
  - **Why:** Retargeting a compiler is a great advanced project with a clean base.
  - **Licence:** MIT · **Stars (2026-09-28):** ~11.9k · **Difficulty:** 🔴 Advanced

- **[donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)**: Guide to designing large-scale systems.
  - **Fork idea:** Add interactive simulations (caching, sharding, queues) readers can tweak in the browser.
  - **Why:** System design sticks better when you can watch it fail.
  - **Licence:** CC-BY-4.0 (per LICENSE) · **Stars (2026-09-28):** ~372.2k · **Difficulty:** 🔴 Advanced

- **[tokio-rs/mini-redis](https://github.com/tokio-rs/mini-redis)**: Incomplete, idiomatic Redis implementation built with Tokio.
  - **Fork idea:** Add replication and cluster mode as documented lessons.
  - **Why:** Extends a trusted async Rust teaching codebase into distributed systems.
  - **Licence:** MIT · **Stars (2026-09-28):** ~4.8k · **Difficulty:** 🔴 Advanced
