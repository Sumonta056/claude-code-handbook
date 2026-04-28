---
icon: plug-circle-plus
cover: ../.gitbook/assets/Claude.png
coverY: 0
coverHeight: 344
layout:
  width: default
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
---

# Master Claude.md!

{% hint style="info" %}
NT: CLAUDE.md should be under 200 lines per file
{% endhint %}

If you have started using Claude Code, you have already know about `CLAUDE.md`.

It sits at the root of your project. Claude reads it automatically at the start of every single session. No prompting required, no manual passing of context. It just loads.

"I treat it like a README. I open a blank file, dump everything I can think of, feel good about how thorough it looks, and then wonder why Claude still uses npm instead of pnpm, still puts test files in the wrong folder, and still forgets to run the migration after editing the schema."\
\
The problem is not quantity. It is signal quality.

This guide is everything I have learned about writing a `CLAUDE.md` that actually works, backed by what the Claude Code team recommends, what real developers report after months of daily use, and the practical patterns that separate a file that helps from a file that just takes up space.

***

### First, Why This File Matters So Much?

<mark style="color:$warning;">**Claude Code is stateless**</mark><mark style="color:$warning;">.</mark> Every session starts from zero. Claude does not remember your last conversation, your project decisions, your tech stack, or what you told it last Tuesday.

The only exception is what you put in `CLAUDE.md`.

Think of it this way: Claude is a very capable new engineer who joins your team fresh every single morning. No memory of yesterday. No context from last week. Brilliant, fast, but starting completely blank. <mark style="color:$success;">**`CLAUDE.md`**</mark><mark style="color:$success;">**&#x20;**</mark><mark style="color:$success;">**is your onboarding doc for that engineer.**</mark> The better the doc, the less time you spend repeating yourself and correcting the same mistakes.

There is also a hard limit worth understanding. Research shows that frontier LLMs can reliably follow roughly 150 to 200 instructions. Claude Code’s own system prompt already uses around 50 of those slots before your file even loads. That means your `CLAUDE.md` has maybe 100 to 150 reliable instruction slots. Every unnecessary line you add eats into that budget and dilutes the instructions that actually matter.

Short, accurate, and specific vs long, comprehensive, and vague. Every time.

***

### What Goes In: The Four Must-Have Categories

When you write `CLAUDE.md` for the first time, the goal is not to document everything about your project. The goal is to communicate the facts that, if missing, will cause Claude to get things wrong in ways that waste your time.

<mark style="color:$warning;">A useful question to ask yourself: what would a new engineer misunderstand or get wrong in their first week here? That is what belongs in this file.</mark>

There are four categories worth prioritizing on day one.

#### 1. Common Commands

Build, test, lint, local dev server. Write them down exactly. If your test command has a specific flag that matters, include it verbatim. Claude will use it as written.

```md
## Commands
- `pnpm dev`: Start development server (port 3000)
- `pnpm test`: Run Jest tests
- `pnpm test -- --runInBand`: Run tests in sequence (use this in CI)
- `pnpm lint`: ESLint check
- `pnpm db:migrate`: Run Prisma migrations after schema changes
```

Do not make Claude guess the package manager. If you use `pnpm` and you do not say so, Claude will use `npm`. Every time. Because that is what most projects use.

> Example: I want a quick format and lint check whenever Claude generates code. Instead of repeating the instruction every time, we just add this rule via a command in `Claude.md`.

#### 2. Project-Specific Constraints and Pitfalls

These are the invisible landmines. The things that are not obvious from reading the code but will cause a mess if Claude gets them wrong.

```md
## Important Rules
- NEVER edit files in /generated, these are auto-built
- The users table uses soft deletes, never use hard DELETE
- All API calls to /payments must go through the PaymentService middleware
- Product images live in Cloudinary, not locally
- NEVER commit .env files
```

Every time you catch yourself correcting Claude for the same mistake twice, that correction belongs here.&#x20;

> The pattern is: correction happens once, you fix it yourself. It happens twice, you write it down.

#### 3. Architecture Context

What each directory does, what the layering rules are, what “shared” means in your codebase. Especially critical in monorepos where there are multiple apps, packages, and services.

```md
## Architecture
- `/app`: Next.js App Router pages and layouts
- `/components/ui`: Reusable UI components only, no business logic
- `/lib`: Utilities and shared logic
- `/services`: Domain services, these are the only files that touch the DB directly
- `/prisma`: Schema and migrations
```

Without this, Claude will make plausible-looking architectural decisions that violate your actual boundaries. It has no way to know your layering rules unless you tell it.

> One thing I suggest (and I normally do) instead of writing any architectural decision directly in the Claude.MD file is to create a.doc folder and keep that architectural documentation, requirements, and planning in that file and just map it in the Claude.md

