# Download AI Models
**UUID:** cli-models-download-001
**ISA-95 L3: MES Layer** | Markdown Executable

Downloads AI models for inference.

## Models

- **BERT Tiny** - Text embeddings (45MB)
- **MobileNet V2** - Image classification (14MB)
- **ResNet18** - Image classification (46MB)
- **SqueezeNet** - Lightweight image classification (5MB)

```bash
#!/bin/bash
# Download AI Models

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../..\" && pwd)"

echo "📥 Downloading AI Models"
echo "========================"
echo ""

cd "$ROOT_DIR/os/models"

# Check if Python script exists
if [ -f "download-models.py" ]; then
    echo "Running model download script..."
    python3 download-models.py
else
    echo "Manual model download URLs:"
    echo ""
    echo "BERT Tiny:"
    echo "  https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased"
    echo ""
    echo "MobileNet V2:"
    echo "  https://github.com/onnx/models/tree/main/vision/classification/mobilenet"
    echo ""
    echo "ResNet18:"
    echo "  https://github.com/onnx/models/tree/main/vision/classification/resnet"
    echo ""
    echo "SqueezeNet:"
    echo "  https://github.com/onnx/models/tree/main/vision/classification/squeezenet"
    echo ""
    echo "Download and place .onnx files in respective directories"
fi

echo ""
echo "========================"
echo "✅ Model download complete"
```

## Usage

```bash
# Download all models
./cli/models/download.md

# Or run Python script directly
cd os/models
python3 download-models.py
```

## Download Locations

Models are downloaded to their respective directories:

```
os/models/
├── bert-tiny/
│   └── model.onnx
├── mobilenet-v2/
│   └── mobilenetv2-7.onnx
├── resnet18/
│   └── resnet18-v1-7.onnx
└── squeezenet/
    └── squeezenet1.1-7.onnx
```

## Model Details

### BERT Tiny (45MB)
- **Use:** Text embeddings
- **Input:** Text strings
- **Output:** 256-dimensional embeddings
- **Source:** Hugging Face
- **Quantized:** Yes

### MobileNet V2 (14MB)
- **Use:** Image classification
- **Input:** 224x224 RGB images
- **Output:** 1000 ImageNet classes
- **Source:** ONNX Model Zoo
- **Optimized:** Mobile/web deployment

### ResNet18 (46MB)
- **Use:** Image classification
- **Input:** 224x224 RGB images
- **Output:** 1000 ImageNet classes
- **Source:** ONNX Model Zoo
- **Accuracy:** Higher than MobileNet

### SqueezeNet (5MB)
- **Use:** Lightweight image classification
- **Input:** 224x224 RGB images
- **Output:** 1000 ImageNet classes
- **Source:** ONNX Model Zoo
- **Optimized:** Minimal size

## Manual Download

If automatic download fails, download manually:

### BERT Tiny
```bash
cd os/models/bert-tiny
wget https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased/resolve/main/onnx/model.onnx
```

### MobileNet V2
```bash
cd os/models/mobilenet-v2
wget https://github.com/onnx/models/raw/main/vision/classification/mobilenet/model/mobilenetv2-7.onnx
```

### ResNet18
```bash
cd os/models/resnet18
wget https://github.com/onnx/models/raw/main/vision/classification/resnet/model/resnet18-v1-7.onnx
```

### SqueezeNet
```bash
cd os/models/squeezenet
wget https://github.com/onnx/models/raw/main/vision/classification/squeezenet/model/squeezenet1.1-7.onnx
```

## Python Download Script

Create `os/models/download-models.py`:

```python
#!/usr/bin/env python3
import urllib.request
import os

MODELS = {
    'bert-tiny': {
        'url': 'https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased/resolve/main/onnx/model.onnx',
        'file': 'model.onnx'
    },
    'mobilenet-v2': {
        'url': 'https://github.com/onnx/models/raw/main/vision/classification/mobilenet/model/mobilenetv2-7.onnx',
        'file': 'mobilenetv2-7.onnx'
    },
    'resnet18': {
        'url': 'https://github.com/onnx/models/raw/main/vision/classification/resnet/model/resnet18-v1-7.onnx',
        'file': 'resnet18-v1-7.onnx'
    },
    'squeezenet': {
        'url': 'https://github.com/onnx/models/raw/main/vision/classification/squeezenet/model/squeezenet1.1-7.onnx',
        'file': 'squeezenet1.1-7.onnx'
    }
}

for model_name, model_info in MODELS.items():
    model_dir = model_name
    os.makedirs(model_dir, exist_ok=True)

    filepath = os.path.join(model_dir, model_info['file'])

    if os.path.exists(filepath):
        print(f"✅ {model_name}: Already exists")
    else:
        print(f"📥 Downloading {model_name}...")
        urllib.request.urlretrieve(model_info['url'], filepath)
        print(f"✅ {model_name}: Downloaded")
```

## Verify Downloads

After downloading, verify with:

```bash
./cli/models/list.md
```

Expected output:
```
🤖 Available AI Models
======================

📦 bert-tiny
   ✅ model.onnx (45MB)

📦 mobilenet-v2
   ✅ mobilenetv2-7.onnx (14MB)

📦 resnet18
   ✅ resnet18-v1-7.onnx (46MB)

📦 squeezenet
   ✅ squeezenet1.1-7.onnx (5.0MB)

======================
Total models: 4
```

## Storage Requirements

- **Minimum:** 110MB (all 4 models)
- **Recommended:** 500MB (models + working space)

## Network Requirements

- Stable internet connection
- ~110MB download bandwidth
- Unrestricted access to GitHub and Hugging Face

## Troubleshooting

### Download Fails

```bash
# Check internet connection
ping github.com

# Try manual download
cd os/models/bert-tiny
curl -LO https://huggingface.co/...
```

### Permission Denied

```bash
# Fix permissions
chmod 755 os/models
chmod +w os/models/*

# Or run as sudo (not recommended)
sudo ./cli/models/download.md
```

### Disk Space

```bash
# Check available space
df -h

# Clean up old models
rm -rf os/models/*/
```

## Related

- `list.md` - List downloaded models
- `/os/models/README.md` - Model documentation
- `../boot.md` - Boot system (loads models)
