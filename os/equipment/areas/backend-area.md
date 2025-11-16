# Backend Area

**ISA-88 Level:** Area
**Parent:** Production Site
**ISA-95 Level:** L3 (MES) / L2 (Supervisory)
**Location:** `/os/backend/`

---

## Area Overview

**Name:** Backend API Services Area
**Purpose:** API request processing, vector search coordination, embedding generation
**Scope:** All backend services that support the medical imaging analysis system

### Area Description

The Backend Area is responsible for server-side processing, including:
- RESTful API endpoints (FastAPI)
- Qdrant vector database integration
- Embedding generation coordination
- Request routing and response formatting
- External service integration

---

## Area Hierarchy

```
Backend Area (/os/backend/)
├── API Gateway Process Cell
│   ├── Health Check Unit
│   ├── Search Unit
│   └── Index Unit
├── Qdrant Integration Process Cell
│   ├── Connection Manager Unit
│   └── Vector Operations Unit
└── Embedding Process Cell
    ├── Text Embedding Unit
    ├── Image Embedding Unit
    └── Multi-modal Embedding Unit
```

---

## Process Cells

### 1. API Gateway Process Cell
**Purpose:** HTTP request handling and routing
**Location:** `/os/backend/api.py`
**Equipment:**
- FastAPI application
- Route handlers
- Request validators
- Response formatters

### 2. Qdrant Integration Process Cell
**Purpose:** Vector database operations
**Equipment:**
- Qdrant client
- Connection pool manager
- Query builder
- Result processor

### 3. Embedding Process Cell
**Purpose:** Generate embeddings for images and text
**Equipment:**
- OpenAI API client
- CodeBERT embedding generator
- CLIP model integration
- Embedding cache

---

## Area Equipment

### Controllers
- **Area PLC:** `/os/backend/plc.html` (100ms scan time, 28 tags)
- **Area SCADA:** `/os/backend/scada.html` (supervisory control)
- **Area HMI:** `/os/backend/hmi.html` (operator interface)

### Infrastructure
- **API Server:** FastAPI Python application
- **Dependencies:** `requirements.txt` (fastapi, qdrant-client, openai, etc.)
- **Containerization:** `Dockerfile`, `docker-compose.yml`

### Tag Provider
- **Tags File:** `/os/controls/tag-providers/backend.json`
- **Tag Count:** 28 tags
- **Categories:** Status, performance, connection, error tags

---

## Area Tags (Level 0)

### Status Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `API_Status` | BOOL | RO | API server running status |
| `Qdrant_Connected` | BOOL | RO | Qdrant connection established |
| `FastAPI_Ready` | BOOL | RO | FastAPI initialized |
| `Server_Health` | STRING | RO | Overall health status |

### Performance Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Request_Count` | INT | RO | Total requests processed |
| `Requests_Per_Second` | REAL | RO | Current RPS |
| `Response_Time_ms` | REAL | RO | Average response time |
| `Response_Time_P95_ms` | REAL | RO | 95th percentile response time |
| `Response_Time_P99_ms` | REAL | RO | 99th percentile response time |

### Connection Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Active_Connections` | INT | RO | Current active HTTP connections |
| `Qdrant_Port` | INT | RO | Qdrant connection port (6333) |
| `Qdrant_Host` | STRING | RO | Qdrant server host |
| `Connection_Pool_Size` | INT | RO | Active connection pool size |

### Operation Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Vector_Search_Active` | BOOL | RO | Vector search in progress |
| `Embedding_Queue_Size` | INT | RO | Embeddings pending generation |
| `Search_Queries_Count` | INT | RO | Total search queries executed |
| `Index_Operations_Count` | INT | RO | Total indexing operations |
| `Collection_Count` | INT | RO | Number of Qdrant collections |

### Error Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Last_Error` | STRING | RO | Most recent error message |
| `Error_Count` | INT | RO | Total errors encountered |
| `Qdrant_Errors` | INT | RO | Qdrant-specific errors |
| `API_Errors` | INT | RO | API endpoint errors |
| `Network_Errors` | INT | RO | Network connectivity errors |

### Control Tags
| Tag Name | Type | Access | Description |
|----------|------|--------|-------------|
| `Enable_Caching` | BOOL | RW | Enable/disable result caching |
| `Max_Query_Results` | INT | RW | Maximum results per query |
| `Timeout_Seconds` | INT | RW | API request timeout |
| `Rate_Limit_RPS` | INT | RW | Rate limiting (requests/second) |

---

## Area Operations

### Normal Production Mode

**Sequence:**
1. Receive HTTP request at endpoint
2. Validate request parameters
3. Route to appropriate handler
4. Execute business logic
5. Format and return response

**Control Logic (PLC):**
```python
# Backend PLC Control Loop (100ms scan)
if API_Status and Qdrant_Connected:
    # Process incoming requests
    for request in request_queue:
        validate_request(request)
        route_request(request)
        execute_handler(request)
        send_response(request)

    # Update performance metrics
    update_response_times()
    update_connection_counts()
    update_error_counts()

    # Monitor health
    check_qdrant_health()
    check_api_health()
```

### Emergency Mode

**Triggers:**
- Qdrant connection lost
- High error rate (>10% requests failing)
- Response time exceeds threshold (>5s)
- Memory exhaustion

**Actions:**
- Switch to degraded mode (cached responses only)
- Log emergency condition
- Alert operators
- Attempt reconnection

---

## Area Metrics

### KPIs
- **Throughput:** Requests per second
- **Latency:** Response time (p50, p95, p99)
- **Availability:** Uptime percentage
- **Error Rate:** Failed requests percentage

### Targets
- **Throughput:** >100 RPS
- **Latency P95:** <500ms
- **Availability:** >99.9%
- **Error Rate:** <0.1%

---

## Process Cell Definitions

See detailed process cell documents:
- `../process-cells/api-gateway-cell.md`
- `../process-cells/qdrant-integration-cell.md`
- `../process-cells/embedding-cell.md`

---

## Related Documents

- `../site/production-site.md` - Parent site
- `/os/backend/plc.html` - Area PLC controller
- `/os/backend/scada.html` - Area SCADA interface
- `/os/backend/hmi.html` - Area HMI panel
- `/os/controls/tag-providers/backend.json` - Tag definitions

---

**Document Version:** 1.0
**Last Updated:** 2025-11-15
**Owner:** Backend Area Management
**Status:** Active