{% code overflow="wrap" expandable="true" %}
```markdown
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_DESIGN.md
│   ├── DATABASE_SCHEMA.md
│   └── DEPLOYMENT.md
├── Claude.md
└── src/
```
{% endcode %}

{% code title="CLAUDE.md" overflow="wrap" expandable="true" %}
```markdown
# Project Overview

## Architecture & Design Decisions
See [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) for:
- System design & component structure
- Tech stack rationale
- Scalability approach

## API Specification
See [`docs/API_DESIGN.md`](./docs/API_DESIGN.md) for:
- Endpoint definitions
- Request/response schemas
- Authentication flow

## Database Design
See [`docs/DATABASE_SCHEMA.md`](./docs/DATABASE_SCHEMA.md) for:
- Entity relationships
- Indexing strategy
- Migration approach

## Deployment & DevOps
See [`docs/DEPLOYMENT.md`](./docs/DEPLOYMENT.md) for:
- Infrastructure setup
- CI/CD pipeline
- Environment configuration
```
{% endcode %}

**Benefits:**

* Claude.md stays as a **navigation hub** (quick scan)
* Deep dives live in separate docs (version-controllable, searchable)
* Easy to link from code comments: `// See docs/ARCHITECTURE.md#Components`
* Scales well as project grows
* Helps to keep Claude.md concise, short and more accurate!

#### 4. The Baseline Workflow

Branch naming, PR requirements, pre-commit checks. One or two sentences is enough.

```md
## Workflow
- Branch names: feature/*, fix/*, chore/*
- Run typecheck and lint before committing
- Every PR needs at least one unit test for new logic
```

For example, in my project, I have specific conventions for branch naming and commit messages. Instead of manually checking file to remember everything, I just added a rule for these conventions. You can also add other workflow rules like this, such as formatting, unit testing, validation checks, etc.

{% code title="Claude.md" overflow="wrap" expandable="true" %}
````markdown
### Formatting & Linting
- **Run before commit:**
```bash
  npm run lint:fix
  ./gradlew checkstyleMain
```

### Code Formats
-  commit message: `TASK-ID: feat(scope): description`
- Branch Naming Pattern
  - Format: `feat/TASK-ID-short-description`
  - Struture: `<type>/<TASK-ID>-<short-description>`
  - Lowercase, hyphens only && Keep description ≤ 3 words

````
{% endcode %}

{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}

### A Complete Real-World Example

Here is what a solid `CLAUDE.md` looks like for a Next.js project. Clean, specific :

{% code title="CLAUDE.md" overflow="wrap" lineNumbers="true" %}
````markdown
# Project: ShopFront

E-commerce app with App Router, Stripe payments, and Prisma ORM.

## Stack
- Backend: Node.js 20 + Express + Prisma + TypeScript
- Databases: PostgreSQL (primary) + MongoDB (metadata) + OpenSearch (search)
- Frontend: Nuxt 3 + Vue 3
- DevOps: Docker + GitHub Actions + AWS (S3, EC2, RDS)
- TypeScript strict mode & Tailwind CSS for styling (no custom CSS files)

## 1. Common Commands

Use exactly as written. Do not substitute package managers. Use `pnpm` only. Never use npm or yarn.

```bash
pnpm dev                 # Local dev server (port 8080)
pnpm test                # Run Jest tests
pnpm lint:fix            # Auto-fix ESLint issues
pnpm db:migrate          # Apply Prisma migrations
pnpm build               # Production build
```

## 2. Important Rules & Constraints & Common Mistakes

- NEVER hard DELETE. All deletes are soft via `deleted_at` timestamp. Always include `where: { deleted_at: null }` in queries.
- Media files live in AWS S3, never locally. Use `MediaService.uploadToS3()`.
- NEVER edit `/generated`. Auto-generated by build scripts. Fix source and rebuild.
- NEVER commit `.env` files.
- All `/payments/*` API calls must route through `src/services/PaymentService.ts`.
- Use OpenSearch via SearchService. Do not query OpenSearch directly.
- Use Gateway in production. External API calls go through Gatewau (port 8001).
- No Hardcoded env vars | Use `process.env.VAR_NAME`

### Architecture Boundaries

- `/components/ui`: Reusable UI components only. No business logic.
- `/services`: Domain logic & external API ownership (Auth, Payment, Search, Media).
- `/lib/utils`: Pure utility functions only. No side effects.
- `/api`: Thin wrappers around services.

## 3. Reference Architecture & Design Decisions

- See `docs/ARCHITECTURE.md` for system design & component structure.
- See `docs/API_DESIGN.md` for REST endpoints & authentication flow.
- See `docs/DATABASE_SCHEMA.md` for entity relationships & indexing.

## 4. Git Workflow

- See `docs/CONVENTIONS.md` for full workflow and CI/CD, Docker & environment setup..

