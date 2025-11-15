# Components
**UI Components** | Reusable Modules

All components < 250 tokens, compiled via MDCompiler.

## Head Components
- `head-default.md` - Standard page head
- `head-dashboard.md` - Dashboard-specific styles

## Navigation
- `nav-main.md` - Main site navigation
- `nav-tabs.md` - Dashboard tab navigation

## Content
- `landing-hero.md` - Landing page hero section
- `dashboard-frame.md` - Dashboard iframe panels

## Footers
- `footer-default.md` - Standard footer

## Component Format

```javascript
const ComponentName = (params) => {
  return `<html-string>`;
};
return ComponentName();
```

Components are pure functions returning HTML strings.
