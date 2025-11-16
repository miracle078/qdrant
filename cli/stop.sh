#!/bin/bash
# Chazon Services Stop Script
# Stops all running services

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🛑 Stopping Chazon Services"
echo "==========================="
echo ""

# Stop Backend API
if [ -f "$ROOT_DIR/cli/logs/backend.pid" ]; then
    PID=$(cat "$ROOT_DIR/cli/logs/backend.pid")
    if kill -0 "$PID" 2>/dev/null; then
        echo "Stopping Backend API (PID: $PID)..."
        kill "$PID"
        rm "$ROOT_DIR/cli/logs/backend.pid"
        echo "  ✅ Backend API stopped"
    else
        echo "  ℹ️  Backend API not running"
        rm "$ROOT_DIR/cli/logs/backend.pid"
    fi
else
    echo "  ℹ️  No Backend API PID file found"
fi

# Stop HTTP server
if [ -f "$ROOT_DIR/cli/logs/httpserver.pid" ]; then
    PID=$(cat "$ROOT_DIR/cli/logs/httpserver.pid")
    if kill -0 "$PID" 2>/dev/null; then
        echo "Stopping HTTP server (PID: $PID)..."
        kill "$PID"
        rm "$ROOT_DIR/cli/logs/httpserver.pid"
        echo "  ✅ HTTP server stopped"
    else
        echo "  ℹ️  HTTP server not running"
        rm "$ROOT_DIR/cli/logs/httpserver.pid"
    fi
else
    echo "  ℹ️  No HTTP server PID file found"
fi

# Stop Qdrant
if docker ps | grep -q qdrant; then
    echo "Stopping Qdrant container..."
    docker stop qdrant > /dev/null
    docker rm qdrant > /dev/null
    echo "  ✅ Qdrant stopped"
else
    echo "  ℹ️  Qdrant not running"
fi

echo ""
echo "==========================="
echo "✅ All services stopped"
