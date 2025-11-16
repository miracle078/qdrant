# System Status
**UUID:** 52bbb1d2-b806-4792-8e85-47b733e00fc5
**ISA-95 Level:** L4 Business
**Directory:** `/cli/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 97.8%

### Resource Utilization
- **CPU:** 57%
- **Memory:** 22%
- **Disk:** 43%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** CLI_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 42ms
- **Faults:** 0

### HMI Status
- **Interface:** CLI_HMI
- **Connected Users:** 2
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 70ms

### SCADA Status
- **Server:** CLI_SCADA
- **Tag Count:** 45
- **Update Rate:** 89%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 2
- **Info:** 1
- **Total:** 2

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 79ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 99 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 91%
- **Quality Rate:** 100.0%

### System Health
- **Response Time:** 50ms
- **Packet Loss:** 0.03%
- **Error Rate:** 0.507%
- **Availability:** 97.8%

## Network Status

### Connections
- **PLC Network:** Degraded
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
- **Total Tags:** 41
- **Active Tags:** 28
- **Stale Tags:** 5
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 11
- **Process Tags:** 37
- **Alarm Tags:** 3
- **Command Tags:** 8
- **Diagnostic Tags:** 13

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
- **Duration:** 298 seconds
- **Transitions:** 46
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
