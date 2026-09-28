# Dev Ideas

> **Scope:** Things you import, embed or apply inside a codebase: libraries, testing, code quality, API and data-layer patterns, frontend engineering, observability and docs.

52 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

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
