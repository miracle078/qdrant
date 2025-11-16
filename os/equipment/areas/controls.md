# Controls Definition
**UUID:** 45aa622e-4407-4019-89ba-65b77607c401
**ISA-95 Level:** L3 MES
**Directory:** `/os/equipment/areas/`

## Overview

This directory represents a control area in the system hierarchy. It contains interfaces for PLC logic, HMI panels, and SCADA monitoring specific to the `areas` subsystem.

## Control Pathways

### PLC (Programmable Logic Controller)
- **Path:** `/os/equipment/areas/plc`
- **Interface:** `os/equipment/areas/plc.html`
- **Scan Time:** 500ms-1s
- **Tags:** ~8 process variables
- **Mode:** RUN
- **Logic:** Ladder logic, structured text, function blocks

### HMI (Human-Machine Interface)
- **Path:** `/os/equipment/areas/hmi.html`
- **Type:** Operator interface
- **Screens:** Process overview, alarms, trends, controls
- **Access Level:** Operator, Engineer, Administrator
- **Update Rate:** 1 second

### SCADA (Supervisory Control and Data Acquisition)
- **Path:** `/os/equipment/areas/scada.html`
- **Type:** Supervisory monitoring
- **Data Points:** All PLC tags + calculated values
- **Historian:** Time-series data storage
- **Alarms:** Priority-based notification system
- **Trends:** Real-time and historical

## Tag Structure

### Naming Convention
```
{area}_{device}_{parameter}_{attribute}

Examples:
- AREAS_PLC_Status_Running
- AREAS_HMI_Alarm_Count
- AREAS_SCADA_Data_Rate
```

### Tag Categories
1. **Status Tags** - System state and health
2. **Process Tags** - Real-time process variables
3. **Alarm Tags** - Fault and warning conditions
4. **Command Tags** - Operator commands and setpoints
5. **Diagnostic Tags** - Performance and debugging data

## Communication Protocols

### Internal (L2-L3)
- **Protocol:** OPC UA
- **Port:** 4840
- **Security:** Certificate-based authentication
- **Encryption:** AES-256

### External (L1-L2)
- **Protocol:** Modbus TCP, Ethernet/IP
- **Port:** 502 (Modbus), 44818 (EtherNet/IP)
- **Polling Rate:** 500ms-1s

## Data Flow

```
Physical Devices (L0)
    ↓
PLC Controllers (L1) - /os/equipment/areas/plc
    ↓
SCADA Systems (L2) - /os/equipment/areas/scada.html
    ↓
MES Layer (L3) - /os/equipment/areas/
    ↓
Business Layer (L4)
```

## Control Logic

### State Machine
The control system uses PackML (ISA-88) state machine:

- **IDLE** - Ready to start
- **STARTING** - Initialization sequence
- **EXECUTE** - Normal operation
- **COMPLETING** - Finishing current cycle
- **COMPLETE** - Cycle complete
- **STOPPING** - Controlled shutdown
- **STOPPED** - Safe state
- **ABORTING** - Emergency stop
- **ABORTED** - Fault state

### Interlocks
Safety and operational interlocks prevent unsafe conditions:
- Emergency stop circuits
- Permission-based sequences
- Dependency checks
- Timeout protection

## Access Control

### Permission Levels
1. **View Only** - Monitor status and data
2. **Operator** - Acknowledge alarms, start/stop processes
3. **Engineer** - Modify setpoints, tune parameters
4. **Administrator** - Configure system, manage users

### Audit Trail
All control actions are logged with:
- Timestamp
- User identification
- Action performed
- Previous/new values
- System response

## Integration Points

### Upstream (Supervisory)
- Receives setpoints and commands
- Reports status and alarms
- Sends process data for analysis

### Downstream (Control)
- Sends commands to PLCs
- Receives sensor data
- Monitors equipment health

### Peer (Lateral)
- Coordinates with other control areas
- Shares process variables
- Synchronizes operations

## Performance Metrics

### Response Time
- **HMI Update:** < 1 second
- **SCADA Refresh:** < 500ms-1s
- **Alarm Propagation:** < 500ms
- **Command Execution:** < 500ms-1s

### Reliability
- **Uptime Target:** 99.9%
- **Mean Time Between Failures:** > 10,000 hours
- **Recovery Time:** < 5 minutes

### Data Quality
- **Accuracy:** ±0.1% of range
- **Precision:** 0.01% resolution
- **Availability:** 99.99%

## Maintenance

### Backup Schedule
- **PLC Program:** Daily
- **HMI Screens:** Weekly
- **SCADA Configuration:** Weekly
- **Historical Data:** Continuous

### Update Procedures
1. Test in development environment
2. Create backup of current configuration
3. Schedule maintenance window
4. Deploy changes
5. Verify operation
6. Document changes

## Related Files

- `README.md` - General area documentation
- `plc.html` - PLC interface
- `hmi.html` - HMI interface
- `scada.html` - SCADA interface
- `index.html` - Area gateway (if applicable)

## References

- ISA-95: Enterprise-Control System Integration
- ISA-88: Batch Control (PackML)
- ISA-101: HMI Design Guidelines
- OPC UA: IEC 62541 Standard
