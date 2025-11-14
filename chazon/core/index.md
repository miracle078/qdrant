# Chazon Core Index
**φ-Balanced Architecture** | ISA-95 L0-L4

Core module registry and loading order for Chazon OS.

## Modules

**MDCompiler** (L3) - Parse and execute markdown code blocks
**ChazonOS** (L4) - Kernel, event bus, module orchestration
**ChazonCLI** (L2) - Command interface and virtual filesystem
**StateManager** (L1) - Persistent localStorage with φ-cache

## ISA-95 Hierarchy

```
L4: Enterprise    → ChazonOS (orchestration)
L3: MES/Control   → MDCompiler (execution)
L2: Supervisory   → ChazonCLI (interface)
L1: Basic Control → StateManager (persistence)
L0: Physical      → Browser APIs
```

## Bootstrap Order

1. MDCompiler (required by all)
2. ChazonOS (kernel init)
3. ChazonCLI (user interface)
4. StateManager (persistence)
5. Extensions (UI/Agents)

## φ-Balance Design

- All modules < 250 tokens
- Timeout: 1618ms (φ * 1000)
- Cache ratio: 61.8% / 38.2%
- Max items: 161 (φ * 100)

## Integration

Modules register on `window` object. ChazonOS discovers via `registerModules()`.
CLI accesses compiler via `ChazonOS.getModule('compiler')`. Event bus enables
decoupled communication. State persists across sessions.

---
**4 core modules** | **φ = 1.618** | **Total: <800 tokens**
