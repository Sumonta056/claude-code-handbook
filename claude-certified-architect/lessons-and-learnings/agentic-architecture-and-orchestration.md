# Agentic Architecture & Orchestration

<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

`stop_reason`&#x20;

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

* Sub agents never talk to each other everything done my coordinator
* What is coordinator?
* Coordinator has 4 Jobs
  * Decompose : break down tasks
  * Delegate : pass tasks to responsible agents
  * Aggregate : combining results
  * Evaluate & Re-delegate
* Sub-agents don't inherit Coordinator history and has isolated context, if they need anything that need to be written in prompt



In multi-agent systems, subagents operate with isolated context and do not automatically inherit the coordinator’s conversation history. The coordinator must explicitly include complete findings from prior agents in each subagent’s prompt. When a synthesis subagent is missing findings, the most common cause is that the coordinator failed to pass the complete results in the prompt.

<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

* Need to pass everything with well-defined in prompt of sub-agents



<figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>





