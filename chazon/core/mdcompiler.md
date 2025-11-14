# Markdown Compiler
**Client-Side Execution** | ISA-95 L3: MES/Control Layer

Parse markdown → Extract code blocks → Execute in sandbox.

```javascript
const MDCompiler = {
  compile(markdown) {
    const blocks = this.parse(markdown);
    return this.execute(blocks);
  },

  parse(md) {
    const regex = /```(\w+)?\n([\s\S]*?)```/g;
    const blocks = [];
    let match;
    while ((match = regex.exec(md))) {
      blocks.push({ lang: match[1] || 'js', code: match[2].trim() });
    }
    return blocks;
  },

  execute(blocks) {
    const results = [];
    for (const block of blocks) {
      try {
        const result = this.runSandbox(block.code, block.lang);
        results.push({ success: true, output: result });
      } catch (err) {
        results.push({ success: false, error: err.message });
      }
    }
    return results;
  },

  runSandbox(code, lang) {
    if (lang === 'js' || lang === 'javascript') {
      return eval(`(function(){${code}})()`);
    }
    if (lang === 'python' || lang === 'py') {
      return eval(code.replace(/print\((.*)\)/g, 'console.log($1)'));
    }
    throw new Error(`Unsupported: ${lang}`);
  }
};

window.MDCompiler = MDCompiler;
```
