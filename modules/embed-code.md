# Code Embeddings
**Code Understanding** | PLC/ST/Ladder

Embed PLC code using OpenAI (CodeBERT alternative).

```javascript
const EmbedCode = {
  async embed(code, language = null) {
    // Prefix with language for better context
    let text = code;
    if (language) {
      text = `# Language: ${language}\n${code}`;
    }

    // Use text embedding (works well for code)
    return await EmbedText.embed(text, 'text-embedding-3-small');
  },

  async embedWithMetadata(codeObj) {
    const { code, lang, platform, function: fn } = codeObj;

    // Build context string
    const context = `
Language: ${lang}
Platform: ${platform}
Function: ${fn}

Code:
${code}
    `.trim();

    return await this.embed(context, lang);
  }
};

window.EmbedCode = EmbedCode;
```
