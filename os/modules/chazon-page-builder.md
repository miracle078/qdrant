# Page Builder
**Dynamic Assembly** | Component-Based Pages

Builds pages from markdown components using PackML state machines.

```javascript
const PageBuilder = {
  async build(pageDef) {
    const state = PackML.create('PageBuild');

    // Parse page definition
    const config = typeof pageDef === 'string'
      ? await this.loadDef(pageDef)
      : pageDef;

    // Load all components
    const parts = {};
    for(const [key, path] of Object.entries(config.components || {})) {
      PackML.setState(state, 'EXECUTE');
      parts[key] = await this.loadComponent(path);
    }

    // Assemble HTML
    PackML.setState(state, 'COMPLETE');
    return this.assemble(parts, config);
  },

  async loadDef(path) {
    const md = await fetch(`chazon/pages/${path}.md`).then(r => r.text());
    const lines = md.split('\n');
    const yaml = lines.filter(l => l.startsWith('---')).join('\n');
    return YAML.parse(yaml);
  },

  async loadComponent(path) {
    const md = await fetch(`chazon/components/${path}.md`).then(r => r.text());
    const blocks = MDCompiler.compile(md);
    return blocks[0]?.output || '';
  },

  assemble(parts, config) {
    return `<!DOCTYPE html>
<html>
${parts.head || ''}
<body>
${parts.nav || ''}
${parts.content || ''}
${parts.footer || ''}
</body>
</html>`;
  }
};

window.PageBuilder = PageBuilder;
```
