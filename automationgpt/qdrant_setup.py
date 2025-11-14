"""
Qdrant database setup and collection management
Creates 6 collections: isa, code, img, aud, vid, doc
"""

import os
import logging
from typing import Optional
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    CollectionInfo,
    OptimizersConfigDiff,
    HnswConfigDiff
)

logger = logging.getLogger(__name__)

# Collection configurations
COLLECTIONS = {
    'isa': {
        'size': 1536,
        'description': 'ISA Standards (95/88/18.2)',
        'payload_schema': ['txt', 'std', 'sec', 'lvl', 'diff']
    },
    'code': {
        'size': 768,
        'description': 'PLC Code (Ladder, ST, SCL)',
        'payload_schema': ['code', 'lang', 'plat', 'isa_pat', 'fn']
    },
    'img': {
        'size': 512,
        'description': 'Diagrams (P&ID, HMI, Loop)',
        'payload_schema': ['url', 'desc', 'type', 'comp', 'lvl']
    },
    'aud': {
        'size': 512,
        'description': 'ISA Songs (Educational)',
        'payload_schema': ['yt', 'title', 'lyr', 'cpt', 'ts']
    },
    'vid': {
        'size': 512,
        'description': 'Training Videos',
        'payload_schema': ['url', 'trans', 'frame', 'topic', 'ts']
    },
    'doc': {
        'size': 1536,
        'description': 'Documentation (Tutorials, FAQ)',
        'payload_schema': ['txt', 'type', 'std', 'skill', 'use']
    }
}


class QdrantManager:
    """Manages Qdrant client and collections"""

    def __init__(self, url: Optional[str] = None, api_key: Optional[str] = None,
                 in_memory: bool = False):
        """
        Initialize Qdrant client

        Args:
            url: Qdrant server URL (default: localhost:6333)
            api_key: API key for Qdrant Cloud
            in_memory: Use in-memory mode for testing
        """
        self.in_memory = in_memory

        if in_memory:
            self.client = QdrantClient(":memory:")
            logger.info("Initialized in-memory Qdrant client")
        else:
            # Try environment variables first
            url = url or os.getenv("QDRANT_URL", "http://localhost:6333")
            api_key = api_key or os.getenv("QDRANT_API_KEY")

            if api_key:
                self.client = QdrantClient(url=url, api_key=api_key)
                logger.info(f"Initialized Qdrant Cloud client: {url}")
            else:
                self.client = QdrantClient(url=url)
                logger.info(f"Initialized Qdrant local client: {url}")

    def setup_collections(self, force_recreate: bool = False):
        """
        Create all collections if they don't exist

        Args:
            force_recreate: Delete and recreate collections
        """
        for name, config in COLLECTIONS.items():
            try:
                # Check if collection exists
                exists = False
                try:
                    self.client.get_collection(name)
                    exists = True
                except Exception:
                    pass

                if exists and force_recreate:
                    logger.info(f"Deleting existing collection: {name}")
                    self.client.delete_collection(name)
                    exists = False

                if not exists:
                    logger.info(f"Creating collection: {name} ({config['description']})")
                    self.client.create_collection(
                        collection_name=name,
                        vectors_config=VectorParams(
                            size=config['size'],
                            distance=Distance.COSINE
                        ),
                        # Optimize for CPU
                        optimizers_config=OptimizersConfigDiff(
                            indexing_threshold=10000,  # Higher threshold for batch indexing
                        ),
                        hnsw_config=HnswConfigDiff(
                            m=16,  # Lower m for CPU
                            ef_construct=100,
                            on_disk=not self.in_memory  # Use disk for large collections
                        )
                    )
                    logger.info(f"✓ Created: {name}")
                else:
                    logger.info(f"✓ Exists: {name}")

            except Exception as e:
                logger.error(f"Failed to create collection {name}: {e}")
                raise

    def get_collection_stats(self) -> dict:
        """Get statistics for all collections"""
        stats = {}
        for name in COLLECTIONS.keys():
            try:
                info = self.client.get_collection(name)
                stats[name] = {
                    'count': info.points_count,
                    'vectors': info.vectors_count,
                    'status': info.status
                }
            except Exception as e:
                stats[name] = {'error': str(e)}
        return stats

    def create_payload_indexes(self):
        """Create indexes on frequently queried payload fields"""
        indexes = {
            'isa': ['std', 'lvl', 'diff'],
            'code': ['lang', 'plat', 'isa_pat'],
            'img': ['type', 'lvl'],
            'aud': ['yt', 'title'],
            'vid': ['topic'],
            'doc': ['type', 'std', 'skill']
        }

        for collection, fields in indexes.items():
            for field in fields:
                try:
                    self.client.create_payload_index(
                        collection_name=collection,
                        field_name=field,
                        field_schema="keyword"
                    )
                    logger.info(f"Created index on {collection}.{field}")
                except Exception as e:
                    logger.warning(f"Could not create index {collection}.{field}: {e}")

    def health_check(self) -> bool:
        """Check if Qdrant is healthy"""
        try:
            # Try to list collections
            collections = self.client.get_collections()
            logger.info(f"Qdrant health check OK - {len(collections.collections)} collections")
            return True
        except Exception as e:
            logger.error(f"Qdrant health check failed: {e}")
            return False


def get_qdrant_client(url: Optional[str] = None, api_key: Optional[str] = None,
                      in_memory: bool = False) -> QdrantManager:
    """
    Get configured Qdrant client

    Args:
        url: Qdrant URL
        api_key: API key
        in_memory: Use in-memory mode

    Returns:
        QdrantManager instance
    """
    return QdrantManager(url=url, api_key=api_key, in_memory=in_memory)


if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(level=logging.INFO)

    # Initialize and setup collections
    manager = get_qdrant_client()

    if manager.health_check():
        manager.setup_collections()
        manager.create_payload_indexes()
        print("\n📊 Collection Stats:")
        for name, stats in manager.get_collection_stats().items():
            print(f"  {name}: {stats}")
    else:
        print("❌ Qdrant not available. Please start Qdrant server.")
        print("   docker run -p 6333:6333 qdrant/qdrant")
