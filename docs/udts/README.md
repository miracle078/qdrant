# UDT Documentation (User Defined Types)
**ISA-95 L4 Business** | Data Structure Definitions

## Overview

This directory contains User Defined Types (UDTs) that define structured data templates for all system pages and components. Following industrial automation best practices from PLC/SCADA systems, UDTs provide:

- **Standardized data structures** across all directories
- **Tag-based information storage** (like PLC tag providers)
- **Template-driven page generation** using structured JSON data
- **Type safety and validation** for consistent data formats

## What are UDTs?

In industrial automation (Rockwell, Siemens, etc.), User Defined Types are custom data structures that:

1. **Define tag structures** - Specify what data points (tags) exist and their types
2. **Enable reusability** - Same template used across multiple instances
3. **Provide type safety** - Ensure data consistency and validation
4. **Support nested types** - Complex structures from simpler ones

### Example: Traditional PLC UDT

```
UDT: MotorControl
  - Running: BOOL
  - Speed: REAL (RPM)
  - Current: REAL (Amps)
  - Temperature: REAL (°C)
  - Faults: ARRAY[1..10] OF Alarm
```

### Our Implementation

We apply this concept to our file system, where each directory has structured tag data:

```json
{
  "UUID": "2a5a7fc3-d3c5-4753-8e28-7da4bac60d2c",
  "ISA_Level": "L3_MES",
  "Title": "Backend",
  "Features": [...],
  "Has_PLC": true,
  "PLC_Path": "/os/backend/plc.html"
}
```

## Available UDTs

### 1. IndexTemplate (`index-template.yaml`)

**Purpose**: Universal directory index structure
**Location**: `{directory}/index/tag.json`
**Loader**: `{directory}/index.html` (generic JavaScript loader)

**Key Tag Groups**:
- **Identity Tags**: UUID, ISA_Level, Directory_Path
- **Metadata Tags**: Title, Description, Icon, Color_Scheme
- **Navigation Tags**: Parent_Path, Child_Directories, Sibling_Directories
- **Documentation Tags**: README_Path, Controls_Path, Status_Path
- **Interface Tags**: Has_PLC, Has_HMI, Has_SCADA (+ paths)
- **Content Tags**: Features, Quick_Actions, Related_Files

