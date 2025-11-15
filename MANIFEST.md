# Chazon Project Manifest
**UUID:** a9504de3-8007-4e73-b18e-74470498dfe8
**Project Root** | ISA-95 L4: Business Planning

Complete manifest of the Chazon (חזון) project with modular markdown architecture.

## 📁 Root Structure

```
/
├── index.html              # Landing page with module bootstrap
├── schema.sql              # SQLite database schema
├── REGISTRY.md             # Module registry with UUIDs
├── MANIFEST.md             # This file (project manifest)
├── REFACTOR_PLAN.md        # Architecture refactoring plan
├── COMPONENT_ARCHITECTURE.md # Component system docs
├── test-modules.html       # Module testing interface
├── dashboard.html          # Unified demo dashboard
│
├── modules/                # 92 markdown modules
│   ├── Core System (17)
│   │   ├── chazon-packml.md          # ISA-88 state machine
│   │   ├── chazon-mdcompiler.md      # Markdown compiler
│   │   ├── chazon-cli.md             # Command-line interface
│   │   ├── db-manager.md             # SQLite manager (UUID: d6f529de...)
│   │   └── module-registry.md        # Registry runtime (UUID: c16e00c3...)
│   │
│   ├── Embeddings (6)
│   │   ├── embed-openai.md           # OpenAI 1536-dim (UUID: 760e861d...)
│   │   ├── embed-codebert.md         # CodeBERT 768-dim (UUID: f66182df...)
│   │   ├── embed-clip.md             # CLIP 512-dim (UUID: c6a53bf8...)
│   │   ├── embed-text.md             # Text embeddings
│   │   ├── embed-code.md             # Code embeddings
│   │   └── ingest-*.md               # Ingestion modules
│   │
│   ├── API (6)
│   │   ├── api-health.md             # Health checks
│   │   ├── api-search.md             # Vector search
│   │   ├── api-index.md              # Document indexing
│   │   ├── api-embed.md              # Embeddings endpoint
│   │   ├── api-collections.md        # Qdrant collections
│   │   └── api-stats.md              # Analytics
│   │
│   ├── Agents (5)
│   │   ├── agent-automationgpt.md    # RAG agent (UUID: 59ae07f8...)
│   │   ├── agent-ci.md               # CI/CD agent
│   │   ├── agent-deploy.md           # Deployment agent
│   │   ├── agent-test.md             # Test agent
│   │   └── agent-index.md            # Agent index
│   │
│   ├── Regulatory (2)
│   │   ├── regulatory-cfr-part-11.md # FDA 21 CFR Part 11 (UUID: d20d52e3...)
│   │   └── regulatory-eu-annex-11.md # EU Annex 11 (UUID: 165af54f...)
│   │
│   ├── Jython/Factory (5)
│   │   ├── jython-compiler.md        # Jython 2.7 compiler
│   │   ├── gateway-ignition.md       # Pseudo Ignition gateway
│   │   ├── plc-repo.md               # Repository PLC
│   │   ├── hmi-repo.md               # Repository HMI
│   │   └── xray-jython.md            # X-ray analysis
│   │
│   ├── ISA Standards (3)
│   ├── Medical (8)
│   ├── UI (7)
│   ├── Programs (14)
│   ├── Components (8)
│   ├── Pages/Templates (5)
│   └── Other (11)
│
├── automationgpt/          # Legacy Python (to be deprecated)
├── backend/                # FastAPI backend
├── chazon/                 # Component files (source for modules/)
├── docs/                   # Documentation
└── frontend/               # React frontend
```

## 🔑 Key Files

| File | UUID | Purpose |
|------|------|---------|
| schema.sql | 8b79fb96-ef94-4fea-b508-6eb6aa3a373a | Database schema |
| REGISTRY.md | e118731b-4918-489d-beac-f1732834ab39 | Module registry |
| MANIFEST.md | a9504de3-8007-4e73-b18e-74470498dfe8 | This manifest |
| modules/db-manager.md | d6f529de-e759-49f9-abcd-cd30e902626a | Database manager |
| modules/module-registry.md | c16e00c3-0ad6-481c-9d2d-586d643994a3 | Registry runtime |

## 📊 Statistics

- **Total Files**: 400+
- **Markdown Modules**: 92
- **With UUIDs**: 10+
- **Lines of Code**: ~5000+ in modules/
- **Average Module Size**: <250 tokens
- **ISA Compliance**: ISA-95 L0-L4, ISA-88, ISA-18.2

## 🏗️ Architecture

### Markdown-First Architecture
- All logic in `.md` files with JavaScript code blocks
- Sub-250 token constraint for extreme modularity
- Dynamic module loader with caching
- Exports to `window.ModuleName` for global access

### ISA-95 Hierarchy
- **L4**: Business planning (agents, registry, manifest)
- **L3**: MES/operations (API, database, search)
- **L2**: Supervisory control (PLC, HMI, SCADA)
- **L1**: Control (PackML state machines)
- **L0**: Field devices (sensors, embeddings)

### PackML State Machines
All modules use ISA-88 PackML states:
- IDLE → STARTING → EXECUTE → COMPLETING → COMPLETE
- STOPPING → STOPPED
- ABORTING → ABORTED → CLEARING → IDLE

## 🚀 Quick Start

### Browser Console
```javascript
// Initialize module system
await ModuleLoader.loadAll(['chazon-packml', 'db-manager', 'module-registry']);

// Initialize database
await DatabaseManager.init();

// Load registry
await ModuleRegistry.init();

// Load AutomationGPT agent
const agent = await ModuleLoader.load('agent-automationgpt');
agent.init('your-anthropic-key');

// Query ISA standards
const result = await agent.query('Explain ISA-95 Level 3');
console.log(result.answer);
```

### Module Development
```javascript
// Create new module: modules/my-module.md
// UUID: <generate with uuid.uuid4()>
// Module Name | Description

// ```javascript
const MyModule = {
  init() {
    console.log('Initialized');
    return this;
  }
};

window.MyModule = MyModule;
// ```

// Register in REGISTRY.md
// Add to dependency graph if needed
```

## 📦 Dependencies

See `REGISTRY.md` for complete dependency graph.

## 🧪 Testing

Open `test-modules.html` in browser to run comprehensive tests.

## 📝 License

Open source - built for the automation community.
