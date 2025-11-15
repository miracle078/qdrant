# Module Registry
**UUID:** c16e00c3-0ad6-481c-9d2d-586d643994a3
**Dynamic Registry** | Module Tracking & Dependencies

Runtime registry for all modules with UUID lookup and dependency resolution.

```javascript
const ModuleRegistry = {
  modules: new Map(),
  dependencies: new Map(),
  uuidIndex: new Map(),

  async init() {
    // Load REGISTRY.md
    const response = await fetch('/REGISTRY.md');
    const markdown = await response.text();

    // Parse module table
    this.parseRegistry(markdown);

    // Initialize database if available
    if (window.DatabaseManager?.db) {
      await this.syncWithDatabase();
    }

    return this;
  },

  parseRegistry(markdown) {
    // Extract UUID table rows
    const uuidPattern = /`([a-f0-9-]{36})`\s*\|\s*(\w+)\s*\|\s*([\w/.-]+)\s*\|/g;
    let match;

    while ((match = uuidPattern.exec(markdown)) !== null) {
      const [, uuid, name, path] = match;

      this.register({
        uuid,
        name,
        path,
        loaded: false
      });
    }
  },

  register(moduleInfo) {
    const { uuid, name, path } = moduleInfo;

    this.modules.set(name, moduleInfo);
    this.uuidIndex.set(uuid, name);

    // Save to database
    if (window.DatabaseManager?.db) {
      DatabaseManager.registerFile(uuid, path, 'module', name);
    }
  },

  getByUUID(uuid) {
    const name = this.uuidIndex.get(uuid);
    return name ? this.modules.get(name) : null;
  },

  getByName(name) {
    return this.modules.get(name);
  },

  getDependencies(moduleName) {
    return this.dependencies.get(moduleName) || [];
  },

  setDependencies(moduleName, deps) {
    this.dependencies.set(moduleName, deps);

    // Save to database
    if (window.DatabaseManager?.db) {
      const module = this.modules.get(moduleName);
      if (module) {
        deps.forEach(dep => {
          const depModule = this.modules.get(dep);
          if (depModule) {
            DatabaseManager.run(
              'INSERT OR IGNORE INTO dependencies (from_uuid, to_uuid, dep_type) VALUES (?, ?, ?)',
              [module.uuid, depModule.uuid, 'requires']
            );
          }
        });
      }
    }
  },

  async loadWithDependencies(moduleName) {
    const deps = this.getDependencies(moduleName);

    // Load dependencies first
    for (const dep of deps) {
      await ModuleLoader.load(dep);
    }

    // Load main module
    return await ModuleLoader.load(moduleName);
  },

  async syncWithDatabase() {
    // Query all files from database
    const result = DatabaseManager.query('SELECT uuid, path, module_name FROM files');

    if (result[0]?.values) {
      result[0].values.forEach(([uuid, path, moduleName]) => {
        if (!this.uuidIndex.has(uuid)) {
          this.register({ uuid, name: moduleName, path });
        }
      });
    }
  },

  listAll() {
    return Array.from(this.modules.values());
  },

  stats() {
    return {
      total: this.modules.size,
      withUUIDs: this.uuidIndex.size,
      withDependencies: this.dependencies.size
    };
  }
};

window.ModuleRegistry = ModuleRegistry;
```
