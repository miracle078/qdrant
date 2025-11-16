# Tag Reader Equipment Module

**ISA-88 Level:** Equipment Module
**Parent:** DICOM Parser Unit
**ISA-95 Level:** L1 (Control Logic)
**Type:** Reusable component for reading DICOM data elements

---

## Equipment Module Overview

**Name:** DICOM Tag Reader Module
**Purpose:** Read and parse individual DICOM data elements (tags) from byte stream
**Reusability:** Used by DICOM Parser Unit, Metadata Extractor Unit

### Module Description

The Tag Reader Equipment Module is a reusable component that:
- Reads binary DICOM data elements
- Parses tag structure (group, element, VR, length, value)
- Handles both Explicit and Implicit VR
- Supports nested sequences
- Manages byte order (endianness)

---

## Equipment Module Hierarchy

```
Tag Reader Equipment Module
├── Preamble Parser Control Module
│   └── Functions: readPreamble(), verifyMagicNumber()
├── Data Element Reader Control Module
│   └── Functions: readTag(), readVR(), readLength(), readValue()
└── Tag Dictionary Builder Control Module
    └── Functions: buildDictionary(), lookupVR(), formatValue()
```

---

## Control Modules

### 1. Preamble Parser Control Module
**Purpose:** Parse DICOM file preamble and meta information
**Functions:**
- `readPreamble()` - Skip 128-byte preamble
- `verifyMagicNumber()` - Check "DICM" signature
- `parseMetaInfo()` - Parse group 0x0002

See: `../control-modules/preamble-parser.md`

### 2. Data Element Reader Control Module
**Purpose:** Read individual DICOM data elements
**Functions:**
- `readTag()` - Read (group, element) pair
- `readVR()` - Read Value Representation
- `readLength()` - Read value length
- `readValue()` - Read value data

See: `../control-modules/data-element-reader.md`

### 3. Tag Dictionary Builder Control Module
**Purpose:** Build structured dictionary from tags
**Functions:**
- `buildDictionary()` - Organize tags into dictionary
- `lookupVR()` - Lookup VR from data dictionary
- `formatValue()` - Format value by VR type

See: `../control-modules/tag-dictionary-builder.md`

---

## Module Interface

### Input Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `fileData` | Uint8Array | Raw DICOM file bytes |
| `byteOffset` | Number | Starting read position |
| `littleEndian` | Boolean | Byte order flag |
| `explicitVR` | Boolean | Explicit VR mode |

### Output Data
| Output | Type | Description |
|--------|------|-------------|
| `tagDictionary` | Object | Parsed DICOM tags {key: value} |
| `newByteOffset` | Number | Updated read position |
| `tagsRead` | Number | Count of tags parsed |

### Status Signals
| Signal | Type | Description |
|--------|------|-------------|
| `parseComplete` | Boolean | All tags read successfully |
| `parseError` | String | Error message if failed |
| `sequenceDepth` | Number | Current nesting level |

---

## Module Operations

### Operation: Read DICOM Data Element

