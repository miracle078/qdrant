# X-Ray Analyzer
**Image Analysis** | Similarity Search

Analyze x-rays and find similar cases using vector embeddings.

```javascript
const XRayAnalyzer = {
  async analyze(imageFile) {
    console.log('🔬 Analyzing x-ray...');

    // 1. Extract image data
    const imageData = await this.readImage(imageFile);

    // 2. Detect body part and modality
    const metadata = this.detectMetadata(imageData);

    // 3. Index in Qdrant
    const id = await QdrantMedical.indexImage(imageData, metadata);

    // 4. Find similar cases
    const similar = await QdrantMedical.search(imageData, 5);

    const result = {
      id,
      metadata,
      similar: similar.map(s => ({
        id: s.id,
        score: s.score.toFixed(3),
        diagnosis: s.payload.diagnosis,
        bodyPart: s.payload.bodyPart
      }))
    };

    ChangeLog.record('xray_analyzed', result);
    return result;
  },

  async readImage(file) {
    // Read image file (File API)
    return new Promise((resolve) => {
      const reader = new FileReader();
      reader.onload = (e) => resolve(e.target.result);
      reader.readAsDataURL(file);
    });
  },

  detectMetadata(imageData) {
    // Mock detection (real: ML model or DICOM tags)
    return {
      modality: 'X-RAY',
      bodyPart: 'CHEST',
      view: 'PA', // Posterior-Anterior
      width: 512,
      height: 512,
      bitDepth: 16
    };
  },

  async batchAnalyze(files) {
    const results = [];
    for (const file of files) {
      const result = await this.analyze(file);
      results.push(result);
    }
    console.log(`✅ Analyzed ${results.length} x-rays`);
    return results;
  },

  generateReport(analysisResult) {
    return `
# X-Ray Analysis Report

**Image ID:** ${analysisResult.id}
**Body Part:** ${analysisResult.metadata.bodyPart}
**Modality:** ${analysisResult.metadata.modality}

## Similar Cases Found: ${analysisResult.similar.length}

${analysisResult.similar.map((s, i) => `
${i + 1}. **Score:** ${s.score} | **Diagnosis:** ${s.diagnosis || 'N/A'}
`).join('\n')}
    `.trim();
  }
};

window.XRayAnalyzer = XRayAnalyzer;
```
