# Medical Imaging Demo
**Qdrant Vector Search** | X-Ray Analysis | ISA-95 L3

Demonstrate medical image similarity search with Qdrant vector database.

```javascript
console.log('🏥 Medical Imaging Demo with Qdrant\n');

// 1. Initialize Qdrant Medical
console.log('1️⃣ Initializing Qdrant...');
await QdrantMedical.init();
console.log(`   Collection: ${QdrantMedical.collection}`);
console.log(`   Dimensions: ${QdrantMedical.db.metadata.dimension}`);

// 2. Load sample dataset
console.log('\n2️⃣ Loading sample x-rays...');
const samples = await MedicalDataset.loadAll();
console.log(`   Loaded: ${samples.length} images`);

// 3. Analyze a sample x-ray
console.log('\n3️⃣ Analyzing chest x-ray...');
const sample = MedicalDataset.get('chest-002'); // Pneumonia case
const analysis = await XRayAnalyzer.analyze(sample.url);

console.log(`   Image ID: ${analysis.id.slice(0, 8)}...`);
console.log(`   Body Part: ${analysis.metadata.bodyPart}`);
console.log(`   Modality: ${analysis.metadata.modality}`);

// 4. Find similar cases
console.log('\n4️⃣ Similar cases:');
analysis.similar.forEach((s, i) => {
  console.log(`   ${i + 1}. Score: ${s.score} | ${s.diagnosis} (${s.bodyPart})`);
});

// 5. Generate embeddings
console.log('\n5️⃣ Generating embeddings...');
const embedding = await MedicalEmbeddings.embed(sample.url);
console.log(`   Vector dimension: ${embedding.length}`);
console.log(`   First 5 values: [${embedding.slice(0, 5).map(v => v.toFixed(3)).join(', ')}...]`);

// 6. Search by body part
console.log('\n6️⃣ Filtering dataset:');
const chestScans = MedicalDataset.filter({ bodyPart: 'CHEST' });
console.log(`   CHEST scans: ${chestScans.length}`);

const handScans = MedicalDataset.filter({ bodyPart: 'HAND' });
console.log(`   HAND scans: ${handScans.length}`);

// 7. Generate report
console.log('\n7️⃣ Analysis Report:');
const report = XRayAnalyzer.generateReport(analysis);
console.log(report);

// 8. Show Qdrant stats
console.log('\n8️⃣ Qdrant Statistics:');
console.log(`   Total indexed: ${QdrantMedical.db.images.length}`);
console.log(`   Distance metric: ${QdrantMedical.db.metadata.distance}`);

console.log('\n✅ Medical imaging demo complete!');

return {
  success: true,
  analyzed: 1,
  similar: analysis.similar.length,
  indexed: QdrantMedical.db.images.length
};
```
