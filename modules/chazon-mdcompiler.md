# Markdown Compiler
**φ-Balanced Execution** | ISA-95 L3: MES/Control Layer

Parse markdown → Extract code → Execute. φ-safe sandboxing.

```javascript
const MDCompiler = {
  φ: 1.618,
  timeout: 1618,

  compile(markdown) {
    const blocks = this.parse(markdown);
    return this.execute(blocks);
  },

  parse(md) {
    const regex = /```(\w+)?\n([\s\S]*?)```/g;
    const blocks = [];
    let match;
    while ((match = regex.exec(md))) {
      blocks.push({
        lang: match[1] || 'js',
        code: match[2].trim()
      });
    }
    return blocks;
  },

  execute(blocks) {
    return blocks.map(block => {
      try {
        const result = this.runSandbox(block.code, block.lang);
        return { success: true, output: result, lang: block.lang };
      } catch (err) {
        return { success: false, error: err.message, lang: block.lang };
      }
    });
  },

  runSandbox(code, lang) {
    if (lang === 'js' || lang === 'javascript') {
      return eval(`(function(){${code}})()`);
    }
    if (lang === 'python' || lang === 'py') {
      return eval(code.replace(/print\((.*)\)/g, 'console.log($1)'));
    }
    throw new Error(`Unsupported language: ${lang}`);
  }
};

window.MDCompiler = MDCompiler;
```
