# Medical Imaging Templates
**DICOM-Compliant Multi-Modality Viewer Templates**

Templated medical imaging system with support for X-Ray, CT, MRI, Ultrasound, PET, and more.

## 📁 Template Files

### Core Module
- **`../modules/medical-imaging.md`** - Medical imaging engine with multi-modality support

### View Templates
- **`views/medical-viewer.md`** - Universal medical imaging viewer
- **`views/xray-template.md`** - X-Ray specific viewer
- **`views/ct-template.md`** - CT scan viewer with MPR
- **`views/mri-template.md`** - MRI viewer with sequences

## 🏥 Supported Modalities

### X-Ray (XR)
- 2D radiography
- PA, AP, Lateral, Oblique views
- Bone and soft tissue enhancement
- Cardiothoracic ratio measurements

### CT Scan (CT)
- 3D computed tomography
- Multi-planar reconstruction (MPR)
- Hounsfield unit measurements
- Window presets (bone, lung, brain, liver, soft tissue)
- Volume rendering

### MRI
- Multiple sequences (T1, T2, FLAIR, DWI, ADC)
- No ionizing radiation
- Tissue segmentation
- Volumetric measurements
- Diffusion and perfusion imaging

### Other Modalities
- **Ultrasound (US)** - Real-time sonography
- **PET Scan (PT)** - Metabolic imaging
- **Mammography (MG)** - Breast imaging
- **Fluoroscopy (FL)** - Real-time X-ray

## 🎯 Quick Start

### Create a Study

```javascript
// X-Ray study
const xrayStudy = MedicalImaging.createStudy({
  modality: 'xray',
  patientId: 'P12345',
  bodyPart: 'CHEST',
  operator: 'Dr. Smith'
});

// CT study
const ctStudy = MedicalImaging.createStudy({
  modality: 'ct',
  patientId: 'P67890',
  bodyPart: 'HEAD',
  window: { level: 40, width: 80 }
});

// MRI study
const mriStudy = MedicalImaging.createStudy({
  modality: 'mri',
  patientId: 'P24680',
  bodyPart: 'BRAIN',
  metadata: {
    fieldStrength: '3T',
    sequence: 'T1-MPRAGE'
  }
});
```

### Add Image Data

```javascript
MedicalImaging.addSeries(ctStudy.id, imageData, {
  slices: 64,
  orientation: 'AXIAL',
  sliceThickness: 2.5,
  rows: 512,
  columns: 512,
  pixelSpacing: [0.5, 0.5]
});
```

### Apply Window/Level

```javascript
// Bone window
const boneView = MedicalImaging.applyFilter(imageData, 'bone');

// Lung window
const lungView = MedicalImaging.applyFilter(imageData, 'lung');

// Brain window
const brainView = MedicalImaging.applyFilter(imageData, 'brain');

// Custom window
const customView = MedicalImaging.applyWindow(imageData, 40, 400);
```

### Generate Report

```javascript
const report = MedicalImaging.generateReport(ctStudy.id);
console.log(report);
// {
//   studyId: '...',
//   modality: 'CT Scan',
//   patientId: 'P67890',
//   bodyPart: 'HEAD',
//   seriesCount: 3,
//   totalSlices: 192,
//   findings: '...'
// }
```

## 📊 Window/Level Presets

### CT Presets
```javascript
'bone':        { level: 400,  width: 1800 }
'lung':        { level: -600, width: 1500 }
'soft_tissue': { level: 40,   width: 400 }
'brain':       { level: 40,   width: 80 }
'liver':       { level: 60,   width: 150 }
```

### X-Ray Presets
```javascript
'default':     { level: 40,   width: 400 }
'bone':        { level: 50,   width: 500 }
'soft':        { level: 30,   width: 300 }
```

## 🔧 Template Parameters

### Common Parameters
```yaml
modality: xray | ct | mri | us | pet | mammography | fluoro
patientId: string
studyDate: ISO date string
bodyPart: CHEST | HEAD | ABDOMEN | SPINE | etc.
operator: string
institution: string
```

### X-Ray Parameters
```yaml
kvp: number          # Kilovolt peak
mas: number          # Milliampere-seconds
sid: number          # Source-to-image distance
grid: boolean        # Anti-scatter grid
view: PA | AP | LAT | OBL
```

### CT Parameters
```yaml
sliceThickness: number    # mm
protocol: string
reconstruction: string
contrast: boolean
windowLevel: number
windowWidth: number
```

### MRI Parameters
```yaml
fieldStrength: 1.5T | 3T | 7T
sequence: T1 | T2 | FLAIR | DWI | etc.
tr: number           # Repetition time (ms)
te: number           # Echo time (ms)
flipAngle: number    # degrees
coil: string
```

## 📝 Template Usage

### Build X-Ray Viewer
```bash
python templates/build.py xray-template
```

### Build CT Viewer
```bash
python templates/build.py ct-template
```

### Build MRI Viewer
```bash
python templates/build.py mri-template
```

### Dynamic Rendering
```javascript
await TemplateEngine.loadTemplate('xray-template');
await TemplateEngine.render('xray-template', container, {
  patientId: 'P12345',
  bodyPart: 'CHEST',
  view: 'PA',
  kvp: 120,
  mas: 5
});
```

## 🔬 Integration with AI Analysis

```javascript
// Analyze X-Ray
const analysis = await XRayAnalyzer.analyze(imageData);

// Render with findings
await TemplateEngine.render('xray-template', container, {
  patientId: 'P12345',
  findings: analysis.findings,
  confidence: analysis.confidence,
  abnormalities: analysis.abnormalities
});
```

## 📋 DICOM Export

```javascript
const dicomData = MedicalImaging.exportDICOM(studyId);
// {
//   SOPClassUID: '1.2.840.10008.5.1.4.1.1.2',
//   StudyInstanceUID: '...',
//   Modality: 'CT',
//   PatientID: 'P67890',
//   ...
// }
```

## 🏗️ Architecture

```
Medical Imaging System
├── modules/medical-imaging.md    # Core engine
├── templates/views/
│   ├── medical-viewer.md         # Universal viewer
│   ├── xray-template.md          # X-Ray viewer
│   ├── ct-template.md            # CT viewer
│   └── mri-template.md           # MRI viewer
└── Integration
    ├── XRayAnalyzer              # AI analysis
    ├── DicomViewer               # DICOM rendering
    └── TemplateEngine            # Template rendering
```

## ✅ Compliance

- **FDA 21 CFR Part 11** - Electronic records
- **HIPAA** - Patient data security
- **DICOM** - Medical imaging standard
- **HL7** - Healthcare data exchange

## 🎨 Customization

Create custom modality template:

```markdown
---
title: Custom Scan Viewer
modality: custom
bodyPart: CUSTOM
---

## Header
# Custom Scan Viewer

## Container
### Your custom layout here
```

## 📚 References

- DICOM Standard: https://www.dicomstandard.org/
- Hounsfield Units: https://radiopaedia.org/articles/hounsfield-unit
- MRI Sequences: https://radiopaedia.org/articles/mri-sequences-overview

---

**Medical Imaging Templates** | DICOM-Compliant | Multi-Modality Support
