# HMI Template
**UUID:** template-hmi-standard-v1
**Type:** Template | Parameterized HMI Generator

Template for generating area-specific HMI (Human-Machine Interface) panels.

## Parameters

```javascript
const hmiConfig = {
  areaName: 'Module System',      // Display name
  areaIcon: '📦',                  // Icon emoji
  plcStatus: 'RUNNING',            // RUNNING, IDLE, FAULT
  scanTime: '50ms',                // PLC scan time
  tagCount: 247,                   // Number of tags
  routineCount: 12,                // Number of routines
  mainColor: '#00ff88',            // Theme color
  operations: [                    // Available operations
    { name: 'Load Module', action: 'loadModule()' },
    { name: 'Scan Directory', action: 'scanDir()' },
    { name: 'Clear Cache', action: 'clearCache()' }
  ],
  metrics: [                       // Live metrics
    { label: 'Modules Loaded', value: '114', unit: '' },
    { label: 'Memory Usage', value: '47.2', unit: 'MB' },
    { label: 'Cache Hit Rate', value: '94.5', unit: '%' }
  ],
  alarms: [                        // Active alarms
    { priority: 'low', message: 'Cache 80% full', time: '14:23:01' }
  ]
};
```

## HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
  <title>HMI - ${areaName}</title>
  <style>
    body {
      font-family: 'Courier New', monospace;
      background: #0a0a0a;
      color: ${mainColor};
      margin: 0;
      padding: 20px;
    }
    .hmi-header {
      background: #1a1a2e;
      border: 2px solid ${mainColor};
      padding: 20px;
      margin-bottom: 20px;
    }
    .status-indicator {
      display: inline-block;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: ${plcStatus === 'RUNNING' ? '#00ff88' : '#ff0044'};
      animation: pulse 2s infinite;
    }
    .control-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
    }
    .control-btn {
      background: #1a1a2e;
      border: 2px solid ${mainColor};
      padding: 20px;
      cursor: pointer;
      transition: all 0.3s;
    }
    .control-btn:hover {
      background: #2a2a3e;
      transform: scale(1.05);
    }
    .metric-card {
      background: #1a1a2e;
      padding: 15px;
      border-left: 4px solid ${mainColor};
    }
    .alarm-list {
      background: #000;
      border: 1px solid #333;
      padding: 10px;
      max-height: 200px;
      overflow-y: auto;
    }
    .alarm-item {
      padding: 5px;
      border-bottom: 1px solid #222;
    }
    .alarm-item.high { color: #ff0044; }
    .alarm-item.medium { color: #ffaa00; }
    .alarm-item.low { color: #00ccff; }
  </style>
</head>
<body>
  <div class="hmi-header">
    <h1>${areaIcon} ${areaName} - HMI</h1>
    <div>
      <span class="status-indicator"></span>
      <strong>PLC Status:</strong> ${plcStatus} |
      <strong>Scan Time:</strong> ${scanTime} |
      <strong>Tags:</strong> ${tagCount}
    </div>
  </div>

  <h2>Operations</h2>
  <div class="control-grid">
    ${operations.map(op => `
      <div class="control-btn" onclick="${op.action}">
        ${op.name}
      </div>
    `).join('')}
  </div>

  <h2>Live Metrics</h2>
  <div class="control-grid">
    ${metrics.map(m => `
      <div class="metric-card">
        <div style="color: #888;">${m.label}</div>
        <div style="font-size: 2em; font-weight: bold;">${m.value}${m.unit}</div>
      </div>
    `).join('')}
  </div>

  <h2>Alarms</h2>
  <div class="alarm-list">
    ${alarms.map(a => `
      <div class="alarm-item ${a.priority}">
        [${a.time}] ${a.message}
      </div>
    `).join('')}
  </div>

  <script>
    // HMI runtime logic
    function refreshMetrics() {
      // Poll PLC for updated metrics
      fetch('../plc.html?action=getMetrics')
        .then(r => r.json())
        .then(data => updateDisplay(data));
    }

    setInterval(refreshMetrics, 1000);
  </script>
</body>
</html>
```

## Usage

```javascript
// Generate HMI for an area
const generateHMI = (config) => {
  const template = readTemplate('hmi-template.md');
  return template.replace(/\$\{(\w+)\}/g, (_, key) => config[key]);
};

// Example: Generate HMI for Models area
const modelsHMI = generateHMI({
  areaName: 'AI Models',
  areaIcon: '🤖',
  plcStatus: 'IDLE',
  scanTime: '100ms',
  tagCount: 48,
  routineCount: 6,
  mainColor: '#00ccff',
  operations: [
    { name: 'Load Model', action: 'loadModel()' },
    { name: 'Run Inference', action: 'runInference()' },
    { name: 'Download Model', action: 'downloadModel()' }
  ],
  metrics: [
    { label: 'Models Available', value: '4', unit: '' },
    { label: 'GPU Memory', value: '2.1', unit: 'GB' },
    { label: 'Inference Speed', value: '45', unit: 'ms' }
  ],
  alarms: []
});
```

## See Also

- `plc-template.md` - Companion PLC template
- `scada-template.md` - SCADA overview template
- `../modules/template-engine.md` - Template engine implementation
