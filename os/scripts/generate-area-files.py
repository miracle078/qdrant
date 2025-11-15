#!/usr/bin/env python3
"""
Generate HMI, PLC, and config files for each OS area
Factory automation - each directory is a PLC area
"""

import os
import yaml

# Area configurations
AREAS = {
    'backend': {
        'name': 'Backend API',
        'icon': '🔧',
        'description': 'FastAPI server, Qdrant integration, MCP servers',
        'plc_status': 'RUNNING',
        'scan_time': '100ms',
        'tag_count': 156,
        'routine_count': 24,
        'color': '#00ccff',
        'operations': [
            {'name': 'Start Server', 'endpoint': '/start'},
            {'name': 'Stop Server', 'endpoint': '/stop'},
            {'name': 'Health Check', 'endpoint': '/health'},
            {'name': 'View Logs', 'endpoint': '/logs'}
        ],
        'metrics': [
            {'label': 'Requests/sec', 'tag': 'api.requests_per_sec', 'unit': ''},
            {'label': 'Response Time', 'tag': 'api.avg_response_ms', 'unit': 'ms'},
            {'label': 'Error Rate', 'tag': 'api.error_rate', 'unit': '%'}
        ]
    },
    'boot': {
        'name': 'Boot Sequencer',
        'icon': '🚀',
        'description': '6-phase initialization system with PackML state machine',
        'plc_status': 'COMPLETE',
        'scan_time': '50ms',
        'tag_count': 72,
        'routine_count': 6,
        'color': '#00ff88',
        'operations': [
            {'name': 'Run Boot Sequence', 'endpoint': '/boot'},
            {'name': 'Reset System', 'endpoint': '/reset'},
            {'name': 'Phase Status', 'endpoint': '/phases'},
            {'name': 'View Log', 'endpoint': '/log'}
        ],
        'metrics': [
            {'label': 'Phases Complete', 'tag': 'boot.phases_complete', 'unit': '/6'},
            {'label': 'Boot Time', 'tag': 'boot.total_time_ms', 'unit': 'ms'},
            {'label': 'Modules Loaded', 'tag': 'boot.modules_loaded', 'unit': ''}
        ]
    },
    'data': {
        'name': 'Data Layer',
        'icon': '💾',
        'description': 'SQL databases, token storage, architecture maps',
        'plc_status': 'RUNNING',
        'scan_time': '75ms',
        'tag_count': 124,
        'routine_count': 18,
        'color': '#ffaa00',
        'operations': [
            {'name': 'Query Database', 'endpoint': '/query'},
            {'name': 'Backup Data', 'endpoint': '/backup'},
            {'name': 'View Schema', 'endpoint': '/schema'},
            {'name': 'Optimize DB', 'endpoint': '/optimize'}
        ],
        'metrics': [
            {'label': 'Records', 'tag': 'db.total_records', 'unit': ''},
            {'label': 'Query Time', 'tag': 'db.avg_query_ms', 'unit': 'ms'},
            {'label': 'DB Size', 'tag': 'db.size_mb', 'unit': 'MB'}
        ]
    },
    'debug': {
        'name': 'Debug Console',
        'icon': '🐛',
        'description': 'System diagnostics, logs, performance monitoring',
        'plc_status': 'RUNNING',
        'scan_time': '200ms',
        'tag_count': 89,
        'routine_count': 14,
        'color': '#ff0044',
        'operations': [
            {'name': 'Refresh System Info', 'endpoint': '/sysinfo'},
            {'name': 'Check Features', 'endpoint': '/features'},
            {'name': 'Scan Modules', 'endpoint': '/modules'},
            {'name': 'Export Logs', 'endpoint': '/export'}
        ],
        'metrics': [
            {'label': 'CPU Usage', 'tag': 'sys.cpu_percent', 'unit': '%'},
            {'label': 'Memory', 'tag': 'sys.mem_used_mb', 'unit': 'MB'},
            {'label': 'Log Entries', 'tag': 'debug.log_count', 'unit': ''}
        ]
    },
    'frontend': {
        'name': 'Frontend HMI',
        'icon': '🖥️',
        'description': 'Medical imaging viewer, DICOM interface, patient UI',
        'plc_status': 'RUNNING',
        'scan_time': '50ms',
        'tag_count': 203,
        'routine_count': 32,
        'color': '#00ff88',
        'operations': [
            {'name': 'Load Study', 'endpoint': '/study'},
            {'name': 'Adjust Window', 'endpoint': '/window'},
            {'name': 'Measure Distance', 'endpoint': '/measure'},
            {'name': 'Export DICOM', 'endpoint': '/export'}
        ],
        'metrics': [
            {'label': 'Studies Loaded', 'tag': 'viewer.studies_loaded', 'unit': ''},
            {'label': 'Frame Rate', 'tag': 'viewer.fps', 'unit': 'fps'},
            {'label': 'Viewport Size', 'tag': 'viewer.viewport_size', 'unit': 'px'}
        ]
    },
    'language': {
        'name': 'SNT Language',
        'icon': '🔤',
        'description': 'Trinary computing, space-time notation, compiler',
        'plc_status': 'IDLE',
        'scan_time': '120ms',
        'tag_count': 67,
        'routine_count': 10,
        'color': '#aa00ff',
        'operations': [
            {'name': 'Compile SNT', 'endpoint': '/compile'},
            {'name': 'Run Program', 'endpoint': '/run'},
            {'name': 'View AST', 'endpoint': '/ast'},
            {'name': 'Trinary Test', 'endpoint': '/trinary'}
        ],
        'metrics': [
            {'label': 'Programs Loaded', 'tag': 'snt.programs_loaded', 'unit': ''},
            {'label': 'Compile Time', 'tag': 'snt.compile_time_ms', 'unit': 'ms'},
            {'label': 'Trinary Ops', 'tag': 'snt.trinary_ops', 'unit': ''}
        ]
    },
    'medical': {
        'name': 'Medical Imaging',
        'icon': '🏥',
        'description': 'DICOM, X-Ray, MRI, CT, AlF-DETECT system',
        'plc_status': 'RUNNING',
        'scan_time': '80ms',
        'tag_count': 178,
        'routine_count': 26,
        'color': '#ff88ff',
        'operations': [
            {'name': 'AlF-DETECT', 'endpoint': '/alf-detect'},
            {'name': 'Analyze X-Ray', 'endpoint': '/xray'},
            {'name': 'View MRI', 'endpoint': '/mri'},
            {'name': 'Generate Report', 'endpoint': '/report'}
        ],
        'metrics': [
            {'label': 'Studies Analyzed', 'tag': 'medical.studies_analyzed', 'unit': ''},
            {'label': 'AlF Detection', 'tag': 'medical.alf_detections', 'unit': ''},
            {'label': 'Avg Confidence', 'tag': 'medical.avg_confidence', 'unit': '%'}
        ]
    },
    'models': {
        'name': 'AI Models',
        'icon': '🤖',
        'description': 'ONNX models, WebGPU inference, embeddings',
        'plc_status': 'IDLE',
        'scan_time': '100ms',
        'tag_count': 94,
        'routine_count': 15,
        'color': '#00ccff',
        'operations': [
            {'name': 'Load Model', 'endpoint': '/load'},
            {'name': 'Run Inference', 'endpoint': '/infer'},
            {'name': 'Download Model', 'endpoint': '/download'},
            {'name': 'Benchmark', 'endpoint': '/benchmark'}
        ],
        'metrics': [
            {'label': 'Models Loaded', 'tag': 'models.loaded_count', 'unit': ''},
            {'label': 'GPU Memory', 'tag': 'models.gpu_mem_mb', 'unit': 'MB'},
            {'label': 'Inference Speed', 'tag': 'models.avg_infer_ms', 'unit': 'ms'}
        ]
    },
    'modules': {
        'name': 'Module System',
        'icon': '📦',
        'description': '114 markdown modules, UUID registry, lazy loading',
        'plc_status': 'RUNNING',
        'scan_time': '60ms',
        'tag_count': 247,
        'routine_count': 38,
        'color': '#00ff88',
        'operations': [
            {'name': 'Load Module', 'endpoint': '/load'},
            {'name': 'Scan Directory', 'endpoint': '/scan'},
            {'name': 'Clear Cache', 'endpoint': '/cache/clear'},
            {'name': 'View Registry', 'endpoint': '/registry'}
        ],
        'metrics': [
            {'label': 'Modules Loaded', 'tag': 'modules.loaded_count', 'unit': ''},
            {'label': 'Memory Usage', 'tag': 'modules.mem_mb', 'unit': 'MB'},
            {'label': 'Cache Hit Rate', 'tag': 'modules.cache_hit_rate', 'unit': '%'}
        ]
    },
    'templates': {
        'name': 'Template Engine',
        'icon': '📄',
        'description': 'ISA templates, view templates, medical workflows',
        'plc_status': 'RUNNING',
        'scan_time': '90ms',
        'tag_count': 56,
        'routine_count': 11,
        'color': '#ffaa00',
        'operations': [
            {'name': 'Render Template', 'endpoint': '/render'},
            {'name': 'List Templates', 'endpoint': '/list'},
            {'name': 'Compile Template', 'endpoint': '/compile'},
            {'name': 'Clear Cache', 'endpoint': '/cache'}
        ],
        'metrics': [
            {'label': 'Templates Loaded', 'tag': 'templates.loaded_count', 'unit': ''},
            {'label': 'Render Time', 'tag': 'templates.avg_render_ms', 'unit': 'ms'},
            {'label': 'Cache Entries', 'tag': 'templates.cache_size', 'unit': ''}
        ]
    }
}

