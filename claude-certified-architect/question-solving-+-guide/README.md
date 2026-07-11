# Question Solving + Guide

<table data-header-hidden><thead><tr><th width="167.116455078125"></th><th width="104.78125"></th><th></th></tr></thead><tbody><tr><td>Domain</td><td>Weight</td><td>What it covers</td></tr><tr><td>Agentic Architecture &#x26; Orchestration</td><td>27%</td><td>Multi-agent systems, agentic loops driven by stop_reason, coordinator/subagent patterns, the Task tool, fork_session, hooks (PostToolUse) for deterministic policy enforcement.</td></tr><tr><td>Tool Design &#x26; MCP Integration</td><td>18%</td><td>Designing MCP servers/clients, tool descriptions, scoping (.mcp.json vs ~/.claude.json), structured errors (isError, errorCategory, isRetryable), tool_choice modes.</td></tr><tr><td>Claude Code Configuration &#x26; Workflows</td><td>20%</td><td>CLAUDE.md hierarchy + @import, .claude/rules/ with path globs, .claude/commands/, .claude/skills/ with SKILL.md frontmatter, plan mode vs direct execution, CI/CD flags (-p, --output-format json).</td></tr><tr><td>Prompt Engineering &#x26; Structured Output</td><td>20%</td><td>Few-shot (2–4 examples), JSON schemas via tool_use, nullable fields to prevent fabrication, validation-retry loops, Message Batches API (50% cheaper, ≤24h, no multi-turn tools).</td></tr><tr><td>Context Management &#x26; Reliability</td><td>15%</td><td>Lost-in-the-middle positioning, persistent case-fact blocks, trimming tool outputs, scratchpad files, escalation triggers (explicit request / policy gap / no progress — NOT sentiment).</td></tr></tbody></table>

#### The 6 production scenarios

You'll see 4 of the 6 on test day, randomly chosen.

* Customer Support Resolution Agent : escalation logic, identity verification, case-fact persistence.
* Code Generation with Claude Code : multi-file edits, plan mode, hooks.
* Multi-Agent Research System : coordinator/subagent hub-and-spoke, fork\_session, provenance.
* Developer Productivity : CLAUDE.md hierarchy, skills, rules.
* Claude Code for CI/CD : -p flag, JSON output, independent-instance review.
* Structured Data Extraction : JSON schemas, validation-retry, Message Batches API.

