# Medical Imaging Module
**UUID:** 3d8f6e9a-4c2b-4f1e-9a7c-5d8f7e3b2a6c
**DICOM** | Multi-Modality Support

Templated medical imaging system supporting X-ray, CT, MRI, Ultrasound, PET, and more.

```javascript
const MedicalImaging = {
  modalities: {
    'xray': { name: 'X-Ray', dims: 2, defaultWindow: { level: 40, width: 400 } },
    'ct': { name: 'CT Scan', dims: 3, defaultWindow: { level: 40, width: 400 } },
    'mri': { name: 'MRI', dims: 3, defaultWindow: { level: 128, width: 256 } },
    'us': { name: 'Ultrasound', dims: 2, defaultWindow: { level: 128, width: 256 } },
    'pet': { name: 'PET Scan', dims: 3, defaultWindow: { level: 128, width: 256 } },
    'mammography': { name: 'Mammography', dims: 2, defaultWindow: { level: 50, width: 500 } },
    'fluoro': { name: 'Fluoroscopy', dims: 2, defaultWindow: { level: 40, width: 400 } }
  },

  studies: new Map(),

  createStudy(params) {
    const study = {
      id: this.generateId(),
      modality: params.modality || 'xray',
      patientId: params.patientId || 'UNKNOWN',
      studyDate: params.studyDate || new Date().toISOString(),
      bodyPart: params.bodyPart || 'CHEST',
      series: [],
      metadata: {
        institution: params.institution || 'Chazon Medical',
        operator: params.operator || 'System',
        equipment: params.equipment || 'Virtual Scanner',
        ...params.metadata
      },
      window: params.window || this.modalities[params.modality]?.defaultWindow
    };

    this.studies.set(study.id, study);
    console.log(`✓ Created ${study.modality.toUpperCase()} study: ${study.id}`);
    return study;
  },

  addSeries(studyId, imageData, params = {}) {
    const study = this.studies.get(studyId);
    if (!study) {
      console.error('Study not found:', studyId);
      return null;
    }

    const series = {
      id: this.generateId(),
      seriesNumber: study.series.length + 1,
      imageData,
      slices: params.slices || 1,
      instanceNumber: params.instanceNumber || 1,
      position: params.position || { x: 0, y: 0, z: 0 },
      orientation: params.orientation || 'AXIAL',
      pixelSpacing: params.pixelSpacing || [1, 1],
      sliceThickness: params.sliceThickness || 1,
      rows: params.rows || 512,
      columns: params.columns || 512,
      timestamp: Date.now()
    };

    study.series.push(series);
    console.log(`✓ Added series ${series.id} to study ${studyId}`);
    return series;
  },

  applyWindow(imageData, level, width) {
    // Window/Level adjustment (simplified)
    const min = level - width / 2;
    const max = level + width / 2;

    return imageData.map(value => {
      if (value <= min) return 0;
      if (value >= max) return 255;
      return Math.round(((value - min) / width) * 255);
    });
  },

  applyFilter(imageData, filter) {
    switch (filter) {
      case 'bone':
        return this.applyWindow(imageData, 400, 1800);
      case 'lung':
        return this.applyWindow(imageData, -600, 1500);
      case 'soft_tissue':
        return this.applyWindow(imageData, 40, 400);
      case 'brain':
        return this.applyWindow(imageData, 40, 80);
      case 'liver':
        return this.applyWindow(imageData, 60, 150);
      default:
        return imageData;
    }
  },

  generateReport(studyId) {
    const study = this.studies.get(studyId);
    if (!study) return null;

    const modalityInfo = this.modalities[study.modality];

    return {
      studyId: study.id,
      modality: modalityInfo.name,
      patientId: study.patientId,
      studyDate: study.studyDate,
      bodyPart: study.bodyPart,
      seriesCount: study.series.length,
      totalSlices: study.series.reduce((sum, s) => sum + s.slices, 0),
      metadata: study.metadata,
      findings: study.findings || 'No findings reported',
      impression: study.impression || 'Normal study'
    };
  },

  exportDICOM(studyId) {
    const study = this.studies.get(studyId);
    if (!study) return null;

    // Simplified DICOM export (metadata only)
    return {
      SOPClassUID: '1.2.840.10008.5.1.4.1.1.2',
      StudyInstanceUID: study.id,
      Modality: study.modality.toUpperCase(),
      PatientID: study.patientId,
      StudyDate: study.studyDate.split('T')[0].replace(/-/g, ''),
      BodyPartExamined: study.bodyPart,
      SeriesCount: study.series.length,
      Institution: study.metadata.institution
    };
  },

  list() {
    console.log('═══════════════════════════════════════');
    console.log('MEDICAL IMAGING STUDIES');
    console.log('═══════════════════════════════════════');

    this.studies.forEach((study, id) => {
      const modalityInfo = this.modalities[study.modality];
      console.log(`\n${id}:`);
      console.log(`  Modality: ${modalityInfo.name}`);
      console.log(`  Patient: ${study.patientId}`);
      console.log(`  Body Part: ${study.bodyPart}`);
      console.log(`  Series: ${study.series.length}`);
      console.log(`  Date: ${new Date(study.studyDate).toLocaleDateString()}`);
    });
  },

  generateId() {
    return `${Date.now()}.${Math.random().toString(36).substr(2, 9)}`;
  }
};

window.MedicalImaging = MedicalImaging;
```

## Supported Modalities

- **X-Ray** - 2D radiography
- **CT** - Computed Tomography (3D)
- **MRI** - Magnetic Resonance Imaging (3D)
- **US** - Ultrasound (2D)
- **PET** - Positron Emission Tomography (3D)
- **Mammography** - Breast imaging (2D)
- **Fluoroscopy** - Real-time X-ray (2D)

## Usage

```javascript
// Create X-Ray study
const xrayStudy = MedicalImaging.createStudy({
  modality: 'xray',
  patientId: 'P12345',
  bodyPart: 'CHEST',
  operator: 'Dr. Smith'
});

// Create CT scan study
const ctStudy = MedicalImaging.createStudy({
  modality: 'ct',
  patientId: 'P67890',
  bodyPart: 'HEAD',
  window: { level: 40, width: 80 }  // Brain window
});

// Add image series
MedicalImaging.addSeries(ctStudy.id, imageData, {
  slices: 64,
  orientation: 'AXIAL',
  sliceThickness: 2.5,
  rows: 512,
  columns: 512
});

// Apply filters
const boneView = MedicalImaging.applyFilter(imageData, 'bone');
const lungView = MedicalImaging.applyFilter(imageData, 'lung');

// Generate report
const report = MedicalImaging.generateReport(ctStudy.id);
console.log(report);
```
