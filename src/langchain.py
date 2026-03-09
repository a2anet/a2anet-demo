import asyncio
import json
import os

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI

from src.prompt import SYSTEM_PROMPT


def get_agent():
    # Set up A2A MCP server
    A2ANET_API_KEY: str = os.environ["A2ANET_API_KEY"]

    A2A_AGENT_CARDS = [
        # Reddit Search
        {
            "url": "https://app.a2anet.com/agent/JRHbiNo2kBy1um4z2oSa/agent-card.json",
            "custom_headers": {"X-API-Key": A2ANET_API_KEY},
        },
        # Tweet Search
        {
            "url": "https://app.a2anet.com/agent/7TaFj4YlbpngypjX74zl/agent-card.json",
            "custom_headers": {"X-API-Key": A2ANET_API_KEY},
        },
        # LinkedIn Profile Search
        {
            "url": "https://app.a2anet.com/agent/BpKQrB8yibpOjUGznfBa/agent-card.json",
            "custom_headers": {"X-API-Key": A2ANET_API_KEY},
        },
        # LinkedIn Company Search
        {
            "url": "https://app.a2anet.com/agent/kq0rkZgtsj7yaAMpxB02/agent-card.json",
            "custom_headers": {"X-API-Key": A2ANET_API_KEY},
        },
        # LinkedIn Post Search
        {
            "url": "https://app.a2anet.com/agent/TEjZexmB5frVZi52Ne0j/agent-card.json",
            "custom_headers": {"X-API-Key": A2ANET_API_KEY},
        },
    ]

    client = MultiServerMCPClient(
        {
            "a2a": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["a2anet-mcp"],
                "env": {"A2A_AGENT_CARDS": json.dumps(A2A_AGENT_CARDS)},
            },
        }
    )

    # Create production-ready agent
    model = ChatOpenAI(model="gpt-5.1", reasoning={"effort": "medium"})
    tools = asyncio.run(client.get_tools())
    agent = create_agent(model, tools=tools, system_prompt=SYSTEM_PROMPT)

    return agent


agent = get_agent()


async def main():
    # Send message to agent
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What agents do you have access to?"}]}
    )

    # Print messages
    for message in result["messages"]:
        message.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())
