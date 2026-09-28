# Learning Projects: Beginner to Advanced

> **Scope:** Classic builds with a twist, grouped by level, each chosen to teach a specific concept.

52 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Beginner](#beginner)
- [Intermediate](#intermediate)
- [Advanced](#advanced)

## Beginner

- **Todo App with Offline Sync and Conflict UI**: The classic todo list, but it works offline and shows a conflict screen when two devices edit the same item.
  - **Why:** Teaches local storage, sync and conflict resolution early.
  - **Stack:** TypeScript, IndexedDB, small sync server · **Difficulty:** 🟢 Beginner

- **Weather CLI with Caching and Rate Limits**: Weather lookup in the terminal that caches responses and respects API limits.
  - **Why:** Teaches HTTP, JSON, caching and error handling.
  - **Stack:** Python or Go, Open-Meteo API · **Difficulty:** 🟢 Beginner · **Prior art:** [open-meteo/open-meteo](https://github.com/open-meteo/open-meteo)

- **URL Shortener with Click Analytics**: Shorten links and show clicks by day, country and referrer.
  - **Why:** Covers databases, redirects and basic analytics.
  - **Stack:** Node or Python, SQLite · **Difficulty:** 🟢 Beginner · **Prior art:** [shlinkio/shlink](https://github.com/shlinkio/shlink)

- **Markdown Blog Generator**: Static site generator that turns Markdown into a blog with tags and RSS.
  - **Why:** Teaches file I/O, templating and build pipelines.
  - **Stack:** Python or Go, templating library · **Difficulty:** 🟢 Beginner

- **Password Generator with Strength Meter**: Generate passphrases and explain their entropy visually.
  - **Why:** Teaches randomness, entropy and UI feedback.
  - **Stack:** TypeScript, zxcvbn-style estimation · **Difficulty:** 🟢 Beginner · **Prior art:** [dropbox/zxcvbn](https://github.com/dropbox/zxcvbn)

- **Habit Tracker with Streak Heatmap**: Track habits and render a GitHub-style contribution heatmap.
  - **Why:** Teaches dates, data modelling and SVG.
  - **Stack:** TypeScript, SVG, localStorage · **Difficulty:** 🟢 Beginner

- **Expense Splitter for Trips**: Split shared costs and compute the fewest payments to settle up.
  - **Why:** Introduces a neat graph-simplification algorithm.
  - **Stack:** Any language, simple web UI · **Difficulty:** 🟢 Beginner

- **Quiz App from Open Trivia Data**: Timed quiz with categories, scores and a leaderboard.
  - **Why:** Teaches API consumption, state and timers.
  - **Stack:** JavaScript, Open Trivia DB API · **Difficulty:** 🟢 Beginner

- **File Organiser Script**: Sort a folder by file type and date with a dry-run mode and undo log.
  - **Why:** Teaches the file system safely with dry runs and undo.
  - **Stack:** Python, pathlib · **Difficulty:** 🟢 Beginner

- **Pomodoro Timer as a Desktop App**: Timer with notifications and session stats packaged for desktop.
  - **Why:** Teaches desktop packaging and notifications.
  - **Stack:** Tauri or Electron · **Difficulty:** 🟢 Beginner

- **Personal Portfolio with Project Case Studies**: Portfolio where each project page explains problem, approach and results, deployed with CI.
  - **Why:** The first project employers see; case studies beat screenshot grids.
  - **Stack:** Astro, Markdown, GitHub Pages · **Difficulty:** 🟢 Beginner · **Prior art:** [withastro/astro](https://github.com/withastro/astro)

- **Discord or Telegram Utility Bot**: Bot with commands for reminders, polls and dice rolls.
  - **Why:** Teaches event-driven programming and APIs.
  - **Stack:** Python or Node, bot library · **Difficulty:** 🟢 Beginner

- **Recipe Scaler and Unit Converter**: Scale recipes by servings and convert units correctly.
  - **Why:** Teaches parsing, fractions and unit handling.
  - **Stack:** Any language, web UI · **Difficulty:** 🟢 Beginner

- **Browser Extension: Focus Mode**: Block distracting sites during scheduled hours with a daily summary.
  - **Why:** Teaches extension APIs and storage.
  - **Stack:** TypeScript, WebExtensions API · **Difficulty:** 🟢 Beginner

- **Countdown and Event Page Generator**: Shareable countdown pages with time-zone handling and calendar links.
  - **Why:** Teaches time zones, a notoriously tricky topic.
  - **Stack:** TypeScript, Temporal API or date library · **Difficulty:** 🟢 Beginner

- **Image Resizer and Optimiser**: Batch-resize and compress images with before/after file sizes.
  - **Why:** Teaches image formats and batch processing.
  - **Stack:** Python Pillow or Sharp · **Difficulty:** 🟢 Beginner

- **Git Stats Visualiser for Your Repos**: Charts of your own commits by hour, weekday and language.
  - **Why:** Uses real data you care about.
  - **Stack:** Python, git log, matplotlib · **Difficulty:** 🟢 Beginner

- **Accessible Form Builder**: Build forms that pass accessibility checks, with labels, errors and keyboard support.
  - **Why:** Teaches accessibility fundamentals from day one.
  - **Stack:** HTML, TypeScript, axe-core · **Difficulty:** 🟢 Beginner

## Intermediate

- **Chat App with End-to-End Encryption**: Real-time chat where messages are encrypted client-side with key verification.
  - **Why:** Teaches WebSockets and applied cryptography.
  - **Stack:** TypeScript, WebSockets, libsodium · **Difficulty:** 🟡 Intermediate

- **Redis Clone**: In-memory key-value server speaking the Redis protocol with expiry and persistence.
  - **Why:** Teaches networking, protocols and data structures.
  - **Stack:** Go or Rust, TCP · **Difficulty:** 🟡 Intermediate · **Prior art:** [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)

- **HTTP Server from Scratch**: HTTP/1.1 server on raw sockets with routing, keep-alive and static files.
  - **Why:** Demystifies web frameworks.
  - **Stack:** Any systems language, sockets · **Difficulty:** 🟡 Intermediate

- **Search Engine for Your Notes**: Inverted index with BM25 ranking, snippets and typo tolerance.
  - **Why:** Teaches information retrieval fundamentals.
  - **Stack:** Python or Rust · **Difficulty:** 🟡 Intermediate

- **Git Implementation (Core Commands)**: Implement init, add, commit, log and checkout using git's object model.
  - **Why:** Understand the tool you use every day.
  - **Stack:** Python or Go, zlib, SHA-1 · **Difficulty:** 🟡 Intermediate

- **Event-Sourced Bank Ledger**: Double-entry ledger built on an append-only event log with projections and replay.
  - **Why:** Teaches event sourcing, invariants and why money needs integer maths.
  - **Stack:** Any backend language, Postgres or SQLite · **Difficulty:** 🟡 Intermediate

- **Real-Time Multiplayer Tic-Tac-Toe with Matchmaking**: Rooms, matchmaking, reconnection and spectators.
  - **Why:** Teaches realtime state and edge cases.
  - **Stack:** TypeScript, WebSockets · **Difficulty:** 🟡 Intermediate

- **Markdown Parser**: Parse CommonMark subset into HTML with a test suite from the spec.
  - **Why:** Teaches parsing and spec-driven testing.
  - **Stack:** Any language, CommonMark spec tests · **Difficulty:** 🟡 Intermediate · **Prior art:** [commonmark/commonmark-spec](https://github.com/commonmark/commonmark-spec)

- **Load Balancer**: Round-robin and least-connections balancer with health checks.
  - **Why:** Teaches networking and resilience.
  - **Stack:** Go, reverse proxy · **Difficulty:** 🟡 Intermediate

- **OAuth Login from Scratch**: Implement the authorisation code flow with PKCE against a real provider.
  - **Why:** Removes the mystery from "Sign in with...".
  - **Stack:** Any backend, OAuth 2.1 · **Difficulty:** 🟡 Intermediate

- **Terminal Text Editor**: A small editor with syntax highlighting, search and undo.
  - **Why:** Teaches terminal I/O and data structures like gap buffers.
  - **Stack:** C, Rust or Go · **Difficulty:** 🟡 Intermediate · **Prior art:** [antirez/kilo](https://github.com/antirez/kilo)

- **DNS Resolver**: Recursive resolver that queries root servers and caches answers.
  - **Why:** Teaches the protocol behind every request.
  - **Stack:** Go or Python, UDP · **Difficulty:** 🟡 Intermediate

- **Static Type Checker for a Tiny Language**: Type-check a small expression language with inference.
  - **Why:** Teaches type systems concretely.
  - **Stack:** OCaml, Rust or TypeScript · **Difficulty:** 🟡 Intermediate

- **Image Filters with SIMD or WebAssembly**: Implement blur, sharpen and edge detection, then speed them up with SIMD or Wasm.
  - **Why:** Teaches performance and low-level optimisation.
  - **Stack:** Rust, WebAssembly · **Difficulty:** 🟡 Intermediate

- **Spreadsheet Engine**: Cells with formulas, dependency tracking and cycle detection.
  - **Why:** Teaches graphs and incremental recomputation.
  - **Stack:** TypeScript · **Difficulty:** 🟡 Intermediate

- **Neural Network from Scratch**: Autograd engine and a small MLP trained on a toy dataset.
  - **Why:** Understand backpropagation by building it.
  - **Stack:** Python, NumPy · **Difficulty:** 🟡 Intermediate · **Prior art:** [karpathy/micrograd](https://github.com/karpathy/micrograd)

- **Tiny MCP Server**: Build an MCP server exposing one useful tool, with tests and a client demo.
  - **Why:** A practical 2026 skill: connecting tools to AI agents.
  - **Stack:** Python or TypeScript MCP SDK · **Difficulty:** 🟡 Intermediate · **Prior art:** [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

- **Unix Shell**: A shell with pipes, redirection, job control and history.
  - **Why:** Teaches processes, file descriptors and signals.
  - **Stack:** C, Rust or Go · **Difficulty:** 🟡 Intermediate

## Advanced

- **Database Storage Engine**: B-tree storage engine with a write-ahead log and crash recovery.
  - **Why:** Teaches how databases really work.
  - **Stack:** C, Rust or Go · **Difficulty:** 🔴 Advanced · **Prior art:** [cstack/db_tutorial](https://github.com/cstack/db_tutorial)

- **Compiler to WebAssembly**: Compile a small language to Wasm with a REPL in the browser.
  - **Why:** Teaches compilation end to end.
  - **Stack:** Rust or TypeScript, Wasm · **Difficulty:** 🔴 Advanced

- **Raft Consensus Implementation**: Implement Raft with leader election and log replication, tested with fault injection.
  - **Why:** Core distributed systems knowledge.
  - **Stack:** Go, deterministic simulation · **Difficulty:** 🔴 Advanced · **Prior art:** [etcd-io/raft](https://github.com/etcd-io/raft)

- **Operating System Kernel**: Boot a kernel with paging, processes and a simple shell.
  - **Why:** The deepest dive into how computers work.
  - **Stack:** C or Rust, QEMU · **Difficulty:** 🔴 Advanced · **Prior art:** [cfenollosa/os-tutorial](https://github.com/cfenollosa/os-tutorial)

- **Ray Tracer**: Path tracer with materials, BVH acceleration and multithreading.
  - **Why:** Teaches geometry, optimisation and parallelism.
  - **Stack:** C++ or Rust · **Difficulty:** 🔴 Advanced · **Prior art:** [RayTracing/raytracing.github.io](https://github.com/RayTracing/raytracing.github.io)

- **Train a Small Language Model**: Tokeniser, transformer and training loop for a tiny GPT on your own text.
  - **Why:** Understand the models you use every day.
  - **Stack:** Python, PyTorch · **Difficulty:** 🔴 Advanced · **Prior art:** [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

- **BitTorrent Client**: Download real torrents: parse metainfo, talk to trackers and peers.
  - **Why:** Teaches peer-to-peer protocols.
  - **Stack:** Go or Rust · **Difficulty:** 🔴 Advanced

- **Container Runtime**: Run processes in namespaces and cgroups with an image format.
  - **Why:** Understand what Docker actually does.
  - **Stack:** Go or Rust, Linux syscalls · **Difficulty:** 🔴 Advanced

- **Browser Rendering Engine**: Parse HTML and CSS, compute layout and paint to a canvas.
  - **Why:** Teaches the web platform from the inside.
  - **Stack:** Rust or Python · **Difficulty:** 🔴 Advanced

- **Coding Agent Harness from Scratch**: Minimal agent loop with tools (read, edit, run), context management and a test-driven stop condition.
  - **Why:** Understand what coding agents do under the hood.
  - **Stack:** Python or TypeScript, LLM API · **Difficulty:** 🔴 Advanced

- **Distributed Key-Value Store with Sharding**: Consistent hashing, replication and rebalancing across nodes.
  - **Why:** Teaches scaling storage.
  - **Stack:** Go, gRPC · **Difficulty:** 🔴 Advanced

- **Regex Engine**: Thompson NFA regex engine with benchmarks against backtracking.
  - **Why:** Classic computer science with a performance twist.
  - **Stack:** C, Rust or Go · **Difficulty:** 🔴 Advanced

- **Vector Database**: HNSW index with filtering, persistence and a query API.
  - **Why:** Understand the retrieval layer behind RAG.
  - **Stack:** Rust or Go · **Difficulty:** 🔴 Advanced

- **Game Boy Emulator**: Emulate the CPU, PPU and memory to run homebrew ROMs.
  - **Why:** Challenging, rewarding hardware emulation.
  - **Stack:** Rust or C++ · **Difficulty:** 🔴 Advanced

- **Stream Processing Engine**: Windowed aggregations with watermarks and exactly-once output.
  - **Why:** Teaches stream processing semantics.
  - **Stack:** Go or Rust · **Difficulty:** 🔴 Advanced

- **Git Server with Pack Protocol**: Serve clone and push over the smart HTTP protocol.
  - **Why:** Deep understanding of git transport.
  - **Stack:** Go · **Difficulty:** 🔴 Advanced
