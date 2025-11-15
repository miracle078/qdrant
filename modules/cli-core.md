# CLI Core Commands
**UUID:** 4f9a6e2c-8d3b-4e1f-9a7c-5d8f6e3b2a9c
**Basic Commands** | ls, cat, help, clear, run

Core command set for Chazon CLI.

```javascript
const CLICore = {
  commands: {},

  register(cli) {
    this.commands = {
      help: () => this.showHelp(cli),
      ls: () => this.listFiles(cli),
      cat: (filename) => this.showFile(cli, filename),
      run: (filename) => this.runFile(cli, filename),
      clear: () => this.clearTerminal(cli),
      pwd: () => this.printWorkingDir(cli),
      whoami: () => this.whoAmI(cli),
      version: () => this.showVersion(cli)
    };

    Object.assign(cli.commands, this.commands);
    return this;
  },

  showHelp(cli) {
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('  CHAZON CLI - CORE COMMANDS', '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');
    cli.print('File Operations:', '#00ff88');
    cli.print('  ls              - List all files', '#888');
    cli.print('  cat <file>      - Display file contents', '#888');
    cli.print('  run <file>      - Execute a program', '#888');
    cli.print('  pwd             - Print working directory', '#888');
    cli.print('');
    cli.print('System:', '#00ff88');
    cli.print('  help            - Show this help', '#888');
    cli.print('  clear           - Clear terminal', '#888');
    cli.print('  whoami          - Show current user', '#888');
    cli.print('  version         - Show Chazon version', '#888');
    cli.print('');
    cli.print('More commands: test, edit, logs, git', '#00ccff');
  },

  listFiles(cli) {
    if (!cli.files || Object.keys(cli.files).length === 0) {
      cli.print('No files loaded', '#ff0000');
      return;
    }

    cli.print('Files:', '#00ff88');
    Object.keys(cli.files).forEach(name => {
      const size = cli.files[name].length;
      cli.print(`  ${name.padEnd(30)} ${size} bytes`, '#888');
    });
  },

  showFile(cli, filename) {
    if (!filename) {
      cli.print('Usage: cat <filename>', '#ff0000');
      return;
    }

    const content = cli.files[filename];
    if (!content) {
      cli.print(`File not found: ${filename}`, '#ff0000');
      return;
    }

    cli.print(`─── ${filename} ───`, '#00ccff');
    cli.print(content, '#ccc');
  },

  runFile(cli, filename) {
    if (!filename) {
      cli.print('Usage: run <filename>', '#ff0000');
      return;
    }

    const content = cli.files[filename];
    if (!content) {
      cli.print(`File not found: ${filename}`, '#ff0000');
      return;
    }

    cli.print(`Running: ${filename}`, '#00ccff');
    try {
      if (window.MDCompiler) {
        const results = MDCompiler.compile(content);
        results.forEach(result => {
          if (result.success) {
            cli.print('✓ Executed successfully', '#00ff88');
          } else {
            cli.print(`✗ Error: ${result.error}`, '#ff0000');
          }
        });
      }
    } catch (err) {
      cli.print(`Error: ${err.message}`, '#ff0000');
    }
  },

  clearTerminal(cli) {
    if (cli.output) {
      cli.output.innerHTML = '';
    }
  },

  printWorkingDir(cli) {
    cli.print('/chazon/programs', '#00ccff');
  },

  whoAmI(cli) {
    cli.print('chazon-user (φ-Balanced)', '#00ccff');
  },

  showVersion(cli) {
    cli.print('Chazon OS v1.0.0 - חזון', '#00ccff');
    cli.print('φ = 1.618 | ISA-95 L0-L4', '#888');
  }
};

window.CLICore = CLICore;
```

## Usage

```javascript
CLICore.register(ChazonCLI);
```
