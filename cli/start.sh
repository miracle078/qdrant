#!/bin/bash
# Chazon Services Start Script
# Starts all backend services

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🔄 Starting Chazon Services"
echo "==========================="
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Start Qdrant vector database
echo "Starting Qdrant vector database..."
if ! docker ps | grep -q qdrant; then
    docker run -d --name qdrant -p 6333:6333 qdrant/qdrant:latest
    echo "  ✅ Qdrant started on port 6333"
else
    echo "  ℹ️  Qdrant already running"
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python."
    exit 1
fi

# Start Backend API
echo ""
echo "Starting Backend API..."
if [ -f "$ROOT_DIR/os/backend/api.py" ]; then
    cd "$ROOT_DIR/os/backend"

    # Check if virtual environment exists
    if [ ! -d "venv" ]; then
        echo "  Creating virtual environment..."
        python3 -m venv venv
    fi

    # Activate virtual environment
    source venv/bin/activate

    # Install requirements if needed
    if [ -f "requirements.txt" ]; then
        echo "  Installing dependencies..."
        pip install -q -r requirements.txt
    fi

    # Start API in background
    echo "  Starting FastAPI server..."
    nohup python api.py > "$ROOT_DIR/cli/logs/backend.log" 2>&1 &
    echo $! > "$ROOT_DIR/cli/logs/backend.pid"
    echo "  ✅ Backend API started (PID: $(cat "$ROOT_DIR/cli/logs/backend.pid"))"
    echo "     Log: $ROOT_DIR/cli/logs/backend.log"
    echo "     URL: http://localhost:8000"
else
    echo "  ⚠️  Backend API not found at $ROOT_DIR/os/backend/api.py"
fi

# Start development server for frontend
echo ""
echo "Starting development server..."
cd "$ROOT_DIR"
echo "  Starting HTTP server on port 8080..."
nohup python3 -m http.server 8080 > "$ROOT_DIR/cli/logs/httpserver.log" 2>&1 &
echo $! > "$ROOT_DIR/cli/logs/httpserver.pid"
echo "  ✅ HTTP server started (PID: $(cat "$ROOT_DIR/cli/logs/httpserver.pid"))"
echo "     Log: $ROOT_DIR/cli/logs/httpserver.log"
echo "     URL: http://localhost:8080"

echo ""
echo "==========================="
echo "✅ All services started!"
echo ""
echo "Services running:"
echo "  🟢 Qdrant:     http://localhost:6333"
echo "  🟢 Backend:    http://localhost:8000"
echo "  🟢 Frontend:   http://localhost:8080"
echo ""
echo "Check health: ./cli/health.sh"
echo "Stop services: ./cli/stop.sh"
echo "View logs: ./cli/logs.sh"
