# ISA-95: Enterprise-Control System Integration

**Full Name:** ANSI/ISA-95 - Enterprise-Control System Integration
**Scope:** Manufacturing operations management, business-to-control interface
**Application:** SCADA gateway, PLC hierarchy, data flow between UI and processing engines

## Functional Hierarchy Model

```
Level 4: Business Planning & Logistics (ERP)
         ↓
Level 3: Manufacturing Operations Management (MES)
         ↓ ← ← ← Chazon SCADA Gateway is here
Level 2: Supervisory Control (SCADA/HMI)
         ↓
Level 1: Batch/Continuous/Discrete Control (PLC)
         ↓
Level 0: Physical Process (Sensors/Actuators)
```

## Chazon Mapping

### Level 4: Business Planning
- **GitHub Pages** - Deployment platform
- **User requests** - Treatment planning, study management
- **Data export** - Reports, DICOM, research datasets

### Level 3: MES (Manufacturing Execution System)
- **SCADA Gateway** (`scada.html`) - Process monitoring
- **Master HMI** (`hmi.html`) - Operator interface
- **Master PLC** (`plc.html`) - Control logic orchestration
- **Token Database** (`tokendb.sql`) - Production tracking
- **Architecture Maps** - Process flow visualization

### Level 2: Supervisory Control
- **Frontend HMI** - Patient/study selection, viewer controls
- **Backend API** - Qdrant integration, embedding services
- **Debug Console** - System diagnostics, performance monitoring
- **Boot Sequencer** - Startup orchestration

### Level 1: Control
- **8 PLC Areas:**
  - `frontend/` - UI control logic
  - `backend/` - API control logic
  - `modules/` - Component control
  - `boot/` - Initialization control
  - `models/` - AI model management
  - `data/` - Database control
  - `language/` - Compiler/interpreter control
  - `medical/` - Imaging pipeline control

### Level 0: Physical Process
- **DICOM files** - Raw input data
- **AI models** - ONNX inference engines
- **Vector database** - Qdrant storage
- **Browser runtime** - WebGPU, ONNX Runtime, IndexedDB

## Functional Data Flow

### Production Information Flow

**Upward (Level 0 → 4):**
```
Sensors/Data → PLC → SCADA → MES → ERP
   ↓            ↓       ↓      ↓      ↓
DICOM file → Module → HMI → DB → GitHub
```

**Downward (Level 4 → 0):**
```
ERP → MES → SCADA → PLC → Actuators
 ↓     ↓      ↓      ↓        ↓
User → UI → Gateway → Module → Render
```

## Activity Models

### Production
- **Process definition** - Medical imaging workflows
- **Production capability** - Supported modalities (X-Ray, CT, MRI)
- **Production schedule** - Batch vs. real-time processing
- **Production performance** - Throughput, latency metrics

### Product Definition
- **Product** - Analyzed medical image with findings
- **Product segment** - Individual analysis (anatomy, pathology)
- **Product routing** - Preprocessing → Analysis → Reporting

### Maintenance
- **Equipment maintenance** - Model updates, cache clearing
- **Equipment health** - GPU memory, inference speed
- **Maintenance definition** - Update schedules, optimization

### Quality
- **Quality test** - Model accuracy, DICOM compliance
- **Quality results** - Confidence scores, validation metrics
- **Quality analysis** - Performance degradation detection

### Inventory
- **Material** - DICOM studies, embeddings, cached results
- **Material definitions** - Image types, metadata schemas
- **Material tracking** - Study IDs, accession numbers

## Information Exchange Model

### Common Object Models

**Work Master:**
- Recipe for medical analysis workflow
- Equipment requirements (GPU, memory)
- Material requirements (DICOM format)
- Procedure (preprocessing steps)

**Work Performance:**
- Job ID (study instance UID)
- Start/end timestamps
- Resource utilization
- Quality metrics
- Product output (findings, report)

**Work Schedule:**
- Batch processing queue
- Priority levels
- Resource allocation

**Work Capability:**
- Supported modalities
- Available AI models
- Processing capacity

## Chazon Implementation

### SCADA Gateway (Level 3)
```javascript
// scada.html
- 8 PLC area monitoring
- Real-time metrics (CPU, memory, scan time)
- Alarm management
- Process flow visualization
- Production KPIs
```

### HMI Panel (Level 2)
```javascript
// hmi.html
- 12 control buttons (8 PLC areas + 4 special functions)
- Live status indicators
- Emergency stop (E-STOP)
- Navigation to area-specific controls
```

### PLC Controllers (Level 1)
```javascript
// plc.html (master) + area PLCs
- Each directory = PLC area
- Control logic per area
- Tag databases
- Scan times (50-100ms)
- Subroutine management
```

### Physical Processes (Level 0)
```javascript
// modules/*.md
- DICOM parsing
- Pixel processing
- AI inference
- Vector search
- Report generation
```

## Data Categories (ISA-95.03)

### Category 1: Schedule & Actual Production
- Study queue
- Processing status
- Completion times

### Category 2: Product Definition
- Imaging protocols
- Analysis parameters
- Output formats

### Category 3: Production Capability
- Equipment status
- Resource availability
- Model readiness

### Category 4: Production Performance
- Throughput (studies/hour)
- Inference time
- Accuracy metrics
- Resource utilization

## See Also

- `scada.html` - Level 3 MES implementation
- `hmi.html` - Level 2 supervisory control
- `plc.html` - Level 1 control logic
- `standards/isa/isa-88/` - Batch control procedures
- `data/architecture-maps.md` - System integration diagrams
