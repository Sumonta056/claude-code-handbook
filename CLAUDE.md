# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a GitBook-based documentation handbook for mastering Claude Code. All content is Markdown. There is no build system, test runner, or linter the only tooling is Git and GitBook's bi-directional sync with GitHub.

## Content Structure

```
SUMMARY.md              # GitBook table of contents — register every new page here
README.md               # Landing page (About section)
getting-started/        # Onboarding content
basics/                 # Core Claude Code concepts (CLAUDE.md, Skills, Agents, MCP, settings, commands, plugins)
resources/              # Advanced topics and curated external links
.claude/                # Template files (ARCHITECTURE.md, SPEC.md) — not GitBook content
.gitbook/assets/        # Images and media referenced in docs
```

## Authoring Rules

- **Every new `.md` file must be registered in `SUMMARY.md`** under the correct section, or GitBook will not render it.
- File names use kebab-case. Match the naming convention of adjacent files in the same directory.
- Internal links use relative paths (e.g., `../basics/integrations.md`).
- Images go in `.gitbook/assets/` and are referenced as `![](.gitbook/assets/filename.png)`.

## Commit Format

```
<type>(<scope>): <short summary>
```

**Types:** `docs`, `chore`, `fix`, `feat`
**Scope:** section name — `basics`, `getting-started`, `resources`, or `root`

Examples:
```
docs(basics): add MCP server setup guide
docs(getting-started): update quickstart roadmap
fix(root): correct broken internal link in SUMMARY.md
chore(root): register new page in SUMMARY.md
```

- Summary is lowercase, imperative mood, no period.
- Keep subject line under 72 characters.

## GitBook Sync

Commits pushed to `main` are automatically synced to GitBook. GitBook edits create automatic commits with messages like `GITBOOK-N: No subject`. Do not rewrite or squash these commits.