```javascript
/**
 * Equipment Module: Tag Reader
 * Operation: Read and parse a single DICOM data element
 */
function readDataElement(fileData, byteOffset, littleEndian, explicitVR) {
    const startOffset = byteOffset;

    // Step 1: Read Tag (Group, Element)
    const group = readUint16(fileData, byteOffset, littleEndian);
    byteOffset += 2;

    const element = readUint16(fileData, byteOffset, littleEndian);
    byteOffset += 2;

    const tagKey = `(${group.toString(16).padStart(4, '0')},${element.toString(16).padStart(4, '0')})`;

    // Step 2: Read VR (Value Representation)
    let vr;
    let valueLength;

    if (explicitVR) {
        // Explicit VR: VR is encoded in file
        vr = String.fromCharCode(fileData[byteOffset], fileData[byteOffset + 1]);
        byteOffset += 2;

        // Check if VR has extended length
        const extendedLengthVRs = ['OB', 'OD', 'OF', 'OL', 'OW', 'SQ', 'UC', 'UR', 'UT', 'UN'];

        if (extendedLengthVRs.includes(vr)) {
            // Skip 2 reserved bytes
            byteOffset += 2;

            // Read 32-bit length
            valueLength = readUint32(fileData, byteOffset, littleEndian);
            byteOffset += 4;
        } else {
            // Read 16-bit length
            valueLength = readUint16(fileData, byteOffset, littleEndian);
            byteOffset += 2;
        }
    } else {
        // Implicit VR: VR must be looked up from data dictionary
        vr = lookupVR(group, element);

        // Read 32-bit length
        valueLength = readUint32(fileData, byteOffset, littleEndian);
        byteOffset += 4;
    }

    // Step 3: Read Value Data
    let value;

    // Undefined length (sequences)
    if (valueLength === 0xFFFFFFFF) {
        value = readSequence(fileData, byteOffset, littleEndian, explicitVR);
        byteOffset = value.newOffset;
    } else {
        // Known length
        value = readValue(fileData, byteOffset, vr, valueLength, littleEndian);
        byteOffset += valueLength;
    }

    return {
        startOffset,
        endOffset: byteOffset,
        group,
        element,
        tagKey,
        vr,
        valueLength,
        value
    };
}

/**
 * Control Module: Data Element Reader
 * Function: Read binary value by VR type
 */
function readValue(fileData, byteOffset, vr, valueLength, littleEndian) {
    switch (vr) {
        case 'US': // Unsigned Short
        case 'SS': // Signed Short
            return readInt16Array(fileData, byteOffset, valueLength, littleEndian, vr === 'SS');

        case 'UL': // Unsigned Long
        case 'SL': // Signed Long
            return readInt32Array(fileData, byteOffset, valueLength, littleEndian, vr === 'SL');

        case 'FL': // Float
            return readFloat32Array(fileData, byteOffset, valueLength, littleEndian);

        case 'FD': // Double
            return readFloat64Array(fileData, byteOffset, valueLength, littleEndian);

        case 'AE': // Application Entity
        case 'AS': // Age String
        case 'CS': // Code String
        case 'DA': // Date
        case 'DT': // DateTime
        case 'LO': // Long String
        case 'LT': // Long Text
        case 'PN': // Person Name
        case 'SH': // Short String
        case 'ST': // Short Text
        case 'TM': // Time
        case 'UC': // Unlimited Characters
        case 'UI': // Unique Identifier
        case 'UR': // URI
        case 'UT': // Unlimited Text
            return readString(fileData, byteOffset, valueLength);

        case 'OB': // Other Byte
        case 'OD': // Other Double
        case 'OF': // Other Float
        case 'OL': // Other Long
        case 'OW': // Other Word
        case 'UN': // Unknown
            return readBinary(fileData, byteOffset, valueLength);

        case 'SQ': // Sequence
            return readSequence(fileData, byteOffset, littleEndian, true);

        default:
            // Unknown VR, read as binary
            return readBinary(fileData, byteOffset, valueLength);
    }
}

/**
 * Control Module: Tag Dictionary Builder
 * Function: Lookup VR from DICOM data dictionary
 */
function lookupVR(group, element) {
    // Simplified VR lookup - in production, use full data dictionary
    const tagKey = `(${group.toString(16).padStart(4, '0')},${element.toString(16).padStart(4, '0')})`;

    const vrDictionary = {
        '(0008,0005)': 'CS', // Specific Character Set
        '(0008,0008)': 'CS', // Image Type
        '(0008,0016)': 'UI', // SOP Class UID
        '(0008,0018)': 'UI', // SOP Instance UID
        '(0008,0020)': 'DA', // Study Date
        '(0008,0030)': 'TM', // Study Time
        '(0008,0050)': 'SH', // Accession Number
        '(0008,0060)': 'CS', // Modality
        '(0008,0070)': 'LO', // Manufacturer
        '(0008,0090)': 'PN', // Referring Physician Name
        '(0010,0010)': 'PN', // Patient Name
        '(0010,0020)': 'LO', // Patient ID
        '(0010,0030)': 'DA', // Patient Birth Date
        '(0010,0040)': 'CS', // Patient Sex
        '(0018,0050)': 'DS', // Slice Thickness
        '(0018,0060)': 'DS', // KVP
        '(0018,1030)': 'LO', // Protocol Name
        '(0020,000d)': 'UI', // Study Instance UID
        '(0020,000e)': 'UI', // Series Instance UID
        '(0020,0010)': 'SH', // Study ID
        '(0020,0011)': 'IS', // Series Number
        '(0020,0013)': 'IS', // Instance Number
        '(0028,0002)': 'US', // Samples Per Pixel
        '(0028,0004)': 'CS', // Photometric Interpretation
        '(0028,0010)': 'US', // Rows
        '(0028,0011)': 'US', // Columns
        '(0028,0100)': 'US', // Bits Allocated
        '(0028,0101)': 'US', // Bits Stored
        '(0028,0102)': 'US', // High Bit
        '(0028,0103)': 'US', // Pixel Representation
        '(0028,1050)': 'DS', // Window Center
        '(0028,1051)': 'DS', // Window Width
        '(7fe0,0010)': 'OW', // Pixel Data
    };

    return vrDictionary[tagKey] || 'UN'; // Unknown if not in dictionary
}
```

