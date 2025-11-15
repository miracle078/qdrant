# MCP Wrapper
**Model Context Protocol** | Module Communication

MCP-compatible wrapper for inter-module communication.

```javascript
const MCP = {
  version: '1.0.0',
  endpoints: {},

  register(name, handler) {
    this.endpoints[name] = {
      name,
      handler,
      state: PackML.create(`mcp:${name}`),
      calls: 0
    };
    console.log(`🔌 MCP: Registered ${name}`);
  },

  async call(endpoint, params) {
    const ep = this.endpoints[endpoint];
    if (!ep) return { error: 'Endpoint not found' };

    // State transition: IDLE → STARTING → EXECUTE
    PackML.start(ep.state.id);
    ep.calls++;

    try {
      const result = await ep.handler(params);

      // Complete
      PackML.transition(ep.state.id, PackML.states.COMPLETING);
      PackML.transition(ep.state.id, PackML.states.COMPLETE);
      PackML.transition(ep.state.id, PackML.states.IDLE);

      ChangeLog.record('mcp_call', { endpoint, params, result, calls: ep.calls });

      return { success: true, result };
    } catch (err) {
      PackML.abort(ep.state.id);
      ChangeLog.record('mcp_error', { endpoint, error: err.message });
      return { success: false, error: err.message };
    }
  },

  list() {
    return Object.keys(this.endpoints).map(name => ({
      name,
      calls: this.endpoints[name].calls,
      state: PackML.getState(this.endpoints[name].state.id)
    }));
  }
};

window.MCP = MCP;

// Auto-register core modules
if (window.ChazonOS) {
  MCP.register('os.boot', () => ChazonOS.boot());
  MCP.register('compiler.compile', (md) => MDCompiler.compile(md));
  MCP.register('cli.exec', (cmd) => ChazonCLI.exec(cmd));
}
```
