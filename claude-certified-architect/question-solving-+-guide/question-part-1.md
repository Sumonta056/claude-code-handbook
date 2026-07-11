# Question Part - 1

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

* Configure the subagent to always return partial results with success status, embedding error details in metadata. The coordinator treats all responses as successful and filters problematic items during synthesis.
  * No : 100%
* Have the coordinator validate all documents before dispatching to the subagent, rejecting documents likely to cause failures to ensure the subagent only receives processable files.
  * No. You are using coordinator itself instead of subagent
  * <mark style="color:$danger;">**I choose : Why ? Validation Check**</mark>
* Have the subagent implement local recovery for transient failures and only propagate errors it cannot resolve to the coordinator, including what was attempted and any partial results obtained.
  * <mark style="color:$success;">**Yes**</mark>
  * Why?
  * Implementing local recovery for transient failures within the **subagent follows the principle of handling errors at the lowest level capable of resolving them**. This reduces excessive coordinator involvement while still escalating truly unresolvable issues with full context, including what recovery was attempted and any partial results obtained.
* Create a dedicated error-handling agent that monitors all subagent failures via a shared queue and makes recovery decisions independently, dispatching retry commands directly to subagents.&#x20;
  * No. You should not let agent handle error.
  * <mark style="color:$danger;">**I choose : Why ? Separate agent**</mark>

***

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Why not A & D ?

* Not purely deterministic&#x20;
* Prompt and Examples can be bi-passed by AI agents

Why not C ?

* Over work

***

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

* D : Run three independent review passes on the full PR and only flag issues that appear in at least two of three

Why not A?

* Not fully automate, spliting may not find similar context

Why not C?

* High tier model doesn't make gurrantee better reviews

Why not D?

* Subagent are indirectly doing same kind of review. If 3 review check do 3 different things and then validate it can be a good option

***

You are building a multi-agent research system with a coordinator agent that delegates to specialized subagents. During testing, you discover that your synthesis subagent produces a report missing key findings that the web search subagent found. The web search subagent’s logs confirm it returned comprehensive results. What is the most likely root cause?

1. The synthesis subagent’s context window is full, causing it to drop information from the middle of the input.
2. The coordinator is not passing the web search subagent’s complete findings into the synthesis subagent’s prompt.
3. The synthesis subagent is running an outdated version of the model that lacks the capacity to process long inputs.
4. The web search subagent and synthesis subagent are sharing memory, causing a race condition that corrupts the findings.

> Why not?
>
> 1: Cause less chance sub agents context gets full&#x20;
>
> 3: Not reasonable enough
>
> 4: Agents don't share memory common

In multi-agent systems, subagents operate with isolated context and do not automatically inherit the coordinator’s conversation history. The coordinator must explicitly include complete findings from prior agents in each subagent’s prompt. When a synthesis subagent is missing findings, the most common cause is that the coordinator failed to pass the complete results in the prompt.

***

Your team’s CLAUDE.md has grown to over 500 lines, covering coding standards, testing conventions, API conventions, deployment procedures, and security guidelines. Developers report that Claude sometimes misses instructions from specific sections. What is the most maintainable approach to restructure this?

1. Split the monolithic CLAUDE.md into focused topic-specific files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md).
2. Keep the single CLAUDE.md but reorganize with clearer headers and a table of contents at the top.
3. Create separate CLAUDE.md files in each subdirectory of the project, duplicating relevant sections.
4. Convert the CLAUDE.md into a skills file in .claude/skills/ so developers can invoke it on demand.



> The .claude/rules/ directory is the recommended approach for organizing topic-specific rule files as an alternative to a monolithic CLAUDE.md. Each file can have YAML frontmatter with path-scoping to activate only when editing relevant files, reducing irrelevant context and improving maintainability.
