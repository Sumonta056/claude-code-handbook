---
icon: fishing-rod
---

# The role of hooks/

The **hooks/** folder is where you place scripts that run automatically at specific points in Claude’s workflow.

These files are not general documentation. They are operational scripts. Their job is usually one of three things:

* Prevent risky actions
* Clean up or validate Claude’s output
* Enforce a workflow requirement

A clean structure might look like this:

```
.claude/
├── settings.json
├── hooks/
│   ├── block-dangerous-commands.sh
│   ├── format-edits.sh
│   └── run-tests-before-stop.sh
└── commands/
    ├── review-pr.md
    ├── write-tests.md
    └── summarize-changes.md
```

In this setup:

* **block-dangerous-commands.sh** is a safety hook
* **format-edits.sh** keeps file changes clean
* **run-tests-before-stop.sh** checks quality before Claude finishes

That is much easier to understand than dropping all three scripts into **.claude/** without a folder.

#### A practical hook example <a href="#id-3d9a" id="id-3d9a"></a>

Imagine you are working in a Python service where every Claude edit should be formatted automatically.

Your workflow might use:

* **ruff format .** for formatting
* **ruff check .** for linting

A good structure would place the formatting logic in a dedicated script:

```
#!/usr/bin/env bash
jq -r '.tool_input.file_path' | xargs ruff format
```

And that script would live here:

```
.claude/
└── hooks/
    └── format-edits.sh
```

The important point is structural: even if the hook is small, it should still live in **hooks/,** because that folder tells your team exactly what kind of file it is.
