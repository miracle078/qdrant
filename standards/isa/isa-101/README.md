# ISA-101: Human-Machine Interface Design

**Full Name:** ANSI/ISA-101 - Human Machine Interfaces for Process Automation Systems
**Scope:** HMI design guidelines, situational awareness, alarm management
**Application:** Medical imaging viewer, SCADA displays, operator interfaces

## High Performance HMI Principles

### 1. Situational Awareness
Users must quickly understand:
- **Current state** - What's happening now?
- **Abnormalities** - What's wrong?
- **Actions needed** - What should I do?

### 2. Information Hierarchy
```
Level 1: Overview Display (1-2 sec comprehension)
   ↓
Level 2: Area Display (5-10 sec comprehension)
   ↓
Level 3: Detailed Display (30-60 sec comprehension)
   ↓
Level 4: Diagnostic/Trend Display (detailed analysis)
```

### 3. Visual Design Standards

**Color Usage:**
- **Gray (#888)** - Normal operation (most of the screen)
- **Green (#00ff88)** - Active/running state
- **Yellow (#ffaa00)** - Warning/caution
- **Red (#ff0044)** - Alarm/fault/critical
- **Blue (#00ccff)** - Information/advisory
- **White** - Text on dark background

**Avoid:**
- Rainbow colors
- Decorative graphics
- Unnecessary animations
- Information overload

## Display Hierarchy in Chazon

### Level 1: Overview (SCADA Gateway)
**File:** `index.html`, `scada.html`

**Purpose:** Entire factory status at a glance
**Refresh:** 1-2 seconds
**Information:**
- 8 PLC areas with status indicators
- System-wide metrics (CPU, memory)
- Active alarms count
- Production line status

**Design:**
- Minimal text
- Status colors (green/yellow/red)
- Live clock
- Single-page overview

### Level 2: Area Overview
**Files:** `frontend/index.html`, `backend/index.html`, etc.

**Purpose:** Specific area status
**Refresh:** 2-5 seconds
**Information:**
- Area-specific modules
- Scan times
- Tag counts
- Local alarms

**Design:**
- Navigation breadcrumb
- Module status cards
- Quick actions

### Level 3: Detailed Control
**Files:** `medical/alf-detect.html`, `debug/index.html`

**Purpose:** Specific function control
**Refresh:** 5-10 seconds
**Information:**
- Detailed parameters
- Control inputs
- Results/outputs
- Configuration options

**Design:**
- Form controls
- Result tables
- Charts/graphs
- Help text

### Level 4: Diagnostic
**Files:** `debug/index.html`, `boot/index.html`

**Purpose:** Troubleshooting and analysis
**Refresh:** On-demand
**Information:**
- System logs
- Performance metrics
- Module internals
- Raw data views

**Design:**
- Console output
- Performance graphs
- Detailed tables
- Export functions

## Alarm Management (ISA-18.2)

### Alarm States
- **UNACKNOWLEDGED** - Red, flashing
- **ACKNOWLEDGED** - Red, steady
- **CLEARED** - Removed from active list
- **SHELVED** - Temporarily suppressed

### Alarm Priority
1. **Critical** - Safety/system failure (immediate action)
2. **High** - Process deviation (urgent action)
3. **Medium** - Degraded performance (timely action)
4. **Low** - Advisory (awareness only)

### Chazon Alarm Implementation

```javascript
// scada.html
const alarms = [
  { id: 1, priority: 'critical', message: 'GPU out of memory', state: 'unack' },
  { id: 2, priority: 'high', message: 'Qdrant connection lost', state: 'unack' },
  { id: 3, priority: 'medium', message: 'Slow inference (>5s)', state: 'ack' },
  { id: 4, priority: 'low', message: 'Cache 80% full', state: 'ack' }
];
```

### Alarm Flooding Prevention
- Max 10 alarms per 10 minutes (normal operation)
- Group related alarms
- Root cause prioritization
- Auto-shelve transient alarms

## Navigation Design

### Golden Rules
1. **3-click rule** - Any screen in ≤3 clicks
2. **Breadcrumbs** - Always show location
3. **Home button** - Quick return to overview
4. **Consistent layout** - Same structure across screens

### Chazon Navigation

```
Home (index.html)
├── SCADA Master (scada.html)
├── PLC Controller (plc.html)
├── HMI Panel (hmi.html)
├── Frontend Area
│   └── Medical Viewer
├── Backend Area
│   └── API Status
├── Medical Area
│   └── AlF-DETECT
├── Debug Area
│   └── Debug Console
└── ... 4 more areas
```

## Screen Layout Standards

### Anatomy of ISA-101 Screen

```
┌─────────────────────────────────────────────────┐
│ Header: Plant/Area/Screen Name    [User] [Time] │ ← Always visible
├─────────────────────────────────────────────────┤
│ Breadcrumb: Home > Area > Screen                │ ← Navigation
├─────────────────────────────────────────────────┤
│                                                  │
│                                                  │
│           Main Process Graphic                   │ ← 70% of screen
│           or Control Panel                       │
│                                                  │
│                                                  │
├─────────────────────────────────────────────────┤
│ Status Bar: Alarms [3] | Mode: AUTO | Scan: 50ms│ ← Key metrics
└─────────────────────────────────────────────────┘
```

### Chazon Implementation

**header section:**
- System name + icon
- Online status with pulsing indicator
- Live clock

**Breadcrumb:**
- Always present
- Links back to previous levels

**Main area:**
- Process graphic (canvas-based flow diagram)
- OR control grid (button layout)
- OR data table (module list)

**Footer/Status:**
- Alarm summary
- System metrics
- Quick links

## Typography

### Font Hierarchy
- **Headers:** 2-2.5em, bold
- **Body:** 1em (14-16px), regular
- **Labels:** 0.8-0.9em, medium
- **Status:** 0.8em, monospace

### Readability
- **Line height:** 1.5x font size
- **Contrast:** 4.5:1 minimum (WCAG AA)
- **Font:** Monospace for terminals, sans-serif for UI

## Control Element Design

### Buttons
- **Primary action:** Green background, high contrast
- **Secondary action:** Gray background, border
- **Danger action:** Red background (E-STOP, delete)
- **Disabled:** Low opacity, no hover

### Indicators
- **Running:** Green circle, solid
- **Warning:** Yellow circle, solid
- **Alarm:** Red circle, flashing
- **Offline:** Gray circle, solid

### Input Fields
- **Normal:** Gray border
- **Focus:** Green border
- **Error:** Red border
- **Read-only:** Darker background

## Medical Imaging HMI

### DICOM Viewer Specific
- **Window/Level controls** - Sliders with presets
- **MPR (Multi-Planar Reconstruction)** - 3 orthogonal views
- **Measurement tools** - Distance, angle, area, HU
- **Annotations** - Arrows, text, ROI
- **Cine mode** - Play/pause for 3D/4D datasets

### AI Analysis Display
- **Confidence meters** - 0-100% gauges
- **Heatmaps** - Overlay on image
- **Finding list** - Table with severity
- **Comparison view** - Similar cases side-by-side

## Accessibility (WCAG 2.1)

### Requirements
- **Keyboard navigation** - Tab order, shortcuts
- **Screen reader support** - ARIA labels
- **High contrast mode** - User preference
- **Zoom support** - Up to 200%

## Performance Targets

- **Initial load:** <2 seconds
- **Screen transition:** <0.5 seconds
- **Control response:** <100ms
- **Data refresh:** 1-10 seconds (context-dependent)

## See Also

- `hmi.html` - Master HMI implementation
- `scada.html` - High-level overview display
- `frontend/index.html` - Medical viewer HMI
- `debug/index.html` - Diagnostic display
- `standards/isa/isa-88/` - Procedural state displays
- `standards/isa/isa-95/` - Information hierarchy
