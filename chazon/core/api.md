# API Layer
**RESTful Interface** | Module Access

HTTP-style API for programmatic access to all modules.

```javascript
const ChazonAPI = {
  version: '1.0.0',
  routes: {},

  route(method, path, handler) {
    const key = `${method} ${path}`;
    this.routes[key] = handler;
    console.log(`🛣️ API: ${key}`);
  },

  async request(method, path, body = null) {
    const key = `${method} ${path}`;
    const handler = this.routes[key];

    if (!handler) {
      return { status: 404, error: 'Route not found' };
    }

    const stateId = `api:${path.replace(/\//g, ':')}`;
    PackML.create(stateId);
    PackML.start(stateId);

    try {
      const result = await handler(body);
      PackML.transition(stateId, PackML.states.COMPLETE);

      ChangeLog.record('api_request', { method, path, status: 200 });

      return { status: 200, data: result };
    } catch (err) {
      PackML.abort(stateId);
      ChangeLog.record('api_error', { method, path, error: err.message });
      return { status: 500, error: err.message };
    }
  },

  // Convenience methods
  get(path) { return this.request('GET', path); },
  post(path, body) { return this.request('POST', path, body); },
  put(path, body) { return this.request('PUT', path, body); },
  delete(path) { return this.request('DELETE', path); }
};

window.ChazonAPI = ChazonAPI;

// Register default routes
ChazonAPI.route('GET', '/status', () => ({
  version: ChazonAPI.version,
  uptime: performance.now(),
  modules: Object.keys(ChazonOS?.modules || {})
}));

ChazonAPI.route('POST', '/compile', (body) => MDCompiler.compile(body.markdown));
ChazonAPI.route('POST', '/exec', (body) => ChazonCLI.exec(body.command));
ChazonAPI.route('GET', '/changelog', () => ChangeLog.get(20));
ChazonAPI.route('GET', '/states', () => PackML.machines);
```
