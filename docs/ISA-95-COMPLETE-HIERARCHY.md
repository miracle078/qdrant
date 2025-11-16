# ISA-95 Architecture Mapping - Complete Hierarchy

**Document:** Chazon SCADA ISA-95 Complete System Hierarchy
**Date:** 2025-11-15
**Purpose:** Map entire codebase structure to ISA-95 levels L0 through L4

---

## ISA-95 Functional Hierarchy - Chazon Implementation

```
┌─────────────────────────────────────────────────────────────┐
│ Level 4: Business Planning & Logistics                      │
│ Location: / (Root)                                          │
│ Components: GitHub Pages, User Interface, Documentation     │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Level 3: Manufacturing Execution System (MES)               │
│ Location: /os/ (Operating System)                          │
│ Components: Master SCADA, Master HMI, Master PLC            │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Level 2: Supervisory Control (SCADA/HMI)                   │
│ Location: /os/controls/                                    │
│ Components: Area SCADA, Area HMI, Tag Providers            │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Level 1: Control Logic (PLCs)                              │
│ Location: /os/{area}/                                      │
│ Components: PLC Controllers, Control Routines              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Level 0: Physical Process (Sensors/Actuators)              │
│ Location: /os/{area}/tags, modules                         │
│ Components: Tag Definitions, I/O Points, Data Sources      │
└─────────────────────────────────────────────────────────────┘
```

---

## LEVEL 4: Business Planning & Logistics

**Location:** `/` (Repository Root)

### Purpose
Strategic business functions, deployment, user-facing documentation, and regulatory compliance.

### Components

```
/ (Root)
├── index.html           → Main business gateway
├── scada.html           → Business-level SCADA overview
├── plc.html             → Business-level PLC management
├── hmi.html             → Business-level HMI dashboard
├── README.md            → Project documentation
├── ABOUT.md             → Project vision
├── MANIFEST.md          → Complete system manifest
├── CHANGELOG.md         → Release history
├── docs/                → Business documentation
│   ├── guides/          → User guides
│   ├── planning/        → Strategic planning
│   ├── presentation/    → Business presentations
│   └── standards/       → Regulatory standards
└── collab/              → Multi-agent collaboration workspace
```

### Functions
- **Business Planning:** Project roadmap, feature planning
- **Logistics:** Deployment to GitHub Pages, CI/CD
- **Resource Management:** Multi-agent coordination
- **Compliance:** 21 CFR Part 11, EU Annex 11, ISO 13485
- **Documentation:** User guides, API docs, standards
- **Data Export:** Reports, DICOM studies, research datasets

### ISA-95 Activities
- Product definition (medical imaging workflows)
- Production scheduling (batch vs. real-time)
- Quality management (accuracy metrics)
- Inventory tracking (DICOM studies)

---

## LEVEL 3: Manufacturing Execution System (MES)

**Location:** `/os/` (Operating System Directory)

### Purpose
Coordinate and manage all production activities, provide real-time monitoring, and bridge business with control layers.

### Components

```
/os/
├── index.html           → MES gateway/dashboard
├── scada.html           → Master SCADA coordinator
├── plc.html             → Master PLC orchestrator
├── hmi.html             → Master HMI control panel
├── backend/             → API services (L3 coordination)
├── frontend/            → UI services (L3 presentation)
├── modules/             → Execution modules (114+ components)
├── data/                → MES database layer
├── logs/                → System-wide logging
├── boot/                → System initialization
├── templates/           → UI template engine
├── models/              → AI model management
├── medical/             → Medical imaging coordination
└── language/            → SNT/trinary compiler
```

### Functions
- **Production Management:** Coordinate all processing operations
- **Resource Allocation:** Manage CPU, GPU, memory across areas
- **Performance Monitoring:** System metrics, KPIs, dashboards
- **Quality Control:** Validation, compliance checking
- **Data Management:** Token database, architecture maps
- **Work Order Management:** Study queue, batch processing
- **Equipment Tracking:** Model status, resource availability

### Key Subsystems

#### Backend API (`/os/backend/`)
- FastAPI REST services
- Qdrant vector database integration
- Embedding generation coordination
- Request routing to Level 2 controllers

#### Frontend UI (`/os/frontend/`)
- React medical imaging viewer
- Study selection interface
- Patient data presentation
- Viewer controls coordination

