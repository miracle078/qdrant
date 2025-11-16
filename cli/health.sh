#!/bin/bash
# Chazon Health Check Script
# Checks the health of all services

set -e

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
    echo "  🔴 Qdrant: DOWN (container not running)"
fi

# Check Backend API
echo "Checking Backend API..."
if [ -f "$ROOT_DIR/cli/logs/backend.pid" ]; then
    PID=$(cat "$ROOT_DIR/cli/logs/backend.pid")
    if kill -0 "$PID" 2>/dev/null; then
        if curl -s http://localhost:8000/api/health > /dev/null 2>&1; then
            echo "  🟢 Backend API: HEALTHY (http://localhost:8000)"
        else
            echo "  🟡 Backend API: DEGRADED (process running but not responding)"
        fi
    else
        echo "  🔴 Backend API: DOWN (process not running)"
    fi
else
    echo "  🔴 Backend API: DOWN (not started)"
fi

# Check HTTP Server
echo "Checking HTTP Server..."
if [ -f "$ROOT_DIR/cli/logs/httpserver.pid" ]; then
    PID=$(cat "$ROOT_DIR/cli/logs/httpserver.pid")
    if kill -0 "$PID" 2>/dev/null; then
        if curl -s http://localhost:8080/index.html > /dev/null 2>&1; then
            echo "  🟢 HTTP Server: HEALTHY (http://localhost:8080)"
        else
            echo "  🟡 HTTP Server: DEGRADED (process running but not responding)"
        fi
    else
        echo "  🔴 HTTP Server: DOWN (process not running)"
    fi
else
    echo "  🔴 HTTP Server: DOWN (not started)"
fi

# Check disk space
echo ""
echo "System Resources:"
DISK_USAGE=$(df -h "$ROOT_DIR" | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -lt 80 ]; then
    echo "  🟢 Disk Usage: ${DISK_USAGE}% (healthy)"
elif [ "$DISK_USAGE" -lt 90 ]; then
    echo "  🟡 Disk Usage: ${DISK_USAGE}% (warning)"
else
    echo "  🔴 Disk Usage: ${DISK_USAGE}% (critical)"
fi

# Check file counts
echo ""
echo "File System:"
MODULE_COUNT=$(find "$ROOT_DIR/os/modules" -name "*.md" 2>/dev/null | wc -l || echo "0")
echo "  📦 Modules: $MODULE_COUNT"

if [ -d "$ROOT_DIR/os/models" ]; then
    MODEL_COUNT=$(find "$ROOT_DIR/os/models" -name "*.onnx" 2>/dev/null | wc -l || echo "0")
    echo "  🤖 Models: $MODEL_COUNT"
fi

LOG_COUNT=$(find "$ROOT_DIR/os/logs" -name "*.log" 2>/dev/null | wc -l || echo "0")
echo "  📋 Log Files: $LOG_COUNT"

echo ""
echo "=============================="
echo "Health check complete"
