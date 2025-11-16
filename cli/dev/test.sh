#!/bin/bash
# Run all tests

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

echo "🧪 Running Chazon Tests"
echo "======================="
echo ""

cd "$ROOT_DIR"

# Run pytest if available
if [ -d "os/test-modules" ]; then
    echo "Running module tests..."
    cd os/test-modules

    if command -v pytest &> /dev/null; then
        pytest -v
        echo "  ✅ Module tests passed"
    else
        echo "  ⚠️  pytest not installed"
        echo "     Install with: pip install pytest"
    fi

    cd "$ROOT_DIR"
fi

# Run backend tests if they exist
if [ -f "os/backend/test_api.py" ]; then
    echo ""
    echo "Running backend tests..."
    cd os/backend
    source venv/bin/activate 2>/dev/null || true
    pytest test_api.py -v
    deactivate 2>/dev/null || true
    cd "$ROOT_DIR"
    echo "  ✅ Backend tests passed"
fi

echo ""
echo "======================="
echo "✅ All tests completed"
