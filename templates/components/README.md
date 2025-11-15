# Component Library
**UUID:** 9f4a7c2e-5b8d-4f1a-9e6c-7d3a5f8b2c9e
**Perspective-Style** | Reusable UI Components

Component library for template engine, inspired by Ignition Perspective.

## Available Components

### Layout Components
- **Container** - Generic container div
- **Header** - Page header
- **Footer** - Page footer
- **BootScreen** - Terminal-style boot screen

### Interactive Components
- **Button** - Clickable button
- **ButtonGroup** - Group of buttons
- **SearchBar** - Search input with button
- **CheckboxGroup** - Multiple checkboxes

### Display Components
- **Card** - Content card
- **ResultsList** - Search results list
- **BootSequence** - Loading sequence display

## Component Definition Format

Each component is defined in markdown:

```markdown
## ComponentType
content or properties
```

## Registering Custom Components

```javascript
TemplateEngine.registerComponent('MyComponent', comp => {
  return `<div class="my-component">${comp.content}</div>`;
});
```

## Example Template

```markdown
---
title: My View
layout: default
---

## Header
# My Title

## Container
Some content here

## Button
Click Me
```

## Component Properties

Components can have properties in YAML format:

```markdown
## SearchBar
placeholder: "Enter search query"
button: "Search"
action: "handleSearch"
```
