# Development Environment Setup
**UUID:** cli-dev-setup-001
**ISA-95 L3: MES Layer** | Markdown Executable

Sets up the complete development environment.

## Actions

1. Checks Python 3.8+ availability
2. Creates backend virtual environment
3. Installs backend dependencies (requirements.txt)
4. Checks Node.js (optional)
5. Installs frontend dependencies if package.json exists
6. Creates log directories
7. Creates .env from .env.example

```bash
#!/bin/bash
# Development Environment Setup

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../..\" && pwd)"

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
echo "  2. Run: ./cli/start.md"
echo "  3. Open: http://localhost:8080"
```

## Usage

```bash
# Setup development environment
./cli/dev/setup.md
```

## Requirements

- **Python 3.8+** - Required for backend
- **Node.js** - Optional, for frontend development
- **Docker** - Required for Qdrant vector database

## What Gets Installed

### Backend (Python)
- Virtual environment in `os/backend/venv/`
- All packages from `os/backend/requirements.txt`:
  - FastAPI
  - Uvicorn
  - Qdrant client
  - OpenAI SDK
  - And more...

### Frontend (Node.js) - Optional
- All packages from `os/frontend/package.json` if it exists
- React and related dependencies

## Post-Setup

1. **Update .env file** with your API keys:
   ```bash
   nano .env
   ```

2. **Start services**:
   ```bash
   ./cli/start.md
   ```

3. **Run health check**:
   ```bash
   ./cli/health.md
   ```

4. **Open browser**:
   ```
   http://localhost:8080
   ```

## Environment Variables

The `.env` file should contain:

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

## Troubleshooting

### Python Version Too Old

```bash
# Check Python version
python3 --version

# Install Python 3.8+ using your package manager
# macOS:
brew install python@3.11

# Ubuntu/Debian:
sudo apt install python3.11

# Update alternatives
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
```

### Virtual Environment Creation Failed

```bash
# Install venv module
sudo apt install python3-venv  # Ubuntu/Debian
# or
brew install python3           # macOS

# Try again
cd os/backend
python3 -m venv venv
```

### Docker Not Found

```bash
# Install Docker
# macOS: Download from docker.com
# Ubuntu:
sudo apt install docker.io
sudo systemctl start docker
sudo usermod -aG docker $USER
```

### Permission Denied

```bash
# Make scripts executable
chmod +x cli/*.md
chmod +x cli/dev/*.md
chmod +x cli/models/*.md
```

## Related

- `test.md` - Run tests
- `../start.md` - Start services
- `../health.md` - Health check
