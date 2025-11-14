"""
AutoArray - Sparse FemtoLLM array with multimodal search
Combines Qdrant vector search with hybrid fusion
"""

import asyncio
import logging
from typing import List, Dict, Any, Optional
from qdrant_client.models import Filter, FieldCondition, MatchValue

from .qdrant_setup import get_qdrant_client, QdrantManager
from .embeddings import (
    embed_text,
    embed_code,
    embed_image,
    embed_audio
)

logger = logging.getLogger(__name__)


class FemtoLLM:
    """
    Tiny 16d LLM for sparse processing
    Mock implementation - expand as needed
    """

    def __init__(self, hidden_size: int = 16):
        import numpy as np
        self.W = np.random.randn(hidden_size, hidden_size) * 0.1
        logger.debug(f"Initialized FemtoLLM with {hidden_size}d")

    async def process(self, text: str) -> str:
        """Process text through micro-LLM"""
        # Mock implementation
        return f"[Processed: {text[:50]}...]"


class AutoArray:
    """
    Sparse array of FemtoLLMs with multimodal Qdrant search
    """

    def __init__(self, qdrant: Optional[QdrantManager] = None):
        """
        Initialize AutoArray

        Args:
            qdrant: QdrantManager instance (creates new if None)
        """
        self.qdrant = qdrant or get_qdrant_client()
        self.femto_array = {}  # Sparse: (x,y,z) -> FemtoLLM

        # Lazy embedders (loaded on first use)
        self.embedders = {
            't': None,  # text
            'c': None,  # code
            'i': None,  # image
            'a': None,  # audio
            'v': None,  # video
        }

        logger.info("AutoArray initialized")

    def spawn_femto(self, x: int, y: int, z: int) -> FemtoLLM:
        """
        Spawn FemtoLLM at sparse coordinates

        Args:
            x, y, z: 3D coordinates in sparse array

        Returns:
            FemtoLLM instance
        """
        coord = (x, y, z)
        if coord not in self.femto_array:
            self.femto_array[coord] = FemtoLLM()
            logger.debug(f"Spawned FemtoLLM at {coord}")
        return self.femto_array[coord]

    async def search(
        self,
        query: str,
        mode: str = 't',
        k: int = 10,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Any]:
        """
        Search in specific modality

        Args:
            query: Query string or data
            mode: Modality - t(text), c(code), i(image), a(audio), v(video)
            k: Number of results
            filters: Qdrant filters

        Returns:
            Search results
        """
        # Get collection name
        collection_map = {
            't': 'isa',
            'c': 'code',
            'i': 'img',
            'a': 'aud',
            'v': 'vid',
            'd': 'doc'
        }
        collection = collection_map.get(mode, 'isa')

        # Get embedding
        embedding = await self._get_embedding(query, mode)

        # Build filter
        qdrant_filter = None
        if filters:
            conditions = []
            for key, value in filters.items():
                conditions.append(
                    FieldCondition(key=key, match=MatchValue(value=value))
                )
            if conditions:
                qdrant_filter = Filter(must=conditions)

        # Search
        try:
            results = self.qdrant.client.search(
                collection_name=collection,
                query_vector=embedding,
                limit=k,
                query_filter=qdrant_filter
            )
            logger.debug(f"Search [{mode}] returned {len(results)} results")
            return results
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

    async def hybrid_search(
        self,
        query: str,
        k_per_mode: int = 5,
        modes: List[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Multimodal hybrid search with Reciprocal Rank Fusion

        Args:
            query: Query string
            k_per_mode: Results per modality
            modes: Modalities to search (default: all)

        Returns:
            Fused results with scores
        """
        modes = modes or ['t', 'c', 'i', 'a']

        # Search all modalities in parallel
        tasks = [self.search(query, mode, k_per_mode) for mode in modes]
        results = await asyncio.gather(*tasks)

        # Reciprocal Rank Fusion
        fused = self._reciprocal_rank_fusion(results, k=60)

        logger.info(f"Hybrid search: {len(fused)} fused results")
        return fused

    def _reciprocal_rank_fusion(
        self,
        result_sets: List[List[Any]],
        k: int = 60
    ) -> List[Dict[str, Any]]:
        """
        Combine multiple result sets using RRF

        Args:
            result_sets: List of search results from different modalities
            k: RRF constant (default 60)

        Returns:
            Fused and ranked results
        """
        scores = {}
        point_data = {}

        for result_set in result_sets:
            for rank, hit in enumerate(result_set):
                point_id = hit.id
                score = 1 / (k + rank + 1)

                if point_id not in scores:
                    scores[point_id] = 0
                    point_data[point_id] = hit

                scores[point_id] += score

        # Sort by fused score
        sorted_ids = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)

        # Build result list
        fused_results = []
        for point_id in sorted_ids[:10]:
            hit = point_data[point_id]
            fused_results.append({
                'id': point_id,
                'score': scores[point_id],
                'payload': hit.payload,
                'original_score': hit.score
            })

        return fused_results

    async def _get_embedding(self, query: Any, mode: str) -> List[float]:
        """Get embedding for query based on modality"""
        if mode == 't' or mode == 'd':
            return await embed_text(query)
        elif mode == 'c':
            return embed_code(query)
        elif mode == 'i':
            return embed_image(query)
        elif mode == 'a':
            return embed_audio(query)
        elif mode == 'v':
            # Video uses same as image for now
            return embed_image(query)
        else:
            raise ValueError(f"Unknown mode: {mode}")


# Singleton instance
_auto_array = None


def get_auto_array() -> AutoArray:
    """Get or create AutoArray singleton"""
    global _auto_array
    if _auto_array is None:
        _auto_array = AutoArray()
    return _auto_array
