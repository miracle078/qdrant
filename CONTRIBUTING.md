# Contributing to AutomationGPT

Thank you for your interest in contributing to AutomationGPT! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, inclusive, and collaborative. We're building this for the automation community.

## How to Contribute

### 1. Report Issues

Found a bug or have a feature request?
- Check existing issues first
- Create a new issue with clear description
- Include steps to reproduce (for bugs)
- Suggest solutions if possible

### 2. Submit Pull Requests

**Process:**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Add tests if applicable
5. Run tests: `pytest`
6. Format code: `black automationgpt/`
7. Commit with clear messages
8. Push to your fork
9. Submit a pull request

**PR Guidelines:**
- Clear description of changes
- Reference related issues
- Include tests for new features
- Update documentation
- Follow existing code style

### 3. Add Data Sources

Help expand the knowledge base!

**ISA Standards:**
- Add to `automationgpt/ingest/isa_standards.py`
- Parse PDFs and extract sections
- Include metadata (standard, section, level)

**PLC Code:**
- Add to `automationgpt/ingest/code_samples.py`
- Include language, platform, function
- Document ISA pattern mapping

**Diagrams:**
- Add image URLs or files
- Include descriptions and component lists
- Tag with ISA levels

**Audio/Video:**
- Add educational content
- Include transcripts and timestamps
- Tag with concepts covered

### 4. Improve Documentation

- Fix typos and clarify instructions
- Add examples and tutorials
- Improve API documentation
- Create video guides

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/qdrant
cd qdrant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks (optional)
pre-commit install
```

## Code Style

**Python:**
- Follow PEP 8
- Use `black` for formatting
- Use `flake8` for linting
- Add type hints where helpful
- Write docstrings for public APIs

**JavaScript/React:**
- Use ES6+ features
- Follow React best practices
- Keep components simple and focused

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=automationgpt

# Run specific test file
pytest automationgpt/tests/test_agent.py
```

## Project Structure

```
automationgpt/
├── __init__.py
├── agent.py              # RAG agent
├── auto_array.py         # Multimodal search
├── qdrant_setup.py       # Database setup
├── embeddings/           # Embedding utilities
│   ├── text_embeddings.py
│   ├── code_embeddings.py
│   ├── image_embeddings.py
│   └── audio_embeddings.py
├── ingest/               # Data ingestion
│   ├── sample_data.py
│   ├── isa_standards.py
│   ├── code_samples.py
│   └── audio_content.py
├── api/                  # FastAPI backend
│   └── main.py
└── tests/                # Test suite
```

## Adding New Features

### New Embedding Type

1. Create new file in `automationgpt/embeddings/`
2. Implement embedding function
3. Add to `embeddings/__init__.py`
4. Update `auto_array.py` to support new mode
5. Add tests

### New API Endpoint

1. Add route to `automationgpt/api/main.py`
2. Create request/response models
3. Update API documentation
4. Add tests

### New Collection

1. Update `COLLECTIONS` in `qdrant_setup.py`
2. Create ingestion pipeline
3. Update search modes if needed
4. Add sample data

## Priority Areas

We especially welcome contributions in:

1. **Data Ingestion:**
   - PDF parsing for ISA standards
   - GitHub scraping for PLC code
   - YouTube processing for audio

2. **Embeddings:**
   - Fine-tuned models for automation
   - Better code embeddings
   - Diagram understanding

3. **Features:**
   - Advanced search filters
   - User authentication
   - Collaborative features
   - Mobile app

4. **Documentation:**
   - Video tutorials
   - More examples
   - Deployment guides

## Questions?

- Open an issue for discussion
- Join our community discussions
- Check existing documentation

## Recognition

Contributors will be:
- Listed in README.md
- Mentioned in release notes
- Credited in documentation

Thank you for helping democratize automation knowledge! 🏭
