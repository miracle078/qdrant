#!/bin/bash
# AutomationGPT Setup Script

set -e

echo "🏭 AutomationGPT Setup"
echo "====================="
echo ""

# Check prerequisites
echo "Checking prerequisites..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi
echo "✓ Docker found"

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi
echo "✓ Docker Compose found"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ first."
    exit 1
fi
echo "✓ Python 3 found"

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.9"
if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION or higher is required (found $PYTHON_VERSION)"
    exit 1
fi
echo "✓ Python $PYTHON_VERSION"

echo ""
echo "Setting up environment..."

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your API keys:"
    echo "   - ANTHROPIC_API_KEY"
    echo "   - OPENAI_API_KEY"
    echo ""
    read -p "Press Enter when you've added your API keys..."
else
    echo "✓ .env file exists"
fi

# Check if API keys are set
source .env
if [ -z "$ANTHROPIC_API_KEY" ] || [ "$ANTHROPIC_API_KEY" = "your_anthropic_api_key_here" ]; then
    echo "⚠️  Warning: ANTHROPIC_API_KEY not set in .env"
fi
if [ -z "$OPENAI_API_KEY" ] || [ "$OPENAI_API_KEY" = "your_openai_api_key_here" ]; then
    echo "⚠️  Warning: OPENAI_API_KEY not set in .env"
fi

echo ""
echo "Starting services with Docker Compose..."
docker-compose up -d

echo ""
echo "Waiting for Qdrant to be ready..."
sleep 5

echo ""
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "Ingesting sample data..."
python -m automationgpt.ingest.sample_data

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Quick Start:"
echo "   - API: http://localhost:8000"
echo "   - Frontend: Open index.html in your browser"
echo "   - Docs: http://localhost:8000/docs"
echo ""
echo "📊 Check status:"
echo "   curl http://localhost:8000/health"
echo ""
echo "🔍 Test query:"
echo "   curl -X POST http://localhost:8000/query \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"q\":\"What is ISA-95 level 3?\",\"mode\":\"hybrid\"}'"
echo ""
echo "Happy searching! 🏭"
