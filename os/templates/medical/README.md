# Medical Imaging System
**Type:** Medical | DICOM Processing

Complete medical imaging processing system with AlF-DETECT AI analysis.

## Components

1. **DICOM Processing** - `dicom-processing.md`
2. **AlF-DETECT** - `alf-detect.md`
3. **Image Viewer** - `viewer.md`
4. **Study Management** - `study-manager.md`

## Architecture

```
┌─────────────────┐
│  DICOM Loader   │
└────────┬────────┘
         │
┌────────▼────────┐
│ Image Processor │
└────────┬────────┘
         │
┌────────▼────────┐
│   AlF-DETECT    │ ← AI Analysis
└────────┬────────┘
         │
┌────────▼────────┐
│  Result Store   │
└─────────────────┘
```

## Supported Modalities

- **X-Ray** - Digital radiography
- **CT** - Computed tomography  
- **MRI** - Magnetic resonance imaging
- **PET** - Positron emission tomography

## AlF-DETECT

AI-powered early detection for:
- Alzheimer's Disease (brain imaging)
- Autism Spectrum Disorder (structural analysis)

## Quick Start

```javascript
// Load DICOM study
const study = await DICOMLoader.loadStudy('study-001');

// Run AlF-DETECT analysis
const results = await AlfDetect.analyze(study);

// Display results
Viewer.showResults(results);
```

## See Also

- `../../../medical/` - Medical imaging PLC area
- `../../../models/` - AI inference models
- `../../data/` - DICOM storage
