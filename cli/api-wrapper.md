# CLI API Wrapper
**UUID:** cli-api-wrapper-001
**ISA-95 L3: MES Layer** | Markdown Executable

FastAPI server that exposes all CLI commands as REST API endpoints.

## Overview

This API wrapper allows you to execute any CLI command via HTTP requests:
- **CLI**: `./cli/boot.md`
- **API**: `POST http://localhost:8001/cli/boot`
- **MCP**: Via MCP server (see mcp-wrapper.md)

```python
#!/usr/bin/env python3
"""
CLI API Wrapper
Exposes all CLI commands as REST API endpoints
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import subprocess
import os
import json
from pathlib import Path
from datetime import datetime

app = FastAPI(
    title="Chazon CLI API",
    description="REST API wrapper for all CLI commands",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get CLI directory
CLI_DIR = Path(__file__).parent.absolute()
ROOT_DIR = CLI_DIR.parent

class CLIRequest(BaseModel):
    args: Optional[List[str]] = []
    async_exec: Optional[bool] = False

class CLIResponse(BaseModel):
    success: bool
    command: str
    stdout: str
    stderr: str
    exit_code: int
    timestamp: str
    execution_time_ms: Optional[float] = None

# Background task storage
background_tasks_status: Dict[str, Any] = {}

def execute_cli_command(command_path: str, args: List[str] = None) -> CLIResponse:
    """Execute a CLI markdown command"""
    import time
    start_time = time.time()

    if args is None:
        args = []

    # Get the .md file path
    md_file = CLI_DIR / command_path
    if not md_file.exists():
        raise HTTPException(status_code=404, detail=f"Command not found: {command_path}")

    # Extract bash code from markdown and execute
    # For now, we'll execute the .md file directly (assuming it's executable)
    # In production, you'd parse the markdown and extract the bash code block

    try:
        result = subprocess.run(
            ["bash", str(md_file)] + args,
            capture_output=True,
            text=True,
            timeout=300,  # 5 minute timeout
            cwd=ROOT_DIR
        )

        execution_time = (time.time() - start_time) * 1000

        return CLIResponse(
            success=result.returncode == 0,
            command=command_path,
            stdout=result.stdout,
            stderr=result.stderr,
            exit_code=result.returncode,
            timestamp=datetime.utcnow().isoformat(),
            execution_time_ms=execution_time
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Command execution timeout")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check
@app.get("/")
@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "Chazon CLI API",
        "version": "1.0.0",
        "available_commands": [
            "boot", "start", "stop", "restart", "health", "logs", "deploy",
            "dev/setup", "dev/test", "models/download", "models/list"
        ]
    }

# List all available commands
@app.get("/cli/commands")
async def list_commands():
    """List all available CLI commands"""
    commands = []

    # Find all .md files in cli directory
    for md_file in CLI_DIR.rglob("*.md"):
        if md_file.name != "README.md" and md_file.name != "api-wrapper.md":
            rel_path = md_file.relative_to(CLI_DIR)
            commands.append({
                "name": str(rel_path.with_suffix('')),
                "path": str(rel_path),
                "endpoint": f"/cli/{rel_path.with_suffix('')}"
            })

    return {"commands": commands, "count": len(commands)}

# System Management Endpoints

@app.post("/cli/boot")
async def boot(request: CLIRequest = CLIRequest()):
    """Boot the OS (6-phase sequence)"""
    return execute_cli_command("boot.md", request.args)

@app.post("/cli/start")
async def start(request: CLIRequest = CLIRequest()):
    """Start all services"""
    return execute_cli_command("start.md", request.args)

@app.post("/cli/stop")
async def stop(request: CLIRequest = CLIRequest()):
    """Stop all services"""
    return execute_cli_command("stop.md", request.args)

@app.post("/cli/restart")
async def restart(request: CLIRequest = CLIRequest()):
    """Restart all services"""
    return execute_cli_command("restart.md", request.args)

@app.get("/cli/health")
@app.post("/cli/health")
async def cli_health(request: CLIRequest = CLIRequest()):
    """System health check"""
    return execute_cli_command("health.md", request.args)

@app.post("/cli/logs")
async def logs(request: CLIRequest = CLIRequest()):
    """View logs (backend|http|system|all)"""
    return execute_cli_command("logs.md", request.args)

@app.post("/cli/deploy")
async def deploy(request: CLIRequest = CLIRequest()):
    """Deploy to GitHub Pages"""
    return execute_cli_command("deploy.md", request.args)

# Development Endpoints

@app.post("/cli/dev/setup")
async def dev_setup(request: CLIRequest = CLIRequest()):
    """Setup development environment"""
    return execute_cli_command("dev/setup.md", request.args)

@app.post("/cli/dev/test")
async def dev_test(request: CLIRequest = CLIRequest()):
    """Run all tests"""
    return execute_cli_command("dev/test.md", request.args)

# Model Management Endpoints

@app.post("/cli/models/download")
async def models_download(request: CLIRequest = CLIRequest()):
    """Download AI models"""
    return execute_cli_command("models/download.md", request.args)

@app.get("/cli/models/list")
@app.post("/cli/models/list")
async def models_list(request: CLIRequest = CLIRequest()):
    """List available models"""
    return execute_cli_command("models/list.md", request.args)

# Generic CLI executor
@app.post("/cli/exec")
async def exec_command(command: str, request: CLIRequest = CLIRequest()):
    """Execute any CLI command by path"""
    return execute_cli_command(command, request.args)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        log_level="info"
    )
```

