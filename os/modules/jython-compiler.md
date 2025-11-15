# Jython 2.7 MD Compiler
**Markdown-to-Jython** | Pure Java Execution

Compiles and executes Python code from markdown files in Jython 2.7 runtime.

```javascript
const JythonCompiler = {
  runtime: null,
  tempDir: null,

  init() {
    this.tempDir = `/tmp/jython_${Date.now()}`;
    this.runtime = {
      jythonJar: './jython/jython-standalone-2.7.3.jar',
      available: false
    };
    return this;
  },

  extractPythonCode(markdown) {
    const pattern = /```python\s*\n([\s\S]*?)\n```/g;
    const blocks = [];
    let match;

    while ((match = pattern.exec(markdown)) !== null) {
      blocks.push(match[1].trim());
    }

    return blocks.join('\n\n');
  },

  async compileMD(mdPath) {
    const response = await fetch(mdPath);
    const markdown = await response.text();
    const pythonCode = this.extractPythonCode(markdown);

    if (!pythonCode) {
      throw new Error('No Python code found in markdown');
    }

    return {
      code: pythonCode,
      path: mdPath,
      compiled: Date.now()
    };
  },

  async executeJython(code, args = []) {
    // Create temp file with code
    const tempFile = `${this.tempDir}/exec_${Date.now()}.py`;

    // In browser, we'd proxy this through backend
    const response = await fetch('/api/jython/execute', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, args })
    });

    return await response.json();
  },

  async runMDFile(mdPath, args = []) {
    const compiled = await this.compileMD(mdPath);
    return await this.executeJython(compiled.code, args);
  }
};

window.JythonCompiler = JythonCompiler;
```
