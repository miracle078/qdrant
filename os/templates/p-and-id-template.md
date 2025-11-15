# P&ID Template System
**UUID:** template-p-and-id-v1
**Type:** Template | Process Flow Diagram Generator

Generate P&ID (Piping and Instrumentation Diagram) from markdown configuration.

## Overview

P&ID diagrams show:
- **Process flow** - Data/control flow between components
- **Instrumentation** - Sensors, actuators, controllers
- **Control loops** - Feedback and feedforward control
- **Protocols** - Communication methods
- **Interfaces** - System boundaries

## P&ID Symbols (ISA-5.1 Standard)

```
Instruments:
  [AT]  - Analyzer/Transmitter
  [FT]  - Flow Transmitter
  [PT]  - Pressure Transmitter
  [TT]  - Temperature Transmitter
  [LT]  - Level Transmitter

Controllers:
  [PID] - PID Controller
  [PLC] - Programmable Logic Controller
  [HMI] - Human-Machine Interface

Equipment:
  [P]   - Pump
  [V]   - Valve
  [T]   - Tank
  [R]   - Reactor
  [M]   - Motor
```

## Chazon Architecture P&ID

```yaml
# architecture-p-and-id.yaml
title: "Chazon Medical Imaging Factory - P&ID"
version: "1.0"
date: "2025-11-15"

# Define components
components:
  - id: SCADA_GATEWAY
    type: HMI
    tag: HMI-001
    name: "SCADA Gateway"
    location: "Root"
    description: "Master control interface"

  - id: OS_GATEWAY
    type: HMI
    tag: HMI-002
    name: "Chazon OS Gateway"
    location: "os/"
    description: "Operating system interface"

  - id: PLC_MODULES
    type: PLC
    tag: PLC-001
    name: "Module System PLC"
    location: "os/modules/"
    description: "Controls 114 markdown modules"
    scan_time: "60ms"

  - id: PLC_BOOT
    type: PLC
    tag: PLC-002
    name: "Boot Sequencer PLC"
    location: "os/boot/"
    description: "6-phase initialization"
    scan_time: "50ms"

  - id: PLC_MEDICAL
    type: PLC
    tag: PLC-003
    name: "Medical Imaging PLC"
    location: "os/medical/"
    description: "DICOM, AlF-DETECT control"
    scan_time: "80ms"

  - id: DB_TOKEN
    type: Database
    tag: DB-001
    name: "Token Database"
    location: "os/data/"
    description: "SQL token storage"

  - id: DB_QDRANT
    type: Database
    tag: DB-002
    name: "Qdrant Vector DB"
    location: "External"
    description: "Medical image embeddings"

  - id: AI_MODELS
    type: Processor
    tag: AI-001
    name: "AI Inference Engine"
    location: "os/models/"
    description: "ONNX Runtime + WebGPU"

  - id: COMPILER
    type: Processor
    tag: COMP-001
    name: "MD Compiler"
    location: "os/modules/"
    description: "Markdown to executable"

# Define connections (process flow)
connections:
  - from: SCADA_GATEWAY
    to: OS_GATEWAY
    protocol: HTTP
    data_type: "Navigation requests"
    line_type: "signal"

  - from: OS_GATEWAY
    to: PLC_MODULES
    protocol: WebSocket
    data_type: "Control commands"
    line_type: "signal"
    bidirectional: true

  - from: PLC_BOOT
    to: PLC_MODULES
    protocol: "Module Router (UUID)"
    data_type: "Module load requests"
    line_type: "process"

  - from: PLC_MODULES
    to: COMPILER
    protocol: "Function call"
    data_type: "Markdown source"
    line_type: "process"

  - from: COMPILER
    to: PLC_MODULES
    protocol: "Return value"
    data_type: "Compiled code"
    line_type: "process"

  - from: PLC_MODULES
    to: DB_TOKEN
    protocol: "SQL"
    data_type: "Module metadata"
    line_type: "data"

  - from: PLC_MEDICAL
    to: AI_MODELS
    protocol: "ONNX API"
    data_type: "Medical images"
    line_type: "process"

  - from: AI_MODELS
    to: DB_QDRANT
    protocol: "gRPC"
    data_type: "Vector embeddings"
    line_type: "data"

  - from: PLC_MEDICAL
    to: DB_QDRANT
    protocol: "REST API"
    data_type: "Similarity search"
    line_type: "data"
    bidirectional: true

# Define control loops
control_loops:
  - name: "Boot Sequence Control"
    controller: PLC_BOOT
    setpoint: "6 phases complete"
    process_variable: "current phase"
    manipulated_variable: "phase execution"
    measurement: "phase status"
    type: "Sequential"

  - name: "Module Load Balancing"
    controller: PLC_MODULES
    setpoint: "Optimal memory usage"
    process_variable: "modules loaded"
    manipulated_variable: "cache eviction"
    measurement: "memory usage"
    type: "PID"

  - name: "Inference Queue Management"
    controller: AI_MODELS
    setpoint: "Target latency <100ms"
    process_variable: "queue depth"
    manipulated_variable: "batch size"
    measurement: "inference time"
    type: "Feedforward"

# Define instrumentation
instruments:
  - tag: AT-001
    type: "Analyzer/Transmitter"
    location: "os/modules/"
    measures: "Module performance"
    range: "0-1000 modules"
    output: "4-20mA to PLC-001"

  - tag: FT-001
    type: "Flow Transmitter"
    location: "os/medical/"
    measures: "Studies per hour"
    range: "0-100 studies/hr"
    output: "MQTT to SCADA"

  - tag: PT-001
    type: "Pressure Transmitter"
    location: "os/models/"
    measures: "GPU memory pressure"
    range: "0-100%"
    output: "WebSocket to HMI"

# Protocol definitions
protocols:
  HTTP:
    port: 8080
    encryption: false

  WebSocket:
    port: 8080
    path: "/ws"

  MQTT:
    broker: "localhost:1883"
    qos: 1

  SQL:
    driver: "sqlite3"
    connection: "os/data/tokendb.sql"

  gRPC:
    port: 6334
    service: "Qdrant"
```

