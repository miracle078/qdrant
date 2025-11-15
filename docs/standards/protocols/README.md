# Communication Protocols
**Industrial Automation & IoT Standards**

Communication protocols used in the Chazon factory automation architecture.

## Protocol Overview

| Protocol | Layer | Speed | Use Case |
|----------|-------|-------|----------|
| **MQTT** | Application | Varies | Pub/Sub messaging, IoT |
| **OPC UA** | Application | 1-100 Mbps | Unified automation |
| **Modbus TCP** | Application/Transport | 10-100 Mbps | PLC communication |
| **EtherNet/IP** | Application/Network | 10-1000 Mbps | Industrial ethernet |
| **Profibus** | Fieldbus | 9.6 Kbps - 12 Mbps | Field devices |
| **BACnet** | Application | Varies | Building automation |
| **WebSocket** | Application | Varies | Real-time web apps |

## Chazon Protocol Usage

```
┌─────────────────────────────────────────────────┐
│  Level 4: Business Planning (ERP)              │
│  Protocol: HTTPS/REST, GraphQL                 │
└────────────────┬────────────────────────────────┘
                 │ HTTP/REST
┌────────────────┴────────────────────────────────┐
│  Level 3: MES/SCADA Gateway                    │
│  Protocol: WebSocket, MQTT, OPC UA             │
└────────────────┬────────────────────────────────┘
                 │ MQTT/WebSocket
┌────────────────┴────────────────────────────────┐
│  Level 2: Supervisory Control                  │
│  Protocol: OPC UA, Modbus TCP, MQTT            │
└────────────────┬────────────────────────────────┘
                 │ Modbus TCP / EtherNet/IP
┌────────────────┴────────────────────────────────┐
│  Level 1: Control (PLCs)                       │
│  Protocol: Modbus RTU, Profibus, EtherNet/IP   │
└────────────────┬────────────────────────────────┘
                 │ Profibus / Fieldbus
┌────────────────┴────────────────────────────────┐
│  Level 0: Field Devices (Sensors/Actuators)    │
│  Protocol: 4-20mA, Digital I/O, Hart           │
└─────────────────────────────────────────────────┘
```

## Protocol Details

See subdirectories for detailed specifications:
- `mqtt/` - MQTT v3.1.1 and v5.0
- `opc-ua/` - OPC Unified Architecture
- `modbus/` - Modbus TCP/RTU
- `ethernet-ip/` - EtherNet/IP (CIP)
- `profibus/` - Profibus DP/PA
- `bacnet/` - BACnet MS/TP and IP
- `websocket/` - WebSocket protocol
