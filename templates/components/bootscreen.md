# BootScreen Component
**UUID:** 8d3f5e9a-2c7b-4f1e-9a6c-5d8f7e3b2a1c

Terminal-style boot screen with ASCII art.

```javascript
TemplateEngine.registerComponent('BootScreen', comp => {
  return `
<div class="boot-screen">
  <pre class="ascii-art">
${comp.content}
  </pre>
</div>
  `.trim();
});
```

## Usage

```markdown
## BootScreen
\`\`\`
┌─────────────────┐
│   CHAZON OS     │
└─────────────────┘
\`\`\`
```
