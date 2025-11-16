# System Status
**UUID:** 1477c35c-9b6c-4a9d-bc1f-33f76d7e4ad4
**ISA-95 Level:** L4 Business
**Directory:** `/collab/3d-worlds/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 94.0%

### Resource Utilization
- **CPU:** 21%
- **Memory:** 31%
- **Disk:** 51%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** 3D-WORLDS_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 94ms
- **Faults:** 0

### HMI Status
- **Interface:** 3D-WORLDS_HMI
- **Connected Users:** 0
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 125ms

### SCADA Status
- **Server:** 3D-WORLDS_SCADA
- **Tag Count:** 28
- **Update Rate:** 94%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 0
- **Total:** 0

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 72ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 66 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 93%
- **Quality Rate:** 98.0%

### System Health
- **Response Time:** 104ms
- **Packet Loss:** 0.14%
- **Error Rate:** 0.263%
- **Availability:** 94.0%

## Network Status

### Connections
- **PLC Network:** Connected
- **HMI Network:** Connected
- **SCADA Network:** Connected
- **Database:** Connected

### Protocols
- **OPC UA:** Port 4840 - Active
- **Modbus TCP:** Port 502 - Active
- **EtherNet/IP:** Port 44818 - Active
- **HTTP/HTTPS:** Port 80/443 - Active

## Tag Summary

### Tag Statistics
- **Total Tags:** 31
- **Active Tags:** 80
- **Stale Tags:** 4
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 10
- **Process Tags:** 31
- **Alarm Tags:** 6
- **Command Tags:** 2
- **Diagnostic Tags:** 5

## PackML State Machine

### Current State: ACTIVE

```
IDLE → STARTING → EXECUTE → COMPLETING → COMPLETE
                     ↑
                  [CURRENT]

Alternative States:
- STOPPING → STOPPED
- ABORTING → ABORTED
- HOLDING → HELD
```

### State Details
- **Entry Time:** 01:51:10
- **Duration:** 259 seconds
- **Transitions:** 34
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 49 minutes
- **Technician:** Operator_3

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 18 minutes
- **Priority:** Normal

## Diagnostics

### System Checks
- ✅ Configuration Valid
- ✅ Communication Active
- ✅ Tags Updating
- ✅ No Active Alarms
- ✅ Historian Recording
- ✅ Backup Current

### Health Indicators
- **Overall:** HEALTHY
- **Hardware:** GOOD
- **Software:** GOOD
- **Network:** GOOD
- **Storage:** GOOD

## Quick Actions

### Available Commands
- `START` - Start operation
- `STOP` - Stop operation
- `RESET` - Reset faults
- `ACKNOWLEDGE` - Acknowledge alarms
- `REFRESH` - Refresh display

### Navigation
- `plc.html` - PLC interface
- `hmi.html` - HMI panel
- `scada.html` - SCADA overview
- `controls.md` - Control definitions
- `README.md` - Documentation

## Related Files

- **Controls:** `controls.md` - PLC/HMI/SCADA pathways
- **Documentation:** `README.md` - Area overview
- **Interfaces:** `plc.html`, `hmi.html`, `scada.html`
- **Configuration:** System configuration files

---

**Status Code:** HEALTHY
**Message:** System operating normally
