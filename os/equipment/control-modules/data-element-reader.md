# Data Element Reader Control Module

**ISA-88 Level:** Control Module
**Parent:** Tag Reader Equipment Module
**ISA-95 Level:** L0/L1 (Physical I/O / Control Logic)
**Type:** Elementary control function

---

## Control Module Overview

**Name:** DICOM Data Element Reader
**Purpose:** Low-level binary reading of DICOM data elements from byte stream
**Type:** Read-only control (no actuators, only sensors)

### Module Description

The Data Element Reader Control Module provides primitive functions for:
- Reading binary data from Uint8Array
- Handling byte order (endianness)
- Converting binary to JavaScript types
- Managing read position (byte offset)

This is the lowest level in the ISA-88 hierarchy - individual control functions that directly interact with the "physical process" (file data).

---

## Control Module Functions

```
Data Element Reader Control Module
├── readUint8() - Read 1-byte unsigned integer
├── readUint16() - Read 2-byte unsigned integer
├── readUint32() - Read 4-byte unsigned integer
├── readInt16() - Read 2-byte signed integer
├── readInt32() - Read 4-byte signed integer
├── readFloat32() - Read 4-byte floating point
├── readFloat64() - Read 8-byte floating point
├── readString() - Read string with encoding
├── readBinary() - Read binary blob
└── readArray() - Read array of values
```

---

## Function Specifications

### readUint16()

**Purpose:** Read 2-byte unsigned integer from byte stream

**Signature:**
```javascript
function readUint16(data, offset, littleEndian)
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | Uint8Array | Source byte array |
| `offset` | Number | Read position |
| `littleEndian` | Boolean | Byte order flag |

**Returns:**
| Return | Type | Description |
|--------|------|-------------|
| `value` | Number | Unsigned 16-bit integer (0-65535) |

**Algorithm:**
```javascript
function readUint16(data, offset, littleEndian) {
    if (littleEndian) {
        // Little endian: LSB first
        return data[offset] | (data[offset + 1] << 8);
    } else {
        // Big endian: MSB first
        return (data[offset] << 8) | data[offset + 1];
    }
}
```

**Performance:**
- **Execution Time:** <0.001ms
- **Memory:** No allocation
- **Side Effects:** None (pure function)

---

### readUint32()

**Purpose:** Read 4-byte unsigned integer from byte stream

**Signature:**
```javascript
function readUint32(data, offset, littleEndian)
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | Uint8Array | Source byte array |
| `offset` | Number | Read position |
| `littleEndian` | Boolean | Byte order flag |

**Returns:**
| Return | Type | Description |
|--------|------|-------------|
| `value` | Number | Unsigned 32-bit integer (0-4294967295) |

**Algorithm:**
```javascript
function readUint32(data, offset, littleEndian) {
    if (littleEndian) {
        // Little endian: LSB first
        return (data[offset] |
                (data[offset + 1] << 8) |
                (data[offset + 2] << 16) |
                (data[offset + 3] << 24)) >>> 0; // >>> 0 ensures unsigned
    } else {
        // Big endian: MSB first
        return ((data[offset] << 24) |
                (data[offset + 1] << 16) |
                (data[offset + 2] << 8) |
                data[offset + 3]) >>> 0;
    }
}
```

---

### readFloat32()

**Purpose:** Read 4-byte IEEE 754 floating point from byte stream

