# Chazon CLI Tools

Command-line interface tools for managing the Chazon Medical Imaging SCADA System.

---

## Quick Reference

### System Management
```bash
./cli/boot.sh           # Boot the OS (6-phase sequence)
./cli/start.sh          # Start all services
./cli/stop.sh           # Stop all services
./cli/restart.sh        # Restart all services
./cli/health.sh         # System health check
./cli/logs.sh [area]    # View logs (backend|http|system|all)
./cli/deploy.sh         # Deploy to GitHub Pages
```

### Development
```bash
./cli/dev/setup.sh      # Setup development environment
./cli/dev/test.sh       # Run all tests
```

### Models
```bash
./cli/models/download.sh    # Download AI models
./cli/models/list.sh        # List available models
```

---

## System Management Scripts

### boot.sh
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
./cli/boot.sh
```

**Output:**
- ✅ Status for each phase
- 🟢 System ready indicators
- 📊 Access points for SCADA/HMI/PLC

---

### start.sh
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
./cli/start.sh
```

**Logs:**
- Backend API: `cli/logs/backend.log`
- HTTP Server: `cli/logs/httpserver.log`

**PID Files:**
- Backend API: `cli/logs/backend.pid`
- HTTP Server: `cli/logs/httpserver.pid`

---

### stop.sh
Stops all running services gracefully.

**Stops:**
- Backend API (kills process, removes PID file)
- HTTP Server (kills process, removes PID file)
- Qdrant (stops and removes Docker container)

**Usage:**
```bash
./cli/stop.sh
```

---

### restart.sh
Convenience script that stops and starts all services.

**Usage:**
```bash
./cli/restart.sh
```

Equivalent to:
```bash
./cli/stop.sh && sleep 2 && ./cli/start.sh
```

---

### health.sh
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
./cli/health.sh
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

### logs.sh
View system logs for different areas.

**Usage:**
```bash
./cli/logs.sh [area]
```

**Areas:**
- `backend` - Backend API logs
- `http` - HTTP server logs
- `system` - OS system logs
- `all` - All logs (default, shows last 10 lines of each)

**Examples:**
```bash
# View all logs (summary)
./cli/logs.sh

# Tail backend logs
./cli/logs.sh backend

# Tail HTTP server logs
./cli/logs.sh http

# View system logs
./cli/logs.sh system
```

**Live Monitoring:**
For live log monitoring, the script will run `tail -f` for single areas.

---

### deploy.sh
Deploy the application to GitHub Pages.

**Process:**
1. Checks for git repository
2. Warns about uncommitted changes
3. Gets current branch name
4. Pushes to origin

**Usage:**
```bash
./cli/deploy.sh
```

**Deployment URL:**
https://teslasolar.github.io/qdrant/

**Note:** GitHub Pages may take a few minutes to update after deployment.

---

## Development Scripts

### dev/setup.sh
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
./cli/dev/setup.sh
```

**Requirements:**
- Python 3.8+
- Node.js (optional, for frontend development)
- Docker (for Qdrant)

**Post-Setup:**
1. Update `.env` with your API keys
2. Run `./cli/start.sh`
3. Open http://localhost:8080

---

### dev/test.sh
Runs all available test suites.

**Test Suites:**
1. Module tests (os/test-modules with pytest)
2. Backend API tests (os/backend/test_api.py)

**Usage:**
```bash
./cli/dev/test.sh
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

### models/download.sh
Downloads AI models for inference.

**Models:**
- **BERT Tiny** - Text embeddings
- **MobileNet V2** - Image classification
- **ResNet18** - Image classification
- **SqueezeNet** - Lightweight image classification

**Usage:**
```bash
./cli/models/download.sh
```

**Download Locations:**
Models are downloaded to their respective directories:
- `os/models/bert-tiny/`
- `os/models/mobilenet-v2/`
- `os/models/resnet18/`
- `os/models/squeezenet/`

---

### models/list.sh
Lists all available AI models and their sizes.

**Usage:**
```bash
./cli/models/list.sh
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
├── boot.sh                 # Boot OS
├── start.sh                # Start services
├── stop.sh                 # Stop services
├── restart.sh              # Restart services
├── health.sh               # Health check
├── logs.sh                 # View logs
├── deploy.sh               # Deploy to GitHub Pages
├── dev/                    # Development tools
│   ├── setup.sh            # Dev environment setup
│   └── test.sh             # Run tests
├── models/                 # Model management
│   ├── download.sh         # Download models
│   └── list.sh             # List models
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
./cli/dev/setup.sh

# 2. Update .env with API keys
nano .env

# 3. Download AI models (optional)
./cli/models/download.sh

# 4. Boot the OS
./cli/boot.sh

# 5. Start all services
./cli/start.sh

# 6. Check health
./cli/health.sh

# 7. Open browser
open http://localhost:8080
```

### Daily Development
```bash
# Start services
./cli/start.sh

# Make changes...

# Run tests
./cli/dev/test.sh

# Check logs
./cli/logs.sh backend

# Restart if needed
./cli/restart.sh

# Stop when done
./cli/stop.sh
```

### Deployment
```bash
# Run tests
./cli/dev/test.sh

# Health check
./cli/health.sh

# Deploy
./cli/deploy.sh
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
./cli/restart.sh
```

### Docker Issues
```bash
# Check Docker is running
docker info

# Remove old Qdrant container
docker stop qdrant && docker rm qdrant

# Restart services
./cli/start.sh
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
chmod +x cli/*.sh
chmod +x cli/dev/*.sh
chmod +x cli/models/*.sh
```

---

## Advanced Usage

### Custom Health Checks
Add your own health checks to `health.sh`:

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
Add custom log areas to `logs.sh`:

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
      - run: ./cli/deploy.sh
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
