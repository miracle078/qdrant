# Test Agent
**ISA-95 L1 + ISA-18.2** | Unit Testing with Alarm Management

Execute unit tests with standardized alarm handling for failures.

```javascript
const TestAgent = {
  isa_level: 1, // L1: Unit/Cell Control

  run(tests) {
    const results = tests.map(t => this.runTest(t));
    this.report(results);
    return results;
  },

  runTest(test) {
    try {
      const start = performance.now();
      const result = eval(test.code);
      const duration = performance.now() - start;
      const passed = test.expect ? result === test.expect : !!result;

      return {
        name: test.name,
        passed,
        duration: `${duration.toFixed(2)}ms`,
        result,
        alarm: passed ? null : this.raiseAlarm(test)
      };
    } catch (err) {
      return {
        name: test.name,
        passed: false,
        error: err.message,
        alarm: this.raiseAlarm(test, err)
      };
    }
  },

  raiseAlarm(test, err) {
    // ISA-18.2 Alarm Management
    return {
      priority: test.critical ? 'HIGH' : 'MEDIUM',
      type: 'TEST_FAILURE',
      message: err?.message || 'Assertion failed',
      standard: 'ISA-18.2'
    };
  },

  report(results) {
    const passed = results.filter(r => r.passed).length;
    console.log(`${passed}/${results.length} tests passed`);
  }
};

window.TestAgent = TestAgent;
```
