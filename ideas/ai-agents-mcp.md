# AI, Agents & MCP

> **Scope:** Agent harnesses, MCP servers, skills, memory, evals, local models and RAG. AI security lives in Security & Privacy.

74 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Harnesses & orchestration](#harnesses--orchestration)
- [MCP servers](#mcp-servers)
- [Skills & plugins](#skills--plugins)
- [Memory & context](#memory--context)
- [Evals & observability](#evals--observability)
- [Local models & inference](#local-models--inference)
- [RAG & documents](#rag--documents)

## Harnesses & orchestration

- **PlugPort**: Write an agent plugin once (skills, hooks, MCP servers, slash commands) and compile it to each harness's native format.
  - **Why:** Plugin authors want reach across Claude Code, Codex, Cursor and newer harnesses without maintaining N copies.
  - **Stack:** TypeScript CLI, JSON Schema, GitHub Action for publishing · **Difficulty:** 🟡 Intermediate · **Prior art:** [anthropics/skills](https://github.com/anthropics/skills)

- **Harness Switchboard**: One config that launches the same task in several coding-agent CLIs and compares diffs, cost and time side by side.
  - **Why:** Teams picking a default agent need evidence on their own repos, not leaderboard numbers.
  - **Stack:** Go or Rust CLI, git worktrees, headless agent modes · **Difficulty:** 🟡 Intermediate · **Prior art:** [openai/codex](https://github.com/openai/codex)

- **Worktree Fleet**: Run N agents in parallel, each in its own git worktree and container, with a merge queue that rebases and tests winners.
  - **Why:** Parallel agents collide on the same checkout; isolation plus a merge queue makes fleets practical.
  - **Stack:** Go, git worktree, Docker, SQLite · **Difficulty:** 🔴 Advanced

- **Spec-to-Tasks Planner**: Turns a product spec into a dependency graph of agent-sized tasks with acceptance tests attached to each node.
  - **Why:** Agents fail on vague, oversized tasks; small tasks with tests raise completion rates.
  - **Stack:** Python, LLM structured output, NetworkX, Markdown export · **Difficulty:** 🟡 Intermediate

- **Agent Done-Checker**: A stop hook that verifies "done" claims by running tests, lint and a requirement checklist before the agent may finish.
  - **Why:** Premature "task complete" is one of the most common agent failure modes.
  - **Stack:** Hook scripts, pytest/vitest runners, small local classifier · **Difficulty:** 🟢 Beginner

- **Headless Agent Runner for CI**: Run a coding agent in CI on labelled issues and open a draft PR with logs, cost and a test report.
  - **Why:** Makes agent work reviewable and auditable instead of happening on laptops.
  - **Stack:** GitHub Actions, containers, agent CLI headless mode · **Difficulty:** 🟡 Intermediate · **Prior art:** [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action)

- **Cost Governor**: Per-task token and dollar budgets for agents, with soft warnings, hard stops and a daily report.
  - **Why:** Runaway agent loops burn money; finance wants caps per repo and per developer.
  - **Stack:** Proxy in Go, LiteLLM-compatible API, SQLite · **Difficulty:** 🟡 Intermediate · **Prior art:** [BerriAI/litellm](https://github.com/BerriAI/litellm)

- **Model Router by Task Type**: Route each agent step (plan, edit, summarise, classify) to the cheapest model that passes a local eval for that step.
  - **Why:** Most steps don't need a frontier model; routing cuts cost without losing quality.
  - **Stack:** Python, eval harness, OpenAI-compatible proxy · **Difficulty:** 🔴 Advanced

- **Agent Handoff Protocol Demo**: Two agents from different vendors cooperating on one task over A2A, with a visual message trace.
  - **Why:** Shows how cross-vendor agent protocols behave in practice and where they break.
  - **Stack:** Python, A2A SDK, web trace viewer · **Difficulty:** 🟡 Intermediate · **Prior art:** [a2aproject/A2A](https://github.com/a2aproject/A2A)

- **AGENTS.md Starter Generator**: Scans a repo and drafts agent instructions with build, test and style commands verified by actually running them.
  - **Why:** Most repos have no agent instructions, and hand-written ones often contain wrong commands.
  - **Stack:** Python, stack detection, command runner · **Difficulty:** 🟢 Beginner

- **Prompt Library with Version Pins**: Stores team prompts in git with versions, owners and the model each was tested on.
  - **Why:** Prompts get copy-pasted and silently drift between people.
  - **Stack:** Markdown, YAML frontmatter, small CLI · **Difficulty:** 🟢 Beginner

- **Agent Task Timeout Watchdog**: Kills or pauses agent runs that loop on the same tool call or exceed wall-clock limits, with a summary.
  - **Why:** Stuck agents waste hours and money overnight.
  - **Stack:** Python, process supervision, log parsing · **Difficulty:** 🟢 Beginner

## MCP servers

- **MCP Server Test Harness**: Record-and-replay tests for MCP servers: capture real sessions, then assert on tool schemas and outputs in CI.
  - **Why:** MCP servers break silently when upstream APIs change; there is little testing culture yet.
  - **Stack:** TypeScript, MCP SDK, Vitest, JSON snapshots · **Difficulty:** 🟡 Intermediate · **Prior art:** [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)

- **OpenAPI to MCP Generator**: Generate a curated MCP server from an OpenAPI spec, grouping endpoints into a few task-level tools.
  - **Why:** One-tool-per-endpoint servers flood the model's context; task-level tools work better.
  - **Stack:** TypeScript, OpenAPI parser, MCP SDK · **Difficulty:** 🟡 Intermediate

- **MCP Gateway with Per-Tool Policies**: A single MCP endpoint that fronts many servers and applies allow/deny, rate limits and redaction per tool.
  - **Why:** Enterprises want one audited entry point instead of dozens of local servers.
  - **Stack:** Go or TypeScript, MCP SDK, OPA policies · **Difficulty:** 🔴 Advanced

- **Postgres Read-Only Analyst MCP**: MCP server that exposes schema docs, safe read-only queries with row limits, and query explanations.
  - **Why:** Lets agents answer data questions without write access or runaway scans.
  - **Stack:** Python, psycopg, MCP SDK, EXPLAIN parsing · **Difficulty:** 🟡 Intermediate · **Prior art:** [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

- **Local Docs MCP**: Index the exact versions of your dependencies' docs locally and serve them to agents over MCP.
  - **Why:** Agents hallucinate APIs from older library versions; version-pinned docs fix that.
  - **Stack:** Python, lockfile parsers, SQLite FTS, MCP SDK · **Difficulty:** 🟡 Intermediate

- **Browser MCP with Session Recording**: MCP browser automation that records every agent action as a replayable trace with screenshots.
  - **Why:** Browser agents are hard to debug; replayable traces make failures reproducible.
  - **Stack:** TypeScript, Playwright, MCP SDK · **Difficulty:** 🟡 Intermediate · **Prior art:** [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

- **Calendar & Email Triage MCP**: A narrow MCP server for inbox and calendar with draft-only writes and human approval for sends.
  - **Why:** Personal-assistant agents need guardrails that make sending impossible without consent.
  - **Stack:** Python, Gmail/Graph APIs, MCP SDK · **Difficulty:** 🟡 Intermediate

- **MCP Registry Crawler**: Crawl public MCP servers, extract tool lists and auth needs, and publish a searchable static index.
  - **Why:** Discovery is fragmented across READMEs and marketplaces.
  - **Stack:** Python, GitHub API, static site · **Difficulty:** 🟢 Beginner

- **Terraform Plan Explainer MCP**: Serve `terraform plan` output to agents as structured changes with risk flags.
  - **Why:** Lets agents review infrastructure changes without parsing raw text.
  - **Stack:** Go, terraform-json, MCP SDK · **Difficulty:** 🟡 Intermediate

- **Kubernetes Read-Only MCP**: Namespaced, read-only cluster introspection for agents: events, logs, rollout status, resource diffs.
  - **Why:** On-call engineers want agent help without handing out cluster-admin.
  - **Stack:** Go, client-go, MCP SDK · **Difficulty:** 🟡 Intermediate

- **MCP Server Scaffolder**: `create-mcp-server` template with auth, tests, a Dockerfile and publishing to a registry baked in.
  - **Why:** Most MCP servers skip tests and packaging; a good template raises the floor.
  - **Stack:** TypeScript or Python template, GitHub Actions · **Difficulty:** 🟢 Beginner · **Prior art:** [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

- **RSS and Newsletter MCP**: An MCP server that exposes your feeds and newsletters as searchable, summarisable resources.
  - **Why:** Assistants can brief you from sources you already trust.
  - **Stack:** Python, MCP SDK, feedparser · **Difficulty:** 🟢 Beginner · **Prior art:** [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

- **Home Assistant Read-Only MCP**: Lets an assistant query sensor history and device states without permission to control anything.
  - **Why:** Useful questions about your home without the risk of unlocking doors.
  - **Stack:** Python, Home Assistant REST API, MCP SDK · **Difficulty:** 🟢 Beginner · **Prior art:** [home-assistant/core](https://github.com/home-assistant/core)

- **Spreadsheet MCP with Formula Awareness**: Exposes spreadsheets to agents with formulas, named ranges and cell provenance rather than flat values.
  - **Why:** Agents break spreadsheets when they only see computed values.
  - **Stack:** TypeScript, MCP SDK, xlsx parser · **Difficulty:** 🟡 Intermediate

- **Git History MCP**: Answers "when and why did this change" by exposing blame, log and PR links as MCP tools.
  - **Why:** Agents make better edits when they know the history behind code.
  - **Stack:** Go or TypeScript, git, MCP SDK · **Difficulty:** 🟢 Beginner

## Skills & plugins

- **SkillCI**: Run each agent skill against test prompts on several models, grade the output and publish a pass/fail badge.
  - **Why:** Thousands of skill repos have no quality signal; badges spread with every README.
  - **Stack:** Python, headless agent CLIs, LLM grader, GitHub Action · **Difficulty:** 🟡 Intermediate

- **Skill Linter**: Static checks for SKILL.md files: frontmatter, trigger clarity, broken references, oversized context.
  - **Why:** Cheap, fast feedback before running expensive behavioural tests.
  - **Stack:** TypeScript, remark, JSON Schema · **Difficulty:** 🟢 Beginner

- **Skill Recommender**: Watch a repo's stack and history and suggest which public skills to install, with reasons.
  - **Why:** Users don't know which of thousands of skills fit their project.
  - **Stack:** Python, embeddings, GitHub API · **Difficulty:** 🟡 Intermediate

- **Team Skill Registry**: Private registry for an org's skills with versioning, owners, usage stats and deprecation notices.
  - **Why:** Companies copy skills around in chat; nobody knows which version is current.
  - **Stack:** Next.js, Postgres, git-backed storage · **Difficulty:** 🟡 Intermediate

- **Skill from Session**: Turn a successful agent session into a reusable skill draft: steps, commands, pitfalls.
  - **Why:** Hard-won workflows get lost when the session ends.
  - **Stack:** Python, transcript parsers, LLM summarisation · **Difficulty:** 🟡 Intermediate

- **Domain Skill Packs**: Curated, tested skill packs for one domain (e.g. accessibility audits, database migrations, i18n).
  - **Why:** Deep, tested packs beat scattered one-off skills.
  - **Stack:** Markdown skills, scripts, SkillCI tests · **Difficulty:** 🟢 Beginner · **Prior art:** [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

- **Commit Message Skill**: A skill that writes commit messages following the repo's own conventions learned from history.
  - **Why:** Agent commits often ignore project conventions.
  - **Stack:** SKILL.md, git log examples · **Difficulty:** 🟢 Beginner

- **Accessibility Review Skill**: A skill that audits UI changes against WCAG checks and proposes concrete fixes.
  - **Why:** Accessibility is skipped when it needs a specialist.
  - **Stack:** SKILL.md, axe-core scripts · **Difficulty:** 🟢 Beginner · **Prior art:** [dequelabs/axe-core](https://github.com/dequelabs/axe-core)

- **Database Migration Safety Skill**: A skill that reviews migrations for locking, backfill and rollback risks before an agent applies them.
  - **Why:** Agents happily write migrations that lock production tables.
  - **Stack:** SKILL.md, SQL analysis scripts · **Difficulty:** 🟡 Intermediate

## Memory & context

- **MemPort**: Open format and CLI to export and import agent memory and rules between harnesses.
  - **Why:** People switch vendors often and lose accumulated context each time.
  - **Stack:** TypeScript CLI, JSON Schema, importers per harness · **Difficulty:** 🟡 Intermediate

- **Context Budget Visualiser**: Show what fills an agent's context window (system prompt, tools, files, history) per turn.
  - **Why:** Context bloat silently degrades quality and raises cost.
  - **Stack:** Web UI, transcript parsers, tokenizers · **Difficulty:** 🟢 Beginner

- **Repo Map Service**: Keep an always-fresh symbol map of a repo (tree-sitter) that agents query instead of grepping.
  - **Why:** Cuts tokens spent on navigation in large codebases.
  - **Stack:** Rust or Python, tree-sitter, SQLite · **Difficulty:** 🟡 Intermediate · **Prior art:** [Aider-AI/aider](https://github.com/Aider-AI/aider)

- **Decision Log for Agents**: Agents append architecture decisions and rejected approaches to a log that future sessions load.
  - **Why:** Stops agents from re-proposing ideas the team already rejected.
  - **Stack:** Markdown ADRs, hooks, retrieval · **Difficulty:** 🟢 Beginner

- **Compaction Quality Checker**: After context compaction, test whether key facts survived by quizzing the summary.
  - **Why:** Bad compaction causes agents to forget constraints mid-task.
  - **Stack:** Python, LLM-as-judge, fact extraction · **Difficulty:** 🟡 Intermediate

- **Memory Inspector UI**: Browse, edit and delete what an agent remembers about you, with the source of each memory.
  - **Why:** Users need to see and correct agent memory to trust it.
  - **Stack:** Web UI, memory store adapters · **Difficulty:** 🟢 Beginner · **Prior art:** [getzep/graphiti](https://github.com/getzep/graphiti)

- **Personal Memory Server**: Self-hosted memory API that any agent or chat app can read and write with user-controlled scopes.
  - **Why:** Keeps personal context portable and private instead of locked in one vendor.
  - **Stack:** Go or Python, Postgres + pgvector, OAuth · **Difficulty:** 🟡 Intermediate · **Prior art:** [mem0ai/mem0](https://github.com/mem0ai/mem0)

- **Project Glossary for Agents**: Maintains a glossary of domain terms and injects relevant entries into agent context automatically.
  - **Why:** Agents misuse domain vocabulary and invent wrong meanings.
  - **Stack:** Python, embeddings, Markdown glossary · **Difficulty:** 🟢 Beginner

- **Context File Linter**: Checks AGENTS.md and similar files for contradictions, stale commands and excessive length.
  - **Why:** Bloated or wrong context files silently degrade agent performance.
  - **Stack:** TypeScript, Markdown parser, command checks · **Difficulty:** 🟢 Beginner

- **Episodic Memory with Forgetting**: Agent memory that decays unimportant facts and consolidates repeated ones over time.
  - **Why:** Memory stores grow noisy and retrieve irrelevant old facts.
  - **Stack:** Python, SQLite, embeddings · **Difficulty:** 🔴 Advanced

## Evals & observability

- **Blackbox**: Cross-harness flight recorder: search, diff and replay agent sessions and export shareable session cards.
  - **Why:** Everyone running parallel agents loses track of what each one did.
  - **Stack:** Tauri or web UI, JSONL parsers, SQLite FTS · **Difficulty:** 🟡 Intermediate

- **Repo-Specific Agent Benchmark**: Mine your merged PRs into SWE-bench-style tasks to measure which agent/model works on your code.
  - **Why:** Public benchmarks don't predict performance on a private codebase.
  - **Stack:** Python, Docker, git history mining · **Difficulty:** 🔴 Advanced · **Prior art:** [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench)

- **Model Upgrade Canary**: When a provider ships a new model version, rerun your prompt and agent suite and report behaviour changes.
  - **Why:** Silent model updates change production behaviour overnight.
  - **Stack:** TypeScript or Python, YAML tests, scheduled CI · **Difficulty:** 🟢 Beginner · **Prior art:** [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)

- **Tool-Call Accuracy Dashboard**: Measure how often an agent picks the right tool with valid arguments, per tool and model.
  - **Why:** Pinpoints which tool descriptions confuse models.
  - **Stack:** Python, OpenTelemetry traces, Grafana · **Difficulty:** 🟡 Intermediate

- **LLM Trace Diff**: Diff two agent traces step by step to see where a new model or prompt diverged.
  - **Why:** Speeds up debugging of "it worked yesterday" regressions.
  - **Stack:** Web UI, OpenTelemetry GenAI conventions · **Difficulty:** 🟡 Intermediate · **Prior art:** [langfuse/langfuse](https://github.com/langfuse/langfuse)

- **Hallucinated Import Detector**: Flag generated code that imports packages or APIs that don't exist in the registry or your lockfile.
  - **Why:** Hallucinated packages waste time and invite slopsquatting.
  - **Stack:** Python, registry APIs, AST parsing · **Difficulty:** 🟢 Beginner

- **Eval Dataset from Support Tickets**: Turns resolved support tickets into evaluation cases for a support assistant.
  - **Why:** Real user questions make the best evals.
  - **Stack:** Python, helpdesk API, LLM labelling · **Difficulty:** 🟡 Intermediate

- **Voice Agent Latency Tester**: Measures per-turn latency of voice agents across speech detection, transcription, model and speech synthesis.
  - **Why:** Voice agents feel broken above a second of delay, and teams can't see where the time goes.
  - **Stack:** Python, WebRTC, recorded audio fixtures · **Difficulty:** 🟢 Beginner

- **Agent Cost per Merged PR**: Links agent spend to merged PRs to show real cost per shipped change.
  - **Why:** Token spend means little without outcomes attached.
  - **Stack:** Python, provider usage APIs, GitHub API · **Difficulty:** 🟡 Intermediate

- **Judge Agreement Analyzer**: Measures how often LLM judges agree with human graders and where they disagree.
  - **Why:** Uncalibrated LLM judges give false confidence.
  - **Stack:** Python, statistics, labelled samples · **Difficulty:** 🟡 Intermediate

## Local models & inference

- **Local Model Speed Database**: Crowd-sourced tokens-per-second results per hardware, model, quantisation and runtime.
  - **Why:** People need real speed numbers before downloading 40 GB models.
  - **Stack:** Python benchmark script, static site, JSON submissions · **Difficulty:** 🟡 Intermediate · **Prior art:** [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit)

- **Local Coding Autocomplete Stack**: One-command setup for private autocomplete using a small local code model and an editor plugin.
  - **Why:** Regulated teams can't send code to cloud APIs.
  - **Stack:** llama.cpp or Ollama, Continue, Docker · **Difficulty:** 🟢 Beginner · **Prior art:** [continuedev/continue](https://github.com/continuedev/continue)

- **Tiny Classifier Distiller**: Distil an expensive LLM classification prompt into a small local model with an eval report.
  - **Why:** Cuts per-call cost and latency for high-volume yes/no decisions.
  - **Stack:** Python, transformers, ONNX Runtime · **Difficulty:** 🔴 Advanced

- **Structured Output Benchmark**: Compare how reliably local models follow JSON schemas with and without constrained decoding.
  - **Why:** Agent pipelines break on malformed JSON; data helps pick models and decoders.
  - **Stack:** Python, llama.cpp grammars, Outlines · **Difficulty:** 🟡 Intermediate · **Prior art:** [dottxt-ai/outlines](https://github.com/dottxt-ai/outlines)

- **Offline Voice Assistant**: Push-to-talk assistant with local speech-to-text, a local LLM and local TTS, all on one laptop.
  - **Why:** Private, no-cloud voice control is a common but fiddly build.
  - **Stack:** whisper.cpp, llama.cpp, Piper or Kokoro · **Difficulty:** 🟡 Intermediate · **Prior art:** [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

- **LoRA Adapter Manager**: Hot-swap fine-tuned adapters per task on one base model with a simple routing API.
  - **Why:** Serving one model per task wastes GPU memory.
  - **Stack:** Python, vLLM or llama.cpp server · **Difficulty:** 🔴 Advanced · **Prior art:** [vllm-project/vllm](https://github.com/vllm-project/vllm)

- **Apple Silicon Fine-Tune Kit**: Scripts and recipes for LoRA fine-tuning small models on a Mac with eval before and after.
  - **Why:** Many developers have Macs but no GPU servers.
  - **Stack:** MLX, Python, Hugging Face datasets · **Difficulty:** 🟡 Intermediate · **Prior art:** [ml-explore/mlx-examples](https://github.com/ml-explore/mlx-examples)

- **Local Model Quantisation Comparer**: Runs the same prompts on several quantisations of a model and compares quality, speed and memory.
  - **Why:** Picking a quantisation is guesswork for most local users.
  - **Stack:** Python, llama.cpp, eval prompts · **Difficulty:** 🟡 Intermediate · **Prior art:** [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

- **Speculative Decoding Playground**: Pairs small draft models with larger targets locally and measures real speedups by task.
  - **Why:** Speculative decoding speedups vary widely by pairing and task.
  - **Stack:** Python, llama.cpp or vLLM · **Difficulty:** 🔴 Advanced

- **On-Device Embedding Server**: A tiny embedding service optimised for CPUs and NPUs with batching and caching.
  - **Why:** Local RAG needs fast embeddings without a GPU.
  - **Stack:** Rust, ONNX Runtime · **Difficulty:** 🔴 Advanced

## RAG & documents

- **Citation-First RAG**: RAG that only answers with quotes and page anchors, and refuses when no source supports the claim.
  - **Why:** Users in legal and research settings need verifiable answers.
  - **Stack:** Python, hybrid search, PDF anchors · **Difficulty:** 🟡 Intermediate

- **RAG Eval from Your Docs**: Auto-generate question/answer pairs from your corpus and score retrieval and answers over time.
  - **Why:** Most RAG systems ship without any retrieval metrics.
  - **Stack:** Python, Ragas, SQLite · **Difficulty:** 🟡 Intermediate · **Prior art:** [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas)

- **Document Parser Bake-off**: Run several PDF/Office parsers on your own documents and compare tables, headings and reading order.
  - **Why:** Parsing quality varies widely by document type and decides RAG quality.
  - **Stack:** Python, Docling, MarkItDown, diff viewer · **Difficulty:** 🟢 Beginner · **Prior art:** [docling-project/docling](https://github.com/docling-project/docling)

- **Codebase Q&A with Line Links**: Ask questions about a repo and get answers where every claim links to `file:line`.
  - **Why:** Onboarding and code review need grounded answers, not summaries.
  - **Stack:** Python, tree-sitter, embeddings, web UI · **Difficulty:** 🟡 Intermediate

- **Changelog-Aware Library Assistant**: Answers "how do I do X in version N" using release notes and migration guides as primary sources.
  - **Why:** Upgrades are where generic LLM answers fail most.
  - **Stack:** Python, GitHub Releases API, retrieval · **Difficulty:** 🟡 Intermediate

- **Meeting-to-Decisions Extractor**: Turn transcripts into decisions, owners and open questions linked to timestamps.
  - **Why:** Decisions get lost in hour-long recordings.
  - **Stack:** faster-whisper, LLM structured output, Markdown · **Difficulty:** 🟢 Beginner · **Prior art:** [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)

- **Table-Aware PDF Q&A**: Q&A over PDFs that keeps tables intact and answers numeric questions with cell citations.
  - **Why:** Flattened tables make RAG answers wrong for financial and scientific documents.
  - **Stack:** Python, Docling, DuckDB · **Difficulty:** 🟡 Intermediate

- **Multimodal Manual Assistant**: Answers questions about product manuals using both text and diagrams with page references.
  - **Why:** Manuals explain half their content in diagrams that text-only RAG ignores.
  - **Stack:** Python, vision-language model, vector store · **Difficulty:** 🔴 Advanced
