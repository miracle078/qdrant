# DICOM Parser Unit

**ISA-88 Level:** Unit
**Parent:** DICOM Processing Cell
**ISA-95 Level:** L1 (Control Logic)
**Location:** `/os/modules/medical/medical-dicom-viewer.md` (parser section)

---

## Unit Overview

**Name:** DICOM File Parser Unit
**Purpose:** Parse DICOM file structure and decode pixel data into usable image arrays
**Type:** Discrete Control (single file at a time)

### Unit Description

The DICOM Parser Unit is responsible for:
- Validating DICOM file format
- Reading DICOM data elements (tags)
- Decoding pixel data from various transfer syntaxes
- Converting to JavaScript-friendly image arrays

---

## Unit Hierarchy

```
DICOM Parser Unit
├── File Validator Equipment Module
│   ├── Magic Number Checker Control Module
│   ├── Structure Validator Control Module
│   └── Encoding Validator Control Module
├── Tag Reader Equipment Module
│   ├── Preamble Parser Control Module
│   ├── Data Element Reader Control Module
│   └── Tag Dictionary Builder Control Module
└── Pixel Decoder Equipment Module
    ├── Transfer Syntax Detector Control Module
    ├── Decompressor Control Module
    └── Array Converter Control Module
```

---

## Equipment Modules

### 1. File Validator Equipment Module
**Purpose:** Validate DICOM file format before parsing
**Control Modules:**
- Magic Number Checker
- Structure Validator
- Encoding Validator

See: `../equipment-modules/file-validator-module.md`

### 2. Tag Reader Equipment Module
**Purpose:** Read and parse all DICOM data elements
**Control Modules:**
- Preamble Parser
- Data Element Reader
- Tag Dictionary Builder

See: `../equipment-modules/tag-reader-module.md`

### 3. Pixel Decoder Equipment Module
**Purpose:** Decode compressed pixel data to image array
**Control Modules:**
- Transfer Syntax Detector
- Decompressor
- Array Converter

See: `../equipment-modules/pixel-decoder-module.md`

---

## Unit Operations

### Normal Operation Sequence

**Operation:** Parse DICOM File

```
Phase 1: Validate File Format
  └─> Control: Check magic number ("DICM" at offset 128)
  └─> Control: Verify file size > minimum
  └─> Control: Detect byte order (little/big endian)
  └─> Result: Valid DICOM file → Continue
            Invalid file → Abort with error

Phase 2: Parse Preamble & Meta Information
  └─> Control: Read 128-byte preamble
  └─> Control: Parse File Meta Information group (0002)
  └─> Control: Extract Transfer Syntax UID
  └─> Result: Meta info parsed → Continue to data set

Phase 3: Parse Data Set
  └─> Control: Read data elements sequentially
  └─> Control: Parse tag (group, element)
  └─> Control: Parse VR (Value Representation)
  └─> Control: Parse value length
  └─> Control: Read value data
  └─> Control: Store in tag dictionary
  └─> Result: All tags parsed → Dictionary complete

Phase 4: Decode Pixel Data
  └─> Control: Locate pixel data tag (7FE0,0010)
  └─> Control: Determine transfer syntax
      ├─ Explicit VR Little Endian → Direct read
      ├─ JPEG Baseline → JPEG decompression
      ├─ JPEG Lossless → JPEG-LS decompression
      └─ RLE → Run-length decode
  └─> Control: Decompress if needed
  └─> Control: Convert to Uint8Array/Uint16Array
  └─> Result: Pixel data ready for rendering
```

---

## Unit Tags

### Input Tags
| Tag | Type | Source | Description |
|-----|------|--------|-------------|
| `File_Data` | BLOB | User Upload | Raw DICOM file bytes |
| `Parse_Start` | BOOL | Control | Trigger parsing |
| `Validate_Strict` | BOOL | Config | Strict validation mode |

### Output Tags
| Tag | Type | Destination | Description |
|-----|------|-------------|-------------|
| `Parse_Complete` | BOOL | Cell | Parsing finished |
| `Tag_Dictionary` | OBJECT | Cell | Parsed DICOM tags |
| `Pixel_Array` | ARRAY | Cell | Decoded pixel data |
| `Transfer_Syntax` | STRING | Cell | Detected transfer syntax |
| `Rows` | INT | Cell | Image height |
| `Columns` | INT | Cell | Image width |
| `Bits_Allocated` | INT | Cell | Bits per pixel |

### Internal Tags
| Tag | Type | Usage | Description |
|-----|------|-------|-------------|
| `Byte_Offset` | INT | Internal | Current read position |
| `Little_Endian` | BOOL | Internal | Byte order flag |
| `Current_Tag` | OBJECT | Internal | Tag being parsed |
| `Sequence_Depth` | INT | Internal | Nesting level (sequences) |

---

## Control Logic

### PackML State Machine

