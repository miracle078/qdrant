# P&ID System
**Type:** Template System | Process Flow Diagrams

Generate P&ID (Piping and Instrumentation Diagram) from YAML configuration.

## Overview

P&ID diagrams visualize:
- **Process flow** - Data/control flow between components
- **Instrumentation** - Sensors, actuators, controllers
- **Control loops** - Feedback and feedforward control
- **Protocols** - Communication methods (MQTT, OPC UA, Modbus)
- **Interfaces** - System boundaries

## Files

- `symbols.md` - ISA-5.1 symbol definitions
- `config-schema.md` - YAML configuration format
- `renderer.md` - JavaScript rendering engine
- `../p-and-id-template.md` - Complete integrated template

## Quick Start

```yaml
# my-system.yaml
title: "My System P&ID"
components:
  - id: PLC_001
    type: PLC
    name: "Main Controller"
    
connections:
  - from: PLC_001
    to: HMI_001
    protocol: "MQTT"
```

## Standards

- **ISA-5.1** - Instrumentation symbols
- **ISA-95** - Enterprise-control integration
- **ISA-88** - Batch control standards

## See Also

- `../../../data/architecture-p-and-id.yaml` - Chazon system P&ID
- `../../docs/standards/isa/` - ISA standards documentation
