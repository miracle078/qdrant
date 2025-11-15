# PackML Baton Passing
**UUID:** 9a6f3e8c-5d2b-4f1e-8a7c-6d4f9e3b2a5c
**ISA-88** | State Handoff System

Implements baton passing between programs using PackML states and flags.

```javascript
const PackMLBaton = {
  batons: new Map(),
  flags: new Map(),

  // Create a new baton
  create(name, initialData = {}) {
    const baton = {
      id: this.generateId(),
      name,
      data: initialData,
      state: 'IDLE',
      holder: null,
      history: [],
      timestamp: Date.now()
    };

    this.batons.set(name, baton);
    console.log(`✓ Baton created: ${name}`);
    return baton;
  },

  // Pass baton from one program to another
  pass(batonName, fromProgram, toProgram, newData = {}) {
    const baton = this.batons.get(batonName);
    if (!baton) {
      console.error(`Baton not found: ${batonName}`);
      return false;
    }

    // Check if fromProgram holds the baton
    if (baton.holder && baton.holder !== fromProgram) {
      console.error(`Baton held by ${baton.holder}, not ${fromProgram}`);
      return false;
    }

    // Record the handoff
    baton.history.push({
      from: fromProgram,
      to: toProgram,
      timestamp: Date.now(),
      state: baton.state,
      data: {...baton.data}
    });

    // Update baton
    baton.holder = toProgram;
    baton.data = {...baton.data, ...newData};
    baton.timestamp = Date.now();

    console.log(`🤝 Baton passed: ${fromProgram} → ${toProgram}`);
    this.setFlag(`${toProgram}_ready`, true);

    return true;
  },

  // Get baton
  get(name) {
    return this.batons.get(name);
  },

  // Release baton
  release(name, program) {
    const baton = this.batons.get(name);
    if (!baton) return false;

    if (baton.holder !== program) {
      console.error(`Program ${program} doesn't hold baton ${name}`);
      return false;
    }

    baton.holder = null;
    baton.state = 'IDLE';
    console.log(`✓ Baton released: ${name} by ${program}`);

    return true;
  },

  // Set a flag for inter-program communication
  setFlag(name, value) {
    this.flags.set(name, {
      value,
      timestamp: Date.now()
    });

    console.log(`🚩 Flag set: ${name} = ${value}`);
  },

  // Get flag value
  getFlag(name) {
    const flag = this.flags.get(name);
    return flag ? flag.value : undefined;
  },

  // Wait for flag to be set (async)
  async waitForFlag(name, expectedValue = true, timeout = 5000) {
    const start = Date.now();

    return new Promise((resolve, reject) => {
      const check = setInterval(() => {
        const value = this.getFlag(name);

        if (value === expectedValue) {
          clearInterval(check);
          resolve(value);
        }

        if (Date.now() - start > timeout) {
          clearInterval(check);
          reject(new Error(`Timeout waiting for flag: ${name}`));
        }
      }, 100);
    });
  },

  // Check PackML state before passing
  checkState(program, requiredState) {
    if (window.PackML) {
      const state = PackML.getState(program);
      return state === requiredState;
    }
    return true;  // Skip check if PackML not available
  },

  // Pass baton with state check
  async passWithStateCheck(batonName, fromProgram, toProgram, requiredState = 'COMPLETE') {
    // Wait for fromProgram to reach required state
    if (window.PackML) {
      await PackML.waitForState(fromProgram, requiredState, 5000);
    }

    // Pass the baton
    return this.pass(batonName, fromProgram, toProgram);
  },

  // Get baton history
  getHistory(name) {
    const baton = this.batons.get(name);
    return baton ? baton.history : [];
  },

  // Clear all batons and flags
  reset() {
    this.batons.clear();
    this.flags.clear();
    console.log('✓ All batons and flags cleared');
  },

  // Generate unique ID
  generateId() {
    return `baton-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
  },

  // List all active batons
  list() {
    console.log('═══════════════════════════════════════');
    console.log('ACTIVE BATONS');
    console.log('═══════════════════════════════════════');

    this.batons.forEach((baton, name) => {
      console.log(`\n${name}:`);
      console.log(`  ID: ${baton.id}`);
      console.log(`  State: ${baton.state}`);
      console.log(`  Holder: ${baton.holder || 'None'}`);
      console.log(`  Data: ${JSON.stringify(baton.data)}`);
      console.log(`  Handoffs: ${baton.history.length}`);
    });
  }
};

window.PackMLBaton = PackMLBaton;
```

## Usage

```javascript
// Create a baton
PackMLBaton.create('processData', { value: 0 });

// Program 1 starts
PackML.setState('program1', 'EXECUTE');
// ... do work ...
PackML.setState('program1', 'COMPLETE');

// Pass baton to program 2
PackMLBaton.pass('processData', 'program1', 'program2', { value: 42 });

// Program 2 waits for flag
await PackMLBaton.waitForFlag('program2_ready');

// Get baton
const baton = PackMLBaton.get('processData');
console.log(baton.data.value);  // 42

// Pass with state check
await PackMLBaton.passWithStateCheck(
  'processData',
  'program2',
  'program3',
  'COMPLETE'
);
```

## Baton Relay Pattern

```javascript
// Sequential program execution with baton passing
async function runProgramRelay(programs) {
  const baton = PackMLBaton.create('relay', { step: 0 });

  for (let i = 0; i < programs.length; i++) {
    const current = programs[i];
    const next = programs[i + 1];

    console.log(`Running: ${current}`);

    // Execute current program
    PackML.setState(current, 'EXECUTE');
    // ... program logic ...
    PackML.setState(current, 'COMPLETE');

    if (next) {
      // Pass baton to next program
      await PackMLBaton.passWithStateCheck(
        'relay',
        current,
        next,
        'COMPLETE'
      );
    }
  }

  console.log('✓ Relay complete!');
}

// Run 3 programs in sequence
await runProgramRelay(['prog1', 'prog2', 'prog3']);
```
