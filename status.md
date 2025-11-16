# System Status
**UUID:** c38ade2d-90ab-4088-8d55-f18b7d9cf378
**ISA-95 Level:** L4 Business
**Directory:** `/./`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 92.5%

### Resource Utilization
- **CPU:** 43%
- **Memory:** 52%
- **Disk:** 80%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** QDRANT_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 67ms
- **Faults:** 0

### HMI Status
- **Interface:** QDRANT_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 61ms

### SCADA Status
- **Server:** QDRANT_SCADA
- **Tag Count:** 41
- **Update Rate:** 92%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 0
- **Total:** 0

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 48ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 54 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 89%
- **Quality Rate:** 99.0%

### System Health
- **Response Time:** 190ms
- **Packet Loss:** 0.21%
- **Error Rate:** 0.250%
- **Availability:** 92.5%

## Network Status

### Connections
- **PLC Network:** Degraded
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
- **Total Tags:** 15
- **Active Tags:** 87
- **Stale Tags:** 1
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 5
- **Process Tags:** 39
- **Alarm Tags:** 6
- **Command Tags:** 3
- **Diagnostic Tags:** 11

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
- **Entry Time:** 01:51:02
- **Duration:** 280 seconds
- **Transitions:** 47
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 19 minutes
- **Technician:** Operator_2

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 22 minutes
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
- **Storage:** WARNING

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
