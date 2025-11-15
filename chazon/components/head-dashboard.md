# Dashboard Head Component
**Dashboard Styles** | Tab Interface

```javascript
const HeadDashboard = () => `
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chazon Unified Dashboard</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Courier New', monospace; background: #0a0a0a; color: #00ff88; overflow: hidden; }
    #topnav { position: fixed; top: 0; width: 100%; height: 60px; background: rgba(0,0,0,0.95); border-bottom: 2px solid #00ff88; display: flex; align-items: center; padding: 0 20px; z-index: 1000; gap: 20px; }
    .logo { font-size: 24px; color: #00ccff; font-weight: bold; }
    .nav-tabs { display: flex; gap: 10px; flex: 1; }
    .tab { background: transparent; border: 2px solid #333; color: #0f0; padding: 8px 20px; cursor: pointer; font-family: inherit; font-size: 14px; transition: all 0.2s; border-radius: 5px 5px 0 0; }
    .tab:hover { border-color: #00ff88; background: rgba(0,255,136,0.1); }
    .tab.active { border-color: #00ff88; background: rgba(0,255,136,0.2); }
    .content { position: fixed; top: 60px; left: 0; width: 100%; height: calc(100% - 60px); display: none; }
    .content.active { display: block; }
    iframe { width: 100%; height: 100%; border: none; }
  </style>
</head>`;

return HeadDashboard();
```
