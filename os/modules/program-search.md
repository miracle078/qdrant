# Qdrant Search
**Vector Search Demo** | ISA-95 L2

Demonstrate Qdrant vector search integration.

```javascript
const QdrantSearch = {
  collections: ['isa', 'code', 'img', 'aud', 'vid', 'doc'],

  search(query, collection = 'isa') {
    console.log(`🔍 Searching "${query}" in ${collection}...`);

    // Mock search results
    const results = [
      { id: 1, score: 0.95, text: 'ISA-95 Level 3: MES Layer' },
      { id: 2, score: 0.87, text: '21 CFR Part 11: Audit Trail' },
      { id: 3, score: 0.82, text: 'EU Annex 11: Validation' }
    ];

    console.log(`Found ${results.length} results`);
    results.forEach(r => console.log(`  [${r.score}] ${r.text}`));

    return results;
  },

  hybrid(query) {
    console.log('🔀 Hybrid search across all collections...');
    return this.collections.map(c => ({
      collection: c,
      results: this.search(query, c).slice(0, 1)
    }));
  }
};

QdrantSearch.search('ISA-95 audit trail');
return QdrantSearch;
```
