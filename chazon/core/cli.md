# Chazon CLI
**Command Line Interface** | ISA-95 L2: Supervisory Control

Parse commands, execute programs, manage virtual filesystem.

```javascript
const ChazonCLI = {
  fs: {},
  cwd: '/',

  exec(input) {
    const [cmd, ...args] = input.trim().split(/\s+/);
    const commands = {
      help: () => 'Commands: run, ls, cat, cd, pwd, clear',
      run: () => this.runProgram(args[0]),
      ls: () => Object.keys(this.fs).join('\n'),
      cat: () => this.fs[args[0]] || 'File not found',
      cd: () => { this.cwd = args[0] || '/'; return `→ ${this.cwd}`; },
      pwd: () => this.cwd,
      clear: () => { console.clear(); return ''; }
    };
    return commands[cmd] ? commands[cmd]() : `Unknown: ${cmd}`;
  },

  runProgram(name) {
    const program = this.fs[name];
    if (!program) return `Not found: ${name}`;
    try {
      const compiler = window.MDCompiler || window.ChazonOS?.modules?.compiler;
      const results = compiler.compile(program);
      return results.map(r => r.success ? r.output : `⚠️ ${r.error}`).join('\n');
    } catch (err) {
      return `Failed: ${err.message}`;
    }
  },

  addFile(name, content) {
    this.fs[name] = content;
  }
};

window.ChazonCLI = ChazonCLI;
```
