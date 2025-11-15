"""
Chazon OS Backend API
FastAPI service for Qdrant and embeddings
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

# Qdrant client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Embeddings (choose one)
try:
    import cohere
    COHERE_AVAILABLE = True
except ImportError:
    COHERE_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

load_dotenv()

app = FastAPI(title="Chazon OS API", version="1.0.0")

# CORS for GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize clients
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL", "http://localhost:6333"),
    api_key=os.getenv("QDRANT_API_KEY")
)

if COHERE_AVAILABLE:
    cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

if OPENAI_AVAILABLE:
    openai.api_key = os.getenv("OPENAI_API_KEY")


# Models
class SearchRequest(BaseModel):
    query: str
    collection: str = "medical_images"
    limit: int = 5

class IndexRequest(BaseModel):
    text: str
    collection: str
    metadata: dict

class EmbedRequest(BaseModel):
    text: str
    model: str = "cohere"  # or "openai"


# Endpoints

@app.get("/")
async def root():
    return {
        "name": "Chazon OS API",
        "version": "1.0.0",
        "qdrant": "connected",
        "cohere": COHERE_AVAILABLE,
        "openai": OPENAI_AVAILABLE
    }

@app.get("/health")
async def health():
    try:
        collections = qdrant.get_collections()
        return {
            "status": "healthy",
            "qdrant": "ok",
            "collections": len(collections.collections)
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }

@app.post("/collections/{name}/create")
async def create_collection(name: str, dimension: int = 512):
    """Create a Qdrant collection"""
    try:
        qdrant.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=dimension, distance=Distance.COSINE)
        )
        return {"collection": name, "dimension": dimension, "created": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/embed")
async def generate_embedding(request: EmbedRequest):
    """Generate text embedding"""
    try:
        if request.model == "cohere" and COHERE_AVAILABLE:
            response = cohere_client.embed(
                texts=[request.text],
                model="embed-english-v3.0"
            )
            return {
                "embedding": response.embeddings[0],
                "dimension": len(response.embeddings[0]),
                "model": "cohere"
            }

        elif request.model == "openai" and OPENAI_AVAILABLE:
            response = openai.Embedding.create(
                input=request.text,
                model="text-embedding-3-large"
            )
            return {
                "embedding": response['data'][0]['embedding'],
                "dimension": len(response['data'][0]['embedding']),
                "model": "openai"
            }

        else:
            raise HTTPException(status_code=400, detail="Model not available")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search_vectors(request: SearchRequest):
    """Search Qdrant collection"""
    try:
        # Generate embedding for query
        if COHERE_AVAILABLE:
            embed_response = cohere_client.embed(
                texts=[request.query],
                model="embed-english-v3.0"
            )
            query_vector = embed_response.embeddings[0]
        else:
            raise HTTPException(status_code=400, detail="No embedding model available")

        # Search Qdrant
        results = qdrant.search(
            collection_name=request.collection,
            query_vector=query_vector,
            limit=request.limit
        )

        return {
            "results": [
                {
                    "id": hit.id,
                    "score": hit.score,
                    "payload": hit.payload
                }
                for hit in results
            ],
            "count": len(results)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/index")
async def index_document(request: IndexRequest):
    """Index document in Qdrant"""
    try:
        # Generate embedding
        if COHERE_AVAILABLE:
            embed_response = cohere_client.embed(
                texts=[request.text],
                model="embed-english-v3.0"
            )
            vector = embed_response.embeddings[0]
        else:
            raise HTTPException(status_code=400, detail="No embedding model available")

        # Generate UUID
        import uuid
        point_id = str(uuid.uuid4())

        # Upsert to Qdrant
        qdrant.upsert(
            collection_name=request.collection,
            points=[
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload=request.metadata
                )
            ]
        )

        return {
            "id": point_id,
            "indexed": True,
            "collection": request.collection
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/collections")
async def list_collections():
    """List all Qdrant collections"""
    try:
        collections = qdrant.get_collections()
        return {
            "collections": [
                {
                    "name": col.name,
                    "vectors_count": qdrant.count(col.name).count
                }
                for col in collections.collections
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
