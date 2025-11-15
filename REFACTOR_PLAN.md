# 📋 Refactor Plan
**Convert to All-Markdown Architecture** | Sub-250 Token Modules

## Goal

Convert entire repository to markdown-first architecture where:
- **All logic in .md files** < 250 tokens
- **Root-level organization** (no deep nesting)
- **MD Compiler executes** JavaScript blocks
- **PackML state machines** manage execution
- **CI/CD agents** test & deploy

## Current Structure (Before)

```
qdrant/
├── automationgpt/           # Python package (needs conversion)
│   ├── api/                 # FastAPI endpoints
│   ├── embeddings/          # Embedding functions
│   ├── ingest/              # Data pipelines
│   ├── regulatory/          # Compliance
│   └── utils/               # Utilities
│
├── chazon/                  # Already markdown-based ✅
│   ├── core/
│   ├── components/
│   ├── templates/
│   └── programs/
│
├── backend/                 # FastAPI service (needs conversion)
│   ├── api.py
│   └── requirements.txt
│
└── *.html                   # Static pages
```

## Target Structure (After)

```
qdrant/
├── modules/                 # ALL MODULES HERE (flat structure)
│   │
│   ├── embed-text.md        # Text embeddings (OpenAI)
│   ├── embed-code.md        # Code embeddings (CodeBERT)
│   ├── embed-image.md       # Image embeddings (CLIP)
│   ├── qdrant-setup.md      # Collection setup
│   ├── qdrant-client.md     # Qdrant operations
│   ├── ingest-isa.md        # ISA standards ingestion
│   ├── ingest-code.md       # Code sample ingestion
│   ├── api-health.md        # Health check endpoint
│   ├── api-query.md         # Query endpoint
│   ├── api-search.md        # Search endpoint
│   ├── api-stats.md         # Stats endpoint
│   ├── rag-retrieve.md      # Retrieval logic
│   ├── rag-format.md        # Context formatting
│   ├── rag-generate.md      # Claude generation
│   ├── regulatory-fda.md    # FDA 21 CFR Part 11
│   ├── regulatory-eu.md     # EU Annex 11
│   ├── packml.md            # PackML state machines
│   ├── mdcompiler.md        # Markdown compiler
│   ├── page-builder.md      # Page assembly
│   ├── cli.md               # Command line
│   └── [50+ more modules]
│
├── components/              # UI components
│   ├── head-default.md
│   ├── nav-main.md
│   ├── landing-hero.md
│   └── [component files]
│
├── templates/               # Page templates
│   ├── base.md
│   └── [template files]
│
├── pages/                   # Page definitions
│   ├── landing.md
│   ├── dashboard.md
│   └── [page files]
│
├── programs/                # Executable programs
│   ├── hello.md
│   ├── medical-demo.md
│   ├── qdrant-demo.md
│   └── [program files]
│
├── agents/                  # CI/CD agents
│   ├── ci-agent.md
│   ├── test-agent.md
│   └── deploy-agent.md
│
├── *.html                   # Entry points (minimal, load modules)
└── README.md                # Documentation
```

## Conversion Strategy

### Phase 1: automationgpt/ → modules/

**Current Python files** → **Target .md files**

```
automationgpt/embeddings/text_embeddings.py
  ↓
modules/embed-text.md
```

**Format:**
```markdown
# Text Embeddings
**OpenAI Embeddings** | 1536d Vectors

\`\`\`javascript
const EmbedText = {
  async embed(text, model = 'text-embedding-3-large') {
    const response = await fetch('/api/embed', {
      method: 'POST',
      body: JSON.stringify({ text, model })
    });
    return response.json();
  }
};
window.EmbedText = EmbedText;
\`\`\`
```

### Phase 2: backend/ → modules/

**Current Python API** → **Markdown API modules**

```
backend/api.py (200 lines)
  ↓
modules/api-health.md      (50 tokens)
modules/api-query.md       (80 tokens)
modules/api-search.md      (70 tokens)
modules/api-stats.md       (60 tokens)
```

**Server-side execution via:**
- Deno (TypeScript runtime)
- Node.js (JavaScript)
- Keep Python FastAPI as thin wrapper

### Phase 3: Flatten chazon/

