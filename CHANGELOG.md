# Changelog
**Chazon Project** | All Notable Changes

All notable changes to the Chazon project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- **Template System** - Perspective-style template engine inspired by Ignition Perspective
  - `modules/template-engine.md` - Template rendering engine (UUID: 3c8e9f7a-4b2d-4e1f-9c6a-8d3f5e7a9b1c)
  - `templates/views/` - View definitions (dashboard.md, chazon.md, demo.md)
  - `templates/components/` - Component library (container.md, searchbar.md, buttongroup.md, bootscreen.md)
  - `templates/layouts/` - Page layouts (default.md)
  - `templates/build.py` - Build script to compile templates to HTML
  - `templates/README.md` - Complete template system guide
- Multi-agent collaboration system in `collab/` directory
- 5 SQLite databases for persistence (180 KB total):
  - `automationgpt.db` - Main database with 8 tables (86 KB)
  - `modules.db` - Module registry and dependencies (24 KB)
  - `embeddings.db` - Embedding cache (24 KB)
  - `qdrant.db` - Qdrant metadata (20 KB)
  - `agents.db` - Agent coordination (28 KB)
- Autonomous agents:
  - Database Management Agent (UUID: d66a2866-a53f-402e-a21f-176cef24fd83)
  - Module Management Agent (UUID: d60b9ca5-8f6f-4864-b47f-86c2d15135a5)
- Executable query scripts:
  - `query-modules.md` - Module registry queries
  - `query-embeddings.md` - Embedding cache queries
- Audio embeddings module (`embed-audio.md`) with LAION CLAP (512-dim)
- Hybrid multimodal search (`search-hybrid.md`) with Reciprocal Rank Fusion (RRF)
- Database manager module (`db-manager.md`) for browser-based SQLite
- Comprehensive documentation:
  - `REGISTRY.md` - Central module registry (94 modules)
  - `MANIFEST.md` - Complete project manifest
  - `collab/README.md` - Multi-agent system guide
  - `collab/databases/README.md` - Database schema documentation

### Changed
- **Project rebranded to "Chazon" (חזון)**
- Updated README.md with Chazon branding and φ-Balanced Computing tagline
- Updated index.html to "Chazon | φ-Balanced Modular AI Platform"
- Updated schema.sql header to "Chazon Database Schema"
- Consolidated all modules into unified `modules/` directory (94 modules)
- Module architecture now fully markdown-first with sub-250 token constraint

### Removed
- `automationgpt/` directory (21 Python files, 2,332 lines)
  - All functionality migrated to markdown modules
- `chazon/` directory (70 markdown files, 4,491 lines)
  - All files already present in `modules/` directory
- `automationgpt.html` - Old branding (replaced by chazon.html)
- `REFACTOR_PLAN.md` - Outdated (refactoring complete)
- **Total cleanup: 93 files, 7,687 lines removed**

## [2024-01] - Modular Architecture

### Added
- 84 markdown modules in `modules/` directory
- Component-based architecture with sub-250 token modules
- ISA-95 Level 0-4 compliance throughout codebase
- PackML state machines for all modules
- UUID system for all files and modules
- Module loading system for browser and CLI
- Jython 2.7 integration for Java interoperability
- X-ray visualization and AI features

### Features
- **Embeddings**: Text (OpenAI 1536d), Code (CodeBERT 768d), Image (CLIP 512d), Audio (CLAP 512d)
- **Vector Search**: Qdrant integration with 5 collections (isa, code, img, aud, doc)
- **Multimodal Search**: Hybrid search with Reciprocal Rank Fusion
- **Database**: SQLite persistence with 8 tables
- **Multi-Agent**: ISA-95 L3-L4 agent coordination
- **UI Components**: 94 modular components for dashboard, demos, and tools
- **ISA Standards**: ISA-5.1, ISA-18.2, ISA-88, ISA-95, ISA-101, ISA-106

### Architecture
- Markdown-first: All logic in .md files
- Sub-250 token constraint: Every file under 250 tokens
- Flat structure: Max 1 level nesting
- Dual execution: Python (CLI) and JavaScript (browser)
- PackML wrapped: All modules use ISA-88 state machines
- φ-Balanced: Golden ratio (1.618) design philosophy

## [2023-12] - Initial Release

### Added
- Initial project structure
- FastAPI backend
- React frontend
- Qdrant integration
- Basic embedding support
- Documentation

---

**Legend:**
- `Added` - New features
- `Changed` - Changes to existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Security fixes