## Usage

### Start the API Server

```bash
# Direct execution
python3 cli/api-wrapper.md

# Or via uvicorn
uvicorn cli.api-wrapper:app --reload --port 8001
```

### API Endpoints

#### Health Check
```bash
curl http://localhost:8001/health
```

#### List Commands
```bash
curl http://localhost:8001/cli/commands
```

#### Boot OS
```bash
curl -X POST http://localhost:8001/cli/boot
```

#### Start Services
```bash
curl -X POST http://localhost:8001/cli/start
```

#### Health Check (CLI)
```bash
curl http://localhost:8001/cli/health
```

#### View Logs
```bash
curl -X POST http://localhost:8001/cli/logs \
  -H "Content-Type: application/json" \
  -d '{"args": ["backend"]}'
```

#### Run Tests
```bash
curl -X POST http://localhost:8001/cli/dev/test
```

#### List Models
```bash
curl http://localhost:8001/cli/models/list
```

## Response Format

```json
{
  "success": true,
  "command": "boot.md",
  "stdout": "🚀 Chazon OS Boot Sequence\n...",
  "stderr": "",
  "exit_code": 0,
  "timestamp": "2025-11-16T12:00:00.000000",
  "execution_time_ms": 1234.56
}
```

## Request Format

```json
{
  "args": ["backend"],  // Optional command arguments
  "async_exec": false   // Execute in background (future)
}
```

## All Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/health` | GET | Health check |
| `/cli/commands` | GET | List all CLI commands |
| `/cli/boot` | POST | Boot OS |
| `/cli/start` | POST | Start services |
| `/cli/stop` | POST | Stop services |
| `/cli/restart` | POST | Restart services |
| `/cli/health` | GET/POST | System health check |
| `/cli/logs` | POST | View logs |
| `/cli/deploy` | POST | Deploy to GitHub Pages |
| `/cli/dev/setup` | POST | Dev setup |
| `/cli/dev/test` | POST | Run tests |
| `/cli/models/download` | POST | Download models |
| `/cli/models/list` | GET/POST | List models |
| `/cli/exec` | POST | Execute any CLI command |

## JavaScript Example

```javascript
// Boot OS
const response = await fetch('http://localhost:8001/cli/boot', {
  method: 'POST'
});
const result = await response.json();
console.log(result.stdout);

// View logs
const logsResponse = await fetch('http://localhost:8001/cli/logs', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ args: ['backend'] })
});
const logs = await logsResponse.json();
console.log(logs.stdout);
```

## Python Example

```python
import requests

# Boot OS
response = requests.post('http://localhost:8001/cli/boot')
result = response.json()
print(result['stdout'])

# Start services
response = requests.post('http://localhost:8001/cli/start')
print(response.json()['stdout'])

# Health check
response = requests.get('http://localhost:8001/cli/health')
print(response.json()['stdout'])
```

## Integration with Main API

Add to `os/backend/api.py`:

```python
from cli.api_wrapper import app as cli_app

# Mount CLI API
app.mount("/cli", cli_app)
```

Now CLI commands available at: `http://localhost:8000/cli/boot`

## CORS

CORS is enabled for all origins. Restrict in production:

```python
allow_origins=["https://teslasolar.github.io"]
```

## Security

### Production Deployment

1. **Add authentication**:
```python
from fastapi.security import HTTPBearer

security = HTTPBearer()

@app.post("/cli/boot")
async def boot(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Verify token
    ...
```

2. **Rate limiting**:
```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@app.post("/cli/deploy")
@limiter.limit("5/minute")
async def deploy():
    ...
```

3. **Restrict commands**:
```python
ALLOWED_COMMANDS = ["boot", "health", "logs"]
```

## Dependencies

```bash
pip install fastapi uvicorn
```

Or add to `requirements.txt`:
```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
```

## Related

- `mcp-wrapper.md` - MCP server wrapper
- `/os/backend/api.py` - Main API server
- All CLI commands (`*.md`)
