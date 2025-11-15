# Dependency Graph
**Module Dependencies** | Complete Dependency Tree

Complete dependency graph for all Chazon modules.

## Core Dependencies
```mermaid
graph TD
    MDCompiler[chazon-mdcompiler]
    OS[chazon-os]
    Attractors[chazon-attractors]
    Equilibrium[chazon-equilibrium]
    PackML[chazon-packml]
    Changelog[chazon-changelog]
    SQLite[chazon-sqlite]

    MDCompiler --> OS
    OS --> PackML
    Attractors --> PackML
    Equilibrium --> Attractors
```

## CLI Dependencies
```mermaid
graph TD
    CLI[chazon-cli]
    Core[cli-core]
    Edit[cli-edit]
    Test[cli-test]
    Logs[cli-logs]
    Git[cli-git]
    DB[cli-db]
    State[chazon-state]
    MCP[chazon-mcp]
    API[chazon-api]

    Core --> CLI
    Edit --> CLI
    Test --> CLI
    Logs --> CLI
    Git --> CLI
    DB --> CLI
    State --> CLI
    MCP --> CLI
    API --> CLI
```

## Medical Dependencies
```mermaid
graph TD
    Imaging[medical-imaging]
    DICOM[medical-dicom-viewer]
    XRay[medical-xray-analyzer]
    Qdrant[medical-qdrant]
    Client[qdrant-client]
    Embed[embed-openai]
    Dataset[medical-dataset]

    DICOM --> Imaging
    XRay --> Imaging
    Qdrant --> Client
    Client --> Embed
    Qdrant --> Dataset
```

## Language Dependencies
```mermaid
graph TD
    Trinary[trinary-core]
    SpaceTime[spacetime-compiler]
    Parser[snt-parser]
    Syntax[snt-syntax]
    Photonic[photonic-layer]
    Emoji[emoji-compression]

    SpaceTime --> Trinary
    Parser --> SpaceTime
    Syntax --> Parser
    Photonic --> Trinary
    Emoji --> Trinary
```

## Boot Dependencies
```mermaid
graph TD
    Sequencer[boot-sequencer]
    P0[boot-phase0-core]
    P1[boot-phase1-cli]
    P2[boot-phase2-ui]
    P3[boot-phase3-medical]
    P4[boot-phase4-language]
    P5[boot-phase5-programs]

    Sequencer --> P0
    Sequencer --> P1
    Sequencer --> P2
    Sequencer --> P3
    Sequencer --> P4
    Sequencer --> P5

    P1 --> P0
    P2 --> P1
    P3 --> P2
    P4 --> P3
    P5 --> P4
```

## Cross-Layer Dependencies
```mermaid
graph TD
    subgraph Layer0[Layer 0: Core]
        MDC[MDCompiler]
        OS[ChazonOS]
    end

    subgraph Layer1[Layer 1: CLI]
        CLI[ChazonCLI]
    end

    subgraph Layer2[Layer 2: UI]
        Desktop[ui-desktop]
    end

    subgraph Layer3[Layer 3: Medical]
        Medical[medical-imaging]
    end

    subgraph Layer4[Layer 4: Language]
        SNT[snt-parser]
    end

    MDC --> CLI
    MDC --> Desktop
    MDC --> Medical
    MDC --> SNT

    OS --> CLI
    CLI --> Desktop
```

## Token Database Dependencies
```mermaid
graph TD
    TokenDB[db-token]
    Analyzer[token-analyzer]
    MCP_DB[mcp-database]
    API_DB[api-database]
    CLI_DB[cli-db]

    Analyzer --> TokenDB
    MCP_DB --> TokenDB
    MCP_DB --> Analyzer
    API_DB --> TokenDB
    CLI_DB --> TokenDB
    CLI_DB --> Analyzer
```

## Execution Flow
```
1. Boot Sequencer Loads
   ├── Phase 0: Core (MDCompiler, OS)
   ├── Phase 1: CLI (ChazonCLI + command modules)
   ├── Phase 2: UI (Desktop, Agents)
   ├── Phase 3: Medical (DICOM, Qdrant)
   ├── Phase 4: Language (SNT, Trinary)
   └── Phase 5: Programs (User programs)

2. User Interaction
   ├── Terminal Input
   ├── ChazonCLI.exec()
   ├── Command Router
   └── Module Execution

3. Data Flow
   ├── Input → Parser → Processor → Output
   └── Database ← API/MCP → Frontend
```

## Critical Paths

### Boot Critical Path
```
MDCompiler → ChazonOS → ChazonCLI → Terminal → Ready
```

### Medical Imaging Path
```
Upload → DICOM Parser → Window/Level → AI Analysis → Qdrant Search → Results
```

### Language Execution Path
```
SNT Code → Parser → SpaceTime Compiler → Trinary Core → Execution
```

### Database Query Path
```
CLI/API → TokenDB → SQL Query → Results → Display
```
