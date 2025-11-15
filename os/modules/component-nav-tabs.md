# Tab Navigation Component
**Dashboard Tabs** | Dynamic Switching

```javascript
const NavTabs = () => {
  const tabs = window.dashboardTabs || [
    { id: 'chazon', title: 'Chazon OS' },
    { id: 'isaos', title: 'ISA-OS' },
    { id: 'automation', title: 'AutomationGPT' },
    { id: 'docs', title: 'Documentation' }
  ];

  return `
<div id="topnav">
  <div class="logo">🌌 CHAZON</div>
  <div class="nav-tabs">
    ${tabs.map((tab, i) => `
      <button class="tab ${i === 0 ? 'active' : ''}" onclick="switchTab('${tab.id}')">
        ${tab.title}
      </button>
    `).join('')}
  </div>
  <div class="status">
    <span id="current-mode">${tabs[0].title}</span>
  </div>
</div>`;
};

return NavTabs();
```
