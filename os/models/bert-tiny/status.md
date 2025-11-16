# System Status
**UUID:** 8eff8871-7e14-4a1c-a424-1c84c6bdd358
**ISA-95 Level:** L3 MES
**Directory:** `/os/models/bert-tiny/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 98.9%

### Resource Utilization
- **CPU:** 40%
- **Memory:** 66%
- **Disk:** 52%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** BERT-TINY_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 73ms
- **Faults:** 0

### HMI Status
- **Interface:** BERT-TINY_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 108ms

### SCADA Status
- **Server:** BERT-TINY_SCADA
- **Tag Count:** 22
- **Update Rate:** 88%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 1
- **Info:** 2
- **Total:** 1

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 93ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 52 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 78%
- **Quality Rate:** 96.0%

### System Health
- **Response Time:** 174ms
- **Packet Loss:** 0.15%
- **Error Rate:** 0.954%
- **Availability:** 98.9%

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
- **Active Tags:** 59
- **Stale Tags:** 2
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 8
- **Process Tags:** 24
- **Alarm Tags:** 3
- **Command Tags:** 8
- **Diagnostic Tags:** 12

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
- **Duration:** 206 seconds
- **Transitions:** 39
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 32 minutes
- **Technician:** Operator_5

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 40 minutes
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