def generate_hmi_html(area_id, config):
    """Generate HMI HTML for area"""
    ops_html = '\\n'.join([
        f'    <div class="control-btn" onclick="executeOperation(\'{op[\'endpoint\']}\')">\\n'
        f'      <div class="op-icon">▶</div>\\n'
        f'      <div class="op-name">{op[\'name\']}</div>\\n'
        f'    </div>'
        for op in config['operations']
    ])

    metrics_html = '\\n'.join([
        f'    <div class="metric-card">\\n'
        f'      <div class="metric-label">{m[\'label\']}</div>\\n'
        f'      <div class="metric-value" data-tag="{m[\'tag\']}">--</div>\\n'
        f'      <div class="metric-unit">{m[\'unit\']}</div>\\n'
        f'    </div>'
        for m in config['metrics']
    ])

    status_color = '#00ff88' if config['plc_status'] == 'RUNNING' else '#ffaa00' if config['plc_status'] == 'IDLE' else '#ff0044'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HMI - {config['name']}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Courier New', monospace;
    background: #0a0a0a;
    color: {config['color']};
    padding: 20px;
  }}
  .hmi-header {{
    background: #1a1a2e;
    border: 3px solid {config['color']};
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
  }}
  .hmi-title {{
    font-size: 2em;
    margin-bottom: 10px;
  }}
  .status-bar {{
    display: flex;
    gap: 20px;
    align-items: center;
    color: #888;
    font-size: 0.9em;
  }}
  .status-indicator {{
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: {status_color};
    animation: pulse 2s infinite;
    margin-right: 5px;
  }}
  @keyframes pulse {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0.4; }}
  }}
  .section {{
    background: #1a1a2e;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
  }}
  .section h2 {{
    color: {config['color']};
    border-bottom: 2px solid {config['color']};
    padding-bottom: 10px;
    margin-bottom: 15px;
  }}
  .control-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
  }}
  .control-btn {{
    background: #000;
    border: 2px solid {config['color']};
    border-radius: 6px;
    padding: 20px;
    cursor: pointer;
    transition: all 0.3s;
    text-align: center;
  }}
  .control-btn:hover {{
    background: {config['color']};
    color: #000;
    transform: scale(1.05);
  }}
  .op-icon {{
    font-size: 2em;
    margin-bottom: 10px;
  }}
  .op-name {{
    font-size: 1.1em;
    font-weight: bold;
  }}
  .metric-card {{
    background: #000;
    border-left: 4px solid {config['color']};
    padding: 15px;
    text-align: center;
  }}
  .metric-label {{
    color: #888;
    font-size: 0.9em;
    margin-bottom: 10px;
  }}
  .metric-value {{
    font-size: 2.5em;
    font-weight: bold;
    color: {config['color']};
  }}
  .metric-unit {{
    color: #666;
    font-size: 0.8em;
    margin-top: 5px;
  }}
  .breadcrumb {{
    color: #888;
    margin-bottom: 20px;
  }}
  .breadcrumb a {{
    color: {config['color']};
    text-decoration: none;
  }}
