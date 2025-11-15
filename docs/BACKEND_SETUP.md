# 🔌 Backend Setup Guide

**Real Qdrant + Embeddings Integration**

Complete guide to setting up the backend API for real vector search.

---

## Quick Start (5 Minutes)

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Get API Keys

**Cohere (Recommended for Hackathon)**
- Visit: https://cohere.com
- Sign up (free tier available)
- Get API key from dashboard
- Cohere is a hackathon sponsor! ✨

**Or OpenAI (Alternative)**
- Visit: https://platform.openai.com
- Create account
- Get API key
- $5 free credit for new accounts

### 3. Configure Environment

```bash
cd backend
cp .env.example .env

# Edit .env:
COHERE_API_KEY=your_key_here
QDRANT_URL=http://localhost:6333
```

### 4. Start Qdrant

**Option A: Docker (Easiest)**
```bash
docker run -p 6333:6333 qdrant/qdrant
```

**Option B: Docker Compose**
```bash
cd backend
docker-compose up -d
```

**Option C: Qdrant Cloud (Production)**
- Sign up: https://cloud.qdrant.io
- Create free cluster
- Copy URL and API key to .env

### 5. Start Backend API

```bash
cd backend
python api.py

# Or with uvicorn:
uvicorn api:app --reload
```

API runs at: **http://localhost:8000**

### 6. Test It!

```bash
# Health check
curl http://localhost:8000/health

# Should return:
# {"status":"healthy","qdrant":"ok","collections":0}
```

---

## Testing the Integration

### From Chazon OS Terminal

```bash
# Open chazon.html in browser

# Run real Qdrant demo:
run qdrant-real-demo.md
```

**Expected Output:**
```
🔌 Real Qdrant Integration Demo

1️⃣ Checking backend connection...
   Status: healthy
   Qdrant: ok
   Collections: 0

2️⃣ Creating collection...
   ✓ Collection: medical_images
   Dimension: 512

3️⃣ Generating embeddings with Cohere...
   ✓ "chest x-ray showing pneumonia"
     Dim: 1024, Model: cohere

4️⃣ Indexing medical cases...
   ✓ Indexed: a3f2b1c... (Pneumonia)

5️⃣ Searching for similar cases...
   Query: "chest x-ray with lung infection"
   Found: 3 results

   1. Score: 0.876
      Diagnosis: Pneumonia
      Body Part: CHEST
```

---

## Deployment Options

### Railway.app (Recommended)

**Free Tier:** 500 hours/month

```bash
# 1. Create Railway account: railway.app
# 2. Install CLI
npm i -g @railway/cli

# 3. Login
railway login

# 4. Initialize
cd backend
railway init

# 5. Add environment variables
railway variables set COHERE_API_KEY=your_key
railway variables set QDRANT_URL=your_qdrant_url

# 6. Deploy
railway up
```

**Railway URL:** `https://your-app.up.railway.app`

### Fly.io

**Free Tier:** 3 VMs

```bash
# 1. Install CLI
curl -L https://fly.io/install.sh | sh

# 2. Login
fly auth login

# 3. Launch
cd backend
fly launch

# 4. Set secrets
fly secrets set COHERE_API_KEY=your_key
fly secrets set QDRANT_URL=your_url

# 5. Deploy
fly deploy
```

**Fly URL:** `https://your-app.fly.dev`

### Vercel (Serverless)

**Free Tier:** Unlimited requests

```bash
# 1. Install CLI
npm i -g vercel

# 2. Login
vercel login

# 3. Deploy
cd backend
vercel

# 4. Add environment variables in Vercel dashboard
```

**Vercel URL:** `https://your-app.vercel.app`

---

## Connecting Frontend to Deployed Backend

### Update Chazon OS Config

Edit `chazon/medical/qdrant-client.md`:

```javascript
const QdrantClient = {
  // Change this to your deployed URL:
  baseURL: 'https://your-app.railway.app',  // or fly.dev, vercel.app
  // ...
};
```

Or configure at runtime:

