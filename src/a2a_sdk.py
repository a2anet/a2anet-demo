import asyncio
import json
import os
import uuid
from traceback import print_stack

import httpx
from a2a.client import A2ACardResolver, A2AClient
from a2a.types import (
    AgentCard,
    Message,
    MessageSendParams,
    Part,
    Role,
    SendMessageRequest,
    SendMessageResponse,
    SendMessageSuccessResponse,
    Task,
    TextPart,
)


def print_str(string: str):
    if len(string) <= 50_000:
        print(string)
    else:
        print(string[:25_000] + "\n...\n" + string[-25_000:])


async def main():
    A2ANET_API_KEY: str = os.environ["A2ANET_API_KEY"]

    async with httpx.AsyncClient(
        timeout=600, headers={"X-API-Key": A2ANET_API_KEY}
    ) as httpx_client:
        # Get Agent Card
        # LinkedIn Job Search
        resolver = A2ACardResolver(
            httpx_client=httpx_client,
            base_url="https://app.a2anet.com",
            agent_card_path="/agent/JU7NwRV5eF8pd56bpUtd/agent-card.json",
        )
        agent_card: AgentCard = await resolver.get_agent_card()
        print_str(agent_card.model_dump_json(indent=4))

        # Initialize A2A Client
        client: A2AClient = A2AClient(httpx_client=httpx_client, agent_card=agent_card)

        # Send Message
        send_message_request = SendMessageRequest(
            id=str(uuid.uuid4()),
            params=MessageSendParams(
                message=Message(
                    message_id=str(uuid.uuid4()),
                    parts=[
                        Part(
                            root=TextPart(
                                text=(
                                    "Find me AI Engineer roles in San Francisco. "
                                    "Then, filter to keep only the roles at startups with equity. "
                                    "Don't analyse the results or ask for my confirmation."
                                )
                            )
                        )
                    ],
                    role=Role.user,
                )
            ),
        )
        send_message_response: SendMessageResponse = await client.send_message(send_message_request)
        print_str(send_message_response.model_dump_json(indent=4))

        # Get Artifacts
        if isinstance(send_message_response.root, SendMessageSuccessResponse) and isinstance(
            send_message_response.root.result, Task
        ):
            if send_message_response.root.result.artifacts:
                for artifact in send_message_response.root.result.artifacts:
                    print_str(artifact.model_dump_json(indent=4))


if __name__ == "__main__":
    asyncio.run(main())
