# API Database Wrapper
**UUID:** f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c
**REST API** | Token Database Endpoints

REST API wrapper for token database operations.

```javascript
const APIDatabase = {
  baseUrl: '/api/db',

  endpoints: {
    // GET /api/db/modules?category=core&limit=10
    getModules: async (params = {}) => {
      const query = new URLSearchParams(params).toString();
      const response = await fetch(`${APIDatabase.baseUrl}/modules?${query}`);
      return await response.json();
    },

    // GET /api/db/modules/:id
    getModule: async (id) => {
      const response = await fetch(`${APIDatabase.baseUrl}/modules/${id}`);
      return await response.json();
    },

    // GET /api/db/modules/:id/dependencies
    getDependencies: async (id) => {
      const response = await fetch(`${APIDatabase.baseUrl}/modules/${id}/dependencies`);
      return await response.json();
    },

    // GET /api/db/stats
    getStats: async () => {
      const response = await fetch(`${APIDatabase.baseUrl}/stats`);
      return await response.json();
    },

    // GET /api/db/architecture?layer=0
    getArchitecture: async (layer) => {
      const query = layer !== undefined ? `?layer=${layer}` : '';
      const response = await fetch(`${APIDatabase.baseUrl}/architecture${query}`);
      return await response.json();
    },

    // POST /api/db/analyze
    analyzeModule: async (path) => {
      const response = await fetch(`${APIDatabase.baseUrl}/analyze`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ path })
      });
      return await response.json();
    },

    // POST /api/db/batch-analyze
    batchAnalyze: async (paths) => {
      const response = await fetch(`${APIDatabase.baseUrl}/batch-analyze`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ paths })
      });
      return await response.json();
    }
  },

  // Helper methods
  async queryModules(category, limit = 10) {
    return await this.endpoints.getModules({ category, limit });
  },

  async searchModules(query) {
    return await this.endpoints.getModules({ search: query });
  },

  async getModuleStats() {
    return await this.endpoints.getStats();
  }
};

window.APIDatabase = APIDatabase;
```