**Color Schemes by ISA-95 Level**:
- `L4_Business`: Green (#00ff88)
- `L3_MES`: Blue (#00ccff)
- `L2_Supervisory`: Purple (#ff88ff)
- `L1_Control`: Orange (#ffaa00)
- `L0_Physical`: Red (#ff6666)

### 2. PageTemplates (`page-templates.yaml`)

Collection of UDTs for different page types:

#### ControlsTemplate
- **Purpose**: PLC/HMI/SCADA control system definitions
- **File**: `controls.md`
- **Tags**: PLC_Scan_Time, Tag_Count, Protocols, PackML_State

#### StatusTemplate
- **Purpose**: Real-time operational status monitoring
- **File**: `status.md`
- **Tags**: Operational_Status, Health, CPU_Usage, Memory_Usage, Active_Alarms

#### ScadaTemplate
- **Purpose**: Supervisory Control and Data Acquisition interface
- **File**: `scada.html`
- **Tags**: Tag_Provider, Update_Rate, Data_Points, Historian_Status

#### HmiTemplate
- **Purpose**: Human-Machine Interface panel
- **File**: `hmi.html`
- **Tags**: Screen_Count, Access_Level, Update_Rate, Connected_Users

#### PlcTemplate
- **Purpose**: Programmable Logic Controller interface
- **File**: `plc.html`
- **Tags**: Controller_Name, Scan_Time, Program_State, Tag_Count, Logic_Type

## How It Works

### 1. Data Storage (Tags)

Each directory has an `index/` subdirectory containing structured tag data:

```
/os/backend/
├── index/
│   └── tag.json          # Structured data following IndexTemplate UDT
├── index.html            # Generic loader (reads tag.json)
├── controls.md           # Controls definition
├── status.md             # Status monitoring
├── plc.html              # PLC interface
├── hmi.html              # HMI interface
└── scada.html            # SCADA interface
```

### 2. Generic Loaders

Instead of hardcoding HTML for each directory, we use generic loaders that:

1. **Fetch** the tag data from `index/tag.json`
2. **Parse** the JSON structure
3. **Render** the page dynamically based on template
4. **Apply** theming (color scheme, icons, etc.)

This is similar to how SCADA systems use tag providers to populate HMI screens.

### 3. Generation Script

`generate_indexes.py` creates all index directories and tag data:

```bash
python3 generate_indexes.py

# Output:
# ✅ Created index for: os/backend
# ✅ Created index for: os/frontend
# ...
# ✅ Generated 87 index directories with tag data
```

## Benefits of This Approach

### 1. Consistency
- All directories follow the same structure
- Standardized data format across system
- Predictable navigation and UX

### 2. Maintainability
- Update template once, affects all instances
- Data separated from presentation
- Easy to modify structure or styling

### 3. Automation
- Generate indexes programmatically
- Update tag data without touching HTML
- Script-driven content management

### 4. ISA-95 Compliance
- Each directory tagged with ISA level
- Proper hierarchy navigation (L4→L3→L2→L1→L0)
- Follows industrial automation standards

### 5. Scalability
- Add new directories automatically
- Tag data grows with system
- Template-driven means no duplication

## Usage Examples

### Reading Tag Data

```javascript
// In any index.html loader
const response = await fetch('index/tag.json');
const tag = await response.json();

console.log(tag.Title);           // "Backend"
console.log(tag.ISA_Level);       // "L3_MES"
console.log(tag.Has_PLC);         // true
console.log(tag.PLC_Path);        // "/os/backend/plc.html"
```

### Creating Custom UDT

```yaml
# docs/udts/custom-template.yaml
name: CustomTemplate
version: 1.0.0
description: Your custom data structure

tags:
  - name: Custom_Field
    type: STRING
    description: Custom field description
```

### Generating Tag Data

```python
# In generate_indexes.py
tag_data = {
    'UUID': str(uuid.uuid4()),
    'ISA_Level': 'L3_MES',
    'Title': 'Backend',
    'Custom_Field': 'Value'  # Add custom fields
}

with open('index/tag.json', 'w') as f:
    json.dump(tag_data, f, indent=2)
```

## Nested UDTs

UDTs can contain other UDTs (composition):

```yaml
# DirectoryLink UDT (used in IndexTemplate)
DirectoryLink:
  - name: path
    type: STRING
  - name: title
    type: STRING
  - name: description
    type: STRING
  - name: icon
    type: STRING

# Usage in parent UDT
Child_Directories:
  type: ARRAY[DirectoryLink]
```

## Tag Naming Conventions

Following ISA-88 and ISA-95 standards:

- **PascalCase** for tag names: `ISA_Level`, `Directory_Path`
- **SCREAMING_SNAKE_CASE** for enums: `L3_MES`, `L4_BUSINESS`
- **Nested objects** use dot notation: `tag.Features[0].title`
- **Arrays** use descriptive plurals: `Child_Directories`, `Quick_Actions`

## Integration with Control Systems

### Tag Provider Analogy

```
SCADA Tag Provider          →  Our index/ directories
├── Area_Backend_Status     →  os/backend/index/tag.json
├── Area_Frontend_Status    →  os/frontend/index/tag.json
└── Area_Medical_Status     →  os/medical/index/tag.json

HMI Screen                  →  index.html (generic loader)
├── Binds to tag provider   →  Fetches tag.json
├── Displays values         →  Renders from structured data
└── Updates on change       →  Refreshes when data changes
```

### PackML State Mapping

UDTs include PackML states for control areas:

```
Tag: PackML_State
Enum: [IDLE, STARTING, EXECUTE, COMPLETING, COMPLETE,
       STOPPING, STOPPED, ABORTING, ABORTED, HOLDING, HELD]

Status: RUNNING  →  PackML: EXECUTE
Status: STOPPED  →  PackML: STOPPED
Status: FAULT    →  PackML: ABORTED
```

## File Structure

```
docs/udts/
├── README.md                    # This file
├── index-template.yaml          # Index page UDT definition
├── page-templates.yaml          # All page UDTs (controls, status, etc.)
└── examples/
    ├── sample-tag.json          # Example tag data
    └── custom-udt.yaml          # Example custom UDT

{any-directory}/
├── index/
│   └── tag.json                 # Tag data instance (from IndexTemplate)
└── index.html                   # Generic loader

generate_indexes.py              # Generator script (creates all indexes)
```

## Extending the System

### Adding New Tags to IndexTemplate

1. Edit `docs/udts/index-template.yaml`
2. Add new tag definition
3. Update `generate_indexes.py` to populate new tag
4. Regenerate all indexes: `python3 generate_indexes.py`
5. Update generic loader if needed

### Creating New Page Template

1. Create UDT in `docs/udts/page-templates.yaml`
2. Create generator script for that page type
3. Create generic loader HTML
4. Generate instances across directories

## Standards Compliance

### ISA-95 (Enterprise-Control Integration)
- Tags classified by functional hierarchy level
- L4 → L3 → L2 → L1 → L0 navigation structure
- Business to control system integration

### ISA-88 (Batch Control / PackML)
- State machine tags for control areas
- Equipment hierarchy support
- Procedural control integration

### ISA-101 (HMI Design)
- Structured navigation tags
- Alarm priority levels
- Screen hierarchy definitions

### OPC UA
- Tag-based architecture (similar to OPC UA information model)
- Type definitions and instances
- Structured data types

## Troubleshooting

### Index Not Loading

1. Check `index/tag.json` exists
2. Validate JSON syntax: `python3 -m json.tool index/tag.json`
3. Check browser console for errors
4. Verify fetch path is correct

### Missing Tag Data

1. Regenerate: `python3 generate_indexes.py`
2. Check UDT definition has required tags
3. Ensure generator populates all required fields

### Styling Issues

1. Check `Color_Scheme` tag value
2. Verify CSS classes exist for color
3. Ensure generic loader CSS is up to date

## References

- ISA-95: Enterprise-Control System Integration
- ISA-88: Batch Control (PackML)
- Rockwell Automation: User-Defined Data Types
- Siemens: User-Defined Data Types (UDT)
- OPC UA: Information Modeling

---

**Generated**: 2025-11-16
**Version**: 1.0.0
**Maintained by**: Chazon Medical Imaging SCADA System
