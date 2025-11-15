# Medical Dataset
**Sample X-Rays** | Training Data

Sample medical imaging dataset for testing and demonstration.

```javascript
const MedicalDataset = {
  samples: [
    {
      id: 'chest-001',
      modality: 'X-RAY',
      bodyPart: 'CHEST',
      view: 'PA',
      diagnosis: 'Normal',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23222"/></svg>'
    },
    {
      id: 'chest-002',
      modality: 'X-RAY',
      bodyPart: 'CHEST',
      view: 'PA',
      diagnosis: 'Pneumonia',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23333"/></svg>'
    },
    {
      id: 'chest-003',
      modality: 'X-RAY',
      bodyPart: 'CHEST',
      view: 'LAT',
      diagnosis: 'Normal',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23444"/></svg>'
    },
    {
      id: 'hand-001',
      modality: 'X-RAY',
      bodyPart: 'HAND',
      view: 'PA',
      diagnosis: 'Fracture',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23555"/></svg>'
    },
    {
      id: 'skull-001',
      modality: 'X-RAY',
      bodyPart: 'SKULL',
      view: 'LAT',
      diagnosis: 'Normal',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23666"/></svg>'
    }
  ],

  async loadAll() {
    console.log(`📚 Loading ${this.samples.length} sample images...`);

    for (const sample of this.samples) {
      await QdrantMedical.indexImage(sample.url, sample);
      console.log(`  ✓ ${sample.id}: ${sample.diagnosis}`);
    }

    ChangeLog.record('dataset_loaded', { count: this.samples.length });
    return this.samples;
  },

  get(id) {
    return this.samples.find(s => s.id === id);
  },

  filter(criteria) {
    return this.samples.filter(s => {
      return (!criteria.bodyPart || s.bodyPart === criteria.bodyPart) &&
             (!criteria.modality || s.modality === criteria.modality) &&
             (!criteria.diagnosis || s.diagnosis === criteria.diagnosis);
    });
  },

  // Generate synthetic dataset for testing
  generateSynthetic(count = 100) {
    const bodyParts = ['CHEST', 'HAND', 'SKULL', 'SPINE', 'KNEE'];
    const diagnoses = ['Normal', 'Fracture', 'Pneumonia', 'Arthritis', 'Tumor'];

    const synthetic = [];
    for (let i = 0; i < count; i++) {
      synthetic.push({
        id: `synthetic-${i}`,
        modality: 'X-RAY',
        bodyPart: bodyParts[i % bodyParts.length],
        view: i % 2 === 0 ? 'PA' : 'LAT',
        diagnosis: diagnoses[i % diagnoses.length],
        url: `data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23${Math.floor(Math.random()*999)}"/></svg>`
      });
    }

    return synthetic;
  }
};

window.MedicalDataset = MedicalDataset;
```
