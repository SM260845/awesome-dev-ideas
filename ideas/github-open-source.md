# GitHub & Open Source Ecosystem

> **Scope:** GitHub Actions and Apps, maintainer and contributor tooling, repo health, community and OSS sustainability.

87 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Maintainer relief](#maintainer-relief)
- [Supply chain & CI hardening](#supply-chain--ci-hardening)
- [Docs & repo health](#docs--repo-health)
- [Community & discovery](#community--discovery)
- [Automation & GitHub Apps](#automation--github-apps)
- [Sustainability & governance](#sustainability--governance)
- [Data & insight on repos](#data--insight-on-repos)

## Maintainer relief

- **PR Triage Card**: Action that posts a card on external PRs: CONTRIBUTING compliance, linked issue, tests touched, size, risky paths, then labels it.
  - **Why:** Maintainers face floods of low-effort and AI-generated PRs; a rules-first filter saves review time.
  - **Stack:** TypeScript Action, Octokit, YAML config · **Difficulty:** 🟡 Intermediate · **Prior art:** [mitchellh/vouch](https://github.com/mitchellh/vouch)

- **Newcomer Path**: When an issue is labelled "good first issue", post a start-here comment with likely files, test commands and a mentor.
  - **Why:** Maintainers lack time to mentor; prepared issues convert newcomers into contributors.
  - **Stack:** TypeScript Action, tree-sitter search, optional LLM · **Difficulty:** 🟡 Intermediate · **Prior art:** [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners)

- **FlakeTag**: Learn flaky tests from rerun history and comment "known flaky, not your fault" on PRs, with a weekly quarantine issue.
  - **Why:** First-time contributors get blamed for red CI they didn't cause.
  - **Stack:** TypeScript Action, JUnit/CTRF parsing, cache storage · **Difficulty:** 🟡 Intermediate · **Prior art:** [ctrf-io/github-test-reporter](https://github.com/ctrf-io/github-test-reporter)

- **Stale Issue Summariser**: Before closing stale issues, post a summary of the discussion, workarounds and the reason for closing.
  - **Why:** Auto-close bots feel hostile; a summary preserves value for future readers.
  - **Stack:** Action, LLM summary, GitHub API · **Difficulty:** 🟢 Beginner · **Prior art:** [actions/stale](https://github.com/actions/stale)

- **Maintainer Load Dashboard**: Show review load, response times and open-PR age per maintainer to rebalance work.
  - **Why:** Burnout starts with invisible, uneven review load.
  - **Stack:** Next.js, GitHub GraphQL, charts · **Difficulty:** 🟡 Intermediate

- **Saved Replies Library**: Shared, versioned saved replies for a project's common answers, inserted via a slash command in comments.
  - **Why:** Maintainers type the same explanations hundreds of times.
  - **Stack:** GitHub App, YAML reply files · **Difficulty:** 🟢 Beginner

- **Issue Form Quality Checker**: Detect issues that skipped required template fields and ask for the missing info politely.
  - **Why:** Incomplete bug reports cost multiple back-and-forth rounds.
  - **Stack:** Action, issue forms schema · **Difficulty:** 🟢 Beginner

- **Contributor Recognition Digest**: Monthly auto-generated post thanking contributors, including non-code work like triage and docs.
  - **Why:** Recognition keeps volunteers engaged; non-code work is usually invisible.
  - **Stack:** Action, GitHub API, Markdown · **Difficulty:** 🟢 Beginner · **Prior art:** [all-contributors/allcontributors.org](https://github.com/all-contributors/allcontributors.org)

- **Duplicate Issue Nudge**: Comments on new issues with the three most similar open or closed issues before a maintainer looks.
  - **Why:** Maintainers spend hours closing duplicates by hand.
  - **Stack:** GitHub Action, embeddings · **Difficulty:** 🟢 Beginner

- **Needs-Reproduction Label Bot**: Asks for a minimal reproduction on bug reports without one and closes them politely after a set time.
  - **Why:** Unreproducible bug reports clog issue trackers.
  - **Stack:** GitHub Action, issue form parsing · **Difficulty:** 🟢 Beginner

- **Maintainer Vacation Mode**: Sets an auto-reply on new issues and PRs while you're away and hands urgent ones to a backup.
  - **Why:** Maintainers feel they can never take a break.
  - **Stack:** GitHub App, config file · **Difficulty:** 🟢 Beginner

- **First-Time Contributor Welcome Kit**: Greets first-time contributors with repo-specific setup tips and a checklist tailored to their PR.
  - **Why:** First contributions often stall on avoidable setup problems.
  - **Stack:** GitHub Action, templates · **Difficulty:** 🟢 Beginner

- **Monorepo Split Mirror**: Mirrors subdirectories of a monorepo into read-only repos with history, redirecting issues back to the source.
  - **Why:** Users want to star, watch and vendor individual packages from big monorepos.
  - **Stack:** Go, git filter-repo, GitHub API · **Difficulty:** 🔴 Advanced · **Prior art:** [newren/git-filter-repo](https://github.com/newren/git-filter-repo)

- **Low-Effort PR Filter**: Flags PRs that only touch whitespace, README typos in bulk or match known spam patterns.
  - **Why:** Hacktoberfest-style spam floods popular repos every year.
  - **Stack:** GitHub Action, heuristics · **Difficulty:** 🟡 Intermediate

## Supply chain & CI hardening

- **PinPR**: Opens one PR that pins actions to SHAs, adds least-privilege permissions and fixes risky triggers, explaining each change.
  - **Why:** Compromised tags on popular actions have leaked secrets from thousands of repos.
  - **Stack:** App/Action, zizmor, YAML AST editing · **Difficulty:** 🟡 Intermediate · **Prior art:** [zizmorcore/zizmor](https://github.com/zizmorcore/zizmor)

- **DepLens**: Comment on Dependabot/Renovate PRs whether changed or vulnerable symbols are reachable from your code.
  - **Why:** Most dependency alerts are unreachable noise, so real ones get ignored.
  - **Stack:** TypeScript/Python, OSV data, tree-sitter call search · **Difficulty:** 🔴 Advanced · **Prior art:** [google/osv-scanner](https://github.com/google/osv-scanner)

- **Workflow Permission Minimiser**: Infer the minimal `permissions:` block for each workflow from the actions and API calls it uses.
  - **Why:** Default token permissions are wider than most workflows need.
  - **Stack:** Go, action metadata, GitHub API · **Difficulty:** 🟡 Intermediate

- **Action Update Explainer**: For each action version bump, summarise what changed upstream and flag new network or permission usage.
  - **Why:** Blindly merging action updates is a supply-chain risk.
  - **Stack:** Action, GitHub Releases API, diff analysis · **Difficulty:** 🟡 Intermediate

- **Secrets Usage Map**: Map which workflows and environments use which secrets, and flag unused or overly broad ones.
  - **Why:** Secret sprawl in orgs makes rotation and audits painful.
  - **Stack:** Go, GitHub API, graph output · **Difficulty:** 🟡 Intermediate

- **Release Provenance Badge**: Action that attests build provenance for releases and adds a verifiable README badge.
  - **Why:** Users increasingly check that binaries were built from the source they see.
  - **Stack:** Actions, Sigstore, SLSA attestations · **Difficulty:** 🟡 Intermediate · **Prior art:** [slsa-framework/slsa-github-generator](https://github.com/slsa-framework/slsa-github-generator)

- **Workflow Trigger Auditor**: Flags risky triggers like pull_request_target combined with checkout of untrusted code.
  - **Why:** This combination is a well-known path to repository compromise.
  - **Stack:** Python, workflow YAML parser · **Difficulty:** 🟢 Beginner · **Prior art:** [zizmorcore/zizmor](https://github.com/zizmorcore/zizmor)

- **Self-Hosted Runner Hygiene Checker**: Checks self-hosted runners for persistent state between jobs and public-repo exposure.
  - **Why:** Persistent runners on public repos let attackers linger between jobs.
  - **Stack:** Go, runner API, host checks · **Difficulty:** 🟡 Intermediate

- **Signed Commit Adoption Tracker**: Shows what share of commits in an org are signed and nudges contributors with setup guides.
  - **Why:** Commit signing only works if adoption is high.
  - **Stack:** GitHub API, dashboard · **Difficulty:** 🟢 Beginner

- **CI Cache Poisoning Checker**: Detects workflows where untrusted PRs can write to caches that trusted jobs later restore.
  - **Why:** Cache poisoning is a subtle but real supply-chain attack path.
  - **Stack:** Python, workflow analysis · **Difficulty:** 🔴 Advanced

## Docs & repo health

- **DocDrift**: Flag README and docs lines a PR just made wrong (removed flags, renamed env vars, dead functions) as inline comments.
  - **Why:** Outdated docs are one of the most common complaints in open source.
  - **Stack:** Action, diff parsing, grep with context · **Difficulty:** 🟡 Intermediate

- **README Code Block Runner**: Execute README code blocks in CI and fail when examples break.
  - **Why:** Broken quickstart examples are the first thing new users hit.
  - **Stack:** Action, Markdown parser, sandboxed runners · **Difficulty:** 🟡 Intermediate · **Prior art:** [nschloe/pytest-codeblocks](https://github.com/nschloe/pytest-codeblocks)

- **Repo2Reel**: Turn a PR or repo into a short narrated architecture video with diagrams linked to `file:line`.
  - **Why:** Reviewers and newcomers get a 60-second mental model before reading code.
  - **Stack:** TypeScript, diagram generation, HTML-to-video, local TTS · **Difficulty:** 🔴 Advanced · **Prior art:** [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

- **Architecture Delta Comment**: Post a diagram on each PR showing which components and dependencies changed.
  - **Why:** Maintainers can judge scope instantly without reading every file.
  - **Stack:** Action, import graph, Mermaid · **Difficulty:** 🟡 Intermediate · **Prior art:** [ahmedkhaleel2004/gitdiagram](https://github.com/ahmedkhaleel2004/gitdiagram)

- **CONTRIBUTING Generator from Repo**: Generate a CONTRIBUTING.md from detected tooling: setup, test, lint and release commands.
  - **Why:** Many repos have no contributor guide because writing one is tedious.
  - **Stack:** CLI, file detection rules, templates · **Difficulty:** 🟢 Beginner

- **Repo Onboarding Score**: Score how fast a newcomer can get from clone to passing tests, by actually running it in a container.
  - **Why:** Measures real onboarding friction instead of checklist compliance.
  - **Stack:** Action, Docker, timing report · **Difficulty:** 🟡 Intermediate

- **Link Rot Sweeper for Wikis**: Scan a repo's wiki and docs for dead links and open one PR with archived replacements.
  - **Why:** Docs accumulate dead links that frustrate readers.
  - **Stack:** Action, lychee, Wayback Machine API · **Difficulty:** 🟢 Beginner · **Prior art:** [lycheeverse/lychee](https://github.com/lycheeverse/lychee)

- **Closed Issue Archaeology Search**: Full-text search across closed issues, PR threads and discussions with code-aware ranking.
  - **Why:** Answers are buried in old closed threads that GitHub search ranks poorly.
  - **Stack:** Python, GitHub GraphQL API, SQLite FTS · **Difficulty:** 🟢 Beginner

- **Badge Cleanup Bot**: Finds broken, redundant or misleading README badges and proposes a trimmed set.
  - **Why:** Badge walls with dead services make projects look abandoned.
  - **Stack:** GitHub Action, HTTP checks · **Difficulty:** 🟢 Beginner

- **Docs Coverage for Public APIs**: Reports which exported functions lack docs and fails CI when coverage drops.
  - **Why:** Undocumented APIs drive support questions.
  - **Stack:** TypeScript or Python analysis, CI comment · **Difficulty:** 🟢 Beginner

- **Topic Tag Suggester**: Suggests GitHub topics for a repo from its README, dependencies and similar popular repos.
  - **Why:** Repos without topics are nearly invisible in GitHub search.
  - **Stack:** GitHub Action, GitHub API · **Difficulty:** 🟢 Beginner

- **Translated README Sync Checker**: Detects when translated READMEs fall behind the English version and lists missing sections.
  - **Why:** Translations silently go stale.
  - **Stack:** Python, Markdown section diff · **Difficulty:** 🟡 Intermediate

## Community & discovery

- **Repo Star History with Events**: Chart stars over time annotated with releases, HN posts and blog mentions.
  - **Why:** Maintainers want to know what actually drove growth.
  - **Stack:** Next.js, GitHub API, HN Algolia API · **Difficulty:** 🟡 Intermediate · **Prior art:** [star-history/star-history](https://github.com/star-history/star-history)

- **Dependents Explorer**: Show who depends on your package, ranked by their own popularity and activity.
  - **Why:** Helps maintainers find users to consult before breaking changes.
  - **Stack:** Python, dependency graph data, web UI · **Difficulty:** 🟡 Intermediate

- **Awesome List Health Checker**: Check an awesome list for dead links, archived repos and stale projects, and open a cleanup PR.
  - **Why:** Curated lists decay quickly without maintenance.
  - **Stack:** Action, GitHub API, lychee · **Difficulty:** 🟢 Beginner · **Prior art:** [sindresorhus/awesome](https://github.com/sindresorhus/awesome)

- **Good First Issue Feed per Stack**: Personalised feed of prepared beginner issues matching a user's languages and past contributions.
  - **Why:** Newcomers struggle to find issues that match their skills.
  - **Stack:** Next.js, GitHub search API · **Difficulty:** 🟡 Intermediate · **Prior art:** [DeepSourceCorp/good-first-issue](https://github.com/DeepSourceCorp/good-first-issue)

- **Discussion to FAQ**: Convert answered GitHub Discussions into a maintained FAQ page in the docs.
  - **Why:** The same questions get asked repeatedly.
  - **Stack:** Action, GraphQL API, Markdown · **Difficulty:** 🟢 Beginner

- **Project Bus Factor Report**: Estimate knowledge concentration per directory from commit and review history.
  - **Why:** Identifies areas where one departure would stall a project.
  - **Stack:** Python, git log mining, charts · **Difficulty:** 🟡 Intermediate

- **Open Source Changelog Newsletter**: Weekly digest of release notes from repos a user stars, grouped and summarised.
  - **Why:** Users miss important releases and breaking changes.
  - **Stack:** Python, GitHub API, email · **Difficulty:** 🟢 Beginner

- **Profile README Widgets that Don't Break**: Self-hosted profile stats cards cached on your own infra, resilient to public-instance rate limits.
  - **Why:** Public stats-card instances regularly hit rate limits.
  - **Stack:** Vercel functions, GitHub GraphQL, SVG · **Difficulty:** 🟢 Beginner · **Prior art:** [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats)

- **Similar Repos Finder**: Suggests repos similar to one you like by topics, dependencies and contributors.
  - **Why:** Discovering alternatives or complementary tools is hard on GitHub.
  - **Stack:** Python, GitHub API, embeddings · **Difficulty:** 🟡 Intermediate

- **Maintainer Office Hours Scheduler**: Lets maintainers publish office-hour slots that contributors can book, linked to issues.
  - **Why:** Real-time help speeds up contributions but is hard to organise.
  - **Stack:** Cal.com-style booking, GitHub OAuth · **Difficulty:** 🟢 Beginner

- **Contributor Map**: A world map of a project's contributors from public profile locations with opt-out.
  - **Why:** Shows a project's global community at a glance.
  - **Stack:** GitHub API, geocoding, MapLibre · **Difficulty:** 🟢 Beginner

- **Contribution Event Readiness Checker**: Checks a repo for labelled starter issues, contribution docs and CI speed before contribution events.
  - **Why:** Event traffic overwhelms repos that aren't ready for it.
  - **Stack:** GitHub Action, GitHub API · **Difficulty:** 🟢 Beginner

- **Open Source Mentorship Matcher**: Matches new contributors with volunteer mentors by language, timezone and project.
  - **Why:** Newcomers need guidance that maintainers can't personally give.
  - **Stack:** Next.js, GitHub OAuth, Postgres · **Difficulty:** 🟡 Intermediate

## Automation & GitHub Apps

- **Label Sync Across an Org**: Declare labels once and sync names, colours and descriptions to every repo.
  - **Why:** Inconsistent labels break cross-repo search and automation.
  - **Stack:** Action, YAML, GitHub API · **Difficulty:** 🟢 Beginner

- **Issue Linker by Similarity**: Suggest related closed issues and PRs when a new issue is opened, with links rather than auto-closing.
  - **Why:** Surfaces prior fixes without the frustration of false duplicate closures.
  - **Stack:** App, embeddings, GitHub API · **Difficulty:** 🟡 Intermediate

- **PR Size Nudger**: Comment when a PR exceeds a size threshold with a suggested split by directory.
  - **Why:** Large PRs get slower and worse reviews.
  - **Stack:** Action, diff stats · **Difficulty:** 🟢 Beginner

- **Required Reviewers by Risk**: Assign reviewers based on risky paths (auth, billing, CI) rather than static CODEOWNERS alone.
  - **Why:** Sensitive changes deserve expert review; trivial ones don't.
  - **Stack:** App, path rules, GitHub API · **Difficulty:** 🟡 Intermediate

- **Merge Queue Simulator**: Estimate how a merge queue would change throughput using your historic PRs and CI times.
  - **Why:** Teams hesitate to adopt merge queues without data.
  - **Stack:** Python, GitHub API, simulation · **Difficulty:** 🔴 Advanced

- **Actions Minutes Attribution**: Break down Actions minutes by workflow, job and trigger to find waste.
  - **Why:** CI costs creep through a few expensive jobs.
  - **Stack:** Python, GitHub API, dashboard · **Difficulty:** 🟢 Beginner

- **Cross-Repo Refactor Campaign Tool**: Apply a codemod across many repos, open PRs and track their merge status on one board.
  - **Why:** Org-wide changes (e.g. runtime upgrades) stall on coordination.
  - **Stack:** Go, GitHub API, codemods · **Difficulty:** 🔴 Advanced

- **Backport Bot**: Comment `/backport v2` to cherry-pick a merged PR onto release branches and open PRs.
  - **Why:** Maintaining release branches by hand is error-prone.
  - **Stack:** App, git, GitHub API · **Difficulty:** 🟡 Intermediate

- **Issue Deadline Reminder**: Nudge assignees about issues tied to a milestone that's due, with a summary for maintainers.
  - **Why:** Milestones slip silently.
  - **Stack:** Action, cron, GitHub API · **Difficulty:** 🟢 Beginner

- **Label-Based Issue Router**: Routes issues to team boards and chat channels based on labels and paths mentioned.
  - **Why:** Big repos need issues to reach the right team fast.
  - **Stack:** GitHub App, config YAML · **Difficulty:** 🟢 Beginner

- **PR Description Checker**: Ensures PR descriptions fill required sections like testing notes and linked issues.
  - **Why:** Empty PR descriptions slow reviews.
  - **Stack:** GitHub Action · **Difficulty:** 🟢 Beginner

- **Auto-Changelog Fragments**: Asks each PR to add a changelog fragment and assembles them at release time.
  - **Why:** Changelogs written at release time miss things.
  - **Stack:** GitHub Action, towncrier-style fragments · **Difficulty:** 🟡 Intermediate · **Prior art:** [twisted/towncrier](https://github.com/twisted/towncrier)

- **Milestone Progress Reporter**: Posts weekly milestone progress with burndown and at-risk issues to a discussion.
  - **Why:** Community projects lack visibility into release progress.
  - **Stack:** GitHub Action, GraphQL API · **Difficulty:** 🟡 Intermediate

- **Cross-Fork CI Status Board**: Shows CI status of downstream forks against upstream changes before release.
  - **Why:** Maintainers break forks and dependents without knowing.
  - **Stack:** GitHub API, dashboard · **Difficulty:** 🔴 Advanced

## Sustainability & governance

- **Funding Readiness Checker**: Check a repo for FUNDING.yml, a governance doc, a security policy and roadmap, and suggest what's missing.
  - **Why:** Funders and companies look for these before sponsoring.
  - **Stack:** Action, file checks, report · **Difficulty:** 🟢 Beginner

- **Sponsor Impact Page**: Generate a page showing what sponsorship money funded, from linked issues and milestones.
  - **Why:** Transparent spending encourages recurring sponsorship.
  - **Stack:** Static site, GitHub API · **Difficulty:** 🟢 Beginner

- **License Compatibility Checker**: Check a project's dependency licences against its own licence and flag conflicts.
  - **Why:** Licence conflicts are discovered late, often by lawyers.
  - **Stack:** Go, SPDX data, lockfile parsers · **Difficulty:** 🟡 Intermediate · **Prior art:** [licensee/licensee](https://github.com/licensee/licensee)

- **Governance Template Kit**: Templates and a CLI for GOVERNANCE.md, MAINTAINERS.md and decision records sized for small projects.
  - **Why:** Projects outgrow "one maintainer decides" without a transition plan.
  - **Stack:** Markdown templates, CLI · **Difficulty:** 🟢 Beginner

- **Maintainer Handoff Checklist**: Guided process to transfer or archive a project: secrets, registries, domains, CI and notices.
  - **Why:** Abandoned projects often have dangling registries and domains that become attack vectors.
  - **Stack:** CLI, checklists, GitHub API · **Difficulty:** 🟢 Beginner

- **AI Contribution Policy Generator**: Generate an AI-usage and disclosure policy for a repo, with a matching PR template checkbox.
  - **Why:** Projects are setting rules for AI-assisted PRs and need clear wording.
  - **Stack:** Markdown templates, CLI · **Difficulty:** 🟢 Beginner

- **OSS Usage Telemetry Alternative**: Privacy-respecting, opt-in install counts derived from registry and release download stats.
  - **Why:** Maintainers want usage data without adding telemetry to their tools.
  - **Stack:** Python, registry APIs, dashboard · **Difficulty:** 🟡 Intermediate

- **Maintainer Burnout Signals**: Tracks review load, off-hours activity and response pressure to warn before burnout.
  - **Why:** Burnout is the top reason projects die.
  - **Stack:** GitHub API, dashboard · **Difficulty:** 🟡 Intermediate

- **Grant Opportunity Finder for OSS**: Matches projects to open-source grants and funds by domain, licence and country.
  - **Why:** Maintainers don't know which funds they qualify for.
  - **Stack:** Web app, curated grant database · **Difficulty:** 🟢 Beginner

- **Contributor Licence Agreement Lite**: A DCO sign-off checker with friendly fix instructions instead of legal CLAs.
  - **Why:** CLAs deter contributors; DCO is lighter but checks are unfriendly.
  - **Stack:** GitHub Action · **Difficulty:** 🟢 Beginner

- **Project Succession Registry**: A registry where maintainers list projects seeking new owners with context and handover docs.
  - **Why:** Abandoned projects need adopters, and adopters need to find them.
  - **Stack:** Static site, GitHub issues as database · **Difficulty:** 🟡 Intermediate

- **Commercial Use Survey Kit**: A privacy-respecting survey and landing page to learn which companies depend on your project.
  - **Why:** Funding asks work better with evidence of commercial use.
  - **Stack:** Static site, form backend · **Difficulty:** 🟢 Beginner

## Data & insight on repos

- **Repo Activity Heatmap**: Show which files change together and which change most, to find coupling and hotspots.
  - **Why:** Hotspots predict bugs and refactoring priority.
  - **Stack:** Python, git log, D3 · **Difficulty:** 🟡 Intermediate

- **Review Latency Report**: Weekly report of time-to-first-review and time-to-merge with outliers highlighted.
  - **Why:** Slow reviews are the main bottleneck for most teams.
  - **Stack:** Action, GitHub API, Markdown · **Difficulty:** 🟢 Beginner

- **Test Coverage Trend Comment**: Comment coverage change per PR and per touched file, without a third-party service.
  - **Why:** Coverage tools often require SaaS accounts.
  - **Stack:** Action, coverage parsers, cache storage · **Difficulty:** 🟢 Beginner

- **Commit Message Quality Coach**: Suggest clearer commit messages using conventional-commit rules and the diff, as a local hook.
  - **Why:** Good history makes bisect, changelogs and review easier.
  - **Stack:** Hook, rule engine, optional local LLM · **Difficulty:** 🟢 Beginner

- **Fork Network Explorer**: Find the most active forks of a repo and summarise what each changed.
  - **Why:** Useful when upstream is abandoned but forks carry fixes.
  - **Stack:** Python, GitHub API, compare API · **Difficulty:** 🟡 Intermediate

- **CODEOWNERS Coverage Checker**: Report unowned paths, owners without write access and rules shadowed by later rules.
  - **Why:** Broken CODEOWNERS silently routes reviews to nobody.
  - **Stack:** Action, CODEOWNERS parser, GitHub API · **Difficulty:** 🟢 Beginner

- **Template Repo Sync**: Propagate updates from a template repository to every repo created from it, as reviewable PRs.
  - **Why:** Repos created from templates never receive later fixes.
  - **Stack:** App, git merge, GitHub API · **Difficulty:** 🟡 Intermediate

- **Issue Response Time SLA Tracker**: Measures time to first response on issues and PRs against a published target.
  - **Why:** Communities trust projects that respond predictably.
  - **Stack:** GitHub Action, GraphQL API · **Difficulty:** 🟡 Intermediate

- **Dependency Popularity Ranking in Your Org**: Ranks the most-used external packages across an org's repos.
  - **Why:** Knowing what you depend on most guides security and sponsorship.
  - **Stack:** Python, GitHub API, lockfile parsers · **Difficulty:** 🟡 Intermediate

- **Contributor Retention Curves**: Shows how many first-time contributors return for a second and third contribution.
  - **Why:** Retention says more about community health than star counts.
  - **Stack:** Python, GitHub API, charts · **Difficulty:** 🟡 Intermediate

- **Language and Framework Drift Report**: Shows how the language mix of an org's repos changes over time.
  - **Why:** Platform teams need to see which stacks they actually support.
  - **Stack:** GitHub API, linguist data, charts · **Difficulty:** 🔴 Advanced

- **Churn Hotspot Map**: Combines change frequency and complexity to find files that deserve refactoring.
  - **Why:** Hotspots predict bugs better than complexity alone.
  - **Stack:** git log, complexity metrics, treemap · **Difficulty:** 🔴 Advanced
