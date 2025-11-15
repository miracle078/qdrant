# Sync Test
**System Synchronization Test** | ISA-95 L4

Test PackML state machines, changelog, and sync engine.

```javascript
console.log('🧪 Testing Sync System...\n');

// 1. Test PackML State Machine
console.log('1️⃣ PackML State Machine:');
const machine = PackML.create('test-machine');
console.log(`  Created: ${machine.id} in state ${machine.state}`);

PackML.start('test-machine');
setTimeout(() => {
  console.log(`  State after start: ${PackML.getState('test-machine')}`);
}, 150);

// 2. Test ChangeLog
console.log('\n2️⃣ ChangeLog System:');
const entry1 = ChangeLog.record('test_event', { foo: 'bar', φ: 1.618 });
console.log(`  Entry: ${entry1.id.slice(0, 8)}...`);

const entry2 = ChangeLog.record('another_event', { data: [1, 2, 3] });
console.log(`  Entry: ${entry2.id.slice(0, 8)}...`);

const recent = ChangeLog.get(5);
console.log(`  Recent entries: ${recent.length}`);

// 3. Test MCP
console.log('\n3️⃣ MCP Endpoints:');
const endpoints = MCP.list();
console.log(`  Registered: ${endpoints.length} endpoints`);
endpoints.slice(0, 3).forEach(ep => {
  console.log(`    ${ep.name} (${ep.state})`);
});

// 4. Test API
console.log('\n4️⃣ API Routes:');
ChazonAPI.get('/status').then(res => {
  console.log(`  GET /status: ${res.status}`);
  console.log(`  Uptime: ${(res.data.uptime / 1000).toFixed(2)}s`);
});

// 5. Test Sync Engine
console.log('\n5️⃣ Sync Engine:');
const snapshot = SyncEngine.export();
console.log(`  Local ID: ${snapshot.id.slice(0, 8)}`);
console.log(`  Changelog: ${snapshot.changelog.length} entries`);
console.log(`  States: ${Object.keys(snapshot.states).length} machines`);

console.log('\n✅ Sync system test complete!');

return { success: true, tests: 5 };
```
