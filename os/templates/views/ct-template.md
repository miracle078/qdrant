---
title: CT Scan Viewer
layout: default
modules: [medical-imaging, dicom-viewer]
modality: ct
bodyPart: HEAD
---

## Header
# CT Scan Viewer
**3D Computed Tomography** | {{bodyPart}}

## Container
class: "scan-info"

### Scan Parameters

**Protocol:** {{protocol}}
**Slice Thickness:** {{sliceThickness}} mm
**Reconstruction:** {{reconstruction}}
**Contrast:** {{contrast}}

## Container
class: "ct-viewer-3d"

### Multi-Planar Reconstruction

```
┌─────────────┬─────────────┐
│   AXIAL     │  SAGITTAL   │
│  (512x512)  │  (512x512)  │
│ Slice {{axialSlice}}    │ Slice {{sagSlice}}     │
└─────────────┴─────────────┘
┌─────────────┬─────────────┐
│  CORONAL    │  3D RENDER  │
│  (512x512)  │  (Volume)   │
│ Slice {{corSlice}}     │  {{angle}}°     │
└─────────────┴─────────────┘
```

## Container
class: "window-presets"

### Window Presets

## ButtonGroup
- **Bone** - L: 400, W: 1800
- **Lung** - L: -600, W: 1500
- **Soft Tissue** - L: 40, W: 400
- **Brain** - L: 40, W: 80
- **Liver** - L: 60, W: 150
- **Custom** - Set custom window

## Container
class: "slice-controls"

### Slice Navigation

**Current Slice:** {{currentSlice}} / {{totalSlices}}
**Position:** {{position}} mm
**Orientation:** {{orientation}}

**Scroll** to navigate | **+/-** to zoom | **Pan** to move

## Container
class: "hounsfield"

### Hounsfield Units

**Cursor Value:** {{huValue}} HU
**Mean:** {{meanHU}} HU
**StdDev:** {{stdDevHU}}

**Air:** -1000 HU
**Water:** 0 HU
**Bone:** +1000 HU

## Container
class: "findings-ct"

### Radiological Findings

**Density:** {{density}}
**Size:** {{size}} mm
**Location:** {{location}}
**Characteristics:** {{characteristics}}

## ButtonGroup
- **Segment** - Auto-segment
- **Measure** - Add measurement
- **3D** - 3D reconstruction
- **MPR** - Multi-planar reformat
- **Report** - Generate report

## Footer
CT Scanner | Dose: {{dose}} mGy | Scan Time: {{scanTime}}s
