# System Status
**UUID:** 50ccb2c7-bed4-45fe-a516-9f8b476c0741
**ISA-95 Level:** L4 Business
**Directory:** `/docs/presentation/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 98.8%

### Resource Utilization
- **CPU:** 17%
- **Memory:** 23%
- **Disk:** 67%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** PRESENTATION_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 76ms
- **Faults:** 0

### HMI Status
- **Interface:** PRESENTATION_HMI
- **Connected Users:** 1
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 200ms

### SCADA Status
- **Server:** PRESENTATION_SCADA
- **Tag Count:** 14
- **Update Rate:** 88%
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
4. `[01:51:02]` Scan cycle - 56ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 100 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 88%
- **Quality Rate:** 99.0%

### System Health
- **Response Time:** 117ms
- **Packet Loss:** 0.49%
- **Error Rate:** 0.124%
- **Availability:** 98.8%

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
- **Total Tags:** 27
- **Active Tags:** 73
- **Stale Tags:** 3
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 11
- **Process Tags:** 23
- **Alarm Tags:** 5
- **Command Tags:** 7
- **Diagnostic Tags:** 10

## PackML State Machine

### Current State: ACTIVE

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
- **Duration:** 209 seconds
- **Transitions:** 45
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 10 minutes
- **Technician:** Operator_4

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 23 minutes
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
