# Chazon Architecture Map
**System Architecture** | Module Dependencies & Flow

Complete architecture map of Chazon system.

## Layer 0: Core (7 modules)
```
chazon-mdcompiler ──┬──> All modules
chazon-os          ─┤
chazon-attractors  ─┤
chazon-equilibrium ─┤
chazon-packml      ─┤
chazon-changelog   ─┤
chazon-sqlite      ─┘
```

## Layer 1: CLI System (12 modules)
```
cli-core ──┬──> chazon-cli ──> Terminal
cli-edit  ─┤
cli-test  ─┤
cli-logs  ─┤
cli-git   ─┘

chazon-state ──┬──> chazon-cli
chazon-mcp    ─┤
chazon-api    ─┤
chazon-wrapper─┤
chazon-sync   ─┤
chazon-integration──┘
```

## Layer 2: UI & Agents (11 modules)
```
agent-ci ──┬──> chazon-packml
agent-test─┤
agent-deploy──┘

ui-desktop ──┬──> ui-index
ui-windows  ─┤
ui-icons    ─┤
ui-taskbar  ─┤
ui-theme    ─┘

isa-standards ──> isa-compliance
```

## Layer 3: Medical Imaging (7 modules)
```
medical-imaging ──┬──> medical-dicom-viewer
                  └──> medical-xray-analyzer

medical-qdrant ──┬──> qdrant-client ──> embed-openai
                 └──> medical-dataset
```

## Layer 4: Language System (6 modules)
```
trinary-core ──┬──> spacetime-compiler ──> snt-parser
               │
               └──> snt-syntax
                    snt-photonic-layer
                    emoji-compression
```

## Boot Flow
```
Phase 0 (Core)
    │
    ├──> Load MDCompiler
    ├──> Load ChazonOS
    └──> Load Core Infrastructure
         │
Phase 1 (CLI)
    │
    ├──> Load CLI Modules
    ├──> Initialize Command Registry
    └──> Setup Terminal
         │
Phase 2 (UI)
    │
    ├──> Load Agents
    ├──> Load UI Components
    └──> Initialize Desktop
         │
Phase 3 (Medical)
    │
    ├──> Load Medical Imaging
    ├──> Load Qdrant Client
    └──> Initialize DICOM Viewer
         │
Phase 4 (Language)
    │
    ├──> Load Trinary Core
    ├──> Load SNT Parser
    └──> Initialize Language System
         │
Phase 5 (Programs)
    │
    ├──> Load User Programs
    └──> Ready for Execution
         │
    BOOT COMPLETE
```

## Dependency Graph
```
┌─────────────────────────────────────────────┐
│              MDCompiler (Core)              │
│         Compiles all .md modules            │
└──────────────────┬──────────────────────────┘
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
  ┌────────┐  ┌────────┐  ┌────────┐
  │  CLI   │  │   UI   │  │Medical │
  │ Layer  │  │ Layer  │  │ Layer  │
  └────────┘  └────────┘  └────────┘
       │           │           │
       └───────────┼───────────┘
                   │
                   ▼
            ┌────────────┐
            │  Language  │
            │   Layer    │
            └────────────┘
                   │
                   ▼
            ┌────────────┐
            │  Programs  │
            └────────────┘
```

## Token Distribution
```
Category          Modules  Avg Tokens  Total Tokens
-------------------------------------------------
Core                   7         180         1,260
CLI                   12         200         2,400
UI                    11         190         2,090
Medical                7         220         1,540
Language               6         210         1,260
Programs              16         180         2,880
Boot                   6         150           900
-------------------------------------------------
TOTAL                 65                    12,330
```

## Data Flow
```
User Input
    │
    ▼
Terminal/CLI ──> ChazonCLI.exec()
    │
    ├──> Command Parser
    │       │
    │       ├──> File Operations (CLI-Edit)
    │       ├──> Testing (CLI-Test)
    │       ├──> Logging (CLI-Logs)
    │       └──> Git (CLI-Git)
    │
    ├──> Module Execution
    │       │
    │       └──> MDCompiler.compile() ──> eval()
    │
    └──> Output ──> Terminal.print()
```

## Medical Imaging Flow
```
Medical Image Upload
    │
    ▼
DICOM Parser (medical-dicom-viewer)
    │
    ├──> Window/Level Processing (medical-imaging)
    │       │
    │       └──> Apply Presets (bone, lung, brain)
    │
    ├──> AI Analysis (medical-xray-analyzer)
    │       │
    │       └──> Abnormality Detection
    │
    └──> Vector Search (medical-qdrant)
            │
            ├──> Generate Embeddings (embed-openai)
            │
            └──> Query Qdrant ──> Similar Cases
```

## API/MCP Wrapper Flow
```
Frontend Request
    │
    ▼
chazon-wrapper
    │
    ├──> chazon-api ──> FastAPI Backend
    │                       │
    │                       └──> Qdrant Client
    │
    └──> chazon-mcp ──> MCP Server
                            │
                            └──> Tool Execution
```
