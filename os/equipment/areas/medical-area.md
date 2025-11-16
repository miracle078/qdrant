# Medical Area

**ISA-88 Level:** Area
**Parent:** Production Site
**ISA-95 Level:** L3 (MES) / L2 (Supervisory)
**Location:** `/os/medical/`

---

## Area Overview

**Name:** Medical Imaging Processing Area
**Purpose:** DICOM image processing, AlF-DETECT analysis, medical imaging pipeline coordination
**Scope:** All medical imaging analysis operations

### Area Description

The Medical Area is responsible for medical image processing, including:
- DICOM file parsing and validation
- AlF-DETECT (Alzheimer's & Autism detection)
- Medical imaging pipelines (X-Ray, CT, MRI)
- Clinical protocol execution
- Diagnostic finding generation

---

## Area Hierarchy

```
Medical Area (/os/medical/)
├── DICOM Processing Cell
│   ├── Parser Unit
│   ├── Validator Unit
│   └── Metadata Extractor Unit
├── AlF-DETECT Process Cell
│   ├── Alzheimer Detection Unit
│   ├── Autism Detection Unit
│   └── Result Aggregation Unit
└── Imaging Pipeline Process Cell
    ├── X-Ray Pipeline Unit
    ├── CT Pipeline Unit
    └── MRI Pipeline Unit
```

---

## Process Cells

### 1. DICOM Processing Cell
**Purpose:** Parse and validate DICOM medical images
**Location:** `/os/modules/medical/medical-dicom-viewer.md`
**Equipment:**
- DICOM parser
- Tag reader
- Pixel data decoder
- Metadata validator

### 2. AlF-DETECT Process Cell
**Purpose:** AI-powered Alzheimer's and Autism detection
**Location:** `/os/medical/alf-detect.html`
**Equipment:**
- Pre-trained neural networks
- Feature extraction modules
- Classification engines
- Confidence scoring system

### 3. Imaging Pipeline Process Cell
**Purpose:** Modality-specific image processing
**Equipment:**
- Window/level adjustment
- Image enhancement (CLAHE)
- Normalization filters
- Segmentation tools

---

## Area Equipment

### Controllers
- **Area PLC:** `/os/medical/plc.html` (200ms scan time, 25 tags)
- **Area SCADA:** `/os/medical/scada.html` (supervisory control)
- **Area HMI:** `/os/medical/hmi.html` (operator interface)

### Applications
- **AlF-DETECT:** `/os/medical/alf-detect.html`
- **DICOM Viewer:** Module-based viewer
- **Analysis Dashboard:** Real-time results display

### Configuration
- **Config:** `/os/medical/config.yaml`
- **Protocols:** Clinical imaging protocols
- **Presets:** Window/level presets per modality

### Tag Provider
- **Tags File:** `/os/controls/tag-providers/medical.json`
- **Tag Count:** 25 tags
- **Categories:** DICOM, detection, quality, performance tags

---

## Area Tags (Level 0)

### DICOM Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `DICOM_File_Loaded` | BOOL | RO | DICOM file successfully loaded |
| `Image_Width` | INT | RO | Image width in pixels |
| `Image_Height` | INT | RO | Image height in pixels |
| `Modality` | STRING | RO | Imaging modality (CR, CT, MR, etc.) |
| `Patient_ID` | STRING | RO | Patient identifier (anonymized) |
| `Study_Instance_UID` | STRING | RO | DICOM study instance UID |
| `Series_Instance_UID` | STRING | RO | DICOM series instance UID |
| `SOPInstance_UID` | STRING | RO | SOP instance UID |

### AlF-DETECT Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `AlF_Detect_Running` | BOOL | RO | Detection analysis in progress |
| `AlF_Detect_Complete` | BOOL | RO | Analysis completed |
| `AlF_Detect_Result` | STRING | RO | Overall result (positive/negative) |
| `Alzheimer_Probability` | REAL | RO | Alzheimer's probability (0.0-1.0) |
| `Alzheimer_Confidence` | REAL | RO | Confidence score for Alzheimer's |
| `Autism_Probability` | REAL | RO | Autism probability (0.0-1.0) |
| `Autism_Confidence` | REAL | RO | Confidence score for Autism |

### Image Processing Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Window_Width` | INT | RW | DICOM window width |
| `Window_Level` | INT | RW | DICOM window level (center) |
| `Enhancement_Applied` | BOOL | RO | Image enhancement active |
| `Normalization_Applied` | BOOL | RO | Intensity normalization applied |
| `Segmentation_Active` | BOOL | RO | Segmentation in progress |

### Quality Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Image_Quality_Score` | REAL | RO | Image quality (0.0-1.0) |
| `DICOM_Compliance` | BOOL | RO | Passes DICOM validation |
| `Metadata_Complete` | BOOL | RO | All required metadata present |

### Performance Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Processing_Time_ms` | REAL | RO | Total processing time |
| `Detection_Time_ms` | REAL | RO | AlF-DETECT execution time |
| `Parse_Time_ms` | REAL | RO | DICOM parsing time |

---

## Area Operations

### DICOM Processing Workflow

**Procedure:** Load and Process DICOM Image

**Unit Procedure 1: Image Acquisition**
```
Operation: Load DICOM File
├── Phase 1: Validate file format
├── Phase 2: Parse DICOM tags
├── Phase 3: Decode pixel data
└── Phase 4: Extract metadata
```

**Unit Procedure 2: Quality Check**
```
Operation: Validate Image Quality
├── Phase 1: Check DICOM compliance
├── Phase 2: Verify metadata completeness
├── Phase 3: Assess image quality
└── Phase 4: Generate quality report
```

**Unit Procedure 3: Preprocessing**
```
Operation: Prepare for Analysis
├── Phase 1: Apply window/level
├── Phase 2: Normalize intensity
├── Phase 3: Enhance contrast (CLAHE)
└── Phase 4: Resize/crop if needed
```

### AlF-DETECT Workflow

**Procedure:** Run AlF-DETECT Analysis

**Unit Procedure 1: Feature Extraction**
```
Operation: Extract Imaging Features
├── Phase 1: Preprocess for model input
├── Phase 2: Run feature extraction CNN
├── Phase 3: Post-process feature maps
└── Phase 4: Validate feature quality
```

**Unit Procedure 2: Classification**
```
Operation: Classify Alzheimer's/Autism
├── Phase 1: Run Alzheimer's classifier
├── Phase 2: Run Autism classifier
├── Phase 3: Calculate confidence scores
└── Phase 4: Threshold probabilities
```

**Unit Procedure 3: Result Generation**
```
Operation: Generate Diagnostic Report
├── Phase 1: Aggregate results
├── Phase 2: Format findings
├── Phase 3: Create structured report
└── Phase 4: Log to database
```

### Control Logic (PLC)

```javascript
// Medical PLC Control Loop (200ms scan)
if (DICOM_File_Loaded && systemReady) {

    // State Machine (PackML)
    switch (currentState) {
        case 'IDLE':
            if (newStudyAvailable) {
                currentState = 'STARTING';
            }
            break;

        case 'STARTING':
            initializePipeline();
            currentState = 'EXECUTE';
            break;

        case 'EXECUTE':
            // Parse DICOM
            parseDICOM();

            // Quality check
            if (!validateQuality()) {
                currentState = 'ABORTING';
                break;
            }

            // Preprocess
            preprocessImage();

            // Run AlF-DETECT
            if (AlF_Detect_Enabled) {
                runAlfDetect();
            }

            // Check completion
            if (processingComplete) {
                currentState = 'COMPLETING';
            }
            break;

        case 'COMPLETING':
            generateReport();
            logResults();
            currentState = 'COMPLETE';
            break;

        case 'COMPLETE':
            notifyCompletion();
            currentState = 'IDLE';
            break;

        case 'ABORTING':
            cleanupResources();
            logError();
            currentState = 'ABORTED';
            break;

        case 'ABORTED':
            // Manual reset required
            break;
    }

    // Update performance metrics
    updateProcessingTimes();
    updateQualityMetrics();
}
```

---

## Area Metrics

### Production KPIs
- **Throughput:** Studies analyzed per hour
- **Cycle Time:** Average processing time per study
- **Queue Depth:** Studies waiting for processing

### Quality KPIs
- **Diagnostic Accuracy:** True positive rate vs. ground truth
- **False Positive Rate:** Incorrect positive detections
- **False Negative Rate:** Missed detections
- **DICOM Compliance:** Percentage passing validation

### Performance KPIs
- **Processing Speed:** Images per second
- **Detection Latency:** Time to result (AlF-DETECT)
- **Resource Utilization:** GPU/CPU usage during processing

---

## Clinical Protocols

### X-Ray Protocol
- **Window/Level:** Lung (-600/1500), Bone (300/1500), Soft Tissue (50/400)
- **Enhancement:** CLAHE with clip limit 2.0
- **Preprocessing:** Normalize to [0,1], resize to 512x512

### CT Protocol
- **Window/Level:** Brain (40/80), Abdomen (60/400), Lung (-600/1600)
- **Slice Handling:** Multi-slice aggregation
- **3D Reconstruction:** Optional volume rendering

### MRI Protocol
- **Sequences:** T1, T2, FLAIR, DWI
- **Normalization:** Z-score normalization per sequence
- **Registration:** Align multi-sequence images

---

## Safety & Quality

### Safety Checks
- Verify patient consent (if required)
- Validate DICOM compliance
- Check image quality before analysis
- Ensure metadata completeness

### Quality Controls
- Ground truth validation (when available)
- Cross-validation with multiple models
- Expert radiologist review flag
- Confidence threshold enforcement

### Regulatory Compliance
- 21 CFR Part 11: Audit trails, electronic signatures
- HIPAA: Patient data anonymization
- DICOM Standard: Compliance validation
- FDA Requirements: Software as Medical Device (SaMD)

---

## Process Cell Definitions

See detailed process cell documents:
- `../process-cells/dicom-processing-cell.md`
- `../process-cells/alf-detect-cell.md`
- `../process-cells/imaging-pipeline-cell.md`

---

## Related Documents

- `../site/production-site.md` - Parent site
- `/os/medical/plc.html` - Area PLC controller
- `/os/medical/scada.html` - Area SCADA interface
- `/os/medical/hmi.html` - Area HMI panel
- `/os/medical/alf-detect.html` - AlF-DETECT application
- `/os/controls/tag-providers/medical.json` - Tag definitions
- `/os/modules/medical/` - Medical imaging modules

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Owner:** Medical Area Management
**Compliance:** 21 CFR Part 11, HIPAA, DICOM Standard
**Status:** Active
