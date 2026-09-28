# Security & Privacy

> **Scope:** AI and agent security, supply chain, secrets, AppSec, cloud hardening, privacy tools and detection.

52 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [AI & agent security](#ai--agent-security)
- [Supply chain](#supply-chain)
- [Secrets & identity](#secrets--identity)
- [AppSec & testing](#appsec--testing)
- [Infrastructure & cloud](#infrastructure--cloud)
- [Privacy tools](#privacy-tools)
- [Detection & response](#detection--response)

## AI & agent security

- **AgentGate**: Local proxy that intercepts package installs run by coding agents and blocks typosquats, brand-new or known-malicious packages, with an audit log.
  - **Why:** Agents install dependencies unattended; supply-chain attacks target exactly that.
  - **Stack:** Go, registry proxy, OSV data, harness hooks · **Difficulty:** 🟡 Intermediate

- **Skill and Plugin Scanner**: Scan agent skills and plugins for prompt injection, hidden instructions, exfiltration commands and obfuscated scripts.
  - **Why:** Skills are shared in one line and executed with the agent's full permissions.
  - **Stack:** Python, static rules, LLM classifier · **Difficulty:** 🟡 Intermediate · **Prior art:** [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)

- **MCP Server Permission Manifest**: A manifest format and checker that declares what an MCP server can touch (network, files, secrets) and enforces it at runtime.
  - **Why:** Users install MCP servers without knowing what they can access.
  - **Stack:** TypeScript, sandboxing, JSON Schema · **Difficulty:** 🔴 Advanced

- **Prompt Injection Test Corpus Runner**: Run a curated corpus of indirect prompt-injection payloads (web pages, PDFs, issues) against your agent and score leaks.
  - **Why:** Agents that browse or read issues are exposed to injected instructions.
  - **Stack:** Python, test harness, canary tokens · **Difficulty:** 🟡 Intermediate · **Prior art:** [NVIDIA/garak](https://github.com/NVIDIA/garak)

- **Canary Tokens for Agents**: Plant fake secrets and files in agent workspaces and alert when an agent reads or sends them.
  - **Why:** Detects exfiltration by compromised tools or injected prompts.
  - **Stack:** Go, file watchers, webhook alerts · **Difficulty:** 🟢 Beginner

- **Agent Egress Firewall**: Per-agent network allowlists enforced by a local proxy, with a log of every domain contacted.
  - **Why:** Limits the damage of prompt injection and malicious dependencies.
  - **Stack:** Go, HTTP CONNECT proxy, DNS filtering · **Difficulty:** 🟡 Intermediate

- **Tool Call Approval Policy Engine**: Declarative rules for auto-approving, asking or denying agent tool calls based on command, path and repo.
  - **Why:** Constant approval prompts cause fatigue, which leads to approving everything.
  - **Stack:** Rust or Go, policy DSL, harness hooks · **Difficulty:** 🟡 Intermediate · **Prior art:** [open-policy-agent/opa](https://github.com/open-policy-agent/opa)

- **LLM App Red-Team Playbook**: Scripted attacks (jailbreaks, data extraction, tool abuse) with pass/fail criteria for your specific app.
  - **Why:** Most LLM apps ship without adversarial testing.
  - **Stack:** Python, PyRIT or promptfoo, CI · **Difficulty:** 🟡 Intermediate · **Prior art:** [microsoft/PyRIT](https://github.com/microsoft/PyRIT)

- **Model Provenance Checker**: Verify downloaded model files against publisher hashes and model cards, and refuse unsafe formats before loading.
  - **Why:** Models are pulled from hubs with little verification.
  - **Stack:** Python, safetensors, hub APIs · **Difficulty:** 🟡 Intermediate · **Prior art:** [protectai/modelscan](https://github.com/protectai/modelscan)

- **PII Redaction Proxy for LLM APIs**: Proxy that redacts personal data before prompts leave the network and restores it in responses.
  - **Why:** Companies want LLM features without sending customer data to vendors.
  - **Stack:** Python, Presidio, reverse proxy · **Difficulty:** 🟡 Intermediate · **Prior art:** [data-privacy-stack/presidio](https://github.com/data-privacy-stack/presidio)

## Supply chain

- **Package Age Gate**: Block installing package versions younger than N days unless explicitly allowed.
  - **Why:** Many malicious versions are caught within days; a cooldown avoids them.
  - **Stack:** Node/Python shims, registry metadata · **Difficulty:** 🟢 Beginner

- **Install Script Sandbox**: Run npm/pip install scripts in a sandbox and report file, network and process activity.
  - **Why:** Install scripts are a common malware vector.
  - **Stack:** Go, bubblewrap or containers, strace · **Difficulty:** 🔴 Advanced

- **Dependency Diff Reviewer**: Show what actually changed in a dependency's published package between versions, including binaries and minified code.
  - **Why:** Source repos and published packages can differ.
  - **Stack:** Python, registry tarballs, diff viewer · **Difficulty:** 🟡 Intermediate

- **SBOM Diff on PRs**: Generate SBOMs for base and head and comment on new, removed and changed components.
  - **Why:** Makes dependency changes explicit in review.
  - **Stack:** Action, Syft, CycloneDX · **Difficulty:** 🟢 Beginner · **Prior art:** [anchore/syft](https://github.com/anchore/syft)

- **Abandoned Dependency Detector**: Flag dependencies with no maintainer activity, expired domains or transferred ownership.
  - **Why:** Account takeovers of abandoned packages are a recurring attack.
  - **Stack:** Python, registry APIs, WHOIS · **Difficulty:** 🟡 Intermediate

- **Lockfile Integrity Checker**: Verify lockfile hashes and registry sources haven't been tampered with in a PR.
  - **Why:** Lockfile injection hides malicious sources in large diffs.
  - **Stack:** Go, lockfile parsers, Action · **Difficulty:** 🟡 Intermediate

- **Reproducible Build Verifier**: Rebuild a released artifact in CI and compare hashes with the published one.
  - **Why:** Proves the published binary matches the source.
  - **Stack:** Docker, diffoscope, Actions · **Difficulty:** 🔴 Advanced · **Prior art:** [sigstore/cosign](https://github.com/sigstore/cosign)

## Secrets & identity

- **Secret Rotation Runbook Automator**: Detect a leaked secret and walk through revoking and rotating it across the providers that use it.
  - **Why:** Finding a leak is easy; rotating everywhere is the hard part.
  - **Stack:** Python, provider APIs, checklists · **Difficulty:** 🟡 Intermediate · **Prior art:** [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)

- **Secrets in Agent Transcripts Scanner**: Scan agent session logs and chat exports for secrets pasted into prompts and flag them for rotation.
  - **Why:** Developers paste keys into agent chats that are stored in plain text.
  - **Stack:** Go, secret detectors, transcript parsers · **Difficulty:** 🟢 Beginner · **Prior art:** [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)

- **Short-Lived Credentials for Local Dev**: Replace long-lived cloud keys on laptops with short-lived credentials issued via SSO.
  - **Why:** Stolen laptop credentials are a top breach cause.
  - **Stack:** Go, OIDC, cloud STS · **Difficulty:** 🔴 Advanced

- **Agent-Safe Secret Injection**: Give commands real secrets at run time while the agent only ever sees placeholders.
  - **Why:** Agents read .env files and can leak their contents into logs or prompts.
  - **Stack:** Go or Rust, exec wrapper, OS keychain · **Difficulty:** 🟡 Intermediate · **Prior art:** [getsops/sops](https://github.com/getsops/sops)

- **SSH Key Inventory**: Audit SSH keys across servers and GitHub accounts: owners, age, algorithm and last use.
  - **Why:** Old keys of departed staff linger for years.
  - **Stack:** Go, SSH, GitHub API · **Difficulty:** 🟡 Intermediate

- **Passkey Demo App**: Minimal app showing passkey registration, login, recovery and account linking done correctly.
  - **Why:** Many developers still avoid passkeys because examples are incomplete.
  - **Stack:** TypeScript, WebAuthn library, Postgres · **Difficulty:** 🟡 Intermediate

- **OAuth Scope Auditor**: List third-party apps connected to your Google/GitHub/Slack org with scopes and last use.
  - **Why:** Over-scoped forgotten integrations are a quiet risk.
  - **Stack:** Python, admin APIs, report · **Difficulty:** 🟡 Intermediate

## AppSec & testing

- **Authorisation Test Generator**: Generate tests that check every API route against every role for broken access control.
  - **Why:** Broken access control is the top web risk in OWASP rankings.
  - **Stack:** Python or TypeScript, OpenAPI, test runner · **Difficulty:** 🟡 Intermediate

- **IDOR Fuzzer**: Replay recorded API calls with swapped object IDs across user sessions to find insecure direct object references.
  - **Why:** IDORs are common and easy to miss in review.
  - **Stack:** Python, mitmproxy, session management · **Difficulty:** 🟡 Intermediate · **Prior art:** [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)

- **Security Headers Fixer**: Scan a site's headers and output exact config snippets for Nginx, Caddy, Vercel or Cloudflare.
  - **Why:** Knowing what's missing is easy; writing correct config is not.
  - **Stack:** TypeScript, header rules, templates · **Difficulty:** 🟢 Beginner

- **Semgrep Rule Pack for One Framework**: Well-tested custom rules for a framework's common security mistakes.
  - **Why:** Generic rules miss framework-specific pitfalls.
  - **Stack:** Semgrep, test fixtures · **Difficulty:** 🟡 Intermediate · **Prior art:** [semgrep/semgrep](https://github.com/semgrep/semgrep)

- **Dependency Confusion Checker**: Check if internal package names are unclaimed on public registries.
  - **Why:** Unclaimed internal names allow dependency-confusion attacks.
  - **Stack:** Python, registry APIs · **Difficulty:** 🟢 Beginner

- **SSRF Test Harness**: A local target that detects outbound requests to metadata IPs and internal hosts during tests.
  - **Why:** SSRF is common in URL-fetching features, including AI "fetch this URL" tools.
  - **Stack:** Go, DNS rebinding tests · **Difficulty:** 🟡 Intermediate

- **Threat Model Diff on PRs**: Flag PRs that add new external calls, data stores or trust boundaries and prompt for a threat model update.
  - **Why:** Threat models go stale as soon as the architecture changes.
  - **Stack:** Python, static analysis, GitHub Action · **Difficulty:** 🟡 Intermediate · **Prior art:** [OWASP/pytm](https://github.com/OWASP/pytm)

- **Webhook Signature Verification Library**: One small library that verifies signed webhooks from major providers with constant-time checks and replay protection.
  - **Why:** Webhook handlers often skip signature or timestamp checks.
  - **Stack:** TypeScript and Python packages, test vectors · **Difficulty:** 🟢 Beginner

## Infrastructure & cloud

- **Public Bucket Finder for Your Org**: Enumerate your cloud storage and flag public or cross-account access with a fix command.
  - **Why:** Public buckets remain a common source of leaks.
  - **Stack:** Python, cloud SDKs · **Difficulty:** 🟢 Beginner

- **IAM Least-Privilege Suggester**: Compare granted IAM permissions with those actually used in logs and propose a tighter policy.
  - **Why:** Over-privileged roles amplify breaches.
  - **Stack:** Python, CloudTrail, policy generation · **Difficulty:** 🔴 Advanced

- **Kubernetes Admission Policy Starter**: A curated set of admission policies with tests and a report-only rollout mode.
  - **Why:** Teams want guardrails without breaking deployments on day one.
  - **Stack:** Kyverno or OPA Gatekeeper, Helm · **Difficulty:** 🟡 Intermediate · **Prior art:** [kyverno/kyverno](https://github.com/kyverno/kyverno)

- **Exposed Services Monitor**: Scan your own IP ranges and domains weekly and alert on newly exposed ports or admin panels.
  - **Why:** Shadow services appear without anyone noticing.
  - **Stack:** Go, nmap or naabu, notifications · **Difficulty:** 🟡 Intermediate · **Prior art:** [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)

- **TLS Certificate Expiry Watcher**: Track certificate expiry across domains and internal services with calendar and chat alerts.
  - **Why:** Expired certificates still cause major outages.
  - **Stack:** Go, crt.sh, cron · **Difficulty:** 🟢 Beginner

- **Container Runtime Anomaly Alerts**: Alert on unexpected processes, shells or network connections inside production containers.
  - **Why:** Detects compromised containers early.
  - **Stack:** eBPF, Falco rules · **Difficulty:** 🔴 Advanced · **Prior art:** [falcosecurity/falco](https://github.com/falcosecurity/falco)

## Privacy tools

- **Tracker Audit for Your Site**: Crawl your own site and list every third-party request, cookie and fingerprinting script per page.
  - **Why:** Compliance teams need an accurate inventory.
  - **Stack:** Playwright, HAR analysis, report · **Difficulty:** 🟢 Beginner

- **Data Deletion Request Tracker**: Track GDPR/CCPA deletion requests sent to companies with deadlines and templated follow-ups.
  - **Why:** Individuals lose track of dozens of requests.
  - **Stack:** Web app, SQLite, email templates · **Difficulty:** 🟢 Beginner

- **Local-First Password Breach Checker**: Check passwords against breach corpora using k-anonymity without sending full hashes.
  - **Why:** Users want breach checks without trusting a website with passwords.
  - **Stack:** CLI, Have I Been Pwned range API · **Difficulty:** 🟢 Beginner

- **EXIF and Metadata Scrubber**: Strip location and device metadata from photos and documents in bulk, with a before/after report.
  - **Why:** Shared files leak location and identity.
  - **Stack:** Rust or Python, exiftool · **Difficulty:** 🟢 Beginner

- **Privacy Policy Diff Watcher**: Monitor services' privacy policies and summarise material changes.
  - **Why:** Policy changes are buried in long documents.
  - **Stack:** Python, change detection, diff · **Difficulty:** 🟢 Beginner · **Prior art:** [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io)

- **Consent Log Service**: Store verifiable, append-only consent records for cookies and marketing opt-ins.
  - **Why:** Regulators ask for proof of consent.
  - **Stack:** Go, Postgres, hash chains · **Difficulty:** 🟡 Intermediate

- **Email Alias Manager**: Self-hosted email aliases per service with forwarding and one-click disable.
  - **Why:** Limits spam and reveals which service leaked your address.
  - **Stack:** Go, Postfix, web UI · **Difficulty:** 🟡 Intermediate · **Prior art:** [simple-login/app](https://github.com/simple-login/app)

- **Browser Extension Permission Auditor**: List installed browser extensions with their permissions, recent ownership changes and update history.
  - **Why:** Popular extensions get sold and turned into spyware.
  - **Stack:** TypeScript, Chrome Web Store data, CLI · **Difficulty:** 🟡 Intermediate

## Detection & response

- **Homelab SIEM Starter**: Collect auth, firewall and container logs into one searchable place with starter alerts.
  - **Why:** Small setups have logs everywhere and alerts nowhere.
  - **Stack:** Vector, Loki or OpenSearch, Grafana · **Difficulty:** 🟡 Intermediate · **Prior art:** [wazuh/wazuh](https://github.com/wazuh/wazuh)

- **GitHub Audit Log Alerts**: Stream org audit logs and alert on risky events: new deploy keys, branch protection changes, secret access.
  - **Why:** Org compromises often start with quiet setting changes.
  - **Stack:** Python, GitHub audit log API, webhooks · **Difficulty:** 🟡 Intermediate

- **Phishing Link Detonator**: Open suspicious links in an isolated browser and report redirects, forms and downloads.
  - **Why:** Safe triage of reported phishing without risking a workstation.
  - **Stack:** Playwright, containers, screenshots · **Difficulty:** 🟡 Intermediate

- **Incident Timeline Builder**: Merge logs, chat and alerts into one incident timeline for postmortems.
  - **Why:** Postmortems waste hours reconstructing what happened.
  - **Stack:** Python, log parsers, web UI · **Difficulty:** 🟡 Intermediate

- **MCP Honeypot Server**: A decoy MCP server that logs which clients and prompts try to misuse its tools.
  - **Why:** Early warning and research data on attacks against agent tooling.
  - **Stack:** TypeScript, MCP SDK, logging · **Difficulty:** 🟡 Intermediate

- **Security Changelog for Your Stack**: Daily digest of advisories affecting only the packages and images you actually run.
  - **Why:** Generic advisory feeds are too noisy to read.
  - **Stack:** Python, OSV API, SBOMs · **Difficulty:** 🟢 Beginner · **Prior art:** [google/osv-scanner](https://github.com/google/osv-scanner)
