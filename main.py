"""Main MCP server module with addition tool."""

from fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("Addition MCP Server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: The first number to add
        b: The second number to add

    Returns:
        The sum of a and b

    """
    return a + b


if __name__ == "__main__":
    mcp.run()
