# Text Embeddings
**OpenAI API** | 1536d Vectors

Generate text embeddings using OpenAI's text-embedding-3-large model.

```javascript
const EmbedText = {
  apiKey: null,
  cache: new Map(),

  init(key) {
    this.apiKey = key || window.OPENAI_API_KEY;
    return this;
  },

  async embed(text, model = 'text-embedding-3-large') {
    // Check cache
    const cacheKey = `${model}:${text}`;
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    // Call API
    try {
      const response = await fetch('https://api.openai.com/v1/embeddings', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.apiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: text, model })
      });

      const data = await response.json();
      const embedding = data.data[0].embedding;

      // Cache result
      this.cache.set(cacheKey, embedding);

      return embedding;
    } catch (err) {
      console.error('Embedding error:', err);
      // Return zero vector fallback
      const dim = model.includes('3-large') ? 1536 : 1536;
      return new Array(dim).fill(0);
    }
  },

  async embedBatch(texts, model = 'text-embedding-3-large') {
    const response = await fetch('https://api.openai.com/v1/embeddings', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ input: texts, model })
    });

    const data = await response.json();
    return data.data.map(item => item.embedding);
  }
};

window.EmbedText = EmbedText;
```
