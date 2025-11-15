# Qdrant Client
**Vector Database** | Search & Index

Qdrant client for vector operations with timeout handling.

```javascript
const QdrantClient = {
  baseURL: window.QDRANT_URL || 'http://localhost:6333',
  timeout: 30000,

  async request(path, options = {}) {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), this.timeout);

    try {
      const response = await fetch(`${this.baseURL}${path}`, {
        ...options,
        signal: controller.signal,
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        }
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      return await response.json();
    } catch (err) {
      clearTimeout(timeoutId);
      if (err.name === 'AbortError') {
        throw new Error('Request timeout');
      }
      throw err;
    }
  },

  async search(collection, vector, limit = 5) {
    return this.request(`/collections/${collection}/points/search`, {
      method: 'POST',
      body: JSON.stringify({
        vector,
        limit,
        with_payload: true
      })
    });
  },

  async upsert(collection, points) {
    return this.request(`/collections/${collection}/points`, {
      method: 'PUT',
      body: JSON.stringify({ points })
    });
  },

  async createCollection(name, vectorSize, distance = 'Cosine') {
    return this.request(`/collections/${name}`, {
      method: 'PUT',
      body: JSON.stringify({
        vectors: { size: vectorSize, distance }
      })
    });
  }
};

window.QdrantClient = QdrantClient;
```
