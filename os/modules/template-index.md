# Templates
**Page Templates** | Assembly System

Dynamic page assembly using component-based architecture.

## Available Templates

### [base.md](base.md)
Base template for assembling pages from markdown components using PackML state machines.

## Architecture

```
Page Definition (YAML + JS)
     ↓
PageBuilder (State Machine)
     ↓
Component Loader (MD Compiler)
     ↓
HTML Assembly
     ↓
Rendered Page
```

All templates follow ISA-88 PackML lifecycle:
IDLE → STARTING → EXECUTE → COMPLETE

Components loaded asynchronously, assembled through state transitions.
