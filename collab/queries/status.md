# System Status
**UUID:** 6cf49839-84ff-4921-9704-4d59c2ea8576
**ISA-95 Level:** L4 Business
**Directory:** `/collab/queries/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 99.5%

### Resource Utilization
- **CPU:** 10%
- **Memory:** 37%
- **Disk:** 60%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** QUERIES_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 52ms
- **Faults:** 0

### HMI Status
- **Interface:** QUERIES_HMI
- **Connected Users:** 1
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 94ms

### SCADA Status
- **Server:** QUERIES_SCADA
- **Tag Count:** 15
- **Update Rate:** 94%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 2
- **Total:** 0

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 56ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 58 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 93%
- **Quality Rate:** 97.0%

### System Health
- **Response Time:** 105ms
- **Packet Loss:** 0.47%
- **Error Rate:** 0.404%
- **Availability:** 99.5%

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
- **Total Tags:** 25
- **Active Tags:** 50
- **Stale Tags:** 1
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 12
- **Process Tags:** 38
- **Alarm Tags:** 7
- **Command Tags:** 2
- **Diagnostic Tags:** 13

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
- **Duration:** 248 seconds
- **Transitions:** 15
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 57 minutes
- **Technician:** Operator_4

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 21 minutes
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
