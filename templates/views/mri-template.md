---
title: MRI Viewer
layout: default
modules: [medical-imaging, dicom-viewer]
modality: mri
bodyPart: BRAIN
---

## Header
# MRI Viewer
**Magnetic Resonance Imaging** | {{bodyPart}}

## Container
class: "sequence-info"

### Sequence Information

**Sequence:** {{sequence}}
**Weighting:** {{weighting}}
**TR:** {{tr}} ms
**TE:** {{te}} ms
**Flip Angle:** {{flipAngle}}°

## Container
class: "mri-viewer"

### MRI Images

```
┌─────────────┬─────────────┬─────────────┐
│     T1      │     T2      │    FLAIR    │
│  (256x256)  │  (256x256)  │  (256x256)  │
│ Slice {{t1Slice}}   │ Slice {{t2Slice}}   │ Slice {{flSlice}}    │
└─────────────┴─────────────┴─────────────┘
┌─────────────┬─────────────┬─────────────┐
│     DWI     │     ADC     │  CONTRAST   │
│  (256x256)  │  (256x256)  │  (256x256)  │
│ Slice {{dwiSlice}}  │ Slice {{adcSlice}}  │ Slice {{conSlice}}   │
└─────────────┴─────────────┴─────────────┘
```

## Container
class: "sequence-select"

### Sequence Selection

## ButtonGroup
- **T1** - T1-weighted
- **T2** - T2-weighted
- **FLAIR** - Fluid-attenuated
- **DWI** - Diffusion-weighted
- **T2*** - Gradient echo
- **PWI** - Perfusion

## Container
class: "mri-params"

### Imaging Parameters

**Field Strength:** {{fieldStrength}} Tesla
**Coil:** {{coil}}
**Matrix:** {{matrix}}
**FOV:** {{fov}} mm
**Slice Gap:** {{gap}} mm

## Container
class: "analysis-mri"

### MRI Analysis

**Signal Intensity:** {{signal}}
**Tissue Type:** {{tissue}}
**Abnormality:** {{abnormality}}

**White Matter:** Normal
**Gray Matter:** Normal
**CSF:** Normal

## Container
class: "measurements-mri"

### Volumetric Measurements

**Brain Volume:** {{brainVol}} cm³
**Lesion Volume:** {{lesionVol}} cm³
**Ventricle Size:** {{ventricleSize}} mm

## ButtonGroup
- **Segment** - Tissue segmentation
- **Track** - Fiber tracking
- **Perfusion** - Perfusion map
- **Spectroscopy** - MR spectroscopy
- **Report** - Generate report

## Footer
MRI System | {{fieldStrength}}T | No ionizing radiation