**Signature:**
```javascript
function readFloat32(data, offset, littleEndian)
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | Uint8Array | Source byte array |
| `offset` | Number | Read position |
| `littleEndian` | Boolean | Byte order flag |

**Returns:**
| Return | Type | Description |
|--------|------|-------------|
| `value` | Number | 32-bit floating point |

**Algorithm:**
```javascript
function readFloat32(data, offset, littleEndian) {
    // Use DataView for proper float conversion
    const dataView = new DataView(data.buffer, data.byteOffset + offset, 4);
    return dataView.getFloat32(0, littleEndian);
}
```

**Note:** Uses DataView for correct IEEE 754 conversion

---

### readFloat64()

**Purpose:** Read 8-byte IEEE 754 double precision from byte stream

**Signature:**
```javascript
function readFloat64(data, offset, littleEndian)
```

**Algorithm:**
```javascript
function readFloat64(data, offset, littleEndian) {
    const dataView = new DataView(data.buffer, data.byteOffset + offset, 8);
    return dataView.getFloat64(0, littleEndian);
}
```

---

### readString()

**Purpose:** Read string with specified encoding

**Signature:**
```javascript
function readString(data, offset, length, encoding = 'utf-8')
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | Uint8Array | Source byte array |
| `offset` | Number | Read position |
| `length` | Number | String length in bytes |
| `encoding` | String | Character encoding (utf-8, ascii, iso-8859-1) |

**Returns:**
| Return | Type | Description |
|--------|------|-------------|
| `value` | String | Decoded string |

**Algorithm:**
```javascript
function readString(data, offset, length, encoding = 'utf-8') {
    const bytes = data.slice(offset, offset + length);

    // Remove trailing null bytes and spaces (DICOM padding)
    let endIdx = bytes.length;
    while (endIdx > 0 && (bytes[endIdx - 1] === 0 || bytes[endIdx - 1] === 32)) {
        endIdx--;
    }

    const trimmedBytes = bytes.slice(0, endIdx);

    // Decode based on encoding
    switch (encoding.toLowerCase()) {
        case 'utf-8':
        case 'utf8':
            return new TextDecoder('utf-8').decode(trimmedBytes);

        case 'ascii':
            return String.fromCharCode(...trimmedBytes);

        case 'iso-8859-1':
        case 'latin1':
            return new TextDecoder('iso-8859-1').decode(trimmedBytes);

        default:
            return new TextDecoder('utf-8').decode(trimmedBytes);
    }
}
```

---

### readBinary()

**Purpose:** Read binary blob (no conversion)

**Signature:**
```javascript
function readBinary(data, offset, length)
```

**Returns:**
| Return | Type | Description |
|--------|------|-------------|
| `value` | Uint8Array | Raw binary data slice |

**Algorithm:**
```javascript
function readBinary(data, offset, length) {
    return data.slice(offset, offset + length);
}
```

---

### readInt16Array()

**Purpose:** Read array of 16-bit integers

