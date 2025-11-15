# Irrational Attractor Demo
**Dynamical Systems** | ISA-95 L0

Demonstrate multi-irrational attractor system with equilibrium convergence.

```javascript
console.log('🌀 Irrational Attractor System Demo\n');

// 1. Initialize attractors
console.log('1️⃣ Irrational Constants:');
console.log(`   φ (phi) = ${Attractors.φ.toFixed(6)} - Golden ratio`);
console.log(`   1/φ     = ${Attractors.φ_inv.toFixed(6)} - Inverse phi`);
console.log(`   e       = ${Attractors.e.toFixed(6)} - Euler's number`);
console.log(`   π       = ${Attractors.π.toFixed(6)} - Pi`);
console.log(`   √2      = ${Attractors['√2'].toFixed(6)} - Root 2`);
console.log(`   √3      = ${Attractors['√3'].toFixed(6)} - Root 3`);
console.log(`   √5      = ${Attractors['√5'].toFixed(6)} - Root 5`);

// 2. Domain mappings
console.log('\n2️⃣ Attractor Domains:');
Object.entries(Attractors.domains).forEach(([domain, attractor]) => {
  const value = Attractors.get(domain);
  console.log(`   ${domain.padEnd(12)} → ${attractor.padEnd(5)} = ${value.toFixed(3)}`);
});

// 3. Timing examples
console.log('\n3️⃣ Attractor-Based Timing:');
['aesthetic', 'growth', 'periodic', 'decay'].forEach(domain => {
  const timing = Attractors.timing(null, domain);
  console.log(`   ${domain.padEnd(12)} → ${timing}ms`);
});

// 4. Fibonacci spiral convergence to φ
console.log('\n4️⃣ Spiral Convergence to φ:');
const spiral = Attractors.spiral('aesthetic', 10);
spiral.forEach((ratio, i) => {
  if (i > 0) {
    const error = Math.abs(ratio - Attractors.φ);
    console.log(`   F${i}/F${i-1} = ${ratio.toFixed(6)} (error: ${error.toFixed(6)})`);
  }
});

// 5. Initialize equilibrium
console.log('\n5️⃣ Dynamic Equilibrium:');
Equilibrium.init();
console.log(`   UI spacing: ${Equilibrium.state.ui.spacing.toFixed(2)}px`);
console.log(`   Cache growth: e^4 = ${Equilibrium.state.performance.cacheGrowth.toFixed(2)} items`);
console.log(`   Rotation speed: π/100 = ${Equilibrium.state.animation.rotationSpeed.toFixed(4)} rad/frame`);
console.log(`   Network timeout: 1000/φ = ${Equilibrium.state.network.timeout.toFixed(2)}ms`);

// 6. Balance demonstration
console.log('\n6️⃣ Golden Section Balance:');
const balanced = Equilibrium.balance(100, 61.8);
console.log(`   Total: 161.8 → Primary: ${balanced.primary.toFixed(2)} (61.8%)`);
console.log(`                → Secondary: ${balanced.secondary.toFixed(2)} (38.2%)`);

// 7. Convergence test
console.log('\n7️⃣ Convergence to Attractor:');
let value = 1.0;
console.log(`   Initial value: ${value.toFixed(6)}`);
for (let i = 0; i < 5; i++) {
  value = Equilibrium.converge(value, Attractors.φ, Attractors.φ, 0.2);
  console.log(`   Iteration ${i+1}: ${value.toFixed(6)}`);
}

// 8. Resonance detection
console.log('\n8️⃣ Harmonic Resonance:');
[Math.PI, 2*Math.PI, 3*Math.PI, 3.5].forEach(freq => {
  const resonant = Equilibrium.isResonant(freq);
  console.log(`   ${freq.toFixed(3)} Hz → ${resonant ? '✓ Resonant' : '✗ Not resonant'}`);
});

console.log('\n✅ Attractor demo complete!');

return {
  success: true,
  attractors: Object.keys(Attractors).filter(k => typeof Attractors[k] === 'number').length,
  domains: Object.keys(Attractors.domains).length,
  φ: Attractors.φ,
  converged: Math.abs(value - Attractors.φ) < 0.01
};
```
