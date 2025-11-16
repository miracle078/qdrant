# List AI Models
**UUID:** cli-models-list-001
**ISA-95 L3: MES Layer** | Markdown Executable

Lists all available AI models and their sizes.

```bash
#!/bin/bash
# List available AI models

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../..\" && pwd)"

echo "🤖 Available AI Models"
echo "======================"
echo ""

cd "$ROOT_DIR/os/models"

for dir in */; do
    if [ -d "$dir" ]; then
        dir_name=$(basename "$dir")
        echo "📦 $dir_name"

        # Check for ONNX models
        onnx_files=$(find "$dir" -name "*.onnx" 2>/dev/null)
        if [ -n "$onnx_files" ]; then
            echo "$onnx_files" | while read -r file; do
                size=$(du -h "$file" | cut -f1)
                echo "   ✅ $(basename "$file") ($size)"
            done
        else
            echo "   ⚠️  No ONNX files found"
        fi
        echo ""
    fi
done

echo "======================"
total=$(find . -name "*.onnx" 2>/dev/null | wc -l)
echo "Total models: $total"
```

## Usage

```bash
# List all models
./cli/models/list.md
```

## Example Output

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

## Model Information

### BERT Tiny (45MB)
- **Path:** `os/models/bert-tiny/model.onnx`
- **Type:** Text embedding
- **Dimensions:** 256
- **Use Case:** Semantic search, text similarity

### MobileNet V2 (14MB)
- **Path:** `os/models/mobilenet-v2/mobilenetv2-7.onnx`
- **Type:** Image classification
- **Classes:** 1000 (ImageNet)
- **Use Case:** Object recognition, mobile deployment

### ResNet18 (46MB)
- **Path:** `os/models/resnet18/resnet18-v1-7.onnx`
- **Type:** Image classification
- **Classes:** 1000 (ImageNet)
- **Use Case:** High-accuracy image recognition

### SqueezeNet (5MB)
- **Path:** `os/models/squeezenet/squeezenet1.1-7.onnx`
- **Type:** Image classification
- **Classes:** 1000 (ImageNet)
- **Use Case:** Lightweight deployment, embedded systems

## Advanced Usage

### List with Full Paths

```bash
cd os/models
find . -name "*.onnx" -type f
```

### Sort by Size

```bash
cd os/models
find . -name "*.onnx" -exec du -h {} + | sort -h
```

### Check Model Metadata

```bash
# Install onnx package
pip install onnx

# View model info
python3 -c "
import onnx
model = onnx.load('os/models/bert-tiny/model.onnx')
print(onnx.helper.printable_graph(model.graph))
"
```

## Model Status Indicators

- ✅ **Model found** - ONNX file exists and is readable
- ⚠️ **No ONNX files found** - Directory exists but no .onnx files
- (Missing from output) - Model directory doesn't exist

## Download Missing Models

If you see ⚠️ warnings:

```bash
# Download all models
./cli/models/download.md

# Or download specific model
cd os/models/bert-tiny
wget https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased/resolve/main/onnx/model.onnx
```

## Integration with ONNX Runtime

Models are loaded via ONNX Runtime in the browser:

```javascript
// Load BERT model
const session = await ort.InferenceSession.create(
  'os/models/bert-tiny/model.onnx',
  { executionProviders: ['webgpu', 'wasm'] }
);

// Run inference
const results = await session.run({
  input_ids: inputTensor
});
```

## Storage Usage

```bash
# Check total model storage
du -sh os/models/

# Check per-model storage
du -sh os/models/*/
```

## Cleanup

```bash
# Remove specific model
rm -rf os/models/bert-tiny/

# Remove all models (keep directories)
find os/models -name "*.onnx" -delete

# Redownload
./cli/models/download.md
```

## Model Registry

Models are registered in the boot sequence (Phase 1):

```bash
./cli/boot.md
# Output shows:
# 🤖 Phase 1: AI Models
#   ✅ Found 4 ONNX models
#   ✅ WebGPU backend initialized
```

## Troubleshooting

### No Models Found

```bash
# Download models
./cli/models/download.md

# Verify download
./cli/models/list.md
```

### Wrong Model Count

```bash
# Count manually
find os/models -name "*.onnx" | wc -l

# Check for hidden files
ls -la os/models/*/
```

### Permission Issues

```bash
# Fix permissions
chmod -R 755 os/models
chmod 644 os/models/**/*.onnx
```

## Related

- `download.md` - Download models
- `../boot.md` - Boot system (loads models)
- `/os/models/README.md` - Model documentation
- `/os/backend/api.py` - Model inference API
