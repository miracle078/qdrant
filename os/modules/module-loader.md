# Module Loader
**Dynamic Module System** | Markdown-to-JS Execution

Load and execute JavaScript modules from markdown files with caching.

```javascript
const ModuleLoader = {
  cache: new Map(),
  baseURL: '/modules/',

  async load(moduleName) {
    if (this.cache.has(moduleName)) {
      return this.cache.get(moduleName);
    }

    try {
      const response = await fetch(`${this.baseURL}${moduleName}.md`);
      if (!response.ok) {
        throw new Error(`Module ${moduleName} not found`);
      }

      const markdown = await response.text();
      const jsCode = this.extractJS(markdown);

      eval(jsCode);

      const exportName = this.getExportName(markdown, moduleName);
      const module = window[exportName];

      this.cache.set(moduleName, module);
      console.log(`✓ ${moduleName} → ${exportName}`);

      return module;
    } catch (error) {
      console.error(`Failed: ${moduleName}`, error);
      throw error;
    }
  },

  extractJS(markdown) {
    const regex = /```(?:javascript|js)\s*\n([\s\S]*?)```/g;
    const blocks = [];
    let match;

    while ((match = regex.exec(markdown)) !== null) {
      blocks.push(match[1].trim());
    }

    return blocks.join('\n\n');
  },

  getExportName(markdown, moduleName) {
    const match = markdown.match(/window\.(\w+)\s*=/);
    if (match) return match[1];

    return moduleName
      .split('-')
      .map(p => p.charAt(0).toUpperCase() + p.slice(1))
      .join('');
  },

  async loadAll(names) {
    const results = await Promise.allSettled(
      names.map(n => this.load(n))
    );

    const loaded = results.filter(r => r.status === 'fulfilled').length;
    const failed = results.filter(r => r.status === 'rejected').length;

    console.log(`📦 ${loaded} loaded, ${failed} failed`);
    return { loaded, failed, results };
  }
};

window.ModuleLoader = ModuleLoader;
```
