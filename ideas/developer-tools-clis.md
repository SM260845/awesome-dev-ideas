# Developer Tools & CLIs

> **Scope:** Tools developers run: CLIs, TUIs, editor extensions, local environments, API clients, profilers and build tooling.

92 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Terminal & shell](#terminal--shell)
- [Git & code review](#git--code-review)
- [Editors & IDE extensions](#editors--ide-extensions)
- [Local environments & containers](#local-environments--containers)
- [APIs & HTTP](#apis--http)
- [Performance & debugging](#performance--debugging)
- [Docs & knowledge tooling](#docs--knowledge-tooling)
- [Build & release](#build--release)

## Terminal & shell

- **Command Explainer TUI**: Paste any shell one-liner and get each flag and pipe stage explained, with a dry-run preview of affected files.
  - **Why:** Copy-pasted commands from docs and agents are a common source of damage.
  - **Stack:** Rust, tree-sitter-bash, man-page parsing, ratatui · **Difficulty:** 🟡 Intermediate · **Prior art:** [tldr-pages/tldr](https://github.com/tldr-pages/tldr)

- **Shell History to Script**: Pick commands from your history and export them as a documented, parameterised script.
  - **Why:** Ad-hoc command sequences become reusable automation instead of being lost.
  - **Stack:** Rust or Python, shell history parsers · **Difficulty:** 🟢 Beginner · **Prior art:** [atuinsh/atuin](https://github.com/atuinsh/atuin)

- **Project Command Palette**: Detect a repo's tasks (package scripts, Makefile, justfile, Taskfile) and show one fuzzy palette to run them.
  - **Why:** Every repo hides its commands in a different file.
  - **Stack:** Go, fzf-style UI, file parsers · **Difficulty:** 🟢 Beginner · **Prior art:** [casey/just](https://github.com/casey/just)

- **Log Tail Highlighter**: Tail logs with automatic JSON pretty-printing, level colours, field filters and time-gap markers.
  - **Why:** Raw JSON logs in a terminal are unreadable.
  - **Stack:** Rust or Go, streaming JSON parser · **Difficulty:** 🟢 Beginner

- **Port and Process Inspector**: `whoport 3000` shows which process, container or compose service holds a port, with a kill option.
  - **Why:** "Address already in use" costs minutes every time.
  - **Stack:** Go, lsof/netstat, Docker API · **Difficulty:** 🟢 Beginner

- **Dotfiles Doctor**: Audit dotfiles for slow shell startup, conflicting aliases and stale PATH entries, with timings per line.
  - **Why:** Shell startup creep goes unnoticed until it's seconds long.
  - **Stack:** Rust, shell tracing, report output · **Difficulty:** 🟢 Beginner

- **Terminal Session Recorder to GIF and Docs**: Record a terminal session and export a GIF plus a Markdown transcript with commands and outputs.
  - **Why:** Docs and bug reports need both visual and copyable versions.
  - **Stack:** Go, asciicast format, VHS-style renderer · **Difficulty:** 🟢 Beginner · **Prior art:** [charmbracelet/vhs](https://github.com/charmbracelet/vhs)

- **Clipboard Ring for the Terminal**: Keep a searchable history of copied text across terminal and GUI apps, with secret detection that skips passwords.
  - **Why:** Lost clipboard contents are a small but constant pain.
  - **Stack:** Rust, OS clipboard APIs, regex secret rules · **Difficulty:** 🟢 Beginner

- **Dev Cache Sweeper**: Find and reclaim space from node_modules, target dirs, virtualenvs, Docker layers and model caches, grouped by project age.
  - **Why:** Developer disks fill with gigabytes of forgotten build caches.
  - **Stack:** Rust, parallel directory walk, TUI · **Difficulty:** 🟢 Beginner

- **Cron Expression Workbench**: Type a cron expression and see the next runs in several time zones, plus conversion between cron dialects.
  - **Why:** Cron dialect and time-zone mistakes cause missed or doubled jobs.
  - **Stack:** TypeScript, web and CLI · **Difficulty:** 🟢 Beginner

- **Directory Notes CLI**: Attach short notes to any directory and see them when you cd in, like a sticky note for projects.
  - **Why:** You forget why a folder exists or what state you left it in.
  - **Stack:** Go or Rust, shell hook · **Difficulty:** 🟢 Beginner

- **Alias Suggester**: Watches your shell history and suggests aliases or functions for commands you type often.
  - **Why:** Most people never set up aliases despite repeating long commands daily.
  - **Stack:** Python or Go, shell history parser · **Difficulty:** 🟢 Beginner

- **Safe rm with Undo**: A drop-in rm replacement that moves files to a timed trash and supports `undo` for the last command.
  - **Why:** One mistyped rm can wipe hours of work.
  - **Stack:** Rust, XDG trash spec · **Difficulty:** 🟢 Beginner

- **SSH Config Manager TUI**: Browse, search, edit and test hosts in ~/.ssh/config with jump hosts shown as a tree.
  - **Why:** SSH configs grow into hundreds of hard-to-read lines.
  - **Stack:** Go, Bubble Tea · **Difficulty:** 🟢 Beginner · **Prior art:** [charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea)

- **JSON and YAML Path Explorer TUI**: Browse large JSON or YAML files as a collapsible tree and copy the path to any value.
  - **Why:** Finding the path to a deeply nested value is tedious with jq alone.
  - **Stack:** Rust, ratatui · **Difficulty:** 🟢 Beginner · **Prior art:** [ratatui/ratatui](https://github.com/ratatui/ratatui)

- **Env File Switcher**: Switch between named .env profiles per project with a diff of what changes.
  - **Why:** Juggling staging and local credentials by renaming files causes mistakes.
  - **Stack:** Go CLI · **Difficulty:** 🟢 Beginner

## Git & code review

- **Stacked PR CLI**: Create, rebase and submit stacks of dependent PRs with one command, keeping each branch small.
  - **Why:** Small reviews are faster, but managing stacks by hand is painful.
  - **Stack:** Go or Rust, git, GitHub API · **Difficulty:** 🔴 Advanced · **Prior art:** [jj-vcs/jj](https://github.com/jj-vcs/jj)

- **Refactor-Aware Diff Summary**: Summarise a PR as renamed symbols, moved code and real logic changes, so reviewers know where to focus.
  - **Why:** Refactors hide the few lines that actually change behaviour.
  - **Stack:** Rust, tree-sitter, git · **Difficulty:** 🔴 Advanced · **Prior art:** [Wilfred/difftastic](https://github.com/Wilfred/difftastic)

- **Git Blame Timeline**: Interactive view of how a single function evolved across commits, following renames and moves.
  - **Why:** Understanding why code looks the way it does needs history, not one blame line.
  - **Stack:** TypeScript web UI, git log -L, tree-sitter · **Difficulty:** 🟡 Intermediate

- **Commit Splitter**: Interactively split a large working-tree change into logical commits, with suggested groupings by file and hunk.
  - **Why:** Messy commits make review and bisect harder.
  - **Stack:** Go, git plumbing, TUI · **Difficulty:** 🟡 Intermediate · **Prior art:** [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)

- **Local PR Review TUI**: Review GitHub PRs in the terminal with inline comments, suggested changes and CI status.
  - **Why:** Keyboard-driven reviewers lose flow switching to the browser.
  - **Stack:** Go, Bubble Tea, GitHub GraphQL · **Difficulty:** 🟡 Intermediate · **Prior art:** [cli/cli](https://github.com/cli/cli)

- **Repo Snapshot Exporter**: Export a repo or subtree to a single token-counted text file for sharing with LLMs, respecting .gitignore.
  - **Why:** Useful for asking questions about code without an agent harness.
  - **Stack:** Rust or Python, tokenizer, glob rules · **Difficulty:** 🟢 Beginner

- **Hook Timing Report**: Profile a repo's pre-commit hooks and suggest which slow ones to move to CI.
  - **Why:** Slow hooks get skipped with --no-verify; fast hooks get used.
  - **Stack:** Go, git hooks, report output · **Difficulty:** 🟢 Beginner · **Prior art:** [evilmartians/lefthook](https://github.com/evilmartians/lefthook)

- **Branch Janitor**: List and delete merged or stale branches locally and on the remote, with a dry-run summary.
  - **Why:** Old branches clutter remotes and confuse teammates.
  - **Stack:** Go, git, GitHub API · **Difficulty:** 🟢 Beginner

- **Gitignore Generator from Project Scan**: Scans a project and builds a .gitignore from the languages and tools actually present.
  - **Why:** Copy-pasted gitignores miss tool-specific junk files.
  - **Stack:** Go, github/gitignore templates · **Difficulty:** 🟢 Beginner · **Prior art:** [github/gitignore](https://github.com/github/gitignore)

- **Git Undo Helper**: Describes what your last few git operations did and offers the exact command to undo each.
  - **Why:** Git's undo paths (reflog, reset, revert) confuse even experienced developers.
  - **Stack:** Rust, git reflog parsing · **Difficulty:** 🟢 Beginner

- **Large File Finder for Git History**: Lists the biggest blobs ever committed and which commits and paths introduced them.
  - **Why:** Bloated repos are slow to clone and nobody knows why.
  - **Stack:** Go, git cat-file batch mode · **Difficulty:** 🟢 Beginner

- **Co-Author Trailer Helper**: Adds Co-authored-by trailers from a team roster with fuzzy search.
  - **Why:** Pairing credit is lost because typing trailers is fiddly.
  - **Stack:** Shell script or Go, prepare-commit-msg hook · **Difficulty:** 🟢 Beginner

- **Review Checklist in the Terminal**: Generates a review checklist for a diff based on touched areas (migrations, auth, public API).
  - **Why:** Reviewers forget area-specific checks under time pressure.
  - **Stack:** Python, git diff, YAML rules · **Difficulty:** 🟡 Intermediate

- **Semantic Merge Driver for JSON and YAML**: A git merge driver that merges structured files by key instead of by line.
  - **Why:** Config and lockfile-like files conflict constantly on unrelated changes.
  - **Stack:** Rust, git merge driver interface · **Difficulty:** 🔴 Advanced

## Editors & IDE extensions

- **Test Impact Gutter**: Editor extension that shows which tests cover the line you're editing and runs just those on save.
  - **Why:** Faster feedback than running the whole suite.
  - **Stack:** VS Code API, coverage maps, LSP · **Difficulty:** 🟡 Intermediate

- **Error Lens for Logs**: Show recent production errors inline next to the code line that threw them.
  - **Why:** Connects runtime reality to source while you edit.
  - **Stack:** VS Code extension, Sentry or OTel API · **Difficulty:** 🟡 Intermediate

- **Codebase Tour Author**: Record guided tours through code (steps with notes) that live in the repo and play in the editor.
  - **Why:** Onboarding docs drift; tours tied to lines stay close to the code.
  - **Stack:** VS Code API, JSON tour files · **Difficulty:** 🟢 Beginner

- **Regex Workbench**: Build and test regexes against real files in your workspace with match highlighting and flavour conversion.
  - **Why:** Regex flavours differ across languages and tools.
  - **Stack:** TypeScript, VS Code webview · **Difficulty:** 🟢 Beginner

- **Structural Search and Replace Panel**: GUI for AST-based search and replace across a repo with preview and per-file approval.
  - **Why:** Safer large refactors than regex.
  - **Stack:** TypeScript, ast-grep bindings · **Difficulty:** 🟡 Intermediate · **Prior art:** [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep)

- **LSP for Config Files**: Language server for a popular config format your team uses (e.g. CI YAML) with schema validation and go-to-definition across includes.
  - **Why:** Config errors are only found after pushing.
  - **Stack:** Go or TypeScript, LSP, JSON Schema · **Difficulty:** 🟡 Intermediate

- **Env Var Hover**: Hover over `process.env.X` or `os.getenv` to see where it's defined across .env files, CI and deploy config.
  - **Why:** Missing or mismatched env vars cause "works on my machine".
  - **Stack:** VS Code extension, file indexing · **Difficulty:** 🟢 Beginner

- **TODO Highlighter with Issue Links**: Highlights TODOs in the editor and links them to issues when they include an ID.
  - **Why:** TODOs get forgotten when they aren't connected to tracked work.
  - **Stack:** VS Code extension, TypeScript · **Difficulty:** 🟢 Beginner

- **Paste as Code**: Pastes JSON as typed structs, curl commands as fetch calls or SQL rows as fixtures.
  - **Why:** Converting between formats by hand is repetitive and error-prone.
  - **Stack:** VS Code extension, TypeScript · **Difficulty:** 🟢 Beginner

- **Focus Mode for Diffs**: Dims everything in the editor except lines changed on the current branch.
  - **Why:** Easier to review your own work before pushing.
  - **Stack:** VS Code or Neovim plugin · **Difficulty:** 🟢 Beginner

- **Unit Test Jump**: Jump between a source file and its test file, creating the test file from a template if missing.
  - **Why:** Friction in creating tests means fewer tests.
  - **Stack:** Neovim plugin in Lua or VS Code extension · **Difficulty:** 🟢 Beginner

- **Inline Bundle Size Annotations**: Shows the minified and gzipped size of each import inline in the editor.
  - **Why:** Developers add heavy dependencies without noticing the cost.
  - **Stack:** VS Code extension, esbuild metafile · **Difficulty:** 🟡 Intermediate · **Prior art:** [evanw/esbuild](https://github.com/evanw/esbuild)

- **Live SQL Result Preview**: Run the SQL query under the cursor against a dev database and show results inline.
  - **Why:** Switching to a separate SQL client breaks flow.
  - **Stack:** VS Code extension, database drivers · **Difficulty:** 🟡 Intermediate

## Local environments & containers

- **Dev Environment Doctor**: `doctor` command that checks tool versions, env vars, ports and services against a repo's declared requirements.
  - **Why:** New contributors lose hours to setup issues.
  - **Stack:** Go, YAML spec, cross-platform checks · **Difficulty:** 🟢 Beginner · **Prior art:** [jdx/mise](https://github.com/jdx/mise)

- **Compose Graph Viewer**: Visualise a docker-compose file as a service graph with ports, volumes and health checks.
  - **Why:** Large compose files are hard to reason about.
  - **Stack:** TypeScript, YAML parser, Mermaid · **Difficulty:** 🟢 Beginner

- **Ephemeral Preview Environments on One VM**: Spin up a preview per branch on a single cheap VM with automatic subdomains and TTL cleanup.
  - **Why:** Managed preview platforms get expensive for small teams.
  - **Stack:** Go, Docker, Caddy, GitHub webhooks · **Difficulty:** 🟡 Intermediate · **Prior art:** [caddyserver/caddy](https://github.com/caddyserver/caddy)

- **Reproducible Dev Shell Generator**: Generate a Nix or devbox config from an existing repo's lockfiles and tool versions.
  - **Why:** Declarative environments without learning Nix from scratch.
  - **Stack:** Python, lockfile parsers, Nix · **Difficulty:** 🟡 Intermediate · **Prior art:** [jetify-com/devbox](https://github.com/jetify-com/devbox)

- **Local Cloud Mocks Dashboard**: Web UI over local AWS emulators showing queues, buckets and events in real time.
  - **Why:** Debugging local serverless flows is opaque.
  - **Stack:** TypeScript, LocalStack APIs · **Difficulty:** 🟡 Intermediate

- **Container Image Slimmer Report**: Analyse an image layer by layer and suggest concrete Dockerfile changes to cut size.
  - **Why:** Smaller images deploy faster and have fewer CVEs.
  - **Stack:** Go, image layer parsing · **Difficulty:** 🟡 Intermediate · **Prior art:** [wagoodman/dive](https://github.com/wagoodman/dive)

- **Seed Data Generator from Schema**: Generate realistic, referentially valid seed data from a live database schema.
  - **Why:** Empty local databases hide bugs and slow UI work.
  - **Stack:** Python, SQLAlchemy reflection, Faker · **Difficulty:** 🟡 Intermediate

- **Port Registry for Local Projects**: Assigns and remembers unique local ports per project so dev servers never collide.
  - **Why:** Every project defaults to port 3000 or 8080.
  - **Stack:** Go CLI, config file, shell integration · **Difficulty:** 🟢 Beginner

- **Docker Compose Profile Picker**: Interactive picker for Compose profiles and services with startup order shown.
  - **Why:** Big Compose files make it hard to run just what you need.
  - **Stack:** Go, Compose file parser · **Difficulty:** 🟡 Intermediate

- **Local HTTPS for Dev Domains**: One command gives each project a trusted local HTTPS domain like app.test.
  - **Why:** OAuth and secure cookies need HTTPS locally; setup is fiddly.
  - **Stack:** Go, mkcert-style local CA, DNS resolver · **Difficulty:** 🟡 Intermediate · **Prior art:** [FiloSottile/mkcert](https://github.com/FiloSottile/mkcert)

- **Devcontainer Linter**: Checks devcontainer.json for slow setups, missing features and unpinned images.
  - **Why:** Slow or broken dev containers waste everyone's first day.
  - **Stack:** TypeScript, JSON schema · **Difficulty:** 🟡 Intermediate

- **Container Resource Usage Recorder**: Records CPU and memory per container during a test run and flags hungry services.
  - **Why:** Local stacks become too heavy for laptops without anyone noticing.
  - **Stack:** Go, Docker stats API · **Difficulty:** 🟡 Intermediate

- **Offline Package Cache Proxy**: A local caching proxy for npm, PyPI and crates so installs work offline and on planes.
  - **Why:** Repeated downloads waste time and fail without internet.
  - **Stack:** Go, registry protocols · **Difficulty:** 🔴 Advanced

## APIs & HTTP

- **API Request Collections as Plain Files**: HTTP client that stores requests as readable text files in the repo, runnable from CLI and editor.
  - **Why:** Postman collections are opaque blobs that don't diff or review well.
  - **Stack:** Rust or Go, .http file format · **Difficulty:** 🟡 Intermediate · **Prior art:** [usebruno/bruno](https://github.com/usebruno/bruno)

- **Webhook Inspector**: Local endpoint that captures webhooks, lets you replay them with edits and forwards to localhost.
  - **Why:** Testing webhook integrations without deploying is fiddly.
  - **Stack:** Go, SQLite, web UI · **Difficulty:** 🟢 Beginner

- **API Changelog from Spec Diffs**: Turn OpenAPI diffs between releases into a readable API changelog with client migration notes.
  - **Why:** API consumers need to know what changed without reading specs.
  - **Stack:** Go or TypeScript, oasdiff output, Markdown · **Difficulty:** 🟡 Intermediate · **Prior art:** [oasdiff/oasdiff](https://github.com/oasdiff/oasdiff)

- **gRPC Explorer TUI**: Browse services via reflection, build requests from protobuf schemas and save them as scripts.
  - **Why:** gRPC debugging lacks curl-level ergonomics.
  - **Stack:** Go, grpcurl libraries, Bubble Tea · **Difficulty:** 🟡 Intermediate · **Prior art:** [fullstorydev/grpcurl](https://github.com/fullstorydev/grpcurl)

- **Mock Server from Traffic**: Record real API traffic and generate a mock server with matching responses and latencies.
  - **Why:** Frontend and integration work stalls when a backend is unavailable.
  - **Stack:** TypeScript, HAR parsing, MSW · **Difficulty:** 🟡 Intermediate · **Prior art:** [mswjs/msw](https://github.com/mswjs/msw)

- **curl Command Beautifier**: Formats long curl commands into readable multi-line form and converts them to HTTPie or code.
  - **Why:** Copied curl commands from browser dev tools are unreadable walls of text.
  - **Stack:** Rust or JavaScript CLI · **Difficulty:** 🟢 Beginner

- **OpenAPI Spec Linter with Fix Suggestions**: Lints OpenAPI specs for naming, pagination and error conventions with auto-fixes.
  - **Why:** Inconsistent APIs are hard to use and hard to fix later.
  - **Stack:** TypeScript, Spectral rules · **Difficulty:** 🟡 Intermediate · **Prior art:** [stoplightio/spectral](https://github.com/stoplightio/spectral)

- **HTTP Load Replay from HAR Files**: Replay a browser HAR recording as a load test with concurrency and timing controls.
  - **Why:** Real user flows make better load tests than synthetic ones.
  - **Stack:** Go, HAR parser · **Difficulty:** 🟡 Intermediate

- **JWT Inspector CLI**: Decodes JWTs, verifies signatures against a JWKS URL and explains expiry and claims.
  - **Why:** Pasting tokens into websites is a security risk.
  - **Stack:** Rust or Go CLI · **Difficulty:** 🟢 Beginner

## Performance & debugging

- **Benchmark Diff Bot**: Run benchmarks on base and head commits locally and print a significance-tested comparison.
  - **Why:** Noise makes naive benchmark comparisons misleading.
  - **Stack:** Rust, statistical tests, hyperfine-style runner · **Difficulty:** 🟡 Intermediate · **Prior art:** [sharkdp/hyperfine](https://github.com/sharkdp/hyperfine)

- **Flamegraph in One Command**: Profile any process or test and open an interactive flamegraph, auto-detecting language runtime.
  - **Why:** Profiling setup differs per language and scares people off.
  - **Stack:** Rust, perf, py-spy, pprof · **Difficulty:** 🟡 Intermediate · **Prior art:** [brendangregg/FlameGraph](https://github.com/brendangregg/FlameGraph)

- **Memory Leak Bisect**: Automatically bisect commits by measured memory growth of a test scenario.
  - **Why:** Leaks are hard to attribute to a specific change.
  - **Stack:** Python, git bisect run, psutil · **Difficulty:** 🟡 Intermediate

- **SQL Query Plan Visualiser**: Paste EXPLAIN output (Postgres/MySQL/SQLite) and see a readable tree with hotspots highlighted.
  - **Why:** Raw plans are hard to read under pressure.
  - **Stack:** TypeScript, web UI · **Difficulty:** 🟢 Beginner

- **Startup Time Profiler**: Measure and break down cold-start time of CLIs and Node/Python apps by module import.
  - **Why:** Slow startup is a top complaint for CLIs and serverless.
  - **Stack:** Python/Node import hooks, flame chart · **Difficulty:** 🟢 Beginner

- **Network Waterfall for CLI Apps**: Capture HTTP calls a CLI or backend makes and show a browser-style waterfall.
  - **Why:** Hidden sequential calls cause most "why is it slow" issues.
  - **Stack:** Go, proxy, HAR output · **Difficulty:** 🟡 Intermediate · **Prior art:** [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

- **Slow Test Finder**: Reports the slowest tests and setup fixtures across runs with a trend over time.
  - **Why:** Test suites slow down gradually and nobody knows which test to fix.
  - **Stack:** Python or Node.js, JUnit XML parser · **Difficulty:** 🟢 Beginner

- **Syscall Tracer Summary**: Wraps strace or dtruss and summarises file, network and process activity in plain language.
  - **Why:** Raw syscall traces are overwhelming for most developers.
  - **Stack:** Rust, strace output parser · **Difficulty:** 🟡 Intermediate

- **Continuous Profiler for Local Dev**: Always-on low-overhead profiling for local dev servers with a timeline to spot slow requests.
  - **Why:** Performance regressions are cheapest to catch before they ship.
  - **Stack:** eBPF or language profilers, web UI · **Difficulty:** 🔴 Advanced · **Prior art:** [grafana/pyroscope](https://github.com/grafana/pyroscope)

- **Deadlock Detector for Async Code**: Detects stuck async tasks and prints what each is waiting on.
  - **Why:** Async deadlocks are silent and hard to reproduce.
  - **Stack:** Rust tokio-console style or Python asyncio debug hooks · **Difficulty:** 🔴 Advanced

## Docs & knowledge tooling

- **Man Page Generator from --help**: Turn a CLI's help output and flags into man pages, Markdown docs and shell completions.
  - **Why:** Many CLIs ship without man pages or completions.
  - **Stack:** Go, parser for common help formats · **Difficulty:** 🟢 Beginner

- **Runbook Runner**: Markdown runbooks with executable code blocks, recorded outputs and step confirmation.
  - **Why:** Incident runbooks go stale and are copy-pasted with typos.
  - **Stack:** Go, Markdown parser, TUI · **Difficulty:** 🟡 Intermediate

- **Architecture Diagram from Code**: Generate a C4-style diagram from imports, services and infra files, regenerated in CI.
  - **Why:** Hand-drawn diagrams drift from reality.
  - **Stack:** Python, tree-sitter, D2 or Mermaid · **Difficulty:** 🟡 Intermediate · **Prior art:** [d2lang/d2](https://github.com/d2lang/d2)

- **Cheat Sheet Builder**: Build personal, searchable cheat sheets from your own shell history and notes.
  - **Why:** Generic cheat sheets don't match your actual tools.
  - **Stack:** Rust, SQLite FTS, TUI · **Difficulty:** 🟢 Beginner

- **Terminal Docs Browser**: Offline docs for your installed language and library versions, searchable from the terminal.
  - **Why:** Online docs often show the wrong version.
  - **Stack:** Rust, DevDocs data, TUI · **Difficulty:** 🟡 Intermediate

- **CLI Help Linter**: Checks a CLI's --help output for consistent flags, examples and descriptions.
  - **Why:** Inconsistent help text makes tools feel unfinished.
  - **Stack:** Python or Go · **Difficulty:** 🟢 Beginner

- **Command Cookbook per Repo**: A searchable, runnable cookbook of the repo's common commands stored in a Markdown file.
  - **Why:** Tribal knowledge about project commands lives in people's heads.
  - **Stack:** Go TUI, Markdown parser · **Difficulty:** 🟡 Intermediate

- **Screenshot Refresher for Docs**: Re-captures docs screenshots automatically from scripted app states in CI.
  - **Why:** Outdated screenshots make docs look abandoned.
  - **Stack:** Playwright, GitHub Actions · **Difficulty:** 🟡 Intermediate

## Build & release

- **Monorepo Affected Graph**: Show which packages and tests are affected by a change, for any language, using the import graph.
  - **Why:** Running everything on every change wastes CI time.
  - **Stack:** Go, language import parsers · **Difficulty:** 🔴 Advanced · **Prior art:** [nrwl/nx](https://github.com/nrwl/nx)

- **Standalone Binary Release Kit for Python and Node CLIs**: Build single-file binaries for each OS and architecture, checksum, sign and upload them to GitHub Releases.
  - **Why:** Users want CLIs without installing a runtime; Go-style release tooling is rarer for Python and Node.
  - **Stack:** PyInstaller or Node SEA, cosign, GitHub Actions · **Difficulty:** 🟡 Intermediate · **Prior art:** [goreleaser/goreleaser](https://github.com/goreleaser/goreleaser)

- **Build Cache Analyzer**: Explain cache misses in CI builds by diffing inputs between runs.
  - **Why:** Unexplained cache misses silently double CI time.
  - **Stack:** Go, build tool logs, hashing · **Difficulty:** 🔴 Advanced

- **Changelog Entry Linter**: Check that changelog entries describe user impact and include migration notes for breaking changes.
  - **Why:** Changelogs full of commit subjects don't help users upgrade.
  - **Stack:** TypeScript, Markdown parser, CI · **Difficulty:** 🟢 Beginner · **Prior art:** [changesets/changesets](https://github.com/changesets/changesets)

- **Version Bump Wizard**: Detects every place a version appears in a repo and bumps them all consistently.
  - **Why:** Versions drift between package files, docs and constants.
  - **Stack:** Rust or Go CLI · **Difficulty:** 🟢 Beginner

- **Release Notes from Merged PRs**: Groups merged PRs by label into draft release notes with contributor credits.
  - **Why:** Writing release notes by hand gets skipped.
  - **Stack:** Node.js, GitHub API · **Difficulty:** 🟡 Intermediate

- **Compile Time Hotspot Finder**: Shows which files, templates or macros dominate compile and link time across a build, with a trace view.
  - **Why:** Slow builds are usually dominated by a handful of files nobody knows about.
  - **Stack:** Clang or rustc timing traces, Chrome trace viewer · **Difficulty:** 🔴 Advanced

- **Cross-Compilation Matrix Builder**: Builds a CLI for every OS and architecture pair with one config and checksums.
  - **Why:** Shipping binaries for many platforms is repetitive CI plumbing.
  - **Stack:** Go or Zig toolchain, GitHub Actions · **Difficulty:** 🔴 Advanced

- **Binary Size Explainer**: Breaks a compiled binary's size down by package and symbol and diffs it between releases.
  - **Why:** Binaries bloat release by release and nobody notices until downloads slow down.
  - **Stack:** Rust or Go, symbol table parsing, CI comment · **Difficulty:** 🔴 Advanced
