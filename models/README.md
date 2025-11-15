# Models Directory
**Client-Side AI Models** | WebGPU & ONNX Runtime

Small quantized models for client-side inference on GitHub Pages.

## Structure

```
models/
├── embeddings/
│   ├── bert-tiny.onnx           # BERT-tiny for text embeddings
│   ├── distilbert.onnx          # DistilBERT (66MB)
│   └── medical-bert.onnx        # Medical domain BERT
├── vision/
│   ├── mobilenet-v3.onnx        # MobileNetV3 for image features
│   ├── resnet18.onnx            # ResNet-18 (44MB)
│   └── clip-vit-tiny.onnx       # CLIP vision encoder
├── medical/
│   ├── xray-classifier.onnx     # X-ray abnormality detection
│   ├── ct-segmentation.onnx     # CT scan segmentation
│   └── dicom-embedder.onnx      # DICOM image embeddings
└── README.md                     # This file
```

## Model Sizes (Quantized)

| Model | Size | Use Case |
|-------|------|----------|
| BERT-tiny | 17MB | Text embeddings |
| DistilBERT | 66MB | Better text embeddings |
| MobileNetV3 | 5MB | Image features |
| ResNet-18 | 44MB | Image classification |
| CLIP-ViT-tiny | 60MB | Multi-modal embeddings |
| XRay classifier | 25MB | Chest X-ray abnormalities |

## WebGPU Support

### Capabilities
- GPU acceleration for inference
- RAM/VRAM sharing
- Fast matrix operations
- WASM + WebGPU combo

### Fallback Chain
```
WebGPU → WebGL → WASM → CPU
```

## ONNX Runtime Web

### Why ONNX?
- Optimized for web inference
- WebGPU/WebGL/WASM backends
- Quantized INT8/FP16 support
- Small bundle size (~1MB)

### Loading Models
```javascript
// Load ONNX model
const session = await ort.InferenceSession.create('./models/embeddings/bert-tiny.onnx', {
  executionProviders: ['webgpu', 'webgl', 'wasm']
});

// Run inference
const results = await session.run({
  input_ids: inputTensor
});
```

## Usage

### Text Embeddings
```javascript
// Load BERT-tiny
const bert = await ModelLoader.load('embeddings/bert-tiny.onnx');

// Generate embeddings
const text = "chest x-ray shows pneumonia";
const embedding = await bert.embed(text);
// → Float32Array[128] (BERT-tiny output dim)

// Search Qdrant
const results = await QdrantClient.search({
  collection: 'medical_text',
  vector: Array.from(embedding),
  limit: 5
});
```

### Medical Image Analysis
```javascript
// Load X-ray classifier
const xrayModel = await ModelLoader.load('medical/xray-classifier.onnx');

// Analyze X-ray
const imageData = canvasCtx.getImageData(0, 0, 224, 224);
const prediction = await xrayModel.classify(imageData);

// Result: { normal: 0.85, pneumonia: 0.12, fracture: 0.03 }
```

### Image Embeddings
```javascript
// Load MobileNetV3
const mobileNet = await ModelLoader.load('vision/mobilenet-v3.onnx');

// Generate image embedding
const embedding = await mobileNet.embed(imageData);
// → Float32Array[1280] (MobileNetV3 feature dim)
```

## Model Sources

### Hugging Face
```bash
# Download quantized ONNX models
wget https://huggingface.co/optimum/bert-tiny-onnx/resolve/main/model.onnx
wget https://huggingface.co/optimum/distilbert-onnx/resolve/main/model_quantized.onnx
```

### ONNX Model Zoo
```bash
# Download pre-converted models
wget https://github.com/onnx/models/raw/main/vision/classification/mobilenet/model/mobilenetv3-small-1.0-224.onnx
wget https://github.com/onnx/models/raw/main/vision/classification/resnet/model/resnet18-v1-7.onnx
```

### Convert PyTorch/TensorFlow
```python
# Export to ONNX
import torch.onnx

model = YourModel()
dummy_input = torch.randn(1, 3, 224, 224)

torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={'input': {0: 'batch'}}
)

# Quantize
from onnxruntime.quantization import quantize_dynamic

quantize_dynamic(
    "model.onnx",
    "model_quantized.onnx",
    weight_type=QuantType.QUInt8
)
```

## Performance

### WebGPU vs CPU
- **Image inference**: 10-50× faster on GPU
- **Text embeddings**: 5-20× faster on GPU
- **Batch processing**: 100× faster on GPU

### Memory Usage
- Models loaded on-demand
- Shared GPU/RAM via WebGPU
- Model caching in IndexedDB
- Lazy loading for GitHub Pages

## Integration

### Boot Phase
```javascript
// Add to boot-phase3-medical.md or create boot-phase6-models.md
modules: [
  '../modules/model-loader.md',
  '../modules/webgpu-inference.md',
  '../modules/onnx-runtime.md',
  '../modules/bert-embeddings.md',
  '../modules/image-embeddings.md',
  '../modules/medical-inference.md'
]
```

### Medical Imaging Flow
```
Upload X-ray
    ↓
Canvas → ImageData
    ↓
WebGPU Inference (xray-classifier.onnx)
    ↓
Generate Embeddings (mobilenet-v3.onnx)
    ↓
Qdrant Search (find similar cases)
    ↓
Display Results + AI Predictions
```

## Offline Support

### Service Worker
```javascript
// Cache models for offline use
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('models-v1').then((cache) => {
      return cache.addAll([
        '/models/embeddings/bert-tiny.onnx',
        '/models/vision/mobilenet-v3.onnx',
        '/models/medical/xray-classifier.onnx'
      ]);
    })
  );
});
```

## Browser Support

| Browser | WebGPU | WebGL | WASM |
|---------|--------|-------|------|
| Chrome 113+ | ✅ | ✅ | ✅ |
| Edge 113+ | ✅ | ✅ | ✅ |
| Firefox | 🔄 | ✅ | ✅ |
| Safari | 🔄 | ✅ | ✅ |

## Benefits

- ✅ **No backend needed** - Runs on GitHub Pages
- ✅ **Privacy** - All inference client-side
- ✅ **Fast** - WebGPU acceleration
- ✅ **Offline** - Cache models locally
- ✅ **Cost** - No API fees
- ✅ **Medical HIPAA** - Data never leaves browser

---

**Client-Side AI** | WebGPU + ONNX Runtime | GitHub Pages Ready
