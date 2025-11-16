/**
 * HMI Template Loader - Ignition-style template system
 * Loads and instantiates reusable component and view templates
 */

class HMITemplateLoader {
    constructor() {
        this.templates = {
            components: {},
            views: {},
            base: {}
        };
        this.baseUrl = this.getBaseUrl();
    }

    /**
     * Get the base URL for the HMI directory
     */
    getBaseUrl() {
        const currentPath = window.location.pathname;
        const hmiIndex = currentPath.indexOf('/HMI/');

        if (hmiIndex !== -1) {
            const basePath = currentPath.substring(0, hmiIndex + 5);
            return window.location.origin + basePath;
        }

        const pathParts = currentPath.split('/');
        pathParts.pop();
        return window.location.origin + pathParts.join('/') + '/';
    }

    /**
     * Load a template by type and name
     */
    async loadTemplate(type, name) {
        const cacheKey = `${type}:${name}`;

        // Check cache first
        if (this.templates[type] && this.templates[type][name]) {
            return this.templates[type][name];
        }

        try {
            const templatePath = `${this.baseUrl}templates/${type}/${name}.json`;
            const response = await fetch(templatePath);

            if (!response.ok) {
                throw new Error(`Template not found: ${type}/${name}`);
            }

            const template = await response.json();

            // Cache the template
            if (!this.templates[type]) {
                this.templates[type] = {};
            }
            this.templates[type][name] = template;

            return template;
        } catch (error) {
            console.error(`Error loading template ${type}/${name}:`, error);
            return null;
        }
    }

    /**
     * Instantiate a template with parameters
     */
    instantiateTemplate(templateDef, parameters = {}) {
        if (!templateDef || !templateDef.template) {
            console.error('Invalid template definition');
            return null;
        }

        // Merge parameters with defaults
        const params = this.mergeParameters(templateDef.parameters, parameters);

        // Validate required parameters
        const validation = this.validateParameters(templateDef.parameters, params);
        if (!validation.valid) {
            console.error('Template parameter validation failed:', validation.errors);
            return null;
        }

        // Clone the template
        const instance = JSON.parse(JSON.stringify(templateDef.template));

        // Replace parameter placeholders
        this.replaceParameters(instance, params);

        return instance;
    }

    /**
     * Merge provided parameters with template defaults
     */
    mergeParameters(parameterDefs, provided) {
        const merged = {};

        if (!parameterDefs) {
            return provided;
        }

        // Set defaults and merge provided values
        Object.keys(parameterDefs).forEach(key => {
            const def = parameterDefs[key];

            if (provided.hasOwnProperty(key)) {
                merged[key] = provided[key];
            } else if (def.default !== undefined) {
                merged[key] = def.default;
            }
        });

        return merged;
    }

    /**
     * Validate parameters against template definition
     */
    validateParameters(parameterDefs, parameters) {
        const errors = [];

        if (!parameterDefs) {
            return { valid: true, errors: [] };
        }

        Object.keys(parameterDefs).forEach(key => {
            const def = parameterDefs[key];

            // Check required parameters
            if (def.required && !parameters.hasOwnProperty(key)) {
                errors.push(`Required parameter missing: ${key}`);
            }

            // Check enum values
            if (def.enum && parameters[key]) {
                if (!def.enum.includes(parameters[key])) {
                    errors.push(`Invalid value for ${key}. Must be one of: ${def.enum.join(', ')}`);
                }
            }

            // Type checking could be added here
        });

        return {
            valid: errors.length === 0,
            errors: errors
        };
    }

    /**
     * Replace parameter placeholders in template object
     */
    replaceParameters(obj, parameters) {
        if (typeof obj === 'string') {
            return this.replaceStringParameters(obj, parameters);
        }

        if (Array.isArray(obj)) {
            for (let i = 0; i < obj.length; i++) {
                obj[i] = this.replaceParameters(obj[i], parameters);
            }
            return obj;
        }

        if (obj !== null && typeof obj === 'object') {
            for (const key in obj) {
                obj[key] = this.replaceParameters(obj[key], parameters);
            }
        }

        return obj;
    }

