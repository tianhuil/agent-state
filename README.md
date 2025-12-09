# Agent State MCP Server

A Model Context Protocol (MCP) server built with FastMCP that provides agent state and log management tools for long-lived agents that may be interrupted and resumed.

## Features

- State management tools for tracking agent progress
- Log management tools for maintaining append-only event history
- Built with FastMCP for easy MCP server development
- Type-safe Python code with proper type hints

## Setup

### Prerequisites

- Python 3.14+
- `uv` package manager

### Installation

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Activate the virtual environment (if needed):
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

## Running the Server

Run the MCP server:
```bash
uv run python main.py
```

## Setting up MCP in Claude Desktop

1. Open Claude Desktop settings:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. Add the MCP server configuration:
   ```json
   {
     "mcpServers": {
       "agent-state": {
         "command": "uv",
         "args": [
           "run",
           "python",
           "[install directory]/agent-state/main.py"
         ]
       }
     }
   }
   ```

3. **Important**: Update the paths in the configuration:
   - Replace `[install directory]/agent-state` with the absolute path to this project on your system
   - Ensure the path uses forward slashes on all platforms

4. Restart Claude Desktop for the changes to take effect.

## Setting up MCP in Cursor (OpenCode)

1. Open Cursor settings:
   - Press `Cmd+,` (macOS) or `Ctrl+,` (Windows/Linux) to open settings
   - Or go to `File > Preferences > Settings`

2. Search for "MCP" in the settings

3. Add the MCP server configuration in your settings JSON:
   ```json
   {
     "mcp.servers": {
       "agent-state {
         "command": "uv",
         "args": [
           "run",
           "python",
           "[install directory]/agent-state/main.py"
         ]
       }
     }
   }
   ```

4. **Important**: Update the paths in the configuration:
   - Replace `[install directory]/agent-state` with the absolute path to this project on your system
   - Use forward slashes for paths even on Windows

5. Restart Cursor for the changes to take effect.

## Alternative: Using the virtual environment directly

If you prefer to use the virtual environment's Python directly:

1. Find the path to your virtual environment's Python:
   ```bash
   which uv run python  # Shows the resolved path
   ```

2. Use that path in your MCP configuration instead of `uv run python`.

## Development

### Code Quality

- Run linting:
  ```bash
  uv run ruff check .
  ```

- Run type checking:
  ```bash
  uv run pyright
  ```

- Format code:
  ```bash
  uv run ruff format .
  ```

### Project Structure

- `main.py` - Main MCP server with agent state and log management tools
- `AGENTS.md` - Coding style guidelines for this project
- `pyproject.toml` - Project configuration and dependencies

## License

MIT

