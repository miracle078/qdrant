# System Status
**UUID:** 7b85c49e-a0e4-4852-a993-f783aaf36749
**ISA-95 Level:** L3 MES
**Directory:** `/os/equipment/areas/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** PRODUCTION
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 99.4%

### Resource Utilization
- **CPU:** 16%
- **Memory:** 56%
- **Disk:** 58%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** AREAS_PLC_001
- **State:** PRODUCTION
- **Scan Time:** 500ms
- **Last Cycle:** 74ms
- **Faults:** 0

### HMI Status
- **Interface:** AREAS_HMI
- **Connected Users:** 1
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 150ms

### SCADA Status
- **Server:** AREAS_SCADA
- **Tag Count:** 39
- **Update Rate:** 91%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 2
- **Info:** 1
- **Total:** 2

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 96ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 63 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 85%
- **Quality Rate:** 96.0%

### System Health
- **Response Time:** 73ms
- **Packet Loss:** 0.40%
- **Error Rate:** 0.720%
- **Availability:** 99.4%

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
- **Total Tags:** 84
- **Active Tags:** 95
- **Stale Tags:** 5
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 14
- **Process Tags:** 22
- **Alarm Tags:** 7
- **Command Tags:** 3
- **Diagnostic Tags:** 15

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
- **Duration:** 146 seconds
- **Transitions:** 43
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 17 minutes
- **Technician:** Operator_3

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 33 minutes
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
