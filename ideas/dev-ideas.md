# Dev Ideas

> **Scope:** Things you import, embed or apply inside a codebase: libraries, testing, code quality, API and data-layer patterns, frontend engineering, observability and docs.

107 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Testing](#testing)
- [Code quality & refactoring](#code-quality--refactoring)
- [APIs & backends](#apis--backends)
- [Data layer](#data-layer)
- [Frontend & UX engineering](#frontend--ux-engineering)
- [Observability & reliability](#observability--reliability)
- [Docs & DX](#docs--dx)

## Testing

- **Property-Based Test Generator from Types**: Generate property-based tests from function signatures and docstrings, starting with round-trip and invariant properties.
  - **Why:** Property tests find edge cases example tests miss, but writing generators is a barrier.
  - **Stack:** Python + Hypothesis or TypeScript + fast-check · **Difficulty:** 🟡 Intermediate · **Prior art:** [HypothesisWorks/hypothesis](https://github.com/HypothesisWorks/hypothesis)

- **Mutation Testing for Changed Lines Only**: Run mutation testing only on lines changed in a PR so it's fast enough for CI.
  - **Why:** Full mutation runs take hours; diff-scoped runs give the signal in minutes.
  - **Stack:** Stryker or mutmut, git diff, CI · **Difficulty:** 🟡 Intermediate · **Prior art:** [stryker-mutator/stryker-js](https://github.com/stryker-mutator/stryker-js)

- **Snapshot Test Pruner**: Find snapshot files no test references anymore and snapshots that change on every run.
  - **Why:** Stale and flaky snapshots erode trust in the suite.
  - **Stack:** Node or Python, test runner hooks · **Difficulty:** 🟢 Beginner

- **Contract Tests from Production Traffic**: Sample real API traffic and generate consumer contract tests with sensitive fields masked.
  - **Why:** Hand-written contracts miss how clients actually call the API.
  - **Stack:** Python, Pact, traffic capture · **Difficulty:** 🔴 Advanced · **Prior art:** [pact-foundation/pact-js](https://github.com/pact-foundation/pact-js)

- **Deterministic Time and Randomness Kit**: Library that controls clocks, timers, random seeds and UUIDs in tests from one fixture.
  - **Why:** Time and randomness cause a large share of flaky tests.
  - **Stack:** TypeScript and Python packages · **Difficulty:** 🟢 Beginner

- **Test Data Builders Generator**: Generate fluent test-data builders from ORM models or TypeScript types.
  - **Why:** Setup code dominates tests and gets copy-pasted.
  - **Stack:** TypeScript AST, Python introspection · **Difficulty:** 🟢 Beginner

- **API Fuzzing from OpenAPI in CI**: Fuzz every endpoint from its OpenAPI schema and report 500s and schema violations on PRs.
  - **Why:** Finds crashes and validation gaps before users do.
  - **Stack:** Schemathesis, GitHub Actions · **Difficulty:** 🟡 Intermediate · **Prior art:** [schemathesis/schemathesis](https://github.com/schemathesis/schemathesis)

- **Visual Regression for Components on a Budget**: Screenshot components in Storybook and diff them in CI without a paid service.
  - **Why:** Visual bugs slip through unit tests.
  - **Stack:** Playwright, Storybook, pixel diff · **Difficulty:** 🟡 Intermediate

- **Testcontainers Recipes Library**: Ready-made, tested containers for common services with seed data and fast startup snapshots.
  - **Why:** Integration test setup is repeated in every project.
  - **Stack:** Testcontainers, Docker, multiple languages · **Difficulty:** 🟢 Beginner · **Prior art:** [testcontainers/testcontainers-java](https://github.com/testcontainers/testcontainers-java)

- **Load Test from User Journeys**: Convert recorded browser sessions into load test scripts with realistic think times.
  - **Why:** Synthetic load tests rarely match real behaviour.
  - **Stack:** k6, HAR parsing · **Difficulty:** 🟡 Intermediate · **Prior art:** [grafana/k6](https://github.com/grafana/k6)

- **Golden File Test Helper**: A tiny library for golden-file tests with an `--update` flag and readable, colourised diffs.
  - **Why:** CLIs, code generators and formatters need output tests without a heavy snapshot framework.
  - **Stack:** Go or Python library · **Difficulty:** 🟢 Beginner

- **HTTP Cassettes with Secret Scrubbing**: Record outbound HTTP in tests VCR-style and scrub tokens, cookies and emails before the cassette is saved.
  - **Why:** Committed cassettes are a common source of leaked API keys.
  - **Stack:** vcrpy plugin or nock wrapper · **Difficulty:** 🟢 Beginner · **Prior art:** [kevin1024/vcrpy](https://github.com/kevin1024/vcrpy)

- **Test Name Linter**: Enforces descriptive test names (behaviour, not "test1") with a configurable pattern.
  - **Why:** Good test names make CI failures self-explanatory.
  - **Stack:** ESLint rule or pytest plugin · **Difficulty:** 🟢 Beginner

- **Tests from Markdown Tables**: Write business-rule cases as Markdown tables in the docs and run them as parameterised tests.
  - **Why:** Rules stay readable for product people and executable for developers.
  - **Stack:** pytest plugin, Markdown parser · **Difficulty:** 🟢 Beginner

- **Timezone and Locale Test Matrix**: A drop-in CI matrix that runs the suite under several TZ and locale settings.
  - **Why:** Date and number-format bugs hide until users elsewhere report them.
  - **Stack:** GitHub Actions matrix, pytest or Jest · **Difficulty:** 🟢 Beginner

- **Postgres Test Isolation Helper**: Gives each test a fresh database cloned from a template, or a rolled-back transaction, automatically.
  - **Why:** Shared test databases cause order-dependent failures.
  - **Stack:** Python or Node.js library, Postgres template databases · **Difficulty:** 🟡 Intermediate

- **Test Pyramid Report**: Classifies tests as unit, integration or end-to-end by what they touch and reports count and runtime share.
  - **Why:** Teams can't see slow end-to-end tests quietly taking over the suite.
  - **Stack:** Python, coverage data, import analysis · **Difficulty:** 🟡 Intermediate

- **HTTP Client Fault Injector**: Middleware that injects latency, timeouts and 5xx responses into outbound calls in tests and staging.
  - **Why:** Retry and timeout paths are rarely exercised until production does it for you.
  - **Stack:** Node.js or Go middleware, YAML config · **Difficulty:** 🟡 Intermediate

## Code quality & refactoring

- **Dead Code Finder Across Languages**: Find unused exports, files and dependencies in a polyglot repo.
  - **Why:** Dead code slows builds and misleads readers and agents.
  - **Stack:** Go or Rust, tree-sitter, import graph · **Difficulty:** 🟡 Intermediate · **Prior art:** [webpro-nl/knip](https://github.com/webpro-nl/knip)

- **Architecture Rules as Tests**: Declare allowed dependencies between layers and fail tests when code violates them.
  - **Why:** Architecture erodes one convenient import at a time.
  - **Stack:** dependency-cruiser, import-linter, ArchUnit · **Difficulty:** 🟢 Beginner · **Prior art:** [sverweij/dependency-cruiser](https://github.com/sverweij/dependency-cruiser)

- **Codemod Library for a Framework Upgrade**: Tested codemods for one painful major-version migration, with a dry-run report.
  - **Why:** Upgrades stall because manual migration is tedious.
  - **Stack:** jscodeshift or ts-morph, fixtures · **Difficulty:** 🟡 Intermediate · **Prior art:** [facebook/jscodeshift](https://github.com/facebook/jscodeshift)

- **Complexity Budget per Module**: Track cyclomatic complexity per module over time and fail PRs that exceed a budget.
  - **Why:** Complexity creep is invisible until code becomes unmaintainable.
  - **Stack:** Language analysers, CI, charts · **Difficulty:** 🟢 Beginner

- **TODO Tracker with Owners and Expiry**: Parse TODO comments with owners and dates, open issues for expired ones and report counts.
  - **Why:** TODOs accumulate forever without accountability.
  - **Stack:** Go, regex parsing, GitHub API · **Difficulty:** 🟢 Beginner

- **Error Message Linter**: Lint user-facing error messages for clarity: what happened, why and what to do next.
  - **Why:** Bad error messages drive support tickets.
  - **Stack:** ESLint or custom AST rules · **Difficulty:** 🟢 Beginner

- **Duplicate Code Detector with Refactor Hints**: Find near-duplicate code blocks and suggest a shared function signature.
  - **Why:** Copy-paste code diverges and doubles bug fixes.
  - **Stack:** Rust, token-based clone detection · **Difficulty:** 🟡 Intermediate

- **Import Cycle Breaker**: Detects import cycles and suggests the smallest set of moves that breaks them.
  - **Why:** Cycles slow builds and cause confusing initialisation-order bugs.
  - **Stack:** Python or TypeScript, graph analysis · **Difficulty:** 🟡 Intermediate

- **Public API Surface Snapshot**: Snapshots a library's exported symbols and signatures and fails CI on unintended breaking changes.
  - **Why:** Accidental breaking changes are the most common semver violation.
  - **Stack:** TypeScript compiler API or griffe for Python · **Difficulty:** 🟡 Intermediate · **Prior art:** [mkdocstrings/griffe](https://github.com/mkdocstrings/griffe)

- **Typed Application Errors Kit**: A pattern and tiny library for errors with codes, causes and user-safe messages.
  - **Why:** Ad-hoc error strings make handling, logging and translation painful.
  - **Stack:** TypeScript or Go · **Difficulty:** 🟢 Beginner

- **Stale Feature Flag Remover**: Finds flags that have been fully on for weeks and opens a PR deleting the dead branch.
  - **Why:** Old flags pile up into unreadable conditionals.
  - **Stack:** tree-sitter, feature flag provider API · **Difficulty:** 🟡 Intermediate

- **Domain Vocabulary Checker**: Finds synonyms used for the same concept (user, account, member) across code and UI strings.
  - **Why:** Inconsistent domain language confuses new developers and users alike.
  - **Stack:** Python, identifier splitting, a glossary file · **Difficulty:** 🟡 Intermediate

- **Type Coverage Ratchet**: Tracks the share of typed code and only allows it to go up, per directory.
  - **Why:** Gradual typing migrations stall without a ratchet.
  - **Stack:** TypeScript compiler API, mypy reports · **Difficulty:** 🟢 Beginner

- **Comment Rot Detector**: Flags comments whose surrounding code changed far more recently than the comment itself.
  - **Why:** Stale comments mislead more than missing ones.
  - **Stack:** git blame, tree-sitter · **Difficulty:** 🟢 Beginner

## APIs & backends

- **Typed API Client Generator with Retries**: Generate typed clients from OpenAPI with built-in retries, pagination and rate-limit handling.
  - **Why:** Generated clients usually skip the hard parts of real APIs.
  - **Stack:** TypeScript, OpenAPI, code templates · **Difficulty:** 🟡 Intermediate · **Prior art:** [hey-api/hey-api](https://github.com/hey-api/hey-api)

- **Idempotency Middleware**: Drop-in middleware for idempotency keys with storage, locking and response replay.
  - **Why:** Retries without idempotency cause double charges and duplicate records.
  - **Stack:** Express/FastAPI, Redis or Postgres · **Difficulty:** 🟡 Intermediate

- **Outbox Pattern Library**: Transactional outbox for Postgres that reliably publishes events to a queue.
  - **Why:** Dual writes to database and queue lose or duplicate events.
  - **Stack:** Go or TypeScript, Postgres, NATS/Kafka · **Difficulty:** 🟡 Intermediate

- **Queue Dashboard for Postgres Job Tables**: One UI to inspect, retry and pause jobs across Postgres-backed queues.
  - **Why:** Postgres queues are popular, but each ships its own (or no) dashboard.
  - **Stack:** TypeScript, Postgres, adapters per queue library · **Difficulty:** 🟡 Intermediate · **Prior art:** [riverqueue/river](https://github.com/riverqueue/river)

- **Rate Limiter Playground**: Compare token bucket, sliding window and GCRA limiters with a visual simulator and a library.
  - **Why:** Rate limiting is often implemented wrong under bursts.
  - **Stack:** TypeScript, Redis, visualisation · **Difficulty:** 🟢 Beginner

- **Feature Flag SDK with Local Evaluation**: Lightweight flag SDK that evaluates rules locally from a JSON file synced from git.
  - **Why:** Hosted flag services are overkill for small teams.
  - **Stack:** TypeScript, Go, OpenFeature provider · **Difficulty:** 🟡 Intermediate · **Prior art:** [open-feature/spec](https://github.com/open-feature/spec)

- **Embedded Webhook Sender**: Library that sends signed webhooks with retries and a delivery log using your existing Postgres, no extra service.
  - **Why:** Small apps need reliable webhooks without running separate infrastructure.
  - **Stack:** Go or TypeScript, Postgres · **Difficulty:** 🟡 Intermediate · **Prior art:** [svix/svix-webhooks](https://github.com/svix/svix-webhooks)

- **API Deprecation Headers Kit**: Middleware that adds Deprecation and Sunset headers and logs which clients still call old endpoints.
  - **Why:** Deprecations fail when you can't see who's still using them.
  - **Stack:** Middleware for several frameworks · **Difficulty:** 🟢 Beginner

- **Multi-Tenant Row-Level Security Starter**: Postgres RLS patterns for multi-tenant apps with tests proving tenants can't see each other's data.
  - **Why:** Tenant data leaks are catastrophic and easy to introduce.
  - **Stack:** Postgres, SQL tests, ORM integration · **Difficulty:** 🟡 Intermediate

- **Typed Config Loader with Boot Validation**: Load config from env, files and secrets into a typed schema and fail fast at startup with clear messages.
  - **Why:** Misconfiguration is discovered at the worst time: mid-request in production.
  - **Stack:** TypeScript + Zod or Python + Pydantic · **Difficulty:** 🟢 Beginner · **Prior art:** [colinhacks/zod](https://github.com/colinhacks/zod)

- **Cursor Pagination Kit**: Opaque, stable cursor pagination helpers for SQL with tie-breaking and tests for inserts during paging.
  - **Why:** Offset pagination skips and duplicates rows under writes.
  - **Stack:** TypeScript and Python, SQL builders · **Difficulty:** 🟡 Intermediate

- **Request ID Propagation Kit**: Middleware that creates a request ID, passes it through HTTP calls and queues, and adds it to every log line.
  - **Why:** Correlating logs across services is the first step of every debugging session.
  - **Stack:** Express, FastAPI and Go middleware · **Difficulty:** 🟢 Beginner

- **Problem Details Error Responses**: A library that returns RFC 9457 problem+json errors consistently from any route.
  - **Why:** Clients get machine-readable errors instead of a different JSON shape per endpoint.
  - **Stack:** Framework middleware for Express, FastAPI or Spring · **Difficulty:** 🟢 Beginner

- **ETag and Conditional Request Helper**: Middleware that computes ETags and handles If-None-Match and If-Match for caching and safe updates.
  - **Why:** Cuts bandwidth and prevents lost updates with almost no code.
  - **Stack:** Express or FastAPI middleware · **Difficulty:** 🟢 Beginner

- **Soft Delete and Audit Trail Mixin**: An ORM mixin that adds deleted_at, created_by and a history table with two lines of code.
  - **Why:** Almost every business app needs this and rebuilds it badly.
  - **Stack:** Django, SQLAlchemy or Prisma · **Difficulty:** 🟢 Beginner

- **Request Body Limits Kit**: Middleware that enforces body size, array length and nesting depth limits with clear error messages.
  - **Why:** Unbounded input is one of the easiest denial-of-service vectors.
  - **Stack:** Express, FastAPI, Go · **Difficulty:** 🟢 Beginner

- **Circuit Breaker with Built-In Metrics**: A small circuit breaker that exports open, half-open and closed transitions as metrics and logs.
  - **Why:** Breakers that trip silently are hard to trust or tune.
  - **Stack:** Go or TypeScript, Prometheus client · **Difficulty:** 🟡 Intermediate

- **GraphQL Query Cost Budget**: Assigns costs to fields and rejects queries that exceed a per-client budget.
  - **Why:** One deeply nested query can take down a GraphQL backend.
  - **Stack:** Node.js, graphql-js · **Difficulty:** 🟡 Intermediate

- **Server-Sent Events with Resume**: An SSE helper that handles Last-Event-ID resume, heartbeats and slow clients.
  - **Why:** SSE is the simplest real-time transport, but resume logic is usually wrong.
  - **Stack:** Node.js or Go · **Difficulty:** 🟡 Intermediate

- **Saga Orchestrator on Postgres**: Define multi-step business transactions with compensating actions and durable state in Postgres.
  - **Why:** Services need rollback semantics without adopting a whole workflow platform.
  - **Stack:** TypeScript or Go, Postgres · **Difficulty:** 🔴 Advanced

## Data layer

- **Schema Migration Linter for MySQL and SQLite**: Flag risky migrations (locking ALTERs, missing indexes, non-backwards-compatible changes) for databases beyond Postgres.
  - **Why:** Squawk covers Postgres; teams on other databases need the same safety net.
  - **Stack:** Go or Python, SQL parser · **Difficulty:** 🟡 Intermediate · **Prior art:** [sbdchd/squawk](https://github.com/sbdchd/squawk)

- **Zero-Downtime Migration Planner**: Turn a desired schema change into an expand/contract sequence of migrations and deploy steps.
  - **Why:** Teams know the pattern but get the order wrong.
  - **Stack:** Python, SQL diffing · **Difficulty:** 🔴 Advanced

- **Database-per-Tenant SQLite Manager**: Run one SQLite file per tenant with a migration runner, backups and routing across thousands of files.
  - **Why:** Per-tenant databases give isolation cheaply, but operations get hard at scale.
  - **Stack:** Go or TypeScript, SQLite, object storage · **Difficulty:** 🔴 Advanced · **Prior art:** [benbjohnson/litestream](https://github.com/benbjohnson/litestream)

- **Local-First Sync Engine Demo**: Offline-first app with CRDT sync, conflict visualisation and a server relay.
  - **Why:** Local-first is growing but hard to learn from toy examples.
  - **Stack:** TypeScript, Yjs or Automerge, WebSocket · **Difficulty:** 🔴 Advanced · **Prior art:** [yjs/yjs](https://github.com/yjs/yjs)

- **Query Cost Guard**: ORM plugin that warns about N+1 queries and full table scans in development.
  - **Why:** Performance problems are cheapest to fix before merge.
  - **Stack:** Django/Rails/Prisma middleware · **Difficulty:** 🟡 Intermediate

- **Migration Squasher**: Collapse hundreds of old migrations into one baseline, verified against a real database.
  - **Why:** Long migration histories slow tests and new environments.
  - **Stack:** Python or Go, schema dumps, Docker · **Difficulty:** 🟡 Intermediate · **Prior art:** [ariga/atlas](https://github.com/ariga/atlas)

- **N+1 Query Test Guard**: Fails a test when one request triggers a burst of near-identical queries.
  - **Why:** N+1 queries slip through code review because they look innocent.
  - **Stack:** Django, SQLAlchemy or ActiveRecord hooks · **Difficulty:** 🟢 Beginner

- **Production Snapshot Anonymiser**: Copy a production database into staging with deterministic masking rules per column.
  - **Why:** Realistic data for debugging without leaking customer PII.
  - **Stack:** Python, Postgres, YAML rules · **Difficulty:** 🟡 Intermediate

- **Enum Drift Checker**: Compares enums in code with database check constraints and fails on any mismatch.
  - **Why:** Adding a value in code but not in the database breaks at runtime.
  - **Stack:** Python or TypeScript, schema introspection · **Difficulty:** 🟢 Beginner

- **Read Replica Router with Stickiness**: Routes read queries to replicas but keeps a user on the primary for a few seconds after a write.
  - **Why:** Scaling reads without "I just saved it, where did it go?" bugs.
  - **Stack:** ORM plugin, Postgres replicas · **Difficulty:** 🔴 Advanced

- **Index Advisor from Slow Query Logs**: Parses slow query logs and proposes indexes with an estimated benefit and write cost.
  - **Why:** Most teams add indexes by guesswork.
  - **Stack:** Python, pg_stat_statements, HypoPG · **Difficulty:** 🔴 Advanced · **Prior art:** [HypoPG/hypopg](https://github.com/HypoPG/hypopg)

- **Money Type Library**: A decimal money type with currencies, rounding modes and allocation that never loses a cent.
  - **Why:** Floats for money cause real, expensive bugs.
  - **Stack:** TypeScript or Python · **Difficulty:** 🟢 Beginner

- **Bitemporal Tables Helper**: Adds valid-time and transaction-time history to tables with "as of" query helpers.
  - **Why:** Finance, insurance and HR need to know what was true and when it was known.
  - **Stack:** Postgres, SQLAlchemy or Prisma extension · **Difficulty:** 🔴 Advanced

## Frontend & UX engineering

- **Accessibility CI Gate**: Run automated accessibility checks on key pages in CI with a baseline so only new issues fail.
  - **Why:** A baseline makes adoption possible on legacy apps.
  - **Stack:** axe-core, Playwright, CI · **Difficulty:** 🟢 Beginner · **Prior art:** [dequelabs/axe-core](https://github.com/dequelabs/axe-core)

- **Bundle Budget Bot**: Enforce size budgets per entry point and comment on which dependency grew.
  - **Why:** Bundle bloat slowly degrades performance.
  - **Stack:** size-limit, bundler stats · **Difficulty:** 🟢 Beginner · **Prior art:** [ai/size-limit](https://github.com/ai/size-limit)

- **Figma Variables to Code Sync**: Sync design variables from Figma into token files and open a PR when designers change them.
  - **Why:** Design and code drift when values are copied by hand.
  - **Stack:** TypeScript, Figma API, Style Dictionary · **Difficulty:** 🟡 Intermediate · **Prior art:** [style-dictionary/style-dictionary](https://github.com/style-dictionary/style-dictionary)

- **Form State Machine Library**: Model multi-step forms as state machines with validation, persistence and analytics hooks.
  - **Why:** Complex forms are a top source of frontend bugs.
  - **Stack:** TypeScript, XState or custom FSM · **Difficulty:** 🟡 Intermediate · **Prior art:** [statelyai/xstate](https://github.com/statelyai/xstate)

- **i18n Missing Keys Finder**: Detect untranslated, unused and interpolation-mismatched keys across locales.
  - **Why:** Broken translations ship because nobody checks every locale.
  - **Stack:** TypeScript, AST parsing · **Difficulty:** 🟢 Beginner

- **Web Vitals Regression Tracker**: Measure Core Web Vitals per PR on preview deploys and comment on regressions.
  - **Why:** Performance regresses release by release.
  - **Stack:** Lighthouse CI, Playwright · **Difficulty:** 🟡 Intermediate · **Prior art:** [GoogleChrome/lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci)

- **Optimistic UI Helpers**: Small library for optimistic updates with rollback and conflict messages.
  - **Why:** Optimistic UIs feel fast but are often buggy on failure.
  - **Stack:** TypeScript, React/Svelte adapters · **Difficulty:** 🟡 Intermediate

- **Skeleton Loader Generator**: Generates skeleton placeholders from a component's real rendered layout.
  - **Why:** Hand-written skeletons drift from the layouts they imitate.
  - **Stack:** React, DOM measurement, Storybook addon · **Difficulty:** 🟡 Intermediate

- **Focus Management Utilities**: Tiny helpers for focus traps, restoring focus after dialogs and announcing route changes.
  - **Why:** Keyboard and screen-reader users get lost in single-page apps.
  - **Stack:** TypeScript, framework-agnostic · **Difficulty:** 🟢 Beginner

- **Design Token Linter**: Flags hard-coded colours, spacing and font sizes that should use design tokens.
  - **Why:** Tokens only pay off if people actually use them.
  - **Stack:** Stylelint plugin, ESLint for CSS-in-JS · **Difficulty:** 🟢 Beginner · **Prior art:** [stylelint/stylelint](https://github.com/stylelint/stylelint)

- **Client Error Boundary Reporter**: An error boundary that captures component stack and recent user actions and posts them to your own endpoint.
  - **Why:** Small teams want crash context without a paid monitoring tool.
  - **Stack:** React, a tiny ingest endpoint · **Difficulty:** 🟢 Beginner

- **Offline Form Queue**: Stores form submissions while offline and replays them with conflict hints when the connection returns.
  - **Why:** Field workers lose data on flaky mobile connections.
  - **Stack:** Service worker, IndexedDB · **Difficulty:** 🟡 Intermediate

- **Reduced Motion Audit**: Finds animations that ignore prefers-reduced-motion and patches them with a shared mixin.
  - **Why:** Motion can cause real discomfort; the fix is small but rarely applied.
  - **Stack:** PostCSS plugin, Playwright check · **Difficulty:** 🟢 Beginner

- **URL State Sync Hook**: Keeps filters, tabs and pagination in the URL with typed parsing and sensible history behaviour.
  - **Why:** Shareable, back-button-friendly UI state with no custom plumbing.
  - **Stack:** React or Vue, Zod · **Difficulty:** 🟢 Beginner

- **Hydration Mismatch Pinpointer**: A dev-mode tool that names the exact node and cause of each SSR hydration mismatch.
  - **Why:** Hydration errors are cryptic and eat hours of debugging.
  - **Stack:** React or Next.js dev plugin · **Difficulty:** 🟡 Intermediate

- **Micro-Frontend Contract Tests**: Verifies that independently deployed micro-frontends still agree on events, routes and shared props.
  - **Why:** Independent deploys break integrations nobody tested together.
  - **Stack:** TypeScript, Pact-style contracts, Playwright · **Difficulty:** 🔴 Advanced

## Observability & reliability

- **Structured Logging Conventions Kit**: Logger wrappers and lint rules that enforce consistent fields (request ID, user ID, error code).
  - **Why:** Inconsistent logs make incidents slower to debug.
  - **Stack:** Language libraries, lint rules · **Difficulty:** 🟢 Beginner

- **OpenTelemetry Auto-Setup**: One import that configures traces, metrics and logs with sensible defaults for a framework.
  - **Why:** OTel setup is verbose and intimidating.
  - **Stack:** OpenTelemetry SDKs · **Difficulty:** 🟡 Intermediate · **Prior art:** [open-telemetry/opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js)

- **SLO Tracker from Logs**: Compute SLOs and error budgets from access logs for teams that don't run Prometheus.
  - **Why:** Small teams want SLOs without adopting a metrics stack first.
  - **Stack:** Go or Python, log parsing, SQLite · **Difficulty:** 🟡 Intermediate · **Prior art:** [pyrra-dev/pyrra](https://github.com/pyrra-dev/pyrra)

- **Compose Chaos Profiles**: Declarative failure scenarios (latency, drops, errors) applied to docker-compose services with one command.
  - **Why:** Resilience code rarely gets tested before production.
  - **Stack:** Go, Toxiproxy, compose · **Difficulty:** 🟡 Intermediate · **Prior art:** [Shopify/toxiproxy](https://github.com/Shopify/toxiproxy)

- **Error Grouping Explainer**: Explain why errors were grouped together and suggest better fingerprints.
  - **Why:** Bad grouping hides new errors among old ones.
  - **Stack:** Python, stack trace parsing · **Difficulty:** 🟡 Intermediate

- **Graceful Shutdown Checker**: Test that a service drains connections and finishes in-flight work on SIGTERM.
  - **Why:** Bad shutdowns drop requests during every deploy.
  - **Stack:** Go, load generator, container runtime · **Difficulty:** 🟢 Beginner

- **Health Check Endpoint Kit**: Standard liveness and readiness endpoints with dependency checks, timeouts and caching.
  - **Why:** Home-grown health checks either lie or cascade failures across services.
  - **Stack:** Go, Node.js and Python libraries · **Difficulty:** 🟢 Beginner

- **Retry Budget Library**: Caps client retries at a percentage of normal traffic to prevent retry storms.
  - **Why:** Naive retries turn a small outage into a big one.
  - **Stack:** Go or Java library · **Difficulty:** 🟡 Intermediate

- **Log Sampling by Severity and Route**: Keeps every error, samples noisy success logs per route and preserves counts.
  - **Why:** Logging bills explode on hot endpoints.
  - **Stack:** structlog or pino processor · **Difficulty:** 🟢 Beginner

- **Deadline Propagation Helper**: Passes request deadlines through HTTP and gRPC calls so downstream work stops when callers give up.
  - **Why:** Work done after a timeout overloads services for no benefit.
  - **Stack:** Go context, Node.js AbortSignal · **Difficulty:** 🔴 Advanced

- **Canary Analysis Library**: Compares canary and baseline metrics with statistical tests and returns a go/no-go verdict.
  - **Why:** Eyeballing dashboards during rollouts misses slow regressions.
  - **Stack:** Python, SciPy, Prometheus API · **Difficulty:** 🔴 Advanced

- **Crash Reporter for CLI Tools**: Opt-in crash reports for command-line tools with scrubbed stack traces and a prefilled GitHub issue.
  - **Why:** CLI authors rarely hear about crashes; users rarely write good bug reports.
  - **Stack:** Python or Go library · **Difficulty:** 🟢 Beginner

- **Memory Leak Canary Test**: A test helper that runs a code path thousands of times and fails if heap usage keeps growing.
  - **Why:** Leaks are cheap to catch in CI and expensive to find in production.
  - **Stack:** Node.js or Python, heap snapshots · **Difficulty:** 🔴 Advanced

- **Graceful Degradation Toggles**: Named kill switches that turn off expensive features under load, with a tiny admin page.
  - **Why:** Shedding non-essential work keeps the core product up during spikes.
  - **Stack:** TypeScript or Go, Redis · **Difficulty:** 🟡 Intermediate

## Docs & DX

- **Docs from Tests**: Generate usage docs from well-named tests and examples so docs stay correct.
  - **Why:** Tests are the most accurate documentation you have.
  - **Stack:** Python or TypeScript, test runner plugins · **Difficulty:** 🟡 Intermediate

- **Upgrade Guide Generator**: Draft migration guides from breaking-change PRs with before-and-after code examples.
  - **Why:** Users upgrade faster with concrete examples than with release notes.
  - **Stack:** TypeScript, GitHub API, LLM summarisation · **Difficulty:** 🟡 Intermediate

- **API Examples Tester**: Execute every example request in API docs against a staging server nightly.
  - **Why:** Docs examples break without anyone noticing.
  - **Stack:** Python, OpenAPI examples, CI · **Difficulty:** 🟢 Beginner

- **Vale Style Pack for Developer Docs**: A tested style pack for API, CLI and tutorial docs: terminology, tense and command formatting.
  - **Why:** Vale is flexible, but writing good rules from scratch is slow.
  - **Stack:** Vale styles, test fixtures · **Difficulty:** 🟢 Beginner · **Prior art:** [vale-cli/vale](https://github.com/vale-cli/vale)

- **Package Publish Checker**: Verify a package's exports, types and files before publishing to npm or PyPI.
  - **Why:** Broken publishes are common and embarrassing.
  - **Stack:** publint, arethetypeswrong, twine check · **Difficulty:** 🟢 Beginner · **Prior art:** [publint/publint](https://github.com/publint/publint)

- **ADR Index Generator**: Architecture decision records with a generated index, status badges and "superseded by" links.
  - **Why:** Decisions get lost in chat; ADRs only work if they're easy to browse.
  - **Stack:** Markdown, Node.js or Python script · **Difficulty:** 🟢 Beginner

- **Env Var Documentation Generator**: Scans code for environment variable reads and generates a documented .env.example.
  - **Why:** New developers waste hours finding which variables an app needs.
  - **Stack:** Python or TypeScript, AST parsing · **Difficulty:** 🟢 Beginner

- **Error Code Catalogue**: Every error code in the codebase links to a docs page generated from source annotations.
  - **Why:** Users and support staff can look up an error instead of opening a ticket.
  - **Stack:** Docstring annotations, static site generator · **Difficulty:** 🟢 Beginner

- **Docs Page Feedback Widget**: A "was this helpful?" widget that files votes and comments as GitHub issues per page.
  - **Why:** Docs teams need signal on which pages fail readers.
  - **Stack:** JavaScript widget, GitHub API · **Difficulty:** 🟢 Beginner

- **Interactive API Tutorial Builder**: Turns a sequence of real API calls into a step-by-step tutorial readers can run against a sandbox.
  - **Why:** Hands-on tutorials convert far better than static reference docs.
  - **Stack:** TypeScript, OpenAPI, sandbox tokens · **Difficulty:** 🟡 Intermediate

- **Code Owner Hints in Docs**: Shows the owning team and a contact link on every internal docs page, pulled from CODEOWNERS.
  - **Why:** Readers with questions don't know who to ask.
  - **Stack:** Static site plugin, CODEOWNERS parser · **Difficulty:** 🟢 Beginner

- **Deprecation Timeline Page**: Generates a public page of deprecated APIs, their replacements and removal dates from code annotations.
  - **Why:** Users need one place to plan upgrades.
  - **Stack:** Annotations, static site generator · **Difficulty:** 🟢 Beginner
