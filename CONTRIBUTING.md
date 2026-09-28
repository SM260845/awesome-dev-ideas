# Contributing

Thanks for helping. This list values **specific, real and useful** over long. One excellent idea beats five vague ones.

## Ways to contribute

- [Suggest an idea](https://github.com/SM260845/awesome-dev-ideas/issues/new?template=suggest-an-idea.yml) through the issue form.
- Open a pull request that adds, improves or removes entries.
- Report a dead link, an archived prior-art repo or an idea that already exists.

## Where does it go?

Each file in [`ideas/`](ideas/) opens with a one-line **Scope**. Put an idea in the single category whose scope fits best. Don't add the same idea to two categories. If it's AI security, it goes in Security & Privacy; if it's a GitHub Action, it goes in GitHub & Open Source Ecosystem; if you'd import it into a codebase, it goes in Dev Ideas.

## Entry format

Add entries under the best-fitting sub-header, using exactly this shape:

```markdown
- **Title**: One-line pitch (what it does).
  - **Why:** Why it's valuable and who needs it (one sentence).
  - **Stack:** Suggested stack · **Difficulty:** 🟡 Intermediate · **Prior art:** [owner/repo](https://github.com/owner/repo)
```

- **Title:** short and descriptive, Title Case, unique across the whole repo.
- **Difficulty:** one of `🟢 Beginner`, `🟡 Intermediate`, `🔴 Advanced` (see the legend in the [README](README.md#entry-format-and-legend)).
- **Prior art:** optional. Only include it if you opened the link, it loads (HTTP 200), and it really is related. Prefer active projects; don't link archived repos as prior art.

### Fork Suggestions format

```markdown
- **[owner/repo](https://github.com/owner/repo)**: One-line description of what it is.
  - **Fork idea:** The specific change: a new niche, a missing feature, a port or a revival.
  - **Why:** Why the fork is worth it.
  - **Licence:** SPDX ID · **Stars (YYYY-MM-DD):** ~12.3k · **Difficulty:** 🟡 Intermediate
```

Rules for forks:

- The repo must exist and have a licence. Get the licence and star count from the API, not from memory, and put the date you checked in the Stars label:
  `gh api repos/OWNER/REPO --jq '[.license.spdx_id, .stargazers_count, .archived] | @tsv'`
- No archived repos unless the idea is to revive it (start the fork idea with "Revive").
- Don't claim a project is abandoned or slow unless you checked the latest commit or release date and state it.

## Quality bar

An idea is accepted when it is:

- **Specific:** someone could start building it tomorrow. "An AI app" is not an idea; "an MCP server that exposes read-only Postgres with row limits" is.
- **Valuable:** it names a real pain and who has it.
- **Honest:** no invented repos, stars, statistics or quotes. If you can't verify it, leave it out.
- **Not filler:** classic builds (todo apps, calculators) belong only in Learning Projects, and only with a twist that teaches something.
- **Concise:** one line each for pitch, why and stack.

## No duplicates

CI runs `python3 scripts/check_duplicates.py`, which fails on duplicate or near-duplicate titles across all files and duplicate fork repos, and warns on very similar pitches. Search the repo before adding an idea. If yours overlaps an existing one, improve that entry instead.

## Link verification

- CI runs [lychee](https://github.com/lycheeverse/lychee) on every Markdown file, on pull requests and weekly.
- Before opening a PR, check your links locally: `lychee --config lychee.toml "**/*.md"`.
- Replace or remove links that redirect to something unrelated, return errors or point to archived projects.

## Counts

Every category must keep at least 50 entries. After editing, run:

```bash
python3 scripts/count_entries.py --write
```

This updates the counts table and badge in the README. CI fails if the counts are stale or a category drops below 50.

## Pull request checklist

- [ ] Entries follow the format and sit in the right category and sub-header.
- [ ] `python3 scripts/check_duplicates.py` passes.
- [ ] `python3 scripts/count_entries.py --write` has been run.
- [ ] `npx markdownlint-cli2 "**/*.md"` passes.
- [ ] Every new link was opened and checked.

By contributing, you agree to release your contribution under [CC0 1.0](LICENSE).
