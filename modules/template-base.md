# Base Template
**Dynamic Page Assembly** | Template Engine

Assembles pages from markdown components using state machines.

```javascript
const BaseTemplate = {
  async render(config) {
    const state = PackML.init('PageRender');

    // STARTING state
    PackML.transition(state, 'STARTING');
    const html = ['<!DOCTYPE html><html lang="en">'];

    // EXECUTE state - assemble components
    PackML.transition(state, 'EXECUTE');

    if(config.head) html.push(await this.loadComponent(config.head));
    html.push('<body>');
    if(config.nav) html.push(await this.loadComponent(config.nav));
    if(config.content) html.push(await this.loadComponent(config.content));
    if(config.footer) html.push(await this.loadComponent(config.footer));
    html.push('</body></html>');

    // COMPLETE state
    PackML.transition(state, 'COMPLETE');
    return html.join('\n');
  },

  async loadComponent(path) {
    const md = await fetch(`chazon/components/${path}.md`).then(r => r.text());
    return MDCompiler.compile(md).join('\n');
  }
};

window.BaseTemplate = BaseTemplate;
```
