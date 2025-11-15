# Dashboard Page Definition
**Unified Interface** | Tab Navigation

```yaml
---
title: Chazon Unified Dashboard
components:
  head: head-dashboard
  nav: nav-tabs
  content: dashboard-frame
params:
  tabs:
    - { id: 'chazon', title: 'Chazon OS', src: 'chazon.html' }
    - { id: 'isaos', title: 'ISA-OS', src: 'isa-os.html' }
    - { id: 'automation', title: 'AutomationGPT', src: 'automationgpt.html' }
    - { id: 'docs', title: 'Documentation', src: 'docs/index.html' }
---
```

Unified dashboard with tabbed interface for all demos.

```javascript
const DashboardPage = {
  config: {
    title: 'Chazon Unified Dashboard',
    components: {
      head: 'head-dashboard',
      nav: 'nav-tabs',
      content: 'dashboard-frame'
    },
    params: {
      tabs: [
        { id: 'chazon', title: 'Chazon OS', src: 'chazon.html' },
        { id: 'isaos', title: 'ISA-OS', src: 'isa-os.html' },
        { id: 'automation', title: 'AutomationGPT', src: 'automationgpt.html' },
        { id: 'docs', title: 'Documentation', src: 'docs/index.html' }
      ]
    }
  },

  async render() {
    window.pageTitle = this.config.title;
    window.dashboardTabs = this.config.params.tabs;
    return await PageBuilder.build(this.config);
  }
};

window.DashboardPage = DashboardPage;
```
