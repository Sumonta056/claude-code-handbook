# Week -1  : AI Pilot Program

### Useful Resources & Tools

* Chrome DevTools – Claude Plugin (Anthropic): Allows Claude to access DOM and Vue elements. It is highly cost-efficient, enables testing with proper test notes, and helps identify mounting issues.
  * _Suggestion:_ Ask Claude for an HTML report that includes snapshots and detailed logs.
* High-Quality Architecture Diagrams: [Excalidraw](https://github.com/excalidraw/).
  * _Usage:_ Use the Excalidraw MCP. I installed it in Claude Code (it is desktop-friendly, though you can also install the VS Code extension). Ask Claude to save the file so you can easily visualize and edit diagrams directly from your codebase.
* Claude Learning Resources: Quick Start | Claude Code Guide.
  * This guide provides multiple case examples explaining when to use specific features, which I found very helpful. The suggestions for the "AI Mentor" were also useful.

### Plugin Suggestions

* Chrome DevTools MCP
* Playwright CLI
* Skill-creator

### Planning & Prompting Strategies

* Two-Step Execution: Plan with Opus 4.8 first, and then verify the plan. Make sure to provide proper context and attach the necessary files in your prompt. Once verified, execute the plan in a new chat—this yields better responses than doing it all in the same chat.
* Provide Context: Explicitly state the business logic and edge cases in your prompts rather than letting Claude guess.
* Clarify with Reports: Ask for an HTML report during the planning phase to get a clearer breakdown of the plan.
* Use Strong Keywords: Use precise vocabulary in your prompts (e.g., "shotgun," "replete"). _(I will share the full list later)._
* Break Down Complex Plans: For long and complex tasks, divide the plan into three distinct steps and verify the output after each step.

### Testing & Verification Workflow

If you are ever unsure whether to trust the AI's test results, do the following:

1. Request Proof: Always ask for an HTML report with detailed snapshot proofs.
2. Use Scripts: Ask Claude to provide a bash script to test specific cases.
3. Test the AI's Limits: Map out complex cases, verify them, and re-ask the prompt to confirm Claude is actually capable of executing the solution.
4. Save Evidence: Always ask the AI to verify its own work and keep snapshots.
