# Chazon Programs
**Sample Program Catalog** | All ISA Levels

Reference guide for example programs demonstrating Chazon OS capabilities.

## Programs by ISA Level

### L0: Physical Process
- **hello.md** - Hello World program, basic execution and console output

### L1: Basic Control
- **calculator.md** - Mathematical operations and object methods
- **data.md** - Data transformation with functional programming

### L2: Supervisory Control
- **search.md** - Qdrant vector search demonstration
- **events.md** - Event-driven architecture and pub/sub messaging

### L3: Manufacturing Operations
- **neural.md** - Neural network with phi-balanced activation
- **cicd.md** - CI/CD pipeline with testing (also L4)

### L4: Business Planning
- **cicd.md** - Deployment orchestration and automation

## Running Programs

Via CLI:
```javascript
ChazonCLI.exec('run hello');
ChazonCLI.exec('run calculator');
ChazonCLI.exec('run search');
```

Direct compilation:
```javascript
const program = await fetch('programs/hello.md').then(r => r.text());
MDCompiler.compile(program);
```

## Features Demonstrated
- Console I/O and return values
- Object-oriented programming
- Functional programming (map, filter, reduce)
- Event-driven architecture
- Mock API integration
- Agent system integration
- Mathematical algorithms
- Data structures and transformations
