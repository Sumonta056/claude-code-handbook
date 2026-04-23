# Built-in Commands

Built-in commands are shortcuts for common actions. There are **60+ built-in commands** and **5 bundled skills** available. Type `/` in Claude Code to see the full list, or type `/` followed by any letters to filter.

<table><thead><tr><th width="249.4190673828125">Command</th><th>Purpose</th></tr></thead><tbody><tr><td><code>/compact [instructions]</code></td><td>⭐⭐ Compact conversation with optional focus instructions</td></tr><tr><td><code>/clear</code></td><td>⭐⭐ Clear conversation (aliases: <code>/reset</code>, <code>/new</code>)</td></tr><tr><td><code>/context</code></td><td>⭐⭐ Visualize context usage as colored grid</td></tr><tr><td><code>/export [filename]</code></td><td>⭐⭐ Export the current conversation to a file or clipboard</td></tr><tr><td><code>/plan [description]</code></td><td>Enter plan mode</td></tr><tr><td><code>/fast [on|off]</code></td><td>Toggle fast mode</td></tr><tr><td><code>/agents</code></td><td>Manage agent configurations</td></tr><tr><td><code>/hooks</code></td><td>View hook configurations</td></tr><tr><td><code>/mcp</code></td><td>Manage MCP servers and OAuth</td></tr><tr><td><code>/skills</code></td><td>List available skills</td></tr><tr><td><code>/memory</code></td><td>Edit <code>CLAUDE.md</code>, toggle auto-memory</td></tr><tr><td><code>/plugin</code></td><td>Manage plugins</td></tr><tr><td><code>/diff</code></td><td>Interactive diff viewer for uncommitted changes</td></tr><tr><td><code>/doctor</code></td><td>Diagnose installation health</td></tr><tr><td><code>/effort [low|medium|high|xhigh|max|auto]</code></td><td>Set effort level via interactive arrow-key slider. Levels: <code>low</code> → <code>medium</code> → <code>high</code> → <code>xhigh</code> (new in v2.1.111) → <code>max</code>. Default is <code>xhigh</code> on Opus 4.7; <code>max</code> requires Opus 4.7</td></tr><tr><td><code>/color [color|default]</code></td><td>Set prompt bar color</td></tr><tr><td><code>/btw &#x3C;question></code></td><td>Side question without adding to history</td></tr><tr><td><code>/exit</code></td><td>Exit the REPL (alias: <code>/quit</code>)</td></tr><tr><td><code>/permissions</code></td><td>View/update permissions (alias: <code>/allowed-tools</code>)</td></tr><tr><td><code>/recap</code></td><td>Show session recap / summary when returning to a session (added v2.1.108)</td></tr><tr><td><code>/remote-control</code></td><td>Remote control from claude.ai (alias: <code>/rc</code>)</td></tr><tr><td><code>/review</code></td><td><strong>Deprecated</strong> — install the <code>code-review</code> plugin instead</td></tr><tr><td><code>/rewind</code></td><td>Rewind conversation and/or code (alias: <code>/checkpoint</code>)</td></tr><tr><td><code>/schedule [description]</code></td><td>Create/manage Cloud scheduled tasks</td></tr><tr><td><code>/security-review</code></td><td>Analyze branch for security vulnerabilities</td></tr><tr><td><code>/tasks</code></td><td>List/manage background tasks</td></tr><tr><td><code>/team-onboarding</code></td><td>Generate a teammate ramp-up guide from the project's Claude Code setup (new in v2.1.101)</td></tr><tr><td><code>/powerup</code></td><td>Discover features through interactive lessons with animated demos</td></tr><tr><td><code>/ultraplan &#x3C;prompt></code></td><td>Draft plan in ultraplan session, review in browser</td></tr><tr><td><code>/ultrareview</code></td><td>Comprehensive cloud-based code review with multi-agent analysis (added v2.1.111)</td></tr><tr><td><code>/usage</code></td><td>Show plan usage limits and rate limit status</td></tr><tr><td><code>/stats</code></td><td>Visualize daily usage, sessions, streaks</td></tr><tr><td><code>/status</code></td><td>Show version, model, account</td></tr></tbody></table>

#### Bundled Skills

These skills ship with Claude Code and are invoked like slash commands:

| Skill                       | Purpose                                                  |
| --------------------------- | -------------------------------------------------------- |
| `/batch <instruction>`      | Orchestrate large-scale parallel changes using worktrees |
| `/claude-api`               | Load Claude API reference for project language           |
| `/debug [description]`      | Enable debug logging                                     |
| `/loop [interval] <prompt>` | Run prompt repeatedly on interval                        |
| `/simplify [focus]`         | Review changed files for code quality                    |

#### Deprecated Commands

#### Recent Changes

* `/fork` renamed to `/branch` with `/fork` kept as alias (v2.1.77)
* `/output-style` deprecated (v2.1.73)
* `/review` deprecated in favor of the `code-review` plugin
* `/effort` command added with `max` level requiring Opus 4.7 (originally Opus 4.6-only)
* `/voice` command added for push-to-talk voice dictation
* `/schedule` command added for creating/managing scheduled tasks
* `/color` command added for prompt bar customization
* /pr-comments removed in v2.1.91 — ask Claude directly to view PR comments
* /vim removed in v2.1.92 — use /config → Editor mode instead
* /ultraplan added for browser-based plan review and execution
* /powerup added for interactive feature lessons
* /sandbox added for toggling sandbox mode
* `/model` picker now shows human-readable labels (e.g., "Sonnet 4.6") instead of raw model IDs
* `/resume` supports `/continue` alias
* MCP prompts are available as `/mcp__<server>__<prompt>` commands (see MCP Prompts as Commands)
* `/team-onboarding` added for auto-generating teammate ramp-up guides (v2.1.101)
* `/tui` command added for flicker-free fullscreen TUI rendering (v2.1.110)
* `/focus` command added for focus view toggle; `Ctrl+O` now only toggles verbose transcript (v2.1.110)
* `/recap` command added to manually trigger session context recap (v2.1.108)
* `/undo` added as alias for `/rewind` (v2.1.108)
* `/proactive` added as alias for `/loop` (v2.1.105)
* `/effort` gained interactive arrow-key slider and new `xhigh` level between `high` and `max`; default effort raised to `xhigh` for Opus 4.7 plans (v2.1.111)
* `/ultrareview` added for comprehensive cloud-based multi-agent code review (v2.1.111)
* `/less-permission-prompts` added to analyze Bash/MCP tool calls and reduce permission prompts via an allowlist in `.claude/settings.json` (v2.1.111)
* Auto mode no longer requires the `--enable-auto-mode` flag for Max subscribers on Opus 4.7 (v2.1.112)

#### `/team-onboarding` — Teammate Ramp-Up Guide

> **New in v2.1.101**

Use `/team-onboarding` to generate a teammate ramp-up guide from your project's local Claude Code usage. The command inspects your `CLAUDE.md`, installed skills, subagents, hooks, and recent workflows, then produces an onboarding document that helps new developers become productive quickly.

It's a built-in command — nothing to install.

**Usage:**

```bash
claude /team-onboarding
```

The generated guide summarizes:

* Project purpose and key conventions from `CLAUDE.md`
* Available skills and when they are auto-invoked
* Configured subagents and their responsibilities
* Hooks that run on common events
* Common workflows newcomers should know about

**Availability:** Shipped in Claude Code v2.1.101 (April 11, 2026).
