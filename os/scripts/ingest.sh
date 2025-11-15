#!/bin/bash
# AutomationGPT Data Ingestion Script

set -e

echo "🏭 AutomationGPT Data Ingestion"
echo "==============================="
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Check if Qdrant is running
echo "Checking Qdrant connection..."
if ! curl -s http://localhost:6333 > /dev/null; then
    echo "❌ Qdrant is not running. Starting with Docker..."
    docker-compose up -d qdrant
    echo "Waiting for Qdrant to start..."
    sleep 5
fi
echo "✓ Qdrant is running"

echo ""
echo "Ingesting sample data..."
python -m automationgpt.ingest.sample_data

echo ""
echo "✅ Ingestion complete!"
echo ""
echo "📊 Collection stats:"
curl -s http://localhost:8000/stats | python -m json.tool

echo ""
