# Desktop Icons
**Icon System** | Draggable Desktop Icons

Create and manage desktop icons with φ-balanced spacing.

```javascript
const IconManager = {
  icons: [],
  φ: (1 + Math.sqrt(5)) / 2,

  create(name, emoji, action) {
    const icon = document.createElement('div');
    icon.className = 'desktop-icon';
    icon.style.cssText = `
      position:absolute;width:80px;text-align:center;cursor:pointer;
      padding:10px;border-radius:5px;transition:background 0.2s;
    `;
    icon.innerHTML = `<div style="font-size:40px;">${emoji}</div><div style="font-size:12px;margin-top:5px;">${name}</div>`;

    icon.onmouseenter = () => icon.style.background = 'rgba(0,255,136,0.1)';
    icon.onmouseleave = () => icon.style.background = 'transparent';
    icon.onclick = action;

    const desktop = document.getElementById('chazon-desktop');
    const row = Math.floor(this.icons.length / 5);
    const col = this.icons.length % 5;
    icon.style.top = `${20 + row * 100 * this.φ}px`;
    icon.style.left = `${20 + col * 100}px`;

    desktop.appendChild(icon);
    this.icons.push(icon);
    return icon;
  }
};

window.IconManager = IconManager;
```
