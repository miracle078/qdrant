# Stop Services
**UUID:** cli-stop-001
**ISA-95 L3: MES Layer** | Markdown Executable

Stops all running services gracefully.

## Services Stopped

- Backend API (kills process, removes PID file)
- HTTP Server (kills process, removes PID file)
- Qdrant (stops and removes Docker container)

```bash
#!/bin/bash
# Stop all Chazon services

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🛑 Stopping Chazon Services"
echo "===========================" echo ""

# Stop Backend API
if [ -f "$ROOT_DIR/cli/logs/backend.pid" ]; then
    PID=$(cat "$ROOT_DIR/cli/logs/backend.pid")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"
        rm "$ROOT_DIR/cli/logs/backend.pid"
        echo "  ✅ Backend API stopped (PID: $PID)"
    else
        echo "  ⚠️  Backend API not running"
        rm "$ROOT_DIR/cli/logs/backend.pid"
    fi
else
    echo "  ⚠️  Backend API not running"
fi

# Stop HTTP Server
if [ -f "$ROOT_DIR/cli/logs/httpserver.pid" ]; then
    PID=$(cat "$ROOT_DIR/cli/logs/httpserver.pid")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"
        rm "$ROOT_DIR/cli/logs/httpserver.pid"
        echo "  ✅ HTTP Server stopped (PID: $PID)"
    else
        echo "  ⚠️  HTTP Server not running"
        rm "$ROOT_DIR/cli/logs/httpserver.pid"
    fi
else
    echo "  ⚠️  HTTP Server not running"
fi

# Stop Qdrant
if docker ps | grep -q qdrant; then
    docker stop qdrant > /dev/null 2>&1
    docker rm qdrant > /dev/null 2>&1
    echo "  ✅ Qdrant stopped"
else
    echo "  ⚠️  Qdrant not running"
fi

echo ""
echo "==========================="
echo "🟢 All services stopped"
```

## Usage

```bash
# Stop all services
./cli/stop.md
```

## What Gets Stopped

1. **Backend API** - Python FastAPI process
2. **HTTP Server** - Python HTTP server
3. **Qdrant** - Docker container

## PID Files Removed

- `cli/logs/backend.pid`
- `cli/logs/httpserver.pid`

## Docker Cleanup

The Qdrant container is both stopped and removed. To preserve data, volumes are kept:
- `qdrant_storage` volume persists

## Safe Shutdown

This script uses:
- `kill` (SIGTERM) for graceful shutdown
- PID file cleanup
- Docker stop/rm for container cleanup

## Troubleshooting

### Process Won't Stop
```bash
# Force kill
kill -9 <PID>

# Find the process manually
ps aux | grep python
ps aux | grep http.server
```

### Docker Container Won't Stop
```bash
# Force remove
docker rm -f qdrant

# Check for orphaned containers
docker ps -a | grep qdrant
```

## Related

- `start.md` - Start services
- `restart.md` - Restart services
- `health.md` - Check service status
