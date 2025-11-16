#!/bin/bash
# List available AI models

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

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
