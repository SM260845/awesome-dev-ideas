# Learning Projects: Beginner to Advanced

> **Scope:** Classic builds with a twist, grouped by level, each chosen to teach a specific concept.

112 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

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

- **Library Book Tracker with ISBN Lookup**: Type or scan an ISBN, fetch metadata from Open Library and track which friend borrowed which book.
  - **Why:** Teaches calling a public REST API, parsing JSON and basic CRUD on real data.
  - **Stack:** Python or JavaScript, Open Library API, SQLite · **Difficulty:** 🟢 Beginner

- **Flashcards with Spaced Repetition**: A flashcard app that schedules reviews with the SM-2 algorithm and shows today's due queue.
  - **Why:** Teaches implementing a small, well-documented algorithm plus date arithmetic.
  - **Stack:** Vanilla JavaScript, localStorage · **Difficulty:** 🟢 Beginner

- **Expression Calculator with a Test Suite**: A calculator that parses typed expressions with operator precedence and parentheses, written test-first.
  - **Why:** Teaches test-driven development and the shunting-yard algorithm at a friendly scale.
  - **Stack:** Python, pytest · **Difficulty:** 🟢 Beginner

- **Currency Converter with Cached Rates**: Converts between currencies using daily rates cached locally with a clear "rates as of" timestamp.
  - **Why:** Teaches caching, stale-data handling and why money needs decimals, not floats.
  - **Stack:** JavaScript, Frankfurter API, localStorage · **Difficulty:** 🟢 Beginner

- **Readability Analyser**: Paste text to get reading time, a Flesch reading-ease score and the longest sentences highlighted.
  - **Why:** Teaches string processing, regular expressions and applying simple formulas.
  - **Stack:** JavaScript or Python · **Difficulty:** 🟢 Beginner

- **Movie Watchlist with Debounced Search**: Search films through an open API, save a watchlist and mark titles watched with a rating.
  - **Why:** Teaches debounced input, keeping API keys out of code and managing list state.
  - **Stack:** React or Svelte, TMDB API · **Difficulty:** 🟢 Beginner

- **Tic-Tac-Toe with an Unbeatable Opponent**: The classic game with a minimax AI and an "easy mode" that makes deliberate mistakes.
  - **Why:** Teaches recursion and game-tree search on a board small enough to reason about.
  - **Stack:** JavaScript canvas or Python · **Difficulty:** 🟢 Beginner

- **Snake in the Terminal**: Snake rendered with curses, with speed levels and a persistent high-score file.
  - **Why:** Teaches the game loop, non-blocking keyboard input and file persistence.
  - **Stack:** Python curses · **Difficulty:** 🟢 Beginner

- **Morse Code Trainer with Audio**: Convert text to Morse, play it with the Web Audio API and decode your own tapped input.
  - **Why:** Teaches lookup tables, timing and basic audio synthesis.
  - **Stack:** JavaScript, Web Audio API · **Difficulty:** 🟢 Beginner

- **Quote Wall with Shareable Filters**: A static site that loads quotes from JSON, filters by author or tag and encodes filters in the URL.
  - **Why:** Teaches DOM manipulation, URL query parameters and free static hosting.
  - **Stack:** HTML, JavaScript, GitHub Pages · **Difficulty:** 🟢 Beginner

- **Tabletop Dice Roller with Probability Charts**: Parses dice notation like 3d6+2, rolls it and charts the full probability distribution.
  - **Why:** Teaches parsing a tiny grammar and basic probability.
  - **Stack:** Python or JavaScript · **Difficulty:** 🟢 Beginner

- **Contact Book CLI with vCard Export**: Add, search, edit and export contacts to vCard from the command line.
  - **Why:** Teaches argument parsing, file formats and simple fuzzy search.
  - **Stack:** Python, argparse, JSON · **Difficulty:** 🟢 Beginner

- **Colour Contrast Checker**: Pick foreground and background colours and see WCAG contrast ratios with pass/fail badges and fixes.
  - **Why:** Teaches colour maths and real accessibility rules.
  - **Stack:** JavaScript · **Difficulty:** 🟢 Beginner

- **Word Frequency Explorer for Classic Books**: Load a Project Gutenberg book and chart its most common words, excluding stop words.
  - **Why:** Teaches tokenising text, counting with dictionaries and plotting.
  - **Stack:** Python, collections, matplotlib · **Difficulty:** 🟢 Beginner

