# Tests
**Automated Testing** | Quality Assurance

Chazon OS test suite (coming soon).

## Test Programs

Currently testing via:
- `chazon/programs/test-sync.md` - Sync engine tests
- `chazon/programs/cicd.md` - CI/CD pipeline tests

## Planned Tests

```javascript
const Tests = {
  unit: ['compiler', 'state', 'sync'],
  integration: ['qdrant-client', 'embeddings'],
  e2e: ['boot-sequence', 'program-execution']
};
```

All programs follow ISA-88 PackML state machines for reliable testing.
