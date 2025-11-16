# HMI Template System Guide

## Overview

This HMI system implements an **Ignition Perspective-style template system** with JSON-based screen definitions, reusable components, and UUID-based navigation. All screens render from JSON, enabling rapid development and consistent UX across the application.

## Key Features

### 1. UUID-Based Navigation (Path Independent)

Navigation uses UUIDs instead of file paths, making the system portable and refactor-friendly.

**Old way:**
```html
<a href="../screens/oee-entry.html">Go to OEE</a>
```

**New way:**
```html
<a href="#" data-nav-uuid="hmi-oee-entry">Go to OEE</a>
```

### 2. JSON Screen Definitions

Screens are defined as JSON (like Ignition Perspective views):

```json
{
  "type": "ia.container.flex",
  "props": {
    "direction": "column"
  },
  "children": [
    {
      "type": "ia.display.label",
      "props": {
        "text": "My Screen"
      }
    }
  ]
}
```

### 3. Reusable Component Templates

Create templates once, use everywhere with different parameters:

```json
{
  "templateType": "component",
  "name": "NavigationButton",
  "parameters": {
    "targetUuid": { "type": "uuid", "required": true },
    "label": { "type": "string", "required": true }
  }
}
```

### 4. View Inheritance

Base views can be extended by other views (like class inheritance):

```json
{
  "templateType": "base",
  "name": "BaseView",
  "template": {
    "children": [
      { "type": "header" },
      { "type": "content-slot" },
      { "type": "footer" }
    ]
  }
}
```

## Directory Structure

```
HMI/
├── css/
│   └── isa101-theme.css              # ISA-101 compliant theme
├── js/
│   ├── navigation.js                  # UUID navigation system
│   ├── screen-renderer.js             # JSON to HTML renderer
│   └── template-loader.js             # Template instantiation
├── templates/
│   ├── components/                    # Reusable components
│   │   ├── NavigationButton.json
│   │   ├── StatusIndicator.json
│   │   ├── EquipmentCard.json
│   │   └── ValueDisplay.json
│   ├── views/                         # Complete view templates
│   └── base/                          # Base view templates
│       └── BaseView.json
├── screens/
│   ├── json/                          # JSON screen definitions
│   │   ├── overview.json
│   │   ├── oee-dashboard.json
│   │   ├── equipment-overview.json
│   │   └── alarms.json
│   ├── oee-dashboard.html             # HTML renders from JSON
│   ├── equipment-overview.html
│   └── alarms.html
├── screen-registry.json               # UUID to path registry
├── index.html                         # Main entry point
└── README.md
```

## Component Types

### Available Component Types

The renderer supports these Ignition-style component types:

| Type | Description |
|------|-------------|
| `ia.container.flex` | Flexbox container |
| `ia.container.coord` | Absolute positioning container |
| `ia.display.label` | Text label |
| `ia.display.value` | Value display with label and unit |
| `ia.display.table` | Data table |
| `ia.display.state-indicator` | ISA-101 state indicator |
| `ia.display.alarm-table` | Alarm list |
| `ia.input.button` | Button |
| `ia.input.text-field` | Text input |
| `ia.input.numeric-entry-field` | Numeric input |
| `ia.input.dropdown` | Dropdown select |
| `ia.input.date-time-input` | Date/time picker |
| `ia.chart.pie` | Pie chart (placeholder) |
| `ia.chart.bar` | Bar chart (placeholder) |

### Component Properties

Each component has a standard structure:

```json
{
  "type": "ia.display.label",
  "version": "1.0.0",
  "props": {
    "text": "Hello World",
    "style": {
      "fontSize": "24px",
      "color": "var(--text-primary)"
    }
  },
  "meta": {
    "name": "MyLabel"
  },
  "position": {
    "basis": "100px",
    "grow": 1,
    "shrink": 0
  },
  "custom": {
    "myCustomData": "anything"
  }
}
```

## Using Templates

### 1. Create a Component Template

`templates/components/MyButton.json`:

```json
{
  "templateType": "component",
  "name": "MyButton",
  "version": "1.0.0",
  "description": "A custom button component",
  "parameters": {
    "label": {
      "type": "string",
      "required": true,
      "description": "Button text"
    },
    "color": {
      "type": "color",
      "required": false,
      "default": "var(--primary-purple)",
      "description": "Button color"
    },
    "onClick": {
      "type": "string",
      "required": false,
      "default": "",
      "description": "Click handler code"
    }
  },
  "template": {
    "type": "ia.input.button",
    "props": {
      "text": "{label}",
      "style": {
        "background": "{color}",
        "padding": "12px 24px"
      }
    },
    "custom": {
      "onClick": "{onClick}"
    }
  }
}
```

