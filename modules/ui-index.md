# Chazon UI System
**Desktop Environment** | φ-Balanced Interface

Complete UI system integrating all components.

```javascript
const ChazonUISystem = {
  init() {
    console.log('🖥️ Initializing Chazon UI System');

    // Initialize core desktop
    if (window.ChazonUI) ChazonUI.init();

    // Initialize taskbar
    if (window.Taskbar) Taskbar.init();

    // Apply theme
    if (window.ThemeSystem) ThemeSystem.apply();

    // Create default icons
    if (window.IconManager) {
      IconManager.create('Terminal', '💻', () => {
        WindowManager.create('Terminal', '<div style="background:#000;padding:10px;font-family:monospace;">chazon@os:~$ _</div>', {width:600,height:400});
      });
      IconManager.create('Calculator', '🔢', () => {
        WindowManager.create('Calculator', '<input type="text" style="width:100%;font-size:24px;padding:10px;">');
      });
      IconManager.create('Settings', '⚙️', () => {
        WindowManager.create('Settings', '<button onclick="ThemeSystem.cycle()">🎨 Change Theme</button>');
      });
      IconManager.create('Files', '📁', () => {
        WindowManager.create('Files', '<div>📄 hello.md<br>📄 calculator.md<br>📄 neural.md</div>');
      });
    }

    console.log('✅ UI System ready | φ=' + ((1+Math.sqrt(5))/2).toFixed(3));
  }
};

window.ChazonUISystem = ChazonUISystem;

// Auto-initialize if desktop exists
if (document.getElementById('chazon-desktop')) {
  ChazonUISystem.init();
}
```
