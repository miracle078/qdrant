# Chazon CLI
**φ-Balanced Interface** | ISA-95 L2: Supervisory Control

Command parsing, program execution, virtual filesystem. φ = 1.618.

```javascript
const ChazonCLI = {
  φ: 1.618,
  fs: {},
  cwd: '/',
  history: [],

  exec(input) {
    if (!input?.trim()) return '';
    this.history.push(input);
    const [cmd, ...args] = input.trim().split(/\s+/);

    const commands = {
      help: () => 'Commands: run, ls, cat, cd, pwd, clear, version',
      run: () => this.runProgram(args[0]),
      ls: () => Object.keys(this.fs).sort().join('\n'),
      cat: () => this.fs[args[0]] || `File not found: ${args[0]}`,
      cd: () => { this.cwd = args[0] || '/'; return `→ ${this.cwd}`; },
      pwd: () => this.cwd,
      clear: () => { console.clear(); return ''; },
      version: () => `Chazon OS ${window.ChazonOS?.version || '1.0.0'} | φ=${this.φ}`
    };

    return commands[cmd] ? commands[cmd]() : `Unknown command: ${cmd}`;
  },

  runProgram(name) {
    const program = this.fs[name];
    if (!program) return `Program not found: ${name}`;

    try {
      const compiler = window.ChazonOS?.getModule('compiler') || window.MDCompiler;
      if (!compiler) return 'Error: Compiler not loaded';

      const results = compiler.compile(program);
      return results.map(r =>
        r.success ? (r.output ?? 'OK') : `⚠️ ${r.error}`
      ).join('\n');
    } catch (err) {
      return `Execution failed: ${err.message}`;
    }
  },

  addFile(name, content) {
    this.fs[name] = content;
    return name;
  }
};

window.ChazonCLI = ChazonCLI;
```
