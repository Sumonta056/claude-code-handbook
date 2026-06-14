# Week -1  : AI Pilot Program

#### 1. Planning Workflow

* Plan with `Opus` first, then verify the plan.
* Make sure to provide proper context and relevant files `(using @)` in the prompt.
* Execute the plan in a new chat rather than continuing in the same chat. The responses are usually better.

_**Suggestions :**_

* Try to provide business logic and edge cases in the prompt rather than letting Claude judge everything by itself. (Otherwise claude goes unecessary thinking)
* Ask Claude to generate an `HTML report` during the planning phase for additional clarity and validation.

_**Handling Long and Complex Plans :**_

* Break large plans into 3 steps.
* Add a verification phase after each step.

***

#### 2. Plugin Suggestions

* `Chrome DevTools MCP`
* `Playwright CLI`
* `Skill Creator`

_**Suggestion :**_

* Ask to claude to make skills or rules for a specific topic and context instead mannually doing it by self (But must review)

***

#### 3. Useful Shortcuts

* `Option + Command + K` → Switch Selected Item to Claude Chat
* Use `/ultrathink`
* Use the `AskUserQuestion` tool

***

#### 4. Testing with Chrome DevTools MCP ( [Link: Chrome DevTools](https://claude.com/plugins/chrome-devtools-mcp) )

_**Results:**_

* The results were very good.
* It helped Claude access the `DOM and Vue` elements, run the project, and interact with it.
* Adding `cookies`, managing `local storage`, and reading `API` responses worked well.
* It was very cost-efficient.
* It could test features with proper test notes and identify mounting-related issues.

_**Suggestions:**_

* Ask for an `HTML report` with `snapshots` and detailed findings.
* It was able to generate useful snapshots in the HTML reports.

***

#### 5. How to Gain Confidence That AI Is Doing the Right Thing

> If you're unsure whether to trust the AI's results:

* Always ask for an `HTML report` with detailed snapshot evidence.
* Ask it to generate a `Bash script` for a specific scenario.
* Verify complex cases separately.
* Map the results and ask Claude to test them again.
* Always ask it to verify findings and keep snapshots.
* Use subagents to verify reports and failed test cases (verification loop).

\
**Real Example :**

There was a scenario where 8 out of 10 test cases passed. Initially, I was happy with the result, but the remaining 2 cases were incorrect. Claude's conclusions for those cases were wrong, so I had to verify them again manually.

**In that situation:**

* Ask Claude Keep verifying until the results are okay and well reasoned.
* Use a subagent verification loop and ask Claude to verify its own responses.
* Ask Claude to explain failures with complete reasoning.

**Important Observation** : `Claude can sometimes show bias in its own validation.`\
Because of that:

* Avoid giving everything in a single prompt.
* First, ask Claude to perform the test or something.
* Then ask it to verify the report separately.

> - If you provide all instructions at once, Claude may become biased toward proving itself correct.
> - Splitting the work into two phases is often more reliable than doing everything in one prompt.

***

#### 6. Use Strong Keywords in Prompts

Examples: `Shotgun`, Replete, etc. (I'll share the full list later.)

_Suggestions_

* Use `"Non-Negotiable"` instead of `"Preference"` when something must be followed.
* If Claude absolutely needs to perform a step, use stronger and more explicit wording.
* Otherwise, Claude may follow the instruction inconsistently.

***

#### 7. Trust Official Resources

* Prefer official Claude documentation and resources.
* Avoid relying heavily on random blogs or articles for implementation details.

***

#### 8. Claude.md Refactoring Suggestions

_**Structure :**_

* Instead of putting everything inside claude.md, use rules and bind them to specific paths.
* This helps keep claude.md more precise and accurate.

_**What Should Stay in Claude.md?**_

* If a rule consistently helps Claude perform better, keep it in claude.md.
* If a rule doesn't improve performance, remove it.
* Ultimately, you should decide what belongs in claude.md.

_**Additional Suggestions**_

* Avoid keeping similar instructions in both claude.md and the Rules/Skills folders.
* Prefer using Skills for task-specific workflows.
* Keep global non-negotiables inside claude.md.

_**Avoid Rules Like This**_

* After ANY correction from the user: update `.claude/lessons.md` with the pattern to prevent the same mistake. (If really needed use skills for that). Try not to use overly broad rules like the above.

_**Team should decide to keep this kind of things in claude.md (First try then decide)**_

```
- Plan first; define success criteria before coding. If unsure, ask via AskUserQuestion before proceeding.
- Fix root causes, not symptoms. Minimum diff — touch only what's necessary, don't over-engineer.
- Never guess APIs, composables, modules, or publication context configs — read the source.
- Use subagents liberally to keep main context clean.
```

***



\
9\. Other Useful Resources Tried<br>

* High-Quality Architecture Diagrams (Repository: [https://github.com/excalidraw/](https://github.com/excalidraw/))
  * Suggestions:
    * Use the Excalidraw MCP.
    * I installed it in Claude Code Desktop, and it works well.
    * You can also install the VS Code extension.
    * Ask Claude to save the file, and you can easily visualize and edit it directly from the codebase.
* Useful Claude Learning Resources : [Claude Code Guide: Templates, Security, Workflows | Anthropic CLI](https://cc.bruniaux.com/)