- **Stopwatch with Laps and CSV Export**: A precise stopwatch with laps, split times and CSV export that stays accurate in background tabs.
  - **Why:** Teaches timers and why setInterval drifts while timestamps don't.
  - **Stack:** JavaScript · **Difficulty:** 🟢 Beginner

- **Sudoku Solver with Step Animation**: Solve puzzles with backtracking and animate every guess and backtrack.
  - **Why:** Teaches backtracking and how to visualise algorithm state.
  - **Stack:** JavaScript canvas or Python pygame · **Difficulty:** 🟢 Beginner

- **Terminal RSS Reader**: Subscribe to feeds, list unread items and open links, with everything stored in SQLite.
  - **Why:** Teaches XML parsing, basic SQL and command-line UX.
  - **Stack:** Python, feedparser, SQLite · **Difficulty:** 🟢 Beginner

- **Birthday Reminder Emailer**: Reads a CSV of birthdays and emails you a reminder the day before, run by cron.
  - **Why:** Teaches scheduling, SMTP and date handling across year boundaries.
  - **Stack:** Python, smtplib, cron · **Difficulty:** 🟢 Beginner

- **Hangman with Word Categories**: Hangman with categories loaded from files, a hint system and ASCII-art stages.
  - **Why:** Teaches loops, string state and reading input files.
  - **Stack:** Python · **Difficulty:** 🟢 Beginner

- **QR Code Generator and Webcam Scanner**: Generate QR codes for text, Wi-Fi and contacts, then scan them back with the webcam.
  - **Why:** Teaches using third-party libraries, canvas and browser media devices.
  - **Stack:** JavaScript, qrcode library, getUserMedia · **Difficulty:** 🟢 Beginner

- **Memory Card Matching Game**: Flip-card game with a timer, move counter and a properly shuffled deck.
  - **Why:** Teaches event handling, Fisher-Yates shuffling and CSS transitions.
  - **Stack:** HTML, CSS, JavaScript · **Difficulty:** 🟢 Beginner

- **Static Photo Gallery Generator**: A script that turns a folder of photos into a static gallery with thumbnails and EXIF captions.
  - **Why:** Teaches file I/O, image processing and HTML templating.
  - **Stack:** Python, Pillow, Jinja2 · **Difficulty:** 🟢 Beginner

- **Keyboard Shortcut Trainer**: Quizzes you on shortcuts for an editor of your choice and repeats the ones you miss.
  - **Why:** Teaches keyboard events and a simple adaptive practice loop.
  - **Stack:** JavaScript · **Difficulty:** 🟢 Beginner

- **Rock Paper Scissors over the LAN**: Two players on the same network play through sockets using a tiny text protocol.
  - **Why:** Teaches sockets, client and server roles and message framing.
  - **Stack:** Python socket · **Difficulty:** 🟢 Beginner

