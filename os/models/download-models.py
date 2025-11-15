#!/usr/bin/env python3
"""
Download pre-trained ONNX models for medical imaging inference
"""

import os
import sys

def download_tinybert():
    """Download pre-trained TinyBERT and export to ONNX"""
    try:
        from transformers import AutoTokenizer, AutoModel
        from optimum.onnxruntime import ORTModelForFeatureExtraction

        print("Downloading TinyBERT from Hugging Face...")
        model_name = "huawei-noah/TinyBERT_General_4L_312D"
        save_path = "bert-tiny-pretrained"

        # Download and export to ONNX
        model = ORTModelForFeatureExtraction.from_pretrained(
            model_name,
            export=True,
            provider="CPUExecutionProvider"
        )
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Save
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)

        print(f"✓ TinyBERT saved to {save_path}/")
        return True

    except ImportError as e:
        print(f"✗ Missing dependencies: {e}")
        print("Install with: pip install transformers optimum[onnxruntime]")
        return False
    except Exception as e:
        print(f"✗ Download failed: {e}")
        return False

def download_mobilenet():
    """Download pre-trained MobileNet-V2"""
    try:
        import torch
        from torchvision import models

        print("Downloading MobileNet-V2 from PyTorch Hub...")
        model = models.mobilenet_v2(pretrained=True)
        model.eval()

        # Export to ONNX
        dummy_input = torch.randn(1, 3, 224, 224)
        torch.onnx.export(
            model,
            dummy_input,
            "mobilenet-v2/mobilenet-v2-pretrained.onnx",
            input_names=['input'],
            output_names=['output'],
            dynamic_axes={'input': {0: 'batch'}, 'output': {0: 'batch'}}
        )

        print("✓ MobileNet-V2 exported to mobilenet-v2/mobilenet-v2-pretrained.onnx")
        return True

    except ImportError:
        print("✗ PyTorch not installed")
        print("Install with: pip install torch torchvision")
        return False
    except Exception as e:
        print(f"✗ Export failed: {e}")
        return False

def download_resnet18():
    """Download pre-trained ResNet-18"""
    try:
        import torch
        from torchvision import models

        print("Downloading ResNet-18 from PyTorch Hub...")
        model = models.resnet18(pretrained=True)
        model.eval()

        # Export to ONNX
        dummy_input = torch.randn(1, 3, 224, 224)
        torch.onnx.export(
            model,
            dummy_input,
            "resnet18/resnet18-pretrained.onnx",
            input_names=['input'],
            output_names=['output'],
            dynamic_axes={'input': {0: 'batch'}, 'output': {0: 'batch'}}
        )

        print("✓ ResNet-18 exported to resnet18/resnet18-pretrained.onnx")
        return True

    except ImportError:
        print("✗ PyTorch not installed")
        return False
    except Exception as e:
        print(f"✗ Export failed: {e}")
        return False

def main():
    """Download all models"""
    os.chdir(os.path.dirname(__file__))

    print("=" * 60)
    print("ONNX Model Downloader for Medical Imaging")
    print("=" * 60)
    print()

    models_to_download = {
        'tinybert': download_tinybert,
        'mobilenet': download_mobilenet,
        'resnet18': download_resnet18,
    }

    if len(sys.argv) > 1:
        # Download specific model
        model_name = sys.argv[1].lower()
        if model_name in models_to_download:
            models_to_download[model_name]()
        else:
            print(f"Unknown model: {model_name}")
            print(f"Available models: {', '.join(models_to_download.keys())}")
    else:
        # Download all models
        for name, download_func in models_to_download.items():
            print(f"\n[{name.upper()}]")
            download_func()
            print()

    print("\n" + "=" * 60)
    print("Note: Downloaded models are gitignored (models/**/*.onnx)")
    print("They exist locally and can be used for client-side inference.")
    print("=" * 60)

if __name__ == "__main__":
    main()