#### Module Library (`/os/modules/`)
- 114+ markdown executable modules
- Module registry and dependency management
- Dynamic loading and caching
- PackML state machine coordination

#### Data Layer (`/os/data/`)
- Token database (SQLite)
- Architecture maps
- Configuration management
- SQL schemas

#### Logs (`/os/logs/`)
- Centralized logging (11 categories)
- System, PLC, SCADA, API, errors, audit
- Retention policies and log rotation

### ISA-95 Activities
- **Production Information:** Real-time status, metrics
- **Production Tracking:** Work order execution
- **Production Performance:** Throughput, latency, quality
- **Resource Management:** Equipment, personnel, materials

---

## LEVEL 2: Supervisory Control (SCADA/HMI)

**Location:** `/os/controls/` + Area SCADA/HMI interfaces

### Purpose
Real-time monitoring, supervisory control, alarm management, and operator interfaces for each production area.

### Components

```
/os/controls/
├── index.html           → Controls gateway
├── scada.html           → Area supervisory control
├── hmi.html             → Area operator interface
├── plc.html             → Area PLC coordination
└── tag-providers/       → Tag database per area
    ├── backend.json
    ├── boot.json
    ├── data.json
    ├── frontend.json
    ├── medical.json
    ├── models.json
    ├── modules.json
    └── tag-browser.html

Plus SCADA/HMI in each area:
├── /os/backend/scada.html        → Backend supervisory
├── /os/frontend/scada.html       → Frontend supervisory
├── /os/modules/scada.html        → Module supervisory
├── /os/boot/scada.html           → Boot supervisory
├── /os/models/scada.html         → AI models supervisory
├── /os/data/scada.html           → Data supervisory
├── /os/medical/scada.html        → Medical supervisory
└── /os/language/scada.html       → Language supervisory
```

### Functions
- **Real-Time Monitoring:** Process variables, equipment status
- **Alarm Management:** Critical alerts, warnings, notifications
- **Trend Analysis:** Historical data, performance graphs
- **Operator Interface:** Control actions, setpoint adjustments
- **Data Acquisition:** Tag scanning, value updates
- **Process Visualization:** P&ID diagrams, flow charts
- **Tag Management:** Tag providers for each area

### Tag Provider System
Each area has JSON-based tag definitions:
- **Structure:** Tag name, description, data type, access
- **Categories:** System tags, control tags, status tags
- **Scan Rate:** 100ms typical, configurable per tag
- **Tag Browser:** Central interface at `tag-providers/tag-browser.html`

### Area SCADA Interfaces
Each of 8 main areas has dedicated SCADA:
1. **Backend SCADA** - API monitoring, request tracking
2. **Frontend SCADA** - UI performance, user interactions
3. **Modules SCADA** - Module execution, dependencies
4. **Boot SCADA** - Startup phases, initialization
5. **Models SCADA** - AI inference, model status
6. **Data SCADA** - Database operations, queries
7. **Medical SCADA** - DICOM processing, imaging pipeline
8. **Language SCADA** - Compiler status, trinary execution

---

## LEVEL 1: Control Logic (PLCs)

**Location:** `/os/{area}/plc.html` + Control Modules

### Purpose
Discrete, continuous, and batch control logic for each production area. Execute control strategies, manage I/O, maintain control loops.

### Components

```
PLC Controllers (8 Main Areas):

1. /os/backend/
   ├── plc.html          → Backend PLC controller
   ├── api.py            → Control logic (FastAPI)
   └── requirements.txt  → Dependencies

2. /os/frontend/
   ├── plc.html          → Frontend PLC controller
   ├── src/              → React control logic
   └── public/           → Static control assets

3. /os/modules/
   ├── plc.html          → Module loader PLC
   ├── REGISTRY.md       → Module routing
   └── {module}.md       → 114+ control modules

4. /os/boot/
   ├── plc.html          → Boot sequencer PLC
   ├── index.html        → 6-phase state machine
   └── hmi.html          → Boot control interface

5. /os/models/
   ├── plc.html          → Model manager PLC
   ├── bert-tiny/        → BERT control
   ├── mobilenet-v2/     → MobileNet control
   ├── resnet18/         → ResNet control
   └── squeezenet/       → SqueezeNet control

6. /os/data/
   ├── plc.html          → Database PLC controller
   ├── sql/              → Schema definitions
   └── architecture/     → System maps

7. /os/medical/
   ├── plc.html          → Medical imaging PLC
   └── alf-detect.html   → AlF-DETECT control

8. /os/language/
   ├── plc.html          → Compiler PLC
   ├── trinary/          → Trinary control logic
   └── snt/              → SNT parser control

Plus deeper PLCs:
├── /os/modules/packml/plc.html    → PackML state machine
├── /os/modules/cli/plc.html       → CLI control
├── /os/modules/ai/plc.html        → AI orchestration
├── /os/modules/medical/plc.html   → Medical modules
├── /os/templates/*/plc.html       → Template controllers
└── /os/controls/tag-providers/plc.html  → Tag controller
```

