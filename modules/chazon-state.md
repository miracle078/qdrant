# State Manager
**φ-Balanced Storage** | ISA-95 L1: Basic Control

Persistent state management with localStorage. φ-optimized caching.

```javascript
const StateManager = {
  φ: 1.618,
  prefix: 'chazon:',
  maxItems: 161,

  set(key, value) {
    try {
      const fullKey = this.prefix + key;
      const data = JSON.stringify({ value, time: Date.now() });
      localStorage.setItem(fullKey, data);
      this.cleanup();
      return true;
    } catch (err) {
      console.warn('State save failed:', err.message);
      return false;
    }
  },

  get(key, defaultVal = null) {
    try {
      const fullKey = this.prefix + key;
      const data = localStorage.getItem(fullKey);
      if (!data) return defaultVal;
      return JSON.parse(data).value;
    } catch (err) {
      return defaultVal;
    }
  },

  remove(key) {
    localStorage.removeItem(this.prefix + key);
  },

  clear() {
    Object.keys(localStorage)
      .filter(k => k.startsWith(this.prefix))
      .forEach(k => localStorage.removeItem(k));
  },

  cleanup() {
    const items = Object.keys(localStorage)
      .filter(k => k.startsWith(this.prefix))
      .map(k => ({ key: k, time: JSON.parse(localStorage[k]).time }))
      .sort((a, b) => b.time - a.time);

    if (items.length > this.maxItems) {
      items.slice(this.maxItems).forEach(item => localStorage.removeItem(item.key));
    }
  },

  size() {
    return Object.keys(localStorage).filter(k => k.startsWith(this.prefix)).length;
  }
};

window.StateManager = StateManager;
```
