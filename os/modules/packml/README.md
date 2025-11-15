# PackML State Machine
**Type:** ISA-88 | Batch Control

PackML (Packaging Machine Language) state machine implementation.

## Module

- **packml-baton.md** - PackML state machine with baton passing
  - State transitions (IDLE → STARTING → EXECUTE → COMPLETING → COMPLETE)
  - Baton passing between modules
  - Error handling and recovery

## PackML States

```
IDLE
  ↓ Start
STARTING
  ↓ Started
EXECUTE
  ↓ Complete
COMPLETING
  ↓ Completed
COMPLETE
  ↓ Reset
IDLE
```

## State Transitions

- **IDLE** → **STARTING**: Start command received
- **STARTING** → **EXECUTE**: Initialization complete
- **EXECUTE** → **COMPLETING**: Task complete
- **COMPLETING** → **COMPLETE**: Finalization complete
- **COMPLETE** → **IDLE**: Reset command

## Baton Passing

Modules pass control to the next module in sequence:
1. Module A completes → passes baton
2. Module B receives baton → executes
3. Module B completes → passes baton to Module C

## See Also

- `../../boot/` - Boot sequencer uses PackML states
- `../../../docs/standards/isa/isa-88/` - ISA-88 batch control standard
