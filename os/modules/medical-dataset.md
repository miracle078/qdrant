# Medical Dataset
**Sample X-Rays** | Training Data

Sample medical imaging dataset for testing.

```javascript
const MedicalDataset = {
  samples: [
    { id: 'chest-001', modality: 'X-RAY', bodyPart: 'CHEST', view: 'PA', diagnosis: 'Normal',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23222"/></svg>' },
    { id: 'chest-002', modality: 'X-RAY', bodyPart: 'CHEST', view: 'PA', diagnosis: 'Pneumonia',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23333"/></svg>' },
    { id: 'chest-003', modality: 'X-RAY', bodyPart: 'CHEST', view: 'LAT', diagnosis: 'Normal',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23444"/></svg>' },
    { id: 'hand-001', modality: 'X-RAY', bodyPart: 'HAND', view: 'PA', diagnosis: 'Fracture',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23555"/></svg>' },
    { id: 'skull-001', modality: 'X-RAY', bodyPart: 'SKULL', view: 'LAT', diagnosis: 'Normal',
      url: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23666"/></svg>' }
  ],

  async loadAll() {
    console.log(`📚 Loading ${this.samples.length} samples...`);
    for (const sample of this.samples) {
      await QdrantMedical.indexImage(sample.url, sample);
      console.log(`  ✓ ${sample.id}: ${sample.diagnosis}`);
    }
    ChangeLog.record('dataset_loaded', { count: this.samples.length });
    return this.samples;
  },

  get(id) { return this.samples.find(s => s.id === id); },

  filter(criteria) {
    return this.samples.filter(s =>
      (!criteria.bodyPart || s.bodyPart === criteria.bodyPart) &&
      (!criteria.modality || s.modality === criteria.modality) &&
      (!criteria.diagnosis || s.diagnosis === criteria.diagnosis)
    );
  },

  generateSynthetic(count = 100) {
    const parts = ['CHEST', 'HAND', 'SKULL', 'SPINE', 'KNEE'];
    const dx = ['Normal', 'Fracture', 'Pneumonia', 'Arthritis'];
    return Array(count).fill(0).map((_, i) => ({
      id: `syn-${i}`,
      modality: 'X-RAY',
      bodyPart: parts[i % parts.length],
      view: i % 2 ? 'LAT' : 'PA',
      diagnosis: dx[i % dx.length],
      url: `data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512"><rect fill="%23${i*111}"/></svg>`
    }));
  }
};

window.MedicalDataset = MedicalDataset;
```
