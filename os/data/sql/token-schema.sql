# Token Database Schema
**UUID:** a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d
**Token-Dense Storage** | Module Registry & Dependencies

Schema for storing markdown modules in token-dense format.

```sql
-- Modules Table
CREATE TABLE IF NOT EXISTS modules (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  uuid TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  path TEXT NOT NULL,
  category TEXT NOT NULL, -- core, cli, ui, medical, language, boot
  token_count INTEGER NOT NULL,
  content_hash TEXT NOT NULL,
  compressed_content BLOB,
  metadata TEXT, -- JSON
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dependencies Table
CREATE TABLE IF NOT EXISTS dependencies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  module_id INTEGER NOT NULL,
  depends_on_id INTEGER NOT NULL,
  dependency_type TEXT NOT NULL, -- requires, imports, extends
  FOREIGN KEY (module_id) REFERENCES modules(id),
  FOREIGN KEY (depends_on_id) REFERENCES modules(id),
  UNIQUE(module_id, depends_on_id)
);

-- Boot Phases Table
CREATE TABLE IF NOT EXISTS boot_phases (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  phase_number INTEGER NOT NULL,
  phase_name TEXT NOT NULL,
  state TEXT NOT NULL, -- IDLE, LOADING, COMPLETE, FAILED
  load_order INTEGER NOT NULL,
  UNIQUE(phase_number)
);

-- Phase Modules Table (many-to-many)
CREATE TABLE IF NOT EXISTS phase_modules (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  phase_id INTEGER NOT NULL,
  module_id INTEGER NOT NULL,
  load_order INTEGER NOT NULL,
  FOREIGN KEY (phase_id) REFERENCES boot_phases(id),
  FOREIGN KEY (module_id) REFERENCES modules(id),
  UNIQUE(phase_id, module_id)
);

-- Architecture Graph Table
CREATE TABLE IF NOT EXISTS architecture_graph (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  node_type TEXT NOT NULL, -- module, phase, system
  node_id INTEGER NOT NULL,
  parent_id INTEGER,
  layer INTEGER NOT NULL, -- 0=core, 1=cli, 2=ui, 3=medical, 4=language
  x_pos REAL,
  y_pos REAL,
  metadata TEXT -- JSON
);

-- Token Statistics Table
CREATE TABLE IF NOT EXISTS token_stats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  module_id INTEGER NOT NULL,
  total_tokens INTEGER NOT NULL,
  code_tokens INTEGER NOT NULL,
  doc_tokens INTEGER NOT NULL,
  compression_ratio REAL,
  analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (module_id) REFERENCES modules(id)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_modules_category ON modules(category);
CREATE INDEX IF NOT EXISTS idx_modules_uuid ON modules(uuid);
CREATE INDEX IF NOT EXISTS idx_dependencies_module ON dependencies(module_id);
CREATE INDEX IF NOT EXISTS idx_dependencies_depends ON dependencies(depends_on_id);
CREATE INDEX IF NOT EXISTS idx_architecture_layer ON architecture_graph(layer);
CREATE INDEX IF NOT EXISTS idx_token_stats_module ON token_stats(module_id);
```
