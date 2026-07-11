# Lessons !

* From 4 option, first cut out which is not answer
* Multiple choice : 1 correct + 3 distractor&#x20;
  * **Careful from distractor!**









#### Anti-patterns the exam loves to test

If you see one of these in an answer choice, it's almost always the wrong answer:

* Using natural-language parsing or iteration caps to terminate an agentic loop (use stop\_reason).
* Putting deterministic business rules in a prompt (use hooks).
* Generic error messages or silently swallowing errors instead of structured error metadata.
* Using sentiment or LLM self-reported confidence as an escalation signal.
* Single-pass review of many files (use per-file + integration passes).
* Required schema fields where source info may be absent (induces fabrication — make them nullable).
* Putting team-wide instructions in \~/.claude/CLAUDE.md instead of the project-level file.
