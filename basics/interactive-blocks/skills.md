---
icon: sailboat
---

# SKILLs!

#### What are Claude Skills?

Skills address a fundamental need: **repeatable, user-invoked workflows with consistent output formats**.

Here's the recommended folder structure for organizing a skill:

```
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md      # Example output showing expected format
└── scripts/
    └── validate.sh    # Script Claude can execute
```

#### The Problem Skills Solve

Without skills, you'd repeatedly type complex instructions every time you need a specific task done:

```
"Review this code for bugs, security issues, and logic errors.
Focus on correctness, not style. Format the output with severity levels.
Include file references and suggested fixes..."
```

With skills, you simply type `/code-reviewer` — turning multi-paragraph instructions into a single command.

<details>

<summary><strong>When to Use Each (Skill vs Agent )</strong></summary>

**Use a Skill when:**

* You want to invoke the same workflow repeatedly
* You need consistent, structured output
* The task is user-initiated (you decide when)
* Examples: `/code-reviewer`, `/changelog`, `/techdebt`

**Use an Agent when:**

* Claude should autonomously decide when to act
* Work can be parallelized or delegated
* Tasks require exploration before action
* Examples: `code-quality-auditor`, `Explore`, `Plan`

Practical Example

**Skill** (`/code-reviewer`): You invoke it when _you_ want a code review, it follows a defined protocol and outputs a structured report.

**Agent** (`code-quality-auditor`): Claude _automatically_ spawns it after writing significant code — it decides when the context warrants review.

Think of it as:

* **Skills** = Tools you wield
* **Agents** = Assistants Claude delegates to

</details>

#### How to create a Skills?

Exercise Prompt: Copy and paste this prompt to Claude to create a learning skill:

```
Create a skill called "explain-code" that helps developers understand unfamiliar code.

Requirements:
1. Create the skill in `.claude/skills/explain-code/SKILL.md`
2. The skill should:
   - Accept a file path or code block as input
   - Explain what the code does in plain English
   - Identify the programming patterns used
   - List any dependencies or imports
   - Highlight potential gotchas or tricky parts
   - Suggest related documentation to read

3. Output format should be structured with these sections:
   - Summary (2-3 sentences)
   - Step-by-Step Breakdown
   - Patterns Used
   - Dependencies
   - Watch Out For (gotchas)
   - Learn More (documentation links)

4. Include a Gotchas section in the skill itself for common issues

Make sure the skill follows the standard SKILL.md frontmatter format with name 
and description.
```

After Creating the Skill: Test your new skill by running:

```
/explain-code src/app.js
```

Or for any code file in your project:

```
/explain-code path/to/any/file.py
```





***

{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>







