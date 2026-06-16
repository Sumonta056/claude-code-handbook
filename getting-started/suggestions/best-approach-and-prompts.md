# Best Approach & Prompts

<details>

<summary><mark style="color:violet;">EXPLAIN</mark> :  Changes with HTML Report</summary>

{% code overflow="wrap" %}
```
Act as a Senior Developer mentoring a Junior Developer. I need you to explain a recent code/system change to me in simple, easy-to-understand words. 

Please provide a comprehensive, step-by-step breakdown of the changes comparing the "Before" and "After" states. 

Please structure your response covering the following areas:

1. Context & Flow
* Explain the overall flow of the process before and after the change.
* Provide a clear, step-by-step walkthrough of the new solution.
* Include placeholders for [Snapshot/Proof] where visual evidence of the flow, layouts, or events would be relevant.

2. Before vs. After Analysis
* Detail the specific cases and issues that existed in the "Before" state.
* Explain inline changes (what exactly was modified in the code).
* List the Pros and Cons of the new "After" solution.

3. Deep Dive into the Details
* Explain how layouts and UI events are affected.
* Detail any changes to the logs (what to look for now vs. before).
* Ensure every corner of the implementation is covered.

4. Final Output: Interactive HTML Report
* After providing the text explanation, generate a single, self-contained, interactive HTML file.
* The HTML report should neatly organize all the information above (Before/After comparisons, flows, code snippets, logs, and placeholders for snapshots) using clean CSS, collapsible sections (accordions), and tabs for easy navigation.
```
{% endcode %}



</details>

<details>

<summary><mark style="color:violet;">EXPLAIN :</mark> A Topic or File with HTM</summary>

{% code overflow="wrap" %}
```
Act as a Senior Developer mentoring a Junior Developer. I need you to explain a specific topic/component in our codebase in simple, easy-to-understand words. 

The topic I need you to explain is: [INSERT TOPIC/COMPONENT/FEATURE NAME HERE]

Please structure your response covering the following areas:

1. High-Level Overview & Flow
* Explain what this topic/component is, why it exists, and its main responsibility in the codebase.
* Provide a clear, step-by-step walkthrough of how data or logic flows through this system.
* Include placeholders for [Architecture Diagram/Snapshot] where visual evidence of the flow or layouts would help a junior dev understand it.

2. Code Architecture & Key Components
* Detail the specific files, modules, or classes involved in this topic.
* Explain the "inline" logic of the most critical functions (what the code is actually doing step-by-step).
* Give concrete examples of different use cases or scenarios where this code triggers.

3. Runtime Behavior (Events, Layouts, & Logs)
* Explain how this topic impacts the UI/layouts (if applicable) and what frontend/backend events are fired.
* Detail the exact logs to look for in the console/terminal to track this system in action. Explain how to use these logs to debug issues related to this topic.

4. Pros, Cons, & Gotchas
* What are the pros and cons of the way this feature/topic was architected?
* List the "gotchas" or common mistakes a junior developer might make when working with or modifying this part of the codebase.

5. Final Output: Interactive HTML Reference Guide
* After providing the text explanation, generate a single, self-contained, interactive HTML file.
* This HTML guide should neatly organize all the information above (Overview, Code Breakdown, Logs/Events, and Pitfalls) using clean CSS, collapsible sections (accordions), and tabs so I can save it locally as a reference doc.
```
{% endcode %}

Understanding a new codebase

```
> Give me a high-level overview of this project's architecture.
> How does the authentication flow work end to end?
> What happens when a user submits an order? Trace the request path.
```

Investigating specific code

```
> Explain what src/middleware/rateLimit.ts does and why it's structured this way.
> What are all the places where we interact with the payments API?
```

</details>

<details>

<summary><mark style="color:red;">BUG :</mark> Fix Approach </summary>

* **Describe the symptom**
* **Ask Claude to locate the cause**
* **Fix and verify**

{% code overflow="wrap" %}
```
Find where this error originates and explain why it happens
```
{% endcode %}

```
> Here's the error from production: "TypeError: Cannot read property 'email' of undefined"
  in src/services/notification.ts:42. The user object is sometimes null when a
  guest checks out. Fix this so guests don't trigger email notifications.
```

\
Tips:&#x20;

* Fix the issue and run the chrome dev tool plugin tests to confirm.
* Paste the full stack trace when available -- Claude uses it to locate the code path.
* Ask Claude to check for similar bugs elsewhere: "Are there other places where we have this issue?"

</details>

<details>

<summary><mark style="color:yellow;">FEAT :</mark> Feature Development Approach (Workflow)</summary>

1. **Explore**: "How does the current notification system work?"

{% code overflow="wrap" expandable="true" %}
```
How does the current implement for {argument} system work in existing codebase?
argument : 
```
{% endcode %}

2. **Plan**: "Plan how to add SMS notifications alongside the existing email system."

{% code overflow="wrap" expandable="true" %}
```
Plan how to add {argument1} alongside the existing {argument2} System.
argument1 :
argument2 :
```
{% endcode %}

3. **Implement**: "Implement the plan. Start with the SMS service class."
4. **Test**: "Write tests for the SMS notification service."
5. **Review**: "Review all the changes we made and check for any issues."

Tips :

* Break large features into smaller pieces and implement them one at a time.
* Ask Claude to follow existing patterns: "Follow the same structure as `EmailService`."
* Commit incrementally: ask Claude to commit after each logical piece is done.

</details>

<details>

<summary><mark style="color:$success;">DEBUG</mark> : How to debug using Claude ?</summary>

**Diagnostic workflow**

```
> The /api/orders endpoint returns a 500 error intermittently. Help me debug this.
  Here are the recent logs: [paste logs]
```

Claude will typically:

1. Analyze the logs for patterns
2. Read the relevant code
3. Identify potential causes
4. Suggest and apply fixes

```
> Add logging to the order processing pipeline so we can trace where requests fail.
  Use our existing logger (src/lib/logger.ts). Don't change any business logic.
```

</details>

<details>

<summary><mark style="color:purple;">REVIEW</mark> : PR's &#x26; Code Reviews</summary>

{% hint style="info" %}
Generate HTML Report!
{% endhint %}

Review your own changes

```bash
git diff main | claude -p "Review these changes. Look for bugs, edge cases,
security issues, and style problems. Be specific about what to fix."
```

Review someone else's PR

```bash
gh pr diff 123 | claude -p "Review this PR. Focus on correctness and whether
the approach is sound. List any concerns."
```

Pre-commit review

```bash
git diff --staged | claude -p "Any issues with these staged changes?"
```

</details>

<details>

<summary>Git Workflows</summary>

Common Git tasks

```
# Create a well-structured commit
"Commit the current changes with a descriptive message"

# Interactive rebase help
"Squash the last 3 commits into one with a clean message"

# Branch management
"Create a feature branch from main called feature/sms-notifications"

# Resolve conflicts
"Help me resolve the merge conflicts in src/services/order.ts"
```

</details>