```javascript
class DICOMParserUnit {
    constructor() {
        this.state = 'IDLE';
        this.byteOffset = 0;
        this.tagDictionary = {};
        this.pixelArray = null;
    }

    execute() {
        switch (this.state) {
            case 'IDLE':
                if (this.fileDataAvailable && this.parseStart) {
                    this.state = 'STARTING';
                }
                break;

            case 'STARTING':
                this.byteOffset = 0;
                this.tagDictionary = {};
                this.state = 'EXECUTE';
                break;

            case 'EXECUTE':
                try {
                    // Phase 1: Validate
                    if (!this.validateFile()) {
                        throw new Error('Invalid DICOM file');
                    }

                    // Phase 2: Parse preamble & meta
                    this.parsePreamble();
                    this.parseMetaInfo();

                    // Phase 3: Parse data set
                    while (this.byteOffset < this.fileData.length) {
                        const tag = this.readDataElement();
                        this.tagDictionary[tag.key] = tag.value;

                        // Stop if pixel data reached
                        if (tag.group === 0x7FE0 && tag.element === 0x0010) {
                            break;
                        }
                    }

                    // Phase 4: Decode pixels
                    this.pixelArray = this.decodePixelData();

                    this.state = 'COMPLETING';

                } catch (error) {
                    this.errorMessage = error.message;
                    this.state = 'ABORTING';
                }
                break;

            case 'COMPLETING':
                this.parseComplete = true;
                this.outputTags();
                this.state = 'COMPLETE';
                break;

            case 'COMPLETE':
                // Notify parent cell
                this.notifyCompletion();
                this.state = 'IDLE';
                break;

            case 'ABORTING':
                this.cleanup();
                this.logError();
                this.state = 'ABORTED';
                break;

            case 'ABORTED':
                // Requires manual reset
                break;
        }
    }

    validateFile() {
        // Check minimum size (132 bytes for preamble + "DICM")
        if (this.fileData.length < 132) return false;

        // Check magic number "DICM" at offset 128
        const magic = String.fromCharCode(
            this.fileData[128],
            this.fileData[129],
            this.fileData[130],
            this.fileData[131]
        );

        return magic === 'DICM';
    }

    parsePreamble() {
        // Skip 128-byte preamble
        this.byteOffset = 128;

        // Skip "DICM" magic number
        this.byteOffset += 4;
    }

    parseMetaInfo() {
        // Parse group 0x0002 (File Meta Information)
        while (this.byteOffset < this.fileData.length) {
            const tag = this.readDataElement();

            // Stop when leaving meta info group
            if (tag.group !== 0x0002) {
                // Rewind to start of this tag
                this.byteOffset = tag.startOffset;
                break;
            }

            this.tagDictionary[tag.key] = tag.value;

            // Extract transfer syntax
            if (tag.element === 0x0010) {
                this.transferSyntax = tag.value;
            }
        }
    }

    readDataElement() {
        const startOffset = this.byteOffset;

        // Read tag (group, element)
        const group = this.readUint16();
        const element = this.readUint16();
        const key = `(${group.toString(16).padStart(4, '0')},${element.toString(16).padStart(4, '0')})`;

        // Read VR (Value Representation)
        const vr = this.readVR();

        // Read value length
        const valueLength = this.readValueLength(vr);

        // Read value data
        const value = this.readValue(vr, valueLength);

        return {
            startOffset,
            group,
            element,
            key,
            vr,
            valueLength,
            value
        };
    }

    decodePixelData() {
        const pixelDataTag = this.tagDictionary['(7fe0,0010)'];

        if (!pixelDataTag) {
            throw new Error('Pixel data tag not found');
        }

        // Determine transfer syntax
        const transferSyntax = this.transferSyntax || '1.2.840.10008.1.2.1'; // Explicit VR Little Endian default

        let pixelArray;

        switch (transferSyntax) {
            case '1.2.840.10008.1.2':
            case '1.2.840.10008.1.2.1':
                // Explicit/Implicit VR Little Endian - uncompressed
                pixelArray = new Uint16Array(pixelDataTag);
                break;

            case '1.2.840.10008.1.2.4.50':
            case '1.2.840.10008.1.2.4.51':
                // JPEG Baseline/Extended
                pixelArray = this.decompressJPEG(pixelDataTag);
                break;

            case '1.2.840.10008.1.2.5':
                // RLE Lossless
                pixelArray = this.decompressRLE(pixelDataTag);
                break;

            default:
                throw new Error(`Unsupported transfer syntax: ${transferSyntax}`);
        }

        return pixelArray;
    }
}
```

---

## Performance Specifications

### Timing
- **Validation:** <5ms
- **Preamble/Meta Parsing:** <10ms
- **Data Set Parsing:** <50ms (typical)
- **Pixel Decoding:** <50ms (uncompressed), <200ms (JPEG)
- **Total Unit Cycle:** <100ms typical, <300ms compressed

### Throughput
- **Files/Second:** >10 files/sec (uncompressed)
- **Files/Second:** >3 files/sec (JPEG compressed)

### Resource Usage
- **Memory:** ~2x file size during parsing
- **CPU:** Single-threaded JavaScript execution

---

## Error Handling

### Error Conditions
1. **Invalid Magic Number:** Not a DICOM file
2. **Corrupted Structure:** Malformed tags
3. **Unsupported Transfer Syntax:** Cannot decode
4. **Missing Required Tags:** Incomplete DICOM
5. **Pixel Data Corruption:** Cannot decompress

### Error Actions
- Log error details
- Set error tags
- Transition to ABORTED state
- Notify operator
- Preserve partial results if possible

---

## Quality Controls

### Validation Checks
- ✅ Magic number "DICM" present
- ✅ File Meta Information group (0002) present
- ✅ Required tags present (Rows, Columns, etc.)
- ✅ Pixel data tag (7FE0,0010) present
- ✅ Transfer Syntax UID valid
- ✅ Byte order correct

### Quality Metrics
- **Parse Success Rate:** >99.9%
- **Validation Pass Rate:** >95%
- **Performance:** <100ms average

---

## Related Documents

- `../process-cells/dicom-processing-cell.md` - Parent process cell
- `../equipment-modules/file-validator-module.md` - File validator
- `../equipment-modules/tag-reader-module.md` - Tag reader
- `../equipment-modules/pixel-decoder-module.md` - Pixel decoder
- `/docs/standards/protocols/dicom.md` - DICOM standard

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Owner:** Medical Area - DICOM Parser
**Compliance:** DICOM Standard PS3.5, PS3.10
**Status:** Active
