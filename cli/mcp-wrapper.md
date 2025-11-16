# CLI MCP Wrapper
**UUID:** cli-mcp-wrapper-001
**ISA-95 L3: MES Layer** | Markdown Executable

Model Context Protocol (MCP) server that exposes all CLI commands as MCP tools.

## Overview

This MCP wrapper allows you to execute any CLI command via MCP:
- **CLI**: `./cli/boot.md`
- **API**: `POST http://localhost:8001/cli/boot`
- **MCP**: `cli_boot` tool via MCP server

```python
#!/usr/bin/env python3
"""
CLI MCP Server
Exposes all CLI commands as MCP tools for Claude Desktop, IDEs, etc.
"""

import asyncio
import subprocess
import json
from pathlib import Path
from typing import Any, Sequence
from datetime import datetime

# MCP SDK imports
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
    from mcp.server.models import InitializationOptions
except ImportError:
    print("MCP SDK not installed. Run: pip install mcp")
    exit(1)

# Get CLI directory
CLI_DIR = Path(__file__).parent.absolute()
ROOT_DIR = CLI_DIR.parent

# Create MCP server
server = Server("chazon-cli")

async def execute_cli_command(command_path: str, args: list[str] = None) -> dict[str, Any]:
    """Execute a CLI markdown command"""
    if args is None:
        args = []

    # Get the .md file path
    md_file = CLI_DIR / command_path
    if not md_file.exists():
        return {
            "success": False,
            "error": f"Command not found: {command_path}",
            "command": command_path
        }

    try:
        # Execute the markdown file as bash
        process = await asyncio.create_subprocess_exec(
            "bash", str(md_file), *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=ROOT_DIR
        )

        stdout, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=300  # 5 minute timeout
        )

        return {
            "success": process.returncode == 0,
            "command": command_path,
            "stdout": stdout.decode(),
            "stderr": stderr.decode(),
            "exit_code": process.returncode,
            "timestamp": datetime.utcnow().isoformat()
        }
    except asyncio.TimeoutError:
        return {
            "success": False,
            "error": "Command execution timeout (5 minutes)",
            "command": command_path
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "command": command_path
        }

@server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available CLI tools"""
    return [
        # System Management
        Tool(
            name="cli_boot",
            description="Boot the Chazon OS with 6-phase sequence (Core, AI Models, Multi-Agent, Medical Imaging, UI, Templates)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="cli_start",
            description="Start all services (Qdrant vector database on port 6333, Backend API on port 8000, HTTP server on port 8080)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="cli_stop",
            description="Stop all running services gracefully (Backend API, HTTP server, Qdrant container)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="cli_restart",
            description="Restart all services (stops and starts with 2 second delay)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="cli_health",
            description="Comprehensive system health check for all services (Qdrant, Backend API, HTTP server, disk usage, file counts)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="cli_logs",
            description="View system logs for different areas",
            inputSchema={
                "type": "object",
                "properties": {
                    "area": {
                        "type": "string",
                        "description": "Log area to view: backend, http, system, or all (default)",
                        "enum": ["backend", "http", "system", "all"],
                        "default": "all"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="cli_deploy",
            description="Deploy the application to GitHub Pages",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),

        # Development
        Tool(
            name="cli_dev_setup",
            description="Setup complete development environment (Python venv, dependencies, Node.js packages, log directories, .env file)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="cli_dev_test",
            description="Run all test suites (module tests and backend API tests)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),

        # Model Management
        Tool(
            name="cli_models_download",
            description="Download all AI models (BERT Tiny, MobileNet V2, ResNet18, SqueezeNet)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="cli_models_list",
            description="List all available AI models with their sizes",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),

        # Generic executor
        Tool(
            name="cli_exec",
            description="Execute any CLI command by path (e.g., 'boot.md', 'dev/test.md')",
            inputSchema={
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Path to CLI command (e.g., 'boot.md', 'dev/setup.md')"
                    },
                    "args": {
                        "type": "array",
                        "description": "Arguments to pass to the command",
                        "items": {"type": "string"},
                        "default": []
                    }
                },
                "required": ["command"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: Any) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Handle tool calls"""

    # Map tool names to command paths
    tool_map = {
        "cli_boot": "boot.md",
        "cli_start": "start.md",
        "cli_stop": "stop.md",
        "cli_restart": "restart.md",
        "cli_health": "health.md",
        "cli_logs": "logs.md",
        "cli_deploy": "deploy.md",
        "cli_dev_setup": "dev/setup.md",
        "cli_dev_test": "dev/test.md",
        "cli_models_download": "models/download.md",
        "cli_models_list": "models/list.md"
    }

    # Handle generic executor
    if name == "cli_exec":
        command_path = arguments.get("command")
        args = arguments.get("args", [])
        result = await execute_cli_command(command_path, args)

    # Handle specific tools
    elif name in tool_map:
        command_path = tool_map[name]

        # Extract args for tools that support them
        args = []
        if name == "cli_logs" and "area" in arguments:
            args = [arguments["area"]]

        result = await execute_cli_command(command_path, args)

    else:
        result = {
            "success": False,
            "error": f"Unknown tool: {name}"
        }

    # Format response
    if result.get("success"):
        response_text = f"""Command: {result['command']}
Exit Code: {result['exit_code']}
Timestamp: {result['timestamp']}

Output:
{result['stdout']}"""

        if result.get('stderr'):
            response_text += f"\n\nErrors:\n{result['stderr']}"
    else:
        response_text = f"""Command Failed: {result['command']}
Error: {result.get('error', 'Unknown error')}"""

        if result.get('stderr'):
            response_text += f"\n\nStderr:\n{result['stderr']}"

    return [TextContent(type="text", text=response_text)]

async def main():
    """Run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="chazon-cli",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities={}
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Installation

### Install MCP SDK

```bash
pip install mcp
```

Or add to `requirements.txt`:
```
mcp>=0.9.0
```

### Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "chazon-cli": {
      "command": "python3",
      "args": [
        "/path/to/qdrant/cli/mcp-wrapper.md"
      ],
      "env": {}
    }
  }
}
```

