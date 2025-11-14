"""
FastAPI backend for AutomationGPT
Multimodal ISA standards search API
"""

import logging
from typing import Optional, List
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from ..agent import get_agent
from ..qdrant_setup import get_qdrant_client
from ..ingest.sample_data import ingest_sample_data

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="AutomationGPT API",
    description="Multimodal ISA Standards Search Engine",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
agent = get_agent()
qdrant = get_qdrant_client()


# Request/Response models
class QueryRequest(BaseModel):
    q: str
    mode: str = 'hybrid'
    max_context: int = 5


class SearchRequest(BaseModel):
    query: str
    k: int = 10
    filters: Optional[dict] = None


class IngestResponse(BaseModel):
    status: str
    counts: dict


# Routes
@app.get("/")
async def root():
    """API root - health check"""
    return {
        "name": "AutomationGPT API",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": [
            "/query",
            "/search/{mode}",
            "/memory",
            "/stats",
            "/ingest"
        ]
    }


@app.post("/query")
async def query(request: QueryRequest):
    """
    Main query endpoint with RAG

    Modes:
    - hybrid: Search all modalities with fusion
    - t: Text/standards only
    - c: Code only
    - i: Image/diagram only
    - a: Audio only
    """
    try:
        result = await agent.query(
            question=request.q,
            mode=request.mode,
            max_context=request.max_context
        )
        return result
    except Exception as e:
        logger.error(f"Query error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/search/{mode}")
async def search(
    mode: str,
    q: str = Query(..., description="Search query"),
    k: int = Query(10, description="Number of results")
):
    """
    Direct search without LLM

    Modes: t, c, i, a, v, d
    """
    try:
        results = await agent.array.search(q, mode=mode, k=k)
        return {
            "query": q,
            "mode": mode,
            "count": len(results),
            "results": [
                {
                    "id": r.id,
                    "score": r.score,
                    "payload": r.payload
                }
                for r in results
            ]
        }
    except Exception as e:
        logger.error(f"Search error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search/code")
async def search_code(code: str):
    """Search for similar code snippets"""
    try:
        results = await agent.array.search(code, mode='c', k=10)
        return {
            "count": len(results),
            "results": [
                {
                    "id": r.id,
                    "score": r.score,
                    "code": r.payload.get('code', ''),
                    "language": r.payload.get('lang', ''),
                    "function": r.payload.get('fn', '')
                }
                for r in results
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search/image")
async def search_image(file: UploadFile = File(...)):
    """Search for similar diagrams/images"""
    try:
        # Read uploaded image
        image_data = await file.read()

        # Search using image embedding
        results = await agent.array.search(image_data, mode='i', k=10)

        return {
            "count": len(results),
            "results": [
                {
                    "id": r.id,
                    "score": r.score,
                    "description": r.payload.get('desc', ''),
                    "type": r.payload.get('type', ''),
                    "url": r.payload.get('url', '')
                }
                for r in results
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/memory")
async def get_memory(limit: int = 10):
    """Get conversation memory"""
    return {
        "count": len(agent.memory),
        "history": agent.memory[-limit:]
    }


@app.delete("/memory")
async def clear_memory():
    """Clear conversation memory"""
    agent.clear_memory()
    return {"status": "cleared"}


@app.get("/stats")
async def get_stats():
    """Get system statistics"""
    try:
        stats = agent.get_stats()
        return stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ingest")
async def ingest():
    """Ingest sample data into Qdrant"""
    try:
        # Setup collections if needed
        qdrant.setup_collections()

        # Ingest sample data
        counts = await ingest_sample_data(qdrant)

        return IngestResponse(
            status="success",
            counts=counts
        )
    except Exception as e:
        logger.error(f"Ingestion error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Detailed health check"""
    qdrant_healthy = qdrant.health_check()

    return {
        "status": "healthy" if qdrant_healthy else "degraded",
        "components": {
            "qdrant": "ok" if qdrant_healthy else "error",
            "agent": "ok",
            "api": "ok"
        }
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    logger.info("🚀 AutomationGPT API starting...")

    # Check Qdrant health
    if qdrant.health_check():
        logger.info("✓ Qdrant connected")

        # Setup collections if needed
        try:
            qdrant.setup_collections()
            logger.info("✓ Collections ready")
        except Exception as e:
            logger.warning(f"Collection setup warning: {e}")
    else:
        logger.warning("⚠ Qdrant not available - some features disabled")

    logger.info("✓ AutomationGPT API ready!")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("AutomationGPT API shutting down...")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
