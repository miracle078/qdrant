# MobileNet-V2 Tiny

**Type:** Image Classification
**Framework:** ONNX
**Size:** ~784 MB (untrained)
**Input:** Image (float32, shape: [1, 3, 224, 224])
**Output:** Class probabilities (float32, shape: [1, 1000])

## Usage

```javascript
// Load model
const session = await ort.InferenceSession.create('models/mobilenet-v2/mobilenet-tiny.onnx');

// Preprocess image to [1, 3, 224, 224]
const imageData = preprocessImage(inputImage, 224, 224);
const tensor = new ort.Tensor('float32', imageData, [1, 3, 224, 224]);

// Run inference
const outputs = await session.run({ input: tensor });
const predictions = outputs.output.data;
```

## Pre-trained Models

Download actual pre-trained MobileNet-V2:

```bash
# From PyTorch Hub
python -c "import torch; torch.hub.load('pytorch/vision', 'mobilenet_v2', pretrained=True)"

# Export to ONNX
python -m torch.onnx.export ...
```

## Medical Imaging

For medical imaging, consider:
- ResNet-18/50 (transfer learning from ImageNet)
- DenseNet-121 (CheXNet for chest X-rays)
- EfficientNet-B0 (lightweight, accurate)