On Linux: `~/.config/Claude/claude_desktop_config.json`

## Available MCP Tools

| Tool Name | Description | Arguments |
|-----------|-------------|-----------|
| `cli_boot` | Boot OS (6-phase) | None |
| `cli_start` | Start all services | None |
| `cli_stop` | Stop all services | None |
| `cli_restart` | Restart services | None |
| `cli_health` | System health check | None |
| `cli_logs` | View logs | `area` (backend/http/system/all) |
| `cli_deploy` | Deploy to GitHub Pages | None |
| `cli_dev_setup` | Setup dev environment | None |
| `cli_dev_test` | Run tests | None |
| `cli_models_download` | Download AI models | None |
| `cli_models_list` | List AI models | None |
| `cli_exec` | Execute any CLI command | `command`, `args` |

## Usage in Claude Desktop

After configuring, you can ask Claude:

```
"Boot the Chazon OS"
→ Claude will call cli_boot tool

"Check system health"
→ Claude will call cli_health tool

"View backend logs"
→ Claude will call cli_logs with area="backend"

"Run all tests"
→ Claude will call cli_dev_test tool

"Download AI models"
→ Claude will call cli_models_download tool
```

## Usage with MCP Client

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Connect to server
server_params = StdioServerParameters(
    command="python3",
    args=["cli/mcp-wrapper.md"]
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()

        # List available tools
        tools = await session.list_tools()
        print(f"Available tools: {[t.name for t in tools.tools]}")

        # Call tool
        result = await session.call_tool("cli_health", arguments={})
        print(result.content[0].text)
```

## Usage with cURL (via MCP HTTP proxy)

If you set up an MCP HTTP proxy:

```bash
# Boot OS
curl -X POST http://localhost:3000/tools/cli_boot \
  -H "Content-Type: application/json" \
  -d '{}'

# View logs
curl -X POST http://localhost:3000/tools/cli_logs \
  -H "Content-Type: application/json" \
  -d '{"area": "backend"}'

# Execute custom command
curl -X POST http://localhost:3000/tools/cli_exec \
  -H "Content-Type: application/json" \
  -d '{"command": "boot.md", "args": []}'
```

## All Three Access Methods

Every CLI command is now accessible via:

### 1. CLI (Direct)
```bash
./cli/boot.md
```

### 2. API (REST)
```bash
curl -X POST http://localhost:8001/cli/boot
```

### 3. MCP (Tool Call)
```python
await session.call_tool("cli_boot", {})
```

## Testing the MCP Server

```bash
# Test server directly (stdio)
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | python3 cli/mcp-wrapper.md

# Or use MCP inspector
npx @modelcontextprotocol/inspector python3 cli/mcp-wrapper.md
```

## Integration with Other MCP Servers

The CLI MCP server can be composed with other MCP servers:

```json
{
  "mcpServers": {
    "chazon-cli": {
      "command": "python3",
      "args": ["qdrant/cli/mcp-wrapper.md"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

## Response Format

All tools return TextContent with:
- Command executed
- Exit code
- Timestamp
- Output (stdout)
- Errors (stderr) if any

Example:
```
Command: boot.md
Exit Code: 0
Timestamp: 2025-11-16T12:00:00.000000

Output:
🚀 Chazon OS Boot Sequence
==========================

⚙️  Phase 0: Core Infrastructure
  ✅ Loading OS kernel
  ✅ Loading markdown compiler
...
```

## Error Handling

Errors are returned as TextContent:
```
Command Failed: invalid.md
Error: Command not found: invalid.md
```

## Timeout

All commands have a 5-minute timeout. Long-running commands will be terminated.

## Security

For production:
1. Restrict allowed commands
2. Add authentication/authorization
3. Validate all inputs
4. Run in sandboxed environment
5. Limit resource usage

## Dependencies

```txt
mcp>=0.9.0
```

## Related

- `api-wrapper.md` - REST API wrapper
- All CLI commands (`*.md`)
- `/os/modules/chazon-mcp.md` - Main MCP integration
