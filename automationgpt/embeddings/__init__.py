"""
Embedding utilities for multimodal content
Supports: Text, Code, Images, Audio
All CPU-based, no GPU required!
"""

from .text_embeddings import embed_text, embed_text_batch
from .code_embeddings import embed_code, embed_code_batch
from .image_embeddings import embed_image
from .audio_embeddings import embed_audio

__all__ = [
    'embed_text',
    'embed_text_batch',
    'embed_code',
    'embed_code_batch',
    'embed_image',
    'embed_audio'
]
