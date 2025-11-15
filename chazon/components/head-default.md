# Default Head Component
**HTML Head** | Meta Tags & Styles

```javascript
const HeadDefault = () => `
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${window.pageTitle || 'Chazon OS'}</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Courier New', monospace;
      background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0a0a0a 100%);
      color: #00ff88;
      min-height: 100vh;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 40px 20px;
    }
    h1 {
      color: #00ccff;
      font-size: 2.5em;
      margin-bottom: 20px;
      text-shadow: 0 0 20px #00ff88;
    }
    a {
      color: #00ccff;
      text-decoration: none;
    }
    a:hover { color: #00ffff; }
  </style>
</head>`;

return HeadDefault();
```
