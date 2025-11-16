#!/bin/bash
# Chazon Deploy Script
# Deploys to GitHub Pages

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🚀 Deploying to GitHub Pages"
echo "============================="
echo ""

cd "$ROOT_DIR"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository"
    exit 1
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  Warning: You have uncommitted changes"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Deployment cancelled"
        exit 1
    fi
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"

# Push to origin
echo ""
echo "Pushing to origin..."
git push origin "$CURRENT_BRANCH"

echo ""
echo "============================="
echo "✅ Deployment complete!"
echo ""
echo "Your site will be available at:"
echo "  https://teslasolar.github.io/qdrant/"
echo ""
echo "Note: GitHub Pages may take a few minutes to update"
