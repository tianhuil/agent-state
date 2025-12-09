"""Main MCP server module with agent state and log management tools."""

from pathlib import Path

from fastmcp import FastMCP

INSTRUCTIONS = """
This MCP server provides state and log management tools for long-lived agents.

IMPORTANT: All tools require a `directory` parameter as the first argument. This
must be the absolute path to the GitHub worktree or GitHub repository directory
where you want the state and log files to be saved.

State Management: - State represents what the agent is currently trying to do
and is updated as the agent progresses - The state file (.agent-state.txt) is
replaced each time it's updated - Use update_state(directory, state) to save the
current state - Use load_state(directory) to retrieve it

Log Management: - The log file (.agent-log.txt) is an append-only history of
what the agent has been doing - Use log_event(directory, message) to append new
events to the log - Use load_log(directory, num_chars) to retrieve the most
recent log entries

This is designed for agents that may be interrupted, allowing future agent
sessions to continue where previous sessions left off by loading the state and
reviewing recent log entries.

Example usage: - update_state("/path/to/your/worktree", "Working on feature X")
- load_state("/path/to/your/worktree") - log_event("/path/to/your/worktree",
"Completed step 1") - load_log("/path/to/your/worktree", 1000)
""".strip()

# Create the MCP server instance
mcp = FastMCP("Agent State MCP Server", instructions=INSTRUCTIONS)


def get_state_file(directory: str) -> Path:
    """Get the path to the state file in the specified directory.

    Args:
        directory: Absolute path to the GitHub worktree or repository directory

    Returns:
        Path to the state file

    """
    worktree = Path(directory)
    if not worktree.is_absolute():
        msg = f"Directory must be an absolute path: {directory}"
        raise ValueError(msg)
    if not worktree.exists():
        msg = f"Directory does not exist: {directory}"
        raise ValueError(msg)
    if not worktree.is_dir():
        msg = f"Path is not a directory: {directory}"
        raise ValueError(msg)
    return worktree / ".agent-state.txt"


def get_log_file(directory: str) -> Path:
    """Get the path to the log file in the specified directory.

    Args:
        directory: Absolute path to the GitHub worktree or repository directory

    Returns:
        Path to the log file

    """
    worktree = Path(directory)
    if not worktree.is_absolute():
        msg = f"Directory must be an absolute path: {directory}"
        raise ValueError(msg)
    if not worktree.exists():
        msg = f"Directory does not exist: {directory}"
        raise ValueError(msg)
    if not worktree.is_dir():
        msg = f"Path is not a directory: {directory}"
        raise ValueError(msg)
    return worktree / ".agent-log.txt"


@mcp.tool()
def update_state(directory: str, state: str) -> None:
    """Update the agent state file, replacing its contents.

    Args:
        directory: Absolute path to the GitHub worktree or repository directory
                   where the state file should be saved
        state: The current state description of what the agent is trying to do

    """
    state_file = get_state_file(directory)
    state_file.write_text(state, encoding="utf-8")


@mcp.tool()
def load_state(directory: str) -> str:
    """Load the current agent state from the state file.

    Args:
        directory: Absolute path to the GitHub worktree or repository directory
                   where the state file is located

    Returns:
        The current state string, or empty string if the file doesn't exist

    """
    state_file = get_state_file(directory)
    if not state_file.exists():
        return ""
    return state_file.read_text(encoding="utf-8")


@mcp.tool()
def log_event(directory: str, message: str) -> None:
    """Append an event message to the log file.

    Args:
        directory: Absolute path to the GitHub worktree or repository directory
                   where the log file should be saved
        message: The event message to append to the log

    """
    log_file = get_log_file(directory)
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"{message}\n")


@mcp.tool()
def load_log(directory: str, num_chars: int) -> str:
    """Load the last num_chars characters from the log file.

    Args:
        directory: Absolute path to the GitHub worktree or repository directory
                   where the log file is located
        num_chars: The number of characters to retrieve from the end of the log

    Returns:
        The last num_chars characters from the log, or the entire log if it's shorter

    """
    log_file = get_log_file(directory)
    if not log_file.exists():
        return ""
    content = log_file.read_text(encoding="utf-8")
    if len(content) <= num_chars:
        return content
    return content[-num_chars:]


if __name__ == "__main__":
    mcp.run()
