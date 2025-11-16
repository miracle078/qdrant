#!/bin/bash
# Download AI Models

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

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
