# 🌌 Chazon - חזון
**Open Source AI Medical Imaging Analyzer**

Chazon (חזון - "Vision") is an open source AI-powered medical imaging analyzer for X-ray, MRI, and CT scans. Built for the [lablab.ai Qdrant Challenge](https://lablab.ai).

![Status](https://img.shields.io/badge/status-production-success)
![License](https://img.shields.io/badge/license-MIT-blue)
![Challenge](https://img.shields.io/badge/lablab.ai-qdrant-purple)

---

## 🎯 What is Chazon?

**Chazon** is a complete medical imaging analysis platform that helps radiologists and medical professionals:

- 📊 **Analyze X-rays** - Detect abnormalities in chest X-rays, bone fractures, etc.
- 🧠 **Process MRI scans** - Multi-sequence viewing (T1, T2, FLAIR, DWI)
- 🔬 **Review CT scans** - Multi-planar reconstruction with Hounsfield unit measurements
- 🔍 **Semantic Search** - Find similar cases using Qdrant vector database
- 🤖 **AI Analysis** - Automated findings detection and diagnosis assistance

### ✨ Live Demo

**Try it now:** Open [`frontend/index.html`](frontend/index.html) in your browser

No installation required! Runs entirely client-side with optional backend for advanced features.

---

## 🏥 Features

### Multi-Modality Support
- **X-Ray (XR)** - 2D radiography with bone/soft tissue enhancement
- **CT Scan** - 3D computed tomography with MPR (multi-planar reconstruction)
- **MRI** - Magnetic resonance with T1, T2, FLAIR, DWI sequences
- **Ultrasound (US)** - Real-time sonography
- **PET Scan** - Metabolic imaging
- **Mammography** - Breast cancer screening

### DICOM Compliant
- Full DICOM standard support
- Window/level presets (bone, lung, brain, liver, soft tissue)
- Multi-planar reconstruction
- Volumetric measurements
- HIPAA compliant architecture

### AI-Powered Analysis
- **Semantic Search** - Find similar medical cases using Qdrant
- **Abnormality Detection** - AI-powered findings identification
- **Diagnosis Assistance** - Confidence scores and recommendations
- **Report Generation** - Automated radiology reports

### Modular Architecture
- **100+ markdown modules** - Every component < 250 tokens
- **No backend required** - Client-side execution option
- **Template System** - Easy customization for different modalities
- **SNT Language** - Space-Time Notation for advanced computation

---

## 🚀 Quick Start

### Option 1: Client-Side Only (No Installation)

```bash
# Clone the repo
git clone https://github.com/teslasolar/qdrant
cd qdrant

# Open in browser
open frontend/index.html
# Or just double-click frontend/index.html
```

### Option 2: Full Stack with Qdrant

```bash
# 1. Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Setup environment
cp .env.example .env
# Edit .env and add your API keys

# 4. Start backend API
cd backend
python api.py

# 5. Open frontend
open frontend/index.html
```

### Option 3: Docker Compose (Recommended)

```bash
docker-compose up -d
```

Chazon will be available at `http://localhost:8000`

---

## 📊 Architecture

```
┌─────────────────────────────────────────────┐
│         Chazon Medical Viewer UI            │
│     DICOM Viewer | Multi-Modality Support   │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         AI Analysis Engine                  │
│   X-Ray Analyzer | Finding Detection        │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│       Qdrant Vector Database                │
│  Medical Image Embeddings | Case Search     │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         Embedding Layer                     │
│  OpenAI | CLIP | Custom Medical Models      │
└─────────────────────────────────────────────┘
```

---

## 🔬 Medical Imaging Templates

### Create a CT Study
```javascript
const ctStudy = MedicalImaging.createStudy({
  modality: 'ct',
  patientId: 'P12345',
  bodyPart: 'HEAD',
  window: { level: 40, width: 80 }
});
```

### Apply Window/Level Presets
```javascript
// Bone window
const boneView = MedicalImaging.applyFilter(imageData, 'bone');

// Lung window
const lungView = MedicalImaging.applyFilter(imageData, 'lung');

// Brain window
const brainView = MedicalImaging.applyFilter(imageData, 'brain');
```

### AI Analysis
```javascript
const analysis = await XRayAnalyzer.analyze(imageData);

console.log(analysis);
// {
//   findings: ["Possible pneumonia in right lower lobe"],
//   confidence: 0.87,
//   abnormalities: [{region: "RLL", severity: "moderate"}]
// }
```

### Semantic Search
```javascript
// Find similar cases in Qdrant
const similar = await QdrantClient.search({
  collection: 'medical_images',
  vector: imageEmbedding,
  limit: 5
});
```

---

## 🎨 Window/Level Presets

### CT Presets
```
Bone:        Level: 400,  Width: 1800
Lung:        Level: -600, Width: 1500
Soft Tissue: Level: 40,   Width: 400
Brain:       Level: 40,   Width: 80
Liver:       Level: 60,   Width: 150
```

### X-Ray Presets
```
Default:     Level: 40,   Width: 400
Bone:        Level: 50,   Width: 500
Soft:        Level: 30,   Width: 300
```

---

## 📁 Project Structure

```
qdrant/
├── frontend/           # Medical imaging viewer UI
├── backend/            # FastAPI + Qdrant integration
├── modules/            # 100+ markdown modules
│   ├── medical-imaging.md
│   ├── xray-analyzer.md
│   ├── dicom-viewer.md
│   └── qdrant-medical.md
├── templates/          # Medical imaging templates
│   └── views/
│       ├── xray-template.md
│       ├── ct-template.md
│       └── mri-template.md
├── language/           # SNT language system
│   ├── trinary/        # Trinary computing
│   └── snt/            # Space-Time Notation
└── docs/               # Documentation
```

---

## 🧬 Technology Stack

- **Frontend:** Vanilla JS (no frameworks needed!)
- **Medical Imaging:** Custom DICOM viewer, window/level engine
- **Vector Search:** Qdrant for semantic similarity
- **AI Analysis:** OpenAI embeddings + custom models
- **Language:** SNT (Space-Time Notation) - trinary quantum computing
- **Architecture:** Markdown-first modular design

---

## 🔑 Configuration

Create a `.env` file:

```bash
# Required for AI features
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Optional: Qdrant Cloud
QDRANT_URL=https://xyz.qdrant.io
QDRANT_API_KEY=...

# Optional: Cohere (sponsor embeddings)
COHERE_API_KEY=...
```

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/analyze` | POST | Analyze medical image |
| `/search` | POST | Semantic search for similar cases |
| `/study` | POST | Create DICOM study |
| `/report` | POST | Generate radiology report |
| `/health` | GET | Health check |

---

## 🏆 Built for lablab.ai

This project was created for the **lablab.ai Qdrant Challenge** to demonstrate:

- ✅ **Vector search** for medical imaging
- ✅ **Semantic similarity** for diagnosis assistance
- ✅ **Multi-modal embeddings** (images + metadata)
- ✅ **Production-ready** architecture
- ✅ **Open source** and accessible

---

## 🌟 Why Chazon?

**Chazon** (חזון - "Vision" in Hebrew) represents our vision for:

- 🌍 **Accessible Healthcare** - Open source medical imaging tools
- 🤖 **AI Assistance** - Help radiologists work faster and more accurately
- 🔬 **Research** - Enable medical research with vector search
- 📚 **Education** - Learn radiology with AI-powered analysis

---

## 📄 License

MIT License - Free for medical and educational use

---

## 🙏 Acknowledgments

- **Qdrant** - Vector database for semantic search
- **lablab.ai** - Hackathon platform and community
- **OpenAI** - Embedding models
- **Medical Community** - DICOM standards and expertise

---

## 📧 Contact

- **GitHub:** https://github.com/teslasolar/qdrant
- **Issues:** https://github.com/teslasolar/qdrant/issues

---

**Built with ❤️ for the medical community**

🏥 Medical Imaging | 🤖 AI-Powered | 🔍 Vector Search | 🌍 Open Source
