/**
 * HMI Navigation System - UUID-based path-independent navigation
 * Enables screens to reference each other by UUID instead of file paths
 */

class HMINavigation {
    constructor() {
        this.registry = null;
        this.baseUrl = this.getBaseUrl();
        this.init();
    }

    /**
     * Get the base URL for the HMI directory
     */
    getBaseUrl() {
        const currentPath = window.location.pathname;
        const hmiIndex = currentPath.indexOf('/HMI/');

        if (hmiIndex !== -1) {
            const basePath = currentPath.substring(0, hmiIndex + 5); // Include '/HMI/'
            return window.location.origin + basePath;
        }

        // Fallback: assume we're in the HMI directory
        const pathParts = currentPath.split('/');
        pathParts.pop(); // Remove current file
        return window.location.origin + pathParts.join('/') + '/';
    }

    /**
     * Initialize the navigation system
     */
    async init() {
        try {
            await this.loadRegistry();
            this.setupNavigationListeners();
        } catch (error) {
            console.error('Failed to initialize HMI Navigation:', error);
        }
    }

    /**
     * Load the screen registry
     */
    async loadRegistry() {
        try {
            const registryPath = this.baseUrl + 'screen-registry.json';
            const response = await fetch(registryPath);

            if (!response.ok) {
                throw new Error(`Failed to load registry: ${response.status}`);
            }

            this.registry = await response.json();
            console.log('HMI Screen Registry loaded:', this.registry.screens);
        } catch (error) {
            console.error('Error loading screen registry:', error);
            // Provide fallback empty registry
            this.registry = { screens: {} };
        }
    }

    /**
     * Navigate to a screen by UUID
     */
    navigateTo(uuid, newWindow = false) {
        if (!this.registry) {
            console.error('Registry not loaded');
            return;
        }

        const screen = this.registry.screens[uuid];

        if (!screen) {
            console.error(`Screen not found: ${uuid}`);
            return;
        }

        const url = this.baseUrl + screen.path;

        if (newWindow) {
            window.open(url, '_blank');
        } else {
            window.location.href = url;
        }
    }

    /**
     * Get screen information by UUID
     */
    getScreen(uuid) {
        if (!this.registry) {
            return null;
        }
        return this.registry.screens[uuid];
    }

    /**
     * Get all screens of a specific type
     */
    getScreensByType(type) {
        if (!this.registry) {
            return [];
        }

        return Object.values(this.registry.screens)
            .filter(screen => screen.type === type);
    }

    /**
     * Get all available screens
     */
    getAllScreens() {
        if (!this.registry) {
            return [];
        }
        return Object.values(this.registry.screens);
    }

    /**
     * Setup automatic navigation for elements with data-nav-uuid attribute
     */
    setupNavigationListeners() {
        document.addEventListener('click', (event) => {
            const element = event.target.closest('[data-nav-uuid]');

            if (element) {
                event.preventDefault();
                const uuid = element.getAttribute('data-nav-uuid');
                const newWindow = element.getAttribute('data-nav-new-window') === 'true';
                this.navigateTo(uuid, newWindow);
            }
        });
    }

    /**
     * Create a navigation link element
     */
    createNavLink(uuid, text, className = '') {
        const screen = this.getScreen(uuid);

        if (!screen) {
            console.error(`Screen not found: ${uuid}`);
            return null;
        }

        const link = document.createElement('a');
        link.href = '#';
        link.textContent = text || screen.name;
        link.className = className;
        link.setAttribute('data-nav-uuid', uuid);
        link.setAttribute('title', screen.description);

        return link;
    }

    /**
     * Build navigation menu from registry
     */
    buildNavigationMenu(containerSelector, options = {}) {
        const container = document.querySelector(containerSelector);

        if (!container) {
            console.error(`Container not found: ${containerSelector}`);
            return;
        }

        const screens = options.type
            ? this.getScreensByType(options.type)
            : this.getAllScreens();

        const menu = document.createElement('ul');
        menu.className = options.menuClass || 'hmi-nav-menu';

        screens.forEach(screen => {
            const li = document.createElement('li');
            const link = this.createNavLink(screen.uuid, screen.name, options.linkClass || '');
            li.appendChild(link);
            menu.appendChild(li);
        });

        container.appendChild(menu);
    }
}

// Create global navigation instance
const hmiNav = new HMINavigation();

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HMINavigation;
}
