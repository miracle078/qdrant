# DICOM Processing Cell

**ISA-88 Level:** Process Cell
**Parent:** Medical Area
**ISA-95 Level:** L2 (Supervisory) / L1 (Control)
**Location:** `/os/modules/medical/medical-dicom-viewer.md`

---

## Process Cell Overview

**Name:** DICOM Image Processing Cell
**Purpose:** Parse, validate, and extract data from DICOM medical images
**Capacity:** Real-time processing, unlimited concurrent files (browser-limited)

### Process Cell Description

The DICOM Processing Cell handles all operations related to DICOM (Digital Imaging and Communications in Medicine) file handling, including:
- File format validation
- DICOM tag parsing
- Pixel data decoding
- Metadata extraction
- Quality validation

---

## Process Cell Hierarchy

```
DICOM Processing Cell
├── DICOM Parser Unit
│   ├── File Validator Equipment Module
│   ├── Tag Reader Equipment Module
│   └── Pixel Decoder Equipment Module
├── Metadata Extractor Unit
│   ├── Patient Info Equipment Module
│   ├── Study Info Equipment Module
│   └── Series Info Equipment Module
└── Quality Validator Unit
    ├── Format Checker Equipment Module
    ├── Completeness Checker Equipment Module
    └── Integrity Checker Equipment Module
```

---

## Units in This Process Cell

### 1. DICOM Parser Unit
**Purpose:** Parse DICOM file structure and decode pixel data
**Location:** Core parsing functionality
**Equipment Modules:**
- File Validator
- Tag Reader
- Pixel Decoder

See: `../units/dicom-parser-unit.md`

### 2. Metadata Extractor Unit
**Purpose:** Extract clinical and technical metadata
**Location:** Metadata extraction logic
**Equipment Modules:**
- Patient Info extractor
- Study Info extractor
- Series Info extractor

See: `../units/metadata-extractor-unit.md`

### 3. Quality Validator Unit
**Purpose:** Validate DICOM compliance and image quality
**Location:** Validation logic
**Equipment Modules:**
- Format Checker
- Completeness Checker
- Integrity Checker

See: `../units/quality-validator-unit.md`

---

## Process Cell Operations

### Standard Operation Procedure

**Procedure:** Process DICOM Image File

```
STARTING Phase:
  └─> Initialize buffers
  └─> Allocate memory
  └─> Set up parsers

EXECUTE Phase:
  Unit Procedure 1: Parse DICOM
    └─> Operation: Validate file
        ├─ Phase: Check magic number
        ├─ Phase: Verify file structure
        └─ Phase: Validate encoding
    └─> Operation: Read tags
        ├─ Phase: Parse preamble
        ├─ Phase: Read data elements
        └─ Phase: Build tag dictionary
    └─> Operation: Decode pixels
        ├─ Phase: Determine transfer syntax
        ├─ Phase: Decompress if needed
        └─ Phase: Convert to image array

  Unit Procedure 2: Extract Metadata
    └─> Operation: Extract patient data
        ├─ Phase: Read patient name
        ├─ Phase: Read patient ID
        └─ Phase: Anonymize if required
    └─> Operation: Extract study data
        ├─ Phase: Read study UID
        ├─ Phase: Read study date
        └─ Phase: Read modality
    └─> Operation: Extract series data
        ├─ Phase: Read series UID
        ├─ Phase: Read series number
        └─ Phase: Read acquisition params

  Unit Procedure 3: Validate Quality
    └─> Operation: Check format compliance
        ├─ Phase: Validate DICOM standard
        ├─ Phase: Check required tags
        └─ Phase: Verify data integrity
    └─> Operation: Assess image quality
        ├─ Phase: Check pixel data validity
        ├─ Phase: Evaluate noise level
        └─ Phase: Detect artifacts

COMPLETING Phase:
  └─> Store parsed data
  └─> Update status tags
  └─> Log completion

COMPLETE Phase:
  └─> Ready for next file
```

---

## Process Cell Tags

### Input Tags (from parent Medical Area)
| Tag | Type | Source | Description |
|-----|------|--------|-------------|
| `DICOM_File_Path` | STRING | User | Path to DICOM file |
| `Parse_Enable` | BOOL | Control | Enable parsing |
| `Anonymize_Enable` | BOOL | Control | Anonymize patient data |

### Output Tags (to parent Medical Area)
| Tag | Type | Destination | Description |
|-----|------|-------------|-------------|
| `DICOM_File_Loaded` | BOOL | Status | File successfully loaded |
| `Image_Width` | INT | Status | Parsed image width |
| `Image_Height` | INT | Status | Parsed image height |
| `Modality` | STRING | Status | Imaging modality |
| `Patient_ID` | STRING | Status | Patient identifier |
| `Study_Instance_UID` | STRING | Status | Study UID |
| `DICOM_Compliance` | BOOL | Quality | Passes validation |
| `Parse_Time_ms` | REAL | Performance | Parsing duration |

