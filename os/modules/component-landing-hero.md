# Landing Hero Component
**Main Content** | Project Cards

```javascript
const LandingHero = () => `
<div class="container" style="text-align: center; padding: 60px 20px;">
  <h1 style="font-size: 3em; margin-bottom: 20px;">🌌 AutomationGPT Project</h1>
  <p style="font-size: 1.2em; color: #00ccff; margin-bottom: 50px;">lablab.ai Qdrant Challenge | ISA Standards + AI</p>

  <div style="margin-bottom: 40px;">
    <a href="dashboard.html" style="display: inline-block; background: linear-gradient(45deg, #00ff88, #00ccff); color: #000; padding: 15px 40px; border-radius: 30px; font-size: 1.2em; font-weight: bold; box-shadow: 0 5px 20px rgba(0,255,136,0.5);">
      🚀 Launch Unified Dashboard
    </a>
    <p style="margin-top: 10px; color: #888; font-size: 0.9em;">All 3 demos | Ctrl+K quick command</p>
  </div>

  ${ProjectCards()}
</div>`;

const ProjectCards = () => {
  const cards = [
    { i: '🌌', t: 'Chazon OS', u: 'chazon.html', b: 'φ-Balanced', d: 'Pseudo-OS', f: ['<250 tokens', 'Markdown', 'ISA L0-L4'] },
    { i: '🏭', t: 'ISA-OS', u: 'isa-os.html', b: 'Container', d: 'Docker→ISA', f: ['Kernel', 'Viz', 'GitHub'] },
    { i: '🔍', t: 'AutomationGPT', u: 'automationgpt.html', b: 'Search', d: 'Multimodal', f: ['Qdrant', 'Claude', 'ISA'] }
  ];

  return `<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:30px;margin-top:40px">
    ${cards.map(c => `
      <a href="${c.u}" style="background:rgba(0,0,0,0.7);border:2px solid #00ff88;border-radius:15px;padding:30px;display:block;transition:all 0.3s" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform=''">
        <div style="font-size:3em;margin-bottom:20px">${c.i}</div>
        <h2 style="color:#00ff88;font-size:2em;margin-bottom:10px">${c.t}</h2>
        <span style="background:#00ff88;color:#000;padding:3px 10px;border-radius:10px;font-size:0.8em">${c.b}</span>
        <p style="margin:15px 0;color:#ccc">${c.d}</p>
        <ul style="list-style:none;text-align:left">
          ${c.f.map(x => `<li style="padding:5px 0;color:#00ccff">✓ ${x}</li>`).join('')}
        </ul>
      </a>
    `).join('')}
  </div>`;
};

return LandingHero();
```
