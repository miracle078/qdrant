# Module Router - UUID-Based Discovery
**UUID:** a1b2c3d4-e5f6-7890-abcd-ef1234567890
**Type:** Core System | Module Discovery & Routing

UUID-based module routing system that allows modules to find each other by UUID instead of file path.

## Architecture

Modules declare their UUID in the header, and the router maintains an index:

```javascript
// UUID Registry
const MODULE_REGISTRY = new Map();

// Module structure
{
  uuid: '1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d',
  name: 'ChazonOS',
  path: '../modules/chazon-os.md',
  type: 'Core System',
  loaded: false,
  exports: {}
}
```

## UUID Format

Every module starts with:
```markdown
# Module Name
**UUID:** xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
**Type:** Category | Description
```

## Router API

```javascript
const ModuleRouter = {
  // Register module by UUID
  register(uuid, moduleInfo) {
    MODULE_REGISTRY.set(uuid, moduleInfo);
  },

  // Find module by UUID
  find(uuid) {
    return MODULE_REGISTRY.get(uuid);
  },

  // Load module by UUID (not path)
  async load(uuid) {
    const module = this.find(uuid);
    if (!module) {
      throw new Error(`Module not found: ${uuid}`);
    }

    if (module.loaded) {
      return module.exports;
    }

    // Fetch and compile
    const response = await fetch(module.path);
    const markdown = await response.text();
    const compiled = await MDCompiler.compile(markdown);

    module.loaded = true;
    module.exports = compiled;

    return compiled;
  },

  // Import by UUID (like ES6 import)
  async import(uuid) {
    return await this.load(uuid);
  },

  // List all modules of a type
  findByType(type) {
    return Array.from(MODULE_REGISTRY.values())
      .filter(m => m.type.includes(type));
  },

  // List all loaded modules
  getLoaded() {
    return Array.from(MODULE_REGISTRY.values())
      .filter(m => m.loaded);
  },

  // Full registry scan (builds index from file headers)
  async scan(directories) {
    for (const dir of directories) {
      const files = await this.scanDirectory(dir);
      for (const file of files) {
        if (file.endsWith('.md')) {
          await this.registerFromFile(file);
        }
      }
    }
  },

  async registerFromFile(path) {
    try {
      const response = await fetch(path);
      const text = await response.text();

      // Extract UUID from header
      const uuidMatch = text.match(/\*\*UUID:\*\*\s*([a-f0-9-]{36})/i);
      const nameMatch = text.match(/^#\s+(.+)$/m);
      const typeMatch = text.match(/\*\*UUID:\*\*[^\n]+\n\*\*([^:]+):\*\*\s*(.+)/);

      if (uuidMatch && nameMatch) {
        this.register(uuidMatch[1], {
          uuid: uuidMatch[1],
          name: nameMatch[1],
          path: path,
          type: typeMatch ? `${typeMatch[1]}: ${typeMatch[2]}` : 'Unknown',
          loaded: false,
          exports: null
        });
      }
    } catch (e) {
      console.warn(`Failed to register ${path}:`, e);
    }
  }
};

window.ModuleRouter = ModuleRouter;
```

## Usage

### Old Way (Path-Based)
```javascript
// Hard-coded path - breaks if file moves
const module = await MDCompiler.loadModule('../modules/chazon-os.md');
```

### New Way (UUID-Based)
```javascript
// UUID-based - works regardless of file location
const module = await ModuleRouter.import('1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d');
```

### Boot Sequence Example
```javascript
// Old
const BootPhase0 = {
  modules: [
    '../modules/chazon-mdcompiler.md',
    '../modules/chazon-os.md',
    '../modules/chazon-attractors.md'
  ]
};

// New (UUID-based)
const BootPhase0 = {
  modules: [
    '7f8e9d0c-1b2a-3948-5a6b-7c8d9e0f1a2b', // MDCompiler
    '1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d', // ChazonOS
    '2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e'  // Attractors
  ]
};

// Load by UUID
for (const uuid of BootPhase0.modules) {
  await ModuleRouter.import(uuid);
}
```

## Module Dependencies

Modules can declare dependencies by UUID:

```markdown
# My Module
**UUID:** aaaa-bbbb-cccc-dddd
**Depends:** 1111-2222-3333-4444, 5555-6666-7777-8888

Module code that imports by UUID:
const CoreOS = await ModuleRouter.import('1111-2222-3333-4444');
const Compiler = await ModuleRouter.import('5555-6666-7777-8888');
```

## Benefits

1. **Location independence** - Modules can move without breaking imports
2. **Versioning** - UUID stays same across versions
3. **Discovery** - Find modules by type, not path
4. **Lazy loading** - Load only what's needed
5. **Dependency resolution** - Auto-load dependencies

## Registry Persistence

```javascript
// Save registry to localStorage
ModuleRouter.save = function() {
  const data = Array.from(MODULE_REGISTRY.entries());
  localStorage.setItem('module_registry', JSON.stringify(data));
};

// Load registry from localStorage
ModuleRouter.restore = function() {
  const data = localStorage.getItem('module_registry');
  if (data) {
    const entries = JSON.parse(data);
    for (const [uuid, info] of entries) {
      MODULE_REGISTRY.set(uuid, info);
    }
  }
};
```

## Future: Distributed Registry

```javascript
// Query remote registries
const remoteModule = await ModuleRouter.import(
  'xyz-uuid',
  { registry: 'https://chazon.io/registry' }
);

// Publish to registry
await ModuleRouter.publish('my-uuid', {
  endpoint: 'https://myregistry.com'
});
```

## See Also

- `modules/chazon-mdcompiler.md` - Compiles MD modules
- `boot/boot-sequence.md` - Uses UUID-based loading
- `data/tokendb.sql` - Stores module metadata
- `os/module-index.md` - Full module index
