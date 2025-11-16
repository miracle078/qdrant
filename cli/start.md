# Start Services
**UUID:** cli-start-001
**ISA-95 L3: MES Layer** | Markdown Executable

Starts all backend services required for full system operation.

## Services

1. **Qdrant** - Vector database on port 6333 (Docker)
2. **Backend API** - FastAPI server on port 8000 (Python)
3. **HTTP Server** - Development server on port 8080 (Python)

```bash
#!/bin/bash
# Start all Chazon services

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🚀 Starting Chazon Services"
echo "==========================="
echo ""

# Create logs directory if it doesn't exist
mkdir -p "$ROOT_DIR/cli/logs"

# 1. Start Qdrant vector database
echo "Starting Qdrant..."
if docker ps | grep -q qdrant; then
    echo "  ⚠️  Qdrant already running"
else
    docker run -d --name qdrant \
        -p 6333:6333 \
        -v qdrant_storage:/qdrant/storage \
        qdrant/qdrant:latest > /dev/null 2>&1
    echo "  ✅ Qdrant started on port 6333"
fi
echo ""

# 2. Start Backend API
echo "Starting Backend API..."
if [ -f "$ROOT_DIR/cli/logs/backend.pid" ] && kill -0 $(cat "$ROOT_DIR/cli/logs/backend.pid") 2>/dev/null; then
    echo "  ⚠️  Backend API already running (PID: $(cat $ROOT_DIR/cli/logs/backend.pid))"
else
    cd "$ROOT_DIR/os/backend"

    # Activate virtual environment if it exists
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        pip install -q -r requirements.txt 2>/dev/null || true
    fi

    # Start backend in background
    nohup python api.py > "$ROOT_DIR/cli/logs/backend.log" 2>&1 &
    echo $! > "$ROOT_DIR/cli/logs/backend.pid"

    echo "  ✅ Backend API started on port 8000 (PID: $!)"

    if [ -f "venv/bin/activate" ]; then
        deactivate 2>/dev/null || true
    fi

    cd "$ROOT_DIR"
fi
echo ""

# 3. Start HTTP Server
echo "Starting HTTP Server..."
if [ -f "$ROOT_DIR/cli/logs/httpserver.pid" ] && kill -0 $(cat "$ROOT_DIR/cli/logs/httpserver.pid") 2>/dev/null; then
    echo "  ⚠️  HTTP Server already running (PID: $(cat $ROOT_DIR/cli/logs/httpserver.pid))"
else
    cd "$ROOT_DIR"
    nohup python3 -m http.server 8080 > "$ROOT_DIR/cli/logs/httpserver.log" 2>&1 &
    echo $! > "$ROOT_DIR/cli/logs/httpserver.pid"
    echo "  ✅ HTTP Server started on port 8080 (PID: $!)"
fi
echo ""

echo "==========================="
echo "🟢 All services started!"
echo ""
echo "Access:"
echo "  🌐 Web UI:       http://localhost:8080"
echo "  🔌 Backend API:  http://localhost:8000"
echo "  🗄️  Qdrant:      http://localhost:6333"
echo ""
echo "Logs:"
echo "  📋 Backend:      cli/logs/backend.log"
echo "  📋 HTTP Server:  cli/logs/httpserver.log"
echo ""
echo "Check status: ./cli/health.md"
echo "View logs:    ./cli/logs.md"
```

## Usage

```bash
# Start all services
./cli/start.md

# Check they started successfully
./cli/health.md
```

## Requirements

- Docker (for Qdrant)
- Python 3.8+ (for Backend API)
- Python 3 (for HTTP Server)

## Log Files

- `cli/logs/backend.log` - Backend API output
- `cli/logs/httpserver.log` - HTTP server output

## PID Files

- `cli/logs/backend.pid` - Backend API process ID
- `cli/logs/httpserver.pid` - HTTP server process ID

## Ports

| Service | Port | Protocol |
|---------|------|----------|
| Qdrant | 6333 | HTTP/gRPC |
| Backend API | 8000 | HTTP |
| HTTP Server | 8080 | HTTP |

## Troubleshooting

### Port Already in Use
```bash
# Check what's using the port
lsof -i :8080
lsof -i :8000
lsof -i :6333

# Kill the process
kill -9 <PID>
```

### Docker Not Running
```bash
# Start Docker service
systemctl start docker  # Linux
open -a Docker         # macOS
```

## Related

- `stop.md` - Stop all services
- `restart.md` - Restart services
- `health.md` - Health check
- `logs.md` - View logs