</style>
</head>
<body>

<div class="breadcrumb">
  <a href="../../">Home</a> / <a href="../">Chazon OS</a> / {config['name']} HMI
</div>

<div class="hmi-header">
  <div class="hmi-title">{config['icon']} {config['name']} - HMI</div>
  <div>{config['description']}</div>
  <div class="status-bar">
    <div>
      <span class="status-indicator"></span>
      <strong>PLC Status:</strong> {config['plc_status']}
    </div>
    <div><strong>Scan Time:</strong> {config['scan_time']}</div>
    <div><strong>Tags:</strong> {config['tag_count']}</div>
    <div><strong>Routines:</strong> {config['routine_count']}</div>
  </div>
</div>

<div class="section">
  <h2>Operations</h2>
  <div class="control-grid">
{ops_html}
  </div>
</div>

<div class="section">
  <h2>Live Metrics</h2>
  <div class="control-grid">
{metrics_html}
  </div>
</div>

<div class="section">
  <h2>Quick Links</h2>
  <div class="control-grid">
    <div class="control-btn" onclick="window.location.href='plc.html'">
      <div class="op-icon">⚙️</div>
      <div class="op-name">View PLC Logic</div>
    </div>
    <div class="control-btn" onclick="window.location.href='index.html'">
      <div class="op-icon">📄</div>
      <div class="op-name">Area Index</div>
    </div>
    <div class="control-btn" onclick="window.location.href='../../scada.html'">
      <div class="op-icon">📊</div>
      <div class="op-name">SCADA Master</div>
    </div>
  </div>
