# Configuration Files
**Chazon Project Configuration**

Build and deployment configuration files.

## Files

### Python Configuration
- **requirements.txt** - Python dependencies
- **setup.py** - Python package setup
- **pytest.ini** - Pytest configuration

### Docker Configuration
- **Dockerfile** - Docker image definition
- **docker-compose.yml** - Docker Compose services

## Usage

### Install Python Dependencies
```bash
pip install -r config/requirements.txt
```

### Install Package
```bash
pip install -e .
```

### Run Tests
```bash
pytest
```

### Docker Build
```bash
docker-compose -f config/docker-compose.yml up
```

## Notes

All configuration files moved from root to keep root directory clean.
