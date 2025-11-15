# Chazon UI System Documentation

## Overview
Complete desktop environment for Chazon OS with φ-balanced (Golden Ratio) design principles.

## Components

### 1. **desktop.md** (84 words)
- **Purpose**: Foundation desktop container
- **φ-Features**: Base layer for all UI elements
- **API**: `ChazonUI.init()`, `addElement()`, `clear()`

### 2. **windows.md** (187 words)
- **Purpose**: Multi-window management
- **φ-Features**:
  - Window cascade uses φ for left positioning: `50 + n * φ`
  - Auto-positioning with golden ratio offset
  - Draggable, minimizable windows with shadow effects
- **API**: `WindowManager.create(title, content, opts)`

### 3. **icons.md** (112 words)
- **Purpose**: Desktop icon grid system
- **φ-Features**:
  - Vertical spacing: `100 * φ` pixels
  - Horizontal spacing: 100 pixels
  - Grid layout: 5 columns
- **API**: `IconManager.create(name, emoji, action)`

### 4. **taskbar.md** (127 words)
- **Purpose**: Bottom taskbar with app management
- **Features**:
  - App launcher menu
  - Window switcher buttons
  - Live clock display
  - φ = 1.618 display
- **API**: `Taskbar.init()`, `addApp(name, win)`

### 5. **theme.md** (127 words)
- **Purpose**: Color theme system
- **φ-Features**: Three φ-balanced color schemes
  - **Default**: Green (#00ff88) on dark gradient
  - **Blue**: Cyan (#0088ff) on blue-dark gradient
  - **Purple**: Magenta (#ff00ff) on purple-dark gradient
- **API**: `ThemeSystem.apply(name)`, `cycle()`

### 6. **index.md** (121 words)
- **Purpose**: System integration and initialization
- **Features**:
  - Orchestrates all component initialization
  - Creates default desktop icons (Terminal, Calculator, Settings, Files)
  - Auto-initialization on desktop ready
- **API**: `ChazonUISystem.init()`

## Integration Flow

```
chazon.html loads modules
    ↓
1. ChazonUI.init() → Creates desktop container
    ↓
2. Taskbar.init() → Adds taskbar to desktop
    ↓
3. ThemeSystem.apply() → Applies default theme
    ↓
4. IconManager.create() → Adds desktop icons
    ↓
5. User clicks icon → WindowManager.create() → Opens window
    ↓
6. Window created → Taskbar.addApp() → Adds to taskbar
```

## φ-Balanced Design Principles

All components use φ = (1 + √5) / 2 ≈ 1.618 (Golden Ratio):

- **Spacing**: Vertical gaps scaled by φ
- **Positioning**: Window cascade offset multiplied by φ
- **Aesthetics**: Visual harmony through golden ratio proportions
- **File Size**: All files < 250 tokens for efficient loading

## Responsive Design

- Desktop fills viewport: `position:fixed; width:100%; height:100%`
- Windows auto-cascade to avoid overlap
- Icons use grid system that adapts to content
- Taskbar fixed to bottom with flexible app list

## Color Scheme

**Primary Colors (Default Theme)**:
- Background: `linear-gradient(135deg, #0a0a0a, #1a1a2e)`
- Primary: `#00ff88` (Chazon green)
- Secondary: `#00cc66`
- Dark: `#0a0a0a`
- Text: `#00ff88`

**Accent Colors**:
- Window shadows: `rgba(0,255,136,0.3)`
- Borders: `2px solid #00ff88`
- Hover states: `rgba(0,255,136,0.1)`

## File Sizes (All < 250 tokens ✓)

| File | Words | Est. Tokens | Status |
|------|-------|-------------|--------|
| desktop.md | 84 | ~109-126 | ✓ |
| icons.md | 112 | ~146-168 | ✓ |
| index.md | 121 | ~157-182 | ✓ |
| taskbar.md | 127 | ~165-191 | ✓ |
| theme.md | 127 | ~165-191 | ✓ |
| windows.md | 187 | ~243-280 | ✓ |

## Usage Example

```javascript
// System auto-initializes via index.md
// Manual usage:

// Create a window
WindowManager.create('My App', '<h1>Hello World</h1>', {
  width: 500,
  height: 400
});

// Add desktop icon
IconManager.create('Browser', '🌐', () => {
  WindowManager.create('Browser', '<p>Web content here</p>');
});

// Change theme
ThemeSystem.cycle(); // Rotates through themes
ThemeSystem.apply('blue'); // Apply specific theme

// Clear desktop
ChazonUI.clear(); // Removes all windows/icons (keeps taskbar)
```

## Client-Side Only

All components are pure JavaScript with inline styles. No external dependencies or server-side code required.

---

**Chazon OS** | חזון | φ=1.618 | Vision through Golden Ratio Computing
