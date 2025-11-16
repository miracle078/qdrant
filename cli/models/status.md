# System Status
**UUID:** aea5ea9d-2682-4110-b988-fb6c1a871863
**ISA-95 Level:** L3/L4 Operations
**Directory:** `/cli/models/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** IDLE
- **Health:** DEGRADED
- **Mode:** Automatic
- **Uptime:** 88.4%

### Resource Utilization
- **CPU:** 35%
- **Memory:** 42%
- **Disk:** 49%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** MODELS_PLC_001
- **State:** IDLE
- **Scan Time:** 500ms
- **Last Cycle:** 96ms
- **Faults:** 2

### HMI Status
- **Interface:** MODELS_HMI
- **Connected Users:** 0
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 105ms

### SCADA Status
- **Server:** MODELS_SCADA
- **Tag Count:** 47
- **Update Rate:** 92%
- **Data Quality:** Uncertain
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 2
- **Total:** 2

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 70ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 77 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 90%
- **Quality Rate:** 100.0%

### System Health
- **Response Time:** 91ms
- **Packet Loss:** 0.04%
- **Error Rate:** 0.533%
- **Availability:** 88.4%

## Network Status

### Connections
- **PLC Network:** Connected
- **HMI Network:** Connected
- **SCADA Network:** Connected
- **Database:** Slow

### Protocols
- **OPC UA:** Port 4840 - Active
- **Modbus TCP:** Port 502 - Active
- **EtherNet/IP:** Port 44818 - Active
- **HTTP/HTTPS:** Port 80/443 - Active

## Tag Summary

### Tag Statistics
- **Total Tags:** 92
- **Active Tags:** 50
- **Stale Tags:** 1
- **Bad Quality:** 3

### Tag Categories
- **Status Tags:** 12
- **Process Tags:** 30
- **Alarm Tags:** 10
- **Command Tags:** 4
- **Diagnostic Tags:** 13

## PackML State Machine

### Current State: IDLE

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
- **Duration:** 142 seconds
- **Transitions:** 28
- **Faults:** 2

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 40 minutes
- **Technician:** Operator_3

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 30 minutes
- **Priority:** High

## Diagnostics

### System Checks
- ✅ Configuration Valid
- ✅ Communication Active
- ✅ Tags Updating
- ⚠️ No Active Alarms
- ✅ Historian Recording
- ✅ Backup Current

### Health Indicators
- **Overall:** DEGRADED
- **Hardware:** GOOD
- **Software:** GOOD
- **Network:** DEGRADED
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

**Status Code:** DEGRADED
**Message:** System degraded - check alarms
