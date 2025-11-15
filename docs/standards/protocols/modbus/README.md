# Modbus
**Simple Industrial Protocol - RTU and TCP**

## Overview

Modbus is a serial communication protocol for connecting industrial electronic devices. Originally developed for PL Cs, it's now widely used in building management and industrial automation.

## Variants

- **Modbus RTU** - Serial (RS-232, RS-485)
- **Modbus TCP** - Ethernet
- **Modbus ASCII** - Serial (rarely used)

## Modbus in Chazon

**Use Cases:**
- PLC area status monitoring
- Simple sensor/actuator communication
- Legacy system integration
- Lightweight M2M communication

**Port:** 502 (Modbus TCP)

## Data Model

Modbus has 4 data tables:

| Table | Type | Access | Size |
|-------|------|--------|------|
| Coils | Discrete Output | Read/Write | 1 bit |
| Discrete Inputs | Discrete Input | Read | 1 bit |
| Input Registers | Analog Input | Read | 16 bit |
| Holding Registers | Analog Output | Read/Write | 16 bit |

## Chazon Register Map

### Holding Registers (Read/Write)

| Address | Name | Type | Unit | Description |
|---------|------|------|------|-------------|
| 40001 | PLC_MODULES_SCAN_TIME | UINT16 | ms | Scan time for PLC-001 |
| 40002 | PLC_BOOT_SCAN_TIME | UINT16 | ms | Scan time for PLC-002 |
| 40003 | PLC_MODELS_SCAN_TIME | UINT16 | ms | Scan time for PLC-003 |
| 40004 | PLC_MEDICAL_SCAN_TIME | UINT16 | ms | Scan time for PLC-004 |
| 40010 | MODULES_LOADED_COUNT | UINT16 | - | Number of modules loaded |
| 40011-40012 | MODULES_MEMORY_USAGE | FLOAT32 | MB | Memory usage (2 registers) |
| 40020 | BOOT_CURRENT_PHASE | UINT16 | - | Current boot phase (0-5) |
| 40021 | BOOT_STATUS | UINT16 | - | 0=IDLE, 1=RUNNING, 2=COMPLETE |
| 40030 | AI_INFERENCE_QUEUE | UINT16 | - | Queue depth |
| 40031-40032 | AI_AVG_LATENCY | FLOAT32 | ms | Average inference latency |

### Input Registers (Read-Only)

| Address | Name | Type | Unit | Description |
|---------|------|------|------|-------------|
| 30001 | SYSTEM_UPTIME | UINT16 | min | System uptime (rolls over) |
| 30002 | TOTAL_REQUESTS | UINT16 | - | Total API requests |
| 30010 | CPU_USAGE | UINT16 | % | CPU usage percentage |
| 30011 | MEMORY_TOTAL | UINT16 | MB | Total system memory |
| 30012 | MEMORY_USED | UINT16 | MB | Used system memory |

### Coils (Read/Write)

| Address | Name | Description |
|---------|------|-------------|
| 00001 | ENABLE_MODULE_AUTOLOAD | Auto-load modules on boot |
| 00002 | ENABLE_CACHE | Enable module caching |
| 00003 | ENABLE_AI_INFERENCE | Enable AI inference engine |
| 00004 | ENABLE_QDRANT | Enable Qdrant vector search |
| 00010 | BOOT_QUICK_MODE | Quick boot (skip non-essential phases) |
| 00011 | DEBUG_MODE | Enable debug logging |

### Discrete Inputs (Read-Only)

| Address | Name | Description |
|---------|------|-------------|
| 10001 | PLC_MODULES_RUNNING | PLC-001 is running |
| 10002 | PLC_BOOT_RUNNING | PLC-002 is running |
| 10003 | PLC_MODELS_RUNNING | PLC-003 is running |
| 10004 | PLC_MEDICAL_RUNNING | PLC-004 is running |
| 10010 | BOOT_PHASE_0_COMPLETE | Phase 0 complete |
| 10011 | BOOT_PHASE_1_COMPLETE | Phase 1 complete |
| 10012 | BOOT_PHASE_2_COMPLETE | Phase 2 complete |
| 10013 | BOOT_PHASE_3_COMPLETE | Phase 3 complete |
| 10014 | BOOT_PHASE_4_COMPLETE | Phase 4 complete |
| 10015 | BOOT_PHASE_5_COMPLETE | Phase 5 complete |

## Example: Read PLC Scan Times

```javascript
const ModbusRTU = require('modbus-serial');
const client = new ModbusRTU();

await client.connectTCP('localhost', { port: 502 });
client.setID(1);

// Read holding registers 40001-40004 (4 registers)
const data = await client.readHoldingRegisters(40001, 4);

console.log('PLC Scan Times:');
console.log('  PLC-001 (Modules):', data.data[0], 'ms');
console.log('  PLC-002 (Boot):', data.data[1], 'ms');
console.log('  PLC-003 (Models):', data.data[2], 'ms');
console.log('  PLC-004 (Medical):', data.data[3], 'ms');
```

## Example: Check Boot Progress

```javascript
// Read current phase and status
const phase = await client.readHoldingRegisters(40020, 1);
const status = await client.readHoldingRegisters(40021, 1);

// Read phase completion bits
const completion = await client.readDiscreteInputs(10010, 6);

console.log('Boot Status:');
console.log('  Current Phase:', phase.data[0]);
console.log('  Status:', ['IDLE', 'RUNNING', 'COMPLETE'][status.data[0]]);
console.log('  Phases Complete:', completion.data.filter(b => b).length, '/6');
```

## Example: Enable AI Inference

```javascript
// Write to coil 00003
await client.writeCoil(3, true);
console.log('AI Inference enabled');
```

## Function Codes

| Code | Name | Description |
|------|------|-------------|
| 01 | Read Coils | Read 1-2000 coils |
| 02 | Read Discrete Inputs | Read 1-2000 inputs |
| 03 | Read Holding Registers | Read 1-125 registers |
| 04 | Read Input Registers | Read 1-125 registers |
| 05 | Write Single Coil | Write 1 coil |
| 06 | Write Single Register | Write 1 register |
| 15 | Write Multiple Coils | Write 1-1968 coils |
| 16 | Write Multiple Registers | Write 1-123 registers |

## Configuration

```yaml
# modbus-config.yaml
modbus_tcp:
  port: 502
  unit_id: 1
  timeout: 5000  # ms

register_map:
  holding_registers:
    start_address: 40001
    count: 100

  input_registers:
    start_address: 30001
    count: 50

  coils:
    start_address: 1
    count: 20

  discrete_inputs:
    start_address: 10001
    count: 20
```
