---
icon: markdown
---

# MCP Servers!

<figure><img src="https://gitbookio.github.io/onboarding-template-images/markdown-hero.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
I will try to list out some of the famous MCP servers of Claude. You can try it in the project; at least I use it on a daily basis in my project and there are GitHub links.
{% endhint %}

Create a `.mcp.json` file in project directory :&#x20;

```json
{
  "mcpServers": { }
}

```

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







