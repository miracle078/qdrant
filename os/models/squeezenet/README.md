# SqueezeNet Tiny

**Type:** Lightweight Image Classification
**Framework:** ONNX
**Size:** ~784 MB (untrained)
**Input:** Image (float32, shape: [1, 3, 224, 224])
**Output:** Class probabilities (float32, shape: [1, 1000])

## Usage

```javascript
// Load model
const session = await ort.InferenceSession.create('models/squeezenet/squeezenet-tiny.onnx');

// Preprocess image
const imageData = preprocessImage(inputImage, 224, 224);
const tensor = new ort.Tensor('float32', imageData, [1, 3, 224, 224]);

// Run inference
const outputs = await session.run({ input: tensor });
const predictions = outputs.output.data;

// Get top-5 predictions
const topK = getTopK(predictions, 5);
```

## Why SqueezeNet?

- **Tiny model size:** 50x smaller than AlexNet
- **Fast inference:** Optimized for edge devices
- **Good accuracy:** Comparable to AlexNet
- **Fire modules:** Squeeze + expand architecture

## Pre-trained Models

```bash
# Download from ONNX Model Zoo (requires git-lfs)
git lfs install
git clone https://github.com/onnx/models
# Model at: models/vision/classification/squeezenet/model/squeezenet1.1-7.onnx
```

## Medical Imaging Adaptation

SqueezeNet works well for:
- Real-time diagnosis on mobile devices
- Lightweight dermatology classifiers
- Retinal image screening
- Pathology slide classification
