# ResNet-18 Medical

**Type:** Medical Image Classification
**Framework:** ONNX
**Size:** ~3.1 MB
**Input:** Image (float32, shape: [1, 3, 224, 224])
**Output:** Binary classification (float32, shape: [1, 2]) - [normal, abnormal]

## Usage

```javascript
// Load model
const session = await ort.InferenceSession.create('models/resnet18/resnet18-medical.onnx');

// Preprocess medical image
const imageData = preprocessMedicalImage(xrayImage, 224, 224);
const tensor = new ort.Tensor('float32', imageData, [1, 3, 224, 224]);

// Run inference
const outputs = await session.run({ input: tensor });
const [normalProb, abnormalProb] = outputs.output.data;

console.log(`Normal: ${normalProb.toFixed(2)}, Abnormal: ${abnormalProb.toFixed(2)}`);
```

## Pre-trained Medical Models

For production medical imaging:

```bash
# CheXNet (Chest X-ray pathology detection)
# Source: Stanford ML Group
wget https://github.com/arnoweng/CheXNet/releases/download/v1.0/model.pth.tar

# NIH Chest X-ray (14 diseases)
# Source: NIH Clinical Center
# Dataset: https://www.kaggle.com/datasets/nih-chest-xrays/data
```

## Training on Medical Data

Fine-tune on domain-specific datasets:
- **Chest X-rays:** NIH, CheXpert, MIMIC-CXR
- **Brain MRI:** BraTS, ADNI
- **CT Scans:** LIDC-IDRI (lung nodules)
