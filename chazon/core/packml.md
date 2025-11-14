# PackML State Machine
**ISA-88 Compliant** | State Management Core

PackML (Packaging Machine Language) state machine for module lifecycle.

```javascript
const PackML = {
  // ISA-88 PackML States
  states: {
    IDLE: 'idle',
    STARTING: 'starting',
    EXECUTE: 'execute',
    COMPLETING: 'completing',
    COMPLETE: 'complete',
    STOPPING: 'stopping',
    STOPPED: 'stopped',
    ABORTING: 'aborting',
    ABORTED: 'aborted',
    CLEARING: 'clearing'
  },

  machines: {},

  create(id) {
    this.machines[id] = {
      id,
      state: this.states.IDLE,
      history: [],
      timestamp: Date.now()
    };
    return this.machines[id];
  },

  transition(id, newState) {
    const machine = this.machines[id];
    if (!machine) return { error: 'Machine not found' };

    const oldState = machine.state;
    machine.state = newState;
    machine.timestamp = Date.now();
    machine.history.push({ from: oldState, to: newState, at: machine.timestamp });

    // Log to changelog
    if (window.ChangeLog) {
      ChangeLog.record('state_transition', { id, oldState, newState });
    }

    return { success: true, from: oldState, to: newState };
  },

  getState(id) {
    return this.machines[id]?.state || this.states.IDLE;
  },

  // Start sequence: IDLE → STARTING → EXECUTE
  start(id) {
    this.transition(id, this.states.STARTING);
    setTimeout(() => this.transition(id, this.states.EXECUTE), 100);
  },

  // Stop sequence: EXECUTE → STOPPING → STOPPED
  stop(id) {
    this.transition(id, this.states.STOPPING);
    setTimeout(() => this.transition(id, this.states.STOPPED), 100);
  },

  // Abort sequence: * → ABORTING → ABORTED
  abort(id) {
    this.transition(id, this.states.ABORTING);
    setTimeout(() => this.transition(id, this.states.ABORTED), 50);
  }
};

window.PackML = PackML;
```
