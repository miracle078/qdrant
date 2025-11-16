#!/bin/bash
# Chazon Restart Script
# Stops and starts all services

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔄 Restarting Chazon Services"
echo ""

# Stop services
"$SCRIPT_DIR/stop.sh"

echo ""
echo "Waiting 2 seconds..."
sleep 2
echo ""

# Start services
"$SCRIPT_DIR/start.sh"