Branch naming: `feat/TASK-ID-short-description`
Example : feat/PROJ-123-user-auth

Commit messages: `TASK-ID: type(scope): description`
Example : PROJ-123: feat(auth): add JWT refresh token

Before pushing: [MUST DO]
```bash
pnpm lint:fix && pnpm typecheck && pnpm test:ci
```

## Code Style
- Named exports only, no default exports
- No `any` types
- Destructure imports where possible

Expected: Server on `http://localhost:8080`, DB connected, OpenSearch ready.
````
{% endcode %}

Notice what is not in there. No project description. No badges. No motivation or philosophy. No aspirational guidelines like “we value clean code.” Just the things Claude needs to not make mistakes.

***

### What to Remove?

This part is underrated. Some things actively make `CLAUDE.md` worse by taking up instruction budget without adding value.

* **Rules already enforced by tooling.** If `.eslintrc`, `.prettierrc`, or `tsconfig.json` handles a rule, do not restate it in prose. Claude can read config files. Duplicating creates drift: eventually your `CLAUDE.md` says one thing and the config says another.
* **Aspirational guidelines.** “We value clean, readable code” or “prefer simple solutions.” These are not actionable. They do not help Claude make a specific decision. Cut them.
* **Standard README content.** Project description, badges, license info, contributor setup instructions. That content exists for humans browsing GitHub, not for Claude’s context window.
* **Stale documentation.** An outdated architecture description or deprecated workflow is worse than nothing, because Claude will follow it confidently. If you are not certain something is still accurate, delete it or fix it before adding it.

***

### The Instruction Budget Problem (And Why Your File Might Already Be Too Long)

This is the thing most developers do not know about.

LLMs do not selectively ignore instructions that are too far down the file. When the instruction count gets too high, instruction-following quality drops uniformly across the entire file. Not just the ones at the bottom. All of them.

The practical implication: a bloated `CLAUDE.md` does not just fail on the extra rules. It starts failing on the important rules too.

The test for every line in your file: would Claude make a mistake without this? If the answer is no, or even “probably not,” cut it. The official guidance from the Claude Code team is to keep it under 300 lines, and shorter is better. Many experienced users keep it under 100 lines by moving detailed content to imported files.

{% hint style="danger" %}
A real signal that your file is too long: Claude asks you something that is clearly answered in `CLAUDE.md`. When that happens, the file is likely either too long, too vague, or both.
{% endhint %}

***

### Extend Claude.md! Use @imports to Keep It Lean

Once your root file starts exceeding 60 to 80 lines, it is time to split.

Claude Code supports `@imports`, which let you reference other files:

```md
# Project: ShopFront

See @README.md for project overview.
See @package.json for available scripts.
See @docs/testing.md for testing conventions.
See @docs/api-guidelines.md for API design rules.
See @docs/auth-flow.md for authentication patterns.
```

The root file stays focused on commands, constraints, and architecture. The detail lives in separate files that Claude loads when they are referenced.

What is worth extracting first:

* Testing conventions
* API design rules
* CI/CD pipeline steps
* Auth patterns
* Deployment procedures

These are the sections that grow fastest and benefit most from being isolated. Keep the four must-have categories in the root. Everything else can be a reference.

Imports can be recursive too. A file you import can import other files. Use this sparingly or you end up with a maze of references that becomes its own maintenance problem.

***

### Monorepos Need a <mark style="color:$warning;">Different Structure!</mark>

A single root `CLAUDE.md` does not scale well in a monorepo. Service-specific rules mixed with global rules become a maintenance headache fast. Someone updates the API service’s deploy process and now the frontend’s context has a paragraph about something completely irrelevant.

The structure that works:

```markdown
CLAUDE.md                        # global constraints only
packages/api/CLAUDE.md           # api-specific rules
packages/web/CLAUDE.md           # web-specific rules
docs/auth-patterns.md            # shared, imported by both
docs/error-handling.md           # shared conventions
```

The root file covers: repo-wide commands, shared tooling config, cross-service constraints, and a brief layout so Claude knows what lives where.

Each package file covers: that service’s own commands, its database notes, its deploy process, anything service-specific.

Shared conventions that multiple services follow go in `docs/` and get imported wherever needed.

Claude Code also supports a `.claude/rules/` directory for larger projects. Any markdown file you drop in `.claude/rules/` gets loaded automatically with the same priority as your main `CLAUDE.md`. No imports needed. This is useful for team environments where different people own different rule sets.

```
your-project/
├── .claude/
│   ├── CLAUDE.md
│   └── rules/
│       ├── code-style.md
│       ├── testing.md
│       └── security.md
```

***

### Where CLAUDE.md Lives: The Four Locations

Most developers only know about the project root. But there are actually four places you can put `CLAUDE.md`, and each one has a different scope.

