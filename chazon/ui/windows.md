# Window Manager
**Multi-Window Support** | Draggable, Resizable Windows

Manage multiple windows in desktop environment.

```javascript
const WindowManager = {
  windows: [],
  zIndex: 100,

  create(title, content, opts = {}) {
    const win = document.createElement('div');
    win.className = 'chazon-window';
    win.style.cssText = `
      position:absolute;
      top:${opts.top || 100}px;
      left:${opts.left || 100}px;
      width:${opts.width || 400}px;
      height:${opts.height || 300}px;
      background:#1a1a2e;
      border:2px solid #00ff88;
      z-index:${this.zIndex++};
    `;

    win.innerHTML = `
      <div class="title-bar" style="background:#00ff88;color:#000;padding:5px;cursor:move;">
        ${title}
        <span style="float:right;cursor:pointer;" onclick="this.parentElement.parentElement.remove()">✖</span>
      </div>
      <div class="content" style="padding:10px;height:calc(100% - 30px);overflow:auto;">
        ${content}
      </div>
    `;

    this.makeDraggable(win);
    document.getElementById('chazon-desktop').appendChild(win);
    this.windows.push(win);
    return win;
  },

  makeDraggable(win) {
    const titleBar = win.querySelector('.title-bar');
    let pos = { x: 0, y: 0, left: 0, top: 0 };

    titleBar.onmousedown = e => {
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
