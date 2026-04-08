---
icon: image-landscape
---

# Guidelines!

{% embed url="https://cc.storyfox.cz/" %}



1. Always use **plan mode**, give Claude a way to verify
2. Ask Claude to interview you using AskUserQuestion tool
3. /btw  :  side chain conversations while Claude works
4. Use cross-model (Claude Code + Codex) to review your plan
5. Use MCP to let Claude see Chrome console logs
6. Take screenshots and share with Claude when stuck

\
1\. Unnecessay context kills intelligence: Plan first. Add all the files you think the task need to touch. Review the plan then execute. I use a seperate chat and paste the plan there to execute. This reduces token usage.\
\
2\. You don't need all those MCPs: MCP usages a lot of tokens. I removed Context7 as most of the AGENT can web search now. I use only figma MCP. You can now enable project based MCPs so turn on and off as needed.\
\
3\. Token Thriftiness is a skill: There are limits and I think the limits are going be increased, cost of the api will also. So If your [AGENTS.md](http://agents.md/) is long you must compress it. If some instruction is not needed in each chat move the knowledge in a seperate \[INSTRUCTION].md file. Use seperate free account or agent in chat to create implemention instructions.\
\
4\. If there are multiple developers you will need your own [AGENTS.md](http://agents.md/)\
\
5\. If you create a workflow dump that knowledge in a new agent/\[workflow]-[knowledge.md](http://knowledge.md/) file.\
\
6\. Use cleanup command i.e /clear after completing a task. Don't drag chats.\
\
7\. Use /save, /resume, /rewind etc in your workflow. Each cli has their own implementation. Read that Documentation you will be surprize. Keep uptodate with changelog.\
\
8\. Use git stage as your restore point. Example If the AGENT's output is 50% ok but needs tinkering then stage that change then give new instruction. Keep the stage area clean. I find the vscode git diff viewer much helpful to keep track of the file changes.\
\
9\. VsCode has a feature to open terminal in editor area and manage them like tabs. Opening multiple terminal for multiple task is breeze. Use keyboard shortcuts.\
{"key": "alt+t alt+t",\
"command": "workbench.action.createTerminalEditor",\
"when": "terminalProcessSupported",}\
\
10\. Agents WILL forget and won't follow [CLAUDE.md](http://claude.md/) or [GEMINI.md](http://gemini.md/).\
\
11\. Agents are also Lazy. They will use magic variables, duplicate function, won't apply design principals even though they are instructed. After completing a task you must check and apply your knowledge and sanitize the code.\
\
12\. Use Strict Linting i.e biome\
\
13\. Whether you hand type or generate or copy paste\
YOU ARE RESPONSIBLE, NOT THE AGENTS\
\
Fullstack specific findings:\
1\. They add unnecessary tailwind classes, tags, states.\
2\. The balance between server component and client component must be handle by you. They tends to lean to one approach.\
3\. Custom hooks, Utils, Constanst are mystery to them. Any Utils or Custom hook should have proper doccumentation. I use TS and JsDoc.\
4\. Modern web or framework feature are often ignored by them.

<br>



<br>

<br>
