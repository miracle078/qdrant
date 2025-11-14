"""
Text embeddings using OpenAI API
Model: text-embedding-3-large (1536 dimensions)
"""

import os
from typing import List, Union
import asyncio
from functools import lru_cache
import logging

logger = logging.getLogger(__name__)

# Lazy import to avoid loading if not needed
_openai_client = None


def _get_openai_client():
    """Lazy load OpenAI client"""
    global _openai_client
    if _openai_client is None:
        try:
            from openai import AsyncOpenAI
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY environment variable not set")
            _openai_client = AsyncOpenAI(api_key=api_key)
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise
    return _openai_client


async def embed_text(text: str) -> List[float]:
    """
    Embed text using OpenAI's text-embedding-3-large model

    Args:
        text: Text to embed

    Returns:
        1536-dimensional embedding vector
    """
    try:
        client = _get_openai_client()
        response = await client.embeddings.create(
            input=text,
            model="text-embedding-3-large"
        )
        return response.data[0].embedding
    except Exception as e:
        logger.error(f"Failed to embed text: {e}")
        # Return zero vector as fallback
        return [0.0] * 1536


async def embed_text_batch(texts: List[str], batch_size: int = 100) -> List[List[float]]:
    """
    Embed multiple texts in batches

    Args:
        texts: List of texts to embed
        batch_size: Maximum batch size (OpenAI limit is 2048)

    Returns:
        List of embedding vectors
    """
    embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        batch_embeddings = await asyncio.gather(*[embed_text(text) for text in batch])
        embeddings.extend(batch_embeddings)

    return embeddings


@lru_cache(maxsize=1000)
def embed_text_cached(text: str) -> List[float]:
    """
    Cached version of embed_text for frequently accessed texts
    Note: This is synchronous, wraps async call
    """
    return asyncio.run(embed_text(text))
