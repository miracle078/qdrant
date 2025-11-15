# Templates System
**UUID:** 1a9f4c7e-2d8b-4f5e-9a6c-3d7f8e5b2c1a
**Perspective-Style** | Markdown → HTML

Template system inspired by Ignition Perspective, storing views as markdown and rendering to HTML.

## 📁 Structure

```
templates/
├── views/              # View definitions (pages)
│   ├── dashboard.md
│   ├── chazon.md
│   ├── demo.md
│   ├── medical-viewer.md      # Universal medical viewer
│   ├── xray-template.md       # X-Ray viewer
│   ├── ct-template.md         # CT scan viewer
│   └── mri-template.md        # MRI viewer
│
├── components/         # Component library
│   ├── container.md
│   ├── searchbar.md
│   ├── buttongroup.md
│   └── bootscreen.md
│
├── layouts/            # Page layouts
│   └── default.md
│
├── build.py            # Build script
├── README.md           # This file
└── MEDICAL-IMAGING.md  # Medical imaging guide
```

## 🎯 Concept

Like **Ignition Perspective** stores views as JSON and renders them to HTML/React, our system stores views as **markdown** and renders them to HTML.

### Ignition Perspective
```json
{
  "type": "View",
  "children": [
    {
      "type": "Label",
      "props": {
        "text": "Dashboard"
      }
    }
  ]
}
```

### Our System
```markdown
---
title: Dashboard
---

## Header
# Dashboard

## Container
Content here
```

## 🚀 Quick Start

### Create a View

```markdown
---
title: My View
layout: default
modules: [db-manager, search-hybrid]
---

## Header
# My View Title

## Container
Some content here

## SearchBar
placeholder: "Search..."
button: "Go"
```

### Build HTML

```bash
# Build all templates
python templates/build.py

# Build specific template
python templates/build.py dashboard

# Watch mode (auto-rebuild)
python templates/build.py --watch
```

### Load in Browser

```javascript
await TemplateEngine.loadTemplate('dashboard');
await TemplateEngine.render('dashboard', document.body);
```

## 📦 Components

### Layout Components
- **Container** - Generic container
- **Header** - Page header
- **Footer** - Page footer

### Interactive Components
- **SearchBar** - Search input with button
- **ButtonGroup** - Group of buttons
- **CheckboxGroup** - Multiple checkboxes

### Display Components
- **BootScreen** - Terminal-style boot screen
- **ResultsList** - Search results
- **Card** - Content card

## 🎨 Creating Components

### 1. Define Component

Create `templates/components/mycomponent.md`:

```markdown
# MyComponent
**UUID:** ...

\`\`\`javascript
TemplateEngine.registerComponent('MyComponent', comp => {
  return `<div class="my-component">${comp.content}</div>`;
});
\`\`\`
```

### 2. Load Component

```javascript
await import('./templates/components/mycomponent.md');
```

### 3. Use in Template

```markdown
## MyComponent
Content for my component
```

## 🔧 Advanced Usage

### Component Properties

```markdown
## SearchBar
placeholder: "Search query"
button: "Search"
action: "handleSearch"
```

### Nested Content

```markdown
## Container
class: "main-container"
style: "padding: 20px;"

## Header
# Nested Header

Content here
```

### Dynamic Loading

```javascript
// Load template dynamically
const template = await TemplateEngine.loadTemplate('dashboard');

// Render to specific container
const container = document.getElementById('app');
await TemplateEngine.render('dashboard', container);
```

## 📊 Benefits

### 1. **Markdown-First**
- All views in human-readable markdown
- Version control friendly
- Easy to edit and review

### 2. **Modular**
- Reusable components
- Sub-250 token constraint
- Single responsibility

### 3. **Build-Time or Runtime**
- Pre-build to static HTML
- Or render dynamically in browser
- Flexible deployment

### 4. **ISA Compliant**
- Follows ISA-95 hierarchy
- PackML state machines
- Regulatory ready

## 🔄 Workflow

```
1. Create view template (dashboard.md)
   ↓
2. Define components (searchbar.md, container.md)
   ↓
3. Build HTML (python build.py)
   ↓
4. Deploy (GitHub Pages, CDN, etc.)
   ↓
5. Or render dynamically (TemplateEngine.render())
```

## 📝 Template Frontmatter

```yaml
---
title: Page Title                    # Browser title
layout: default                       # Layout template
modules: [module1, module2]           # Required modules
theme: dark                           # Theme
author: Chazon Team                   # Author
---
```

## 🧪 Testing

```bash
# Test build
python templates/build.py dashboard

# Test in browser
# Open dashboard.html in browser
```

## 📚 Examples

See `views/` for complete examples:
- **dashboard.md** - System dashboard
- **chazon.md** - Boot screen
- **demo.md** - Search demo
- **medical-viewer.md** - Universal medical imaging viewer
- **xray-template.md** - X-Ray viewer with parameters
- **ct-template.md** - CT scan viewer with MPR
- **mri-template.md** - MRI viewer with sequences

See **[MEDICAL-IMAGING.md](MEDICAL-IMAGING.md)** for complete medical imaging documentation.

## 🔗 Integration

Integrates with:
- **Module System** - Load required modules
- **Database Manager** - Query data
- **PackML** - State management
- **Multi-Agent System** - Coordinate agents

## 🎯 Use Cases

1. **Clean HTML** - Replace static HTML with generated files
2. **Dynamic Views** - Render views from database
3. **Multi-Tenancy** - Different views per user
4. **A/B Testing** - Switch templates easily
5. **Documentation** - Auto-generate docs from templates
