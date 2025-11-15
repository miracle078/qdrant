# 📂 Project Structure
**Chazon OS + AutomationGPT** | Complete File Tree

```
qdrant/
│
├── 🏠 ROOT LEVEL
│   ├── index.html ......................... Landing page (3 demos)
│   ├── chazon.html ........................ Chazon OS terminal
│   ├── isa-os.html ........................ ISA-OS container runtime
│   ├── automationgpt.html ................. AutomationGPT search
│   ├── README.md .......................... Project overview
│   ├── SITEMAP.md ......................... Navigation guide
│   └── STRUCTURE.md ....................... This file
│
├── 📚 docs/ ............................... Documentation hub
│   ├── index.html ......................... Documentation index
│   ├── PROJECT_STATUS.md .................. Status (93/100)
│   ├── HACKATHON_ANALYSIS.md .............. Competition analysis
│   ├── DEMO_VIDEO_SCRIPT.md ............... 60-second script
│   ├── PITCH_DECK.md ...................... 20 slides
│   ├── BACKEND_SETUP.md ................... Deployment guide
│   └── IMPROVEMENT_PLAN.md ................ Roadmap
│
├── 🌌 chazon/ ............................. Chazon OS (pseudo-OS)
│   ├── index.html ......................... Redirect to chazon.html
│   ├── README.md .......................... OS overview
│   ├── INDEX.md ........................... Complete module list
│   │
│   ├── core/ .............................. OS kernel (12 files)
│   │   ├── index.md ....................... Core modules index
│   │   ├── changelog.md ................... UUID-based changelog
│   │   ├── packml.md ...................... State machines
│   │   ├── sqlite.md ...................... Persistence
│   │   ├── mdcompiler.md .................. Markdown → JS
│   │   ├── os.md .......................... Kernel
│   │   ├── cli.md ......................... Command line
│   │   ├── state.md ....................... State management
│   │   ├── attractors.md .................. Multi-irrational system
│   │   ├── equilibrium.md ................. Dynamic equilibrium
│   │   ├── attractor-theory.md ............ Math foundation
│   │   └── [mcp.md, api.md, wrapper.md, sync.md, integration.md]
│   │
│   ├── agents/ ............................ CI/CD automation (3 files)
│   │   ├── index.md ....................... Agents index
│   │   ├── ci.md .......................... Continuous integration
│   │   ├── test.md ........................ Automated testing
│   │   └── deploy.md ...................... Deployment agent
│   │
│   ├── ui/ ................................ Desktop environment (6 files)
│   │   ├── index.md ....................... UI modules index
│   │   ├── desktop.md ..................... Desktop manager
│   │   ├── windows.md ..................... Window system
│   │   ├── icons.md ....................... Icon system
│   │   ├── taskbar.md ..................... Taskbar
│   │   └── theme.md ....................... Theming
│   │
│   ├── isa/ ............................... ISA standards (2 files)
│   │   ├── index.md ....................... Standards index
│   │   ├── standards.md ................... ISA-95/88/18.2
│   │   └── compliance.md .................. Regulatory mapping
│   │
│   ├── medical/ ........................... Medical imaging (7 files)
│   │   ├── index.md ....................... Medical modules index
│   │   ├── qdrant.md ...................... Mock Qdrant
│   │   ├── qdrant-client.md ............... Real backend client
│   │   ├── embeddings.md .................. Vector generation
│   │   ├── xray-analyzer.md ............... X-ray analysis
│   │   ├── dataset.md ..................... Sample data
│   │   └── dicom-viewer.md ................ DICOM viewer
│   │
│   ├── programs/ .......................... Executable programs (13 files)
│   │   ├── index.md ....................... Programs index
│   │   ├── hello.md ....................... Hello world
│   │   ├── calculator.md .................. Calculator
│   │   ├── neural.md ...................... Neural network
│   │   ├── medical-demo.md ................ Medical imaging demo
│   │   ├── xray-3d.md ..................... 3D x-ray viewer
│   │   ├── cicd.md ........................ CI/CD pipeline
│   │   ├── test-sync.md ................... Sync testing
│   │   ├── attractor-demo.md .............. Attractor visualization
│   │   ├── qdrant-real-demo.md ............ Real Qdrant demo
│   │   ├── isa-os-demo.md ................. ISA-OS demo
│   │   └── [data.md, search.md, events.md]
│   │
│   └── tests/ ............................. Test suite
│       └── index.md ....................... Tests index
│
├── ⚙️ backend/ ............................ FastAPI + Qdrant (11 files)
│   ├── index.html ......................... Backend docs
│   ├── README.md .......................... API documentation
│   ├── api.py ............................. FastAPI service
│   ├── requirements.txt ................... Python deps
│   ├── .env.example ....................... Config template
│   ├── docker-compose.yml ................. Local dev
│   ├── Dockerfile ......................... Container image
│   ├── Procfile ........................... Railway config
│   ├── railway.json ....................... Build settings
│   ├── railway-deploy.sh .................. Deploy script
│   └── fly.toml ........................... Fly.io config
│
└── 🐍 automationgpt/ ...................... Python package
    ├── api/ ............................... API endpoints
    ├── embeddings/ ........................ Embedding generation
    ├── ingest/ ............................ Data ingestion
    ├── regulatory/ ........................ Compliance mapping
    ├── tests/ ............................. Test suite
    └── utils/ ............................. Utilities
```

## 📊 Statistics

**Total Files:** 65+
**Markdown Programs:** 52 (all < 250 tokens)
**Documentation:** 3,000+ lines
**Code:** 5,000+ lines (Python + JavaScript)

**Index Files:**
- ✅ Root: `index.html` (landing page)
- ✅ docs/: `index.html` (docs hub)
- ✅ chazon/: `index.html` (redirect)
- ✅ backend/: `index.html` (API docs)
- ✅ All chazon/ subdirs: `index.md`

## 🗺️ Navigation Flow

```
GitHub Pages Root (/)
│
├─→ index.html ................ Landing Page
│   ├─→ chazon.html ........... Chazon OS Demo
│   ├─→ isa-os.html ........... ISA-OS Demo
│   ├─→ automationgpt.html .... AutomationGPT Demo
│   └─→ docs/ ................. Documentation Hub
│
├─→ docs/index.html ........... Docs Hub
│   ├─→ PROJECT_STATUS.md ..... Current Status
│   ├─→ HACKATHON_ANALYSIS.md . Competition Analysis
│   ├─→ DEMO_VIDEO_SCRIPT.md .. Video Script
│   ├─→ PITCH_DECK.md ......... Pitch Slides
│   └─→ BACKEND_SETUP.md ...... Deploy Guide
│
├─→ chazon/index.html ......... → Redirects to /chazon.html
│   └─→ All subdirs/index.md .. Module Indexes
│
└─→ backend/index.html ........ Backend Docs
    └─→ README.md ............. Full API Docs
```

## 🎯 Quick Access

**For Judges:**
- Start: [`index.html`](index.html)
- Status: [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md)
- Pitch: [`docs/PITCH_DECK.md`](docs/PITCH_DECK.md)

**For Developers:**
- Setup: [`README.md`](README.md)
- Deploy: [`docs/BACKEND_SETUP.md`](docs/BACKEND_SETUP.md)
- Structure: This file

**For Users:**
- Try Chazon: [`chazon.html`](chazon.html)
- Try ISA-OS: [`isa-os.html`](isa-os.html)
- All Docs: [`docs/index.html`](docs/index.html)

---

**Built with ❤️ for lablab.ai Qdrant Challenge**

φ = 1.618 | ISA-95 Compliant | MIT License
