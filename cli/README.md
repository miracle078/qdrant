# Chazon CLI Tools

**Markdown-executable** command-line interface tools for managing the Chazon Medical Imaging SCADA System.

All CLI tools are **markdown files (.md)** that follow the system's markdown-first architecture.

## Three Access Methods

Every CLI command is accessible via **three interfaces**:

| Method | Example | Port |
|--------|---------|------|
| **CLI** (Direct) | `./cli/boot.md` | N/A |
| **API** (REST) | `POST http://localhost:8001/cli/boot` | 8001 |
| **MCP** (Tool) | `cli_boot` tool via MCP server | stdio |

### Start Wrappers

```bash
# Start API wrapper (port 8001)
python3 cli/api-wrapper.md

# Start MCP wrapper (stdio)
python3 cli/mcp-wrapper.md

# Or configure MCP in Claude Desktop (see mcp-wrapper.md)
```

---

## Quick Reference

### System Management
```bash
./cli/boot.md           # Boot the OS (6-phase sequence)
./cli/start.md          # Start all services
./cli/stop.md           # Stop all services
./cli/restart.md        # Restart all services
./cli/health.md         # System health check
./cli/logs.md [area]    # View logs (backend|http|system|all)
./cli/deploy.md         # Deploy to GitHub Pages
```

### Development
```bash
./cli/dev/setup.md      # Setup development environment
./cli/dev/test.md       # Run all tests
```

### Models
```bash
./cli/models/download.md    # Download AI models
./cli/models/list.md        # List available models
```

---

## Complete Examples (All 3 Methods)

### Boot OS
```bash
# CLI
./cli/boot.md

# API
curl -X POST http://localhost:8001/cli/boot

# MCP (natural language in Claude Desktop)
"Boot the Chazon OS"
```

### Start Services
```bash
# CLI
./cli/start.md

# API
curl -X POST http://localhost:8001/cli/start

# MCP
"Start all services"
```

### Health Check
```bash
# CLI
./cli/health.md

# API
curl http://localhost:8001/cli/health

# MCP
"Check system health"
```

### View Logs
```bash
# CLI
./cli/logs.md backend

# API
curl -X POST http://localhost:8001/cli/logs \
  -H "Content-Type: application/json" \
  -d '{"args": ["backend"]}'

# MCP
"Show me the backend logs"
```

### Run Tests
```bash
# CLI
./cli/dev/test.md

# API
curl -X POST http://localhost:8001/cli/dev/test

# MCP
"Run all tests"
```

### List Models
```bash
# CLI
./cli/models/list.md

# API
curl http://localhost:8001/cli/models/list

# MCP
"List all AI models"
```

---

## API & MCP Wrappers

### api-wrapper.md
FastAPI server that exposes all CLI commands as REST endpoints.

**Features:**
- All CLI commands available via HTTP POST/GET
- JSON responses with stdout/stderr/exit codes
- CORS enabled
- 5-minute timeout per command
- `/cli/commands` endpoint lists all available commands

**Endpoints:**
- `GET /health` - API health check
- `GET /cli/commands` - List all commands
- `POST /cli/boot` - Boot OS
- `POST /cli/start` - Start services
- `POST /cli/stop` - Stop services
- `POST /cli/restart` - Restart services
- `GET /cli/health` - System health
- `POST /cli/logs` - View logs
- `POST /cli/deploy` - Deploy
- `POST /cli/dev/setup` - Dev setup
- `POST /cli/dev/test` - Run tests
- `POST /cli/models/download` - Download models
- `GET /cli/models/list` - List models
- `POST /cli/exec` - Execute any command

### mcp-wrapper.md
Model Context Protocol server for Claude Desktop and other MCP clients.

**Features:**
- 12 MCP tools (one per CLI command)
- Natural language interface
- Async execution
- 5-minute timeout per command
- Works with Claude Desktop, IDEs, etc.

**Tools:**
- `cli_boot` - Boot OS
- `cli_start` - Start services
- `cli_stop` - Stop services
- `cli_restart` - Restart services
- `cli_health` - Health check
- `cli_logs` - View logs (with area parameter)
- `cli_deploy` - Deploy
- `cli_dev_setup` - Dev setup
- `cli_dev_test` - Run tests
- `cli_models_download` - Download models
- `cli_models_list` - List models
- `cli_exec` - Execute any command

---

## System Management Scripts

### boot.md
Runs the 6-phase boot sequence to initialize the Chazon OS.

**Phases:**
1. Phase 0: Core Infrastructure (OS, Compiler, PackML)
2. Phase 1: AI Models (ONNX, WebGPU)
3. Phase 2: Multi-Agent System (Swarm, Conway, GPT)
4. Phase 3: Medical Imaging (DICOM, Qdrant, AlF-DETECT)
5. Phase 4: UI Components (Modules, Icons, Screens)
6. Phase 5: Templates (ISA, Views, Medical)

