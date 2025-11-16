# Controls Definition
**UUID:** ffc7439d-b42e-414d-ad69-2a9e254f8d1b
**ISA-95 Level:** L4 Business
**Directory:** `/collab/queries/`

## Overview

This directory represents a control area in the system hierarchy. It contains interfaces for PLC logic, HMI panels, and SCADA monitoring specific to the `queries` subsystem.

## Control Pathways

### PLC (Programmable Logic Controller)
- **Path:** `/collab/queries/plc`
- **Interface:** `collab/queries/plc.html`
- **Scan Time:** N/A
- **Tags:** ~8 process variables
- **Mode:** RUN
- **Logic:** Ladder logic, structured text, function blocks

### HMI (Human-Machine Interface)
- **Path:** `/collab/queries/hmi.html`
- **Type:** Operator interface
- **Screens:** Process overview, alarms, trends, controls
- **Access Level:** Operator, Engineer, Administrator
- **Update Rate:** 1 second

### SCADA (Supervisory Control and Data Acquisition)
- **Path:** `/collab/queries/scada.html`
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
- QUERIES_PLC_Status_Running
- QUERIES_HMI_Alarm_Count
- QUERIES_SCADA_Data_Rate
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
- **Polling Rate:** N/A

## Data Flow

```
Physical Devices (L0)
    ↓
PLC Controllers (L1) - /collab/queries/plc
    ↓
SCADA Systems (L2) - /collab/queries/scada.html
    ↓
MES Layer (L3) - /collab/queries/
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
- **SCADA Refresh:** < N/A
- **Alarm Propagation:** < 500ms
- **Command Execution:** < N/A

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
