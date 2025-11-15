# Chazon CLI
**UUID:** 8f3e9a5c-2d7b-4e1f-9a6c-7d5f8e2b4a3c
**φ-Balanced Interface** | ISA-95 L2: Supervisory Control

Modular command-line interface with extensible command sets. φ = 1.618.

```javascript
const ChazonCLI = {
  φ: 1.618,
  files: {},
  cwd: '/',
  history: [],
  commands: {},
  output: null,
  commandModules: [],

  init(outputElement) {
    this.output = outputElement;
    this.loadCommands();
    return this;
  },

  loadCommands() {
    // Register command modules
    if (window.CLICore) {
      CLICore.register(this);
      this.commandModules.push('CLICore');
    }
    if (window.CLIEdit) {
      CLIEdit.register(this);
      this.commandModules.push('CLIEdit');
    }
    if (window.CLITest) {
      CLITest.register(this);
      this.commandModules.push('CLITest');
    }
    if (window.CLILogs) {
      CLILogs.register(this);
      this.commandModules.push('CLILogs');
    }
    if (window.CLIGit) {
      CLIGit.register(this);
      this.commandModules.push('CLIGit');
    }

    console.log(`✓ Loaded ${this.commandModules.length} CLI command modules`);
  },

  exec(input) {
    if (!input?.trim()) return;

    this.history.push(input);
    const parts = input.trim().split(/\s+/);
    const cmd = parts[0];
    const args = parts.slice(1);

    // Execute command
    if (this.commands[cmd]) {
      this.commands[cmd](...args);
    } else {
      this.print(`Command not found: ${cmd}`, '#ff0000');
      this.print('Type "help" for available commands', '#888');
    }
  },

  executeCommand(cmd) {
    this.exec(cmd);
  },

  print(message, color = '#00ff88') {
    if (!this.output) {
      console.log(message);
      return;
    }

    const line = document.createElement('div');
    line.style.color = color;
    line.textContent = message;
    this.output.appendChild(line);

    // Auto-scroll
    this.output.scrollTop = this.output.scrollHeight;
  },

  addFile(name, content) {
    this.files[name] = content;
    return name;
  },

  getFile(name) {
    return this.files[name];
  },

  listFiles() {
    return Object.keys(this.files).sort();
  }
};

window.ChazonCLI = ChazonCLI;
```

## Features

- **Modular Commands** - Load command sets from separate modules
- **Command History** - Track all executed commands
- **File System** - Virtual filesystem for programs
- **Output Formatting** - Colored terminal output
- **Extensible** - Easy to add new command modules

## Command Modules

Load these modules before initializing CLI:
- `cli-core.md` - Basic commands (ls, cat, help)
- `cli-edit.md` - File editing (edit, save, rm)
- `cli-test.md` - Testing (test, coverage, lint)
- `cli-logs.md` - Logging (logs, tail, grep)
- `cli-git.md` - Version control (status, commit, push)
