# CLI Database Commands
**UUID:** e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b
**Database CLI** | Token Database Commands

CLI commands for token database operations.

```javascript
const CLIDatabase = {
  commands: {
    'db:init': {
      description: 'Initialize token database',
      async execute(args, cli) {
        cli.print('Initializing token database...', '#00ccff');
        await TokenDB.init();
        cli.print('✓ Database initialized', '#00ff88');
      }
    },

    'db:analyze': {
      description: 'Analyze all modules and populate database',
      async execute(args, cli) {
        cli.print('Analyzing modules...', '#00ccff');

        const paths = [
          // Core
          '../modules/chazon-mdcompiler.md',
          '../modules/chazon-os.md',
          '../modules/chazon-attractors.md',
          '../modules/chazon-equilibrium.md',
          '../modules/chazon-packml.md',
          '../modules/chazon-changelog.md',
          '../modules/chazon-sqlite.md',
          // CLI
          '../modules/cli-core.md',
          '../modules/cli-edit.md',
          '../modules/cli-test.md',
          '../modules/cli-logs.md',
          '../modules/cli-git.md',
          '../modules/cli-db.md',
          // Add more as needed
        ];

        let count = 0;
        for (const path of paths) {
          try {
            const analysis = await TokenAnalyzer.analyzeModule(path);
            await TokenDB.insertModule(analysis);
            cli.print(`  ✓ ${analysis.name} (${analysis.tokenCount} tokens)`, '#888');
            count++;
          } catch (err) {
            cli.print(`  ✗ ${path}: ${err.message}`, '#ff0044');
          }
        }

        cli.print(`\n✓ Analyzed ${count} modules`, '#00ff88');
      }
    },

    'db:stats': {
      description: 'Show token statistics',
      async execute(args, cli) {
        const stats = await TokenDB.getTokenStats();

        cli.print('\nToken Statistics by Category:', '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');
        cli.print('Category      Modules   Total    Avg', '#888');
        cli.print('─────────────────────────────────────────', '#888');

        stats.forEach(row => {
          const line = `${row.category.padEnd(12)} ${String(row.module_count).padStart(7)} ${String(row.total_tokens).padStart(7)} ${String(Math.round(row.avg_tokens)).padStart(6)}`;
          cli.print(line, '#00ff88');
        });

        cli.print('─────────────────────────────────────────\n', '#888');
      }
    },

    'db:query': {
      description: 'Query modules by category',
      usage: 'db:query <category>',
      async execute(args, cli) {
        if (!args[0]) {
          cli.print('Usage: db:query <category>', '#ff0044');
          cli.print('Categories: core, cli, ui, medical, language, boot', '#888');
          return;
        }

        const modules = await TokenDB.getModulesByCategory(args[0]);

        cli.print(`\nModules in category: ${args[0]}`, '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');

        modules.forEach(mod => {
          cli.print(`${mod.name} (${mod.token_count} tokens)`, '#00ff88');
          cli.print(`  Path: ${mod.path}`, '#888');
          cli.print(`  UUID: ${mod.uuid}`, '#888');
        });

        cli.print(`\nTotal: ${modules.length} modules\n`, '#00ccff');
      }
    },

    'db:deps': {
      description: 'Show module dependencies',
      usage: 'db:deps <module_id>',
      async execute(args, cli) {
        if (!args[0]) {
          cli.print('Usage: db:deps <module_id>', '#ff0044');
          return;
        }

        const deps = await TokenDB.getDependencies(parseInt(args[0]));

        cli.print(`\nDependencies for module ${args[0]}:`, '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');

        deps.forEach(dep => {
          cli.print(`${dep.name} (${dep.dependency_type})`, '#00ff88');
        });

        cli.print(`\nTotal: ${deps.length} dependencies\n`, '#00ccff');
      }
    },

    'db:export': {
      description: 'Export database to file',
      async execute(args, cli) {
        cli.print('Exporting database...', '#00ccff');
        const data = TokenDB.export();

        if (data) {
          const blob = new Blob([data], { type: 'application/octet-stream' });
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'tokens.db';
          a.click();
          cli.print('✓ Database exported', '#00ff88');
        } else {
          cli.print('✗ Export not available', '#ff0044');
        }
      }
    },

    'db:arch': {
      description: 'Show architecture graph',
      async execute(args, cli) {
        const graph = await TokenDB.getArchitectureGraph();

        cli.print('\nArchitecture Graph:', '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');

        const layers = {};
        graph.forEach(node => {
          if (!layers[node.layer]) {
            layers[node.layer] = [];
          }
          layers[node.layer].push(node);
        });

        Object.keys(layers).sort().forEach(layer => {
          cli.print(`\nLayer ${layer}:`, '#00ccff');
          layers[layer].forEach(node => {
            cli.print(`  ${node.node_type}: ${node.node_id}`, '#00ff88');
          });
        });

        cli.print('', '#888');
      }
    }
  },

  register(cli) {
    Object.entries(this.commands).forEach(([name, cmd]) => {
      cli.registerCommand(name, cmd);
    });
  }
};

// Auto-register if ChazonCLI exists
if (window.ChazonCLI) {
  CLIDatabase.register(ChazonCLI);
}

window.CLIDatabase = CLIDatabase;
```
