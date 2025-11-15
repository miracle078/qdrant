# Quantum Superposition
**UUID:** 2a8f5e9c-6d4b-4f3e-7a1c-9d2f8e5b3a6c
**Quantum States in SNT** | Superposition & Collapse

Demonstrates quantum state operations in Space-Time Notation.

```snt
// Quantum superposition
|0⟩ + |1⟩ = |+⟩

// Create superposed state
quantum state {
  amplitude: [|0⟩, |1⟩, |+⟩]
  collapsed: false
}

// Measurement collapses superposition
@present measure(state)
@future collapse(|0⟩ or |1⟩)

// Quantum entanglement
entangle {
  particle_a: |0⟩
  particle_b: |1⟩
  measure(a) → collapse(b)
}
```

## JavaScript Implementation

```javascript
// Create quantum state
const qState = {
  trits: [1, -1, 0],  // |0⟩, |1⟩, |+⟩
  superposed: true
};

// Map to photonic representation
const photons = PhotonicLayer.encodePhotonic(qState.trits);

// Superpose photons
const superposed = PhotonicLayer.superpose(photons[0], photons[1]);

console.log(superposed);
// {
//   amplitude: 0.5,    // Averaged
//   polarization: 45,  // Diagonal
//   wavelength: 550    // Green
// }

// Collapse to definite state
const collapsed = PhotonicLayer.photonToTrit(superposed);
// 0 (neutral state)
```

## State Diagram

```
Initial: |0⟩ + |1⟩
          ↓
    Superposition: |+⟩
          ↓
      Measurement
          ↓
    Collapse: |0⟩ or |1⟩
    (50% probability each)

Trinary Mapping:
  |0⟩ →  1 (positive)
  |1⟩ → -1 (negative)
  |+⟩ →  0 (superposition)
```
