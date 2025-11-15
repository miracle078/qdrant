# OpenAI Text Embeddings
**UUID:** 760e861d-afa5-47d7-bf35-c03509263f40
**Model:** text-embedding-3-large (1536 dim)

OpenAI embeddings with lazy loading and caching for text vectorization.

```javascript
const EmbedOpenAI = {
  apiKey: null,
  cache: new Map(),
  model: 'text-embedding-3-large',
  dimension: 1536,

  init(apiKey) {
    this.apiKey = apiKey || localStorage.getItem('openai_api_key');
    return this;
  },

  async embed(text) {
    const cacheKey = `${this.model}:${text}`;

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    const response = await fetch('https://api.openai.com/v1/embeddings', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        input: text,
        model: this.model
      })
    });

    if (!response.ok) {
      console.error(`OpenAI API error: ${response.statusText}`);
      return new Array(this.dimension).fill(0);
    }

    const data = await response.json();
    const embedding = data.data[0].embedding;

    this.cache.set(cacheKey, embedding);

    // Save to SQLite if available
    if (window.DatabaseManager?.db) {
      DatabaseManager.cacheEmbedding(
        '760e861d-afa5-47d7-bf35-c03509263f40',
        text,
        embedding,
        this.model,
        this.dimension
      );
    }

    return embedding;
  },

  async embedBatch(texts, batchSize = 100) {
    const embeddings = [];

    for (let i = 0; i < texts.length; i += batchSize) {
      const batch = texts.slice(i, i + batchSize);
      const batchEmbeddings = await Promise.all(
        batch.map(text => this.embed(text))
      );
      embeddings.push(...batchEmbeddings);
    }

    return embeddings;
  }
};

window.EmbedOpenAI = EmbedOpenAI;
```
