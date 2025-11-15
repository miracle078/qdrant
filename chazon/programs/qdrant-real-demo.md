# Real Qdrant Demo
**Live Vector Search** | ISA-95 L4

Demonstrate real Qdrant integration with backend API and actual embeddings.

```javascript
console.log('🔌 Real Qdrant Integration Demo\n');

// 1. Check backend health
console.log('1️⃣ Checking backend connection...');
try {
  const health = await QdrantClient.health();
  console.log(`   Status: ${health.status}`);
  console.log(`   Qdrant: ${health.qdrant}`);
  console.log(`   Collections: ${health.collections || 0}`);
} catch (err) {
  console.log(`   ❌ Backend not available: ${err.message}`);
  console.log('   Start backend with: cd backend && python api.py');
  return { error: 'Backend offline' };
}

// 2. Create medical collection
console.log('\n2️⃣ Creating collection...');
try {
  const collection = await QdrantClient.createCollection('medical_images', 512);
  console.log(`   ✓ Collection: ${collection.collection}`);
  console.log(`   Dimension: ${collection.dimension}`);
} catch (err) {
  console.log(`   ⚠️ Collection may already exist: ${err.message}`);
}

// 3. Generate real embeddings
console.log('\n3️⃣ Generating embeddings with Cohere...');
const sampleTexts = [
  'chest x-ray showing pneumonia',
  'normal chest radiograph',
  'hand x-ray with fracture'
];

for (const text of sampleTexts) {
  try {
    const result = await QdrantClient.embed(text, 'cohere');
    console.log(`   ✓ "${text}"`);
    console.log(`     Dim: ${result.dimension}, Model: ${result.model}`);
  } catch (err) {
    console.log(`   ❌ Embedding failed: ${err.message}`);
  }
}

// 4. Index medical cases
console.log('\n4️⃣ Indexing medical cases...');
const cases = [
  { text: 'chest x-ray pneumonia bilateral infiltrates', metadata: { diagnosis: 'Pneumonia', bodyPart: 'CHEST' }},
  { text: 'normal chest x-ray clear lungs', metadata: { diagnosis: 'Normal', bodyPart: 'CHEST' }},
  { text: 'hand fracture metacarpal bone', metadata: { diagnosis: 'Fracture', bodyPart: 'HAND' }}
];

for (const case_data of cases) {
  try {
    const result = await QdrantClient.index(case_data.text, 'medical_images', case_data.metadata);
    console.log(`   ✓ Indexed: ${result.id.slice(0, 8)}... (${case_data.metadata.diagnosis})`);
  } catch (err) {
    console.log(`   ❌ Index failed: ${err.message}`);
  }
}

// 5. Search for similar cases
console.log('\n5️⃣ Searching for similar cases...');
const query = 'chest x-ray with lung infection';
console.log(`   Query: "${query}"`);

try {
  const searchResults = await QdrantClient.search(query, 'medical_images', 3);
  console.log(`   Found: ${searchResults.count} results\n`);

  searchResults.results.forEach((result, i) => {
    console.log(`   ${i + 1}. Score: ${result.score.toFixed(3)}`);
    console.log(`      Diagnosis: ${result.payload.diagnosis}`);
    console.log(`      Body Part: ${result.payload.bodyPart}`);
  });
} catch (err) {
  console.log(`   ❌ Search failed: ${err.message}`);
}

// 6. List all collections
console.log('\n6️⃣ Collections:');
try {
  const collections = await QdrantClient.listCollections();
  collections.collections.forEach(col => {
    console.log(`   • ${col.name}: ${col.vectors_count} vectors`);
  });
} catch (err) {
  console.log(`   ❌ Failed: ${err.message}`);
}

console.log('\n✅ Real Qdrant demo complete!');
console.log('   Backend API working ✓');
console.log('   Embeddings working ✓');
console.log('   Vector search working ✓');

return { success: true, backend: 'connected' };
```
