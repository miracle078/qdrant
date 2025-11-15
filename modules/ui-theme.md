# Theme System
**φ-Balanced Colors** | Golden Ratio Design

Color themes based on golden ratio aesthetics.

```javascript
const ThemeSystem = {
  φ: (1 + Math.sqrt(5)) / 2,

  themes: {
    default: {
      bg: 'linear-gradient(135deg,#0a0a0a,#1a1a2e)',
      primary: '#00ff88',
      secondary: '#00cc66',
      text: '#00ff88',
      dark: '#0a0a0a'
    },
    blue: {
      bg: 'linear-gradient(135deg,#0a0a1a,#1a1a3e)',
      primary: '#0088ff',
      secondary: '#0066cc',
      text: '#00aaff',
      dark: '#0a0a1a'
    },
    purple: {
      bg: 'linear-gradient(135deg,#1a0a1a,#2e1a3e)',
      primary: '#ff00ff',
      secondary: '#cc00cc',
      text: '#ff88ff',
      dark: '#1a0a1a'
    }
  },

  current: 'default',

  apply(name = this.current) {
    const theme = this.themes[name] || this.themes.default;
    const desktop = document.getElementById('chazon-desktop');
    if (desktop) {
      desktop.style.background = theme.bg;
      desktop.style.color = theme.text;
    }
    document.documentElement.style.setProperty('--primary', theme.primary);
    document.documentElement.style.setProperty('--secondary', theme.secondary);
    this.current = name;
  },

  cycle() {
    const names = Object.keys(this.themes);
    const idx = (names.indexOf(this.current) + 1) % names.length;
    this.apply(names[idx]);
    console.log(`🎨 Theme: ${names[idx]}`);
  }
};

window.ThemeSystem = ThemeSystem;
```
