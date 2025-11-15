# Health API
**System Health** | Status Checks

Health check endpoints for Chazon OS API with Qdrant connectivity monitoring.

```javascript
const HealthAPI = {
  baseURL: '/api',

  async getRoot() {
    const response = await fetch(`${this.baseURL}/`);
    return await response.json();
  },

  async checkHealth() {
    try {
      const response = await fetch(`${this.baseURL}/health`);
      const data = await response.json();

      return {
        status: data.status,
        qdrant: data.qdrant,
        collections: data.collections,
        healthy: data.status === 'healthy'
      };
    } catch (error) {
      return {
        status: 'unhealthy',
        error: error.message,
        healthy: false
      };
    }
  },

  async getInfo() {
    const root = await this.getRoot();
    return {
      name: root.name,
      version: root.version,
      providers: {
        qdrant: root.qdrant === 'connected',
        cohere: root.cohere,
        openai: root.openai
      }
    };
  }
};

window.HealthAPI = HealthAPI;
```
