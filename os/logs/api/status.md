# System Status
**UUID:** effec69a-d6b5-43d0-adf0-e8d2537c1142
**ISA-95 Level:** L3 MES
**Directory:** `/os/logs/api/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 94.9%

### Resource Utilization
- **CPU:** 24%
- **Memory:** 31%
- **Disk:** 51%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** API_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 71ms
- **Faults:** 0

### HMI Status
- **Interface:** API_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 114ms

### SCADA Status
- **Server:** API_SCADA
- **Tag Count:** 20
- **Update Rate:** 98%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 3
- **Info:** 0
- **Total:** 3

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 87ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 89 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 77%
- **Quality Rate:** 96.0%

### System Health
- **Response Time:** 159ms
- **Packet Loss:** 0.40%
- **Error Rate:** 0.799%
- **Availability:** 94.9%

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
- **Total Tags:** 95
- **Active Tags:** 72
- **Stale Tags:** 4
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 12
- **Process Tags:** 10
- **Alarm Tags:** 6
- **Command Tags:** 3
- **Diagnostic Tags:** 8

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
- **Duration:** 238 seconds
- **Transitions:** 10
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 58 minutes
- **Technician:** Operator_1

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 38 minutes
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
