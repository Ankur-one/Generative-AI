import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

# Load environment variables from this project's .env file
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


async def main():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to your .env file."
        )

    client = MultiServerMCPClient(
        {
            "Math": {
                "command": sys.executable,
                "args": [str(BASE_DIR / "mathserver.py")],
                "transport": "stdio",
            },
            "Weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )

    # Discover tools from both MCP servers
    tools = await client.get_tools()

    print("Available MCP tools:")
    for tool in tools:
        print(f"- {tool.name}")

    # Use a Groq model ID available to your account
    model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)

    agent = create_agent(
    model=model,
    tools=tools,
    )

    agent = create_agent(model, tools)

    response = await agent.ainvoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What's (3 + 5) * 12? Use the math tools.",
            }
        ]
    }
)

    print("\nFinal answer:")
    print(response["messages"][-1].content)



    weather_response = await agent.ainvoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Get the weather for California using the get_weather tool.",
            }
        ]
    }
)

    print("\nWeather Response:")
    print(weather_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())