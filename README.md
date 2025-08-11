# MCP-Context

## Overview
MCP-Context is an AI-powered project designed to provide persistent, portable user context for any LLM (Large Language Model) application that supports MCP servers. The goal is to ensure that user information, preferences, and context are always up-to-date and available across different platforms and AI tools, eliminating the need to re-establish context when switching between tools or starting new conversations.

## Features
- **Single Source of Truth:** All user information is stored in a local `context.json` file, which acts as the definitive context for the user.
- **FastMCP Integration:** The project uses FastMCP to expose tools for reading and updating user context.
- **Stateless HTTP API:** The server runs as a stateless HTTP service, making it easy to integrate with other applications.
- **Easy Context Updates:** User information can be updated or queried using simple API calls.

## Architecture
- **context.json:** Stores all user data, such as name, current project, hobbies, education, employment status, and more. This file is read and updated by the server.
- **server.py:** Main entry point. Exposes two MCP tools:
  - `get_user_information(query: str)`: Returns user information from `context.json` based on a natural language query.
  - `update_user_information(updates: dict)`: Updates multiple fields in `context.json` with new values.
- **ai.py:** Placeholder for future AI-related functions (currently not implemented).
- **database.py:** **Not in use anymore.** Previous versions used MongoDB for user data, but the project now relies solely on `context.json`.

## Usage
1. **Start the Server:**
   ```bash
   python server.py
   ```
2. **Query User Information:**
   Use the `get_user_information` tool to fetch any user data from `context.json`.
3. **Update User Information:**
   Use the `update_user_information` tool to modify or add fields in `context.json`.

## Claude Desktop Configuration

To use this MCP server with Claude Desktop, you need to add the server configuration to Claude's config file:

### Step 1: Locate Claude Config File
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### Step 2: Add MCP Server Configuration
Add the following configuration to your Claude config file:

```json
{
  "mcpServers": {
    "mcp-context": {
      "command": "python",
      "args": ["/path/to/your/mcp-context/server.py"],
      "env": {}
    }
  }
}
```

**Important:** Replace `/path/to/your/mcp-context/server.py` with the actual absolute path to your `server.py` file.

### Step 3: Example Complete Config File
Here's what your complete `claude_desktop_config.json` might look like:

```json
{
  "mcpServers": {
    "mcp-context": {
      "command": "python",
      "args": ["/Users/ajay/Learn/MCP/mcp-context/server.py"],
      "env": {}
    }
  }
}
```

### Step 4: Restart Claude Desktop
After saving the config file, restart Claude Desktop for the changes to take effect.

### Step 5: Verify Connection
Once restarted, Claude Desktop should automatically connect to your MCP server. You can verify this by asking Claude about your personal information - it should now have access to the data in your `context.json` file.

## Example `context.json`
context.json initially starts empty, and will be updated as the user provides information to the server.



## License
MIT
