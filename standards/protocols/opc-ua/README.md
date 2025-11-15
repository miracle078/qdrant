# OPC UA (Unified Architecture)
**Platform-Independent Industrial Communication**

## Overview

OPC UA is a machine-to-machine communication protocol for industrial automation. It provides secure, reliable data exchange with built-in discovery, information modeling, and publish-subscribe.

## OPC UA in Chazon

**Use Cases:**
- PLC-to-SCADA communication
- Standardized data models for medical devices
- Secure inter-system communication
- Historical data access (HDA)
- Alarms and events (A&E)

**Port:** 4840 (opc.tcp://), 4843 (HTTPS)

## Information Model

```
Root
├── Objects
│   ├── Chazon
│   │   ├── OS
│   │   │   ├── Modules
│   │   │   │   ├── LoadedCount (Variable)
│   │   │   │   ├── MemoryUsage (Variable)
│   │   │   │   └── CacheHitRate (Variable)
│   │   │   ├── Boot
│   │   │   │   ├── CurrentPhase (Variable)
│   │   │   │   ├── PhaseStatus[0..5] (Array)
│   │   │   │   └── StartBoot (Method)
│   │   │   └── Medical
│   │   │       ├── StudiesAnalyzed (Variable)
│   │   │       ├── AlFDetections (Variable)
│   │   │       └── RunAnalysis (Method)
│   │   └── PLC
│   │       ├── Area[001..006] (Array)
│   │       │   ├── ScanTime (Variable)
│   │       │   ├── Status (Variable)
│   │       │   └── TagCount (Variable)
│   │       └── MasterController
│   └── DeviceSet
└── Types
    ├── ObjectTypes
    │   └── ChazonPLCType (Custom)
    └── VariableTypes
        └── ModuleMetricType (Custom)
```

## Security

**Authentication:**
- Anonymous
- Username/Password
- X.509 Certificates

**Encryption:**
- None
- Basic128Rsa15 (deprecated)
- Basic256
- Basic256Sha256 (recommended)

**Message Security Mode:**
- None
- Sign
- SignAndEncrypt (recommended)

## Example: Read Module Count

```javascript
const { OPCUAClient } = require('node-opcua');

const client = OPCUAClient.create({
  endpointMustExist: false,
  securityMode: 'SignAndEncrypt',
  securityPolicy: 'Basic256Sha256'
});

await client.connect('opc.tcp://localhost:4840');

const session = await client.createSession();

// Read variable
const dataValue = await session.readVariableValue(
  'ns=2;s=Chazon.OS.Modules.LoadedCount'
);

console.log('Modules loaded:', dataValue.value.value);

await session.close();
await client.disconnect();
```

## Example: Subscribe to Boot Events

```javascript
const subscription = await session.createSubscription2({
  publishingInterval: 1000,
  maxNotificationsPerPublish: 10
});

const monitoredItem = await subscription.monitor({
  nodeId: 'ns=2;s=Chazon.OS.Boot.CurrentPhase',
  attributeId: AttributeIds.Value
}, {
  samplingInterval: 100,
  discardOldest: true,
  queueSize: 10
});

monitoredItem.on('changed', (dataValue) => {
  console.log('Boot phase:', dataValue.value.value);
});
```

## Example: Call Method

```javascript
// Call StartBoot method
const inputArguments = [
  { dataType: DataType.Boolean, value: true }  // quickBoot
];

const result = await session.call({
  objectId: 'ns=2;s=Chazon.OS.Boot',
  methodId: 'ns=2;s=Chazon.OS.Boot.StartBoot',
  inputArguments
});

console.log('Boot result:', result.outputArguments[0].value);
```

## Node IDs

| NodeId | Name | Type | Access |
|--------|------|------|--------|
| ns=2;s=Chazon.OS.Modules.LoadedCount | Loaded Count | Int32 | Read |
| ns=2;s=Chazon.OS.Modules.MemoryUsage | Memory Usage | Double | Read |
| ns=2;s=Chazon.OS.Boot.CurrentPhase | Current Phase | Int32 | Read |
| ns=2;s=Chazon.PLC.Area[001].ScanTime | PLC-001 Scan Time | Double | Read |
| ns=2;s=Chazon.PLC.Area[001].Status | PLC-001 Status | String | Read |

## Configuration

```yaml
# opc-ua-config.yaml
server:
  port: 4840
  hostname: localhost

security:
  mode: SignAndEncrypt
  policy: Basic256Sha256

certificate:
  path: ./certs/server_cert.der
  key_path: ./certs/server_key.pem

namespace:
  index: 2
  uri: "urn:chazon:opcua:server"

nodes:
  - id: "Chazon.OS.Modules"
    browseName: "Modules"
    variables:
      - name: "LoadedCount"
        dataType: "Int32"
        initialValue: 0
      - name: "MemoryUsage"
        dataType: "Double"
        initialValue: 0.0
```
