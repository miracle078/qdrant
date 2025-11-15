# Paradox Resolution
**UUID:** 9f2e6a8c-5d3b-4f7e-8a1c-6d4f7e2b9a5c
**Temporal Paradox Example** | Timeline Branching

Demonstrates paradox detection and resolution in SNT.

```snt
// Grandfather paradox scenario
@past kill(grandfather)
@present exists(self)
@future resolve(paradox)

// Detection
paradox bootstrap {
  @past create(information)
  @future send(information)
  @past receive(information)  // Loop!
}

// Resolution: Create timeline branch
resolve {
  timeline.split()
  timeline.A: past unchanged
  timeline.B: past modified
}
```

## JavaScript Implementation

```javascript
const paradoxCode = `
  @past modify(x)
  @present compute(x)
  @past read(x)
`;

const result = SNTParser.exec(paradoxCode);

// Detect cycle
const paradox = SpaceTimeCompiler.detectParadox(result.timeline);

if (paradox.detected) {
  console.log(paradox.resolution);
  // {
  //   strategy: 'timeline-branch',
  //   original: -1,
  //   resolved: 1,
  //   message: 'Paradox resolved: -1 → 1'
  // }
}
```

## Timeline Visualization

```
Before Resolution:
  Past ← modify(x)
    ↓
  Present ← compute(x)
    ↓
  Past ← read(x)  ⚠️ PARADOX!

After Resolution:
  Timeline A:  Past (unchanged)
               ↓
  Timeline B:  Past (modified)
               ↓
  Both exist in superposition
```
