# Embed API
**Text Embeddings** | Cohere/OpenAI

Generate vector embeddings using Cohere or OpenAI models.

```javascript
const EmbedAPI = {
  baseURL: '/api',

  async embed(text, model = 'cohere') {
    const response = await fetch(`${this.baseURL}/embed`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, model })
    });

    if (!response.ok) {
      throw new Error(`Embedding failed: ${response.statusText}`);
    }

    const data = await response.json();

    return {
      embedding: data.embedding,
      dimension: data.dimension,
      model: data.model
    };
  },

  async embedBatch(texts, model = 'cohere') {
    const embeddings = [];

    for (const text of texts) {
      const result = await this.embed(text, model);
      embeddings.push(result.embedding);
    }

    return { embeddings, dimension: embeddings[0]?.length || 0 };
  }
};

window.EmbedAPI = EmbedAPI;
```
