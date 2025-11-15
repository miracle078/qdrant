# Tag Providers
**Type:** SCADA Infrastructure | ISA-95 L2 Control

Centralized tag provider system modeled after Ignition SCADA tag providers. Manages all tag values, history, and subscriptions for HMI/SCADA interfaces.

## Architecture

Each OS subdirectory gets its own tag provider:
- `frontend.json` - Frontend HMI tags
- `backend.json` - Backend API tags
- `modules.json` - Module library tags
- `boot.json` - Boot sequencer tags
- `models.json` - AI models tags
- `data.json` - Database tags
- `language.json` - SNT language tags
- `medical.json` - Medical imaging tags

## Tag Structure

```json
{
  "provider": "frontend",
  "description": "Frontend HMI Control Tags",
  "tags": {
    "status": {
      "value": "RUNNING",
      "type": "string",
      "quality": "GOOD",
      "timestamp": "2025-11-15T05:50:00Z"
    },
    "scanTime": {
      "value": 50,
      "type": "number",
      "unit": "ms",
      "quality": "GOOD",
      "timestamp": "2025-11-15T05:50:00Z"
    },
    "modulesLoaded": {
      "value": 41,
      "type": "number",
      "quality": "GOOD",
      "timestamp": "2025-11-15T05:50:00Z"
    }
  }
}
```

## Tag Types

- **Analog**: Numbers (int, float)
- **Digital**: Booleans (on/off, true/false)
- **String**: Text values
- **Quality**: GOOD, BAD, UNCERTAIN
- **Timestamp**: ISO 8601 format

## Quality Codes

Following ISA-5.1 instrument signals:
- `GOOD` - Tag value is reliable
- `BAD` - Tag value is unreliable (sensor failure, connection lost)
- `UNCERTAIN` - Tag value may be inaccurate (calibration needed)

## Tag Provider API

```javascript
const TagProvider = {
  // Read tag value
  read(provider, tagName) {
    const data = this.providers[provider];
    return data?.tags[tagName]?.value;
  },

  // Write tag value
  write(provider, tagName, value) {
    const tag = this.providers[provider]?.tags[tagName];
    if (tag) {
      tag.value = value;
      tag.timestamp = new Date().toISOString();
      this.notifySubscribers(provider, tagName, value);
    }
  },

  // Subscribe to tag changes
  subscribe(provider, tagName, callback) {
    const key = `${provider}.${tagName}`;
    if (!this.subscriptions[key]) {
      this.subscriptions[key] = [];
    }
    this.subscriptions[key].push(callback);
  },

  // Load provider
  async loadProvider(name) {
    const response = await fetch(`tag-providers/${name}.json`);
    const data = await response.json();
    this.providers[name] = data;
  }
};
```

## Usage in HMI/SCADA

### Old Way (Hardcoded)
```javascript
document.getElementById('status').textContent = 'RUNNING';
document.getElementById('scanTime').textContent = '50ms';
```

### New Way (Tag Provider)
```javascript
// Load provider
await TagProvider.loadProvider('frontend');

// Read tags
const status = TagProvider.read('frontend', 'status');
const scanTime = TagProvider.read('frontend', 'scanTime');

document.getElementById('status').textContent = status;
document.getElementById('scanTime').textContent = scanTime + 'ms';

// Subscribe to updates
TagProvider.subscribe('frontend', 'status', (newValue) => {
  document.getElementById('status').textContent = newValue;
});
```

## Historical Data

Tag providers can store historical values for trending:

```json
{
  "history": [
    { "value": 50, "timestamp": "2025-11-15T05:49:00Z" },
    { "value": 52, "timestamp": "2025-11-15T05:49:30Z" },
    { "value": 51, "timestamp": "2025-11-15T05:50:00Z" }
  ]
}
```

## Benefits

1. **Centralized Data Management** - All tag values in one place
2. **Decoupling** - HMIs don't need to know where data comes from
3. **History & Trending** - Built-in historical data storage
4. **Quality Indicators** - Know when data is unreliable
5. **Pub/Sub Pattern** - Efficient updates via subscriptions
6. **ISA Compliance** - Follows industrial automation standards

## Integration with SCADA

The SCADA system reads from tag providers to display real-time data:
- Process values
- Alarms
- System metrics
- PLC status

This matches Ignition's architecture where HMI screens bind to tag paths like:
```
[provider]path/to/tag
```

Example: `[frontend]status` → "RUNNING"
