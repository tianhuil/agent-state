"""Main MCP server module with agent state and log management tools."""

from pathlib import Path

from fastmcp import FastMCP

INSTRUCTIONS = """This MCP server provides state and log management tools for long-lived agents.

State Management:
- State represents what the agent is currently trying to do and is updated as the agent progresses
- The state file (.agent-state.txt) is replaced each time it's updated
- Use update_state() to save the current state, and load_state() to retrieve it

Log Management:
- The log file (.agent-log.txt) is an append-only history of what the agent has been doing
- Use log_event() to append new events to the log
- Use load_log() to retrieve the most recent log entries

This is designed for agents that may be interrupted, allowing future agent
sessions to continue where previous sessions left off by loading the state and
reviewing recent log entries."""

# Create the MCP server instance
mcp = FastMCP("Agent State MCP Server", instructions=INSTRUCTIONS)

# File paths
STATE_FILE = Path(".agent-state.txt")
LOG_FILE = Path(".agent-log.txt")


@mcp.tool()
def update_state(state: str) -> None:
    """Update the agent state file, replacing its contents.

    Args:
        state: The current state description of what the agent is trying to do

    """
    STATE_FILE.write_text(state, encoding="utf-8")


@mcp.tool()
def load_state() -> str:
    """Load the current agent state from the state file.

    Returns:
        The current state string, or empty string if the file doesn't exist

    """
    if not STATE_FILE.exists():
        return ""
    return STATE_FILE.read_text(encoding="utf-8")


@mcp.tool()
def log_event(message: str) -> None:
    """Append an event message to the log file.

    Args:
        message: The event message to append to the log

    """
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"{message}\n")


@mcp.tool()
def load_log(num_chars: int) -> str:
    """Load the last num_chars characters from the log file.

    Args:
        num_chars: The number of characters to retrieve from the end of the log

    Returns:
        The last num_chars characters from the log, or the entire log if it's shorter

    """
    if not LOG_FILE.exists():
        return ""
    content = LOG_FILE.read_text(encoding="utf-8")
    if len(content) <= num_chars:
        return content
    return content[-num_chars:]


if __name__ == "__main__":
    mcp.run()
