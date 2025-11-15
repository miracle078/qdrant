# Chazon Core Index
**φ-Balanced Architecture** | ISA-95 L0-L4 | ISA-88 PackML

Core module registry with state machines, sync, and API/MCP wrappers.

## Modules (13 files)

### State Management (ISA-88)
**PackML** - State machine (IDLE→STARTING→EXECUTE→COMPLETE)
**ChangeLog** - UUID-based change tracking
**SQLiteDB** - Browser SQLite persistence
**SyncEngine** - Multi-device synchronization

### Execution Layer (ISA-95)
**ChazonOS** (L4) - Kernel, event bus, orchestration
**MDCompiler** (L3) - Markdown → JavaScript execution
**ChazonCLI** (L2) - Command interface
**StateManager** (L1) - localStorage with φ-cache (161 items)

### Integration Layer
**MCP** - Model Context Protocol wrapper
**ChazonAPI** - RESTful API (GET/POST/PUT/DELETE)
**ModuleWrapper** - Auto-wrap modules with CLI/API/MCP
**ChazonIntegration** - System initialization orchestrator

## ISA Compliance

**ISA-95 Hierarchy:**
```
L4: Enterprise    → ChazonOS, ChazonIntegration
L3: MES/Control   → MDCompiler
L2: Supervisory   → ChazonCLI, ChazonAPI
L1: Basic Control → StateManager, SQLiteDB
L0: Physical      → PackML, Browser APIs
```

**ISA-88 PackML States:**
- IDLE, STARTING, EXECUTE, COMPLETING, COMPLETE
- STOPPING, STOPPED, ABORTING, ABORTED, CLEARING

## Bootstrap Order

1. **PackML** (state machine core)
2. **ChangeLog** (tracking infrastructure)
3. **SQLiteDB** (persistence layer)
4. **MDCompiler** (required by all)
5. **ChazonOS** (kernel init)
6. **ChazonCLI** (user interface)
7. **StateManager** (localStorage)
8. **MCP** (protocol wrapper)
9. **ChazonAPI** (REST interface)
10. **ModuleWrapper** (auto-integration)
11. **SyncEngine** (multi-device sync)
12. **ChazonIntegration** (orchestration)

## φ-Balance Design

- All modules < 250 tokens
- Timeout: 1618ms (φ × 1000)
- Cache: 161 items (φ × 100)
- Cascade: `50 + n × 30 × φ` pixels

## Features

**CLI/API/MCP:** Every module automatically wrapped with 3 interfaces
**State Machines:** PackML tracks lifecycle of every operation
**Sync:** UUID-based conflict-free replication across devices
**Changelog:** Immutable audit trail with full history
**SQLite:** Browser-compatible persistence with localStorage fallback

---
**13 core modules** | **φ = 1.618** | **Total: ~2,100 tokens**
