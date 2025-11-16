# System Status
**UUID:** 1149711d-2ce8-40b9-ac6b-28f7a1d46fe1
**ISA-95 Level:** L3 MES
**Directory:** `/os/logs/system/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 94.5%

### Resource Utilization
- **CPU:** 60%
- **Memory:** 37%
- **Disk:** 54%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** SYSTEM_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 59ms
- **Faults:** 0

### HMI Status
- **Interface:** SYSTEM_HMI
- **Connected Users:** 0
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 199ms

### SCADA Status
- **Server:** SYSTEM_SCADA
- **Tag Count:** 28
- **Update Rate:** 83%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 2
- **Total:** 0

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 50ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 60 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 85%
- **Quality Rate:** 96.0%

### System Health
- **Response Time:** 121ms
- **Packet Loss:** 0.42%
- **Error Rate:** 0.352%
- **Availability:** 94.5%

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
- **Total Tags:** 26
- **Active Tags:** 46
- **Stale Tags:** 0
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 9
- **Process Tags:** 17
- **Alarm Tags:** 10
- **Command Tags:** 4
- **Diagnostic Tags:** 14

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
- **Duration:** 64 seconds
- **Transitions:** 29
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 56 minutes
- **Technician:** Operator_3

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 32 minutes
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