**Usage:**
```bash
./cli/boot.md
```

**Output:**
- ✅ Status for each phase
- 🟢 System ready indicators
- 📊 Access points for SCADA/HMI/PLC

---

### start.md
Starts all backend services required for full system operation.

**Services Started:**
1. **Qdrant** - Vector database on port 6333 (Docker)
2. **Backend API** - FastAPI server on port 8000 (Python)
3. **HTTP Server** - Development server on port 8080 (Python)

**Requirements:**
- Docker (for Qdrant)
- Python 3.8+ (for Backend API)

**Usage:**
```bash
./cli/start.md
```

**Logs:**
- Backend API: `cli/logs/backend.log`
- HTTP Server: `cli/logs/httpserver.log`

**PID Files:**
- Backend API: `cli/logs/backend.pid`
- HTTP Server: `cli/logs/httpserver.pid`

---

### stop.md
Stops all running services gracefully.

**Stops:**
- Backend API (kills process, removes PID file)
- HTTP Server (kills process, removes PID file)
- Qdrant (stops and removes Docker container)

**Usage:**
```bash
./cli/stop.md
```

---

### restart.md
Convenience script that stops and starts all services.

**Usage:**
```bash
./cli/restart.md
```

Equivalent to:
```bash
./cli/stop.md && sleep 2 && ./cli/start.md
```

---

### health.md
Comprehensive system health check for all services and resources.

**Checks:**
1. **Qdrant** - Container status and HTTP response
2. **Backend API** - Process status and health endpoint
3. **HTTP Server** - Process status and serving files
4. **Disk Usage** - Warns if >80% full
5. **File System** - Counts modules, models, logs

**Status Indicators:**
- 🟢 HEALTHY - Service responding normally
- 🟡 DEGRADED - Service running but not responding
- 🔴 DOWN - Service not running

**Usage:**
```bash
./cli/health.md
```

**Example Output:**
```
🟢 Qdrant: HEALTHY (http://localhost:6333)
🟢 Backend API: HEALTHY (http://localhost:8000)
🟢 HTTP Server: HEALTHY (http://localhost:8080)
🟢 Disk Usage: 45% (healthy)
📦 Modules: 114
🤖 Models: 4
📋 Log Files: 12
```

---

### logs.md
View system logs for different areas.

**Usage:**
```bash
./cli/logs.md [area]
```

**Areas:**
- `backend` - Backend API logs
- `http` - HTTP server logs
- `system` - OS system logs
- `all` - All logs (default, shows last 10 lines of each)

**Examples:**
```bash
# View all logs (summary)
./cli/logs.md

# Tail backend logs
./cli/logs.md backend

# Tail HTTP server logs
./cli/logs.md http

# View system logs
./cli/logs.md system
```

**Live Monitoring:**
For live log monitoring, the script will run `tail -f` for single areas.

---

### deploy.md
Deploy the application to GitHub Pages.

**Process:**
1. Checks for git repository
2. Warns about uncommitted changes
3. Gets current branch name
4. Pushes to origin

**Usage:**
```bash
./cli/deploy.md
```

**Deployment URL:**
https://teslasolar.github.io/qdrant/

**Note:** GitHub Pages may take a few minutes to update after deployment.

---

## Development Scripts

### dev/setup.md
Sets up the complete development environment.

**Actions:**
1. Checks Python 3.8+ availability
2. Creates backend virtual environment
3. Installs backend dependencies (requirements.txt)
4. Checks Node.js (optional)
5. Installs frontend dependencies if package.json exists
6. Creates log directories
7. Creates .env from .env.example

**Usage:**
```bash
./cli/dev/setup.md
```

**Requirements:**
- Python 3.8+
- Node.js (optional, for frontend development)
- Docker (for Qdrant)

**Post-Setup:**
1. Update `.env` with your API keys
2. Run `./cli/start.md`
3. Open http://localhost:8080

---

### dev/test.md
Runs all available test suites.

**Test Suites:**
1. Module tests (os/test-modules with pytest)
2. Backend API tests (os/backend/test_api.py)

**Usage:**
```bash
./cli/dev/test.md
```

**Requirements:**
- pytest (`pip install pytest`)

**Example Output:**
```
🧪 Running Chazon Tests
=======================

Running module tests...
  ✅ Module tests passed

Running backend tests...
  ✅ Backend tests passed

=======================
✅ All tests completed
```

---

## Model Management Scripts

### models/download.md
Downloads AI models for inference.

**Models:**
- **BERT Tiny** - Text embeddings
- **MobileNet V2** - Image classification
- **ResNet18** - Image classification
- **SqueezeNet** - Lightweight image classification

