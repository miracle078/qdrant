# Irrational Attractors
**Dynamical Systems** | Equilibrium Points

Multi-irrational attractor system where each irrational number governs its optimal domain.

```javascript
const Attractors = {
  // Irrational constants as equilibrium points
  φ: (1 + Math.sqrt(5)) / 2,           // 1.618 - Golden ratio (aesthetics, balance)
  φ_inv: 2 / (1 + Math.sqrt(5)),       // 0.618 - Inverse phi (decay, reduction)
  e: Math.E,                            // 2.718 - Natural growth (exponential)
  π: Math.PI,                           // 3.142 - Circular/periodic (waves, rotations)
  √2: Math.sqrt(2),                     // 1.414 - Diagonal/scaling (geometric)
  √3: Math.sqrt(3),                     // 1.732 - Hexagonal packing
  √5: Math.sqrt(5),                     // 2.236 - Pentagonal symmetry

  // Domain mappings - which irrational governs which system
  domains: {
    aesthetic: 'φ',        // UI spacing, layouts, visual balance
    growth: 'e',           // Learning rates, exponential processes
    periodic: 'π',         // Rotations, waves, cycles
    scaling: '√2',         // Zoom levels, geometric progression
    packing: '√3',         // Data structures, spatial organization
    decay: 'φ_inv',        // Timeout reduction, fallback strategies
    resonance: '√5'        // Network effects, viral coefficients
  },

  // Get attractor value for domain
  get(domain) {
    const key = this.domains[domain];
    return this[key] || this.φ;
  },

  // Calculate equilibrium point for given system
  equilibrium(systemType, initialValue = 1) {
    const attractor = this.get(systemType);

    // Iterate toward attractor (simple fixed-point iteration)
    let value = initialValue;
    for (let i = 0; i < 10; i++) {
      value = attractor * Math.sin(value / attractor) + attractor;
    }

    return value;
  },

  // Spiral convergence (like Fibonacci)
  spiral(domain, iterations = 10) {
    const attr = this.get(domain);
    const sequence = [1, 1];

    for (let i = 2; i < iterations; i++) {
      sequence[i] = sequence[i-1] + sequence[i-2];
    }

    return sequence.map((val, i) =>
      i === 0 ? val : sequence[i] / sequence[i-1]
    );
  },

  // Apply attractor-based timing
  timing(operation, domain = 'aesthetic') {
    const base = 1000; // 1 second
    const attr = this.get(domain);

    switch(domain) {
      case 'aesthetic': return Math.floor(base * attr);           // 1618ms (φ)
      case 'growth': return Math.floor(base * this.e);            // 2718ms (e)
      case 'periodic': return Math.floor(base * this.π);          // 3142ms (π)
      case 'scaling': return Math.floor(base * this['√2']);       // 1414ms (√2)
      case 'decay': return Math.floor(base * this.φ_inv);         // 618ms (1/φ)
      default: return base;
    }
  }
};

window.Attractors = Attractors;
```
