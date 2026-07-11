# Page 2

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
