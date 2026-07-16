---
icon: box-circle-check
---

# Claude Setting.json

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

How to make UI like this ?

{% code overflow="wrap" expandable="true" %}
```
code ~/.claude/settings.json
```
{% endcode %}

Then Paste this configs :&#x20;

{% code overflow="wrap" expandable="true" %}
```
"statusLine": {
    "type": "command",
    "command": "bash /Users/yourUser/.claude/statusline-command.sh",
    "padding": 0
  }
```
{% endcode %}

Now paste the file in the .claude system root folder :&#x20;

{% file src="../.gitbook/assets/statusline-command.sh" %}

More Statusline UI :thumbsup:

* [https://powerline.owloops.com/](https://powerline.owloops.com/)
* [https://github.com/sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline)  ( I am using  this)

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
More Claude Settings Tools Integration : [https://app.aitmpl.com/settings](https://app.aitmpl.com/settings)
{% endhint %}

<div data-full-width="true"><figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

In this section, we will explore the various settings available in Claude and how to configure them to optimize your experience. Claude environment variables will allow your to customize the behavior of Claude and tailor it to your specific needs.

#### Official Documentation

All of the claude code settings and environment variables are recorded in following website:

* [Environment Variables Documentation](https://code.claude.com/docs/en/env-vars)
* [Available Settings Documentation](https://code.claude.com/docs/en/settings#available-settings)

#### Global Claude Settings

Use global claude settings to apply common settings across all your projects.

```bash
code ~/.claude/settings.json
```

Examaple settings for environment:

```json
"env": {
    "cleanupPeriodDays": "120", //Default value for cleanupPeriodDays is 30 days.
    "BASH_MAX_OUTPUT_LENGTH": "150000", //Default value for BASH_MAX_OUTPUT_LENGTH is 30000.
},
```

**Disable analytics for claude code:**

```
"DISABLE_TELEMETRY": "1"
"DISABLE_ERROR_REPORTING": "1"
"CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY": "1"
```

#### Lock Permssion in Settings

{% code title="" overflow="wrap" lineNumbers="true" %}
```
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git status)",
      "Bash(git diff *)",
      "Read",
      "Write",
      "Edit"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)"
    ]
  }
}
```
{% endcode %}



{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}
