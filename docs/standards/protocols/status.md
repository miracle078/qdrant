# System Status
**UUID:** f1aed73b-7910-4e85-9272-87bc8a236773
**ISA-95 Level:** L4 Business
**Directory:** `/docs/standards/protocols/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 87.4%

### Resource Utilization
- **CPU:** 48%
- **Memory:** 27%
- **Disk:** 56%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** PROTOCOLS_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 59ms
- **Faults:** 0

### HMI Status
- **Interface:** PROTOCOLS_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 114ms

### SCADA Status
- **Server:** PROTOCOLS_SCADA
- **Tag Count:** 10
- **Update Rate:** 89%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 3
- **Info:** 1
- **Total:** 3

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 75ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 98 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 83%
- **Quality Rate:** 95.0%

### System Health
- **Response Time:** 148ms
- **Packet Loss:** 0.36%
- **Error Rate:** 0.006%
- **Availability:** 87.4%

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
- **Total Tags:** 60
- **Active Tags:** 68
- **Stale Tags:** 4
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 5
- **Process Tags:** 34
- **Alarm Tags:** 8
- **Command Tags:** 3
- **Diagnostic Tags:** 12

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
- **Duration:** 105 seconds
- **Transitions:** 6
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 12 minutes
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
