# Agentic Architecture & Orchestration

<figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

> Agentic Loop is a deterministic control flow pattern — not a prompt trick, not a retry loop, and not a chatbot turn

<figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

#### The Agentic Loop Lifecycle

The loop follows four steps, repeated until completion:

1. **Send a request** to Claude via the Messages API. This includes the conversation history (system prompt, prior messages, and any tool results from the previous iteration).
2. **Inspect the `stop_reason` field** in the response. This field is the authoritative signal for what happens next. It has two values relevant to agentic loops:
   * `"tool_use"` — Claude wants to call one or more tools. The loop continues.
   * `"end_turn"` — Claude has finished its work. The loop terminates.
3. **If `stop_reason` is `"tool_use"`**: execute the requested tool(s), append the tool results to the conversation history as a new message, and send the updated conversation back to Claude.
4. **If `stop_reason` is `"end_turn"`**: the agent has finished. Present the final response to the user.

The critical detail is step 3: tool results **must** be appended to conversation history. Without this, Claude cannot reason about the new information on the next iteration. The model needs to see what the tool returned in order to decide what to do next.

{% hint style="info" %}
The whole conversation is re-sent every iteration : Claude is stateless, so history accumulates and step 10 re-processes everything from steps 1–9. That's where your token cost lives.
{% endhint %}

<details>

<summary>Example : The scenario: a single <code>get_weather</code> tool, and a user question that forces exactly one tool round-trip before Claude finishes.</summary>

**Iteration 1** --Step 1 sends the user question. Claude decides it needs the tool, so the response has `stop_reason: "tool_use"` and a `tool_use` block instead of a final answer:

```json
{
  "id": "msg_01Abc...",
  "role": "assistant",
  "stop_reason": "tool_use",
  "content": [
    { "type": "text", "text": "Let me check the current weather in Dhaka." },
    {
      "type": "tool_use",
      "id": "toolu_01XyZ...",
      "name": "get_weather",
      "input": { "city": "Dhaka" }
    }
  ]
}
```

Step 2 reads `stop_reason` → it's `"tool_use"`, so Step 3 fires. Your code runs `get_weather("Dhaka")`, then appends **two** messages to history: Claude's assistant turn verbatim, and a new user message carrying the result. The critical bit is that `tool_use_id` must echo the `id` from the `tool_use` block:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01XyZ...",
      "content": "Dhaka: 31°C, humid, scattered thunderstorms."
    }
  ]
}
```

**Iteration 2** — Step 1 sends that expanded history back. Now Claude has the tool output and can answer, so this time `stop_reason` is `"end_turn"`:

```json
{
  "id": "msg_01Def...",
  "role": "assistant",
  "stop_reason": "end_turn",
  "content": [
    {
      "type": "text",
      "text": "It's 31°C in Dhaka with scattered thunderstorms, so yes — take the umbrella."
    }
  ]
}
```

Step 2 reads `stop_reason` → `"end_turn"` → Step 4 terminates the loop and returns the text.

Console output from the script:

```
[stop_reason = tool_use]
[stop_reason = end_turn]

FINAL: It's 31°C in Dhaka with scattered thunderstorms, so yes — take the umbrella.
```

A few things worth flagging, since a real loop rarely stays this tidy:

The whole conversation is re-sent every iteration — Claude is stateless, so history accumulates and step 10 re-processes everything from steps 1–9. That's where your token cost lives.

If Claude emits several `tool_use` blocks in one response (parallel calls), you run all of them and return all `tool_result` blocks in a _single_ user message. The loop in the script already handles this via the `for block in response.content` pass.

When a tool fails, return the error _as a `tool_result`_ rather than throwing — that way Claude can see what went wrong and retry, instead of the loop dying.

And `tool_use`/`end_turn` are only two of the values you'll see. Production code should also branch on `pause_turn` (server-tool loop hit its internal limit — re-send the response as-is to continue), `max_tokens` (output got truncated mid-JSON, which silently corrupts a tool call), and `refusal` (current models like Fable 5 can decline on a normal 200 response).

</details>

<mark style="color:$danger;">The exam consistently tests three specific anti-patterns for loop termination. Know these cold</mark>

* Checking if Claude said "I'm done" or "task complete" to determine whether the loop should end. This is wrong because natural language is inherently ambiguous
* Setting "stop after 10 loops" as the main way to terminate the agent. This is wrong because it either cuts off useful work
* Using `response.content[0].type == "text"` to decide the loop is finished. This is wrong because Claude can return text alongside `tool_use` blocks

{% hint style="danger" %}
Don't fall for this distractor : A plausible fix for premature termination
{% endhint %}

* **`tool_choice = "any"`** — the failure is a specific one: it prevents `end_turn` and therefore causes an **infinite loop**. Lock that cause-and-effect in
* Decision-making is **dynamic / model-driven**, and you correctly said critical logic should be **enforced programmatically** instead.

> The number-one beginner confusion: 'Claude runs the tool.' It does not. **Claude only REQUESTS a tool; your code executes it and appends the result**. Miss that and the whole loop stops making sense.

<figure><img src="../../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

* Sub agents never talk to each other everything done my coordinator
* What is coordinator?
* Coordinator has 4 Jobs
  * Decompose : break down tasks
  * Delegate : pass tasks to responsible agents
  * Aggregate : combining results
  * Evaluate & Re-delegate
* Sub-agents don't inherit Coordinator history and has isolated context, if they need anything that need to be written in prompt



In multi-agent systems, subagents operate with isolated context and do not automatically inherit the coordinator’s conversation history. The coordinator must explicitly include complete findings from prior agents in each subagent’s prompt. When a synthesis subagent is missing findings, the most common cause is that the coordinator failed to pass the complete results in the prompt.

<figure><img src="../../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

* Need to pass everything with well-defined in prompt of sub-agents



<figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>







<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>



Why not A & C

* Core Diff Legacy vs Agentic : We are not using pre connfigure deicision trees & hard codes
* LLM evaluates the new context non deterministically  and dynamically decides the next best decision
