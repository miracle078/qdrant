"""
Image embeddings using CLIP
Model: openai/clip-vit-large-patch14 (512 dimensions)
"""

from typing import List, Union
import logging
from PIL import Image
import io

logger = logging.getLogger(__name__)

# Lazy load models
_clip_model = None
_clip_processor = None


def _get_clip_models():
    """Lazy load CLIP model and processor"""
    global _clip_model, _clip_processor
    if _clip_model is None:
        try:
            from transformers import CLIPModel, CLIPProcessor
            _clip_model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
            _clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")
            # Set to eval mode
            _clip_model.eval()
            logger.info("CLIP model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load CLIP model: {e}")
            raise
    return _clip_model, _clip_processor


def embed_image(image: Union[str, bytes, Image.Image]) -> List[float]:
    """
    Embed image using CLIP

    Args:
        image: Image path, bytes, or PIL Image object

    Returns:
        512-dimensional embedding vector
    """
    try:
        model, processor = _get_clip_models()

        # Load image if needed
        if isinstance(image, str):
            img = Image.open(image).convert('RGB')
        elif isinstance(image, bytes):
            img = Image.open(io.BytesIO(image)).convert('RGB')
        else:
            img = image.convert('RGB')

        # Process and embed
        inputs = processor(images=img, return_tensors="pt")

        with torch.no_grad():
            image_features = model.get_image_features(**inputs)

        # Normalize
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)

        return image_features[0].cpu().numpy().tolist()

    except Exception as e:
        logger.error(f"Failed to embed image: {e}")
        return [0.0] * 512


def embed_image_from_url(url: str) -> List[float]:
    """
    Embed image from URL

    Args:
        url: Image URL

    Returns:
        512-dimensional embedding vector
    """
    try:
        import requests
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return embed_image(response.content)
    except Exception as e:
        logger.error(f"Failed to fetch and embed image from {url}: {e}")
        return [0.0] * 512
