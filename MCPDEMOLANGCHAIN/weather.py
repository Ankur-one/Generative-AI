from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Weather",
    host="127.0.0.1",
    port=8000,
)


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the weather for a location."""
    return f"It's always raining in {location}."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")