---
icon: fishing-rod
---

# Hooks!

{% hint style="info" %}
List of all hooks template : [https://app.aitmpl.com/hooks](https://app.aitmpl.com/hooks)
{% endhint %}

<div data-full-width="true"><figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

#### **Hooks Run outside the Agent Loop** <a href="#id-104c" id="id-104c"></a>

`PreToolUse`, `PostToolUse`, and `Stop` — three hook points that most Claude Code users have never configured.

What makes them architecturally interesting: they execute **outside Claude’s main reasoning loop**. No tokens consumed. No task interruption. They’re side-channel automation attached to Claude’s actions, not part of Claude’s actions.

A few concrete uses:

**Auto-formatting on write**: A `PostToolUse` hook running `gofmt` after every Go file write means formatting is never something you ask Claude to do — it just happens.

**Guarded destructive operations**: The `/careful` pattern activates a `PreToolUse` hook that intercepts any irreversible action — file deletion, overwrite, branch force-push — and requires explicit confirmation before proceeding. You activate it before a risky refactor; it deactivates when the task completes.

**Completion verification**: Covered in pattern 11.



We configure two practical hooks for the RAG service. The post-tool hook runs our code formatter quietly after every write operation. The pre-tool hook defers any git push that targets the main branch.

```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/gate_git_push.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "uv run ruff format $CLAUDE_TOOL_FILE_PATH >/dev/null 2>&1 || true"
          }
        ]
      }
    ],
    "PermissionDenied": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "jq -c . >> .claude/logs/denied.jsonl"
          }
        ]
      }
    ]
  }
}
```
