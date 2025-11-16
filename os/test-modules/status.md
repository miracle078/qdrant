# System Status
**UUID:** 873f17b7-2b33-4971-a3c0-8a714257c966
**ISA-95 Level:** L3 MES
**Directory:** `/os/test-modules/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** RUNNING
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 99.7%

### Resource Utilization
- **CPU:** 38%
- **Memory:** 48%
- **Disk:** 33%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** TEST-MODULES_PLC_001
- **State:** RUNNING
- **Scan Time:** 500ms
- **Last Cycle:** 47ms
- **Faults:** 0

### HMI Status
- **Interface:** TEST-MODULES_HMI
- **Connected Users:** 2
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 157ms

### SCADA Status
- **Server:** TEST-MODULES_SCADA
- **Tag Count:** 40
- **Update Rate:** 92%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 3
- **Info:** 1
- **Total:** 3

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 99ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 56 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 89%
- **Quality Rate:** 98.0%

### System Health
- **Response Time:** 178ms
- **Packet Loss:** 0.07%
- **Error Rate:** 0.284%
- **Availability:** 99.7%

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
- **Total Tags:** 20
- **Active Tags:** 66
- **Stale Tags:** 0
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 13
- **Process Tags:** 15
- **Alarm Tags:** 8
- **Command Tags:** 2
- **Diagnostic Tags:** 5

## PackML State Machine

### Current State: RUNNING

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
- **Duration:** 87 seconds
- **Transitions:** 11
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 53 minutes
- **Technician:** Operator_3

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 41 minutes
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
