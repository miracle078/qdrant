# Qdrant Client
**Real Vector DB Connection** | Backend Integration

Client for connecting Chazon OS to real Qdrant backend API.

```javascript
const QdrantClient = {
  baseURL: 'http://localhost:8000', // Change to deployed URL

  async createCollection(name, dimension = 512) {
    const response = await fetch(`${this.baseURL}/collections/${name}/create?dimension=${dimension}`, {
      method: 'POST'
    });
    return response.json();
  },

  async embed(text, model = 'cohere') {
    const response = await fetch(`${this.baseURL}/embed`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, model })
    });
    return response.json();
  },

  async search(query, collection = 'medical_images', limit = 5) {
    const response = await fetch(`${this.baseURL}/search`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, collection, limit })
    });
    return response.json();
  },

  async index(text, collection, metadata) {
    const response = await fetch(`${this.baseURL}/index`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, collection, metadata })
    });
    return response.json();
  },

  async listCollections() {
    const response = await fetch(`${this.baseURL}/collections`);
    return response.json();
  },

  async health() {
    const response = await fetch(`${this.baseURL}/health`);
    return response.json();
  },

  // Configure for production
  configure(url) {
    this.baseURL = url;
    console.log(`🔌 Qdrant client configured: ${url}`);
  }
};

window.QdrantClient = QdrantClient;
```
