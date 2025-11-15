# Boot Sequencer
**UUID:** 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d
**Boot State Machine** | Phase Orchestration

Boot sequencer manages all boot phases with state machine.

```javascript
const BootSequencer = {
  state: 'IDLE',
  currentPhase: 0,

  phases: [
    '../boot/boot-phase0-core.md',
    '../boot/boot-phase1-cli.md',
    '../boot/boot-phase2-ui.md',
    '../boot/boot-phase3-medical.md',
    '../boot/boot-phase4-language.md',
    '../boot/boot-phase5-programs.md'
  ],

  bootLog: null,

  log(message) {
    if (this.bootLog) {
      const line = document.createElement('div');
      line.className = 'boot-line';
      line.textContent = message;
      this.bootLog.appendChild(line);
    }
  },

  async loadPhaseModule(path) {
    const response = await fetch(path);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const markdown = await response.text();
    const regex = /```javascript\n([\s\S]*?)```/;
    const match = regex.exec(markdown);
    if (match) {
      eval(match[1]);
    }
  },

  async loadModule(path) {
    try {
      const response = await fetch(path);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      const markdown = await response.text();

      // Compile using MDCompiler
      if (window.MDCompiler) {
        const compiled = MDCompiler.compile(markdown);
        let hasError = false;
        compiled.forEach(result => {
          if (!result.success) {
            this.log(`    Error in ${path.split('/').pop()}: ${result.error}`);
            hasError = true;
          }
        });
        if (!hasError) {
          this.log(`  ✓ ${path.split('/').pop()}`);
        }
      }
    } catch (err) {
      this.log(`  ✗ ${path.split('/').pop()}: ${err.message}`);
    }
  },

  async boot() {
    this.state = 'BOOTING';
    this.bootLog = document.getElementById('boot-log');

    this.log('🌌 Chazon v1.0.0');
    this.log('חזון - AI Medical Imaging Analyzer');
    this.log('');

    // Load phase modules first
    this.log('Loading boot sequencer...');
    for (const phasePath of this.phases) {
      await this.loadPhaseModule(phasePath);
    }

    // Execute phases in sequence
    const phaseObjects = [
      window.BootPhase0,
      window.BootPhase1,
      window.BootPhase2,
      window.BootPhase3,
      window.BootPhase4,
      window.BootPhase5
    ];

    for (const phase of phaseObjects) {
      if (phase) {
        await phase.execute(this);
      }
    }

    // Initialize OS
    this.log('');
    this.log('Initializing Chazon OS...');
    if (window.ChazonOS) ChazonOS.boot();

    this.log('');
    this.log('✅ Boot complete!');
    this.log('Type "help" for commands');

    this.state = 'READY';

    setTimeout(() => this.showTerminal(), 2000);
  },

  showTerminal() {
    document.getElementById('boot-screen').classList.add('hidden');
    document.getElementById('terminal').classList.add('active');
    document.querySelector('.taskbar').classList.add('active');

    if (window.ChazonCLI) {
      const output = document.getElementById('output');
      ChazonCLI.init(output);
    }

    // Print welcome
    Terminal.print('═══════════════════════════════════════════════════════════', '#00ff88');
    Terminal.print('      🌌 CHAZON - חזון (Vision)      ', '#00ccff');
    Terminal.print('═══════════════════════════════════════════════════════════', '#00ff88');
    Terminal.print('');
    Terminal.print('🏥 AI Medical Imaging Analyzer | lablab.ai Qdrant Challenge', '#888');
    Terminal.print('');
    Terminal.print('Type "help" for all commands', '#00ccff');
    Terminal.print('Quick Start:', '#00ccff');
    Terminal.print('  ls            - List programs', '#888');
    Terminal.print('  run hello.md  - Run hello program', '#888');
    Terminal.print('  help          - Show all commands', '#888');
    Terminal.print('');
    Terminal.print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', '#00ff88');
    Terminal.print('');

    document.getElementById('input').focus();
  }
};

window.BootSequencer = BootSequencer;
```