### 2. Use the Template

In JavaScript:

```javascript
// Load and instantiate template
const buttonDef = await hmiTemplates.createComponent('MyButton', {
    label: 'Click Me',
    color: '#10b981',
    onClick: 'alert("Clicked!")'
});

// Render to screen
const renderer = new HMIScreenRenderer('#container');
renderer.renderScreen([buttonDef]);
```

Or reference in a JSON screen definition:

```json
{
  "type": "template:MyButton",
  "params": {
    "label": "Click Me",
    "color": "#10b981"
  }
}
```

### 3. Template Parameters

Templates support parameter substitution with `{paramName}`:

```json
{
  "template": {
    "props": {
      "text": "{label}",
      "style": {
        "color": "{textColor}",
        "fontSize": "{size === 'large' ? '24px' : '16px'}"
      }
    }
  }
}
```

Parameter types:

- `string` - Text values
- `number` - Numeric values
- `boolean` - True/false
- `color` - CSS colors
- `uuid` - Screen UUIDs
- `array` - Arrays of values
- `object` - Nested objects
- `enum` - Restricted values

## Creating Screens

### Method 1: Pure JSON Definition

`screens/json/my-screen.json`:

```json
{
  "type": "ia.container.flex",
  "props": {
    "direction": "column",
    "style": {
      "padding": "20px"
    }
  },
  "children": [
    {
      "type": "ia.display.label",
      "props": {
        "text": "My Screen Title",
        "style": {
          "fontSize": "32px",
          "fontWeight": "bold"
        }
      }
    }
  ]
}
```

`screens/my-screen.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="../css/isa101-theme.css">
</head>
<body>
    <div id="screen-root"></div>
    <script src="../js/navigation.js"></script>
    <script src="../js/screen-renderer.js"></script>
    <script>
        const renderer = new HMIScreenRenderer('#screen-root');
        renderer.loadScreen('json/my-screen.json');
    </script>
</body>
</html>
```

### Method 2: Using Base Templates

```javascript
const screenDef = await hmiTemplates.createBaseView('BaseView', {
    title: 'My Screen',
    subtitle: 'Real-time monitoring',
    icon: '📊'
}, [
    // Content goes here
    {
        type: 'ia.display.label',
        props: {
            text: 'Screen content'
        }
    }
]);

renderer.renderScreen([screenDef]);
```

### Method 3: Composing from Templates

```javascript
// Create components from templates
const navButton1 = await hmiTemplates.createComponent('NavigationButton', {
    targetUuid: 'hmi-overview-main',
    label: 'Home',
    icon: '🏠'
});

const navButton2 = await hmiTemplates.createComponent('NavigationButton', {
    targetUuid: 'hmi-alarms-active',
    label: 'Alarms',
    icon: '🔔'
});

const statusCard = await hmiTemplates.createComponent('EquipmentCard', {
    equipmentName: 'Line 1',
    equipmentId: 'line-1',
    state: 'running',
    metrics: [
        {label: 'Speed', value: '1250', unit: 'units/hr'},
        {label: 'Temp', value: '75.3', unit: '°C'}
    ]
});

// Compose into screen
const screen = {
    type: 'ia.container.flex',
    props: { direction: 'column' },
    children: [navButton1, navButton2, statusCard]
};

renderer.renderScreen([screen]);
```

## UUID-Based Navigation

### 1. Register Screens

`screen-registry.json`:

```json
{
  "screens": {
    "my-custom-screen": {
      "uuid": "my-custom-screen",
      "name": "My Custom Screen",
      "path": "screens/my-screen.html",
      "type": "custom",
      "description": "Description here"
    }
  }
}
```

### 2. Navigate in HTML

```html
<!-- Automatic navigation with data attribute -->
<button data-nav-uuid="my-custom-screen">Go to Screen</button>

<!-- Or use href -->
<a href="#" data-nav-uuid="my-custom-screen">Link</a>
```

### 3. Navigate in JavaScript

```javascript
// Navigate to screen
hmiNav.navigateTo('my-custom-screen');

// Open in new window
hmiNav.navigateTo('my-custom-screen', true);

// Get screen info
const screen = hmiNav.getScreen('my-custom-screen');
console.log(screen.name, screen.path);

// Get all screens of type
const dashboards = hmiNav.getScreensByType('dashboard');
```

## ISA-101 Theme Usage

### Color Variables

