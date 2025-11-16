# System Status
**UUID:** 9a4e8f39-2866-4daf-aee9-e2ed67947846
**ISA-95 Level:** L4 Business
**Directory:** `/docs/planning/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 90.3%

### Resource Utilization
- **CPU:** 44%
- **Memory:** 20%
- **Disk:** 60%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** PLANNING_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 58ms
- **Faults:** 0

### HMI Status
- **Interface:** PLANNING_HMI
- **Connected Users:** 2
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 74ms

### SCADA Status
- **Server:** PLANNING_SCADA
- **Tag Count:** 26
- **Update Rate:** 87%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 1
- **Info:** 1
- **Total:** 1

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 59ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 60 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 82%
- **Quality Rate:** 97.0%

### System Health
- **Response Time:** 170ms
- **Packet Loss:** 0.04%
- **Error Rate:** 0.011%
- **Availability:** 90.3%

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
- **Total Tags:** 74
- **Active Tags:** 15
- **Stale Tags:** 4
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 15
- **Process Tags:** 33
- **Alarm Tags:** 9
- **Command Tags:** 5
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
- **Entry Time:** 01:51:02
- **Duration:** 95 seconds
- **Transitions:** 40
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 11 minutes
- **Technician:** Operator_5

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 37 minutes
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
