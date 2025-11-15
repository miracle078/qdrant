# CodeBERT Embeddings
**UUID:** f66182df-7159-49cd-a5f5-9d078d83d854
**Model:** microsoft/codebert-base (768 dim)

Code embeddings for PLC code, Ladder Logic, Structured Text with transformer.

```javascript
const EmbedCodeBERT = {
  modelUrl: 'https://huggingface.co/microsoft/codebert-base',
  model: null,
  dimension: 768,
  cache: new Map(),

  async init() {
    // Use Transformers.js for browser-based inference
    const { pipeline } = await import('https://cdn.jsdelivr.net/npm/@xenova/transformers@2.6.0');

    this.model = await pipeline('feature-extraction', 'Xenova/codebert-base');
    console.log('✓ CodeBERT loaded (browser mode)');

    return this;
  },

  async embed(code) {
    if (!this.model) await this.init();

    const cacheKey = code.slice(0, 100);

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    try {
      const output = await this.model(code, {
        pooling: 'mean',
        normalize: true
      });

      const embedding = Array.from(output.data);

      this.cache.set(cacheKey, embedding);

      if (window.DatabaseManager?.db) {
        DatabaseManager.cacheEmbedding(
          'f66182df-7159-49cd-a5f5-9d078d83d854',
          code,
          embedding,
          'codebert-base',
          this.dimension
        );
      }

      return embedding;
    } catch (error) {
      console.error('CodeBERT error:', error);
      return new Array(this.dimension).fill(0);
    }
  },

  async embedBatch(codes, batchSize = 32) {
    const embeddings = [];

    for (let i = 0; i < codes.length; i += batchSize) {
      const batch = codes.slice(i, i + batchSize);
      const batchEmbeddings = await Promise.all(
        batch.map(code => this.embed(code))
      );
      embeddings.push(...batchEmbeddings);
    }

    return embeddings;
  }
};

window.EmbedCodeBERT = EmbedCodeBERT;
```
