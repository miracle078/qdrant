# Calculator
**Mathematical Operations** | ISA-95 L1

Simple calculator with basic operations.

```javascript
const calculator = {
  add: (a, b) => a + b,
  sub: (a, b) => a - b,
  mul: (a, b) => a * b,
  div: (a, b) => b !== 0 ? a / b : 'Error: Div by zero',
  phi: () => (1 + Math.sqrt(5)) / 2
};

console.log('Calculator ready');
console.log('5 + 3 =', calculator.add(5, 3));
console.log('10 - 4 =', calculator.sub(10, 4));
console.log('6 × 7 =', calculator.mul(6, 7));
console.log('20 ÷ 4 =', calculator.div(20, 4));
console.log('φ =', calculator.phi());

return calculator;
```
