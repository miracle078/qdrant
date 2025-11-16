# System Status
**UUID:** 5bb8a00c-e66c-4706-867f-2cbe23b3023e
**ISA-95 Level:** L3 MES
**Directory:** `/os/modules/packml/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 97.3%

### Resource Utilization
- **CPU:** 42%
- **Memory:** 52%
- **Disk:** 79%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** PACKML_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 76ms
- **Faults:** 0

### HMI Status
- **Interface:** PACKML_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 54ms

### SCADA Status
- **Server:** PACKML_SCADA
- **Tag Count:** 25
- **Update Rate:** 88%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 1
- **Info:** 1
- **Total:** 1

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 48ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 83 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 81%
- **Quality Rate:** 100.0%

### System Health
- **Response Time:** 87ms
- **Packet Loss:** 0.49%
- **Error Rate:** 0.886%
- **Availability:** 97.3%

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
- **Total Tags:** 53
- **Active Tags:** 82
- **Stale Tags:** 1
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 11
- **Process Tags:** 13
- **Alarm Tags:** 10
- **Command Tags:** 5
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
- **Entry Time:** 01:51:10
- **Duration:** 24 seconds
- **Transitions:** 10
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 51 minutes
- **Technician:** Operator_2

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 26 minutes
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
