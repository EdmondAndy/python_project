import asyncio
from datetime import datetime, timezone
from random import randint
from typing import Annotated

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIAssistantsClient
from pydantic import Field

"""
OpenAI Assistants with Function Tools Example

This sample demonstrates function tool integration with OpenAI Assistants,
showing both agent-level and query-level tool configuration patterns.
"""


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."


def get_time() -> str:
    """Get the current UTC time."""
    current_time = datetime.now(timezone.utc)
    return f"The current UTC time is {current_time.strftime('%Y-%m-%d %H:%M:%S')}."

agent = ChatAgent(
    chat_client=OpenAIAssistantsClient(),
    instructions="You are a helpful assistant that can provide weather and time information.",
    tools=[get_weather, get_time],  # Tools defined at agent creation
)

# async def main() -> None:
def main():
    print("=== OpenAI Assistants Chat Client Agent with Function Tools Examples ===\n")

    import logging

    from agent_framework.devui import serve

    #setup logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger = logging.getLogger(__name__)

    logger.info("Starting DevUI on http://localhost:7860")
    logger.info("Entity ID: agent_framework_devui")
    serve(entities=[agent], port=7860, auto_open=True)

    # await tools_on_agent_level()
    # await tools_on_run_level()
    # await mixed_tools_example()


if __name__ == "__main__":
    # asyncio.run(main())
    main()