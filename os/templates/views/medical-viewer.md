---
title: Medical Imaging Viewer
layout: default
modules: [medical-imaging, dicom-viewer, xray-analyzer]
modality: xray
---

## Header
# Medical Imaging Viewer
**Multi-Modality DICOM Viewer**

## Container
class: "controls-panel"

### Modality Selection

## ButtonGroup
- **X-Ray** - 2D Radiography
- **CT Scan** - Computed Tomography
- **MRI** - Magnetic Resonance
- **Ultrasound** - Sonography
- **PET** - Positron Emission
- **Mammography** - Breast Imaging

## Container
class: "study-info"

### Study Information

**Patient ID:** {{patientId}}
**Study Date:** {{studyDate}}
**Modality:** {{modality}}
**Body Part:** {{bodyPart}}
**Series:** {{seriesCount}}

## Container
class: "viewer-controls"

### Window/Level Controls

**Window Level:** {{windowLevel}}
**Window Width:** {{windowWidth}}

## ButtonGroup
- **Bone** - Bone window
- **Lung** - Lung window
- **Soft Tissue** - Soft tissue window
- **Brain** - Brain window
- **Liver** - Liver window

## Container
class: "image-viewer"

### Image Display

```
[DICOM IMAGE CANVAS]
512 x 512 pixels
Slice: {{currentSlice}} / {{totalSlices}}
```

**Orientation:** {{orientation}}
**Pixel Spacing:** {{pixelSpacing}}
**Slice Thickness:** {{sliceThickness}} mm

## Container
class: "analysis-panel"

### AI Analysis

**Status:** {{analysisStatus}}
**Findings:** {{findings}}
**Confidence:** {{confidence}}%

## ButtonGroup
- **Analyze** - Run AI analysis
- **Report** - Generate report
- **Export** - Export DICOM
- **Annotate** - Add annotations

## Container
class: "series-selector"

### Series Navigation

**Series 1:** Axial (64 slices)
**Series 2:** Sagittal (64 slices)
**Series 3:** Coronal (64 slices)

## Footer
DICOM Viewer | FDA 21 CFR Part 11 Compliant | HIPAA Secure
