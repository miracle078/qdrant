# Template Engine
**UUID:** 3c8e9f7a-4b2d-4e1f-9c6a-8d3f5e7a9b1c
**Perspective-Style** | Markdown → HTML

Renders markdown templates to HTML like Ignition Perspective renders JSON views.

```javascript
const TemplateEngine = {
  templates: new Map(),
  components: new Map(),

  async loadTemplate(name) {
    const response = await fetch(`templates/${name}.md`);
    const markdown = await response.text();
    this.templates.set(name, this.parseTemplate(markdown));
    return this.templates.get(name);
  },

  parseTemplate(markdown) {
    const meta = {};
    const components = [];

    // Extract YAML frontmatter
    const frontmatterMatch = markdown.match(/^---\n([\s\S]*?)\n---/);
    if (frontmatterMatch) {
      const lines = frontmatterMatch[1].split('\n');
      lines.forEach(line => {
        const [key, ...value] = line.split(':');
        if (key && value) meta[key.trim()] = value.join(':').trim();
      });
    }

    // Extract component blocks
    const componentRegex = /##\s+(\w+)\s*\n([\s\S]*?)(?=\n##\s+\w+|\n```|$)/g;
    let match;
    while ((match = componentRegex.exec(markdown)) !== null) {
      components.push({
        type: match[1],
        content: match[2].trim()
      });
    }

    return { meta, components };
  },

  async render(templateName, container = document.body) {
    const template = this.templates.get(templateName) || await this.loadTemplate(templateName);

    const html = template.components.map(comp =>
      this.renderComponent(comp)
    ).join('\n');

    container.innerHTML = html;
    return container;
  },

  renderComponent(component) {
    const renderer = this.components.get(component.type);
    return renderer ? renderer(component) : `<div>${component.content}</div>`;
  },

  registerComponent(type, renderFn) {
    this.components.set(type, renderFn);
  }
};

// Register default components
TemplateEngine.registerComponent('Container', comp =>
  `<div class="container">${comp.content}</div>`
);

TemplateEngine.registerComponent('Header', comp =>
  `<header><h1>${comp.content}</h1></header>`
);

TemplateEngine.registerComponent('Button', comp =>
  `<button>${comp.content}</button>`
);

window.TemplateEngine = TemplateEngine;
```

## Usage

```javascript
await TemplateEngine.loadTemplate('view-dashboard');
await TemplateEngine.render('view-dashboard');

// Register custom component
TemplateEngine.registerComponent('Card', comp => `
  <div class="card">
    <h3>${comp.content}</h3>
  </div>
`);
```
