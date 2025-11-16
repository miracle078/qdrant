# System Status
**UUID:** 5db164b2-56a1-4348-a079-f72e010654dd
**ISA-95 Level:** L3 MES
**Directory:** `/os/backend/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** RUNNING
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 99.5%

### Resource Utilization
- **CPU:** 40%
- **Memory:** 63%
- **Disk:** 51%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** BACKEND_PLC_001
- **State:** RUNNING
- **Scan Time:** 500ms
- **Last Cycle:** 63ms
- **Faults:** 0

### HMI Status
- **Interface:** BACKEND_HMI
- **Connected Users:** 2
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 191ms

### SCADA Status
- **Server:** BACKEND_SCADA
- **Tag Count:** 32
- **Update Rate:** 81%
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
4. `[01:51:02]` Scan cycle - 92ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 52 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 76%
- **Quality Rate:** 100.0%

### System Health
- **Response Time:** 148ms
- **Packet Loss:** 0.06%
- **Error Rate:** 0.831%
- **Availability:** 99.5%

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
- **Total Tags:** 88
- **Active Tags:** 67
- **Stale Tags:** 3
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 14
- **Process Tags:** 10
- **Alarm Tags:** 3
- **Command Tags:** 2
- **Diagnostic Tags:** 6

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
- **Entry Time:** 01:51:02
- **Duration:** 164 seconds
- **Transitions:** 24
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 17 minutes
- **Technician:** Operator_1

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 44 minutes
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
