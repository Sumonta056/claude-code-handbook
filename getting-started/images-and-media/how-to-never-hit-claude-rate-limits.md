---
cover: ../../.gitbook/assets/claude2.png
coverY: 0
layout:
  width: default
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
---

# How to Never Hit Claude Rate Limits!

> This is a must read blog to understand the Claude Cache System and How to utilize the cache:&#x20;
>
> [Prompt Caching: From Zero to Architecture](https://foyzul.substack.com/p/prompt-caching-from-zero-to-architecture?r=9rews\&utm_campaign=post-expanded-share\&utm_medium=linkedin\&mytag=myvalue\&triedRedirect=true)

{% hint style="warning" %}
Claude re-reads the entire conversation of every single message.\
Not just your last prompt.\
Everything.\
Message 20 = 105K tokens. Message 30 = 232K tokens.
{% endhint %}

{% hint style="danger" %}
The two biggest levers: model choice and conversation length. Most people get both wrong.
{% endhint %}

{% stepper %}
{% step %}
### Use the right model

* Haiku handles 50% of daily work. Haiku → quick replies, formatting, simple tasks
* Sonnet covers the next of work. Sonnet → default for writing, analysis, coding
* Opus is for the 5% that genuinely needs it. Opus → deep reasoning only. Not for everything.

> Don't leave Opus on and burn through your limit. Opus costs 5× more per message. Stop using it as your default. Turn off Extended Thinking unless you actually need it.
{% endstep %}

{% step %}
### Turn off the token burners

* Extended Thinking doubles your usage.
* Web Search enabled adds 2 to 3x.
* Connectors add 1.5 to 2x
* MCP usages 2x more token

> Leave them all off by default and only turn them on when the task demands it.
{% endstep %}

{% step %}
### Fresh chat every 15–20 messages

* Message 1 costs around 200 tokens.
* By message 15 you are spending 10,000.
* By message 30 a single question costs 50,000+.

> Summarise what you have, open a new chat, paste it in.

Long chats are expensive chats. Every message pays for all previous ones.\
At message \~15, prompt: "Summarize all decisions, constraints, current state."

{% hint style="success" %}
Tricks : Copy summary (500–1,500 tokens) → Open new chat → Paste as first message → Zero context wasted. No tokens burned re-explaining.
{% endhint %}
{% endstep %}

{% step %}
### Batch questions into one

* Three messages means three context loads.
* One combined message means one load.
* Claude sees the full picture at once.

The answers are better too.

> ❌ "Summarize this." wait. "List main points." wait. "Suggest headline."\
> ✅ "Summarize this, list main points as bullets, suggest a headline." — one context load.
{% endstep %}

{% step %}
### Spread your work across the day

* Claude runs on a 5-hour rolling window.
* Burn through it in one session and you wait.
* Split into 2 to 3 sessions and quota frees up.

Space your work and your oldest messages expire automatically.

{% hint style="info" %}
If you work 9-5, then send a small message to Claude at 8 am, this will create a new 5 hour sessions, so after 1 pm, you can have another 5 hour window session
{% endhint %}
{% endstep %}

{% step %}
### Use Projects for repeat files

* Same PDF in five chats costs five token loads.
* Projects cache your uploaded files once.
* Every new chat reads them free.

Upload once and stop wasting tokens on the same file.
{% endstep %}

{% step %}
### Store your context once

* Memory for Chat.
* CLAUDE.md for Code.
* Skills for repeated workflows.

Write these once. Never repeat yourself.
{% endstep %}

{% step %}
### Fix your context file

Your Claude.md should be under 2,000 words or 120 lines. Not 10,000. Not "everything about project."&#x20;

What to keep: Go through this [integrations.md](../../basics/integrations.md "mention")

What to remove: → Lengthy writing samples → Repeated instructions → Old project context → Anything you haven't used in 30 days
{% endstep %}

{% step %}
### Rewinding Instead of Correcting

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

If I had to pick one habit that signals good context management, it’s rewind.

\
In Claude Code, `double-tapping Esc(or running /rewind)` lets you jump back to any previous message and re-prompt from there. The messages after that point are dropped from the context.

\
Rewind is often the better approach to correction. For example, Claude reads five files, tries an approach, and it doesn't work. Your instinct may be to type "that didn't work, try X instead." but the better move is to rewind to just after the file reads, and re-prompt with what you learned. "Don't use approach A, the foo module doesn't expose that — go straight to B."

\
You can also use “summarize from here” to have Claude summarize its learnings and create a handoff message, kind of like a message to the previous iteration of Claude from its future self that tried something and it didn’t work.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

> [Using Claude Code: Session Management & 1M Context](https://x.com/trq212/status/2044548257058328723)
{% endstep %}

{% step %}
### Master the Cache!

This is a must read blog to understand the Claude Cache System and How to utilize the cache: [Prompt Caching: From Zero to Architecture](https://foyzul.substack.com/p/prompt-caching-from-zero-to-architecture?r=9rews\&utm_campaign=post-expanded-share\&utm_medium=linkedin\&mytag=myvalue\&triedRedirect=true)

**Five things that kill your cache (Don’ts): Cache kills mean more token use!**

1. `/clear` : nukes the entire cached prefix
2. Auto-compaction : rewrites old turns, invalidates everything below
3. Tool definitions changing mid-session : reshuffles the prefix
4. Edits near the top of the request : collapses the whole tower
5. Idle gaps longer than 5 minutes : the cache expires silently

```
The practical implication:

  Fast iteration (< 5 min gaps):    Slow, thoughtful work (> 5 min gaps):

  Turn 1 → cache write               Turn 1 → cache write
  Turn 2 (30s later) → cache hit ✓   ...8 minutes pass...
  Turn 3 (45s later) → cache hit ✓   Turn 2 → cache MISS, full recompute ✗
  Turn 4 (20s later) → cache hit ✓   ...12 minutes pass...
  Turn 5 (1m later)  → cache hit ✓   Turn 3 → cache MISS, full recompute ✗

  Hit rate: ~80%+                     Hit rate: ~0%
  Cost: $                             Cost: $$$$
```

**Principles for cache-friendly work (Dos):**

1. The rule isn’t “don’t have many skills installed.” It’s more nuanced:

> Don’t have Claude speculatively invoke skills you don’t need. Each invoked skill body permanently adds to your context, eating context-window budget and bringing auto-compaction closer. But the skills you don’t invoke cost you nothing.

2. Don't let claude figure out, you must specify files

Telling Claude _which_ file to read is one round trip. Telling Claude to “go figure out the codebase” is twenty round trips, twenty output-token bursts, and twenty file contents bloating the context forever. Same answer, very different bill. The goal isn’t to eliminate tool calls it’s to make every tool call a directed one.

```
What "let Claude figure it out" actually costs:

  Directed prompt               Exploratory prompt
  (you specify the files)       ("go figure out the codebase")
  ─────────────────────         ──────────────────────────────
  Round trips:     3            Round trips:     30
  Output tokens:   ~1K          Output tokens:   ~10K
  Context bloat:   3 files      Context bloat:   30 files
  Cache hit rate:  high ✓       Cache hit rate:  high ✓  ← same!
  Total cost:      $            Total cost:      $$$$$$$$
```

3. **State the goal at turn one.** Course-corrections at turn 15 don’t directly invalidate the cache (they just append), but they waste context window space on misunderstandings, which brings auto-compaction closer. A clear goal upfront is cache-friendly via the context-window-pressure path. It’s also just better prompting, but the cache angle adds a real cost reason.

The cache rewards a certain kind of discipline: **focused sessions, directed tool use, eager context loading, and velocity**. Understanding these mechanics is the difference between a cheap day and a very expensive one.

<br>
{% endstep %}

{% step %}
###

`/insights`

Generate a report analyzing your Claude Code sessions, including project areas, interaction patterns, and friction points. it will create a html file giving you insights about how you are using claude, what's working, whats hindering quick wins that one can implement

`/recap`&#x20;

f

`/compact`&#x20;


{% endstep %}

{% step %}
###


{% endstep %}

{% step %}
###


{% endstep %}
{% endstepper %}

***

> Remember :  The tool isn't the problem. The habits are.Fix the habits once. You'll never complain about limits again.

{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
