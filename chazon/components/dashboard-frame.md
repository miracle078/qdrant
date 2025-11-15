# Dashboard Frame Component
**Content Panels** | Tab Content

```javascript
const DashboardFrame = () => {
  const tabs = window.dashboardTabs || [];

  const panels = tabs.map((tab, i) => `
    <div id="${tab.id}-panel" class="content ${i === 0 ? 'active' : ''}">
      <iframe src="${tab.src}" title="${tab.title}"></iframe>
    </div>
  `).join('\n');

  const script = `
<script>
function switchTab(name) {
  document.querySelectorAll('.content').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));

  document.getElementById(name + '-panel').classList.add('active');
  event.target.classList.add('active');

  const tab = window.dashboardTabs.find(t => t.id === name);
  document.getElementById('current-mode').textContent = tab.title;
}

document.addEventListener('keydown', (e) => {
  if(e.ctrlKey && e.key >= '1' && e.key <= '4') {
    e.preventDefault();
    const tabs = window.dashboardTabs || [];
    switchTab(tabs[parseInt(e.key) - 1].id);
  }
});
</script>`;

  return panels + script;
};

return DashboardFrame();
```
