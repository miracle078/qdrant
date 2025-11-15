# ISA Standards
**ISA-95 | ISA-88 | ISA-18.2** | Standards Compliance

Chazon OS implements industrial automation standards for production-ready architecture.

## Available Modules

### [standards.md](standards.md)
ISA-95 automation hierarchy (L0-L4), ISA-88 PackML state machines, ISA-18.2 alarm management.

### [compliance.md](compliance.md)
Regulatory mapping: 21 CFR Part 11 (FDA), EU Annex 11 (GMP), DICOM, HL7.

## ISA-95 Levels

```
L4: Enterprise (ERP)      → Business Planning
L3: Operations (MES)      → Manufacturing Execution
L2: Supervisory (SCADA)   → Supervisory Control
L1: Control (PLC)         → Real-time Control
L0: Field Devices         → Sensors & Actuators
```

## ISA-88 PackML States

```
IDLE → STARTING → EXECUTE → COMPLETE
         ↓
      ABORTING → ABORTED
         ↓
      STOPPING → STOPPED
```

All Chazon OS programs follow PackML lifecycle state machines.
