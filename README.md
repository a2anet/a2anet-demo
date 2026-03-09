# A2A Net Demo

[![License](https://img.shields.io/github/license/a2anet/a2a-mcp)](https://github.com/a2anet/a2a-mcp/blob/main/LICENSE) [![A2A Protocol](https://img.shields.io/badge/A2A-Protocol-blue)](https://a2a-protocol.org) [![MCP](https://img.shields.io/badge/MCP-Protocol-orange)](https://modelcontextprotocol.io) [![Discord](https://img.shields.io/discord/1391916121589944320?color=7289da&label=Discord&logo=discord&logoColor=white)](https://discord.gg/674NGXpAjU)

This repository demonstrates how to use agents on [A2A Net](https://app.a2anet.com) with [LangGraph](https://www.langchain.com/langgraph) and the [A2A MCP server](https://github.com/a2anet/a2a-mcp). It also shows how to use them with the [A2A Python SDK](https://github.com/a2aproject/a2a-python).

## 📋 Requirements

To run the server you need to install uv if you haven't already.

MacOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 🚀 Quick Start

1. Install dependencies: `uv sync`
2. Create an account on [A2A Net](https://app.a2anet.com)
3. Go to [Dashboard](https://app.a2anet.com/dashboard)
4. Click "+ Create Key" > Create Key > Copy Your Key
5. Create an `.env` file: `cp .env.example .env`
6. Set `A2ANET_API_KEY` (and `OPENAI_API_KEY` if using LangGraph)

### LangGraph

To open the agent in [Agent Chat UI](https://docs.langchain.com/oss/python/langchain/ui):

```bash
uv run --env-file .env langgraph dev
```

To invoke the agent in the terminal:

```bash
uv run --env-file .env -m src.langchain
```

### A2A Python SDK

To send a message with the A2A Python SDK:

```bash
uv run --env-file .env src/a2a_sdk.py
```

## ⚙️ Configuration

By default the [A2A MCP server](https://github.com/a2anet/a2a-mcp) connects to [Reddit Search](https://app.a2anet.com/agent/JRHbiNo2kBy1um4z2oSa), [Tweet Search](https://app.a2anet.com/agent/7TaFj4YlbpngypjX74zl), [LinkedIn Profile Search](https://app.a2anet.com/agent/BpKQrB8yibpOjUGznfBa), [LinkedIn Company Search](https://app.a2anet.com/agent/kq0rkZgtsj7yaAMpxB02), and [LinkedIn Post Search](https://app.a2anet.com/agent/TEjZexmB5frVZi52Ne0j).

To add more agents:

1. Get the URL(s) of the agent(s) you want to use on [A2A Net](https://app.a2anet.com). E.g. [Indeed Job Search](https://app.a2anet.com/agent/0HHsPhXgjJexL1fglj57): `https://app.a2anet.com/agent/0HHsPhXgjJexL1fglj57`
2. Add `/agent-card.json` to the end of the URL(s) to get Agent Card URL(s). E.g. `https://app.a2anet.com/agent/0HHsPhXgjJexL1fglj57/agent-card.json`
3. Add the Agent Card URL(s) to `A2A_AGENT_CARDS` with `"custom_headers": {"X-API-Key": A2ANET_API_KEY}`

## 📄 License

`a2anet-demo` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.

## 🤝 Join the A2A Net Community

A2A Net is a site to find and share AI agents and open-source community. Join to share your A2A agents, ask questions, stay up-to-date with the latest A2A news, be the first to hear about open-source releases, tutorials, and more!

- 🌍 Site: [A2A Net](https://app.a2anet.com)
- 🤖 Discord: [Join the Discord](https://discord.gg/674NGXpAjU)
