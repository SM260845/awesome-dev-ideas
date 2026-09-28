# Project Inspiration

> **Scope:** Ambitious multi-week builds (platforms, engines, AI-native products, civic and science tools) worth a serious portfolio piece or a startup.

52 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Developer platforms](#developer-platforms)
- [AI-native products](#ai-native-products)
- [Infrastructure & systems](#infrastructure--systems)
- [Collaboration & productivity](#collaboration--productivity)
- [Open data & civic](#open-data--civic)
- [Creative & media platforms](#creative--media-platforms)
- [Education & science](#education--science)
- [Hardware-software systems](#hardware-software-systems)

## Developer platforms

- **Self-Hosted Forge with Built-In Agents**: A lightweight git forge where issues can be assigned to sandboxed agents that open PRs, with full audit trails.
  - **Why:** Teams want agent workflows without sending code to third-party platforms.
  - **Stack:** Go, Forgejo-style architecture, containers, OIDC · **Difficulty:** 🔴 Advanced · **Prior art:** [go-gitea/gitea](https://github.com/go-gitea/gitea)

- **Personal PaaS on One Server**: Push-to-deploy for apps and databases on a single VPS with backups, TLS and preview environments.
  - **Why:** Indie developers want Heroku ergonomics at VPS prices.
  - **Stack:** Go, Docker, Caddy, SQLite · **Difficulty:** 🔴 Advanced · **Prior art:** [coollabsio/coolify](https://github.com/coollabsio/coolify)

- **Code Search Engine for Your Org**: Fast regex and symbol search across all repos with cross-references and history.
  - **Why:** Grep across hundreds of repos doesn't scale.
  - **Stack:** Rust or Go, trigram index, tree-sitter · **Difficulty:** 🔴 Advanced · **Prior art:** [sourcegraph/zoekt](https://github.com/sourcegraph/zoekt)

- **Internal Developer Portal Lite**: Service catalogue, ownership, docs and scorecards generated from repo metadata files.
  - **Why:** Backstage is powerful but heavy for small orgs.
  - **Stack:** TypeScript, YAML catalog files, static site · **Difficulty:** 🟡 Intermediate · **Prior art:** [backstage/backstage](https://github.com/backstage/backstage)

- **Classroom Coding Environments**: Browser IDE workspaces per student with starter code, autograding and teacher view of progress.
  - **Why:** Teachers lose lessons to setup problems on student machines.
  - **Stack:** code-server, containers, autograder scripts · **Difficulty:** 🔴 Advanced · **Prior art:** [coder/code-server](https://github.com/coder/code-server)

- **CI Runner on Spare Hardware**: Run CI jobs on your own idle machines with isolation, caching and a queue dashboard.
  - **Why:** Hosted CI minutes get expensive for heavy builds.
  - **Stack:** Go, Firecracker or containers, GitHub runner API · **Difficulty:** 🔴 Advanced

- **Realtime Sync Backend as a Library**: Embeddable server for rooms, presence and authoritative state sync that any web app or game can use.
  - **Why:** Realtime features get rebuilt from scratch for every product.
  - **Stack:** TypeScript or Rust, WebSockets, CRDT or authoritative state · **Difficulty:** 🔴 Advanced · **Prior art:** [colyseus/colyseus](https://github.com/colyseus/colyseus)

## AI-native products

- **Research Agent with Source Grading**: An agent that researches a question, grades each source's reliability and outputs a cited report with confidence levels.
  - **Why:** Most research agents treat every web page as equally trustworthy.
  - **Stack:** Python, search APIs, LLM, citation checker · **Difficulty:** 🔴 Advanced

- **Codebase Migration Agent**: Agent that migrates a codebase between frameworks module by module, keeping tests green at every step.
  - **Why:** Large migrations are among the most expensive engineering projects.
  - **Stack:** Python, agent harness, test runner, git · **Difficulty:** 🔴 Advanced

- **AI Pair for Data Notebooks**: Notebook assistant that proposes analyses, runs them in a sandbox and explains results with charts.
  - **Why:** Analysts spend time on boilerplate, not questions.
  - **Stack:** Python, Jupyter or marimo, sandbox kernel · **Difficulty:** 🔴 Advanced · **Prior art:** [marimo-team/marimo](https://github.com/marimo-team/marimo)

- **Voice-First Coding Companion**: Talk through a change while the assistant edits code, runs tests and reads back results.
  - **Why:** Accessibility and ergonomic benefits for developers with RSI.
  - **Stack:** Local STT/TTS, agent CLI, editor plugin · **Difficulty:** 🔴 Advanced

- **Multi-Agent Game Master**: Tabletop RPG game master with persistent world state, rules enforcement and several NPC agents.
  - **Why:** A demanding, fun test bed for agent memory and planning.
  - **Stack:** Python, SQLite world model, LLM · **Difficulty:** 🟡 Intermediate

- **Personal Knowledge OS**: Ingest notes, email, bookmarks and files into a local graph with semantic search and daily briefings.
  - **Why:** People drown in scattered information across apps.
  - **Stack:** Rust or TypeScript, SQLite, local embeddings · **Difficulty:** 🔴 Advanced · **Prior art:** [logseq/logseq](https://github.com/logseq/logseq)

- **AI Video Explainer Studio**: Turn a script or document into a narrated explainer video with generated diagrams and captions.
  - **Why:** Educational video production is slow and expensive.
  - **Stack:** Python, HTML-to-video renderer, TTS · **Difficulty:** 🔴 Advanced · **Prior art:** [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

## Infrastructure & systems

- **Distributed SQLite Service**: Replicated SQLite with leader election, read replicas and simple HTTP API.
  - **Why:** A great systems project that teaches Raft and replication.
  - **Stack:** Go, Raft, SQLite · **Difficulty:** 🔴 Advanced · **Prior art:** [rqlite/rqlite](https://github.com/rqlite/rqlite)

- **Object Storage Server**: S3-compatible storage with erasure coding across disks and a web console.
  - **Why:** Deep project on storage, consistency and APIs.
  - **Stack:** Go or Rust, S3 API, erasure coding · **Difficulty:** 🔴 Advanced · **Prior art:** [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs)

- **Edge Function Runtime**: Run WebAssembly functions at the edge with cold starts under 5 ms and per-tenant limits.
  - **Why:** Explores isolation, scheduling and Wasm runtimes.
  - **Stack:** Rust, Wasmtime, HTTP · **Difficulty:** 🔴 Advanced · **Prior art:** [bytecodealliance/wasmtime](https://github.com/bytecodealliance/wasmtime)

- **Time-Series Database for IoT**: Compressed columnar storage for sensor data with downsampling and a query language.
  - **Why:** Specialised databases beat general ones for telemetry.
  - **Stack:** Rust, Gorilla compression, SQL subset · **Difficulty:** 🔴 Advanced

- **Service Mesh Visualiser**: Real-time map of service-to-service traffic from eBPF with latency and error overlays.
  - **Why:** Understanding microservice traffic without code changes.
  - **Stack:** Go, eBPF, WebGL graph · **Difficulty:** 🔴 Advanced · **Prior art:** [cilium/hubble](https://github.com/cilium/hubble)

- **Global Anycast DNS for Homelabs**: Authoritative DNS you run across a few cheap VPS locations with health-checked failover.
  - **Why:** Learn DNS, BGP concepts and high availability hands-on.
  - **Stack:** Go, CoreDNS plugins, VPS · **Difficulty:** 🔴 Advanced · **Prior art:** [coredns/coredns](https://github.com/coredns/coredns)

- **Log Search Engine**: Ingest logs, index them with compression and search with a simple query language.
  - **Why:** Commercial log platforms are costly at scale.
  - **Stack:** Rust, inverted index, object storage · **Difficulty:** 🔴 Advanced · **Prior art:** [quickwit-oss/quickwit](https://github.com/quickwit-oss/quickwit)

## Collaboration & productivity

- **Local-First Notion Alternative**: Blocks-based documents and databases that work offline and sync peer-to-peer.
  - **Why:** Users want ownership of their notes without losing collaboration.
  - **Stack:** TypeScript, CRDTs, SQLite, Tauri · **Difficulty:** 🔴 Advanced · **Prior art:** [AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)

- **Whiteboard with Code Execution**: Infinite canvas where code cells run and their outputs become diagram nodes.
  - **Why:** Bridges exploratory thinking and working code.
  - **Stack:** TypeScript, tldraw SDK, Pyodide · **Difficulty:** 🔴 Advanced · **Prior art:** [tldraw/tldraw](https://github.com/tldraw/tldraw)

- **Async Standup Tool with Git Context**: Standups generated from commits, PRs and calendar, edited by each person before posting.
  - **Why:** Meetings for status updates waste time.
  - **Stack:** Next.js, GitHub API, Slack API · **Difficulty:** 🟡 Intermediate

- **Open-Source Meeting Recorder**: Local meeting recorder with transcription, speaker labels and searchable archives, no bot joining the call.
  - **Why:** Privacy-conscious teams avoid cloud meeting bots.
  - **Stack:** Tauri, whisper.cpp, SQLite · **Difficulty:** 🔴 Advanced

- **Spreadsheet with Real Programming**: Spreadsheet where cells can hold Python, with dependency tracking and version control.
  - **Why:** Spreadsheets run businesses but lack testing and history.
  - **Stack:** Rust or TypeScript, Pyodide, CRDT · **Difficulty:** 🔴 Advanced · **Prior art:** [gristlabs/grist-core](https://github.com/gristlabs/grist-core)

- **Team Wiki that Tests Itself**: Wiki pages with embedded checks (links, commands, API examples) that flag stale content.
  - **Why:** Internal wikis rot within months.
  - **Stack:** TypeScript, Markdown, scheduled checks · **Difficulty:** 🟡 Intermediate

- **Private Registry Mirror with Policies**: Self-hosted npm/PyPI mirror that caches packages and enforces org policies (licences, age, known-bad versions).
  - **Why:** Orgs want faster installs and one place to enforce supply-chain rules.
  - **Stack:** Go or Node, registry protocols, policy engine · **Difficulty:** 🔴 Advanced · **Prior art:** [verdaccio/verdaccio](https://github.com/verdaccio/verdaccio)

- **Personal Finance Engine with Local Categorisation**: Import bank exports, categorise transactions with a local model and produce budgets and forecasts.
  - **Why:** Finance apps want your bank login; this keeps data on your machine.
  - **Stack:** TypeScript, SQLite, small local classifier · **Difficulty:** 🟡 Intermediate · **Prior art:** [actualbudget/actual](https://github.com/actualbudget/actual)

- **Federated Devlog Platform**: ActivityPub-native devlogs where project updates, releases and screenshots federate to Mastodon.
  - **Why:** Developers want an audience without a centralised platform.
  - **Stack:** Go or Elixir, ActivityPub, Markdown · **Difficulty:** 🔴 Advanced · **Prior art:** [mastodon/mastodon](https://github.com/mastodon/mastodon)

## Open data & civic

- **Public Transport Delay Tracker**: Archive real-time transit feeds and publish reliability stats per route and stop.
  - **Why:** Commuters and advocates need data to push for improvements.
  - **Stack:** Python, GTFS-RT, DuckDB, static site · **Difficulty:** 🟡 Intermediate

- **Government Spending Explorer**: Normalise public procurement data into a searchable, chartable site with supplier profiles.
  - **Why:** Transparency data is published but rarely usable.
  - **Stack:** Python, Postgres, Next.js · **Difficulty:** 🟡 Intermediate

- **Local News Archive Search**: Crawl and index local news sites into a full-text archive with entity pages.
  - **Why:** Local journalism disappears when sites shut down.
  - **Stack:** Python, Scrapy, Meilisearch · **Difficulty:** 🟡 Intermediate · **Prior art:** [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

- **Air Quality Map from Community Sensors**: Aggregate low-cost sensor data with calibration and anomaly detection on a live map.
  - **Why:** Official monitors are sparse; community data fills gaps.
  - **Stack:** Python, TimescaleDB, MapLibre · **Difficulty:** 🟡 Intermediate · **Prior art:** [maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js)

- **Legislation Diff Viewer**: Show how bills and laws change between versions like a code diff, with plain-English summaries.
  - **Why:** Legal changes are hard for citizens to follow.
  - **Stack:** Python, text diffing, web UI · **Difficulty:** 🟡 Intermediate

- **Open Dataset Catalogue with Previews**: Crawl open-data portals and provide unified search with schema previews and freshness.
  - **Why:** Finding the right dataset takes longer than analysing it.
  - **Stack:** Python, DCAT metadata, DuckDB · **Difficulty:** 🟡 Intermediate · **Prior art:** [ckan/ckan](https://github.com/ckan/ckan)

## Creative & media platforms

- **Self-Hosted Podcast Platform**: Host, publish and analyse podcasts with RSS, transcripts and chapter generation.
  - **Why:** Podcasters want ownership and privacy-friendly analytics.
  - **Stack:** Go, object storage, whisper · **Difficulty:** 🟡 Intermediate

- **Photo Library with Local AI Search**: Self-hosted photo library with face clustering and natural-language search, all local.
  - **Why:** Replace cloud photo services without losing smart search.
  - **Stack:** Go/Python, CLIP embeddings, Postgres · **Difficulty:** 🔴 Advanced · **Prior art:** [immich-app/immich](https://github.com/immich-app/immich)

- **Collaborative Music Sequencer in the Browser**: Multiplayer step sequencer with shared sessions, synths and export.
  - **Why:** Fun real-time collaboration and audio engineering project.
  - **Stack:** TypeScript, Web Audio, CRDTs · **Difficulty:** 🔴 Advanced · **Prior art:** [Tonejs/Tone.js](https://github.com/Tonejs/Tone.js)

- **Open Font Editor for the Web**: Browser-based font editor with variable font support and live preview.
  - **Why:** Font tools are expensive or desktop-only.
  - **Stack:** TypeScript, OpenType.js, Canvas · **Difficulty:** 🔴 Advanced · **Prior art:** [opentypejs/opentype.js](https://github.com/opentypejs/opentype.js)

- **Interactive Documentary Engine**: Framework for scroll-driven stories with maps, charts and media synced to narrative.
  - **Why:** Newsrooms rebuild these one-off for every story.
  - **Stack:** TypeScript, Scrollama, D3, MapLibre · **Difficulty:** 🟡 Intermediate · **Prior art:** [russellsamora/scrollama](https://github.com/russellsamora/scrollama)

## Education & science

- **Interactive Algorithm Textbook**: Explanations with live, steppable visualisations and editable code for each algorithm.
  - **Why:** Algorithms click when you can see and tweak them.
  - **Stack:** TypeScript, Svelte, Pyodide · **Difficulty:** 🟡 Intermediate

- **Open Lab Notebook**: Versioned, reproducible lab notebook linking protocols, data files and results.
  - **Why:** Research reproducibility suffers from scattered records.
  - **Stack:** Python, git-backed storage, web UI · **Difficulty:** 🟡 Intermediate

- **Browser-Based Circuit Simulator**: Draw digital or analog circuits and simulate them in real time with oscilloscope views.
  - **Why:** Useful for students without lab access.
  - **Stack:** TypeScript, SPICE-like solver, Canvas · **Difficulty:** 🔴 Advanced

- **Language Learning from Your Media**: Turn subtitles from shows you watch into spaced-repetition decks with audio clips.
  - **Why:** Learning with content you enjoy improves retention.
  - **Stack:** Python, subtitle parsing, Anki export · **Difficulty:** 🟡 Intermediate · **Prior art:** [ankitects/anki](https://github.com/ankitects/anki)

- **Citizen Science Image Labeller**: Platform for volunteers to label images with consensus, quality scoring and model-assisted pre-labels.
  - **Why:** Research projects need labelled data at scale.
  - **Stack:** Python, Label Studio, Postgres · **Difficulty:** 🟡 Intermediate · **Prior art:** [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio)

## Hardware-software systems

- **Open Smart Home Hub with Local Voice**: Hub combining device control, automations and fully local voice commands.
  - **Why:** Cloud smart speakers raise privacy and reliability concerns.
  - **Stack:** Python, Home Assistant, Wyoming protocol · **Difficulty:** 🔴 Advanced · **Prior art:** [home-assistant/core](https://github.com/home-assistant/core)

- **Robot Arm Controller with Vision**: Pick-and-place with a cheap robot arm, camera calibration and a web control panel.
  - **Why:** Hands-on robotics that combines vision, kinematics and UI.
  - **Stack:** Python, OpenCV, ROS 2 · **Difficulty:** 🔴 Advanced · **Prior art:** [ros2/ros2](https://github.com/ros2/ros2)

- **Drone Mapping Pipeline**: Turn drone photos into orthomosaics and 3D models with a job queue and viewer.
  - **Why:** Mapping software is expensive; open pipelines exist but need packaging.
  - **Stack:** Python, OpenDroneMap, web viewer · **Difficulty:** 🔴 Advanced · **Prior art:** [OpenDroneMap/ODM](https://github.com/OpenDroneMap/ODM)

- **Mesh Network Messenger**: Off-grid text messaging over LoRa radios with a phone app and message relay.
  - **Why:** Disaster preparedness and outdoor communication.
  - **Stack:** C++, Meshtastic firmware, mobile app · **Difficulty:** 🔴 Advanced · **Prior art:** [meshtastic/firmware](https://github.com/meshtastic/firmware)

- **E-Ink Dashboard Platform**: Configurable low-power e-ink displays showing calendars, weather and custom data from plugins.
  - **Why:** Always-on information without screens that glow.
  - **Stack:** ESP32, Python server rendering, e-ink · **Difficulty:** 🟡 Intermediate

- **Offline Knowledge Box with Voice**: One installer bundling offline Wikipedia, maps and manuals, the best local model the machine can run, and voice Q&A over the library.
  - **Why:** Preparedness, remote work and privacy all want knowledge that works without internet.
  - **Stack:** Kiwix ZIM files, llama.cpp, whisper.cpp, Docker · **Difficulty:** 🔴 Advanced · **Prior art:** [kiwix/kiwix-tools](https://github.com/kiwix/kiwix-tools)
