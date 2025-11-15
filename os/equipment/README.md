# Equipment Hierarchy - ISA-88 Complete Architecture

**Standard:** ISA-88 (Batch Control Equipment Hierarchy)
**Application:** Chazon Medical Imaging SCADA System
**Purpose:** Complete equipment and control module definitions from Enterprise down to Control Modules

---

## Overview

This directory contains the complete ISA-88 equipment hierarchy for the Chazon system, organized as follows:

```
ISA-88 Equipment Hierarchy:

Enterprise                    (Business/Strategic Level)
└── Site                      (Production Facility)
    └── Area                  (Production Area)
        └── Process Cell      (Group of Units for specific process)
            └── Unit          (Major processing equipment)
                └── Equipment Module    (Reusable component)
                    └── Control Module  (Elementary control function)
```

---

## Directory Structure

```
/os/equipment/
├── README.md                           → This file
├── enterprise/                         → Enterprise level (1)
│   └── chazon-enterprise.md
├── site/                               → Site level (1)
│   └── production-site.md
├── areas/                              → Area level (8 areas)
│   ├── backend-area.md
│   ├── frontend-area.md
│   ├── medical-area.md
│   ├── models-area.md
│   ├── data-area.md
│   ├── modules-area.md
│   ├── boot-area.md
│   └── language-area.md
├── process-cells/                      → Process Cell level (24+ cells)
│   ├── dicom-processing-cell.md
│   ├── alf-detect-cell.md
│   ├── api-gateway-cell.md
│   └── ... (more cells)
├── units/                              → Unit level (72+ units)
│   ├── dicom-parser-unit.md
│   ├── metadata-extractor-unit.md
│   ├── quality-validator-unit.md
│   └── ... (more units)
├── equipment-modules/                  → Equipment Module level (200+ modules)
│   ├── file-validator-module.md
│   ├── tag-reader-module.md
│   ├── pixel-decoder-module.md
│   └── ... (more modules)
└── control-modules/                    → Control Module level (500+ functions)
    ├── data-element-reader.md
    ├── preamble-parser.md
    ├── tag-dictionary-builder.md
    └── ... (more control modules)
```

---

## ISA-88 Hierarchy Explained

### Level 1: Enterprise

**Count:** 1 enterprise
**Location:** `enterprise/chazon-enterprise.md`
**ISA-95 Level:** L4 (Business Planning & Logistics)

**Purpose:**
- Strategic business planning
- Regulatory compliance
- Enterprise-wide KPIs
- Resource management across all sites

**Example:** Chazon Medical Imaging SCADA Enterprise

---

### Level 2: Site

**Count:** 1 production site
**Location:** `site/production-site.md`
**ISA-95 Level:** L4/L3 Bridge

**Purpose:**
- Physical/virtual location of manufacturing
- Site-wide resource coordination
- Production scheduling
- Quality management

**Example:** Chazon GitHub Pages Production Site

---

### Level 3: Area

**Count:** 8 areas
**Location:** `areas/*.md`
**ISA-95 Level:** L3 (MES) / L2 (Supervisory)

**Purpose:**
- Functional grouping of process cells
- Area-level control (PLC, SCADA, HMI)
- Tag provider coordination
- Area-specific KPIs

**Areas:**
1. **Backend Area** - API services, Qdrant integration
2. **Frontend Area** - UI rendering, DICOM viewer
3. **Medical Area** - DICOM processing, AlF-DETECT
4. **Models Area** - AI inference, ONNX runtime
5. **Data Area** - Database operations, SQLite
6. **Modules Area** - Module loading, 114+ components
7. **Boot Area** - System initialization, 6 phases
8. **Language Area** - SNT/trinary compiler

---

### Level 4: Process Cell

**Count:** 24+ process cells (3 per area typical)
**Location:** `process-cells/*.md`
**ISA-95 Level:** L2/L1 (Supervisory/Control)

**Purpose:**
- Group related units for a specific process
- Coordinate multi-unit operations
- Cell-level control logic
- Process sequencing

**Example Process Cells:**
- **DICOM Processing Cell** (Medical Area)
  - Units: Parser, Metadata Extractor, Quality Validator
- **AlF-DETECT Cell** (Medical Area)
  - Units: Alzheimer Detector, Autism Detector, Aggregator
- **API Gateway Cell** (Backend Area)
  - Units: Health Check, Search, Index

**Cell Responsibilities:**
- Coordinate unit execution
- Manage cell-level state machine
- Handle inter-unit data flow
- Monitor cell performance

---

### Level 5: Unit

**Count:** 72+ units (3 per process cell typical)
**Location:** `units/*.md`
**ISA-95 Level:** L1 (Control Logic)

**Purpose:**
- Major processing equipment
- Unit-level control logic
- PackML state machine
- Equipment module coordination

**Example Units:**
- **DICOM Parser Unit** (DICOM Processing Cell)
  - Modules: File Validator, Tag Reader, Pixel Decoder
- **Metadata Extractor Unit** (DICOM Processing Cell)
  - Modules: Patient Info, Study Info, Series Info
