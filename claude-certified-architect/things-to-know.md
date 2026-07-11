# Things to Know!



* [ ] Multi-agent research system with the Claude Agent SDK
*



### The Five Exam Domains

The exam is organized around five weighted domains. Each domain tests specific knowledge and skills required for building production Claude applications. Understanding the weight distribution is essential for study planning.

#### Domain 1: Agentic Architecture and Orchestration (27%)

This is the heaviest domain and, according to most candidates who have passed, the trickiest. It covers designing, building, and managing agentic systems where Claude serves as the reasoning engine.

Key subdomains:

* **1.1 Agentic Loops** — Design agentic loops that use tool results to determine next actions. The loop checks `stop_reason`: “tool\_use” means execute the tool and continue; “end\_turn” means the agent is done. Tool results must be appended to conversation history before the next request.
* **1.2 Multi-Agent Orchestration** — Implement orchestration patterns using the Agent SDK: hub-and-spoke (coordinator delegates to specialists), handoff chains, and parallel fan-out. Know when to choose centralized control vs. peer-to-peer delegation.
* **1.3 Subagent Invocation and Context** — Subagents do NOT inherit the parent’s conversation history. Only what the coordinator explicitly passes in the prompt reaches the subagent. This is a frequently tested distinction.
* **1.4 Session State and Resumption** — Managing session state and conversation history across turns, including context window management, progressive summarization, and immutable fact blocks for critical data.
* **1.5 SDK Hooks** — Configure PreToolUse and PostToolUse hooks that can block, modify, or log tool calls deterministically. This is a critical concept: programmatic enforcement vs. prompt-based guidance.
* **1.6 Task Decomposition** — Decompose complex tasks into subtasks with clear boundaries, expected outputs, and success criteria.

The single most tested concept across the entire exam, according to multiple candidates, is the distinction between programmatic enforcement and prompt-based guidance. When something must happen (e.g., blocking a refund above a threshold, verifying identity before granting access), you use programmatic enforcement through hooks and interceptors, not prompt instructions.

#### Domain 2: Tool Design and MCP Integration (18%)

This domain covers designing effective tools that Claude can reliably use and integrating them through the Model Context Protocol.

Key subdomains:

* **2.1 Effective Tool Interfaces** — Write tool descriptions that enable Claude to select the correct tool and provide valid inputs. The exam frequently presents broken or suboptimal tool schemas and asks you to identify the flaw.
* **2.2 Structured Error Responses** — Design error responses for transient errors, business logic errors, and permission errors. When an MCP tool encounters an error, it uses `isError: true` in the response. A generic error gives the agent no information for decision-making.
* **2.3 Tool Distribution** — Distribute tools across agents and configure tool choice (`tool_choice` parameter) to control when and how Claude selects tools.
* **2.4 MCP Server Integration** — Configure MCP servers in Claude Code and agent workflows. Know the distinction between `.mcp.json` (project-level, shared via version control) and `~/.claude.json` (user-level, personal/experimental).

SSE transport trade-offs, authentication patterns for production MCP deployments, and deciding when to consolidate or split tools are frequently tested here.

#### Domain 3: Claude Code Configuration and Workflows (20%)

This domain gets surprisingly specific about Claude Code internals. Many candidates underestimate it.

Key subdomains:

* **3.1 CLAUDE.md Hierarchy** — Configure CLAUDE.md with hierarchy, scoping, and organization. Know the precedence rules for project-level, directory-level, and user-level CLAUDE.md files, plus path-specific rules in `.claude/rules/`.
* **3.2 Custom Slash Commands and Skills** — Create custom commands and skills with frontmatter options. The `context: fork` frontmatter option runs the skill in an isolated sub-agent, preventing verbose output from polluting the main session context.
* **3.3 Plan Mode** — Understand when and how to use Plan Mode for complex tasks.
* **3.4 CI/CD Integration** — Use the `-p` (or `--print`) flag for non-interactive mode. Add `--output-format json` and `--json-schema` for structured PR comments and pipeline integration.
* **3.5 Built-in Tools** — Understand Read, Write, Edit, Bash, Grep, and Glob tools and their appropriate use cases.

#### Domain 4: Prompt Engineering and Structured Output (20%)

This domain tests production-grade prompt engineering, not basic prompting skills.

Key subdomains:

* **4.1 Explicit Criteria Prompting** — Design prompts with explicit, measurable criteria rather than vague instructions.
* **4.2 Few-Shot Prompting** — Apply few-shot examples for output consistency, especially in ambiguous scenarios.
* **4.3 Structured Output via tool\_use** — Enforce structured output using `tool_use` and JSON schemas, including nullable fields to reduce hallucinations.
* **4.4 Validation-Retry Loops** — Implement validation, retry, and feedback loops where output is checked against a schema and re-requested if invalid.
* **4.5 Multi-Pass Review** — Design multi-instance and multi-pass review architectures. A key insight: a model retains reasoning context from generation, making self-review less effective. Independent review instances (without prior reasoning context) catch issues more reliably.

#### Domain 5: Context Management and Reliability (15%)

The lightest domain by weight but consistently underestimated by candidates. Context management questions are often the easiest marks if you know the patterns, and the easiest to lose if you don’t.

Key subdomains:

* **5.1 CALM Framework** — Context-Aware LLM Management, covering prompt caching with `cache_control` breakpoints, conversation compaction, and token estimation.
* **5.2 Escalation Patterns** — Define when to escalate (policy gaps, customer requests, capability limits) vs. resolve autonomously. Do NOT escalate based on sentiment analysis or self-assessed confidence scores.
* **5.3 Error Propagation** — Manage how errors flow through multi-agent systems.
* **5.4 Information Provenance** — Track where information came from across a multi-step workflow.
* **5.5 Confidence Calibration** — Design confidence-routed human review workflow
