# Module Library

UUID-based markdown module system with 114 modules

**PLC Area:** Module System

## Module Organization

```
modules/
├── cli/              # CLI command modules (7 files)
├── medical/          # Medical imaging modules (10 files)
├── ai/               # AI inference modules (3 files)
├── packml/           # PackML state machine (1 file)
└── *.md              # Core modules (~93 files)
```

## Contents

- **114 total modules** - All markdown-based executable modules
- **cli/** - Command-line interface (ls, cat, help, test, git, etc.)
- **medical/** - DICOM processing, AlF-DETECT, Qdrant search
- **ai/** - Model loading, ONNX Runtime, WebGPU inference
- **packml/** - ISA-88 batch control state machine
- **module-router.md** - UUID-based routing system
- **UUID registry** - Location-independent module loading

## CLI Commands

```bash
# Navigate to modules
cd os/modules/

# Count total modules
ls -la *.md cli/*.md medical/*.md ai/*.md packml/*.md | wc -l

# View specific category
ls cli/
ls medical/
ls ai/

# Read router
cat module-router.md
```

## Key Tags

- `modulesLoaded`
- `memoryUsage`
- `cacheHitRate`

## Navigation

- **Parent:** `os/`
- **HMI Panel:** `os/modules/hmi.html`
- **PLC Logic:** `os/modules/plc.html`
- **Tag Provider:** `os/controls/tag-providers/modules.json`
- **Tag Browser:** `os/controls/tag-providers/tag-browser.html`
- **OS Gateway:** `os/index.html`
- **Root Gateway:** `index.html`
