---
title: X-Ray Viewer
layout: default
modules: [medical-imaging, xray-analyzer]
modality: xray
bodyPart: CHEST
---

## Header
# X-Ray Viewer
**2D Radiography** | {{bodyPart}}

## Container
class: "patient-info"

### Patient Information

**ID:** {{patientId}}
**Age:** {{patientAge}}
**Gender:** {{patientGender}}
**Date:** {{studyDate}}

## Container
class: "xray-viewer"

### X-Ray Image

```
[X-RAY IMAGE CANVAS]
2048 x 2048 pixels
View: {{view}}
```

**Exposure:** {{kvp}} kVp, {{mas}} mAs
**SID:** {{sid}} cm
**Grid:** {{grid}}

## Container
class: "view-options"

### View Options

## CheckboxGroup
- **PA** - Posteroanterior
- **AP** - Anteroposterior
- **Lateral** - Side view
- **Oblique** - Angled view

## Container
class: "enhancement"

### Image Enhancement

**Brightness:** {{brightness}}%
**Contrast:** {{contrast}}%
**Invert:** {{inverted}}

## ButtonGroup
- **Auto** - Auto-adjust
- **Bone** - Bone enhancement
- **Soft** - Soft tissue
- **Reset** - Reset to original

## Container
class: "findings"

### Findings

**Lungs:** {{lungFindings}}
**Heart:** {{heartFindings}}
**Bones:** {{boneFindings}}
**Other:** {{otherFindings}}

## Container
class: "measurements"

### Measurements

**Cardiothoracic Ratio:** {{ctr}}
**Costophrenic Angles:** {{angles}}
**Tracheal Position:** {{trachea}}

## ButtonGroup
- **Measure** - Add measurement
- **Annotate** - Add annotation
- **Compare** - Compare with previous
- **Report** - Generate report

## Footer
X-Ray Imaging System | Radiation Safety Compliant
