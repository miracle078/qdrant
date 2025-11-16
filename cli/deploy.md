# Deploy to GitHub Pages
**UUID:** cli-deploy-001
**ISA-95 L4: Business Layer** | Markdown Executable

Deploy the application to GitHub Pages.

## Process

1. Checks for git repository
2. Warns about uncommitted changes
3. Gets current branch name
4. Pushes to origin
5. GitHub Actions deploys to Pages

```bash
#!/bin/bash
# Deploy to GitHub Pages

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$ROOT_DIR"

echo "🚀 Deploying to GitHub Pages"
echo "============================="
echo ""

# Check if this is a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not a git repository"
    echo "Run: git init"
    exit 1
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "⚠️  Warning: You have uncommitted changes"
    echo ""
    git status --short
    echo ""
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Deployment cancelled"
        exit 1
    fi
fi

# Get current branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $BRANCH"
echo ""

# Push to origin
echo "Pushing to origin..."
git push origin "$BRANCH"

echo ""
echo "============================="
echo "✅ Deployed!"
echo ""
echo "Deployment URL:"
echo "  🌐 https://teslasolar.github.io/qdrant/"
echo ""
echo "Note: GitHub Pages may take a few minutes to update"
echo ""
echo "Check deployment status:"
echo "  https://github.com/teslasolar/qdrant/actions"
```

## Usage

```bash
# Deploy current branch
./cli/deploy.md
```

## Deployment URL

**Live Site:** https://teslasolar.github.io/qdrant/

## Prerequisites

- Git repository initialized
- Remote origin configured
- GitHub Pages enabled in repository settings
- GitHub Actions workflow configured (optional but recommended)

## GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main, master]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
          exclude_assets: '.github,cli,os/backend,**/*.py,**/*.sh'
```

## What Gets Deployed

The entire static site including:
- HTML files (index.html, scada.html, hmi.html, plc.html)
- Markdown modules (os/modules/*.md)
- JavaScript files
- CSS files
- Medical imaging files
- Documentation

## What's Excluded

Backend services (run separately):
- Python backend (os/backend/)
- Qdrant database
- Server-side processing

## Deployment Checklist

1. ✅ Run tests: `./cli/dev/test.md`
2. ✅ Health check: `./cli/health.md`
3. ✅ Commit changes: `git commit -am "Your message"`
4. ✅ Deploy: `./cli/deploy.md`
5. ✅ Verify: Open deployment URL

## Troubleshooting

### Push Rejected

```bash
# Pull latest changes first
git pull origin main

# Then deploy again
./cli/deploy.md
```

### GitHub Pages Not Enabled

1. Go to repository Settings
2. Navigate to Pages section
3. Select source branch (usually `main` or `gh-pages`)
4. Click Save

### Deployment Not Updating

```bash
# Check GitHub Actions
# https://github.com/teslasolar/qdrant/actions

# Force update
git commit --allow-empty -m "Trigger deployment"
git push origin main
```

## Manual Deployment

If automatic deployment fails:

```bash
# Build (if needed)
./cli/dev/build.md

# Create gh-pages branch
git checkout -b gh-pages

# Commit and push
git add .
git commit -m "Deploy"
git push -f origin gh-pages

# Switch back
git checkout main
```

## Related

- `dev/build.md` - Build assets
- `health.md` - Pre-deployment health check
- `dev/test.md` - Run tests before deployment