- **Task API with Tests and OpenAPI Docs**: A small REST API for tasks with validation, tests and auto-generated interactive docs.
  - **Why:** Teaches HTTP verbs, status codes and documenting an API.
  - **Stack:** FastAPI, pytest · **Difficulty:** 🟢 Beginner · **Prior art:** [fastapi/fastapi](https://github.com/fastapi/fastapi)

- **Markdown Notes with Live Preview**: A split-pane editor that saves notes locally and renders sanitised Markdown as you type.
  - **Why:** Teaches input events, HTML sanitising and local storage.
  - **Stack:** JavaScript, marked, DOMPurify · **Difficulty:** 🟢 Beginner

- **Mad Libs Story Generator**: Fill-in-the-blank stories from templates with word-type prompts and shareable results.
  - **Why:** Teaches templates, string formatting and collecting user input.
  - **Stack:** Python or JavaScript · **Difficulty:** 🟢 Beginner

- **Weighted Grade Calculator**: Enter assignments with category weights and see your current grade and the score you need on the final.
  - **Why:** Teaches weighted averages, form handling and edge cases like missing marks.
  - **Stack:** JavaScript or Python · **Difficulty:** 🟢 Beginner

- **CV as a JSON API**: A JSON endpoint serving your CV plus a page that renders it and a print-ready PDF export.
  - **Why:** Teaches JSON schemas, rendering from data and print CSS.
  - **Stack:** Node.js, JSON Resume schema · **Difficulty:** 🟢 Beginner · **Prior art:** [jsonresume/jsonresume.org](https://github.com/jsonresume/jsonresume.org)

- **Minesweeper with Flood Fill**: Classic Minesweeper with a guaranteed-safe first click and recursive reveal of empty areas.
  - **Why:** Teaches 2D arrays, flood fill and game state.
  - **Stack:** JavaScript canvas · **Difficulty:** 🟢 Beginner

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

- **Redis-Backed Job Queue with Retries**: A background job queue with exponential backoff, a dead-letter list and a small status page.
  - **Why:** Teaches producer/consumer design and handling failures deliberately.
  - **Stack:** Python or Go, Redis · **Difficulty:** 🟡 Intermediate

- **Collaborative Text Editor with a Hand-Written CRDT**: Two browsers edit one document through a sequence CRDT you implement yourself.
  - **Why:** Teaches convergence, causality and why CRDTs work without a central lock.
  - **Stack:** TypeScript, WebSocket · **Difficulty:** 🟡 Intermediate

- **Static Site Generator with Incremental Builds**: Rebuild only the pages affected by a change, using a dependency graph and content hashes.
  - **Why:** Teaches caching, dependency tracking and file watching.
  - **Stack:** Go or Rust · **Difficulty:** 🟡 Intermediate

- **JSON Parser from Scratch**: A recursive-descent JSON parser with precise error messages, checked against a public conformance suite.
  - **Why:** Teaches lexing, parsing and good error reporting.
  - **Stack:** Any language, JSONTestSuite · **Difficulty:** 🟡 Intermediate · **Prior art:** [nst/JSONTestSuite](https://github.com/nst/JSONTestSuite)

- **Chess Engine with Alpha-Beta Search**: Move generation, alpha-beta search and the UCI protocol so it plugs into existing chess GUIs.
  - **Why:** Teaches search, pruning and implementing a real protocol.
  - **Stack:** C++, Rust or Go · **Difficulty:** 🟡 Intermediate

- **Polite Concurrent Web Crawler**: A crawler that respects robots.txt, rate-limits per host and deduplicates canonical URLs.
  - **Why:** Teaches concurrency, work queues and HTTP semantics.
  - **Stack:** Go or Python asyncio · **Difficulty:** 🟡 Intermediate

- **Bloom Filter and HyperLogLog Playground**: Implement both probabilistic structures and chart false-positive and error rates as they fill.
  - **Why:** Teaches hashing and trading accuracy for memory.
  - **Stack:** Python or JavaScript · **Difficulty:** 🟡 Intermediate

- **Lisp Interpreter with Tail Calls**: A REPL with closures, proper tail calls and a small standard library.
  - **Why:** Teaches environments, evaluation and recursion.
  - **Stack:** Python, Go or Rust · **Difficulty:** 🟡 Intermediate

- **Multi-Tenant Invoice App**: Invoices for several organisations with role-based access and PDF generation.
  - **Why:** Teaches tenancy boundaries, authorisation roles and document rendering.
  - **Stack:** Django or Laravel, Postgres · **Difficulty:** 🟡 Intermediate

- **Mandelbrot Explorer with Web Workers**: A zoomable fractal renderer that splits work across workers and refines progressively.
  - **Why:** Teaches parallelism in the browser and the limits of floating-point precision.
  - **Stack:** JavaScript, Web Workers, canvas · **Difficulty:** 🟡 Intermediate

- **Receive-Only SMTP Server**: A minimal SMTP server that accepts mail and shows messages in a web inbox.
  - **Why:** Teaches a line-based protocol, MIME parsing and state machines.
  - **Stack:** Go or Python · **Difficulty:** 🟡 Intermediate

- **Huffman File Compressor**: Compress and decompress files with Huffman coding and compare the results with gzip.
  - **Why:** Teaches trees, bit-level I/O and entropy.
  - **Stack:** C, Rust or Python · **Difficulty:** 🟡 Intermediate

- **Pathfinding Visualiser**: Draw walls on a grid and watch BFS, Dijkstra and A* explore it side by side.
  - **Why:** Teaches graph search and how heuristics change behaviour.
  - **Stack:** JavaScript canvas or React · **Difficulty:** 🟡 Intermediate

- **Link Preview Service with SSRF Defences**: Fetch a URL, extract Open Graph data, cache it and block requests to private networks.
  - **Why:** Teaches HTML parsing, caching and a real server-side security risk.
  - **Stack:** Node.js or Go · **Difficulty:** 🟡 Intermediate

- **Toy Package Manager Resolver**: Resolve semver ranges into a lockfile with backtracking and readable conflict messages.
  - **Why:** Teaches constraint solving and semantic versioning.
  - **Stack:** Python or Rust · **Difficulty:** 🟡 Intermediate

- **Diff Viewer on the Myers Algorithm**: Implement Myers diff and render side-by-side and inline views with word highlights.
  - **Why:** Teaches a classic algorithm and presenting its output well.
  - **Stack:** TypeScript · **Difficulty:** 🟡 Intermediate

- **System Metrics Exporter**: An agent that samples CPU, memory and disk and exposes a Prometheus endpoint, plus a dashboard.
  - **Why:** Teaches operating-system APIs, metric types and pull-based scraping.
  - **Stack:** Go, Prometheus, Grafana · **Difficulty:** 🟡 Intermediate

- **Time-Travel Debugger for a State Store**: Record every action and state in a Redux-style store, scrub a timeline and replay.
  - **Why:** Teaches immutability and event sourcing on the frontend.
  - **Stack:** TypeScript, React · **Difficulty:** 🟡 Intermediate

- **Delta File Sync with Rolling Checksums**: Sync two folders by sending only changed blocks, rsync-style.
  - **Why:** Teaches rolling hashes and bandwidth-efficient protocols.
  - **Stack:** Go or Rust · **Difficulty:** 🟡 Intermediate

- **Cron Daemon Clone**: Parse crontab lines, run jobs, capture output and catch up on runs missed during sleep.
  - **Why:** Teaches time maths, process management and persistence.
  - **Stack:** Go or Rust · **Difficulty:** 🟡 Intermediate

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

- **SQL Engine over CSV Files**: A parser, planner and iterator-based executor with joins and aggregates over plain CSV files.
  - **Why:** Teaches query planning and volcano-style execution.
  - **Stack:** Rust or Go · **Difficulty:** 🔴 Advanced

- **JIT Compiler for a Bytecode VM**: Build a stack VM for a small language, then JIT-compile hot loops to x86-64 or ARM64.
  - **Why:** Teaches bytecode design, machine code and calling conventions.
  - **Stack:** C or Rust · **Difficulty:** 🔴 Advanced

- **User-Space TCP/IP Stack**: Implement ARP, IPv4, ICMP and a basic TCP on top of a TAP device.
  - **Why:** Teaches networking from the wire up.
  - **Stack:** C or Rust, TUN/TAP · **Difficulty:** 🔴 Advanced

- **Garbage Collector for a Toy Runtime**: Start with mark-sweep, move to a generational collector and visualise the heap.
  - **Why:** Teaches memory management and collector trade-offs.
  - **Stack:** C or Rust · **Difficulty:** 🔴 Advanced

- **Adaptive Bitrate Video Server**: Transcode uploads into HLS renditions and serve a player that switches quality with bandwidth.
  - **Why:** Teaches codecs, segmenting and adaptive streaming.
  - **Stack:** FFmpeg, Go or Node.js, hls.js · **Difficulty:** 🔴 Advanced

- **Tensor Library with GPU Kernels**: A tensor library with reverse-mode autodiff and hand-written CUDA or Metal kernels.
  - **Why:** Teaches automatic differentiation and GPU programming together.
  - **Stack:** C++ and CUDA, or Rust and wgpu · **Difficulty:** 🔴 Advanced

- **Tiny Hypervisor on KVM**: Create a VM with the KVM API and boot a minimal kernel inside it.
  - **Why:** Teaches virtualisation, CPU modes and memory mapping.
  - **Stack:** C or Rust, Linux KVM · **Difficulty:** 🔴 Advanced

- **Rigid-Body Physics Engine**: Collision detection with GJK and EPA, contact constraints and a stable iterative solver.
  - **Why:** Teaches numerical integration and computational geometry.
  - **Stack:** C++ or Rust · **Difficulty:** 🔴 Advanced

- **Language Server for Your Own Language**: A full LSP with diagnostics, go-to-definition and completion for a toy language.
  - **Why:** Teaches incremental parsing and editor protocols.
  - **Stack:** Rust or TypeScript, tree-sitter · **Difficulty:** 🔴 Advanced

- **Software Rasteriser**: Draw textured triangles with a z-buffer and perspective-correct interpolation, no GPU APIs.
  - **Why:** Teaches the graphics pipeline from first principles.
  - **Stack:** C, C++ or Rust · **Difficulty:** 🔴 Advanced
