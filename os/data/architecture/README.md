# System Architecture
**Type:** Documentation | Architecture Diagrams

System architecture documentation and diagrams for Chazon.

## Files

- **architecture-map.md** - Complete system component map
- **dependency-graph.md** - Module dependency graph (moved from parent)
- **../architecture-p-and-id.yaml** - P&ID diagram configuration

## Architecture Levels

Following ISA-95 hierarchical model:
- **Level 4** - Business planning
- **Level 3** - Manufacturing operations (SCADA)
- **Level 2** - Supervisory control (PLCs)
- **Level 1** - Basic control (HMI/Tags)
- **Level 0** - Physical process (AI/Data)

## Components

### Gateway Layer
- Root SCADA gateway
- OS gateway

### PLC Layer
10 PLC areas with individual control:
- Backend, Boot, Models, Medical, Data
- Language, Debug, Frontend, Templates, Modules

### Data Layer
- Tag providers (MQTT/OPC UA/Modbus)
- SQL databases
- Vector database (Qdrant)
- ONNX models

## See Also

- `../../README.md` - OS overview
- `../../controls/tag-providers/` - Tag system
- `../../../docs/standards/` - ISA standards
