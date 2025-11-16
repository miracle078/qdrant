# System Status
**UUID:** 1efca88b-486a-4f2f-8b2a-da48b83ab297
**ISA-95 Level:** L2 Supervisory
**Directory:** `/os/controls/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** RUNNING
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 91.9%

### Resource Utilization
- **CPU:** 53%
- **Memory:** 20%
- **Disk:** 79%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** CONTROLS_PLC_001
- **State:** RUNNING
- **Scan Time:** 100ms
- **Last Cycle:** 57ms
- **Faults:** 0

### HMI Status
- **Interface:** CONTROLS_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 78ms

### SCADA Status
- **Server:** CONTROLS_SCADA
- **Tag Count:** 30
- **Update Rate:** 84%
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
4. `[01:51:02]` Scan cycle - 80ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 55 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 90%
- **Quality Rate:** 99.0%

### System Health
- **Response Time:** 168ms
- **Packet Loss:** 0.14%
- **Error Rate:** 0.050%
- **Availability:** 91.9%

## Network Status

### Connections
- **PLC Network:** Degraded
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
- **Total Tags:** 38
- **Active Tags:** 61
- **Stale Tags:** 5
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 5
- **Process Tags:** 20
- **Alarm Tags:** 3
- **Command Tags:** 8
- **Diagnostic Tags:** 15

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
- **Duration:** 133 seconds
- **Transitions:** 32
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 33 minutes
- **Technician:** Operator_3

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 43 minutes
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
