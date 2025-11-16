# System Status
**UUID:** 660ff6a5-f7ba-47ed-9509-d53f79a9b616
**ISA-95 Level:** L3 MES
**Directory:** `/os/models/squeezenet/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 93.1%

### Resource Utilization
- **CPU:** 48%
- **Memory:** 56%
- **Disk:** 68%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** SQUEEZENET_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 72ms
- **Faults:** 0

### HMI Status
- **Interface:** SQUEEZENET_HMI
- **Connected Users:** 2
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 190ms

### SCADA Status
- **Server:** SQUEEZENET_SCADA
- **Tag Count:** 10
- **Update Rate:** 94%
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
4. `[01:51:02]` Scan cycle - 87ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 81 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 77%
- **Quality Rate:** 96.0%

### System Health
- **Response Time:** 125ms
- **Packet Loss:** 0.40%
- **Error Rate:** 0.861%
- **Availability:** 93.1%

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
- **Total Tags:** 18
- **Active Tags:** 20
- **Stale Tags:** 1
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 11
- **Process Tags:** 31
- **Alarm Tags:** 10
- **Command Tags:** 8
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
- **Duration:** 201 seconds
- **Transitions:** 7
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 27 minutes
- **Technician:** Operator_5

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 31 minutes
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
