# Hello SNT
**UUID:** 7e1f8a9c-4d2b-4f6e-9a5c-3d7f9e4b2a1c
**Hello World in SNT** | Space-Time Notation

Simple SNT program demonstrating timeline operations.

```snt
// Hello World across timelines
@past load "Hello"
@present compute concat
@future store "Hello, Space-Time!"

// Emoji encoding
🔮.encode(72)  // 'H' = [0, 0, 1, -1, 0, 1]
🔮.encode(101) // 'e' = [1, 0, 1, 1, -1, 0]

// Quantum greeting
|0⟩ + |1⟩ = |+⟩  // Superposition state
```

## Expected Output

```javascript
const result = SNTParser.exec(`
  @past load "Hello"
  @present compute concat
  @future store "Hello, Space-Time!"
`);

// Timeline results:
// past (-1): load "Hello"
// present (0): compute concat
// future (1): store "Hello, Space-Time!"
```

## Visualization

```
Timeline:
  Past    [-1] ← load "Hello"
  Present [ 0] ← compute concat
  Future  [ 1] → store result
```
