# Container Component
**UUID:** 7e9f2a4c-6d3b-4f8e-9a5c-8d7f3e2b1a9c

Generic container for grouping content.

```javascript
TemplateEngine.registerComponent('Container', comp => {
  const classes = comp.props?.class || 'container';
  const style = comp.props?.style || '';

  return `
<div class="${classes}" style="${style}">
  ${comp.content}
</div>
  `.trim();
});
```

## Usage

```markdown
## Container
Your content here
```

## With Properties

```markdown
## Container
class: "container-fluid"
style: "background: #1a1a2e; padding: 20px;"

Content goes here
```
