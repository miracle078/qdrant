# 🚀 AutomationGPT - Quick Start Guide

Get up and running in 5 minutes!

## 🌌 Chazon OS - Super Quick Start (30 seconds!)

**No API keys, no installation, no backend!**

```bash
# Just open in your browser:
open chazon.html

# Or visit:
https://teslasolar.github.io/qdrant/chazon.html
```

**Commands:**
```
help          - Show available commands
run hello.md  - Run Hello World
demo          - Run demo programs
ls            - List all programs
```

**That's it!** Chazon OS runs entirely client-side. See [Chazon README](chazon/README.md) for details.

---

## 🏭 AutomationGPT Classic - Full Setup

For the full multimodal search engine with API backend:

## Prerequisites

- Docker & Docker Compose
- Python 3.9+
- API Keys:
  - Anthropic Claude API key
  - OpenAI API key

## Step 1: Get API Keys

### Anthropic API Key
1. Visit https://console.anthropic.com/
2. Sign up or log in
3. Go to API Keys
4. Create new key
5. Copy the key (starts with `sk-ant-`)

### OpenAI API Key
1. Visit https://platform.openai.com/
2. Sign up or log in
3. Go to API Keys
4. Create new key
5. Copy the key (starts with `sk-`)

## Step 2: Clone Repository

```bash
git clone https://github.com/teslasolar/qdrant
cd qdrant
```

## Step 3: Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file
nano .env  # or use your favorite editor
```

Add your API keys:
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-key-here
```

## Step 4: Start Services

### Option A: Docker Compose (Recommended)

```bash
# Start Qdrant + API
docker-compose up -d

# Check logs
docker-compose logs -f
```

### Option B: Manual Setup

```bash
# Terminal 1: Start Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Terminal 2: Install dependencies and start API
pip install -r requirements.txt
uvicorn automationgpt.api.main:app --reload
```

## Step 5: Ingest Sample Data

```bash
# Install Python dependencies (if not using Docker)
pip install -r requirements.txt

# Run ingestion script
python -m automationgpt.ingest.sample_data
```

**Expected output:**
```
INFO:root:Ingesting ISA standards...
✓ Ingested 15 ISA standards
INFO:root:Ingesting PLC code samples...
✓ Ingested 3 code samples
INFO:root:Ingesting documentation...
✓ Ingested 2 documentation items

📊 Ingestion Complete:
  isa: 15 items
  code: 3 items
  doc: 2 items
  img: 0 items
  aud: 0 items
  vid: 0 items
```

## Step 6: Test the API

### Health Check

```bash
curl http://localhost:8000/health
```

**Expected response:**
```json
{
  "status": "healthy",
  "components": {
    "qdrant": "ok",
    "agent": "ok",
    "api": "ok"
  }
}
```

### Test Query

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"q":"What is ISA-95 level 3?","mode":"hybrid"}'
```

**Expected response:**
```json
{
  "answer": "ISA-95 Level 3 is the Manufacturing Execution System (MES) layer...",
  "sources": [...],
  "mode": "hybrid",
  "retrieval_time": 0.234,
  "context_count": 5
}
```

### Test Code Search

```bash
curl -X POST http://localhost:8000/search/code \
  -H "Content-Type: application/json" \
  -d '"PID controller"'
```

## Step 7: Open Frontend

### Option A: Landing Page
1. Open `index.html` - Choose between Chazon OS or AutomationGPT Classic

### Option B: Chazon OS (No API Required)
1. Open `chazon.html` in your browser
2. Type `demo` to see sample programs
3. Pure client-side, no backend needed!

### Option C: AutomationGPT Classic
1. Open `automationgpt.html` in your browser
2. Enter a query (e.g., "Explain ISA-95 level 3")
3. Click Search

**Note:** Update API_URL in automationgpt.html if not using localhost:8000

### React App (Optional)

```bash
cd frontend
npm install
npm start
```

Visit: http://localhost:3000

## Step 8: Try Some Queries!

### Text Queries
- "What is ISA-95 level 3?"
- "Explain the difference between ISA-95 and ISA-88"
- "What is alarm rationalization in ISA-18.2?"

### Code Queries
- "PID controller in structured text"
- "Interlock logic example"
- "Batch phase state machine"

### Hybrid Queries
- "ISA-95 level 2 with code examples"
- "Show me MES implementation"

## Troubleshooting

### Issue: "Qdrant connection failed"

**Solution:**
```bash
# Check if Qdrant is running
docker ps | grep qdrant

# Restart Qdrant
docker-compose restart qdrant
```

### Issue: "OpenAI API error"

**Solution:**
- Check your OPENAI_API_KEY in .env
- Ensure you have API credits
- Try: `export OPENAI_API_KEY=sk-your-key`

### Issue: "Anthropic API error"

**Solution:**
- Check your ANTHROPIC_API_KEY in .env
- Ensure you have API credits
- Try: `export ANTHROPIC_API_KEY=sk-ant-your-key`

### Issue: "Empty results"

**Solution:**
- Run ingestion again: `python -m automationgpt.ingest.sample_data`
- Check collection stats: `curl http://localhost:8000/stats`

### Issue: "Port 8000 already in use"

**Solution:**
```bash
# Change port in docker-compose.yml
ports:
  - "8001:8000"  # Use 8001 instead

# Or kill existing process
lsof -ti:8000 | xargs kill -9
```

## Next Steps

1. ✅ **Add more data:**
   - PDF standards → `automationgpt/ingest/isa_standards.py`
   - GitHub code → `automationgpt/ingest/code_samples.py`
   - YouTube audio → `automationgpt/ingest/audio_content.py`

2. ✅ **Customize:**
   - Modify system prompt in `automationgpt/agent.py`
   - Add custom collections in `automationgpt/qdrant_setup.py`
   - Adjust search parameters

3. ✅ **Deploy:**
   - See deployment guides in README.md
   - Configure for production use
   - Set up monitoring

## Quick Reference

### Start Everything
```bash
docker-compose up -d
```

### Stop Everything
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs -f api
```

### Restart API
```bash
docker-compose restart api
```

### Check Status
```bash
curl http://localhost:8000/stats
```

### Clear Data
```bash
docker-compose down -v
docker-compose up -d
python -m automationgpt.ingest.sample_data
```

## Support

- **Documentation:** See README.md
- **Issues:** https://github.com/teslasolar/qdrant/issues
- **Discussions:** GitHub Discussions

---

**Happy searching! 🔍**
