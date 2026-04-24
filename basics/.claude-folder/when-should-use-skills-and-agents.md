---
icon: wirsindhandwerk
---

# When should use skills/ & agents/?

Once the core of your **.claude/** folder is organized, the next question is whether you need more specialized capabilities.

> This is where **skills/** and **agents/** come in.

These two folders are useful, but they should not be the starting point for most projects. They make sense when your team has recurring workflows that are complex enough to deserve their own structure. If **CLAUDE.md**, **rules/**, **hooks/**, and **commands/** already cover most of your needs, that is a good sign. It means your setup is still simple and efficient.

You add **skills/** and **agents/** when you want Claude to handle more specialized work in a cleaner, more reusable way.

#### What belongs in `skills/ Folder?` <a href="#id-1706" id="id-1706"></a>

A skill is best thought of as a packaged capability. It is useful when a workflow has:

* A clear purpose
* A repeatable process
* Supporting files or detailed guidance
* Enough complexity that a short command file is no longer enough

That is why **skills/** usually work best as a folder of self-contained directories rather than loose files. A clean structure looks like this:

```
.claude/
└── skills/
    ├── api-review/
    │   ├── SKILL.md
    │   └── checklist.md
    ├── release-prep/
    │   ├── SKILL.md
    │   └── release-template.md
    └── docs-audit/
        ├── SKILL.md
        └── style-guide.md
```

This is efficient because each skill has its own home. The logic, description, and supporting files stay together.

#### A practical skill example <a href="#id-7706" id="id-7706"></a>

Imagine your team regularly prepares releases. That workflow involves:

* Checking recent changes
* Reviewing version notes
* Drafting a release summary
* Confirming whether migrations or breaking changes exist

That is more than a quick reusable prompt. It is a repeatable process with context. So instead of storing everything in **commands/**, you package it like this:

```
.claude/
└── skills/
    └── release-prep/
        ├── SKILL.md
        └── release-template.md
```

The **SKILL.md** defines what the skill is for, and **release-template.md** gives Claude a reusable output structure. That is much cleaner than scattering release instructions across multiple command files.

#### When should a workflow stay a command instead? <a href="#id-4de0" id="id-4de0"></a>

This distinction matters for structure. A command is usually enough when the task is:

* Short
* Direct
* Mostly prompt-driven
* Easy to express in one file

A skill makes more sense when the task:

* Has several steps
* Needs companion documents
* Is important enough to standardize more carefully
* Will be reused over time

A simple way to think about it:

* **commands/** = lightweight reusable tasks
* **skills/** = packaged workflows with more depth

#### What belongs in `agents/ folder?` <a href="#f4cc" id="f4cc"></a>

The **agents/** folder is for specialized subagents. These are useful when you want a narrower, role-based persona for a certain kind of work. Instead of using the same general Claude setup for every task, you define focused roles such as:

* Code reviewer
* Security auditor
* Documentation editor
* Migration checker
* Performance reviewer

A clean structure looks like this:

```
.claude/
└── agents/
    ├── code-reviewer.md
    ├── security-auditor.md
    ├── docs-writer.md
    └── performance-checker.md
```

This works well because each agent file has a single, clear purpose.

#### A practical agent example <a href="#id-9ac9" id="id-9ac9"></a>

Suppose your team often asks Claude to review API changes for correctness and edge cases before merging. A general prompt may work, but over time, you may want a dedicated reviewer persona with tighter boundaries.

That is a strong case for an agent like:

```
.claude/
└── agents/
    └── code-reviewer.md
```

That agent can be designed to focus on:

* Correctness
* Risky assumptions
* Missing edge cases
* Test coverage gaps

The structural benefit is that your specialized review logic is no longer hidden inside a random prompt or spread across multiple files. It has one dedicated home.

#### Keep both folders clean and purpose-specific <a href="#fbe5" id="fbe5"></a>

One of the biggest mistakes with **skills/** and **agents/** is treating them as experimental storage. That usually leads to folders full of:

* Half-finished skills
* Duplicate agents
* Overlapping reviewer personas
* Vague names like **helper.md** or **analysis.md**

That makes the setup harder to use, not more efficient. A better rule is this:

* Each skill should solve one recurring workflow
* Each agent should own one specialized role
* If two files overlap heavily, they probably should be merged or simplified

#### Folder/code-tree visual <a href="#id-997d" id="id-997d"></a>

Here is a visual you can place in the article:

```
.claude/
├── commands/
│   ├── review-pr.md
│   └── write-tests.md
├── skills/
│   ├── release-prep/
│   │   ├── SKILL.md
│   │   └── release-template.md
│   └── docs-audit/
│       ├── SKILL.md
│       └── style-guide.md
└── agents/
    ├── code-reviewer.md
    ├── security-auditor.md
    └── docs-writer.md
```

This is useful because it shows the progression:

* **commands/** for lighter reusable tasks
* **skills/** for richer packaged workflows
* **agents/** for specialized personas

#### A realistic example for a product team <a href="#id-7012" id="id-7012"></a>

For a SaaS team, the structure might look like this:

```
.claude/
├── skills/
│   ├── release-prep/
│   │   ├── SKILL.md
│   │   └── release-template.md
│   ├── api-audit/
│   │   ├── SKILL.md
│   │   └── api-checklist.md
│   └── onboarding-docs/
│       ├── SKILL.md
│       └── docs-outline.md
└── agents/
    ├── code-reviewer.md
    ├── security-auditor.md
    └── documentation-editor.md
```

This kind of structure works well when the team has a few recurring workflows that deserve more than a one-line command.

#### When not to add these folders yet? <a href="#f70d" id="f70d"></a>

This is important for keeping the article practical.

Do not add **skills/** and **agents/** just because they exist. Add them when there is a clear structural reason.

You probably do **not** need them yet if:

* Most tasks are still simple
* Your team rarely repeats the same advanced workflow
* Command files already solve the problem
* You are still refining basic instructions and permissions

Efficiency does not come from having more folders. It comes from adding structure only when the workflow justifies it.