- **Alzheimer Detection Unit** (AlF-DETECT Cell)
  - Modules: Feature Extractor, Classifier, Thresholder

**Unit Responsibilities:**
- Execute PackML state machine (IDLE → EXECUTE → COMPLETE)
- Coordinate equipment modules
- Manage unit-level tags
- Report unit status to cell

---

### Level 6: Equipment Module

**Count:** 200+ equipment modules
**Location:** `equipment-modules/*.md`
**ISA-95 Level:** L1 (Control Logic)

**Purpose:**
- Reusable functional components
- Modular equipment building blocks
- Encapsulated functionality
- Portable across units

**Example Equipment Modules:**
- **File Validator Module** (DICOM Parser Unit)
  - Controls: Magic Number Checker, Structure Validator, Encoding Validator
- **Tag Reader Module** (DICOM Parser Unit)
  - Controls: Preamble Parser, Data Element Reader, Dictionary Builder
- **Pixel Decoder Module** (DICOM Parser Unit)
  - Controls: Transfer Syntax Detector, Decompressor, Array Converter

**Module Characteristics:**
- **Reusable:** Can be used in multiple units
- **Modular:** Clear input/output interface
- **Testable:** Isolated functionality
- **Configurable:** Parameterized behavior

---

### Level 7: Control Module

**Count:** 500+ control modules
**Location:** `control-modules/*.md`
**ISA-95 Level:** L0/L1 (Physical I/O / Control Logic)

**Purpose:**
- Elementary control functions
- Low-level operations
- Direct I/O interaction
- Primitive operations

**Example Control Modules:**
- **Data Element Reader** (Tag Reader Module)
  - Functions: readUint8(), readUint16(), readUint32(), readString(), readBinary()
- **Preamble Parser** (Tag Reader Module)
  - Functions: readPreamble(), verifyMagicNumber(), parseMetaInfo()
- **Magic Number Checker** (File Validator Module)
  - Functions: checkDICM(), validateOffset(), verifyFormat()

**Control Characteristics:**
- **Atomic:** Single, indivisible operation
- **Pure:** No side effects (typically)
- **Fast:** <1ms execution (typically)
- **Testable:** Easy to unit test

---

## Mapping to ISA-95 Levels

### ISA-88 to ISA-95 Mapping

| ISA-88 Level | ISA-95 Level | Chazon Location | Examples |
|--------------|--------------|-----------------|----------|
| **Enterprise** | L4 (Business) | `/` (root) | Business planning, documentation |
| **Site** | L4/L3 (MES) | `/os/` | Production site, MES coordination |
| **Area** | L3/L2 (MES/SCADA) | `/os/{area}/` | 8 areas with PLC/SCADA/HMI |
| **Process Cell** | L2/L1 (SCADA/PLC) | Process cells | DICOM Processing, AlF-DETECT |
| **Unit** | L1 (PLC) | Units | DICOM Parser, Metadata Extractor |
| **Equipment Module** | L1 (PLC) | Modules | File Validator, Tag Reader |
| **Control Module** | L0/L1 (Tags/PLC) | Functions | readUint16(), parseTag() |

---

## Data Flow Through Hierarchy

### Example: DICOM Image Processing

```
L1: Enterprise
    └─> Strategic Goal: Analyze 1000 studies/day
        └─> KPI: Diagnostic accuracy > 95%

L2: Site
    └─> Production Plan: Schedule 24/7 processing
        └─> Resource Allocation: GPU, memory, network

L3: Area (Medical Area)
    └─> Area Control: DICOM processing pipeline
        └─> Tags: DICOM_File_Loaded, Image_Width, Image_Height

L4: Process Cell (DICOM Processing Cell)
    └─> Cell Coordination: Parse → Extract → Validate
        └─> State: IDLE → EXECUTE → COMPLETE

L5: Unit (DICOM Parser Unit)
    └─> Unit Operation: Parse DICOM file structure
        └─> PackML State: STARTING → EXECUTE → COMPLETING

L6: Equipment Module (Tag Reader Module)
    └─> Module Function: Read and parse DICOM tags
        └─> Operations: readTag(), buildDictionary()

L7: Control Module (Data Element Reader)
    └─> Control Function: Read binary data from byte stream
        └─> Functions: readUint16(), readString(), readBinary()
```

---

## How to Use This Documentation

### For System Architects
Start at Enterprise level, work down:
1. `enterprise/chazon-enterprise.md` - Understand overall system
2. `site/production-site.md` - Understand site organization
3. `areas/*.md` - Understand each functional area
4. Review hierarchy mapping to ISA-95 levels

### For Control Engineers
Start at Area level, work down:
1. `areas/{area}-area.md` - Understand area scope
2. `process-cells/*.md` - Understand process organization
3. `units/*.md` - Understand unit control logic
4. `equipment-modules/*.md` - Understand reusable components

### For Software Developers
Start at Unit/Module level:
1. `units/*.md` - Understand unit interfaces
2. `equipment-modules/*.md` - Understand module APIs
3. `control-modules/*.md` - Understand function signatures
4. Implement based on specifications

