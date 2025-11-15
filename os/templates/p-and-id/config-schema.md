# P&ID Configuration Schema
**Type:** Schema | YAML Configuration Format

YAML schema for defining P&ID diagrams.

## Root Structure

```yaml
title: "System Name P&ID"
version: "1.0"
date: "2025-11-15"
components: []
connections: []
control_loops: []
instruments: []
```

## Component Schema

```yaml
components:
  - id: UNIQUE_ID             # Unique identifier
    type: PLC|HMI|DATABASE|AI # Component type
    tag: TAG-001              # ISA tag number
    name: "Component Name"    # Display name
    location: "path/"         # File system location
    description: "..."        # Description
    scan_time: "50ms"         # (Optional) PLC scan time
    coordinates: {x: 100, y: 200}  # Canvas position
```

## Connection Schema

```yaml
connections:
  - from: COMPONENT_ID_1
    to: COMPONENT_ID_2
    protocol: "MQTT|OPC UA|Modbus|WebSocket|gRPC|REST"
    data_type: "Description of data"
    line_type: "process|signal|electric|data"
    flow_rate: "Optional flow rate/throughput"
```

## Control Loop Schema

```yaml
control_loops:
  - name: "Loop Name"
    tag: LOOP-001
    controller: PLC_ID
    setpoint: "Target value"
    process_variable: "Measured variable"
    manipulated_variable: "Control output"
    control_type: "PID|ON-OFF|CASCADING"
    tuning:
      Kp: 1.0
      Ki: 0.5
      Kd: 0.1
```

## Instrument Schema

```yaml
instruments:
  - tag: FT-001
    type: Flow Transmitter
    location: "Line description"
    measurement: "Flow rate"
    unit: "L/min"
    range: "0-100"
    connected_to: PLC_ID
```

## Example: Complete System

```yaml
title: "Medical Imaging Factory - P&ID"
version: "1.0"
date: "2025-11-15"

components:
  - id: PLC_MEDICAL
    type: PLC
    tag: PLC-004
    name: "Medical Imaging PLC"
    location: "os/medical/"
    scan_time: "80ms"
    coordinates: {x: 300, y: 200}

  - id: AI_PROCESSOR
    type: AI
    tag: AI-001
    name: "AlF-DETECT Processor"
    location: "os/medical/alf-detect.html"
    coordinates: {x: 500, y: 200}

  - id: DICOM_DB
    type: DATABASE
    tag: DB-001
    name: "DICOM Storage"
    location: "os/data/dicom/"
    coordinates: {x: 500, y: 400}

connections:
  - from: PLC_MEDICAL
    to: AI_PROCESSOR
    protocol: "WebSocket"
    data_type: "DICOM images"
    line_type: "data"

  - from: AI_PROCESSOR
    to: DICOM_DB
    protocol: "REST"
    data_type: "Analysis results"
    line_type: "data"

control_loops:
  - name: "AI Queue Management"
    tag: LOOP-001
    controller: PLC_MEDICAL
    setpoint: "Queue < 10 studies"
    process_variable: "Inference queue length"
    manipulated_variable: "Processing rate"
    control_type: "PID"

instruments:
  - tag: AT-001
    type: Analyzer/Transmitter
    location: "AlF-DETECT output"
    measurement: "Detection confidence"
    unit: "%"
    range: "0-100"
```

## See Also

- `symbols.md` - ISA-5.1 symbol definitions
- `../../../docs/standards/isa/isa-95/` - ISA-95 architecture levels
