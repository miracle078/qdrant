# Landing Page Definition
**Page Assembly Config** | Component References

```yaml
---
title: Chazon OS + AutomationGPT
components:
  head: head-default
  nav: nav-main
  content: landing-hero
  footer: footer-default
params:
  showDashboardButton: true
  projectCount: 3
---
```

Page configuration for assembling the landing page from components.

```javascript
const LandingPage = {
  config: {
    title: 'Chazon OS + AutomationGPT',
    components: {
      head: 'head-default',
      nav: 'nav-main',
      content: 'landing-hero',
      footer: 'footer-default'
    },
    params: {
      showDashboardButton: true,
      projectCount: 3
    }
  },

  async render() {
    window.pageTitle = this.config.title;
    return await PageBuilder.build(this.config);
  }
};

window.LandingPage = LandingPage;
```