**Signature:**
```javascript
function readInt16Array(data, offset, length, littleEndian, signed = false)
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | Uint8Array | Source byte array |
| `offset` | Number | Read position |
| `length` | Number | Total bytes (not count) |
| `littleEndian` | Boolean | Byte order flag |
| `signed` | Boolean | Signed vs unsigned |

**Returns:**
| Return | Type | Description |
|--------|------|-------------|
| `value` | Int16Array or Uint16Array | Array of integers |

**Algorithm:**
```javascript
function readInt16Array(data, offset, length, littleEndian, signed = false) {
    const count = length / 2;
    const array = signed ? new Int16Array(count) : new Uint16Array(count);

    for (let i = 0; i < count; i++) {
        const byteOffset = offset + (i * 2);

        if (littleEndian) {
            array[i] = data[byteOffset] | (data[byteOffset + 1] << 8);
        } else {
            array[i] = (data[byteOffset] << 8) | data[byteOffset + 1];
        }

        // Sign extension for signed values
        if (signed && array[i] & 0x8000) {
            array[i] |= 0xFFFF0000; // Extend sign bit
        }
    }

    return array;
}
```

**Optimization Note:** For large arrays, consider using DataView in a loop instead of bit shifting for better performance.

---

## Control Module Interface

### Inputs (Sensors)
| Input | Type | Source | Description |
|-------|------|--------|-------------|
| `fileData` | Uint8Array | User upload | Raw DICOM bytes |
| `byteOffset` | Number | Parent module | Current read position |
| `littleEndian` | Boolean | Meta info | Byte order flag |

### Outputs (No Actuators)
| Output | Type | Destination | Description |
|--------|------|-------------|-------------|
| `value` | Various | Parent module | Parsed value |

### Internal State
| State | Type | Usage | Description |
|-------|------|-------|-------------|
| None | - | - | Pure functions, no state |

**Note:** This control module is stateless - all functions are pure (no side effects).

---

## Error Handling

### Error Conditions
1. **Out of Bounds:** offset + length > data.length
2. **Invalid Encoding:** Unsupported character encoding
3. **Invalid Float:** NaN or Infinity in float conversion
4. **Type Error:** data is not Uint8Array

### Error Actions
```javascript
function readUint16(data, offset, littleEndian) {
    // Validate inputs
    if (!(data instanceof Uint8Array)) {
        throw new TypeError('data must be Uint8Array');
    }

    if (offset + 2 > data.length) {
        throw new RangeError(`Offset ${offset} out of bounds (length ${data.length})`);
    }

    // Proceed with read...
}
```

---

## Performance Characteristics

### Execution Time
| Function | Time | Notes |
|----------|------|-------|
| `readUint8()` | <0.001ms | Single byte access |
| `readUint16()` | <0.001ms | Bit shift operation |
| `readUint32()` | <0.001ms | Bit shift operation |
| `readFloat32()` | <0.01ms | DataView overhead |
| `readFloat64()` | <0.01ms | DataView overhead |
| `readString(100)` | <0.1ms | TextDecoder overhead |
| `readInt16Array(1000)` | <1ms | Loop overhead |

### Memory Usage
| Function | Memory | Notes |
|----------|--------|-------|
| `readUint*()` | 0 bytes | No allocation |
| `readFloat*()` | 4-8 bytes | DataView temporary |
| `readString()` | ~2x length | TextDecoder buffer |
| `readArray()` | exact length | Typed array allocation |

---

## Testing & Validation

### Unit Tests
```javascript
// Test readUint16 - Little Endian
const data = new Uint8Array([0x34, 0x12, 0x78, 0x56]);
assert(readUint16(data, 0, true) === 0x1234);
assert(readUint16(data, 2, true) === 0x5678);

// Test readUint16 - Big Endian
assert(readUint16(data, 0, false) === 0x3412);
assert(readUint16(data, 2, false) === 0x7856);

// Test readFloat32
const floatData = new Uint8Array([0x00, 0x00, 0x80, 0x3F]); // 1.0 in LE
assert(readFloat32(floatData, 0, true) === 1.0);

// Test readString
const strData = new Uint8Array([0x48, 0x65, 0x6C, 0x6C, 0x6F]); // "Hello"
assert(readString(strData, 0, 5) === 'Hello');

// Test error handling
assert.throws(() => readUint16(data, 100, true), RangeError);
```

### Integration Tests
- Test with actual DICOM files
- Verify correct byte order handling
- Validate string encoding conversions
- Check array reading performance

---

## Usage Guidelines

### Best Practices
1. **Validate inputs** before calling (bounds checking)
2. **Use appropriate types** (Uint vs Int, Float32 vs Float64)
3. **Handle endianness** correctly based on DICOM transfer syntax
4. **Optimize array reads** for large data (use DataView)
5. **Cache DataView** if reading multiple values from same buffer

### Common Pitfalls
- ❌ Forgetting to check bounds
- ❌ Wrong endianness
- ❌ Signed vs unsigned confusion
- ❌ String encoding mismatches
- ❌ Memory leaks from large buffer slices

---

## Related Documents

- `../equipment-modules/tag-reader-module.md` - Parent equipment module
- `../units/dicom-parser-unit.md` - Grandparent unit
- `/docs/standards/protocols/dicom.md` - DICOM encoding specifications

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Owner:** DICOM Parser - Binary I/O
**Compliance:** DICOM Standard PS3.5 (Data Structures and Encoding)
**Status:** Active
