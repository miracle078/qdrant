# HMI (Human-Machine Interface) System

A modern, ISA-101 compliant HMI system with JSON-based screen definitions and UUID-based navigation.

## Overview

This HMI system provides a complete solution for industrial automation interfaces with:

- **JSON-Based Screen Definitions**: All screens are defined as JSON files (similar to Ignition Perspective)
- **UUID-Based Navigation**: Path-independent navigation system using UUIDs
- **ISA-101 Compliance**: Follows ISA-101 standards for colors, alarms, and UX
- **Purple & Cream Theme**: Modern, professional color scheme with high contrast
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Architecture

### No Python Files Policy

**IMPORTANT**: This HMI system does NOT use Python files. All code is either:
- HTML/CSS/JavaScript for the frontend
- JSON for configuration and screen definitions
- Markdown files with code blocks for CLI documentation

If you need Python functionality, it should be:
1. Moved to the CLI directory
2. Documented as markdown with code blocks
3. Parsed by existing markdown parsers

This keeps the HMI system pure web-based and portable.

## Directory Structure

```
HMI/
├── css/
│   └── isa101-theme.css          # Centralized ISA-101 theme
├── js/
│   ├── navigation.js              # UUID-based navigation system
│   └── screen-renderer.js         # JSON screen renderer
├── screens/
│   ├── json/                      # JSON screen definitions
│   │   ├── overview.json
│   │   ├── oee-entry.json
│   │   ├── equipment.json
│   │   └── ...
│   ├── overview.html              # Rendered HTML screens
│   ├── oee-entry.html
│   └── ...
├── screen-registry.json           # UUID to path mapping
├── index.html                     # Main HMI entry point
└── README.md                      # This file
```

## Key Features

### 1. UUID-Based Navigation

Instead of hardcoding file paths, all navigation uses UUIDs:

```html
<!-- Old way (path-dependent) -->
<a href="../screens/oee-entry.html">OEE Entry</a>

<!-- New way (path-independent) -->
<a href="#" data-nav-uuid="hmi-oee-entry">OEE Entry</a>
```

**Benefits**:
- Move files without breaking links
- Centralized path management
- Easy to refactor directory structure
- Better for version control

### 2. JSON Screen Definitions

Screens are defined as JSON (similar to Ignition Perspective views):

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
        "text": "OEE Dashboard"
      }
    }
  ]
}
```

### 3. ISA-101 Compliant Theme

The theme follows ISA-101 standards:

**Alarm Colors**:
- 🔴 Red (`--alarm-critical`): Critical/Emergency alarms
- 🟠 Orange (`--alarm-high`): High priority alarms
- 🟡 Yellow (`--alarm-medium`): Medium priority alarms
- 🔵 Blue (`--alarm-low`): Low/Advisory alarms
- ⚪ Gray (`--alarm-acknowledged`): Acknowledged alarms

**Equipment States**:
- 🟢 Green (`--state-running`): Running/Normal
- ⚪ Gray (`--state-stopped`): Stopped
- 🟣 Purple (`--state-manual`): Manual mode
- 🔵 Blue (`--state-auto`): Auto mode
- 🟠 Orange (`--state-maintenance`): Maintenance
- 🔴 Red (`--state-fault`): Fault condition

## Usage

### Creating a New Screen

1. **Define the JSON** in `screens/json/your-screen.json`:

```json
{
  "type": "ia.container.flex",
  "version": 0,
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
        "text": "My Screen Title"
      }
    }
  ]
}
```

2. **Register the screen** in `screen-registry.json`:

```json
{
  "screens": {
    "your-screen-uuid": {
      "uuid": "your-screen-uuid",
      "name": "Your Screen Name",
      "path": "screens/your-screen.html",
      "type": "custom",
      "description": "Description of your screen"
    }
  }
}
```

3. **Create the HTML renderer** in `screens/your-screen.html` that loads the JSON

### Navigating Between Screens

Use the UUID-based navigation system:

**In HTML**:
```html
<!-- Automatic navigation with data attribute -->
<button data-nav-uuid="hmi-oee-entry">Go to OEE Entry</button>

<!-- Or use JavaScript -->
<button onclick="hmiNav.navigateTo('hmi-oee-entry')">Go to OEE Entry</button>
```

**In JavaScript**:
```javascript
// Navigate to a screen
hmiNav.navigateTo('hmi-oee-entry');

// Open in new window
hmiNav.navigateTo('hmi-oee-entry', true);

// Get screen info
const screen = hmiNav.getScreen('hmi-oee-entry');
console.log(screen.name, screen.path);

// Get all screens of a type
const dashboards = hmiNav.getScreensByType('dashboard');
```

### Using the Theme

Include the theme in your HTML:

```html
<link rel="stylesheet" href="../css/isa101-theme.css">
```

Then use the CSS classes:

```html
<!-- Alarm display -->
<div class="alarm alarm-critical alarm-active">
  Critical temperature alarm!
</div>

<!-- Equipment state -->
<span class="state-indicator state-running">Running</span>

<!-- Buttons -->
<button class="hmi-button hmi-button-primary">Start Process</button>
<button class="hmi-button hmi-button-danger">Emergency Stop</button>

<!-- Value display -->
<div class="hmi-value-display">
  <span class="hmi-value-label">Temperature</span>
  <span class="hmi-value-number">
    75.3
    <span class="hmi-value-unit">°C</span>
  </span>
</div>
```

## ISA-101 Standards Applied

This HMI system follows ISA-101 (Human Machine Interfaces for Process Automation Systems) standards:

1. **Situational Awareness**: Clear visual hierarchy showing normal vs abnormal states
2. **Alarm Management**: Standard color coding and prioritization
3. **Navigation**: Consistent navigation patterns across all screens
4. **Readability**: High contrast, appropriate font sizes, reduced eye strain
5. **Operator Efficiency**: Minimal clicks, logical grouping, quick access to critical functions

## Color Palette

### Primary Colors
- Purple: `#6B46C1` (Brand primary)
- Cream: `#F5F3E8` (Background/text)

### Functional Colors
All colors are ISA-101 compliant and provide proper contrast for 24/7 operation.

See `css/isa101-theme.css` for the complete color system.

## Browser Compatibility

- Chrome/Edge: ✅ Fully supported
- Firefox: ✅ Fully supported
- Safari: ✅ Fully supported
- IE11: ❌ Not supported (use modern browser)

## Performance

- Lazy loading for screens
- Minimal dependencies (vanilla JavaScript)
- Optimized CSS with CSS variables
- Efficient rendering with modern browser APIs

## Security

- No inline scripts (CSP compatible)
- Input validation on all forms
- Secure navigation (no eval or dynamic script injection)

## Future Enhancements

- [ ] Real-time data binding with WebSocket
- [ ] User authentication and role-based access
- [ ] Audit logging
- [ ] Screen builder UI
- [ ] Mobile app wrapper
- [ ] Offline mode support

## Contributing

When adding new screens:
1. Follow ISA-101 color standards
2. Use UUID-based navigation
3. Define screens as JSON when possible
4. Document in screen registry
5. Test on multiple screen sizes
6. Remember: **No Python files** - use HTML/CSS/JS or document as Markdown

## License

See main repository LICENSE file.

## Support

For issues or questions, see the main project documentation.
