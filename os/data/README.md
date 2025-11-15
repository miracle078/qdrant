# Data Directory
**Token Database & Architecture Maps**

This directory contains token-dense database system and architecture documentation.

## Structure

```
data/
├── sql/
│   └── token-schema.sql       # Database schema
├── architecture-map.md         # System architecture overview
├── dependency-graph.md         # Module dependency graphs
└── README.md                   # This file
```

## Token Database System

### Purpose
Store all markdown modules in token-dense format for:
- Fast querying and analysis
- Dependency tracking
- Architecture visualization
- Token counting and optimization
- MCP/API access

### Schema Tables

**modules** - Core module registry
- id, uuid, name, path, category
- token_count, content_hash, compressed_content
- metadata (JSON)

**dependencies** - Module dependencies
- module_id → depends_on_id
- dependency_type (requires, imports, extends)

**boot_phases** - Boot sequence tracking
- phase_number, phase_name, state
- load_order

**phase_modules** - Phase → Module mapping
- Links modules to boot phases

**architecture_graph** - Visual architecture
- node_type, node_id, parent_id
- layer (0-4), x_pos, y_pos

**token_stats** - Token statistics
- Per-module token counts
- Code vs documentation tokens
- Compression ratios

## Usage

### Initialize Database
```javascript
await TokenDB.init();
```

### Analyze Modules
```javascript
const analysis = await TokenAnalyzer.analyzeModule('../modules/chazon-os.md');
await TokenDB.insertModule(analysis);
```

### Query Modules
```javascript
const coreModules = await TokenDB.getModulesByCategory('core');
const stats = await TokenDB.getTokenStats();
```

### CLI Commands
```bash
db:init              # Initialize database
db:analyze           # Analyze all modules
db:stats             # Show token statistics
db:query core        # Query modules by category
db:deps 1            # Show dependencies for module ID 1
db:export            # Export database to file
db:arch              # Show architecture graph
```

### MCP Tools
```javascript
// Query modules via MCP
await MCPDatabase.handleToolCall('query_modules', { category: 'core' });

// Get dependencies
await MCPDatabase.handleToolCall('get_dependencies', { module_name: 'chazon-os' });

// Get architecture
await MCPDatabase.handleToolCall('get_architecture', { layer: 0 });

// Get stats
await MCPDatabase.handleToolCall('get_token_stats', {});
```

### API Endpoints
```
GET  /api/db/modules?category=core&limit=10
GET  /api/db/modules/:id
GET  /api/db/modules/:id/dependencies
GET  /api/db/stats
GET  /api/db/architecture?layer=0
POST /api/db/analyze
POST /api/db/batch-analyze
```

## Architecture Maps

### architecture-map.md
Complete system architecture showing:
- 5 layers (Core, CLI, UI, Medical, Language)
- Module organization per layer
- Boot flow sequence
- Data flow diagrams
- Token distribution

### dependency-graph.md
Mermaid diagrams showing:
- Module dependencies per layer
- Cross-layer dependencies
- Boot dependencies
- Database dependencies
- Critical execution paths

## Token Counting

### Token Estimation
- **Rough estimate**: ~4 characters per token
- Separates code tokens from documentation tokens
- Tracks compression ratios

### Categories
- **core** - Core infrastructure (7 modules)
- **cli** - CLI system (12+ modules)
- **ui** - UI components (11 modules)
- **medical** - Medical imaging (7 modules)
- **language** - SNT language (6 modules)
- **boot** - Boot system (6 modules)
- **programs** - User programs (16+ modules)

## Integration

### Boot Phase
Database modules can be loaded in boot phase:
```javascript
// In boot-phase1-cli.md or custom phase
modules: [
  '../modules/db-token.md',
  '../modules/token-analyzer.md',
  '../modules/mcp-database.md',
  '../modules/api-database.md',
  '../modules/cli-db.md'
]
```

### Frontend Access
```javascript
// Initialize and query
await TokenDB.init();
const stats = await TokenDB.getTokenStats();
console.log(stats);
```

### Backend Integration
Python backend can serve API endpoints:
```python
from fastapi import FastAPI
import sqlite3

@app.get("/api/db/stats")
async def get_stats():
    conn = sqlite3.connect("data/sql/tokens.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM token_stats")
    return cursor.fetchall()
```

## Benefits

- **Token-dense**: Optimized for LLM processing
- **Queryable**: Fast SQL queries for module lookup
- **Dependency tracking**: Know what depends on what
- **Architecture clarity**: Visual maps of system structure
- **MCP compatible**: Use from Claude Desktop or other MCP clients
- **API ready**: REST endpoints for web access
- **CLI integrated**: Test and query from terminal

---

**Token Database System** | Chazon Architecture Data
