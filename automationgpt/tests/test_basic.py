"""
Basic tests for AutomationGPT components
"""

import pytest
import asyncio
from automationgpt.qdrant_setup import QdrantManager


def test_qdrant_manager_initialization():
    """Test Qdrant manager can be initialized"""
    manager = QdrantManager(in_memory=True)
    assert manager is not None
    assert manager.in_memory is True


def test_collections_setup():
    """Test collections can be created"""
    manager = QdrantManager(in_memory=True)
    manager.setup_collections()

    stats = manager.get_collection_stats()
    assert 'isa' in stats
    assert 'code' in stats
    assert 'img' in stats
    assert 'aud' in stats
    assert 'vid' in stats
    assert 'doc' in stats


@pytest.mark.asyncio
async def test_sample_data_ingestion():
    """Test sample data can be ingested"""
    from automationgpt.ingest.sample_data import ingest_sample_data

    manager = QdrantManager(in_memory=True)
    manager.setup_collections()

    counts = await ingest_sample_data(manager)

    assert counts['isa'] > 0
    assert counts['code'] > 0
    assert counts['doc'] > 0


def test_imports():
    """Test all main modules can be imported"""
    from automationgpt import agent
    from automationgpt import auto_array
    from automationgpt import qdrant_setup
    from automationgpt.embeddings import text_embeddings
    from automationgpt.embeddings import code_embeddings

    assert agent is not None
    assert auto_array is not None
    assert qdrant_setup is not None
    assert text_embeddings is not None
    assert code_embeddings is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
