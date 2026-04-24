---
icon: google-drive
---

# CLAUDE.md vs rules/ ⭐⭐

One of the easiest ways to make .**claude/** folder inefficient is to put too much into **CLAUDE.md**.

At the beginning, that file usually works well because the project is still small. You add a few commands, some coding conventions, and maybe a short note about architecture. But once the codebase grows, **CLAUDE.md** often turns into a catch-all document for everything the team wants Claude to remember. That is when it starts losing clarity.

A better structure is to treat **CLAUDE.md** as the **project’s operating guide**, not its entire knowledge base.

**CLAUDE.md** should hold the instructions Claude needs across most sessions:

* What the project is
* How it is organized
* Which commands matter most
* What conventions apply broadly
* What constraints should Claude not miss

The **rules/** folder is where more specific guidance belongs. That includes instructions tied to a certain part of the codebase, a certain workflow, or a certain engineering concern like testing or security.

A simple way to think about it is this:

* **CLAUDE.md** holds **global guidance**
* **rules/** holds **specialized guidance**

That split makes the structure easier to maintain and easier to scale.

#### A practical example <a href="#e7c3" id="e7c3"></a>

Imagine you are working on a product with three main areas:

* a Next.js frontend
* a FastAPI backend
* a data pipeline for reporting jobs

If you try to describe everything in **CLAUDE.md**, the file becomes noisy very quickly. Frontend conventions sit next to backend validation rules and data pipeline notes. Claude gets more context, but not always better context.

**A cleaner setup would look like this:**

```
your-project/
├── CLAUDE.md
└── .claude/
    └── rules/
        ├── frontend.md
        ├── backend-api.md
        ├── testing.md
        └── data-pipelines.md
```

In this setup:

* **CLAUDE.md:** explains the product at a high-level
* **frontend.md:** focuses on UI conventions
* **backend-api.md:** focuses on API behavior and validation rules
* **testing.md:** explains how tests should be written and run
* **data-pipelines.md**: captures conventions for batch jobs and scheduled tasks

That is much easier to maintain than one large instruction file.

#### What should stay in `CLAUDE.md?` <a href="#af55" id="af55"></a>

A good **CLAUDE.md** usually includes:

* The main stack
* The high-level architecture
* The most important development commands
* Broad code conventions
* Important project-wide warnings or constraints

Here is a short example for a FastAPI project:

```
# Project: Customer Insights AP

## Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pytest

## Structure
- `app/api/` contains route definitions
- `app/services/` contains business logic
- `app/models/` contains ORM models
- `app/schemas/` contains request and response schemas

## Commands
- `pytest` runs the test suite
- `alembic upgrade head` applies migrations
- `ruff check .` runs linting
- `ruff format .` formats the code

## Conventions
- Validate all request bodies with Pydantic schemas
- Keep route handlers thin; business logic belongs in services
- Do not expose internal exception details in API responses
```

This is useful because it gives Claude a reliable starting point without drowning it in detail.

#### What should move into `rules/?` <a href="#id-3525" id="id-3525"></a>

Once instructions become narrow or area-specific, move them out of **CLAUDE.md**.

For example, **backend-api.md** might contain rules like these:

```
# Backend API Rules

- Every new endpoint must include request and response schemas
- Use dependency injection for database sessions
- Return paginated results for collection endpoints
- Log external API failures with the shared logger
- Prefer service-layer functions over logic inside route files
```

And **frontend.md** might say:

```
# Frontend Rules

- Prefer server components unless client interactivity is required
- Keep UI state local unless it is shared across pages
- Reuse design system components before creating new ones
- Put page-specific components beside their route when possible
```

Now each file has a clear purpose.

#### When `rules/` becomes the better choice <a href="#id-0dd9" id="id-0dd9"></a>

You should usually split into **rules/** when:

* **CLAUDE.md** starts feeling crowded
* Different parts of the repo need different guidance
* Different people have different standards
* The team updates conventions often
* You want to scope instructions to specific paths or concerns

This is where modularity starts paying off. Instead of editing one big document every time, you update only the file that matches the problem.

Press enter or click to view image in full size

<figure><img src="https://miro.medium.com/v2/resize:fit:1400/1*_I9C0ZB-jaLCKGkIrip2PA.png" alt="" height="428" width="700"><figcaption></figcaption></figure>

This diagram helps the reader see that **CLAUDE.md** is the central layer, while **rules/** breaks out detailed guidance into smaller units.
