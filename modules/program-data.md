# Data Transformer
**Array & Object Operations** | ISA-95 L1

Data transformation using functional programming.

```javascript
const DataTransformer = {
  data: [
    { id: 1, type: 'sensor', value: 42, status: 'ok' },
    { id: 2, type: 'actuator', value: 85, status: 'warning' },
    { id: 3, type: 'sensor', value: 23, status: 'ok' },
    { id: 4, type: 'sensor', value: 91, status: 'critical' }
  ],

  filter(predicate) {
    return this.data.filter(predicate);
  },

  transform(mapper) {
    return this.data.map(mapper);
  },

  aggregate(reducer, initial = 0) {
    return this.data.reduce(reducer, initial);
  }
};

console.log('Data Transformer');
console.log('Sensors:', DataTransformer.filter(d => d.type === 'sensor').length);
console.log('Critical:', DataTransformer.filter(d => d.status === 'critical'));
console.log('Avg Value:', (DataTransformer.aggregate((sum, d) => sum + d.value, 0) / DataTransformer.data.length).toFixed(1));

return DataTransformer;
```
