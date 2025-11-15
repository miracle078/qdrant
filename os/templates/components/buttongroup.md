# ButtonGroup Component
**UUID:** 4c9e7f2a-3d8b-4e5f-9a6c-7d5f8e2b3a1c

Group of buttons rendered from markdown list.

```javascript
TemplateEngine.registerComponent('ButtonGroup', comp => {
  const lines = comp.content.split('\n').filter(l => l.trim());

  const buttons = lines.map(line => {
    const match = line.match(/^-\s+\*\*(.+?)\*\*\s+-\s+(.+)$/);
    if (match) {
      const [, label, desc] = match;
      return `
<button class="btn" title="${desc}">
  ${label}
</button>
      `.trim();
    }
    return '';
  }).filter(Boolean).join('\n');

  return `
<div class="button-group">
  ${buttons}
</div>
  `.trim();
});
```

## Usage

```markdown
## ButtonGroup
- **Search** - Execute search
- **Query** - Run query
- **Monitor** - View status
```