## Rendering Engine

```javascript
class PIDRenderer {
  constructor(config) {
    this.config = config;
    this.canvas = document.getElementById('pid-canvas');
    this.ctx = this.canvas.getContext('2d');
  }

  render() {
    this.drawComponents();
    this.drawConnections();
    this.drawInstruments();
    this.drawLegend();
  }

  drawComponents() {
    this.config.components.forEach(comp => {
      const { x, y, type } = this.getPosition(comp.id);

      switch(comp.type) {
        case 'PLC':
          this.drawPLC(x, y, comp.tag, comp.name);
          break;
        case 'HMI':
          this.drawHMI(x, y, comp.tag, comp.name);
          break;
        case 'Database':
          this.drawDatabase(x, y, comp.tag, comp.name);
          break;
        case 'Processor':
          this.drawProcessor(x, y, comp.tag, comp.name);
          break;
      }
    });
  }

  drawPLC(x, y, tag, name) {
    // Draw PLC symbol (rectangle with diagonal corners)
    this.ctx.strokeStyle = '#00ff88';
    this.ctx.lineWidth = 2;
    this.ctx.strokeRect(x, y, 100, 60);

    // Draw diagonal corners
    this.ctx.beginPath();
    this.ctx.moveTo(x, y);
    this.ctx.lineTo(x + 10, y + 10);
    this.ctx.moveTo(x + 100, y);
    this.ctx.lineTo(x + 90, y + 10);
    this.ctx.stroke();

    // Draw tag and name
    this.ctx.fillStyle = '#00ff88';
    this.ctx.font = '12px Courier New';
    this.ctx.fillText(tag, x + 10, y - 5);
    this.ctx.fillText(name, x + 10, y + 35);
  }

  drawConnections() {
    this.config.connections.forEach(conn => {
      const from = this.getPosition(conn.from);
      const to = this.getPosition(conn.to);

      // Draw line
      this.ctx.strokeStyle = this.getLineColor(conn.line_type);
      this.ctx.lineWidth = conn.line_type === 'process' ? 3 : 1;
      this.ctx.beginPath();
      this.ctx.moveTo(from.x + 50, from.y + 30);
      this.ctx.lineTo(to.x + 50, to.y + 30);
      this.ctx.stroke();

      // Draw arrow
      this.drawArrow(to.x + 50, to.y + 30);

      // Draw protocol label
      this.ctx.fillStyle = '#00ccff';
      this.ctx.font = '10px Courier New';
      const midX = (from.x + to.x) / 2;
      const midY = (from.y + to.y) / 2;
      this.ctx.fillText(conn.protocol, midX, midY - 5);
    });
  }

  getLineColor(type) {
    switch(type) {
      case 'process': return '#00ff88';  // Green - process flow
      case 'signal': return '#00ccff';   // Blue - control signal
      case 'data': return '#ffaa00';     // Orange - data flow
      default: return '#888';
    }
  }
}

// Usage
const renderer = new PIDRenderer(configFromYAML);
renderer.render();
```

## SVG Export

```javascript
function exportSVG(config) {
  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800">
      <defs>
        <style>
          .plc { fill: none; stroke: #00ff88; stroke-width: 2; }
          .hmi { fill: none; stroke: #00ccff; stroke-width: 2; }
          .process-line { stroke: #00ff88; stroke-width: 3; }
          .signal-line { stroke: #00ccff; stroke-width: 1; }
        </style>
      </defs>
      ${generateSVGElements(config)}
    </svg>
  `;
  return svg;
}
```

## See Also

- `../modules/template-engine.md` - Template compilation
- `../../docs/standards/isa/isa-5.1/` - P&ID symbols standard (planned)
- `architecture-p-and-id.yaml` - Chazon system P&ID
