# System Status
**UUID:** 7f20df30-7753-4a54-9895-e23738812004
**ISA-95 Level:** L4 Business
**Directory:** `/docs/standards/isa/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 85.5%

### Resource Utilization
- **CPU:** 56%
- **Memory:** 25%
- **Disk:** 56%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** ISA_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 74ms
- **Faults:** 0

### HMI Status
- **Interface:** ISA_HMI
- **Connected Users:** 0
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 55ms

### SCADA Status
- **Server:** ISA_SCADA
- **Tag Count:** 16
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
4. `[01:51:02]` Scan cycle - 43ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 66 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 77%
- **Quality Rate:** 98.0%

### System Health
- **Response Time:** 181ms
- **Packet Loss:** 0.49%
- **Error Rate:** 0.121%
- **Availability:** 85.5%

## Network Status

### Connections
- **PLC Network:** Degraded
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
- **Total Tags:** 61
- **Active Tags:** 32
- **Stale Tags:** 0
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 5
- **Process Tags:** 30
- **Alarm Tags:** 3
- **Command Tags:** 3
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
- **Duration:** 135 seconds
- **Transitions:** 16
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 20 minutes
- **Technician:** Operator_3

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 15 minutes
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
