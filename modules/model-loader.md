# Model Loader
**UUID:** c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f
**Model Management** | Download, Cache, Load

Client-side model loader with IndexedDB caching.

```javascript
const ModelLoader = {
  dbName: 'chazon-models',
  dbVersion: 1,
  db: null,

  models: {
    'bert-tiny': {
      url: 'https://huggingface.co/optimum/bert-tiny-onnx/resolve/main/model.onnx',
      size: 17 * 1024 * 1024, // 17MB
      type: 'embeddings'
    },
    'mobilenet-v3': {
      url: 'https://github.com/onnx/models/raw/main/vision/classification/mobilenet/model/mobilenetv3-small-1.0-224.onnx',
      size: 5 * 1024 * 1024, // 5MB
      type: 'vision'
    },
    'distilbert': {
      url: 'https://huggingface.co/optimum/distilbert-base-uncased-onnx/resolve/main/model_quantized.onnx',
      size: 66 * 1024 * 1024, // 66MB
      type: 'embeddings'
    }
  },

  async initDB() {
    if (this.db) return this.db;

    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, this.dbVersion);

      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve(this.db);
      };

      request.onupgradeneeded = (event) => {
        const db = event.target.result;

        if (!db.objectStoreNames.contains('models')) {
          db.createObjectStore('models', { keyPath: 'name' });
        }
      };
    });
  },

  async getFromCache(modelName) {
    const db = await this.initDB();

    return new Promise((resolve, reject) => {
      const transaction = db.transaction(['models'], 'readonly');
      const store = transaction.objectStore('models');
      const request = store.get(modelName);

      request.onsuccess = () => resolve(request.result?.data);
      request.onerror = () => reject(request.error);
    });
  },

  async saveToCache(modelName, data) {
    const db = await this.initDB();

    return new Promise((resolve, reject) => {
      const transaction = db.transaction(['models'], 'readwrite');
      const store = transaction.objectStore('models');
      const request = store.put({
        name: modelName,
        data: data,
        timestamp: Date.now()
      });

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  },

  async download(modelName, onProgress) {
    const modelInfo = this.models[modelName];
    if (!modelInfo) {
      throw new Error(`Unknown model: ${modelName}`);
    }

    console.log(`Downloading model: ${modelName} (${(modelInfo.size / 1024 / 1024).toFixed(1)}MB)`);

    const response = await fetch(modelInfo.url);
    if (!response.ok) {
      throw new Error(`Failed to download model: ${response.statusText}`);
    }

    const contentLength = response.headers.get('content-length');
    const total = parseInt(contentLength, 10) || modelInfo.size;

    const reader = response.body.getReader();
    const chunks = [];
    let received = 0;

    while (true) {
      const { done, value } = await reader.read();

      if (done) break;

      chunks.push(value);
      received += value.length;

      if (onProgress) {
        onProgress({
          loaded: received,
          total,
          percentage: (received / total) * 100
        });
      }
    }

    const blob = new Blob(chunks);
    const arrayBuffer = await blob.arrayBuffer();

    await this.saveToCache(modelName, arrayBuffer);

    return arrayBuffer;
  },

  async load(modelName, options = {}) {
    // Check cache first
    let modelData = await this.getFromCache(modelName);

    if (!modelData) {
      // Download if not cached
      console.log(`Model not in cache, downloading: ${modelName}`);
      modelData = await this.download(modelName, options.onProgress);
    } else {
      console.log(`Model loaded from cache: ${modelName}`);
    }

    // Load with ONNX Runtime
    const session = await ONNXRuntime.loadModel(modelData, {
      providers: options.providers || ['webgpu', 'webgl', 'wasm']
    });

    return this.createModelWrapper(modelName, session);
  },

  createModelWrapper(modelName, session) {
    const modelType = this.models[modelName]?.type || 'unknown';

    return {
      name: modelName,
      type: modelType,
      session,

      async run(inputs) {
        return await ONNXRuntime.run(session, inputs);
      },

      async embed(data) {
        // Generic embedding function
        const result = await this.run({ input: data });
        const outputName = session.outputNames[0];
        return result[outputName].data;
      },

      async classify(data) {
        // Generic classification function
        const result = await this.run({ input: data });
        const outputName = session.outputNames[0];
        const logits = Array.from(result[outputName].data);

        // Softmax
        const max = Math.max(...logits);
        const exps = logits.map(x => Math.exp(x - max));
        const sum = exps.reduce((a, b) => a + b, 0);
        const probs = exps.map(x => x / sum);

        return probs;
      }
    };
  },

  async listCached() {
    const db = await this.initDB();

    return new Promise((resolve, reject) => {
      const transaction = db.transaction(['models'], 'readonly');
      const store = transaction.objectStore('models');
      const request = store.getAllKeys();

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  },

  async clearCache() {
    const db = await this.initDB();

    return new Promise((resolve, reject) => {
      const transaction = db.transaction(['models'], 'readwrite');
      const store = transaction.objectStore('models');
      const request = store.clear();

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  },

  async getCacheSize() {
    const db = await this.initDB();

    return new Promise((resolve, reject) => {
      const transaction = db.transaction(['models'], 'readonly');
      const store = transaction.objectStore('models');
      const request = store.getAll();

      request.onsuccess = () => {
        const models = request.result;
        const totalSize = models.reduce((sum, model) => {
          return sum + (model.data?.byteLength || 0);
        }, 0);

        resolve({
          count: models.length,
          totalSize,
          models: models.map(m => ({
            name: m.name,
            size: m.data?.byteLength || 0,
            timestamp: m.timestamp
          }))
        });
      };

      request.onerror = () => reject(request.error);
    });
  }
};

window.ModelLoader = ModelLoader;
```
