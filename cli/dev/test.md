# Run Tests
**UUID:** cli-dev-test-001
**ISA-95 L2: Supervisory Control** | Markdown Executable

Runs all available test suites.

## Test Suites

1. **Module tests** - os/test-modules with pytest
2. **Backend API tests** - os/backend/test_api.py

```bash
#!/bin/bash
# Run all tests

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../..\" && pwd)"

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
```

## Usage

```bash
# Run all tests
./cli/dev/test.md

# Run with verbose output
./cli/dev/test.md -v

# Run specific test file
cd os/test-modules
pytest test_specific.py -v
```

## Requirements

- **pytest** - `pip install pytest`
- **Backend virtual environment** - Run `./cli/dev/setup.md` first

## Test Structure

```
os/
├── test-modules/          # Module unit tests
│   ├── test_chazon_os.py
│   ├── test_compiler.py
│   └── ...
└── backend/
    └── test_api.py        # Backend API tests
```

## Example Output

```
🧪 Running Chazon Tests
=======================

Running module tests...
============================= test session starts ==============================
collected 24 items

test_chazon_os.py::test_module_loading PASSED                            [  4%]
test_chazon_os.py::test_packml_states PASSED                             [  8%]
test_compiler.py::test_markdown_compilation PASSED                       [ 12%]
...

============================== 24 passed in 2.34s ==============================
  ✅ Module tests passed

Running backend tests...
============================= test session starts ==============================
collected 12 items

test_api.py::test_health_endpoint PASSED                                 [  8%]
test_api.py::test_search_endpoint PASSED                                 [ 16%]
test_api.py::test_collection_creation PASSED                             [ 25%]
...

============================== 12 passed in 1.56s ==============================
  ✅ Backend tests passed

=======================
✅ All tests completed
```

## Writing Tests

### Module Tests

Create test files in `os/test-modules/`:

```python
# test_my_module.py
import pytest

def test_module_exists():
    assert True

def test_module_functionality():
    result = my_function()
    assert result == expected_value
```

### Backend Tests

Add tests to `os/backend/test_api.py`:

```python
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

## Test Coverage

```bash
# Install coverage
pip install pytest-cov

# Run with coverage
cd os/test-modules
pytest --cov=. --cov-report=html

# View report
open htmlcov/index.html
```

## Continuous Testing

```bash
# Watch mode (requires pytest-watch)
pip install pytest-watch
cd os/test-modules
ptw

# Run on file change
while inotifywait -e modify os/**/*.py; do
    ./cli/dev/test.md
done
```

## Troubleshooting

### pytest Not Found

```bash
# Install pytest
pip install pytest

# Or in virtual environment
cd os/backend
source venv/bin/activate
pip install pytest
```

### Tests Fail

```bash
# Run with verbose output
pytest -v

# Run with debugging
pytest -v -s

# Run single test
pytest test_file.py::test_function_name -v

# Show local variables on failure
pytest -v -l
```

### Import Errors

```bash
# Add project root to PYTHONPATH
export PYTHONPATH="$PWD:$PYTHONPATH"

# Or in pytest.ini
[pytest]
pythonpath = .
```

## CI/CD Integration

### GitHub Actions

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install pytest
          cd os/backend && pip install -r requirements.txt

      - name: Run tests
        run: ./cli/dev/test.md
```

## Related

- `setup.md` - Setup development environment
- `../health.md` - System health check
- `../deploy.md` - Deploy after tests pass
