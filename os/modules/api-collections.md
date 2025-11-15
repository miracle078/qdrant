# Collections API
**Qdrant Management** | Collection CRUD

Manage Qdrant collections with creation and listing operations.

```javascript
const CollectionsAPI = {
  baseURL: '/api',

  async list() {
    const response = await fetch(`${this.baseURL}/collections`);

    if (!response.ok) {
      throw new Error(`List failed: ${response.statusText}`);
    }

    const data = await response.json();

    return {
      collections: data.collections.map(col => ({
        name: col.name,
        count: col.vectors_count
      })),
      total: data.collections.length
    };
  },

  async create(name, dimension = 512) {
    const response = await fetch(`${this.baseURL}/collections/${name}/create`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ dimension })
    });

    if (!response.ok) {
      throw new Error(`Creation failed: ${response.statusText}`);
    }

    return await response.json();
  }
};

window.CollectionsAPI = CollectionsAPI;
```