**Usage:**
```bash
./cli/models/download.md
```

**Download Locations:**
Models are downloaded to their respective directories:
- `os/models/bert-tiny/`
- `os/models/mobilenet-v2/`
- `os/models/resnet18/`
- `os/models/squeezenet/`

---

### models/list.md
Lists all available AI models and their sizes.

**Usage:**
```bash
./cli/models/list.md
```

**Example Output:**
```
🤖 Available AI Models
======================

📦 bert-tiny
   ✅ model.onnx (45MB)

📦 mobilenet-v2
   ✅ mobilenetv2-7.onnx (14MB)

📦 resnet18
   ✅ resnet18-v1-7.onnx (46MB)

📦 squeezenet
   ✅ squeezenet1.1-7.onnx (5.0MB)

======================
Total models: 4
```

---

## Directory Structure

```
cli/
├── README.md               # This file
├── api-wrapper.md          # REST API wrapper (port 8001)
├── mcp-wrapper.md          # MCP server wrapper (stdio)
├── boot.md                 # Boot OS
├── start.md                # Start services
├── stop.md                 # Stop services
├── restart.md              # Restart services
├── health.md               # Health check
├── logs.md                 # View logs
├── deploy.md               # Deploy to GitHub Pages
├── dev/                    # Development tools
│   ├── setup.md            # Dev environment setup
│   └── test.md             # Run tests
├── models/                 # Model management
│   ├── download.md         # Download models
│   └── list.md             # List models
├── backup/                 # Backup tools (future)
└── logs/                   # Service logs
    ├── backend.log         # Backend API logs
    ├── backend.pid         # Backend API PID
    ├── httpserver.log      # HTTP server logs
    └── httpserver.pid      # HTTP server PID
```

---

## Environment Variables

Create a `.env` file in the root directory (use `.env.example` as template):

```bash
# API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
COHERE_API_KEY=...

# Qdrant
QDRANT_URL=https://xyz.qdrant.io
QDRANT_API_KEY=...

# Application
DEBUG=false
LOG_LEVEL=INFO
PORT=8000
```

---

## Typical Workflow

### First-Time Setup
```bash
# 1. Setup development environment
./cli/dev/setup.md

# 2. Update .env with API keys
nano .env

# 3. Download AI models (optional)
./cli/models/download.md

# 4. Boot the OS
./cli/boot.md

# 5. Start all services
./cli/start.md

# 6. Check health
./cli/health.md

# 7. Open browser
open http://localhost:8080
```

### Daily Development
```bash
# Start services
./cli/start.md

# Make changes...

# Run tests
./cli/dev/test.md

# Check logs
./cli/logs.md backend

# Restart if needed
./cli/restart.md

# Stop when done
./cli/stop.md
```

### Deployment
```bash
# Run tests
./cli/dev/test.md

# Health check
./cli/health.md

# Deploy
./cli/deploy.md
```

---

## Troubleshooting

### Services Won't Start
```bash
# Check if ports are already in use
lsof -i :6333  # Qdrant
lsof -i :8000  # Backend API
lsof -i :8080  # HTTP Server

# Kill processes using ports
kill -9 <PID>

# Restart services
./cli/restart.md
```

### Docker Issues
```bash
# Check Docker is running
docker info

# Remove old Qdrant container
docker stop qdrant && docker rm qdrant

# Restart services
./cli/start.md
```

### Python Virtual Environment Issues
```bash
# Remove and recreate venv
cd os/backend
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Permission Issues
```bash
# Make scripts executable
chmod +x cli/*.md
chmod +x cli/dev/*.md
chmod +x cli/models/*.md
```

---

## Advanced Usage

### Custom Health Checks
Add your own health checks to `health.md`:

```bash
# Check custom service
echo "Checking My Service..."
if curl -s http://localhost:9000/health > /dev/null 2>&1; then
    echo "  🟢 My Service: HEALTHY"
else
    echo "  🔴 My Service: DOWN"
fi
```

### Custom Log Monitoring
Add custom log areas to `logs.md`:

```bash
myservice)
    echo "My Service Logs:"
    tail -f "$ROOT_DIR/cli/logs/myservice.log"
    ;;
```

### Automated Deployment
Set up GitHub Actions to automatically deploy:

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: ./cli/deploy.md
```

---

## Related Documentation

- **Main README:** `/README.md`
- **Architecture:** `/docs/ISA-95-COMPLETE-HIERARCHY.md`
- **Equipment:** `/os/equipment/README.md`
- **Boot System:** `/os/boot/README.md`

---

**Version:** 1.0
**Last Updated:** 2025-11-15
**Maintained By:** Chazon Development Team
