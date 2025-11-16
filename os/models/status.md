# System Status
**UUID:** 53036a7f-b3bc-4594-b8f9-c3b3624e646d
**ISA-95 Level:** L3 MES
**Directory:** `/os/models/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** IDLE
- **Health:** DEGRADED
- **Mode:** Automatic
- **Uptime:** 92.4%

### Resource Utilization
- **CPU:** 15%
- **Memory:** 41%
- **Disk:** 60%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** MODELS_PLC_001
- **State:** IDLE
- **Scan Time:** 500ms
- **Last Cycle:** 100ms
- **Faults:** 2

### HMI Status
- **Interface:** MODELS_HMI
- **Connected Users:** 0
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 117ms

### SCADA Status
- **Server:** MODELS_SCADA
- **Tag Count:** 10
- **Update Rate:** 100%
- **Data Quality:** Uncertain
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 1
- **Info:** 1
- **Total:** 3

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 79ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 96 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 76%
- **Quality Rate:** 96.0%

### System Health
- **Response Time:** 67ms
- **Packet Loss:** 0.15%
- **Error Rate:** 0.163%
- **Availability:** 92.4%

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
- **Total Tags:** 56
- **Active Tags:** 42
- **Stale Tags:** 3
- **Bad Quality:** 2

### Tag Categories
- **Status Tags:** 9
- **Process Tags:** 28
- **Alarm Tags:** 10
- **Command Tags:** 2
- **Diagnostic Tags:** 7

## PackML State Machine

### Current State: IDLE

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
- **Duration:** 141 seconds
- **Transitions:** 50
- **Faults:** 2

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 40 minutes
- **Technician:** Operator_5

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 34 minutes
- **Priority:** High

## Diagnostics

### System Checks
- ✅ Configuration Valid
- ✅ Communication Active
- ✅ Tags Updating
- ⚠️ No Active Alarms
- ✅ Historian Recording
- ✅ Backup Current

### Health Indicators
- **Overall:** DEGRADED
- **Hardware:** GOOD
- **Software:** GOOD
- **Network:** DEGRADED
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

**Status Code:** DEGRADED
**Message:** System degraded - check alarms
