# Boot Phase 5: Programs
**UUID:** 6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c
**User Programs** | Demo Programs, Examples

Phase 5 loads user programs and examples.

```javascript
const BootPhase5 = {
  name: 'Phase 5: Programs',
  state: 'IDLE',

  programs: [
    '../modules/program-hello.md',
    '../modules/program-calculator.md',
    '../modules/program-data.md',
    '../modules/program-search.md',
    '../modules/program-events.md',
    '../modules/program-neural.md',
    '../modules/program-cicd.md',
    '../modules/program-test-sync.md',
    '../modules/program-attractor-demo.md',
    '../modules/program-qdrant-real-demo.md',
    '../modules/program-isa-os-demo.md',
    '../modules/program-medical-demo.md',
    '../modules/program-xray-3d.md',
    '../language/snt/examples/hello-snt.md',
    '../language/snt/examples/paradox-resolution.md',
    '../language/snt/examples/quantum-superposition.md'
  ],

  async execute(loader) {
    if (!window.ChazonCLI) {
      loader.log('⚠️ CLI not available, skipping programs');
      this.state = 'SKIPPED';
      return false;
    }

    this.state = 'LOADING';
    loader.log('Phase 5: Loading programs...');

    for (const program of this.programs) {
      try {
        const response = await fetch(program);
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const content = await response.text();
        const name = program.split('/').pop();
        ChazonCLI.addFile(name, content);
        loader.log(`  ✓ ${name}`);
      } catch (err) {
        loader.log(`  ✗ ${program.split('/').pop()}: ${err.message}`);
      }
    }

    this.state = 'COMPLETE';
    loader.log('✓ Phase 5 complete');
    return true;
  }
};

window.BootPhase5 = BootPhase5;
```
