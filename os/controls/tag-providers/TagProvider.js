/**
 * Tag Provider System
 * Centralized tag management for SCADA/HMI interfaces
 * Modeled after Ignition SCADA tag providers
 */

class TagProvider {
  constructor() {
    this.providers = {}; // Loaded providers
    this.subscriptions = {}; // Tag subscriptions
    this.history = {}; // Historical data
    this.historyLimit = 1000; // Max history points per tag
  }

  /**
   * Load a tag provider from JSON
   * @param {string} name - Provider name (e.g., 'frontend', 'backend')
   */
  async loadProvider(name) {
    try {
      const response = await fetch(`tag-providers/${name}.json`);
      if (!response.ok) {
        throw new Error(`Failed to load provider: ${name}`);
      }
      const data = await response.json();
      this.providers[name] = data;
      console.log(`[TagProvider] Loaded provider: ${name}`);
      return data;
    } catch (error) {
      console.error(`[TagProvider] Error loading ${name}:`, error);
      return null;
    }
  }

  /**
   * Load all providers
   */
  async loadAll() {
    const providers = [
      'frontend', 'backend', 'modules', 'boot',
      'models', 'data', 'language', 'medical'
    ];

    const promises = providers.map(name => this.loadProvider(name));
    await Promise.all(promises);
    console.log('[TagProvider] All providers loaded');
  }

  /**
   * Read tag value
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @returns {any} Tag value or undefined
   */
  read(provider, tagName) {
    const data = this.providers[provider];
    if (!data) {
      console.warn(`[TagProvider] Provider not found: ${provider}`);
      return undefined;
    }

    const tag = data.tags[tagName];
    if (!tag) {
      console.warn(`[TagProvider] Tag not found: ${provider}.${tagName}`);
      return undefined;
    }

    return tag.value;
  }

  /**
   * Read tag with full metadata
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @returns {object} Full tag object
   */
  readFull(provider, tagName) {
    const data = this.providers[provider];
    return data?.tags[tagName];
  }

  /**
   * Write tag value
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @param {any} value - New value
   * @param {string} quality - Quality code (GOOD, BAD, UNCERTAIN)
   */
  write(provider, tagName, value, quality = 'GOOD') {
    const data = this.providers[provider];
    if (!data) {
      console.warn(`[TagProvider] Provider not found: ${provider}`);
      return;
    }

    const tag = data.tags[tagName];
    if (!tag) {
      console.warn(`[TagProvider] Tag not found: ${provider}.${tagName}`);
      return;
    }

    // Update tag
    const oldValue = tag.value;
    tag.value = value;
    tag.quality = quality;
    tag.timestamp = new Date().toISOString();

    // Store history
    this.addHistory(provider, tagName, value, quality);

    // Notify subscribers
    this.notifySubscribers(provider, tagName, value, oldValue);

    console.log(`[TagProvider] ${provider}.${tagName} = ${value}`);
  }

  /**
   * Subscribe to tag changes
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @param {function} callback - Callback function(newValue, oldValue)
   */
  subscribe(provider, tagName, callback) {
    const key = `${provider}.${tagName}`;
    if (!this.subscriptions[key]) {
      this.subscriptions[key] = [];
    }
    this.subscriptions[key].push(callback);
    console.log(`[TagProvider] Subscribed to ${key}`);
  }

  /**
   * Unsubscribe from tag changes
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @param {function} callback - Callback function to remove
   */
  unsubscribe(provider, tagName, callback) {
    const key = `${provider}.${tagName}`;
    if (this.subscriptions[key]) {
      this.subscriptions[key] = this.subscriptions[key].filter(cb => cb !== callback);
    }
  }

  /**
   * Notify all subscribers of tag change
   * @private
   */
  notifySubscribers(provider, tagName, newValue, oldValue) {
    const key = `${provider}.${tagName}`;
    const callbacks = this.subscriptions[key] || [];
    callbacks.forEach(callback => {
      try {
        callback(newValue, oldValue);
      } catch (error) {
        console.error(`[TagProvider] Subscription callback error:`, error);
      }
    });
  }

  /**
   * Add value to tag history
   * @private
   */
  addHistory(provider, tagName, value, quality) {
    const key = `${provider}.${tagName}`;
    if (!this.history[key]) {
      this.history[key] = [];
    }

    this.history[key].push({
      value,
      quality,
      timestamp: new Date().toISOString()
    });

    // Limit history size
    if (this.history[key].length > this.historyLimit) {
      this.history[key].shift();
    }
  }

  /**
   * Get tag history
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @param {number} limit - Max number of points
   * @returns {array} History points
   */
  getHistory(provider, tagName, limit = 100) {
    const key = `${provider}.${tagName}`;
    const history = this.history[key] || [];
    return history.slice(-limit);
  }

  /**
   * Get all tags from a provider
   * @param {string} provider - Provider name
   * @returns {object} All tags
   */
  getAll(provider) {
    return this.providers[provider]?.tags || {};
  }

  /**
   * List all loaded providers
   * @returns {array} Provider names
   */
  listProviders() {
    return Object.keys(this.providers);
  }

  /**
   * List all tags in a provider
   * @param {string} provider - Provider name
   * @returns {array} Tag names
   */
  listTags(provider) {
    const data = this.providers[provider];
    return data ? Object.keys(data.tags) : [];
  }

  /**
   * Bind tag to DOM element (auto-update)
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @param {string} elementId - DOM element ID
   * @param {function} formatter - Optional value formatter
   */
  bind(provider, tagName, elementId, formatter = null) {
    const element = document.getElementById(elementId);
    if (!element) {
      console.warn(`[TagProvider] Element not found: ${elementId}`);
      return;
    }

    // Initial value
    const value = this.read(provider, tagName);
    element.textContent = formatter ? formatter(value) : value;

    // Subscribe to updates
    this.subscribe(provider, tagName, (newValue) => {
      element.textContent = formatter ? formatter(newValue) : newValue;
    });
  }

  /**
   * Batch read multiple tags
   * @param {array} tags - Array of {provider, tagName}
   * @returns {object} Values keyed by 'provider.tagName'
   */
  readBatch(tags) {
    const result = {};
    tags.forEach(({ provider, tagName }) => {
      const key = `${provider}.${tagName}`;
      result[key] = this.read(provider, tagName);
    });
    return result;
  }

  /**
   * Create a new tag dynamically
   * @param {string} provider - Provider name
   * @param {string} tagName - Tag name
   * @param {object} tagConfig - Tag configuration
   */
  createTag(provider, tagName, tagConfig) {
    const data = this.providers[provider];
    if (!data) {
      console.warn(`[TagProvider] Provider not found: ${provider}`);
      return;
    }

    data.tags[tagName] = {
      value: tagConfig.value || null,
      type: tagConfig.type || 'string',
      quality: tagConfig.quality || 'GOOD',
      timestamp: new Date().toISOString(),
      ...tagConfig
    };

    console.log(`[TagProvider] Created tag: ${provider}.${tagName}`);
  }
}

// Global instance
window.TagProvider = new TagProvider();

// Export for modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = TagProvider;
}
