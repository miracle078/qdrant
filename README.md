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
pip install -r requirements.txt
python backend/api.py
```

## Key URLs

- **SCADA Gateway:** `/index.html`
- **SCADA Master:** `/scada.html`
- **PLC Controller:** `/plc.html`
- **HMI Panel:** `/hmi.html`
- **AlF-DETECT:** `/medical/alf-detect.html`
- **Frontend:** `/frontend/index.html`
- **Debug Console:** `/debug/index.html`
- **API Status:** `/backend/index.html`

## File Structure

```
qdrant/
├── index.html          # SCADA Gateway landing
├── scada.html          # Master SCADA control
├── plc.html            # Master PLC logic
├── hmi.html            # Master HMI panel
├── boot/               # 6-phase boot system
│   ├── index.html      # Boot dashboard
│   ├── boot-phase0-core.md
│   ├── boot-phase1-ai.md
│   ├── boot-phase2-agents.md
│   ├── boot-phase3-medical.md
│   ├── boot-phase4-ui.md
│   └── boot-phase5-templates.md
├── modules/            # 114 markdown modules
│   ├── index.html      # Module browser
│   ├── medical-*.md    # Medical imaging
│   ├── chazon-*.md     # Core OS
│   ├── qdrant-*.md     # Vector DB
│   └── ui-*.md         # UI components
├── models/             # AI models
│   ├── index.html      # Model manager
│   ├── bert-tiny/
│   ├── mobilenet-v3/
│   └── distilbert/
├── medical/            # Medical systems
│   └── alf-detect.html # AlF-DETECT Alzheimer's/Autism
├── frontend/           # Main medical viewer
│   └── index.html      # DICOM viewer
├── backend/            # FastAPI server
│   ├── index.html      # API status
│   ├── api.py
│   └── mcp-*.py        # MCP servers
├── data/               # SQL databases
│   ├── index.html      # Schema viewer
│   ├── tokendb.sql     # Token-dense storage
│   └── architecture-maps.md
├── language/           # SNT/trinary
│   ├── index.html      # Language docs
│   └── trinary/
├── debug/              # Debug tools
│   └── index.html      # Debug console
└── templates/          # ISA templates
    └── views/
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
cd backend && python api.py

# Qdrant Docker
docker run -p 6333:6333 qdrant/qdrant

# MCP Servers
python backend/mcp-codesign.py
python backend/mcp-qdrant.py
python backend/mcp-sqlite.py

# Local server (already running on :8080)
python3 -m http.server 8080

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

## Medical Imaging Modules

- `medical-imaging.md` - Core imaging system
- `medical-xray-analyzer.md` - X-ray AI analysis
- `medical-dicom-viewer.md` - DICOM viewer
- `medical-qdrant.md` - Vector search integration
- `medical-dataset.md` - Medical datasets
- `alf-detect.html` - Alzheimer's/Autism detection

## SNT Language

Space-Time Notation with trinary computing:
- Base-3 arithmetic (0, 1, 2)
- Emoji compression
- Quantum-inspired state management
- See: `language/` directory

## License

MIT - Open source for medical/educational use

## More Info

See `ABOUT.md` for vision, features, acknowledgments.
