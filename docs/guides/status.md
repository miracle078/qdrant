# System Status
**UUID:** 29d28a6d-3beb-4701-88fa-2ff78e6bba5b
**ISA-95 Level:** L4 Business
**Directory:** `/docs/guides/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 87.2%

### Resource Utilization
- **CPU:** 20%
- **Memory:** 44%
- **Disk:** 61%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** GUIDES_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 82ms
- **Faults:** 0

### HMI Status
- **Interface:** GUIDES_HMI
- **Connected Users:** 2
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 55ms

### SCADA Status
- **Server:** GUIDES_SCADA
- **Tag Count:** 47
- **Update Rate:** 94%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 1
- **Total:** 0

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 64ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 88 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 85%
- **Quality Rate:** 97.0%

### System Health
- **Response Time:** 190ms
- **Packet Loss:** 0.28%
- **Error Rate:** 0.605%
- **Availability:** 87.2%

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
- **Total Tags:** 66
- **Active Tags:** 22
- **Stale Tags:** 5
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 14
- **Process Tags:** 31
- **Alarm Tags:** 3
- **Command Tags:** 8
- **Diagnostic Tags:** 9

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
- **Duration:** 182 seconds
- **Transitions:** 41
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 40 minutes
- **Technician:** Operator_4

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 39 minutes
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