### Functions Per PLC Area

#### Backend PLC (`/os/backend/plc.html`)
- **Scan Time:** 100ms
- **Tags:** 28 control points
- **Routines:**
  - API request processing
  - Qdrant connection management
  - Vector search execution
  - Embedding generation
  - Response formatting

#### Frontend PLC (`/os/frontend/plc.html`)
- **Scan Time:** 50ms
- **Tags:** 47 UI control points
- **Routines:**
  - React component rendering
  - User input handling
  - State management
  - DICOM viewer control
  - Window/level adjustments

#### Modules PLC (`/os/modules/plc.html`)
- **Scan Time:** 75ms
- **Tags:** Dynamic (per module)
- **Routines:**
  - Module loading/unloading
  - Dependency resolution
  - Execution scheduling
  - State machine coordination (PackML)
  - Error handling

#### Boot PLC (`/os/boot/plc.html`)
- **Scan Time:** Phase-dependent
- **Tags:** 18 boot sequence tags
- **Routines:**
  - Phase 0-5 execution
  - Module initialization
  - Dependency validation
  - Health checks
  - Startup coordination

#### Models PLC (`/os/models/plc.html`)
- **Scan Time:** Variable (inference-dependent)
- **Tags:** 12 per model
- **Routines:**
  - Model loading (ONNX)
  - Inference execution
  - Preprocessing
  - Postprocessing
  - Memory management

#### Data PLC (`/os/data/plc.html`)
- **Scan Time:** 100ms
- **Tags:** 15 database tags
- **Routines:**
  - SQLite operations
  - Query execution
  - Token management
  - Schema updates
  - Cache control

#### Medical PLC (`/os/medical/plc.html`)
- **Scan Time:** 200ms (imaging pipeline)
- **Tags:** 25 medical tags
- **Routines:**
  - DICOM parsing
  - Image preprocessing
  - AlF-DETECT execution
  - Result aggregation
  - Report generation

#### Language PLC (`/os/language/plc.html`)
- **Scan Time:** Compile-dependent
- **Tags:** 10 compiler tags
- **Routines:**
  - SNT parsing
  - Trinary compilation
  - Lexical analysis
  - Code generation
  - Optimization

### Control Logic Patterns
All PLCs follow ISA-88 PackML state machine:
```javascript
States: IDLE → STARTING → EXECUTE → COMPLETING → COMPLETE
        ↓        ↓          ↓           ↓           ↓
     ABORTING ← STOPPING ← HOLDING ← SUSPENDING
        ↓        ↓          ↓
     ABORTED  STOPPED    HELD
```

---

## LEVEL 0: Physical Process (Sensors/Actuators/Tags)

**Location:** `/os/controls/tag-providers/*.json` + Module I/O + Data Sources

### Purpose
Physical process interface - sensors, actuators, I/O points, data acquisition, field devices.

### Components

#### Tag Definitions (`/os/controls/tag-providers/`)

**Backend Tags (`backend.json`):**
```json
{
  "tags": [
    {"name": "API_Status", "type": "BOOL", "access": "RO"},
    {"name": "Qdrant_Connected", "type": "BOOL", "access": "RO"},
    {"name": "Request_Count", "type": "INT", "access": "RO"},
    {"name": "Response_Time_ms", "type": "REAL", "access": "RO"},
    {"name": "Active_Connections", "type": "INT", "access": "RO"},
    {"name": "Vector_Search_Active", "type": "BOOL", "access": "RO"},
    {"name": "Embedding_Queue_Size", "type": "INT", "access": "RO"},
    {"name": "Last_Error", "type": "STRING", "access": "RO"}
  ]
}
```

