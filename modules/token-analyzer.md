# Token Analyzer
**UUID:** c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f
**Module Analysis** | Token Counting & Compression

Analyzes markdown modules for token count and dependencies.

```javascript
const TokenAnalyzer = {
  async analyzeModule(path) {
    const response = await fetch(path);
    const content = await response.text();

    // Extract metadata
    const uuidMatch = content.match(/\*\*UUID:\*\*\s+([a-f0-9-]+)/);
    const nameMatch = path.match(/([^/]+)\.md$/);

    // Count tokens (rough estimate: ~4 chars per token)
    const totalTokens = Math.ceil(content.length / 4);

    // Extract code blocks
    const codeBlocks = content.match(/```[\s\S]*?```/g) || [];
    const codeContent = codeBlocks.join('\n');
    const codeTokens = Math.ceil(codeContent.length / 4);
    const docTokens = totalTokens - codeTokens;

    // Detect dependencies
    const dependencies = this.extractDependencies(content);

    // Generate hash
    const contentHash = await this.hashContent(content);

    // Determine category
    const category = this.categorize(path);

    return {
      uuid: uuidMatch ? uuidMatch[1] : this.generateUUID(),
      name: nameMatch ? nameMatch[1] : 'unknown',
      path,
      category,
      tokenCount: totalTokens,
      codeTokens,
      docTokens,
      contentHash,
      dependencies,
      metadata: {
        hasCode: codeBlocks.length > 0,
        codeBlockCount: codeBlocks.length,
        lines: content.split('\n').length
      }
    };
  },

  extractDependencies(content) {
    const deps = [];

    // Look for window.XXX references
    const windowRefs = content.match(/window\.(\w+)/g) || [];
    windowRefs.forEach(ref => {
      const name = ref.replace('window.', '');
      if (name !== 'undefined' && name !== 'null') {
        deps.push({ name, type: 'requires' });
      }
    });

    // Look for fetch() calls to other modules
    const fetchCalls = content.match(/fetch\(['"]([^'"]+\.md)['"]\)/g) || [];
    fetchCalls.forEach(call => {
      const match = call.match(/['"]([^'"]+\.md)['"]/);
      if (match) {
        deps.push({ name: match[1], type: 'imports' });
      }
    });

    return deps;
  },

  categorize(path) {
    if (path.includes('/boot/')) return 'boot';
    if (path.includes('/language/')) return 'language';
    if (path.includes('medical')) return 'medical';
    if (path.includes('cli-')) return 'cli';
    if (path.includes('ui-')) return 'ui';
    if (path.includes('agent-')) return 'ui';
    if (path.includes('program-')) return 'programs';
    if (path.includes('chazon-')) return 'core';
    return 'other';
  },

  async hashContent(content) {
    if (typeof crypto !== 'undefined' && crypto.subtle) {
      const encoder = new TextEncoder();
      const data = encoder.encode(content);
      const hash = await crypto.subtle.digest('SHA-256', data);
      return Array.from(new Uint8Array(hash))
        .map(b => b.toString(16).padStart(2, '0'))
        .join('');
    }
    // Fallback: simple hash
    let hash = 0;
    for (let i = 0; i < content.length; i++) {
      hash = ((hash << 5) - hash) + content.charCodeAt(i);
      hash |= 0;
    }
    return hash.toString(16);
  },

  generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
      const r = Math.random() * 16 | 0;
      const v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  },

  async analyzeAll(paths) {
    const results = [];
    for (const path of paths) {
      try {
        const analysis = await this.analyzeModule(path);
        results.push(analysis);
      } catch (err) {
        console.error(`Failed to analyze ${path}:`, err);
      }
    }
    return results;
  }
};

window.TokenAnalyzer = TokenAnalyzer;
```
