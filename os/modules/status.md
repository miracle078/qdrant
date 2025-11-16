# System Status
**UUID:** 5bd0b2e5-a02a-4086-8150-25d8a968bb51
**ISA-95 Level:** L3 MES
**Directory:** `/os/modules/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** RUNNING
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 94.7%

### Resource Utilization
- **CPU:** 24%
- **Memory:** 56%
- **Disk:** 46%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** MODULES_PLC_001
- **State:** RUNNING
- **Scan Time:** 500ms
- **Last Cycle:** 80ms
- **Faults:** 0

### HMI Status
- **Interface:** MODULES_HMI
- **Connected Users:** 2
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 129ms

### SCADA Status
- **Server:** MODULES_SCADA
- **Tag Count:** 35
- **Update Rate:** 91%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 1
- **Total:** 0

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 68ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 68 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 90%
- **Quality Rate:** 95.0%

### System Health
- **Response Time:** 137ms
- **Packet Loss:** 0.10%
- **Error Rate:** 0.099%
- **Availability:** 94.7%

## Network Status

### Connections
- **PLC Network:** Connected
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
- **Total Tags:** 34
- **Active Tags:** 64
- **Stale Tags:** 4
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 6
- **Process Tags:** 24
- **Alarm Tags:** 3
- **Command Tags:** 5
- **Diagnostic Tags:** 14

## PackML State Machine

### Current State: RUNNING

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
- **Duration:** 53 seconds
- **Transitions:** 43
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 34 minutes
- **Technician:** Operator_4

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 19 minutes
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
