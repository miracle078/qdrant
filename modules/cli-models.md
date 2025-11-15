# CLI Models Commands
**UUID:** e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b
**Model CLI** | Model Management Commands

CLI commands for model management and inference.

```javascript
const CLIModels = {
  commands: {
    'models:list': {
      description: 'List available models',
      async execute(args, cli) {
        cli.print('\nAvailable Models:', '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');

        Object.entries(ModelLoader.models).forEach(([name, info]) => {
          const sizeMB = (info.size / 1024 / 1024).toFixed(1);
          cli.print(`${name.padEnd(20)} ${sizeMB.padStart(6)}MB  ${info.type}`, '#00ff88');
        });

        cli.print('', '#888');
      }
    },

    'models:cached': {
      description: 'List cached models',
      async execute(args, cli) {
        const cached = await ModelLoader.listCached();

        cli.print('\nCached Models:', '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');

        if (cached.length === 0) {
          cli.print('No models cached', '#888');
        } else {
          cached.forEach(name => {
            cli.print(`✓ ${name}`, '#00ff88');
          });
        }

        cli.print('', '#888');
      }
    },

    'models:download': {
      description: 'Download a model',
      usage: 'models:download <model-name>',
      async execute(args, cli) {
        if (!args[0]) {
          cli.print('Usage: models:download <model-name>', '#ff0044');
          cli.print('Available: bert-tiny, mobilenet-v3, distilbert', '#888');
          return;
        }

        const modelName = args[0];

        cli.print(`Downloading ${modelName}...`, '#00ccff');

        try {
          await ModelLoader.download(modelName, (progress) => {
            const pct = progress.percentage.toFixed(1);
            const bar = '█'.repeat(Math.floor(pct / 2)) + '░'.repeat(50 - Math.floor(pct / 2));
            cli.print(`\r[${bar}] ${pct}%`, '#00ff88', true);
          });

          cli.print(`\n✓ Downloaded ${modelName}`, '#00ff88');
        } catch (err) {
          cli.print(`\n✗ Download failed: ${err.message}`, '#ff0044');
        }
      }
    },

    'models:load': {
      description: 'Load a model',
      usage: 'models:load <model-name>',
      async execute(args, cli) {
        if (!args[0]) {
          cli.print('Usage: models:load <model-name>', '#ff0044');
          return;
        }

        const modelName = args[0];
        cli.print(`Loading ${modelName}...`, '#00ccff');

        try {
          const model = await ModelLoader.load(modelName);
          cli.print(`✓ Loaded ${modelName}`, '#00ff88');
          cli.print(`  Type: ${model.type}`, '#888');
          cli.print(`  Inputs: ${model.session.inputNames.join(', ')}`, '#888');
          cli.print(`  Outputs: ${model.session.outputNames.join(', ')}`, '#888');
        } catch (err) {
          cli.print(`✗ Load failed: ${err.message}`, '#ff0044');
        }
      }
    },

    'models:clear': {
      description: 'Clear model cache',
      async execute(args, cli) {
        cli.print('Clearing model cache...', '#00ccff');
        await ModelLoader.clearCache();
        cli.print('✓ Cache cleared', '#00ff88');
      }
    },

    'models:info': {
      description: 'Show model cache info',
      async execute(args, cli) {
        const info = await ModelLoader.getCacheSize();

        cli.print('\nModel Cache Info:', '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');
        cli.print(`Models cached: ${info.count}`, '#00ff88');
        cli.print(`Total size: ${(info.totalSize / 1024 / 1024).toFixed(1)}MB`, '#00ff88');

        if (info.models.length > 0) {
          cli.print('\nCached Models:', '#00ccff');
          info.models.forEach(m => {
            const sizeMB = (m.size / 1024 / 1024).toFixed(1);
            const date = new Date(m.timestamp).toLocaleString();
            cli.print(`  ${m.name}: ${sizeMB}MB (${date})`, '#888');
          });
        }

        cli.print('', '#888');
      }
    },

    'models:backend': {
      description: 'Show inference backend info',
      async execute(args, cli) {
        const info = await ONNXRuntime.getBackendInfo();

        cli.print('\nInference Backend Info:', '#00ccff');
        cli.print('─────────────────────────────────────────', '#888');
        cli.print(`Available: ${info.available.join(', ')}`, '#00ff88');
        cli.print(`Preferred: ${info.preferred}`, '#00ff88');
        cli.print(`WebGPU: ${info.webgpuSupport ? '✓' : '✗'}`, info.webgpuSupport ? '#00ff88' : '#ff0044');
        cli.print(`WebGL: ${info.webglVersion}`, '#888');

        if (WebGPUInference.supported) {
          const gpuInfo = WebGPUInference.getInfo();
          cli.print('\nWebGPU Details:', '#00ccff');
          cli.print(`  Vendor: ${gpuInfo.vendor}`, '#888');
          cli.print(`  Architecture: ${gpuInfo.architecture}`, '#888');
          cli.print(`  Max Buffer: ${(gpuInfo.maxBufferSize / 1024 / 1024).toFixed(0)}MB`, '#888');
        }

        cli.print('', '#888');
      }
    },

    'models:benchmark': {
      description: 'Benchmark inference performance',
      usage: 'models:benchmark [model-name]',
      async execute(args, cli) {
        const modelName = args[0] || 'mobilenet-v3';

        cli.print(`Benchmarking ${modelName}...`, '#00ccff');

        try {
          const model = await ModelLoader.load(modelName);
          const result = await ONNXRuntime.benchmark(model.session);

          cli.print('\nBenchmark Results:', '#00ccff');
          cli.print('─────────────────────────────────────────', '#888');
          cli.print(`Model: ${result.model}`, '#00ff88');
          cli.print(`Backend: ${result.backend}`, '#00ff88');
          cli.print(`Iterations: ${result.iterations}`, '#888');
          cli.print(`Avg time: ${result.avgTime.toFixed(2)}ms`, '#888');
          cli.print(`Throughput: ${result.throughput.toFixed(1)} inferences/sec`, '#00ff88');
          cli.print('', '#888');
        } catch (err) {
          cli.print(`✗ Benchmark failed: ${err.message}`, '#ff0044');
        }
      }
    },

    'models:test-xray': {
      description: 'Test X-ray analysis (demo)',
      async execute(args, cli) {
        cli.print('Testing X-ray analysis...', '#00ccff');

        try {
          // Create dummy image
          const canvas = document.createElement('canvas');
          canvas.width = 224;
          canvas.height = 224;
          const ctx = canvas.getContext('2d');
          ctx.fillStyle = '#808080';
          ctx.fillRect(0, 0, 224, 224);

          const imageData = ctx.getImageData(0, 0, 224, 224);

          // Run analysis
          await MedicalInference.init();
          const result = await MedicalInference.analyzeXRay(imageData);

          cli.print('\nAnalysis Results:', '#00ccff');
          cli.print('─────────────────────────────────────────', '#888');

          result.predictions.slice(0, 5).forEach(pred => {
            const pct = (pred.confidence * 100).toFixed(1);
            cli.print(`${pred.label.padEnd(15)} ${pct.padStart(5)}%`, '#00ff88');
          });

          cli.print('', '#888');
        } catch (err) {
          cli.print(`✗ Test failed: ${err.message}`, '#ff0044');
        }
      }
    }
  },

  register(cli) {
    Object.entries(this.commands).forEach(([name, cmd]) => {
      cli.registerCommand(name, cmd);
    });
  }
};

// Auto-register
if (window.ChazonCLI) {
  CLIModels.register(ChazonCLI);
}

window.CLIModels = CLIModels;
```
