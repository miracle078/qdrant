# Index API
**Document Indexing** | Qdrant Upsert

Index documents into Qdrant collections with automatic embedding generation.

```javascript
const IndexAPI = {
  baseURL: '/api',

  async index(text, collection, metadata = {}) {
    const response = await fetch(`${this.baseURL}/index`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, collection, metadata })
    });

    if (!response.ok) {
      throw new Error(`Indexing failed: ${response.statusText}`);
    }

    const data = await response.json();

    return {
      id: data.id,
      indexed: data.indexed,
      collection: data.collection
    };
  },

  async indexBatch(documents, collection) {
    const results = [];

    for (const doc of documents) {
      const result = await this.index(doc.text, collection, doc.metadata);
      results.push(result);
    }

    return { indexed: results.length, ids: results.map(r => r.id) };
  }
};

window.IndexAPI = IndexAPI;
```
