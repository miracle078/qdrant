# Stats API
**Analytics** | Usage Metrics

Statistics and analytics for API usage and collection metrics.

```javascript
const StatsAPI = {
  baseURL: '/api',

  async getCollectionStats(name) {
    const collections = await CollectionsAPI.list();
    const target = collections.collections.find(c => c.name === name);

    if (!target) {
      throw new Error(`Collection ${name} not found`);
    }

    return {
      name: target.name,
      vectors: target.count,
      size: `${(target.count * 512 * 4 / 1024 / 1024).toFixed(2)} MB`
    };
  },

  async getSystemStats() {
    const health = await HealthAPI.checkHealth();
    const collections = await CollectionsAPI.list();

    const totalVectors = collections.collections.reduce(
      (sum, col) => sum + col.count,
      0
    );

    return {
      status: health.status,
      collections: collections.total,
      totalVectors,
      healthy: health.healthy
    };
  }
};

window.StatsAPI = StatsAPI;
```
