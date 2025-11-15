# Module Wrapper
**CLI/API/MCP Integration** | Unified Interface

Wraps any module with CLI, API, and MCP interfaces automatically.

```javascript
const ModuleWrapper = {
  wrap(name, module, methods) {
    const wrapped = {
      name,
      module,
      state: PackML.create(`module:${name}`),
      uuid: ChangeLog.uuid(),
      created: Date.now()
    };

    // Auto-register with MCP
    methods.forEach(method => {
      MCP.register(`${name}.${method}`, (params) => module[method](params));
    });

    // Auto-register with API
    methods.forEach(method => {
      ChazonAPI.route('POST', `/${name}/${method}`, (body) => module[method](body));
    });

    // Add CLI commands
    methods.forEach(method => {
      const cmdName = `${name}:${method}`;
      if (window.ChazonCLI) {
        ChazonCLI.commands = ChazonCLI.commands || {};
        ChazonCLI.commands[cmdName] = (args) => module[method](args);
      }
    });

    ChangeLog.record('module_wrapped', { name, methods, uuid: wrapped.uuid });

    return wrapped;
  },

  wrapAll() {
    const wrappers = [];

    // Wrap core modules
    if (window.MDCompiler) {
      wrappers.push(this.wrap('compiler', MDCompiler, ['compile', 'parse', 'execute']));
    }

    if (window.ChazonCLI) {
      wrappers.push(this.wrap('cli', ChazonCLI, ['exec', 'runProgram', 'addFile']));
    }

    if (window.TestAgent) {
      wrappers.push(this.wrap('test', TestAgent, ['run', 'runTest']));
    }

    if (window.DeployAgent) {
      wrappers.push(this.wrap('deploy', DeployAgent, ['deploy', 'validate', 'rollback']));
    }

    console.log(`🎁 Wrapped ${wrappers.length} modules`);
    return wrappers;
  }
};

window.ModuleWrapper = ModuleWrapper;
```
