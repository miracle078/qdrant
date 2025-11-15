# ONNX Runtime Web
**UUID:** b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e
**ONNX Inference** | WebGPU/WebGL/WASM Backends

ONNX Runtime Web wrapper for model inference.

```javascript
const ONNXRuntime = {
  loaded: false,
  sessions: new Map(),

  async init() {
    if (this.loaded) return true;

    // Load ONNX Runtime Web from CDN
    if (typeof ort === 'undefined') {
      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/npm/onnxruntime-web@1.17.0/dist/ort.min.js';

      await new Promise((resolve, reject) => {
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
      });
    }

    // Configure backends
    ort.env.wasm.wasmPaths = 'https://cdn.jsdelivr.net/npm/onnxruntime-web@1.17.0/dist/';

    this.loaded = true;
    console.log('ONNX Runtime Web initialized');
    return true;
  },

  async loadModel(path, options = {}) {
    if (!this.loaded) {
      await this.init();
    }

    if (this.sessions.has(path)) {
      return this.sessions.get(path);
    }

    const sessionOptions = {
      executionProviders: options.providers || ['webgpu', 'webgl', 'wasm'],
      graphOptimizationLevel: 'all',
      ...options
    };

    try {
      console.log(`Loading model: ${path}`);
      const session = await ort.InferenceSession.create(path, sessionOptions);

      this.sessions.set(path, session);

      console.log(`Model loaded: ${path}`, {
        inputNames: session.inputNames,
        outputNames: session.outputNames
      });

      return session;
    } catch (err) {
      console.error(`Failed to load model ${path}:`, err);
      throw err;
    }
  },

  async run(sessionOrPath, inputs) {
    let session;

    if (typeof sessionOrPath === 'string') {
      session = await this.loadModel(sessionOrPath);
    } else {
      session = sessionOrPath;
    }

    // Convert inputs to tensors
    const feeds = {};
    for (const [name, data] of Object.entries(inputs)) {
      if (data instanceof ort.Tensor) {
        feeds[name] = data;
      } else {
        // Auto-detect tensor type and shape
        feeds[name] = this.createTensor(data);
      }
    }

    try {
      const results = await session.run(feeds);
      return results;
    } catch (err) {
      console.error('Inference failed:', err);
      throw err;
    }
  },

  createTensor(data) {
    if (data instanceof Float32Array) {
      return new ort.Tensor('float32', data, [1, data.length]);
    } else if (data instanceof Int32Array || data instanceof BigInt64Array) {
      return new ort.Tensor('int64', data, [1, data.length]);
    } else if (Array.isArray(data)) {
      // Assume 2D array
      const flat = data.flat();
      const shape = [data.length, data[0].length];
      return new ort.Tensor('float32', new Float32Array(flat), shape);
    } else {
      throw new Error('Unsupported data type for tensor');
    }
  },

  async benchmark(modelPath) {
    const session = await this.loadModel(modelPath);

    // Get input shape from model
    const inputName = session.inputNames[0];
    const inputMeta = session.inputMetadata[inputName];
    const inputShape = inputMeta.shape;

    // Create dummy input
    const inputSize = inputShape.reduce((a, b) => a * b, 1);
    const inputData = new Float32Array(inputSize).fill(1.0);
    const inputTensor = new ort.Tensor('float32', inputData, inputShape);

    // Warmup
    await session.run({ [inputName]: inputTensor });

    // Benchmark
    const iterations = 10;
    const start = performance.now();

    for (let i = 0; i < iterations; i++) {
      await session.run({ [inputName]: inputTensor });
    }

    const end = performance.now();
    const avgTime = (end - start) / iterations;

    return {
      model: modelPath,
      iterations,
      avgTime,
      throughput: 1000 / avgTime,
      inputShape,
      backend: session.handler._backend || 'unknown'
    };
  },

  async getBackendInfo() {
    if (!this.loaded) {
      await this.init();
    }

    const backends = [];

    // Check WebGPU
    if (navigator.gpu) {
      backends.push('webgpu');
    }

    // Check WebGL
    const canvas = document.createElement('canvas');
    const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
    if (gl) {
      backends.push('webgl');
    }

    // WASM always available
    backends.push('wasm');
    backends.push('cpu');

    return {
      available: backends,
      preferred: backends[0],
      webgpuSupport: navigator.gpu !== undefined,
      webglVersion: gl ? (gl.getParameter(gl.VERSION)) : 'not supported'
    };
  },

  clearCache() {
    this.sessions.clear();
    console.log('Model cache cleared');
  }
};

window.ONNXRuntime = ONNXRuntime;
```