```javascript
// In terminal or program:
QdrantClient.configure('https://your-app.railway.app');
```

---

## Architecture

```
┌─────────────────────────────────────────┐
│   Chazon OS (GitHub Pages)              │
│   - Browser-based frontend              │
│   - QdrantClient.js                     │
└──────────────┬──────────────────────────┘
               │ HTTPS
               ▼
┌─────────────────────────────────────────┐
│   Backend API (Railway/Fly/Vercel)      │
│   - FastAPI service                     │
│   - CORS enabled                        │
│   - api.py                              │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
┌─────────────┐  ┌──────────────┐
│   Qdrant    │  │   Cohere     │
│   Vector DB │  │   Embeddings │
│   (Cloud)   │  │   API        │
└─────────────┘  └──────────────┘
```

---

## Cost Estimates

### Free Tier Options

**Qdrant Cloud:**
- Free: 1GB storage
- ~50,000 vectors (512D)

**Cohere:**
- Free: 100 API calls/min
- Perfect for demo/testing

**Railway:**
- Free: 500 hours/month
- Enough for hackathon

**Fly.io:**
- Free: 3 VMs
- Always-on option

**Total Cost: $0** (using free tiers!)

### Paid Options (Production)

**Qdrant Cloud:**
- $25/month - 8GB RAM, 2vCPU
- Millions of vectors

**Cohere:**
- $0.0001 per embedding
- $10 = 100,000 embeddings

**Railway:**
- $5/month for usage

**Total: ~$40/month** for production

---

## Troubleshooting

### Backend Won't Start

**Error:** `ModuleNotFoundError: No module named 'qdrant_client'`

**Fix:**
```bash
pip install -r requirements.txt
```

### Qdrant Connection Failed

**Error:** `Connection refused on localhost:6333`

**Fix:**
```bash
# Start Qdrant:
docker run -p 6333:6333 qdrant/qdrant
```

### Cohere API Error

**Error:** `Invalid API key`

**Fix:**
1. Check .env file has correct key
2. Restart backend after changing .env
3. Verify key at cohere.com dashboard

### CORS Error in Browser

**Error:** `Access-Control-Allow-Origin`

**Fix:**
- Backend has CORS enabled by default
- If still blocked, check backend logs
- Ensure HTTPS for production

---

## Security Best Practices

### Environment Variables

**Never commit:**
- `.env` file
- API keys
- Qdrant credentials

**Always use:**
- `.env.example` as template
- Environment variables in production
- Secrets management (Railway/Fly)

### API Authentication

For production, add API key authentication:

```python
# api.py
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

@app.get("/search", dependencies=[Depends(verify_api_key)])
async def search_vectors(...):
    # ...
```

### Rate Limiting

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.get("/search")
@limiter.limit("10/minute")
async def search_vectors(...):
    # ...
```

---

## Monitoring

### Logs

**Railway:**
```bash
railway logs
```

**Fly.io:**
```bash
fly logs
```

**Local:**
```bash
# Backend logs to stdout
python api.py
```

### Metrics

Add basic metrics:

```python
import time
from collections import defaultdict

metrics = defaultdict(int)

@app.middleware("http")
async def track_requests(request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    metrics['requests'] += 1
    metrics['duration_sum'] += duration

    return response

@app.get("/metrics")
async def get_metrics():
    return {
        "requests": metrics['requests'],
        "avg_duration": metrics['duration_sum'] / max(metrics['requests'], 1)
    }
```

---

## Next Steps

1. ✅ Start backend locally
2. ✅ Test with qdrant-real-demo.md
3. ✅ Deploy to Railway/Fly
4. ✅ Update frontend config
5. ✅ Test from GitHub Pages
6. ✅ Monitor and optimize

**Ready for hackathon submission!** 🚀

---

## Support

**Issues:** https://github.com/teslasolar/qdrant/issues

**Documentation:**
- Qdrant: https://qdrant.tech/documentation/
- Cohere: https://docs.cohere.com/
- FastAPI: https://fastapi.tiangolo.com/
