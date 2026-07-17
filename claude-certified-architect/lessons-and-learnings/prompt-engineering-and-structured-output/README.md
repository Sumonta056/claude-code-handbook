# Prompt Engineering & Structured Output

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>



> biggest mistake in production prompt engineering is relying on vague instructions. Phrases like "be conservative," "only report high-confidence findings," or "use your best judgement" give the model no actionable decision boundary

The correct approach is **explicit categorical criteria** that define precisely what the model should flag and what it should skip. Compare these two system prompts for a CI/CD code review pipeline:

**Wrong approach:**

`Review this code. Be conservative. Only report high-confidence findings.`

**Correct approach:**

`Flag comments only when claimed behaviour contradicts actual code behaviour. Report bugs and security vulnerabilities. Skip minor style preferences and local patterns.`



**Prose description (insufficient):**

{% code overflow="wrap" %}
```
Critical: Issues that could cause system failures or data loss Minor: Issues that affect code readability but not functionality
```
{% endcode %}

**Code example approach (correct):**

{% code overflow="wrap" %}
```
Critical — Unsanitised user input in SQL query: query = f"SELECT * FROM users WHERE id = {user_input}" 
Minor — Inconsistent variable naming: userName vs user_name in the same module
```
{% endcode %}

<figure><img src="../../../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

{% columns %}
{% column %}
<figure><img src="../../../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column valign="middle" %}
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

When and How to retry?

* Specific feedback with exact validation errors instead of Blind Retries
* Know when retry is Futile : Fix format structure > Absent information from source



#### Important :thumbsup:

<figure><img src="../../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

