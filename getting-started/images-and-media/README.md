---
icon: image-landscape
layout:
  width: default
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
  actions:
    visible: true
---

# Guidelines!

{% embed url="https://cc.storyfox.cz/" %}

> _End of the day : Whether you hand type or generate or copy paste, YOU ARE RESPONSIBLE, NOT THE AGENTS_

### Basic Guidelines for better use!

1. Managed token usage. It means we are going to get usage full month but with limitation. You are not going to run out in the middle of the month even if you want. You can empty your weekly limit but can't empty your entire months limit at once. With Copilot we can empty 300 Premium request in a single day.
2. Always <mark style="color:$success;">use</mark> <mark style="color:$success;"></mark><mark style="color:$success;">**plan mode**</mark>, Unnecessay context kills intelligence: Plan first. Add all the files you think the task need to touch. Review the plan then execute. I use a seperate chat and paste the plan there to execute. This reduces token usage.
3. Ask Claude to interview you using AskUserQuestion tool for a feature Implement
4. Use cleanup command i.e `/clear` after completing a task. Don't drag chats.
5. Close chats after each task instead of letting them sprawl. When a chat must continue, ask Claude to summarize the state in 500 words, open a fresh chat, and paste the summary. You just replaced 10,000 tokens with 500.
6. Use Default to Sonnet. Only reach for Opus on gnarly multi-file refactors or hard debugging. Also try to use Haiku for basic question asking and chats!
7. Opus & Sonnet has effort parameter (LOW | MEDIUM | HIGH) you can control how much effort you think that problem should require. This is a real deal that how much effort do you think the Agent might require to find out the problem or you are handing over the solution to your agent and expecting agent just applying it for you. Use effort parameter wisely to manage your token.
8.  Use hooks for things that should happen every time

    Formatting, validation, guardrails, notifications - anything deterministic is better handled by the system than by hoping the model remembers.

> Claude.md : Keep the most important constraints at the very top. Claude Code has primacy bias. The first things it reads stick hardest.

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

If I had to pick one habit that signals good context management, it’s rewind.

\
In Claude Code, `double-tapping Esc(or running /rewind)` lets you jump back to any previous message and re-prompt from there. The messages after that point are dropped from the context.

\
Rewind is often the better approach to correction. For example, Claude reads five files, tries an approach, and it doesn't work. Your instinct may be to type "that didn't work, try X instead." but the better move is to rewind to just after the file reads, and re-prompt with what you learned. "Don't use approach A, the foo module doesn't expose that — go straight to B."

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

\
You can also use “summarize from here” to have Claude summarize its learnings and create a handoff message, kind of like a message to the previous iteration of Claude from its future self that tried something and it didn’t work.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

> [Using Claude Code: Session Management & 1M Context](https://x.com/trq212/status/2044548257058328723)

### Be Careful!

* You don't need all those MCPs: <mark style="color:$danger;">MCP usages a lot of tokens</mark>. I removed Context7 as most of the AGENT can web search now. I use only Click up and MongoDB MCP. You can now enable project based MCPs so turn on and off as needed.
* Make Sure Claude.md is under 120 Lines! This is a fixed cost token usage in every request. If some instruction is not needed in each chat move the knowledge in a seperate \[INSTRUCTION].md file
* No matter what <mark style="color:$danger;">Agents are also Lazy</mark>. They will use magic variables, duplicate function, won't apply design principals even though they are instructed. After completing a task you must check and apply your knowledge and sanitize the code.
* <mark style="color:$danger;">Stop uploading PDFs</mark>. Convert to markdown first. A 10-page PDF drops from 8,000 tokens to about 2,500. Same content.



### Extra Tricks!

1. `/btw` :  side chain conversations while Claude works
2. Use `/save`, `/resume`, `/rewind` etc in your workflow
3. Use MCP to let Claude see Chrome console logs
4. Take screenshots and share with Claude when stuck



### Good To know!

<mark style="color:$success;">Session limitation</mark> : The Claude Pro subscription works with a \~5-hour session window and has token/message limits per model.

* You will be blocked for the rest of the session (up to \~5 hours)
* You cannot continue working during that time&#x20;
* No fallbacks like Copilot or Codex tool for using lower models

Once you hit the limit: Example (approx, varies by usage):

* Sonnet: \~80–100 messages / 5 hours
* Opus: \~40–50 messages / 5 hours

<br>

### In Claude if you hit the limit:

1. You can start working on different task which doesn't require AI assistance.
2. &#x20;You can use /extra-usage to continue work if you get credit from your organization.
3. You can export your session from Claude and feed to another ai tool/model if you have other subscription.
4. You can resume your Claude Code season from the point where you have stopped. (Though this is going to be costly as we are seeing a tendency that model/tool providers are reducing Caching time and experimenting with it.)
5. You session will not be lost and the token that you spent will not be waste totally. But if you have urgency then you can't work with AI in that time if you have no way out.

<br>

{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}

#### Master Claude Commands !

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