### For Operators
Focus on Area and Process Cell levels:
1. `areas/*.md` - Understand area operations
2. `process-cells/*.md` - Understand process workflows
3. Review HMI/SCADA interfaces
4. Follow standard operating procedures

---

## Document Templates

Each level follows a standard template:

### Enterprise Template
- Overview
- Hierarchy
- Functions
- Standards
- Metrics
- Organization
- Data Model
- Integration
- Deployment

### Site Template
- Overview
- Hierarchy
- Areas
- Resources
- Operations
- Infrastructure
- Safety & Security
- Metrics
- Personnel
- Integration

### Area Template
- Overview
- Hierarchy
- Process Cells
- Equipment
- Tags (Level 0)
- Operations
- Metrics
- Related Docs

### Process Cell Template
- Overview
- Hierarchy
- Units
- Operations (Procedures)
- Tags
- Performance
- Control Strategy
- Alarms & Events

### Unit Template
- Overview
- Hierarchy
- Equipment Modules
- Operations (Phases)
- Tags
- Control Logic (PackML)
- Performance
- Error Handling

### Equipment Module Template
- Overview
- Hierarchy
- Control Modules
- Operations
- Interface
- Configuration
- Performance
- Error Handling

### Control Module Template
- Overview
- Functions
- Specifications
- Interface (Inputs/Outputs)
- Algorithm
- Performance
- Error Handling
- Testing

---

## Standards Compliance

### ISA-88 Compliance
- ✅ 7-level equipment hierarchy
- ✅ Procedural model (Procedure → Unit Procedure → Operation → Phase)
- ✅ PackML state machines (IDLE → EXECUTE → COMPLETE)
- ✅ Recipe model (Master → Control recipes)
- ✅ Batch control concepts

### ISA-95 Compliance
- ✅ 5-level functional hierarchy (L4 → L0)
- ✅ MES coordination (Level 3)
- ✅ Activity models (Production, Quality, Maintenance)
- ✅ Information exchange models
- ✅ Data categories

### ISA-101 Compliance
- ✅ HMI standardization
- ✅ Operator interfaces per area
- ✅ Consistent visual design
- ✅ Alarm management

---

## Creating New Equipment Definitions

### Steps to Add New Equipment

1. **Identify Level** - Determine ISA-88 level (Area, Cell, Unit, Module)
2. **Create Document** - Use appropriate template
3. **Define Hierarchy** - Show parent and children
4. **Specify Interface** - Document inputs/outputs/tags
5. **Document Operations** - Procedures, phases, control logic
6. **Add Performance Specs** - Timing, throughput, quality
7. **Link to Related Docs** - Cross-reference parent/children

### Naming Convention

```
{name}-{level}.md

Examples:
- chazon-enterprise.md
- production-site.md
- backend-area.md
- dicom-processing-cell.md
- dicom-parser-unit.md
- tag-reader-module.md
- data-element-reader.md (control module)
```

---

## Related Documentation

### Standards
- `/docs/standards/isa/isa-88/README.md` - ISA-88 batch control
- `/docs/standards/isa/isa-95/README.md` - ISA-95 enterprise integration
- `/docs/standards/isa/isa-101/README.md` - ISA-101 HMI design

### System Architecture
- `/docs/ISA-95-COMPLETE-HIERARCHY.md` - Complete hierarchy mapping
- `/os/controls/tag-providers/` - Tag definitions (Level 0)
- `/os/{area}/plc.html` - PLC controllers (Level 1)
- `/os/{area}/scada.html` - SCADA interfaces (Level 2)
- `/os/index.html` - MES gateway (Level 3)

---

## Statistics

### Current Documentation Coverage

| Level | Count | Documented | Coverage |
|-------|-------|------------|----------|
| Enterprise | 1 | 1 | 100% |
| Site | 1 | 1 | 100% |
| Area | 8 | 2 (examples) | 25% |
| Process Cell | ~24 | 1 (example) | 4% |
| Unit | ~72 | 1 (example) | 1% |
| Equipment Module | ~200 | 1 (example) | <1% |
| Control Module | ~500 | 1 (example) | <1% |

**Note:** Example documents provided as templates. Additional documentation can be created following the same patterns.

---

## Roadmap

### Phase 1: Core Documentation (Current)
- ✅ Enterprise definition
- ✅ Site definition
- ✅ Area examples (Backend, Medical)
- ✅ Process Cell example (DICOM Processing)
- ✅ Unit example (DICOM Parser)
- ✅ Equipment Module example (Tag Reader)
- ✅ Control Module example (Data Element Reader)

### Phase 2: Complete Medical Area
- ⬜ All Medical Area process cells
- ⬜ All Medical Area units
- ⬜ Medical equipment modules
- ⬜ Medical control modules

### Phase 3: All Areas
- ⬜ Complete all 8 areas
- ⬜ All process cells per area
- ⬜ All units per cell
- ⬜ Common equipment modules
- ⬜ Common control modules

### Phase 4: Validation & Testing
- ⬜ Validate hierarchy completeness
- ⬜ Test cross-references
- ⬜ Verify ISA-88/95 compliance
- ⬜ Generate documentation metrics

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Maintained By:** Chazon Architecture Team
**Status:** Active - Templates Complete
