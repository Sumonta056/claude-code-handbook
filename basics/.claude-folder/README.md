---
icon: folder-open
---

# .claude Folder ⭐⭐

{% code title="" overflow="wrap" lineNumbers="true" %}
```
your-project/
├── CLAUDE.md                  # Main project instructions
├── CLAUDE.local.md            # Personal overrides (not committed)
└── .claude/
    ├── settings.json          # Control layer
    ├── rules/                 # Modular instructions
    ├── hooks/                 # Automation scripts
    ├── commands/              # Reusable prompt workflows
    ├── skills/                # Packaged capabilities
    └── agents/                # Specialized subagents
```
{% endcode %}

{% code title="" overflow="wrap" lineNumbers="true" %}
```
your-project/
├── CLAUDE.md
├── CLAUDE.local.md
└── .claude/
    ├── settings.json
    ├── settings.local.json
    ├── rules/
    │   ├── backend.md
    │   ├── frontend.md
    │   ├── testing.md
    │   └── security.md
    ├── hooks/
    │   ├── block-dangerous-commands.sh
    │   ├── format-edits.sh
    │   └── run-checks-before-stop.sh
    ├── commands/
    │   ├── review-pr.md
    │   ├── write-tests.md
    │   └── summarize-changes.md
    ├── skills/
    │   └── release-prep/
    │       ├── SKILL.md
    │       └── release-template.md
    └── agents/
        ├── code-reviewer.md
        └── security-auditor.md
```
{% endcode %}

_**A simple way to think about it is this:**_

* **CLAUDE.md:** explains how the project works
* **settings.json:** controls how Claude operates in the project
* The **subfolders** exist to keep everything else organized

That separation is useful because these files serve different purposes. **CLAUDE.md** is about guidance. **settings.json** is about control. One tells Claude what matters in the codebase. The other shapes what Claude is allowed to do and what automatic behaviors should happen around its work.

For example, in a FastAPI project, **CLAUDE.md** might explain that all API schemas live in **schemas/,** all service logic lives in **services/**, and every endpoint should validate inputs with Pydantic models.

Meanwhile, **.claude/settings.json** might allow Claude to run test commands, deny access to **.env** files, and trigger a formatting hook after file edits. Those two files work together, but they should not be mixed together.

The top level should also make a clear distinction between shared files and personal overrides. A shared **CLAUDE.md** belongs in the root because the whole team benefits from it.

A personal override, such as **CLAUDE.local.md,** is different. It exists for local preferences and should stay out of the team’s shared structure. The same logic applies to **settings.local.json** inside **.claude/**.

In other words, the top level should answer the biggest questions first. What does Claude need to know about this project? What is Claude allowed to do here? Everything else can be organized underneath that foundation.

{% content-ref url="claude.md-vs-rules.md" %}
[claude.md-vs-rules.md](claude.md-vs-rules.md)
{% endcontent-ref %}

{% content-ref url="/broken/pages/PbYb0GukRhiS4qCHdRal" %}
[Broken link](/broken/pages/PbYb0GukRhiS4qCHdRal)
{% endcontent-ref %}

{% content-ref url="the-role-of-commands.md" %}
[the-role-of-commands.md](the-role-of-commands.md)
{% endcontent-ref %}

A cleaner pattern is:

* `CLAUDE.md` explains the project
* `rules/` refines guidance
* `hooks/` contains automatic operational scripts
* `commands/` contains reusable prompt workflows

That division makes the folder easier to scan, easier to extend, and easier for teammates to understand.

#### Folder/code-tree visual <a href="#ecc9" id="ecc9"></a>

Here is a visual you can place in the article:

```
.claude/
├── settings.json
├── rules/
│   ├── frontend.md
│   ├── backend-api.md
│   └── testing.md
├── hooks/
│   ├── block-dangerous-commands.sh
│   ├── format-edits.sh
│   └── run-tests-before-stop.sh
└── commands/
    ├── review-pr.md
    ├── write-tests.md
    └── summarize-changes.md
```

This works well because it shows that **hooks/** and **commands/** sit beside the instruction layer, not inside it.

Press enter or click to view image in full size

<figure><img src="https://miro.medium.com/v2/resize:fit:1400/1*5wZz4jXjRAS9aLG93WUzTg.png" alt="" height="428" width="700"><figcaption></figcaption></figure>

{% content-ref url="when-should-use-skills-and-agents.md" %}
[when-should-use-skills-and-agents.md](when-should-use-skills-and-agents.md)
{% endcontent-ref %}

{% hint style="info" %}
### A useful way to think about the blueprint is as a progression:

* Start with **CLAUDE.md** and **settings.json**
* Add **rules/** when one instruction file stops scaling
* Add **hooks/** when you need automation or enforcement
* Add **commands/** when prompts become repetitive
* Add **skills/** when workflows become deeper
* Add **agents/** when specialization clearly improves results
{% endhint %}

***

Special thanks to this article :&#x20;

{% embed url="https://levelup.gitconnected.com/how-to-structure-claude-folder-for-maximum-efficiency-c26ef3f552ba" %}

{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}
