"""
Audio embeddings using LAION CLAP
Model: LAION CLAP (512 dimensions)
Supports audio search for ISA educational songs!
"""

from typing import List, Union
import logging
import numpy as np

logger = logging.getLogger(__name__)

# Lazy load model
_clap_model = None


def _get_clap_model():
    """Lazy load CLAP model"""
    global _clap_model
    if _clap_model is None:
        try:
            from laion_clap import CLAP_Module
            _clap_model = CLAP_Module(enable_fusion=False)
            _clap_model.load_ckpt()
            logger.info("CLAP model loaded successfully")
        except Exception as e:
            logger.warning(f"Failed to load CLAP model (optional): {e}")
            # CLAP is optional, return None if unavailable
            return None
    return _clap_model


def embed_audio(audio_data: Union[str, np.ndarray], sample_rate: int = 48000) -> List[float]:
    """
    Embed audio using CLAP

    Args:
        audio_data: Audio file path or numpy array
        sample_rate: Sample rate (default 48kHz for CLAP)

    Returns:
        512-dimensional embedding vector
    """
    try:
        model = _get_clap_model()
        if model is None:
            logger.warning("CLAP model not available, returning zero vector")
            return [0.0] * 512

        if isinstance(audio_data, str):
            # Load from file
            embedding = model.get_audio_embedding_from_filelist(
                x=[audio_data],
                use_tensor=False
            )
        else:
            # Use numpy array
            embedding = model.get_audio_embedding_from_data(
                x=audio_data,
                use_tensor=False
            )

        return embedding[0].tolist()

    except Exception as e:
        logger.error(f"Failed to embed audio: {e}")
        return [0.0] * 512


def embed_audio_text(text: str) -> List[float]:
    """
    Embed text description of audio (for text-to-audio search)

    Args:
        text: Text description

    Returns:
        512-dimensional embedding vector
    """
    try:
        model = _get_clap_model()
        if model is None:
            return [0.0] * 512

        embedding = model.get_text_embedding([text], use_tensor=False)
        return embedding[0].tolist()

    except Exception as e:
        logger.error(f"Failed to embed audio text: {e}")
        return [0.0] * 512
