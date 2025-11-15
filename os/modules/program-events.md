# Event System
**Event-Driven Architecture** | ISA-95 L2

Custom event bus for publish-subscribe messaging.

```javascript
const EventBus = {
  listeners: {},

  on(event, callback) {
    if (!this.listeners[event]) this.listeners[event] = [];
    this.listeners[event].push(callback);
    console.log(`Registered: ${event}`);
  },

  emit(event, data) {
    console.log(`Event: ${event}`, data);
    const handlers = this.listeners[event] || [];
    handlers.forEach(cb => cb(data));
  },

  off(event) {
    delete this.listeners[event];
  }
};

// Demo: ISA alarm system
EventBus.on('alarm', (alarm) => {
  console.log(`ALARM [${alarm.level}]: ${alarm.message}`);
});

EventBus.on('data', (data) => {
  console.log(`Data received: ${data.value}`);
});

EventBus.emit('alarm', { level: 'HIGH', message: 'Temperature limit exceeded' });
EventBus.emit('data', { sensor: 'temp-01', value: 95 });

return EventBus;
```
