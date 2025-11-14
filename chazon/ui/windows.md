# Window Manager
**Multi-Window Support** | Draggable Windows with φ-spacing

Manage multiple windows with golden ratio positioning.

```javascript
const WindowManager = {
  windows: [],
  zIndex: 100,
  φ: (1 + Math.sqrt(5)) / 2,

  create(title, content, opts = {}) {
    const n = this.windows.length * 30;
    const win = document.createElement('div');
    win.className = 'chazon-window';
    win.style.cssText = `
      position:absolute;top:${opts.top || 50 + n}px;left:${opts.left || 50 + n * this.φ}px;
      width:${opts.width || 400}px;height:${opts.height || 300}px;background:#1a1a2e;
      border:2px solid #00ff88;border-radius:8px;box-shadow:0 4px 20px rgba(0,255,136,0.3);
      z-index:${this.zIndex++};
    `;

    win.innerHTML = `
      <div class="title-bar" style="background:#00ff88;color:#000;padding:8px;cursor:move;border-radius:6px 6px 0 0;font-weight:bold;">
        ${title}
        <span style="float:right;cursor:pointer;padding:0 8px;" onclick="this.parentElement.parentElement.style.display='none'">−</span>
        <span style="float:right;cursor:pointer;padding:0 8px;" onclick="this.parentElement.parentElement.remove()">✖</span>
      </div>
      <div class="content" style="padding:15px;height:calc(100% - 38px);overflow:auto;color:#00ff88;">${content}</div>
    `;

    this.makeDraggable(win);
    document.getElementById('chazon-desktop').appendChild(win);
    this.windows.push(win);
    if (window.Taskbar) Taskbar.addApp(title, win);
    return win;
  },

  makeDraggable(win) {
    const titleBar = win.querySelector('.title-bar');
    let pos = {};

    titleBar.onmousedown = e => {
      if (e.target.tagName === 'SPAN') return;
      pos = { x: e.clientX, y: e.clientY, left: win.offsetLeft, top: win.offsetTop };
      document.onmousemove = ev => {
        win.style.left = pos.left + ev.clientX - pos.x + 'px';
        win.style.top = pos.top + ev.clientY - pos.y + 'px';
      };
      document.onmouseup = () => { document.onmousemove = document.onmouseup = null; };
    };
  }
};

window.WindowManager = WindowManager;
```
