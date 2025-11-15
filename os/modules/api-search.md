# Search API
**Vector Search** | Semantic Retrieval

Vector search endpoint with Qdrant similarity search and ranking.

```javascript
const SearchAPI = {
  baseURL: '/api',

  async search(query, collection = 'medical_images', limit = 5) {
    const response = await fetch(`${this.baseURL}/search`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, collection, limit })
    });

    if (!response.ok) {
      throw new Error(`Search failed: ${response.statusText}`);
    }

    const data = await response.json();

    return {
      results: data.results.map(hit => ({
        id: hit.id,
        score: hit.score,
        payload: hit.payload
      })),
      count: data.count,
      collection
    };
  },

  async findSimilar(text, options = {}) {
    const { collection = 'isa', limit = 3 } = options;
    return await this.search(text, collection, limit);
  }
};

window.SearchAPI = SearchAPI;
```