**Current nested structure** → **Flat modules/**

```
chazon/core/attractors.md
  ↓
modules/attractors.md

chazon/medical/qdrant.md
  ↓
modules/qdrant-medical.md
```

## File Naming Convention

**Pattern:** `{category}-{function}.md`

**Categories:**
- `embed-*` - Embedding functions
- `qdrant-*` - Qdrant operations
- `ingest-*` - Data ingestion
- `api-*` - API endpoints
- `rag-*` - RAG pipeline
- `regulatory-*` - Compliance
- `packml-*` - State machines
- `ui-*` - UI components

**Examples:**
- `embed-text.md`
- `qdrant-setup.md`
- `ingest-isa.md`
- `api-query.md`
- `rag-retrieve.md`
- `regulatory-fda.md`

## Module Template

```markdown
# Module Title
**Brief Description** | Tags

Purpose and context in 1-2 sentences.

\`\`\`javascript
const ModuleName = {
  // State management
  init() {
    this.state = PackML.create('ModuleName');
    PackML.setState(this.state, 'IDLE');
  },

  async execute(params) {
    PackML.setState(this.state, 'EXECUTE');

    try {
      const result = await this.logic(params);
      PackML.setState(this.state, 'COMPLETE');
      return result;
    } catch (err) {
      PackML.setState(this.state, 'ABORTED');
      throw err;
    }
  },

  async logic(params) {
    // Actual logic here (keep under 150 tokens)
    return { success: true };
  }
};

window.ModuleName = ModuleName;
\`\`\`
```

## Bootstrap System

**index.html** loads module registry:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Chazon OS</title>
  <script src="modules/mdcompiler.md"></script>
  <script src="modules/packml.md"></script>
  <script>
    // Load module registry
    const modules = [
      'embed-text', 'embed-code', 'embed-image',
      'qdrant-client', 'qdrant-setup',
      'api-health', 'api-query',
      'rag-retrieve', 'rag-format', 'rag-generate',
      // ... 50+ more modules
    ];

    // Load all modules via MD compiler
    modules.forEach(async (mod) => {
      const md = await fetch(`modules/${mod}.md`).then(r => r.text());
      MDCompiler.compile(md);
    });
  </script>
</head>
<body>
  <!-- Content assembled from components -->
</body>
</html>
```

## Execution Flow

```
User opens index.html
  ↓
Bootstrap loads MDCompiler + PackML
  ↓
Load module registry
  ↓
For each module:
  - Fetch module.md
  - MDCompiler.compile()
  - Execute JavaScript blocks
  - Register in window.ModuleName
  ↓
Modules available globally
  ↓
Page builder assembles UI from components
  ↓
User interacts → modules execute via PackML
```

## Benefits

### 1. Extreme Modularity
- Each file < 250 tokens
- Single responsibility
- Easy to understand/test

### 2. Runtime Assembly
- No build step needed
- Dynamic loading
- Hot reload possible

### 3. Standards Compliant
- PackML state machines (ISA-88)
- L0-L4 hierarchy (ISA-95)
- Regulatory ready

### 4. CI/CD Ready
- Test individual modules
- Agent-based deployment
- Automated QA

### 5. Language Agnostic
- Markdown is universal
- JavaScript execution
- Can add Python/TypeScript blocks

## Migration Steps

### Step 1: Create modules/ directory
```bash
mkdir -p modules
```

### Step 2: Convert embeddings
```bash
# Convert automationgpt/embeddings/*.py → modules/embed-*.md
- text_embeddings.py → embed-text.md
- code_embeddings.py → embed-code.md
- image_embeddings.py → embed-image.md
```

### Step 3: Convert API endpoints
```bash
# Convert backend/api.py → modules/api-*.md
- health endpoint → api-health.md
- query endpoint → api-query.md
- search endpoint → api-search.md
- stats endpoint → api-stats.md
```

### Step 4: Convert ingestion
```bash
# Convert automationgpt/ingest/*.py → modules/ingest-*.md
- sample_data.py → ingest-isa.md, ingest-code.md
```

### Step 5: Flatten chazon/
```bash
# Move chazon/*/*.md → modules/*.md with prefixes
- chazon/core/attractors.md → modules/attractors.md
- chazon/medical/qdrant.md → modules/qdrant-medical.md
```

### Step 6: Update index.html
```bash
# Update bootstrap to load from modules/
```

### Step 7: Test & deploy
```bash
# Verify all < 250 tokens
# Test module loading
# Deploy to GitHub Pages
```

## File Count Estimate

**Before:**
- Python files: ~30
- Markdown files: ~70
- **Total:** ~100 files

**After:**
- Markdown modules: ~120
- Components: ~15
- Templates: ~5
- Programs: ~20
- **Total:** ~160 files (all .md, all < 250 tokens)

## Constraints

1. **250 Token Maximum**
   - Enforced via CI/CD
   - Agent checks on commit
   - Auto-reject if over limit

2. **Markdown Only**
   - All logic in .md files
   - JavaScript in code blocks
   - Python/TypeScript optional

3. **Flat Structure**
   - Max 1 level deep
   - modules/ contains all logic
   - components/ for UI only

4. **State Machine Wrapped**
   - All modules use PackML
   - Consistent lifecycle
   - Error handling built-in

## Success Criteria

- [ ] All files < 250 tokens
- [ ] Flat directory structure
- [ ] Markdown-first architecture
- [ ] PackML state machines
- [ ] CI/CD agents working
- [ ] All tests passing
- [ ] GitHub Pages deploys
- [ ] Documentation complete

## Timeline

- **Phase 1:** 2 hours (embeddings)
- **Phase 2:** 2 hours (API)
- **Phase 3:** 1 hour (flatten chazon)
- **Phase 4:** 1 hour (testing)
- **Total:** ~6 hours

## Next Steps

1. Review this plan
2. Approve approach
3. Start Phase 1: embeddings
4. Iterate through phases
5. Test & deploy

---

**Ready to execute!** 🚀