    /**
     * Replace parameter placeholders in string
     */
    replaceStringParameters(str, parameters) {
        if (typeof str !== 'string') {
            return str;
        }

        // Replace {paramName} style placeholders
        return str.replace(/\{([^}]+)\}/g, (match, expr) => {
            try {
                // Handle simple parameter references
                if (parameters.hasOwnProperty(expr)) {
                    return parameters[expr];
                }

                // Handle expressions (e.g., {value > 10 ? 'high' : 'low'})
                // Create a safe eval context with only the parameters
                const func = new Function(...Object.keys(parameters), `return ${expr}`);
                return func(...Object.values(parameters));
            } catch (error) {
                console.warn(`Error evaluating expression: ${expr}`, error);
                return match; // Return original if evaluation fails
            }
        });
    }

    /**
     * Create a component instance from template
     */
    async createComponent(componentName, parameters = {}) {
        const template = await this.loadTemplate('components', componentName);

        if (!template) {
            console.error(`Component template not found: ${componentName}`);
            return null;
        }

        return this.instantiateTemplate(template, parameters);
    }

    /**
     * Create a view instance from template
     */
    async createView(viewName, parameters = {}, content = []) {
        const template = await this.loadTemplate('views', viewName);

        if (!template) {
            console.error(`View template not found: ${viewName}`);
            return null;
        }

        const instance = this.instantiateTemplate(template, parameters);

        // Inject content into content slot if specified
        if (content.length > 0 && instance) {
            this.injectContent(instance, content);
        }

        return instance;
    }

    /**
     * Create a view based on base template
     */
    async createBaseView(baseName, parameters = {}, content = []) {
        const template = await this.loadTemplate('base', baseName);

        if (!template) {
            console.error(`Base template not found: ${baseName}`);
            return null;
        }

        const instance = this.instantiateTemplate(template, parameters);

        // Find and populate content slot
        if (content.length > 0 && instance) {
            this.injectContent(instance, content);
        }

        return instance;
    }

    /**
     * Inject content into template content slot
     */
    injectContent(template, content) {
        // Find the content slot (marked with custom.slot === 'content')
        const slot = this.findContentSlot(template);

        if (slot && Array.isArray(slot.children)) {
            slot.children.push(...content);
        }
    }

    /**
     * Find content slot in template recursively
     */
    findContentSlot(obj) {
        if (!obj || typeof obj !== 'object') {
            return null;
        }

        // Check if this is the content slot
        if (obj.custom && obj.custom.slot === 'content') {
            return obj;
        }

        // Check children
        if (Array.isArray(obj.children)) {
            for (const child of obj.children) {
                const found = this.findContentSlot(child);
                if (found) {
                    return found;
                }
            }
        }

        return null;
    }

    /**
     * Preload commonly used templates
     */
    async preloadCommonTemplates() {
        const commonComponents = [
            'NavigationButton',
            'StatusIndicator',
            'ValueDisplay',
            'EquipmentCard'
        ];

        const commonBases = [
            'BaseView'
        ];

        const promises = [
            ...commonComponents.map(name => this.loadTemplate('components', name)),
            ...commonBases.map(name => this.loadTemplate('base', name))
        ];

        await Promise.all(promises);
        console.log('Common templates preloaded');
    }

    /**
     * Get all loaded templates of a type
     */
    getLoadedTemplates(type) {
        return this.templates[type] || {};
    }

    /**
     * Clear template cache
     */
    clearCache() {
        this.templates = {
            components: {},
            views: {},
            base: {}
        };
    }
}

// Create global template loader instance
const hmiTemplates = new HMITemplateLoader();

// Preload common templates on page load
document.addEventListener('DOMContentLoaded', () => {
    hmiTemplates.preloadCommonTemplates();
});

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HMITemplateLoader;
}
