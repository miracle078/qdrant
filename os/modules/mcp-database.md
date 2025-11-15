# MCP Database Wrapper
**UUID:** d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a
**MCP Tools** | Database Operations via MCP

MCP server tools for token database operations.

```javascript
const MCPDatabase = {
  tools: [
    {
      name: 'query_modules',
      description: 'Query modules from token database',
      inputSchema: {
        type: 'object',
        properties: {
          category: {
            type: 'string',
            description: 'Module category (core, cli, ui, medical, language, boot)'
          },
          limit: {
            type: 'integer',
            description: 'Maximum number of results',
            default: 10
          }
        }
      }
    },
    {
      name: 'get_dependencies',
      description: 'Get module dependencies',
      inputSchema: {
        type: 'object',
        properties: {
          module_name: {
            type: 'string',
            description: 'Module name'
          }
        },
        required: ['module_name']
      }
    },
    {
      name: 'get_architecture',
      description: 'Get system architecture graph',
      inputSchema: {
        type: 'object',
        properties: {
          layer: {
            type: 'integer',
            description: 'Architecture layer (0-4)',
            minimum: 0,
            maximum: 4
          }
        }
      }
    },
    {
      name: 'get_token_stats',
      description: 'Get token statistics by category',
      inputSchema: {
        type: 'object',
        properties: {}
      }
    },
    {
      name: 'analyze_module',
      description: 'Analyze a module and store in database',
      inputSchema: {
        type: 'object',
        properties: {
          path: {
            type: 'string',
            description: 'Module path relative to project root'
          }
        },
        required: ['path']
      }
    }
  ],

  async handleToolCall(name, args) {
    if (!window.TokenDB) {
      throw new Error('TokenDB not initialized');
    }

    switch (name) {
      case 'query_modules':
        if (args.category) {
          return await TokenDB.getModulesByCategory(args.category);
        }
        return await TokenDB.query('SELECT * FROM modules LIMIT ?', [args.limit || 10]);

      case 'get_dependencies':
        const module = await TokenDB.query(
          'SELECT id FROM modules WHERE name = ?',
          [args.module_name]
        );
        if (module.length === 0) {
          throw new Error(`Module not found: ${args.module_name}`);
        }
        return await TokenDB.getDependencies(module[0].id);

      case 'get_architecture':
        if (args.layer !== undefined) {
          return await TokenDB.query(
            'SELECT * FROM architecture_graph WHERE layer = ?',
            [args.layer]
          );
        }
        return await TokenDB.getArchitectureGraph();

      case 'get_token_stats':
        return await TokenDB.getTokenStats();

      case 'analyze_module':
        const analysis = await TokenAnalyzer.analyzeModule(args.path);
        await TokenDB.insertModule(analysis);
        return analysis;

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  },

  async listTools() {
    return this.tools;
  },

  getToolSchema(name) {
    return this.tools.find(t => t.name === name);
  }
};

window.MCPDatabase = MCPDatabase;
```
