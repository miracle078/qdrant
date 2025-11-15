# SNT Parser
**UUID:** 4a7f9e2c-6d1b-4f3e-8a5c-9d2f6e4b1a7c
**Space-Time Notation Parser** | Trinary Compiler Interface

Parses SNT syntax and compiles to trinary space-time code.

```javascript
const SNTParser = {
  parse(sntCode) {
    const lines = sntCode.split('\n').filter(l => l.trim());
    const ast = [];

    lines.forEach(line => {
      const node = this.parseLine(line);
      if (node) ast.push(node);
    });

    return ast;
  },

  parseLine(line) {
    // Timeline declarations: @past, @present, @future
    if (line.startsWith('@')) {
      const time = line.slice(1).split(' ')[0];
      const code = line.slice(line.indexOf(' ') + 1);
      return { type: 'timeline', time, code };
    }

    // Emoji operations: 🔮.encode(value)
    if (line.includes('🔮')) {
      const match = line.match(/🔮\.(\w+)\((.*?)\)/);
      if (match) {
        return { type: 'emoji', op: match[1], args: match[2] };
      }
    }

    // Quantum states: |0⟩, |1⟩, |+⟩
    if (line.includes('|') && line.includes('⟩')) {
      return { type: 'quantum', state: line.match(/\|(.*?)⟩/)[1] };
    }

    // Standard code
    return { type: 'code', line };
  },

  compile(ast, timeline = 0) {
    if (!window.SpaceTimeCompiler) {
      throw new Error('SpaceTimeCompiler not loaded');
    }

    const results = [];

    ast.forEach(node => {
      if (node.type === 'timeline') {
        const offset = { past: -1, present: 0, future: 1 }[node.time] || 0;
        const compiled = SpaceTimeCompiler.compile(node.code, timeline + offset);
        results.push({ ...compiled, timeline: timeline + offset });
      } else if (node.type === 'emoji') {
        results.push(this.compileEmoji(node));
      } else if (node.type === 'quantum') {
        results.push(this.compileQuantum(node));
      } else {
        const compiled = SpaceTimeCompiler.compile(node.line, timeline);
        results.push(compiled);
      }
    });

    return results;
  },

  compileEmoji(node) {
    if (!window.TrinaryCore) {
      throw new Error('TrinaryCore not loaded');
    }

    switch (node.op) {
      case 'encode':
        const trits = TrinaryCore.encode(parseInt(node.args));
        return { type: 'emoji', op: 'encode', trits };
      case 'decode':
        const value = TrinaryCore.decode(JSON.parse(node.args));
        return { type: 'emoji', op: 'decode', value };
      default:
        return { type: 'emoji', op: node.op, args: node.args };
    }
  },

  compileQuantum(node) {
    const stateMap = { '0': 1, '1': -1, '+': 0 };
    const trit = stateMap[node.state] ?? 0;
    return { type: 'quantum', state: node.state, trit };
  },

  exec(sntCode, timeline = 0) {
    const ast = this.parse(sntCode);
    const compiled = this.compile(ast, timeline);
    return compiled;
  }
};

window.SNTParser = SNTParser;
```

## Syntax Examples

```snt
@past load data
@present compute result
@future store output

🔮.encode(42)
🔮.decode([1, 1, -1, 0, 0])

|0⟩ + |1⟩ = |+⟩
```
