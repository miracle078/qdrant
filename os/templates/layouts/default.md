# Default Layout
**UUID:** 6d9f3e8a-4c2b-4f7e-9a5c-7d8f2e3b5a1c

Default page layout for all views.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{title}} | Chazon</title>

  <!-- Core modules -->
  <script src="/modules/packml.md"></script>
  <script src="/modules/template-engine.md"></script>
  <script src="/modules/module-loader.md"></script>

  <!-- Page-specific modules -->
  {{modules}}

  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Courier New', monospace;
      background: linear-gradient(135deg, #0a0a0a, #1a1a2e);
      color: #00ff88;
      padding: 20px;
      line-height: 1.6;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
      background: rgba(26, 26, 46, 0.8);
      border: 1px solid #00ff88;
      border-radius: 8px;
      margin-bottom: 20px;
    }

    header {
      text-align: center;
      padding: 40px 20px;
      border-bottom: 2px solid #00ff88;
      margin-bottom: 40px;
    }

    footer {
      text-align: center;
      padding: 20px;
      border-top: 2px solid #00ff88;
      margin-top: 40px;
      opacity: 0.7;
    }

    button {
      background: transparent;
      border: 2px solid #00ff88;
      color: #00ff88;
      padding: 10px 20px;
      cursor: pointer;
      font-family: 'Courier New', monospace;
      margin: 5px;
      transition: all 0.3s;
    }

    button:hover {
      background: #00ff88;
      color: #0a0a0a;
    }

    .search-bar {
      display: flex;
      gap: 10px;
      margin: 20px 0;
    }

    .search-input {
      flex: 1;
      padding: 10px;
      background: #0a0a0a;
      border: 2px solid #00ff88;
      color: #00ff88;
      font-family: 'Courier New', monospace;
    }

    .boot-screen pre {
      color: #00ff88;
      font-size: 12px;
      line-height: 1.2;
    }
  </style>
</head>
<body>
  {{content}}

  <script>
    // Initialize PackML for page
    PackML.setState('page', 'IDLE');
    console.log('✓ Template rendered: {{title}}');
  </script>
</body>
</html>
```

## Variables

- `{{title}}` - Page title
- `{{modules}}` - Module script tags
- `{{content}}` - Page content
