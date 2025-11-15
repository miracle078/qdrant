# Repository HMI
**Visual Control Interface** | ISA-95 L2

HMI visualization for GitHub repository as manufacturing system.

```javascript
const RepoHMI = {
  session: null,
  project: 'RepoVision',

  init() {
    this.session = {
      user: 'operator',
      started: Date.now(),
      views: new Map()
    };

    this.createViews();
    console.log('📺 HMI: RepoVision loaded');
  },

  createViews() {
    // Main Dashboard view
    this.session.views.set('Dashboard', {
      components: [
        { type: 'ia.chart.timeSeries', binding: '[Repo]CommitRate' },
        { type: 'ia.display.gauge', binding: '[Production]QualityScore' },
        { type: 'ia.display.led', binding: '[Repo]BuildStatus' }
      ]
    });

    // Production view
    this.session.views.set('Production', {
      components: [
        { type: 'ia.display.label', binding: '[Production]ModulesBuilt' },
        { type: 'ia.display.label', binding: '[Production]ComponentsAssembled' },
        { type: 'ia.chart.pie', binding: '[Production]Stats' }
      ]
    });

    // Alarms view
    this.session.views.set('Alarms', {
      components: [
        { type: 'ia.display.alarmTable', source: 'gateway' }
      ]
    });
  },

  renderDashboard() {
    const commitRate = IgnitionGateway.readTag('[Repo]CommitRate').value;
    const quality = IgnitionGateway.readTag('[Production]QualityScore').value;
    const buildStatus = IgnitionGateway.readTag('[Repo]BuildStatus').value;

    return `
<div class="hmi-dashboard" style="background:#1a1a1a;color:#00ff88;padding:20px;font-family:monospace">
  <h1>🏭 Repository Factory - RepoVision HMI</h1>

  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:20px">
    <div class="gauge" style="border:2px solid #00ff88;padding:15px;border-radius:10px">
      <h3>Commit Rate</h3>
      <div style="font-size:2em;color:#00ccff">${commitRate} /hr</div>
    </div>

    <div class="gauge" style="border:2px solid #00ff88;padding:15px;border-radius:10px">
      <h3>Quality Score</h3>
      <div style="font-size:2em;color:${quality > 80 ? '#00ff88' : '#ff0044'}">${quality}%</div>
    </div>

    <div class="status-led" style="border:2px solid #00ff88;padding:15px;border-radius:10px">
      <h3>Build Status</h3>
      <div style="font-size:1.5em">${buildStatus === 'Success' ? '🟢' : '🟡'} ${buildStatus}</div>
    </div>
  </div>

  <div style="margin-top:20px;border:2px solid #00ff88;padding:15px;border-radius:10px">
    <h3>Active Alarms</h3>
    <div id="alarm-list">${this.renderAlarms()}</div>
  </div>
</div>`;
  },

  renderAlarms() {
    const activeAlarms = IgnitionGateway.alarms.filter(a => a.state === 'Active');

    if (activeAlarms.length === 0) {
      return '<p style="color:#00ff88">No active alarms</p>';
    }

    return activeAlarms.map(alarm => `
      <div style="padding:10px;border-left:3px solid ${alarm.priority === 'High' ? '#ff0044' : '#ff0'};margin:5px 0">
        ${alarm.message} - ${alarm.priority}
      </div>
    `).join('');
  },

  openView(viewName) {
    const view = this.session.views.get(viewName);
    if (view) {
      console.log(`Opening view: ${viewName}`);
      return view;
    }
    return null;
  }
};

window.RepoHMI = RepoHMI;
```
