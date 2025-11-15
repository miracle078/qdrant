# Main Navigation Component
**Top Navigation** | Menu Links

```javascript
const NavMain = (links = []) => {
  const defaultLinks = [
    { href: '/', text: '🏠 Home' },
    { href: '/dashboard.html', text: '🚀 Dashboard' },
    { href: '/chazon.html', text: '🌌 Chazon OS' },
    { href: '/docs/', text: '📚 Docs' }
  ];

  const menuLinks = (links.length ? links : defaultLinks)
    .map(l => `<a href="${l.href}">${l.text}</a>`)
    .join(' | ');

  return `
<nav style="background: rgba(0,0,0,0.9); padding: 15px; border-bottom: 2px solid #00ff88; position: sticky; top: 0; z-index: 100;">
  <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center;">
    <div style="font-size: 1.2em; color: #00ccff; font-weight: bold;">חזון CHAZON</div>
    <div style="display: flex; gap: 20px; font-size: 0.9em;">${menuLinks}</div>
  </div>
</nav>`;
};

return NavMain();
```
