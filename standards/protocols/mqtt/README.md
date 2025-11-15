# MQTT (Message Queuing Telemetry Transport)
**Lightweight Pub/Sub Protocol for IoT**

## Overview

MQTT is a lightweight publish-subscribe messaging protocol designed for constrained devices and low-bandwidth, high-latency networks.

## MQTT in Chazon

**Use Cases:**
- Medical imaging event notifications
- Module state change broadcasts
- Boot sequence progress updates
- Real-time metric streaming
- Alarm distribution

**Broker:** Mosquitto or HiveMQ
**Port:** 1883 (unencrypted), 8883 (TLS)

## Topic Structure

```
chazon/
├── os/
│   ├── modules/
│   │   ├── status              # Module system status
│   │   ├── loaded              # Module load events
│   │   └── cache/hitrate       # Cache metrics
│   ├── boot/
│   │   ├── phase/0/status      # Phase 0 status
│   │   ├── phase/1/status      # Phase 1 status
│   │   └── complete            # Boot complete event
│   ├── medical/
│   │   ├── study/new           # New study uploaded
│   │   ├── analysis/complete   # Analysis finished
│   │   └── alf-detect/result   # AlF-DETECT result
│   └── debug/
│       ├── cpu                 # CPU usage %
│       ├── memory              # Memory usage MB
│       └── logs/error          # Error log events
├── plc/
│   ├── area/modules/status     # PLC status for modules area
│   ├── area/boot/scan_time     # PLC scan time
│   └── alarms/+                # All alarms (wildcard)
└── scada/
    ├── gateway/online          # SCADA gateway status
    └── metrics/#               # All SCADA metrics
```

## QoS Levels

- **QoS 0** (At most once) - Fire and forget (metrics, logs)
- **QoS 1** (At least once) - Acknowledged delivery (events)
- **QoS 2** (Exactly once) - Guaranteed delivery (commands, alarms)

## Message Examples

### Publish Module Load Event
```javascript
mqtt.publish('chazon/os/modules/loaded', JSON.stringify({
  module_uuid: '1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d',
  module_name: 'medical-imaging.md',
  timestamp: Date.now(),
  load_time_ms: 45
}), { qos: 1 });
```

### Subscribe to Boot Events
```javascript
mqtt.subscribe('chazon/os/boot/+/status', (topic, message) => {
  const phase = topic.split('/')[3];
  const status = JSON.parse(message);
  console.log(`Boot Phase ${phase}: ${status.state}`);
});
```

### Publish AlF-DETECT Result
```javascript
mqtt.publish('chazon/os/medical/alf-detect/result', JSON.stringify({
  patient_id: 'P12345',
  study_id: 'S67890',
  alzheimers_prob: 0.78,
  autism_prob: 0.12,
  normal_prob: 0.10,
  risk_score: 85.4,
  timestamp: Date.now()
}), { qos: 2, retain: true });
```

## Configuration

```yaml
# mqtt-config.yaml
broker:
  host: localhost
  port: 1883
  tls: false

client:
  client_id: chazon-os-${random}
  clean_session: true
  keepalive: 60

topics:
  subscribe:
    - chazon/os/+/status
    - chazon/plc/alarms/#
  publish:
    prefix: chazon/os
    qos_default: 1
```

## Security

**Authentication:**
- Username/password
- TLS client certificates
- OAuth 2.0 tokens (MQTT v5)

**Authorization:**
- Topic-based ACLs
- Role-based access control

## MQTT v5 Features

- **Reason Codes** - Detailed error information
- **User Properties** - Custom metadata
- **Topic Aliases** - Reduce bandwidth
- **Shared Subscriptions** - Load balancing
- **Message Expiry** - TTL for messages
