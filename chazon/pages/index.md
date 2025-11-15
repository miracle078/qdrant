# Pages
**Page Definitions** | Component Config

Page definitions specify which components to assemble.

## Available Pages

### [landing.md](landing.md)
Main landing page with project cards and dashboard button.

### [dashboard.md](dashboard.md)
Unified dashboard with tabbed interface for all demos.

## Page Definition Format

```yaml
---
title: Page Title
components:
  head: component-name
  nav: component-name
  content: component-name
  footer: component-name
params:
  key: value
---
```

Each page definition includes config + render function. PageBuilder assembles components using state machines.
