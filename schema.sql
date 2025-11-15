-- Chazon Database Schema
-- UUID: 8b79fb96-ef94-4fea-b508-6eb6aa3a373a
-- ISA-95 L3: MES/Data Layer

-- File registry table
CREATE TABLE IF NOT EXISTS files (
    uuid TEXT PRIMARY KEY,
    path TEXT UNIQUE NOT NULL,
    type TEXT NOT NULL,
    module_name TEXT,
    created_at INTEGER DEFAULT (strftime('%s', 'now')),
    updated_at INTEGER DEFAULT (strftime('%s', 'now')),
    size_bytes INTEGER,
    hash TEXT,
    metadata TEXT -- JSON
);

-- Module dependency graph
CREATE TABLE IF NOT EXISTS dependencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_uuid TEXT NOT NULL,
    to_uuid TEXT NOT NULL,
    dep_type TEXT, -- 'import', 'load', 'requires'
    FOREIGN KEY (from_uuid) REFERENCES files(uuid),
    FOREIGN KEY (to_uuid) REFERENCES files(uuid),
    UNIQUE(from_uuid, to_uuid)
);

-- Embeddings cache
CREATE TABLE IF NOT EXISTS embeddings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_uuid TEXT,
    text TEXT NOT NULL,
    vector BLOB NOT NULL, -- Serialized float array
    model TEXT NOT NULL,
    dimension INTEGER NOT NULL,
    created_at INTEGER DEFAULT (strftime('%s', 'now')),
    FOREIGN KEY (file_uuid) REFERENCES files(uuid)
);

CREATE INDEX IF NOT EXISTS idx_embeddings_file ON embeddings(file_uuid);
CREATE INDEX IF NOT EXISTS idx_embeddings_model ON embeddings(model);

-- Qdrant collection metadata
CREATE TABLE IF NOT EXISTS collections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    dimension INTEGER NOT NULL,
    distance_metric TEXT DEFAULT 'cosine',
    vector_count INTEGER DEFAULT 0,
    created_at INTEGER DEFAULT (strftime('%s', 'now')),
    updated_at INTEGER DEFAULT (strftime('%s', 'now')),
    config TEXT -- JSON
);

-- Point tracking for Qdrant
CREATE TABLE IF NOT EXISTS points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    point_id TEXT UNIQUE NOT NULL,
    collection_name TEXT NOT NULL,
    file_uuid TEXT,
    payload TEXT, -- JSON
    synced_at INTEGER DEFAULT (strftime('%s', 'now')),
    FOREIGN KEY (file_uuid) REFERENCES files(uuid),
    FOREIGN KEY (collection_name) REFERENCES collections(name)
);

CREATE INDEX IF NOT EXISTS idx_points_collection ON points(collection_name);
CREATE INDEX IF NOT EXISTS idx_points_file ON points(file_uuid);

-- Build log
CREATE TABLE IF NOT EXISTS builds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    build_id TEXT UNIQUE NOT NULL,
    status TEXT NOT NULL, -- 'running', 'success', 'failed'
    started_at INTEGER DEFAULT (strftime('%s', 'now')),
    finished_at INTEGER,
    modules_built INTEGER DEFAULT 0,
    errors TEXT -- JSON array
);

-- ISA standards tracking
CREATE TABLE IF NOT EXISTS isa_standards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    standard TEXT NOT NULL, -- 'ISA-95', 'ISA-88', 'ISA-18.2'
    section TEXT,
    level INTEGER, -- L0-L4 for ISA-95
    title TEXT,
    content TEXT,
    file_uuid TEXT,
    FOREIGN KEY (file_uuid) REFERENCES files(uuid)
);

CREATE INDEX IF NOT EXISTS idx_isa_standard ON isa_standards(standard, section);
CREATE INDEX IF NOT EXISTS idx_isa_level ON isa_standards(level);
