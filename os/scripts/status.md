# System Status
**UUID:** 468695d1-494e-410d-847d-a45c012fd10d
**ISA-95 Level:** L3 MES
**Directory:** `/os/scripts/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 94.0%

### Resource Utilization
- **CPU:** 57%
- **Memory:** 32%
- **Disk:** 46%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** SCRIPTS_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 68ms
- **Faults:** 0

### HMI Status
- **Interface:** SCRIPTS_HMI
- **Connected Users:** 0
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 170ms

### SCADA Status
- **Server:** SCRIPTS_SCADA
- **Tag Count:** 27
- **Update Rate:** 80%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 3
- **Info:** 2
- **Total:** 3

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 44ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 100 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 87%
- **Quality Rate:** 100.0%

### System Health
- **Response Time:** 167ms
- **Packet Loss:** 0.21%
- **Error Rate:** 0.639%
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
- **Total Tags:** 85
- **Active Tags:** 55
- **Stale Tags:** 0
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 14
- **Process Tags:** 24
- **Alarm Tags:** 10
- **Command Tags:** 6
- **Diagnostic Tags:** 13

## PackML State Machine

### Current State: PRODUCTION

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
- **Duration:** 178 seconds
- **Transitions:** 8
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 54 minutes
- **Technician:** Operator_1

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
