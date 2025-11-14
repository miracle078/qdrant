"""
Code embeddings using CodeBERT
Model: microsoft/codebert-base (768 dimensions)
CPU-optimized with FP16 quantization
"""

from typing import List
import logging
import torch

logger = logging.getLogger(__name__)

# Lazy load model
_code_model = None


def _get_code_model():
    """Lazy load CodeBERT model"""
    global _code_model
    if _code_model is None:
        try:
            from sentence_transformers import SentenceTransformer
            _code_model = SentenceTransformer('microsoft/codebert-base')
            # Use FP16 for 50% memory reduction on CPU
            _code_model.half()
            logger.info("CodeBERT model loaded successfully (FP16 mode)")
        except Exception as e:
            logger.error(f"Failed to load CodeBERT model: {e}")
            raise
    return _code_model


def embed_code(code: str) -> List[float]:
    """
    Embed code snippet using CodeBERT

    Args:
        code: Source code to embed (any language)

    Returns:
        768-dimensional embedding vector
    """
    try:
        model = _get_code_model()
        embedding = model.encode(code, convert_to_numpy=True)
        return embedding.tolist()
    except Exception as e:
        logger.error(f"Failed to embed code: {e}")
        return [0.0] * 768


def embed_code_batch(codes: List[str], batch_size: int = 32) -> List[List[float]]:
    """
    Embed multiple code snippets in batches

    Args:
        codes: List of code snippets
        batch_size: Batch size for processing

    Returns:
        List of embedding vectors
    """
    try:
        model = _get_code_model()
        embeddings = model.encode(
            codes,
            batch_size=batch_size,
            show_progress_bar=False,
            convert_to_numpy=True
        )
        return embeddings.tolist()
    except Exception as e:
        logger.error(f"Failed to embed code batch: {e}")
        return [[0.0] * 768] * len(codes)