### Internal Tags (cell-level)
| Tag | Type | Usage | Description |
|-----|------|-------|-------------|
| `Parser_State` | STRING | Internal | Current parser state |
| `Current_Tag_Group` | INT | Internal | Current DICOM group |
| `Current_Tag_Element` | INT | Internal | Current DICOM element |
| `Bytes_Processed` | INT | Internal | Total bytes processed |
| `Tags_Parsed` | INT | Internal | Number of tags parsed |

---

## Process Cell Performance

### Cycle Time Targets
- **Parse Time:** <100ms (typical DICOM file)
- **Metadata Extraction:** <10ms
- **Quality Validation:** <50ms
- **Total Cycle:** <200ms

### Throughput Targets
- **Files/Second:** >5 files/sec
- **Concurrent Operations:** Limited by browser
- **Queue Depth:** No queuing (real-time)

### Quality Targets
- **DICOM Compliance:** 100% for valid files
- **Parsing Success Rate:** >99.9%
- **Metadata Completeness:** >95%

---

## Control Strategy

### Control Modes

**Manual Mode:**
- Operator initiates parsing
- Step-by-step execution
- Full visibility of each phase

**Automatic Mode:**
- Auto-parse on file upload
- Background processing
- Notification on completion

**Batch Mode:**
- Process multiple files
- Sequential or parallel
- Progress reporting

### Control Logic

```javascript
// DICOM Processing Cell Control Logic
class DICOMProcessingCell {
    constructor() {
        this.state = 'IDLE';
        this.currentUnit = null;
        this.dicomData = null;
    }

    execute() {
        switch (this.state) {
            case 'IDLE':
                if (this.newFileAvailable()) {
                    this.state = 'STARTING';
                }
                break;

            case 'STARTING':
                this.initializeBuffers();
                this.state = 'EXECUTE';
                break;

            case 'EXECUTE':
                // Unit 1: Parse DICOM
                this.currentUnit = 'DICOM_PARSER';
                const parsedData = this.parserUnit.parse(this.fileData);

                if (!parsedData.valid) {
                    this.state = 'ABORTING';
                    break;
                }

                // Unit 2: Extract Metadata
                this.currentUnit = 'METADATA_EXTRACTOR';
                this.metadata = this.metadataUnit.extract(parsedData);

                // Unit 3: Validate Quality
                this.currentUnit = 'QUALITY_VALIDATOR';
                const qualityCheck = this.qualityUnit.validate(parsedData, this.metadata);

                if (!qualityCheck.passed) {
                    this.qualityWarning = qualityCheck.warnings;
                }

                this.state = 'COMPLETING';
                break;

            case 'COMPLETING':
                this.storeParsedData();
                this.updateStatusTags();
                this.logCompletion();
                this.state = 'COMPLETE';
                break;

            case 'COMPLETE':
                this.notifyCompletion();
                this.state = 'IDLE';
                break;

            case 'ABORTING':
                this.cleanupResources();
                this.logError();
                this.state = 'ABORTED';
                break;
        }
    }
}
```

---

## Equipment Modules

See detailed equipment module definitions:
- `../equipment-modules/file-validator-module.md`
- `../equipment-modules/tag-reader-module.md`
- `../equipment-modules/pixel-decoder-module.md`
- `../equipment-modules/patient-info-module.md`
- `../equipment-modules/study-info-module.md`
- `../equipment-modules/series-info-module.md`

---

## Alarms & Events

### Critical Alarms
- **Invalid DICOM Format:** File does not conform to DICOM standard
- **Corrupted Pixel Data:** Pixel data cannot be decoded
- **Missing Required Tags:** Required DICOM tags absent

### Warnings
- **Non-Standard Tags:** Custom tags present
- **Deprecated Transfer Syntax:** Old compression method
- **Image Quality Low:** Noise or artifacts detected

### Events
- **Parse Started:** DICOM parsing initiated
- **Parse Completed:** DICOM parsing finished successfully
- **Metadata Extracted:** Metadata extraction complete
- **Quality Validated:** Quality check passed

---

## Maintenance

### Preventive Maintenance
- **Weekly:** Clear parsing cache
- **Monthly:** Update DICOM dictionary
- **Quarterly:** Validate against latest DICOM standard

### Corrective Maintenance
- **Parse Failures:** Review error logs, update parser
- **Memory Leaks:** Profile memory usage, fix leaks
- **Performance Degradation:** Optimize hot paths

---

## Documentation

### Standards
- **DICOM Standard:** PS3.1-PS3.21 (latest version)
- **Transfer Syntaxes:** Supported compression formats
- **Character Sets:** Supported text encodings

### Validation Rules
- Required DICOM tags list
- Tag value range constraints
- Metadata completeness criteria
- Image quality thresholds

---

## Related Documents

- `../areas/medical-area.md` - Parent area
- `../units/dicom-parser-unit.md` - Parser unit details
- `../units/metadata-extractor-unit.md` - Metadata extractor details
- `../units/quality-validator-unit.md` - Quality validator details
- `/docs/standards/protocols/dicom.md` - DICOM standard reference

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Owner:** Medical Area - DICOM Processing
**Compliance:** DICOM Standard PS3.1-PS3.21
**Status:** Active
