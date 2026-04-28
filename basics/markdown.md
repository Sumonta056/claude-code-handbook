---
icon: markdown
---

# MCP Servers!

{% hint style="info" %}
I will try to list out some of the famous MCP servers of Claude. You can try it in the project; at least I use it on a daily basis in my project and there are GitHub links.
{% endhint %}

### What Is MCP?

MCP (Model Context Protocol) is an open standard that lets Claude connect to external tools, data sources, and services — extending what Claude can do beyond its built-in capabilities.

Think of MCP servers as **plugins for Claude**: each server exposes a set of tools that Claude can call, just like any built-in tool (Read, Write, Bash, etc.).

MCP servers are configured in a `.mcp.json` file at the project root. Claude Code reads this file on startup and connects to all listed servers.

Project Structure :

```
claude-workshop/
├── .mcp.json              ← MCP server config (project-level)
├── .claude/
│   └── settings.json
```

Create a `.mcp.json` file in project directory :&#x20;

```json
{
  "mcpServers": { }
}
```

You can also configure MCP globally in `~/.claude/settings.json` for servers you want available in every project.

In Claude Code, run:

```
/mcp
```

You should see your mcp listed as a connected server with its available tools.

***

#### MCP Server Configuration's

#### MongoDB Server

{% code overflow="wrap" lineNumbers="true" expandable="true" %}
```json
{
  "mcpServers": {
    "mongodb": {
      "command": "npx",
      "args": [
        "-y",
        "@mongodb-js/mongodb-mcp-server",
        "--connectionString",
        "mongodb+srv://your_url"
      ]
    }
  }
}

```
{% endcode %}

#### GitHub CLI

Link : [https://cli.github.com/](https://cli.github.com/)

GitHub CLI  can do many things for you in the GitHub, like pushing your branch, everything related to GitHub you can do and tell claude to do it for you. In that case claude can have the GitHub CLI and cp to have access to all of these things

#### Chrome DevTools MCP

Your agent finally sees your web the exact tabs, cookies, dashboards, Linear boards, Notion pages, and internal tools you already have open.

This is the moment the biggest friction in browser agents disappeared.

Google shipped native DevTools MCP live-session attach (Chrome 146+), and tools like OpenClaw and Browser Use instantly plugged in

Link : [https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session](https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session)

#### More tools :&#x20;

* Clickup MCP : [https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)
* Postman MCP Server : [https://github.com/postmanlabs/postman-mcp-server](https://github.com/postmanlabs/postman-mcp-server)

#### **Context7**

Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors

Link : [https://github.com/upstash/context7](https://github.com/upstash/context7)

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

#### **Sequential-thinking**

An MCP server implementation that provides a tool for dynamic and reflective problem-solving through a structured thinking process.

**Link :** [https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

#### Need More ?

{% hint style="info" %}
Go to this website : [https://app.aitmpl.com/mcps](https://app.aitmpl.com/mcps)
{% endhint %}

<div data-full-width="true"><figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure></div>





{% hint style="success" %}
**A small request:**

Would You like donate a small amount : [**Click Here**](https://forms.gle/S1FJaEpzGcnMQbm77)

_If you find value in what we’re doing, please **subscribe to My YouTube channel** & Newsletter and **share this initiative** with others in your network. Together, we can build a stronger tech community._&#x20;

**Want to learn a topic like this? \[**[**Subscribe to My YouTube Channel**](https://www.youtube.com/@LearnCodewithPS5638)**]**

**Code & Career Golpo Newsletter:** [Subscribe to My Newsletter](https://www.linkedin.com/newsletters/code-career-golpo-7309186050084544512/)
{% endhint %}

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>