Location Scope Use Case `~/.claude/CLAUDE.md` All sessions, all projects Personal preferences, global tools `./CLAUDE.md` (project root) This project only, shared via git Project rules for the whole team Parent directories Monorepo-wide Rules that apply across packages Child directories That directory only, loaded on demand Specific module conventions

The home folder version is powerful for personal preferences you want everywhere. For example: your preferred language for responses, your formatting preferences, or tools you always want available.

```md
# ~/.claude/CLAUDE.md

## Personal Preferences
- Respond in concise, direct language
- For TypeScript projects, always use strict mode
- When suggesting commands, use pnpm unless the project specifies otherwise
```

***

### CLAUDE.md Is a <mark style="color:$success;">Living Document, Not a Setup Task</mark>

Most developers write `CLAUDE.md` once during project setup and never touch it again. That is how it becomes stale and harmful.

The right mental model is: `CLAUDE.md` is a code file. It should be reviewed in PRs, updated when what it describes changes, and pruned when things become outdated.

A few habits that keep it honest:

* **Update in the same PR where you change what it describes.** If you migrate from `yarn` to `pnpm`, the command update and the `CLAUDE.md` update should be in the same commit. Treat it like any other tracked file.
* **Delete stale content aggressively.** It is tempting to keep old rules “just in case.” Do not. If something no longer reflects how the project works, remove it. A shorter accurate file beats a longer partially-wrong one.
* **Do a quarterly pass.** Once every few months, read through and ask: is each item still true? Is it still actionable? Could it be said in fewer words?
* **Let Claude’s questions tell you what’s missing.** If Claude asks something about your project that should have been obvious, that is a signal to add it to the file. The questions are a feedback loop.

***

### Two Bonus Features Worth Knowing

The `/init` Command

If you are starting from scratch, run `/init` inside Claude Code. It analyzes your codebase, detects build systems, test frameworks, and directory structure, and generates a starter `CLAUDE.md`.

The output tends to be bloated. Treat it as a draft, not a finished file. Read through it, remove anything that does not meet the “would Claude make a mistake without this?” test, and add whatever it missed. Starting from a generated draft is faster than starting from blank, but the draft needs editing.

The `/reflection` Command

At the end of a session, run `/reflection`. Claude Code will review what happened in the session and surface lessons that should probably be written into `CLAUDE.md` as permanent rules.

This is how you close the loop. Instead of manually translating corrections into rules, you let the tool do it. Run it at the end of any session where you caught Claude making a repeatable mistake. Then decide whether the suggested rule is worth adding.

***

### The WHAT, WHY, HOW Framework

When you are not sure what to write, use this framework to check whether you have covered the right things.

* **WHAT:** What is the tech stack? What is the project structure? Give Claude a map. Which directories are which? What are the apps, what are the shared packages, and what is each one for?
* **WHY:** What is the purpose of the project? What is each part doing and why? Context about intent helps Claude make better decisions when it encounters ambiguous situations.
* **HOW:** How should Claude work on this project? `bun` instead of `node`? `pnpm` instead of `npm`? How does Claude verify its changes? How does it run tests, typechecks, and compilation steps?

Every good `CLAUDE.md` covers all three. Most files cover WHAT but skip WHY and only partially cover HOW. That is where the gaps show up in practice.

***

#### Workflow Orchestration

Here are different segment, you can add in your claude.md. Like I use the 1 & 3 in my claude.md

{% code title="" overflow="wrap" lineNumbers="true" %}
```
## Workflow Orchestration

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `.claude/rules/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `.claude/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `.claude/todo.md` 
6. **Capture Lessons**: Update `.claude/rules/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.
```
{% endcode %}

***

#### Tips for Token Efficient!

Add this rules in Claude.md. This repository says : [https://github.com/drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient). Just adding this reduce huge token in every request - response!

{% code title="" overflow="wrap" lineNumbers="true" %}
```
## Approach
- Read existing files before writing. Don't re-read unless changed.
- Thorough in reasoning, concise in output.
- Skip files over 100KB unless required.
- No sycophantic openers or closing fluff.
- No emojis or em-dashes.
- Do not guess APIs, versions, flags, commit SHAs, or package names. Verify by reading code or docs before asserting.
```
{% endcode %}

> Must visit this repository to try out different profiles for different cases&#x20;

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### Summary

`CLAUDE.md` is not documentation. It is collaboration infrastructure.

Its value is not that it covers everything. Its value is that it communicates the most important facts about your project as clearly as possible, so Claude can do its best work without you repeating yourself session after session.

The one-line version: document what Claude gets wrong, not everything Claude needs to know.

Start small. Stay accurate. Add rules when Claude makes a mistake, not before. And treat the file like code, because that is exactly what it is.

***

_Written for Weekly’s Byte. If you found this useful, share it with one person who just started using Claude Code. See you next week._

{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}
