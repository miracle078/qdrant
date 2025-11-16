# System Status
**UUID:** 0687f350-a1ba-4669-9e52-9a9ec9983219
**ISA-95 Level:** L4 Business
**Directory:** `/docs/standards/protocols/mqtt/`
**Last Updated:** 2025-11-16 01:51:02 UTC

## Current State

### Operational Status
- **Status:** ACTIVE
- **Health:** HEALTHY
- **Mode:** Automatic
- **Uptime:** 96.7%

### Resource Utilization
- **CPU:** 51%
- **Memory:** 28%
- **Disk:** 77%
- **Network:** Active

## Control System

### PLC Status
- **Controller:** MQTT_PLC_001
- **State:** ACTIVE
- **Scan Time:** 500ms
- **Last Cycle:** 54ms
- **Faults:** 0

### HMI Status
- **Interface:** MQTT_HMI
- **Connected Users:** 1
- **Screen:** Main Overview
- **Refresh Rate:** 1 second
- **Response Time:** 114ms

### SCADA Status
- **Server:** MQTT_SCADA
- **Tag Count:** 18
- **Update Rate:** 90%
- **Data Quality:** Good
- **Historian:** Connected

## Alarms & Events

### Active Alarms
- **Critical:** 0
- **Warning:** 2
- **Info:** 2
- **Total:** 2

### Recent Events
1. `[01:51:02]` System heartbeat - Normal
2. `[01:51:02]` Tag refresh - Success
3. `[01:51:02]` Communication - Active
4. `[01:51:02]` Scan cycle - 67ms
5. `[01:51:02]` Status update - Complete

## Performance Metrics

### Production (if applicable)
- **Current Output:** 95 units/hr
- **Target Output:** 100 units/hr
- **Efficiency:** 82%
- **Quality Rate:** 100.0%

### System Health
- **Response Time:** 197ms
- **Packet Loss:** 0.24%
- **Error Rate:** 0.840%
- **Availability:** 96.7%

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
- **Total Tags:** 38
- **Active Tags:** 48
- **Stale Tags:** 3
- **Bad Quality:** 0

### Tag Categories
- **Status Tags:** 5
- **Process Tags:** 14
- **Alarm Tags:** 4
- **Command Tags:** 5
- **Diagnostic Tags:** 5

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
- **Duration:** 264 seconds
- **Transitions:** 36
- **Faults:** 0

## Maintenance

### Last Maintenance
- **Date:** 2025-11-16
- **Type:** Preventive
- **Duration:** 28 minutes
- **Technician:** Operator_1

### Next Scheduled
- **Date:** 2025-11-16
- **Type:** Inspection
- **Estimated Duration:** 27 minutes
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