**Frontend Tags (`frontend.json`):**
```json
{
  "tags": [
    {"name": "UI_Loaded", "type": "BOOL", "access": "RO"},
    {"name": "React_State", "type": "STRING", "access": "RO"},
    {"name": "DICOM_Viewer_Active", "type": "BOOL", "access": "RO"},
    {"name": "Window_Width", "type": "INT", "access": "RW"},
    {"name": "Window_Level", "type": "INT", "access": "RW"},
    {"name": "Zoom_Factor", "type": "REAL", "access": "RW"},
    {"name": "Pan_X", "type": "INT", "access": "RW"},
    {"name": "Pan_Y", "type": "INT", "access": "RW"},
    {"name": "Current_Study_UID", "type": "STRING", "access": "RO"}
  ]
}
```

**Models Tags (`models.json`):**
```json
{
  "tags": [
    {"name": "BERT_Loaded", "type": "BOOL", "access": "RO"},
    {"name": "BERT_Inference_Time_ms", "type": "REAL", "access": "RO"},
    {"name": "MobileNet_Loaded", "type": "BOOL", "access": "RO"},
    {"name": "MobileNet_Inference_Time_ms", "type": "REAL", "access": "RO"},
    {"name": "ResNet_Loaded", "type": "BOOL", "access": "RO"},
    {"name": "GPU_Memory_Used_MB", "type": "REAL", "access": "RO"},
    {"name": "Model_Cache_Size_MB", "type": "REAL", "access": "RO"}
  ]
}
```

**Medical Tags (`medical.json`):**
```json
{
  "tags": [
    {"name": "DICOM_File_Loaded", "type": "BOOL", "access": "RO"},
    {"name": "Image_Width", "type": "INT", "access": "RO"},
    {"name": "Image_Height", "type": "INT", "access": "RO"},
    {"name": "Modality", "type": "STRING", "access": "RO"},
    {"name": "Patient_ID", "type": "STRING", "access": "RO"},
    {"name": "AlF_Detect_Running", "type": "BOOL", "access": "RO"},
    {"name": "AlF_Detect_Result", "type": "REAL", "access": "RO"},
    {"name": "Alzheimer_Probability", "type": "REAL", "access": "RO"},
    {"name": "Autism_Probability", "type": "REAL", "access": "RO"}
  ]
}
```

#### Physical Data Sources

**DICOM Files (Sensors):**
- Location: Browser FileAPI, IndexedDB
- Type: Medical imaging raw data
- Interface: DICOM parser modules
- Tags: `DICOM_File_Loaded`, `Image_Width`, `Image_Height`, `Modality`

**AI Models (Actuators/Processors):**
- Location: `/os/models/*/`
- Type: ONNX inference engines
- Interface: ONNX Runtime WebGPU
- Tags: `*_Loaded`, `*_Inference_Time_ms`, `GPU_Memory_Used_MB`

**Vector Database (Storage):**
- Location: Qdrant (external service)
- Type: Semantic search engine
- Interface: REST API (port 6333)
- Tags: `Qdrant_Connected`, `Vector_Search_Active`

**Browser Runtime (Environment):**
- Location: Client browser
- Type: JavaScript execution environment
- Interface: WebGPU, IndexedDB, FileAPI
- Tags: `UI_Loaded`, `React_State`, `GPU_Memory_Used_MB`

**Module Execution (Processes):**
- Location: `/os/modules/*.md`
- Type: JavaScript markdown modules
- Interface: Dynamic module loader
- Tags: Module-specific state tags

#### Field I/O Mapping

```
Physical Layer          →  Tag Provider  →  PLC          →  SCADA
─────────────────────────────────────────────────────────────────
DICOM pixel data        →  medical.json  →  medical/plc  →  medical/scada
User mouse click        →  frontend.json →  frontend/plc →  frontend/scada
API HTTP request        →  backend.json  →  backend/plc  →  backend/scada
ONNX inference result   →  models.json   →  models/plc   →  models/scada
Module state change     →  modules.json  →  modules/plc  →  modules/scada
Database query result   →  data.json     →  data/plc     →  data/scada
Boot phase complete     →  boot.json     →  boot/plc     →  boot/scada
Compiler output         →  language.json →  language/plc →  language/scada
```

---

## Data Flow Through Levels

### Upward Flow (L0 → L4)
**Physical Process → Control → Supervisory → MES → Business**

Example: Medical Image Analysis

