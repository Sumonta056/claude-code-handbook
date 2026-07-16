# Lessons & Learnings

* From 4 option, first cut out which is not answer
* Multiple choice : 1 correct + 3 distractor&#x20;
  * **Careful from distractor!**



* Guarantees beat instructions :&#x20;
  * When a rule MUST hold : enforce it in code: hooks, gates, schemas.
  * Prompts are probabilistic; they fail a small % of the time.
  * "Gurantee Compliance Required" = answer is hooks
* Fix root cause proportionately
  * If two tools are getting confused? Improve description
  * Don't build routing classifers
  * Exam has full of over engineer wrong answer
* Context is scarce and leaky
  *
* Gurantee



1. stop\_reason is your source of truth in agentic loops
2. Prompt instructions have a failure rate. Programmatic enforcement doesn't. Prompt instructions have a failure rate. Programmatic enforcement doesn't.
3. Subagents don't inherit context — you have to pass it explicitly
4. Tool descriptions are how Claude chooses tools
   1. If two tools have similar descriptions, Claude will pick the wrong one. The exam teaches this through painful examples — analyze\_content vs. analyze\_document, or get\_customer vs. get\_account\_info both described as "retrieves customer data." The fix is always richer descriptions: what the tool handles, when to use it, when not to use it, edge cases, and how it differs from similar tools.
5.



#### Anti-patterns the exam loves to test

If you see one of these in an answer choice, it's almost always the wrong answer:

* Using natural-language parsing or iteration caps to terminate an agentic loop (use stop\_reason).
* Putting deterministic business rules in a prompt (use hooks).
* Generic error messages or silently swallowing errors instead of structured error metadata.
* Using sentiment or LLM self-reported confidence as an escalation signal.
* Single-pass review of many files (use per-file + integration passes).
* Required schema fields where source info may be absent (induces fabrication — make them nullable).
* Putting team-wide instructions in \~/.claude/CLAUDE.md instead of the project-level file.



<figure><img src="../../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>
