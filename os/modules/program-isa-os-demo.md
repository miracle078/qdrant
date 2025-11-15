# ISA-OS Demo
**Docker → ISA-95 Mapping** | Container Runtime

Demonstrates how Docker container layers map to ISA-95 automation levels.

```javascript
const ISAOSDemo = {
  async run() {
    Terminal.print('\n🏭 ISA-OS Container Runtime Demo\n');

    // Show ISA level mapping
    const mapping = {
      'L0 (Field Devices)': 'FROM - Base image',
      'L1 (Control)': 'RUN - Build commands',
      'L2 (Supervisory)': 'COPY/WORKDIR/ENV - File operations',
      'L3 (Operations)': 'CMD/ENTRYPOINT - Execution',
      'L4 (Enterprise)': 'EXPOSE - Network/Integration'
    };

    for(const [level, cmd] of Object.entries(mapping)) {
      Terminal.print(`  ${level}: ${cmd}`);
      await new Promise(r => setTimeout(r, 200));
    }

    Terminal.print('\n✨ Try it: isa-os.html');
    Terminal.print('Load Dockerfiles from GitHub and watch them build!');

    return {
      status: 'complete',
      message: 'ISA-OS demonstrates deep ISA-95 understanding'
    };
  }
};

window.ISAOSDemo = ISAOSDemo;
```
