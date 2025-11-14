# Taskbar
**Enhanced Taskbar** | App Launcher & Window Switcher

φ-balanced taskbar with app management.

```javascript
const Taskbar = {
  apps: [],

  init() {
    const bar = document.createElement('div');
    bar.id = 'taskbar';
    bar.style.cssText = `
      position:fixed;bottom:0;width:100%;height:40px;
      background:#0a0a0a;border-top:2px solid #00ff88;
      display:flex;align-items:center;padding:0 10px;z-index:1000;
    `;
    bar.innerHTML = `
      <button onclick="Taskbar.showMenu()" style="background:#00ff88;color:#000;border:none;padding:5px 10px;cursor:pointer;margin-right:10px;">☰</button>
      <span id="taskbar-title">🌌 Chazon OS | חזון | φ=1.618</span>
      <div id="taskbar-apps" style="flex:1;display:flex;gap:5px;margin-left:10px;"></div>
      <span id="taskbar-clock" style="margin-left:auto;"></span>
    `;
    document.getElementById('chazon-desktop').appendChild(bar);
    this.updateClock();
    setInterval(() => this.updateClock(), 1000);
  },

  addApp(name, win) {
    const btn = document.createElement('button');
    btn.textContent = name;
    btn.style.cssText = 'background:#00ff88;color:#000;border:none;padding:5px 10px;cursor:pointer;font-size:11px;';
    btn.onclick = () => win.style.display = win.style.display === 'none' ? 'block' : 'none';
    document.getElementById('taskbar-apps').appendChild(btn);
  },

  updateClock() {
    const clock = document.getElementById('taskbar-clock');
    if (clock) clock.textContent = new Date().toLocaleTimeString();
  },

  showMenu() {
    alert('🌌 Chazon OS\n\nApps:\n• Terminal\n• Calculator\n• Neural Net\n• Search');
  }
};

window.Taskbar = Taskbar;
```
