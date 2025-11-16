#!/bin/bash
# Development Environment Setup

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

echo "🔧 Setting up development environment"
echo "======================================"
echo ""

cd "$ROOT_DIR"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

echo "Python: $(python3 --version)"

# Create virtual environment for backend
if [ -d "os/backend" ]; then
    echo ""
    echo "Setting up backend virtual environment..."
    cd os/backend
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        echo "  ✅ Backend dependencies installed"
    fi
    deactivate
    cd "$ROOT_DIR"
fi

# Check Node.js (optional)
if command -v node &> /dev/null; then
    echo ""
    echo "Node.js: $(node --version)"
    echo "npm: $(npm --version)"

    # Install frontend dependencies if package.json exists
    if [ -f "os/frontend/package.json" ]; then
        echo ""
        echo "Installing frontend dependencies..."
        cd os/frontend
        npm install
        echo "  ✅ Frontend dependencies installed"
        cd "$ROOT_DIR"
    fi
else
    echo ""
    echo "⚠️  Node.js not found (optional)"
fi

# Check Docker
if command -v docker &> /dev/null; then
    echo ""
    echo "Docker: $(docker --version)"
else
    echo ""
    echo "⚠️  Docker not found (required for Qdrant)"
fi

# Create log directories
mkdir -p cli/logs
echo ""
echo "  ✅ Log directories created"

# Create .env if it doesn't exist
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    echo ""
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo "  ✅ .env created (please update with your API keys)"
fi

echo ""
echo "======================================"
echo "✅ Development environment ready!"
echo ""
echo "Next steps:"
echo "  1. Update .env with your API keys"
echo "  2. Run: ./cli/start.sh"
echo "  3. Open: http://localhost:8080"
