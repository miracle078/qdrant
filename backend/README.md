# Chazon OS Backend API

FastAPI service providing Qdrant vector database and embedding generation for Chazon OS.

## Features

- ✅ Qdrant vector database integration
- ✅ Cohere embeddings (recommended for hackathon)
- ✅ OpenAI embeddings (alternative)
- ✅ Collection management
- ✅ Vector search with cosine similarity
- ✅ CORS enabled for GitHub Pages

## Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env and add your API keys
```

### 3. Start Qdrant

**Option A: Docker**
```bash
docker run -p 6333:6333 qdrant/qdrant
```

**Option B: Qdrant Cloud**
- Sign up at https://cloud.qdrant.io
- Create cluster
- Add URL and API key to .env

### 4. Run API

```bash
python api.py
# Or with uvicorn:
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: http://localhost:8000

## API Endpoints

### Health Check
```bash
GET /health
```

### Create Collection
```bash
POST /collections/{name}/create?dimension=512
```

### Generate Embedding
```bash
POST /embed
{
  "text": "example text",
  "model": "cohere"  # or "openai"
}
```

### Search Vectors
```bash
POST /search
{
  "query": "search query",
  "collection": "medical_images",
  "limit": 5
}
```

### Index Document
```bash
POST /index
{
  "text": "document text",
  "collection": "medical_images",
  "metadata": {
    "title": "Example",
    "type": "medical"
  }
}
```

### List Collections
```bash
GET /collections
```

## Deployment

### Railway.app (Free Tier)

1. Create account at railway.app
2. New project → Deploy from GitHub
3. Add environment variables
4. Deploy!

### Fly.io

```bash
fly launch
fly secrets set COHERE_API_KEY=...
fly deploy
```

### Vercel (Serverless)

```bash
vercel deploy
```

## Example Usage

### Python
```python
import requests

# Generate embedding
response = requests.post('http://localhost:8000/embed', json={
    'text': 'chest x-ray with pneumonia',
    'model': 'cohere'
})
embedding = response.json()['embedding']

# Search
response = requests.post('http://localhost:8000/search', json={
    'query': 'similar chest x-ray',
    'collection': 'medical_images',
    'limit': 5
})
results = response.json()['results']
```

### JavaScript
```javascript
// From Chazon OS frontend
const response = await fetch('http://localhost:8000/search', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    query: 'chest x-ray pneumonia',
    collection: 'medical_images',
    limit: 5
  })
});

const data = await response.json();
console.log(data.results);
```

## Testing

```bash
# Health check
curl http://localhost:8000/health

# Create collection
curl -X POST http://localhost:8000/collections/test/create?dimension=1024

# Generate embedding
curl -X POST http://localhost:8000/embed \
  -H "Content-Type: application/json" \
  -d '{"text": "example", "model": "cohere"}'
```

## Production Considerations

- Add authentication (API keys, JWT)
- Rate limiting
- Caching (Redis)
- Monitoring (Prometheus, Grafana)
- Logging (structured logs)
- HTTPS (SSL certificates)

## License

MIT - Part of Chazon OS project
