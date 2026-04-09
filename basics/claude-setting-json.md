---
icon: box-circle-check
---

# Claude Setting.json

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

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