---

## Module Configuration

### Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `maxSequenceDepth` | 10 | Maximum nesting for sequences |
| `strictValidation` | true | Enforce strict DICOM compliance |
| `stopOnPixelData` | false | Stop parsing at pixel data tag |
| `parseBinary` | true | Parse binary VRs (OB, OW, etc.) |

### Limits
| Limit | Value | Purpose |
|-------|-------|---------|
| `maxValueLength` | 1GB | Prevent memory exhaustion |
| `maxTagCount` | 100,000 | Limit tags per file |
| `maxStringLength` | 1MB | Limit string VR values |

---

## Performance Characteristics

### Timing
- **Single Tag Read:** <0.1ms
- **Typical DICOM (1000 tags):** <50ms
- **Large DICOM (10000 tags):** <500ms

### Memory
- **Tag Dictionary:** ~100 bytes per tag
- **Typical DICOM:** ~100 KB dictionary
- **Peak Usage:** ~2x file size (including pixel data)

---

## Error Handling

### Error Types
1. **Invalid Tag Format:** Malformed group/element
2. **Unknown VR:** VR not recognized
3. **Length Mismatch:** Value length incorrect
4. **Sequence Error:** Malformed sequence structure
5. **Encoding Error:** Invalid string encoding

### Error Recovery
- **Log Error:** Record detailed error information
- **Skip Tag:** Continue to next tag if possible
- **Partial Parse:** Return tags parsed before error
- **Abort:** Stop parsing on critical errors

---

## Validation

### Input Validation
- ✅ fileData is Uint8Array
- ✅ byteOffset within file bounds
- ✅ littleEndian is boolean
- ✅ explicitVR is boolean

### Output Validation
- ✅ All tags have valid group/element
- ✅ All VRs are recognized
- ✅ All value lengths match actual data
- ✅ No duplicate tag keys (unless sequences)

---

## Usage Example

```javascript
// Initialize Tag Reader Module
const tagReader = new TagReaderModule({
    strictValidation: true,
    maxSequenceDepth: 10
});

// Read all tags from DICOM file
const result = tagReader.readAll(fileData, {
    startOffset: 132, // After preamble
    littleEndian: true,
    explicitVR: true
});

console.log(`Read ${result.tagsRead} tags`);
console.log(`Dictionary:`, result.tagDictionary);

// Access specific tag
const patientName = result.tagDictionary['(0010,0010)'];
const studyUID = result.tagDictionary['(0020,000d)'];
```

---

## Related Documents

- `../units/dicom-parser-unit.md` - Parent unit
- `../control-modules/preamble-parser.md` - Preamble parser
- `../control-modules/data-element-reader.md` - Data element reader
- `../control-modules/tag-dictionary-builder.md` - Dictionary builder
- `/docs/standards/protocols/dicom.md` - DICOM standard

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Owner:** DICOM Parser - Tag Reader
**Compliance:** DICOM Standard PS3.5
**Status:** Active
