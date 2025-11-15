# Chazon Medical Imaging SCADA System

**Status:** Production | **License:** MIT | **Live:** https://teslasolar.github.io/qdrant/

## Quick Start

```bash
# Clone
git clone https://github.com/teslasolar/qdrant && cd qdrant

# Run client-side (no install)
open index.html

# Full stack
docker run -p 6333:6333 qdrant/qdrant
pip install -r os/backend/requirements.txt
python os/backend/api.py
```

## Key URLs

- **SCADA Gateway:** `/index.html`
- **SCADA Master:** `/scada.html`
- **PLC Controller:** `/plc.html`
- **HMI Panel:** `/hmi.html`
- **Chazon OS:** `/os/index.html`
- **Frontend:** `/os/frontend/index.html`
- **Backend API:** `/os/backend/index.html`
- **Modules:** `/os/modules/index.html`
- **Boot:** `/os/boot/index.html`
- **Models:** `/os/models/index.html`
- **Data:** `/os/data/index.html`
- **Language:** `/os/language/index.html`
- **Templates:** `/os/templates/`
- **AlF-DETECT:** `/os/medical/alf-detect.html`
- **Debug:** `/os/debug/index.html`

## File Structure

```
qdrant/
├── index.html          # SCADA Gateway landing
├── scada.html          # Master SCADA control
├── plc.html            # Master PLC logic
├── hmi.html            # Master HMI panel
├── standards/          # ISA standards
│   └── isa/
│       ├── isa-88/     # Batch control
│       ├── isa-95/     # Enterprise-control
│       └── isa-101/    # HMI design
├── docs/               # Documentation
├── config/             # Docker, pytest configs
├── scripts/            # Setup/deployment scripts
├── collab/             # Multi-agent workspace
└── os/                 # Operating System (all runtime components)
    ├── index.html      # OS gateway
    ├── module-router.md # UUID-based module discovery
    ├── frontend/       # Medical viewer UI
    ├── backend/        # FastAPI server
    ├── modules/        # 114 markdown modules
    ├── boot/           # 6-phase boot system
    ├── debug/          # Debug console
    ├── models/         # AI models (ONNX)
    ├── medical/        # AlF-DETECT runtime
    ├── data/           # SQL databases, architecture maps
    ├── language/       # SNT/trinary compiler
    └── templates/      # ISA template engine
```

## Architecture

**Factory Automation Model (ISA-95):**
- 8 PLC areas (Frontend, Backend, Modules, Boot, Models, Data, Language, Medical)
- Master SCADA gateway with real-time monitoring
- HMI operator panels for each area
- PackML state machines for module control

**Medical Imaging:**
- DICOM-compliant viewer (X-Ray, CT, MRI)
- AlF-DETECT: Alzheimer's/Autism early detection
- Qdrant vector search for case similarity
- WebGPU client-side inference

**Boot System:**
- Phase 0: Core (OS, Compiler, PackML)
- Phase 1: AI (ONNX, WebGPU, Models)
- Phase 2: Multi-Agent (Swarm, Conway, GPT)
- Phase 3: Medical (DICOM, Qdrant, Imaging)
- Phase 4: UI (Components, Icons, Screens)
- Phase 5: Templates (ISA, Views, Medical)

## CLI Commands

```bash
# Backend API
cd os/backend && python api.py

# Qdrant Docker
docker run -p 6333:6333 qdrant/qdrant

# MCP Servers
python os/backend/mcp-codesign.py
python os/backend/mcp-qdrant.py
python os/backend/mcp-sqlite.py

# Local server
python3 -m http.server 8080

# Download AI models
cd os/models && python download-models.py

# Deploy to GitHub Pages
git push origin claude/automation-gpt-multimodal-search-*
```

## Key Technologies

- **Vector DB:** Qdrant for medical case search
- **AI:** ONNX Runtime, WebGPU inference
- **Language:** SNT (Space-Time Notation), trinary computing
- **Medical:** DICOM, dual-energy X-ray, Vision Transformers
- **Architecture:** Markdown-first (114 modules), token-dense storage
- **SCADA:** Ignition Perspective-style factory automation

## API Endpoints

```
POST /analyze       # Analyze medical image
POST /search        # Qdrant similarity search
POST /study         # Create DICOM study
POST /report        # Generate radiology report
GET  /health        # Health check
```

## Environment

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
QDRANT_URL=https://xyz.qdrant.io
QDRANT_API_KEY=...
COHERE_API_KEY=...
```

## Key Components

**Medical Imaging:**
- `os/modules/medical-imaging.md` - Core imaging system
- `os/modules/medical-xray-analyzer.md` - X-ray AI analysis
- `os/modules/medical-dicom-viewer.md` - DICOM viewer
- `os/modules/medical-qdrant.md` - Vector search integration
- `os/medical/alf-detect.html` - AlF-DETECT Alzheimer's/Autism detection

**SNT Language:**
- Space-Time Notation with trinary computing
- Base-3 arithmetic, emoji compression
- See: `os/language/` directory

**ISA Standards:**
- ISA-88: Batch control, procedural model
- ISA-95: Enterprise-control integration
- ISA-101: HMI design guidelines
- See: `standards/isa/` directory

## License

MIT - Open source for medical/educational use

## More Info

See `ABOUT.md` for vision, features, acknowledgments.