```
L0: DICOM file loaded
    ↓ (tag: DICOM_File_Loaded = TRUE)
L1: Medical PLC detects file, triggers preprocessing
    ↓ (routine: preprocessImage())
L2: Medical SCADA updates status, monitors progress
    ↓ (display: "Processing X-Ray...")
L3: MES logs operation, updates work order
    ↓ (database: study_status = "analyzing")
L4: Business dashboard shows throughput metric
    ↓ (report: "Studies/Hour: 45")
```

### Downward Flow (L4 → L0)
**Business → MES → Supervisory → Control → Physical Process**

Example: Start New Analysis

```
L4: User clicks "Analyze" button
    ↓ (business: new work order created)
L3: MES creates work schedule, allocates resources
    ↓ (coordination: assign GPU, queue model)
L2: SCADA sends command to PLC
    ↓ (command: startAnalysis())
L1: PLC executes control logic
    ↓ (routine: loadModel(), runInference())
L0: Physical process executes
    ↓ (action: ONNX model runs on GPU)
```

---

## Navigation Structure Reflecting ISA-95

### Level 4 (Business) Navigation
```
/ (Root)
├── index.html      → Business gateway
├── scada.html      → Business SCADA overview
├── hmi.html        → Business HMI dashboard
└── plc.html        → Business PLC management
    Links down to ↓
    /os/index.html (Level 3 MES)
```

### Level 3 (MES) Navigation
```
/os/ (MES)
├── index.html      → MES gateway/coordinator
├── scada.html      → Master SCADA (coordinates all L2 SCADA)
├── hmi.html        → Master HMI (coordinates all L2 HMI)
└── plc.html        → Master PLC (coordinates all L1 PLCs)
    Links down to ↓
    /os/controls/ (Level 2 Supervisory)
    /os/{area}/scada.html (Level 2 per area)
```

### Level 2 (Supervisory) Navigation
```
/os/controls/ (SCADA/HMI Layer)
├── index.html              → Controls gateway
├── scada.html              → Supervisory control
├── hmi.html                → Operator interface
├── plc.html                → PLC coordination
└── tag-providers/          → Tag database
    ├── tag-browser.html    → View all tags
    └── *.json              → Tag definitions
    Links down to ↓
    /os/{area}/plc.html (Level 1 PLCs)
```

### Level 1 (Control) Navigation
```
/os/{area}/ (PLC Layer)
├── plc.html        → Area PLC controller
├── hmi.html        → Area HMI
└── scada.html      → Area SCADA
    Links down to ↓
    Tag providers (Level 0 tags)
    Module execution (Level 0 processes)
```

### Level 0 (Physical) Access
```
/os/controls/tag-providers/
├── tag-browser.html        → View all physical I/O
├── backend.json            → Backend sensor/actuator tags
├── frontend.json           → Frontend UI tags
├── medical.json            → Medical imaging tags
├── models.json             → AI model tags
├── modules.json            → Module execution tags
├── data.json               → Database tags
└── boot.json               → Boot sequence tags
```

---

## Summary: Complete ISA-95 Hierarchy

| Level | Location | Purpose | Key Files |
|-------|----------|---------|-----------|
| **L4** | `/` (Root) | Business Planning | index.html, docs/, README.md |
| **L3** | `/os/` | MES Coordination | os/index.html, os/scada.html, os/plc.html |
| **L2** | `/os/controls/` + area SCADA | Supervisory Control | controls/scada.html, {area}/scada.html |
| **L1** | `/os/{area}/` | PLC Control Logic | {area}/plc.html, control routines |
| **L0** | `/os/controls/tag-providers/` | Physical I/O | tag-browser.html, *.json tags |

**Total Components:**
- 1 Root gateway (L4)
- 1 MES coordinator (L3)
- 8 Area supervisory systems (L2)
- 8 Main PLCs + 24 sub-PLCs = 32 controllers (L1)
- 11 Tag provider files + modules = physical layer (L0)

**ISA-95 Compliance:** ✅ Complete
**ISA-88 Compliance:** ✅ PackML state machines
**ISA-101 Compliance:** ✅ HMI standardization

---

## See Also

- `/docs/standards/isa/isa-95/README.md` - Original ISA-95 documentation
- `/docs/standards/isa/isa-88/README.md` - PackML state machines
- `/os/controls/tag-providers/tag-browser.html` - View all L0 tags
- `/os/index.html` - MES gateway (L3)
- `/os/controls/index.html` - SCADA gateway (L2)
