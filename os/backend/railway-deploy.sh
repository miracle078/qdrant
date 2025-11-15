#!/bin/bash
# Railway.app Deployment Script for Chazon OS Backend
# Free tier: 500 hours/month

set -e

echo "🚂 Railway.app Deployment Script"
echo "================================="
echo ""

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found"
    echo ""
    echo "Install with:"
    echo "  npm i -g @railway/cli"
    echo ""
    echo "Or use brew:"
    echo "  brew install railway"
    echo ""
    exit 1
fi

echo "✅ Railway CLI found"
echo ""

# Check if logged in
if ! railway whoami &> /dev/null; then
    echo "🔑 Not logged in to Railway"
    echo "Running: railway login"
    echo ""
    railway login
fi

echo "✅ Logged in to Railway"
echo ""

# Check if project exists
if ! railway status &> /dev/null; then
    echo "📦 Initializing new Railway project..."
    railway init
    echo ""
fi

echo "✅ Railway project ready"
echo ""

# Prompt for API keys
echo "🔑 Setting environment variables..."
echo ""

read -p "Enter your Cohere API key (or press Enter to skip): " COHERE_KEY
read -p "Enter your Qdrant Cloud URL (or press Enter for local): " QDRANT_URL
read -p "Enter your Qdrant API key (or press Enter if not using cloud): " QDRANT_KEY

# Set variables
if [ ! -z "$COHERE_KEY" ]; then
    railway variables set COHERE_API_KEY="$COHERE_KEY"
    echo "  ✓ COHERE_API_KEY set"
fi

if [ ! -z "$QDRANT_URL" ]; then
    railway variables set QDRANT_URL="$QDRANT_URL"
    echo "  ✓ QDRANT_URL set"
else
    railway variables set QDRANT_URL="http://localhost:6333"
    echo "  ✓ QDRANT_URL set to localhost (will need Qdrant service)"
fi

if [ ! -z "$QDRANT_KEY" ]; then
    railway variables set QDRANT_API_KEY="$QDRANT_KEY"
    echo "  ✓ QDRANT_API_KEY set"
fi

echo ""
echo "📤 Deploying to Railway..."
echo ""

railway up

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Next steps:"
echo "  1. Get your app URL: railway domain"
echo "  2. Test health endpoint: curl https://your-app.up.railway.app/health"
echo "  3. Update chazon/medical/qdrant-client.md baseURL to your Railway URL"
echo ""
echo "💡 Useful commands:"
echo "  railway logs    - View logs"
echo "  railway domain  - Get app URL"
echo "  railway open    - Open in browser"
echo ""
