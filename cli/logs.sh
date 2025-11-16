#!/bin/bash
# Chazon Logs Viewer
# View logs for different areas

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

AREA=${1:-"all"}

echo "📋 Chazon System Logs"
echo "====================="
echo ""

case "$AREA" in
    backend)
        echo "Backend API Logs:"
        echo "----------------"
        if [ -f "$ROOT_DIR/cli/logs/backend.log" ]; then
            tail -f "$ROOT_DIR/cli/logs/backend.log"
        else
            echo "No backend logs found"
        fi
        ;;
    http)
        echo "HTTP Server Logs:"
        echo "----------------"
        if [ -f "$ROOT_DIR/cli/logs/httpserver.log" ]; then
            tail -f "$ROOT_DIR/cli/logs/httpserver.log"
        else
            echo "No HTTP server logs found"
        fi
        ;;
    system)
        echo "System Logs:"
        echo "-----------"
        if [ -d "$ROOT_DIR/os/logs/system" ]; then
            tail -f "$ROOT_DIR/os/logs/system"/*.log 2>/dev/null || echo "No system logs found"
        else
            echo "No system logs directory found"
        fi
        ;;
    all|*)
        echo "All Service Logs:"
        echo "----------------"
        echo ""
        echo "Backend API:"
        [ -f "$ROOT_DIR/cli/logs/backend.log" ] && tail -n 10 "$ROOT_DIR/cli/logs/backend.log" || echo "  No logs"
        echo ""
        echo "HTTP Server:"
        [ -f "$ROOT_DIR/cli/logs/httpserver.log" ] && tail -n 10 "$ROOT_DIR/cli/logs/httpserver.log" || echo "  No logs"
        echo ""
        echo "System:"
        if [ -d "$ROOT_DIR/os/logs/system" ]; then
            tail -n 10 "$ROOT_DIR/os/logs/system"/*.log 2>/dev/null || echo "  No logs"
        else
            echo "  No logs"
        fi
        echo ""
        echo "====================="
        echo "Usage: ./cli/logs.sh [backend|http|system|all]"
        echo "Use tail -f for live updates"
        ;;
esac
