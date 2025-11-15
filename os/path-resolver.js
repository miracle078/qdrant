/**
 * Path Resolver for GitHub Pages
 * Automatically detects environment and resolves paths correctly
 */

(function() {
  // Detect if we're on GitHub Pages
  const isGitHubPages = window.location.hostname.includes('github.io');
  const repoName = 'qdrant';

  // Set base path
  window.BASE_PATH = isGitHubPages ? `/${repoName}` : '';

  /**
   * Resolve path relative to base
   * @param {string} path - Path to resolve
   * @returns {string} - Resolved path
   */
  window.resolvePath = function(path) {
    // Remove leading slash if present
    const cleanPath = path.startsWith('/') ? path.substring(1) : path;
    return `${window.BASE_PATH}/${cleanPath}`;
  };

  /**
   * Navigate to path
   * @param {string} path - Path to navigate to
   */
  window.navigateTo = function(path) {
    window.location.href = resolvePath(path);
  };

  /**
   * Get current area from path
   * @returns {string} - Current area ID (e.g., 'modules', 'boot')
   */
  window.getCurrentArea = function() {
    const path = window.location.pathname;
    const match = path.match(/\/os\/([^\/]+)\//);
    return match ? match[1] : null;
  };

  /**
   * Get breadcrumb links
   * @returns {Array} - Array of {label, path} objects
   */
  window.getBreadcrumbs = function() {
    const path = window.location.pathname;
    const breadcrumbs = [
      { label: 'Home', path: '' }
    ];

    if (path.includes('/os/')) {
      breadcrumbs.push({ label: 'Chazon OS', path: 'os/' });

      const area = getCurrentArea();
      if (area) {
        // Capitalize first letter
        const areaLabel = area.charAt(0).toUpperCase() + area.slice(1);
        breadcrumbs.push({ label: areaLabel, path: `os/${area}/` });
      }
    }

    return breadcrumbs;
  };

  console.log('Path Resolver initialized:', {
    isGitHubPages,
    basePath: window.BASE_PATH,
    currentArea: getCurrentArea()
  });
})();
