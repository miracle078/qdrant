# AI Inference Modules
**Type:** AI/ML | Inference Engine

AI model loading, inference, and GPU acceleration modules.

## Modules

### Model Loading
- **model-loader.md** - Dynamic ONNX model loader
  - Load models from files or URLs
  - Model caching and versioning
  - Metadata extraction

### ONNX Runtime
- **onnx-runtime.md** - ONNX inference engine
  - CPU and GPU backends
  - Batch inference
  - Performance optimization

### WebGPU Inference
- **webgpu-inference.md** - Browser-based GPU inference
  - WebGPU acceleration
  - Shader compilation
  - Real-time inference

## Architecture

```
┌─────────────────┐
│  Model Loader   │
└────────┬────────┘
         │
┌────────▼────────┐
│  ONNX Runtime   │ ← CPU/GPU Backend
└────────┬────────┘
         │
┌────────▼────────┐
│ WebGPU Inference│ ← Browser GPU
└─────────────────┘
```

## Usage

```javascript
// Load model
const model = await ModelLoader.load('bert-tiny.onnx');

// Run inference (ONNX Runtime)
const output = await ONNXRuntime.infer(model, input);

// Run inference (WebGPU)
const result = await WebGPUInference.infer(model, input);
```

## See Also

- `../../models/` - AI model files (ONNX)
- `../../medical/` - Medical imaging AI
- `../../../controls/tag-providers/models.json` - Model tags
