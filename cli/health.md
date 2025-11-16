# Health Check
**UUID:** cli-health-001
**ISA-95 L2: Supervisory Control** | Markdown Executable

Comprehensive system health check for all services and resources.

## Checks

1. **Qdrant** - Container status and HTTP response
2. **Backend API** - Process status and health endpoint
3. **HTTP Server** - Process status and serving files
4. **Disk Usage** - Warns if >80% full
5. **File System** - Counts modules, models, logs

## Status Indicators

- 🟢 HEALTHY - Service responding normally
- 🟡 DEGRADED - Service running but not responding
- 🔴 DOWN - Service not running

```bash
#!/bin/bash
# Chazon System Health Check

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🏥 Chazon System Health Check"
echo "=============================="
echo ""

# Check Qdrant
echo "Checking Qdrant..."
if docker ps | grep -q qdrant; then
    if curl -s http://localhost:6333/health > /dev/null 2>&1; then
        echo "  🟢 Qdrant: HEALTHY (http://localhost:6333)"
    else
        echo "  🟡 Qdrant: DEGRADED (container running but not responding)"
    fi
else
    echo "  🔴 Qdrant: DOWN"
fi
echo ""

# Check Backend API
echo "Checking Backend API..."
if [ -f "$ROOT_DIR/cli/logs/backend.pid" ] && kill -0 $(cat "$ROOT_DIR/cli/logs/backend.pid") 2>/dev/null; then
    PID=$(cat "$ROOT_DIR/cli/logs/backend.pid")
    if curl -s http://localhost:8000/api/health > /dev/null 2>&1; then
        echo "  🟢 Backend API: HEALTHY (http://localhost:8000, PID: $PID)"
    else
        echo "  🟡 Backend API: DEGRADED (process running but not responding, PID: $PID)"
    fi
else
    echo "  🔴 Backend API: DOWN"
fi
echo ""

# Check HTTP Server
echo "Checking HTTP Server..."
if [ -f "$ROOT_DIR/cli/logs/httpserver.pid" ] && kill -0 $(cat "$ROOT_DIR/cli/logs/httpserver.pid") 2>/dev/null; then
    PID=$(cat "$ROOT_DIR/cli/logs/httpserver.pid")
    if curl -s http://localhost:8080 > /dev/null 2>&1; then
        echo "  🟢 HTTP Server: HEALTHY (http://localhost:8080, PID: $PID)"
    else
        echo "  🟡 HTTP Server: DEGRADED (process running but not responding, PID: $PID)"
    fi
else
    echo "  🔴 HTTP Server: DOWN"
fi
echo ""

# Check Disk Usage
echo "Checking Disk Usage..."
DISK_USAGE=$(df -h "$ROOT_DIR" | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -lt 80 ]; then
    echo "  🟢 Disk Usage: ${DISK_USAGE}% (healthy)"
elif [ "$DISK_USAGE" -lt 90 ]; then
    echo "  🟡 Disk Usage: ${DISK_USAGE}% (warning)"
else
    echo "  🔴 Disk Usage: ${DISK_USAGE}% (critical)"
fi
echo ""

# File System Stats
echo "File System Stats:"
MODULE_COUNT=$(find "$ROOT_DIR/os/modules" -name "*.md" 2>/dev/null | wc -l)
MODEL_COUNT=$(find "$ROOT_DIR/os/models" -name "*.onnx" 2>/dev/null | wc -l || echo "0")
LOG_COUNT=$(find "$ROOT_DIR/os/logs" -name "*.log" 2>/dev/null | wc -l || echo "0")

echo "  📦 Modules: $MODULE_COUNT"
echo "  🤖 Models: $MODEL_COUNT"
echo "  📋 Log Files: $LOG_COUNT"
echo ""

echo "=============================="
echo "Health check complete"
```

## Usage

```bash
# Run health check
./cli/health.md

# Run continuously (every 5 seconds)
watch -n 5 ./cli/health.md
```

## Example Output

```
🏥 Chazon System Health Check
==============================

Checking Qdrant...
  🟢 Qdrant: HEALTHY (http://localhost:6333)

Checking Backend API...
  🟢 Backend API: HEALTHY (http://localhost:8000, PID: 12345)

Checking HTTP Server...
  🟢 HTTP Server: HEALTHY (http://localhost:8080, PID: 12346)

Checking Disk Usage...
  🟢 Disk Usage: 45% (healthy)

File System Stats:
  📦 Modules: 114
  🤖 Models: 4
  📋 Log Files: 12

==============================
Health check complete
```

## Health Endpoints

| Service | Endpoint | Expected Response |
|---------|----------|-------------------|
| Qdrant | `http://localhost:6333/health` | 200 OK |
| Backend API | `http://localhost:8000/api/health` | 200 OK + JSON |
| HTTP Server | `http://localhost:8080` | 200 OK + HTML |

## Disk Usage Thresholds

- **< 80%** - 🟢 Healthy
- **80-89%** - 🟡 Warning
- **≥ 90%** - 🔴 Critical

## Troubleshooting

### Service in DEGRADED State

Process running but not responding:

```bash
# View logs
./cli/logs.md backend
./cli/logs.md http

# Restart service
./cli/restart.md
```

### High Disk Usage

```bash
# Find large files
du -sh os/* | sort -h

# Clean up logs
rm -f os/logs/**/*.log

# Clean up Docker
docker system prune -a
```

## Related

- `start.md` - Start services
- `stop.md` - Stop services
- `logs.md` - View logs
