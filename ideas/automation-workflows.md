# Automation & Workflows

> **Scope:** Glue that connects existing services: personal and business automations, workflow engines, browser automation, bots and sync.

90 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Personal automation](#personal-automation)
- [Developer workflow automation](#developer-workflow-automation)
- [Business operations](#business-operations)
- [Workflow engines & patterns](#workflow-engines--patterns)
- [Browser & desktop automation](#browser--desktop-automation)
- [Messaging bots](#messaging-bots)
- [Data sync & integration](#data-sync--integration)

## Personal automation

- **Inbox Zero Rules Engine**: Local rules plus a small classifier that labels, archives and drafts replies to email, with a daily digest.
  - **Why:** Email triage eats hours; rules alone miss nuance and cloud AI tools read everything.
  - **Stack:** Python, Gmail API, local LLM · **Difficulty:** 🟡 Intermediate

- **Bill Due-Date Aggregator**: Parse bill emails and PDFs into a calendar of due dates with amount and pay links.
  - **Why:** Late fees come from bills buried in the inbox.
  - **Stack:** Python, email parsing, Calendar API · **Difficulty:** 🟢 Beginner

- **Document Autofiler**: Watch a scan folder, OCR documents, name them by content and file them into the right folder.
  - **Why:** Paper and PDF clutter makes documents impossible to find.
  - **Stack:** Python, OCRmyPDF, rules or classifier · **Difficulty:** 🟢 Beginner · **Prior art:** [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

- **Price Drop Watcher**: Track product prices across shops and alert when they fall below a target.
  - **Why:** Saves money on planned purchases without manual checking.
  - **Stack:** Python, Playwright, SQLite, ntfy · **Difficulty:** 🟢 Beginner · **Prior art:** [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io)

- **Read-Later to Summary Digest**: Collect saved articles and send a weekly digest with summaries and reading-time estimates.
  - **Why:** Read-later queues grow forever and never get read.
  - **Stack:** Python, readability parser, LLM, email · **Difficulty:** 🟢 Beginner

- **Automatic Expense Categoriser**: Import bank CSVs, categorise with rules learned from corrections and export to a budget app.
  - **Why:** Manual categorisation is the main reason people abandon budgeting.
  - **Stack:** Python, scikit-learn, CSV · **Difficulty:** 🟢 Beginner

- **Home Admin Reminder Bot**: Chat bot that reminds you about rego renewals, insurance, warranties and passport expiry.
  - **Why:** Life admin deadlines are rare, so they're easy to forget.
  - **Stack:** Telegram bot, SQLite, cron · **Difficulty:** 🟢 Beginner

- **Photo Backup Deduplicator**: Find duplicate and near-duplicate photos across drives and cloud exports before backup.
  - **Why:** Duplicates waste storage and make libraries messy.
  - **Stack:** Python, perceptual hashing · **Difficulty:** 🟢 Beginner

- **Voice Memo to Notes**: Phone voice memos are transcribed locally and filed into your notes app with tags and action items.
  - **Why:** Ideas captured on the go never make it into a system.
  - **Stack:** whisper.cpp, sync folder watcher, Markdown · **Difficulty:** 🟢 Beginner · **Prior art:** [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)

- **Daily Brief Agent**: A scheduled agent compiles calendar, weather, commute, news topics and open tasks into one morning message.
  - **Why:** Checking five apps every morning is a habit worth automating.
  - **Stack:** Python, cron, calendar and weather APIs, LLM · **Difficulty:** 🟢 Beginner

- **Downloads Folder Organiser**: Sort downloads by type and source, archive old files and delete stale installers after a grace period.
  - **Why:** Downloads folders grow into unsearchable dumps.
  - **Stack:** Python, watchdog, rules YAML · **Difficulty:** 🟢 Beginner

- **Job Posting Watcher**: Track job boards and company careers pages with filters and alert on new matching roles.
  - **Why:** Good roles fill fast; manual checking is slow.
  - **Stack:** Python, Playwright, SQLite, notifications · **Difficulty:** 🟢 Beginner

- **Parcel Tracking Aggregator**: Forward shipping emails and get one page tracking every parcel across carriers with delivery-day alerts.
  - **Why:** Online shoppers juggle tracking links from a dozen carriers.
  - **Stack:** Python, email parsing, carrier APIs · **Difficulty:** 🟢 Beginner

- **Library Loan Due-Date Reminders**: Logs into your public library account and reminds you before loans are due, with one-click renewals.
  - **Why:** Library fines and holds lost to forgotten due dates.
  - **Stack:** Python, Playwright, cron · **Difficulty:** 🟢 Beginner · **Prior art:** [microsoft/playwright](https://github.com/microsoft/playwright)

- **Screenshot Organiser with OCR**: Renames and files screenshots by their text content and makes them searchable.
  - **Why:** Screenshot folders become unsearchable piles.
  - **Stack:** Python, Tesseract, folder watcher · **Difficulty:** 🟢 Beginner · **Prior art:** [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

- **Weekly Review Generator**: Collects your calendar, completed tasks and notes into a weekly review template every Friday.
  - **Why:** Weekly reviews help but gathering the material takes too long.
  - **Stack:** Python, calendar and task APIs, Markdown · **Difficulty:** 🟢 Beginner

- **Podcast Episode Auto-Downloader with Chapters**: Downloads new episodes from chosen feeds, embeds chapters and moves them to your phone or NAS.
  - **Why:** Podcast apps lock downloads in; power listeners want files.
  - **Stack:** Python, feedparser, ffmpeg · **Difficulty:** 🟢 Beginner

- **Kids' Screen Time Report**: Compiles weekly screen time from router and device data into a readable family report.
  - **Why:** Parents want an overview without installing spyware.
  - **Stack:** Python, router API, email · **Difficulty:** 🟡 Intermediate

## Developer workflow automation

- **Repository Mirroring Scheduler**: Mirror repos between GitHub, GitLab and Codeberg on a schedule, including tags and releases.
  - **Why:** Mirrors protect against account loss and platform outages.
  - **Stack:** Go, git, platform APIs · **Difficulty:** 🟢 Beginner

- **Dependency Update Batching**: Group low-risk dependency updates into one weekly PR and auto-merge when tests pass.
  - **Why:** Many small update PRs cause review fatigue.
  - **Stack:** Renovate config, GitHub Actions · **Difficulty:** 🟢 Beginner · **Prior art:** [renovatebot/renovate](https://github.com/renovatebot/renovate)

- **Preview Deploy Cleanup**: Delete preview environments, databases and DNS records when PRs close.
  - **Why:** Orphaned previews cost money and leak data.
  - **Stack:** GitHub Actions, cloud CLIs · **Difficulty:** 🟢 Beginner

- **Standup Notes from Git Activity**: Each morning, compile yesterday's commits, PRs and reviews into a short personal note.
  - **Why:** Saves time recalling what you did.
  - **Stack:** Python, GitHub API, cron · **Difficulty:** 🟢 Beginner

- **Auto-Generated Onboarding Tasks**: When someone joins, create accounts, repo access and a checklist issue automatically.
  - **Why:** Manual onboarding misses steps and delays productivity.
  - **Stack:** Python, SCIM/Google/GitHub APIs · **Difficulty:** 🟡 Intermediate

- **Incident Channel Automation**: Create an incident channel, invite on-call, post runbook links and start a timeline when an alert fires.
  - **Why:** The first minutes of an incident are wasted on setup.
  - **Stack:** Slack API, PagerDuty/Opsgenie webhooks · **Difficulty:** 🟡 Intermediate

- **Release Announcement Fan-Out**: On a GitHub release, post to Discord, X, Bluesky and a newsletter with per-channel formatting.
  - **Why:** Releases go unnoticed without promotion.
  - **Stack:** GitHub Actions, platform APIs · **Difficulty:** 🟢 Beginner

- **Database Backup Verification**: Nightly restore of the latest backup into a scratch database with row-count and query checks.
  - **Why:** Untested backups often fail when you need them.
  - **Stack:** Bash or Python, Postgres, cron · **Difficulty:** 🟢 Beginner · **Prior art:** [restic/restic](https://github.com/restic/restic)

- **Calendar Focus Block Defender**: Books focus blocks around existing meetings and declines conflicting invites with a polite note.
  - **Why:** Meetings fragment days into useless half hours.
  - **Stack:** Google Calendar API, rules engine · **Difficulty:** 🟢 Beginner

- **Nightly Dependency Smoke Test**: Installs the latest versions of all dependencies nightly and runs tests to catch breakage early.
  - **Why:** Upstream breakage surfaces weeks later during an unrelated change.
  - **Stack:** GitHub Actions scheduled workflow · **Difficulty:** 🟢 Beginner

- **Issue to Branch Automation**: Creates a correctly named branch and draft PR from an issue with one command or label.
  - **Why:** Branch naming conventions are forgotten and PRs aren't linked to issues.
  - **Stack:** GitHub CLI extension or Action · **Difficulty:** 🟢 Beginner

- **PR Screenshot Bot for UI Changes**: Captures before and after screenshots of changed pages on each PR and posts them as a comment.
  - **Why:** Reviewers approve UI changes without ever seeing them.
  - **Stack:** GitHub Action, Playwright · **Difficulty:** 🟡 Intermediate

- **Flaky Deploy Auto-Retry with Context**: Retries failed deploy steps that match known transient errors and posts context when it gives up.
  - **Why:** Engineers manually re-run deploys for the same transient failures.
  - **Stack:** CI plugin, error pattern config · **Difficulty:** 🟡 Intermediate

- **Database Migration Approval Gate**: Pauses deploys containing risky migrations until a DBA approves in chat.
  - **Why:** Dangerous migrations slip into routine deploys.
  - **Stack:** GitHub Actions environments, Slack API · **Difficulty:** 🟡 Intermediate

## Business operations

- **Lead Enrichment Pipeline**: Enrich inbound leads with company data, score them and route to the right salesperson.
  - **Why:** Sales teams waste time on unqualified leads.
  - **Stack:** n8n or Python, enrichment APIs, CRM API · **Difficulty:** 🟡 Intermediate · **Prior art:** [n8n-io/n8n](https://github.com/n8n-io/n8n)

- **Invoice to Accounting Sync**: Extract invoice data from emailed PDFs and create draft bills in accounting software.
  - **Why:** Data entry is error-prone and slow.
  - **Stack:** Python, PDF parsing, Xero/QuickBooks API · **Difficulty:** 🟡 Intermediate

- **Contract Renewal Tracker**: Extract renewal and notice dates from contracts and schedule reminders before deadlines.
  - **Why:** Auto-renewals lock companies into unwanted contracts.
  - **Stack:** Python, LLM extraction, calendar · **Difficulty:** 🟢 Beginner

- **Customer Onboarding Sequence**: Trigger emails, tasks and check-ins based on what a new customer has or hasn't done.
  - **Why:** Activation drops when onboarding is one-size-fits-all.
  - **Stack:** Workflow engine, product events, email API · **Difficulty:** 🟡 Intermediate · **Prior art:** [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev)

- **Form to Spreadsheet to Slack**: Validate form submissions, append them to a sheet and post a summary to a channel.
  - **Why:** Classic glue that small teams need weekly.
  - **Stack:** Serverless function, Google Sheets API, Slack API · **Difficulty:** 🟢 Beginner

- **Supplier Price List Normaliser**: Convert supplier price lists in varied spreadsheets into one normalised catalogue.
  - **Why:** Resellers spend hours reformatting spreadsheets.
  - **Stack:** Python, pandas, fuzzy matching · **Difficulty:** 🟡 Intermediate

- **Social Mention Monitor**: Track brand mentions across Reddit, HN, Bluesky and news with sentiment and alerts.
  - **Why:** Small companies miss conversations about them.
  - **Stack:** Python, platform APIs, classifier · **Difficulty:** 🟡 Intermediate

- **Quote to Contract to Invoice Chain**: When a quote is accepted, generate the contract, collect a signature and schedule invoices.
  - **Why:** Small agencies retype the same details into three tools.
  - **Stack:** n8n or Node.js, e-signature API, accounting API · **Difficulty:** 🟡 Intermediate · **Prior art:** [n8n-io/n8n](https://github.com/n8n-io/n8n)

- **Employee Onboarding Checklist Runner**: Creates accounts, sends welcome packs and schedules check-ins when a hire is added to HR.
  - **Why:** Onboarding steps get missed and new hires wait days for access.
  - **Stack:** Workflow engine, Google Workspace and Slack APIs · **Difficulty:** 🟡 Intermediate

- **Timesheet Reminder and Approval Flow**: Reminds staff to submit timesheets, escalates missing ones and routes them for approval.
  - **Why:** Payroll gets delayed by chasing timesheets manually.
  - **Stack:** Python, Slack or Teams API, spreadsheet · **Difficulty:** 🟡 Intermediate

- **Customer Feedback Router**: Classifies feedback from email, forms and reviews into bugs, requests and praise and routes each.
  - **Why:** Feedback lands in shared inboxes where it rots.
  - **Stack:** n8n, small classifier, issue tracker API · **Difficulty:** 🟢 Beginner

- **Low Stock Reorder Automation**: Watches stock levels and drafts purchase orders to suppliers when items hit reorder points.
  - **Why:** Small retailers run out of best-sellers.
  - **Stack:** Python, POS API, email · **Difficulty:** 🟢 Beginner

- **Refund Request Triage**: Pulls refund requests, checks order history against policy and pre-fills approve or deny decisions.
  - **Why:** Support teams make inconsistent refund decisions under pressure.
  - **Stack:** Node.js, Stripe API, helpdesk API · **Difficulty:** 🟡 Intermediate

## Workflow engines & patterns

- **Durable Workflow Examples Gallery**: Real-world workflow examples (payments, onboarding, data sync) implemented on a durable execution engine.
  - **Why:** Durable execution is powerful but examples are mostly toy-sized.
  - **Stack:** Temporal or Restate SDKs · **Difficulty:** 🟡 Intermediate · **Prior art:** [temporalio/temporal](https://github.com/temporalio/temporal)

- **Human-in-the-Loop Approval Step**: Reusable approval step for workflows via Slack or email with timeouts and escalation.
  - **Why:** Many automations need a human decision before acting.
  - **Stack:** Workflow engine plugin, Slack API · **Difficulty:** 🟢 Beginner

- **Workflow Diff and Review**: Show changes to visual workflow definitions (JSON) as readable diffs in PRs.
  - **Why:** Visual automation tools are hard to review in git.
  - **Stack:** TypeScript, JSON diff, Action · **Difficulty:** 🟡 Intermediate

- **Automation Error Inbox**: Central inbox of failed automation runs across tools with retry buttons.
  - **Why:** Failures in Zapier/n8n/cron get lost in email.
  - **Stack:** Next.js, webhooks, Postgres · **Difficulty:** 🟡 Intermediate

- **Webhook Fan-Out Router**: Receive one webhook and route it to multiple destinations with filters and transforms.
  - **Why:** Many services allow only one webhook URL.
  - **Stack:** Go, config file, retries · **Difficulty:** 🟢 Beginner

- **Scheduled Job Dashboard**: One view of all cron jobs across servers and platforms with last run and next run.
  - **Why:** Scheduled jobs are scattered and undocumented.
  - **Stack:** Go, agents or API polling, web UI · **Difficulty:** 🟡 Intermediate

- **Idempotent Automation Kit**: Helpers for dedupe keys, checkpoints and safe retries in scripts.
  - **Why:** Re-running scripts after failure causes duplicates.
  - **Stack:** Python library, SQLite · **Difficulty:** 🟢 Beginner

- **Workflow Dry-Run Mode**: Run an automation against real triggers but with side effects stubbed and logged.
  - **Why:** Testing automations in production is scary; dry runs make changes safe.
  - **Stack:** TypeScript library, adapter mocks · **Difficulty:** 🟡 Intermediate

- **Automation Dependency Map**: Draws which automations trigger which, across tools, to find loops and single points of failure.
  - **Why:** Companies lose track of chains of Zaps and scripts.
  - **Stack:** Python, workflow exports, Graphviz · **Difficulty:** 🟡 Intermediate

- **Rate-Limit-Aware Task Scheduler**: Schedules API-heavy automations to stay under each provider's rate limits.
  - **Why:** Automations fail at scale because they ignore rate limits.
  - **Stack:** Go or Python, token bucket per provider · **Difficulty:** 🔴 Advanced

- **Event Replay for Automations**: Store every trigger event so failed workflows can be replayed after a fix.
  - **Why:** Fixing a bug doesn't recover the events it dropped.
  - **Stack:** Postgres, TypeScript, webhook capture · **Difficulty:** 🔴 Advanced

- **Workflow Versioning with Migrations**: Safely update long-running workflows while in-flight instances continue on old logic.
  - **Why:** Editing a running workflow breaks instances midway.
  - **Stack:** Temporal-style engine, TypeScript · **Difficulty:** 🔴 Advanced · **Prior art:** [temporalio/temporal](https://github.com/temporalio/temporal)

- **Cross-Tool Automation Audit Log**: Collects run logs from Zapier, n8n, cron jobs and GitHub Actions into one searchable audit trail.
  - **Why:** When something odd happens, nobody knows which automation did it.
  - **Stack:** Go, provider APIs, ClickHouse · **Difficulty:** 🔴 Advanced

## Browser & desktop automation

- **Form Filler from Structured Data**: Fill repetitive web forms from a CSV with human review before submit.
  - **Why:** Government and legacy portals lack APIs.
  - **Stack:** Playwright, CSV, review UI · **Difficulty:** 🟢 Beginner · **Prior art:** [microsoft/playwright](https://github.com/microsoft/playwright)

- **Screenshot Monitoring for Dashboards**: Periodically screenshot key dashboards and alert when values cross thresholds.
  - **Why:** Some systems only expose data through a UI.
  - **Stack:** Playwright, OCR, alerts · **Difficulty:** 🟡 Intermediate

- **Desktop Macro Recorder with Parameters**: Record mouse and keyboard macros and turn them into parameterised scripts.
  - **Why:** Repetitive desktop tasks in legacy apps waste time.
  - **Stack:** Python, pynput, script generation · **Difficulty:** 🟡 Intermediate

- **Text Expander Snippet Sync**: Sync text snippets across machines and share team snippets from a git repo.
  - **Why:** Consistent replies and templates across a team.
  - **Stack:** Espanso, git · **Difficulty:** 🟢 Beginner · **Prior art:** [espanso/espanso](https://github.com/espanso/espanso)

- **Tab and Session Organiser**: Save, name and restore browser tab sessions per project with search.
  - **Why:** Tab overload kills focus.
  - **Stack:** Browser extension, IndexedDB · **Difficulty:** 🟢 Beginner

- **Web Data Extractor with Self-Healing Selectors**: Scraper that recovers when page structure changes by re-locating elements semantically.
  - **Why:** Scrapers break on every redesign.
  - **Stack:** Playwright, embeddings or LLM fallback · **Difficulty:** 🟡 Intermediate · **Prior art:** [apify/crawlee](https://github.com/apify/crawlee)

- **Receipt Downloader for Online Accounts**: Logs into utility and SaaS accounts monthly and downloads invoices into one folder.
  - **Why:** Accountants ask for invoices scattered across dozens of portals.
  - **Stack:** Playwright, scheduler, secrets manager · **Difficulty:** 🟢 Beginner

- **Booking Slot Sniper**: Watches a booking site for cancellations and alerts you when a slot opens.
  - **Why:** Popular slots (tennis courts, visa appointments) open unpredictably.
  - **Stack:** Playwright, notifications · **Difficulty:** 🟢 Beginner

- **Desktop Window Layout Restorer**: Saves and restores window layouts per task, like "coding" or "meetings".
  - **Why:** Rearranging windows after every monitor change wastes time.
  - **Stack:** Python or Swift, OS window APIs · **Difficulty:** 🟢 Beginner

- **Web Form Regression Watcher**: Periodically submits test data to critical forms and alerts when they break.
  - **Why:** Broken lead forms go unnoticed for days.
  - **Stack:** Playwright, cron, alerts · **Difficulty:** 🟡 Intermediate

## Messaging bots

- **Team Lunch Order Bot**: Collect lunch orders in chat, total them and send one order to the restaurant.
  - **Why:** Group orders are chaos in chat threads.
  - **Stack:** Slack or Discord bot, SQLite · **Difficulty:** 🟢 Beginner

- **On-Call Handoff Bot**: Post a summary of open incidents, alerts and notes at each on-call rotation change.
  - **Why:** Context is lost between on-call shifts.
  - **Stack:** Slack bot, PagerDuty API · **Difficulty:** 🟢 Beginner

- **Knowledge Base Answer Bot with Sources**: Chat bot answering questions from internal docs with links and "I don't know" when unsure.
  - **Why:** Repeated questions interrupt experts.
  - **Stack:** Python, retrieval, Slack API · **Difficulty:** 🟡 Intermediate

- **Telegram Alerts Hub**: Route alerts from many sources into categorised Telegram topics with mute schedules.
  - **Why:** Personal alerts are scattered across apps.
  - **Stack:** Python, Telegram Bot API, webhooks · **Difficulty:** 🟢 Beginner

- **Meeting Notes to Tasks Bot**: Post meeting notes in chat and get tasks created in the tracker with owners and due dates.
  - **Why:** Action items get forgotten after meetings.
  - **Stack:** Slack bot, LLM extraction, Linear/Jira API · **Difficulty:** 🟢 Beginner

- **Community Moderation Assistant**: Flag spam, scams and rule violations in Discord with moderator review queues.
  - **Why:** Volunteer moderators can't watch everything.
  - **Stack:** Discord bot, classifiers, dashboard · **Difficulty:** 🟡 Intermediate

- **Office Plant Watering Rota Bot**: Rotates plant-watering duty in team chat and tracks which plants were watered when.
  - **Why:** Office plants die from diffusion of responsibility.
  - **Stack:** Slack bot, SQLite · **Difficulty:** 🟢 Beginner

- **Birthday and Work Anniversary Bot**: Posts celebrations in team chat from an HR spreadsheet with opt-out.
  - **Why:** Small gestures matter but are easy to forget.
  - **Stack:** Slack or Discord bot, Google Sheets API · **Difficulty:** 🟢 Beginner

- **Shared Expenses Bot for Group Chats**: Log shared expenses in a group chat and get running balances and settle-up suggestions.
  - **Why:** Friends track group costs in messy chat threads.
  - **Stack:** Telegram bot, SQLite · **Difficulty:** 🟢 Beginner · **Prior art:** [python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

- **Meeting Room No-Show Releaser**: Frees booked meeting rooms when nobody checks in within ten minutes of the start.
  - **Why:** Ghost bookings make rooms unavailable all day.
  - **Stack:** Google Calendar or Microsoft Graph API, check-in page · **Difficulty:** 🟢 Beginner

- **Customer Support Handoff Bot**: A WhatsApp bot that answers FAQs and hands off to a human with context when stuck.
  - **Why:** Small businesses drown in repetitive WhatsApp questions.
  - **Stack:** WhatsApp Cloud API, Node.js · **Difficulty:** 🟡 Intermediate

## Data sync & integration

- **Two-Way Calendar Sync**: Sync busy blocks between work and personal calendars with privacy-preserving titles.
  - **Why:** Double-booking across calendars is common.
  - **Stack:** Python, Google/Microsoft Graph APIs · **Difficulty:** 🟡 Intermediate

- **Notion or Airtable to Postgres Mirror**: Mirror no-code databases into Postgres for SQL and BI access.
  - **Why:** No-code tools lack proper querying.
  - **Stack:** Python, platform APIs, incremental sync · **Difficulty:** 🟡 Intermediate

- **Contact Deduplicator Across Services**: Merge duplicate contacts across Google, phone and CRM with review.
  - **Why:** Duplicate contacts cause embarrassing mistakes.
  - **Stack:** Python, fuzzy matching, APIs · **Difficulty:** 🟢 Beginner

- **Git-Backed Config Sync**: Sync SaaS settings (DNS records, feature flags, alerts) to a git repo and apply changes from PRs.
  - **Why:** Manual config changes are unreviewed and unreversible.
  - **Stack:** Go, provider APIs, GitHub Actions · **Difficulty:** 🟡 Intermediate

- **File Sync with Transform Rules**: Sync folders between cloud providers, converting formats and renaming on the way.
  - **Why:** Moving files between services is repetitive.
  - **Stack:** rclone, rules config · **Difficulty:** 🟢 Beginner · **Prior art:** [rclone/rclone](https://github.com/rclone/rclone)

- **Unified Notifications API**: One API call sends to push, email, SMS or chat depending on user preferences.
  - **Why:** Every app rebuilds notification routing.
  - **Stack:** Go or Python, Apprise · **Difficulty:** 🟢 Beginner · **Prior art:** [caronc/apprise](https://github.com/caronc/apprise)

- **Shopify to Accounting Reconciliation**: Matches Shopify payouts to orders, fees and refunds and posts journal entries.
  - **Why:** Reconciling marketplace payouts by hand is a monthly nightmare.
  - **Stack:** Python, Shopify and Xero APIs · **Difficulty:** 🟡 Intermediate

- **Google Sheets to Static Site**: Publishes a Google Sheet as a searchable static site that rebuilds on change.
  - **Why:** Non-developers maintain data in sheets but want a nice public page.
  - **Stack:** Google Sheets API, Astro, GitHub Actions · **Difficulty:** 🟢 Beginner

- **CRM to Newsletter Segment Sync**: Keeps newsletter segments in sync with CRM fields like plan, region and lifecycle stage.
  - **Why:** Segments drift and customers get the wrong emails.
  - **Stack:** Node.js, CRM and newsletter APIs · **Difficulty:** 🟢 Beginner

- **Bidirectional Task Sync**: Syncs tasks between a personal to-do app and a team tracker with conflict rules.
  - **Why:** People track the same work in two places.
  - **Stack:** TypeScript, task app APIs, sync state DB · **Difficulty:** 🔴 Advanced

- **Accounting Ledger Migration Tool**: Migrates years of transactions, contacts and invoices between accounting platforms with validation reports.
  - **Why:** Switching accounting software is so painful that businesses stay on tools they hate.
  - **Stack:** Python, accounting APIs, reconciliation reports · **Difficulty:** 🔴 Advanced
