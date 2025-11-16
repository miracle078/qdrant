# System Status
**UUID:** 0dc232d7-4d57-49da-be61-c96ee151e907
**ISA-95 Level:** L3 MES
**Directory:** `/os/equipment/site/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 85.7%

### Resource Utilization
- **CPU:** 58%
- **Memory:** 56%
- **Disk:** 47%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** SITE_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 86ms
- **Faults:** 0

### HMI Status
- **Interface:** SITE_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 144ms

### SCADA Status
- **Server:** SITE_SCADA
- **Tag Count:** 44
- **Update Rate:** 98%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 2
- **Info:** 2
- **Total:** 2

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 76ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 60 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 84%
- **Quality Rate:** 97.0%

### System Health
- **Response Time:** 104ms
- **Packet Loss:** 0.03%
- **Error Rate:** 0.048%
- **Availability:** 85.7%

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
- **Total Tags:** 18
- **Active Tags:** 66
- **Stale Tags:** 0
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 7
- **Process Tags:** 15
- **Alarm Tags:** 9
- **Command Tags:** 3
- **Diagnostic Tags:** 9

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
- **Entry Time:** 01:51:10
- **Duration:** 125 seconds
- **Transitions:** 9
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 39 minutes
- **Technician:** Operator_1

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 45 minutes
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
