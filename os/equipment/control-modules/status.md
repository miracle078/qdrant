# System Status
**UUID:** fc959b9b-5a40-4a51-9c72-38a774843dce
**ISA-95 Level:** L3 MES
**Directory:** `/os/equipment/control-modules/`
**Last Updated:** 2025-11-16 01:51:10 UTC

## Current State

### Operational Status
- **Status:** RUNNING
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 94.3%

### Resource Utilization
- **CPU:** 40%
- **Memory:** 39%
- **Disk:** 38%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** CONTROL-MODULES_PLC_001
- **State:** RUNNING
- **Scan Time:** 500ms
- **Last Cycle:** 82ms
- **Faults:** 0

### HMI Status
- **Interface:** CONTROL-MODULES_HMI
- **Connected Users:** 3
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 167ms

### SCADA Status
- **Server:** CONTROL-MODULES_SCADA
- **Tag Count:** 41
- **Update Rate:** 94%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 0
- **Info:** 0
- **Total:** 0

### Recent Events
1. `[01:51:10]` System heartbeat - Normal
2. `[01:51:10]` Tag refresh - Success
3. `[01:51:10]` Communication - Active
4. `[01:51:10]` Scan cycle - 94ms
5. `[01:51:10]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 51 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 78%
- **Quality Rate:** 95.0%

### System Health
- **Response Time:** 124ms
- **Packet Loss:** 0.48%
- **Error Rate:** 0.943%
- **Availability:** 94.3%

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
- **Total Tags:** 19
- **Active Tags:** 65
- **Stale Tags:** 0
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 14
- **Process Tags:** 10
- **Alarm Tags:** 5
- **Command Tags:** 5
- **Diagnostic Tags:** 13

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
- **Duration:** 112 seconds
- **Transitions:** 39
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 59 minutes
- **Technician:** Operator_1

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 32 minutes
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
