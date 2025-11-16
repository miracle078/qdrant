# Controls Directory
**ISA-95 L2 Supervisory** | Control System Structure

## Overview

This directory contains the complete control system structure with SCADA, PLC, HMI, and Tag subsystems.

## Subdirectories

- **scada/** - Supervisory Control and Data Acquisition
- **plc/** - Programmable Logic Controller
- **hmi/** - Human-Machine Interface
- **tags/** - Tag Definitions and Data Points

## Architecture

```
controls/
├── scada/           # L2 - Supervisory control
│   └── index/tag.json
├── plc/             # L1 - Direct control logic
│   └── index/tag.json
├── hmi/             # L2 - Operator interface
│   └── index/tag.json
└── tags/            # L2 - Tag provider
    └── index/tag.json
```

## ISA-95 Hierarchy

- **L2 Supervisory** - SCADA, HMI, Tags
- **L1 Control** - PLC logic execution

## Usage

Navigate to each subdirectory to access the specific control interface.

---

**Auto-generated** by generate_control_structure.py