```css
/* Use in styles */
.my-element {
    color: var(--text-primary);
    background: var(--bg-surface);
    border-color: var(--primary-purple);
}
```

### CSS Classes

```html
<!-- Alarms -->
<div class="alarm alarm-critical alarm-active">Critical alarm!</div>

<!-- Status indicators -->
<span class="state-indicator state-running">Running</span>

<!-- Buttons -->
<button class="hmi-button hmi-button-primary">Primary</button>
<button class="hmi-button hmi-button-danger">Emergency Stop</button>

<!-- Tables -->
<table class="hmi-table">
  <thead>
    <tr><th>Column</th></tr>
  </thead>
</table>

<!-- Value display -->
<div class="hmi-value-display">
  <span class="hmi-value-label">Temperature</span>
  <span class="hmi-value-number">75.3<span class="hmi-value-unit">°C</span></span>
</div>
```

## Best Practices

### 1. Keep JSON Definitions Clean

```json
// Good - clean structure
{
  "type": "ia.container.flex",
  "props": {
    "direction": "column"
  },
  "children": [...]
}

// Avoid - inline styling
{
  "type": "ia.container.flex",
  "props": {
    "style": {
      "background": "#123456",
      "padding": "10px"
    }
  }
}

// Better - use theme variables
{
  "type": "ia.container.flex",
  "props": {
    "style": {
      "background": "var(--bg-surface)",
      "padding": "var(--spacing-md)"
    }
  }
}
```

### 2. Create Reusable Templates

If you use a pattern more than once, make it a template!

### 3. Use Descriptive UUIDs

```json
// Good
"uuid": "hmi-oee-dashboard-production-line-1"

// Bad
"uuid": "screen-1"
```

### 4. Document Templates

Add good descriptions and examples to your templates:

```json
{
  "description": "Equipment card showing real-time status",
  "example": {
    "equipmentName": "Line 1",
    "state": "running"
  }
}
```

### 5. Follow ISA-101 Standards

- Use standard alarm colors
- Show clear state indicators
- Provide good situational awareness
- High contrast for readability

## Examples

See the `screens/json/` directory for complete examples:

- `overview.json` - Main dashboard with KPIs
- `oee-dashboard.json` - OEE metrics display
- `equipment-overview.json` - Equipment status cards
- `alarms.json` - Alarm management screen

## API Reference

### HMINavigation

```javascript
const hmiNav = new HMINavigation();

// Navigate
hmiNav.navigateTo(uuid, newWindow);

// Get screen info
hmiNav.getScreen(uuid);
hmiNav.getScreensByType(type);
hmiNav.getAllScreens();

// Create nav links
hmiNav.createNavLink(uuid, text, className);
hmiNav.buildNavigationMenu(containerSelector, options);
```

### HMITemplateLoader

```javascript
const hmiTemplates = new HMITemplateLoader();

// Load templates
await hmiTemplates.loadTemplate(type, name);

// Create instances
await hmiTemplates.createComponent(name, params);
await hmiTemplates.createView(name, params, content);
await hmiTemplates.createBaseView(name, params, content);

// Utilities
hmiTemplates.preloadCommonTemplates();
hmiTemplates.clearCache();
```

### HMIScreenRenderer

```javascript
const renderer = new HMIScreenRenderer('#container');

// Load from JSON file
await renderer.loadScreen('path/to/screen.json');

// Render from object
renderer.renderScreen(screenObject);

// Render single component
const element = renderer.renderComponent(componentDef);
```

## Troubleshooting

### Screen doesn't load

1. Check browser console for errors
2. Verify JSON is valid (use a JSON validator)
3. Check that paths are correct in screen-registry.json
4. Ensure all scripts are loaded (navigation.js, template-loader.js, screen-renderer.js)

### Navigation doesn't work

1. Verify UUID exists in screen-registry.json
2. Check that navigation.js is loaded before use
3. Look for console errors about missing screens

### Template parameters not working

1. Check parameter names match exactly
2. Verify required parameters are provided
3. Check template JSON for syntax errors

### Styles not applying

1. Verify isa101-theme.css is loaded
2. Check CSS variable names are correct
3. Use browser dev tools to inspect applied styles

## Further Development

To extend the system:

1. **Add New Component Types**: Extend `HMIScreenRenderer.componentRegistry`
2. **Create New Templates**: Add JSON files to `templates/` directories
3. **Add Screens**: Create JSON in `screens/json/` and register in `screen-registry.json`
4. **Customize Theme**: Modify `css/isa101-theme.css` variables

## Support

For issues or questions, see the main HMI README.md file.