</div>

<script>
function executeOperation(endpoint) {{
  console.log('Executing operation:', endpoint);
  alert('Operation: ' + endpoint + '\\nIn production, this would call the backend API.');
}}

// Simulate metric updates
function updateMetrics() {{
  document.querySelectorAll('.metric-value').forEach(el => {{
    const tag = el.getAttribute('data-tag');
    // In production, fetch from PLC
    el.textContent = Math.floor(Math.random() * 100);
  }});
}}

setInterval(updateMetrics, 2000);
updateMetrics();
</script>

</body>
</html>'''

def generate_config_yaml(area_id, config):
    """Generate config.yaml for area"""
    return yaml.dump({
        'area': {
            'id': area_id,
            'name': config['name'],
            'icon': config['icon'],
            'description': config['description']
        },
        'plc': {
            'status': config['plc_status'],
            'scan_time_ms': int(config['scan_time'].replace('ms', '')),
            'tag_count': config['tag_count'],
            'routine_count': config['routine_count']
        },
        'hmi': {
            'color': config['color'],
            'refresh_interval_ms': 1000
        },
        'operations': config['operations'],
        'metrics': config['metrics']
    }, default_flow_style=False)

def main():
    os_dir = '/home/user/qdrant/os'

    for area_id, config in AREAS.items():
        area_path = os.path.join(os_dir, area_id)

        # Generate HMI
        hmi_path = os.path.join(area_path, 'hmi.html')
        with open(hmi_path, 'w') as f:
            f.write(generate_hmi_html(area_id, config))
        print(f'✓ Created {area_id}/hmi.html')

        # Generate config.yaml
        config_path = os.path.join(area_path, 'config.yaml')
        with open(config_path, 'w') as f:
            f.write(generate_config_yaml(area_id, config))
        print(f'✓ Created {area_id}/config.yaml')

    print(f'\\n✓ Generated HMI and config files for {len(AREAS)} areas')

if __name__ == '__main__':
    main()
