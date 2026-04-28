---
icon: meteor
cover: ../.gitbook/assets/Screenshot 2026-04-28 at 11.08.26 AM.png
coverY: 0
coverHeight: 289
---

# Useful Plugins + Skills!

{% hint style="info" %}
List of Plugins Templates : [https://app.aitmpl.com/plugins](https://app.aitmpl.com/plugins)
{% endhint %}

#### Agent Skills ⭐⭐⭐ <a href="#claude-mem" id="claude-mem"></a>

**Production-grade engineering skills for AI coding agents.**

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. These ones are packaged so AI agents follow them consistently across every phase of development.

```
  DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

| What you're doing    | Command          | Key principle           |
| -------------------- | ---------------- | ----------------------- |
| Define what to build | `/spec`          | Spec before code        |
| Plan how to build it | `/plan`          | Small, atomic tasks     |
| Build incrementally  | `/build`         | One slice at a time     |
| Prove it works       | `/test`          | Tests are proof         |
| Review before merge  | `/review`        | Improve code health     |
| Simplify the code    | `/code-simplify` | Clarity over cleverness |
| Ship to production   | `/ship`          | Faster is safer         |

{% code overflow="wrap" %}
```
/plugin install agent-skills@addy-agent-skills
```
{% endcode %}

Link : [https://github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

***

#### Karpathy-Inspired Claude Code Guidelines ⭐⭐⭐ <a href="#claude-mem" id="claude-mem"></a>

A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

Link : [https://github.com/forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)

{% code overflow="wrap" %}
```
/plugin install andrej-karpathy-skills@karpathy-skills
```
{% endcode %}

***

#### Codex plugin for Claude Code ⭐⭐⭐ <a href="#claude-mem" id="claude-mem"></a>

Use Codex from Claude Code to review code or delegate tasks.

{% code overflow="wrap" %}
```
/plugin marketplace add openai/codex-plugin-cc
```
{% endcode %}

{% code overflow="wrap" %}
```
/codex:review --background
/codex:status
/codex:result
```
{% endcode %}

Link : [https://github.com/openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

***

#### Claude-Mem ⭐⭐⭐ <a href="#claude-mem" id="claude-mem"></a>

Persistent memory compression system for Claude Code

Claude-Mem seamlessly preserves context across sessions by automatically capturing tool usage observations, generating semantic summaries, and making them available to future sessions. This enables Claude to maintain continuity of knowledge about projects even after sessions end or reconnect.

Link : [https://github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

{% code overflow="wrap" expandable="true" %}
```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```
{% endcode %}

***

#### Superpowerss

Superpowers is a complete software development workflow for your coding agents, built on top of a set of composable "skills" and some initial instructions that make sure your agent uses them.

Link : [https://github.com/obra/superpowers](https://github.com/obra/superpowers)

{% code overflow="wrap" expandable="true" %}
```
/plugin install superpowers@claude-plugins-official
```
{% endcode %}

***

#### Skills Me⭐⭐

The missing pluginmanager for Claude. Detects your project stack and installs the right Claude Code plugins in one command. Search across 4 marketplaces, install, update, and manage — all from the terminal.

{% code overflow="wrap" %}
```
skillme init
```
{% endcode %}

Link : [https://skillme-cli.vercel.app/](https://skillme-cli.vercel.app/)

#### UI-UX-PRO MAX Skill

An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

Link : [https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

{% code overflow="wrap" expandable="true" %}
```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```
{% endcode %}

***

#### Shadcn/ui Skills

Complete shadcn/ui component library guide including installation, configuration, and implementation of accessible React components...

{% code overflow="wrap" expandable="true" %}
```
npx @smithery/cli@latest skill add giuseppe-trisciuoglio/shadcn-ui
```
{% endcode %}

***

#### Make Interfaces Feel Better

An agent skill based on the "Details that make interfaces feel better" article

{% code overflow="wrap" expandable="true" %}
```
npx skills add jakubkrehel/make-interfaces-feel-better
```
{% endcode %}

***

#### emilkowalski/skill

A skill file based on the articles written on my personal site. Designed for designers and engineers to help them build better user interfaces.

It covers animations, design, code, performance, and more.

{% code overflow="wrap" expandable="true" %}
```
npx skills add emilkowalski/skill
```
{% endcode %}





{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>
