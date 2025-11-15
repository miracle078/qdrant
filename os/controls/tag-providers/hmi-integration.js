/**
 * HMI Tag Integration Helper
 * Automatically loads and binds tags to HMI pages
 */

class HMITagIntegration {
  constructor() {
    this.area = null;
    this.updateInterval = 2000; // Update every 2 seconds
    this.intervalId = null;
  }

  /**
   * Initialize tag integration for current area
   * @param {string} areaName - Area name (boot, data, frontend, etc.)
   */
  async init(areaName) {
    this.area = areaName;
    console.log(`[HMI] Initializing tag integration for: ${areaName}`);

    // Load tag provider
    await window.TagProvider.loadProvider(areaName);

    // Auto-bind tags to DOM elements
    this.autoBind();

    // Start live updates
    this.startLiveUpdates();

    console.log(`[HMI] Tag integration complete for: ${areaName}`);
  }

  /**
   * Automatically bind tags to DOM elements
   * Uses data-tag attribute: <span data-tag="status"></span>
   */
  autoBind() {
    const elements = document.querySelectorAll('[data-tag]');
    console.log(`[HMI] Auto-binding ${elements.length} tags`);

    elements.forEach(el => {
      const tagName = el.getAttribute('data-tag');
      const formatter = el.getAttribute('data-format');

      // Bind tag to element
      window.TagProvider.bind(
        this.area,
        tagName,
        el.id || this.generateId(el, tagName),
        formatter ? this.getFormatter(formatter) : null
      );
    });
  }

  /**
   * Generate ID for element if it doesn't have one
   */
  generateId(element, tagName) {
    const id = `tag-${tagName}-${Date.now()}`;
    element.id = id;
    return id;
  }

  /**
   * Get formatter function by name
   */
  getFormatter(name) {
    const formatters = {
      'percent': (v) => `${v}%`,
      'ms': (v) => `${v}ms`,
      'sec': (v) => `${v}s`,
      'mb': (v) => `${v}MB`,
      'count': (v) => v.toLocaleString(),
      'bool': (v) => v ? 'ON' : 'OFF',
      'updown': (v) => v ? '▲' : '▼'
    };
    return formatters[name] || ((v) => v);
  }

  /**
   * Start live tag updates (simulated)
   */
  startLiveUpdates() {
    this.intervalId = setInterval(() => {
      this.simulateUpdates();
    }, this.updateInterval);
  }

  /**
   * Stop live updates
   */
  stopLiveUpdates() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  /**
   * Simulate tag value changes (for demo)
   * In production, this would come from WebSocket/MQTT
   */
  simulateUpdates() {
    const tags = window.TagProvider.listTags(this.area);

    // Randomly update some tags
    tags.forEach(tagName => {
      if (Math.random() > 0.7) { // 30% chance
        const tag = window.TagProvider.readFull(this.area, tagName);
        let newValue;

        switch (tag.type) {
          case 'number':
            // Vary by ±10%
            const variance = tag.value * 0.1;
            newValue = tag.value + (Math.random() * variance * 2 - variance);
            newValue = Math.max(0, Math.round(newValue * 100) / 100);
            break;

          case 'boolean':
            // Random flip (rare)
            if (Math.random() > 0.95) {
              newValue = !tag.value;
            }
            break;

          case 'string':
            // Don't change strings randomly
            break;

          default:
            newValue = tag.value;
        }

        if (newValue !== undefined && newValue !== tag.value) {
          window.TagProvider.write(this.area, tagName, newValue);
        }
      }
    });
  }

  /**
   * Manually bind specific tags to specific elements
   * @param {array} bindings - Array of {tag, elementId, formatter}
   */
  bindTags(bindings) {
    bindings.forEach(({ tag, elementId, formatter }) => {
      window.TagProvider.bind(
        this.area,
        tag,
        elementId,
        formatter ? this.getFormatter(formatter) : null
      );
    });
  }

  /**
   * Read tag value
   */
  read(tagName) {
    return window.TagProvider.read(this.area, tagName);
  }

  /**
   * Write tag value
   */
  write(tagName, value) {
    window.TagProvider.write(this.area, tagName, value);
  }

  /**
   * Subscribe to tag changes
   */
  subscribe(tagName, callback) {
    window.TagProvider.subscribe(this.area, tagName, callback);
  }
}

// Global instance
window.HMITagIntegration = new HMITagIntegration();

// Auto-initialize if area is specified in URL or meta tag
document.addEventListener('DOMContentLoaded', () => {
  const areaMeta = document.querySelector('meta[name="hmi-area"]');
  if (areaMeta) {
    const area = areaMeta.getAttribute('content');
    window.HMITagIntegration.init(area);
  }
});
