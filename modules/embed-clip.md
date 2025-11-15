# CLIP Image Embeddings
**UUID:** c6a53bf8-34eb-4620-8e87-ac8629f97d1b
**Model:** openai/clip-vit-base-patch32 (512 dim)

Multimodal embeddings for P&ID diagrams, HMI screens, process diagrams.

```javascript
const EmbedCLIP = {
  model: null,
  processor: null,
  dimension: 512,
  cache: new Map(),

  async init() {
    const { AutoModel, AutoProcessor } = await import(
      'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.6.0'
    );

    this.model = await AutoModel.from_pretrained('Xenova/clip-vit-base-patch32');
    this.processor = await AutoProcessor.from_pretrained('Xenova/clip-vit-base-patch32');

    console.log('✓ CLIP loaded (vision + text)');
    return this;
  },

  async embedImage(imageUrl) {
    if (!this.model) await this.init();

    const cacheKey = `img:${imageUrl}`;

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    try {
      const img = await this.loadImage(imageUrl);
      const inputs = await this.processor(img);
      const output = await this.model(inputs);
      const embedding = Array.from(output.image_embeds.data);

      this.cache.set(cacheKey, embedding);
      return embedding;
    } catch (error) {
      console.error('CLIP image error:', error);
      return new Array(this.dimension).fill(0);
    }
  },

  async embedText(text) {
    if (!this.model) await this.init();

    const cacheKey = `txt:${text}`;

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    try {
      const inputs = await this.processor(text, { padding: true });
      const output = await this.model(inputs);
      const embedding = Array.from(output.text_embeds.data);

      this.cache.set(cacheKey, embedding);
      return embedding;
    } catch (error) {
      console.error('CLIP text error:', error);
      return new Array(this.dimension).fill(0);
    }
  },

  async loadImage(url) {
    return new Promise((resolve, reject) => {
      const img = new Image();
      img.crossOrigin = 'anonymous';
      img.onload = () => resolve(img);
      img.onerror = reject;
      img.src = url;
    });
  }
};

window.EmbedCLIP = EmbedCLIP;
```
