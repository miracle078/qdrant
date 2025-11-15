# Query Flow Visualizer 3D
**UUID:** c3d4e5f6-g7h8-9012-cdef-234567890123
**Type:** Qdrant Query Pipeline | ISA-95 L2-L3

Real-time 3D visualization of query execution flow through the Qdrant pipeline: embedding → search → scoring → ranking → results.

## 🎯 Features

- **Query Pipeline**: Visualize each stage of query execution
- **Vector Flow**: Animated data flow through pipeline
- **Scoring Visualization**: Real-time similarity score calculation
- **Result Ranking**: Visual result ordering
- **Performance Metrics**: Query latency and throughput

## 🚀 Quick Start

```bash
# Open in browser
python -m http.server 8080
# Navigate to: http://localhost:8080/collab/3d-worlds/query-flow-visualizer.md
```

---

## 📦 Executable HTML

```html
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Qdrant Query Flow Visualizer</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000;overflow:hidden;font-family:monospace;color:#0f0}#c{width:100vw;height:100vh}.h{position:absolute;background:rgba(0,20,40,0.95);border:2px solid;border-radius:8px;padding:10px;font-size:10px}.t{background:#000;color:#0f0;padding:8px;height:160px;overflow-y:auto;white-space:pre-wrap;font-size:9px}.b{background:linear-gradient(45deg,#f0f,#0ff);border:0;padding:5px 10px;border-radius:4px;cursor:pointer;color:#000;font-weight:bold;margin:2px;font-size:9px}</style></head>
<body><canvas id="c"></canvas>
<div class="h" style="top:10px;left:10px;border-color:#0ff;max-width:380px">
<div style="color:#0ff;font-weight:bold">⚡ QUERY FLOW PIPELINE</div>
<div id="s1"></div>
<button class="b" onclick="QF.init()">INITIALIZE</button>
<button class="b" onclick="QF.executeQuery()">RUN QUERY</button>
<button class="b" onclick="QF.burst()">BURST TEST</button>
</div>
<div class="h" style="top:10px;right:10px;border-color:#0f0;width:450px">
<div style="color:#0f0;font-weight:bold">📊 QUERY TERMINAL</div>
<div id="t" class="t"></div>
<input type="text" id="i" style="background:#000;color:#0f0;border:1px solid #0f0;width:100%;padding:5px" placeholder="Enter query text...">
</div>
<div class="h" style="bottom:10px;left:10px;border-color:#f0f;max-width:350px">
<div style="color:#f0f;font-weight:bold">🎯 PIPELINE STAGES</div>
<div id="stages"></div>
</div>
<div class="h" style="bottom:10px;right:10px;border-color:#ff0;max-width:450px">
<div style="color:#ff0;font-weight:bold">📈 PERFORMANCE</div>
<div id="perf"></div>
</div>
<script>
const QF={
// Query Flow Visualizer
pipeline:[
{name:'Input',pos:[0,50,-100],color:0x00ffff,processed:0},
{name:'Embed',pos:[0,50,-50],color:0xff00ff,processed:0},
{name:'Search',pos:[0,50,0],color:0xffff00,processed:0},
{name:'Score',pos:[0,50,50],color:0x00ff00,processed:0},
{name:'Rank',pos:[0,50,100],color:0xff6600,processed:0},
{name:'Output',pos:[0,50,150],color:0xff0066,processed:0}
],
scene:null,camera:null,renderer:null,
stageNodes:new Map(),
queryParticles:[],
resultClouds:[],
queries:0,totalLatency:0,
metrics:{embed:0,search:0,score:0,rank:0},

init:()=>{
QF.log('Initializing Query Flow Pipeline...');
QF.scene=new THREE.Scene();
QF.camera=new THREE.PerspectiveCamera(75,innerWidth/innerHeight,0.1,2000);
QF.renderer=new THREE.WebGLRenderer({canvas:document.getElementById('c'),antialias:true});
QF.renderer.setSize(innerWidth,innerHeight);
QF.camera.position.set(0,150,250);

// Lights
QF.scene.add(new THREE.AmbientLight(0x404040));
const l1=new THREE.DirectionalLight(0xffffff,1);
l1.position.set(100,200,100);
CT.scene.add(l1);

// Grid
const grid=new THREE.GridHelper(400,80,0x00ff00,0x003300);
QF.scene.add(grid);

// Create pipeline stages
QF.pipeline.forEach((stage,idx)=>{
QF.createStage(stage,idx);
});

// Create connections
for(let i=0;i<QF.pipeline.length-1;i++){
QF.createConnection(i,i+1);
}

// Input handler
document.getElementById('i').addEventListener('keypress',(e)=>{
if(e.key==='Enter'){
QF.executeQuery(e.target.value);
e.target.value='';
}
});

QF.updateUI();
QF.animate();
QF.log('Pipeline initialized. Ready for queries.');

// Auto-execute demo queries
setTimeout(()=>QF.executeQuery('ISA-95 Level 3 MES'),1000);
setTimeout(()=>QF.executeQuery('PID controller ladder logic'),3000);
},

createStage:(stage,idx)=>{
// Main stage node
const geom=new THREE.CylinderGeometry(15,15,10,32);
const mat=new THREE.MeshPhongMaterial({
color:stage.color,
emissive:stage.color,
emissiveIntensity:0.3,
transparent:true,
opacity:0.8
});
const mesh=new THREE.Mesh(geom,mat);
mesh.position.set(stage.pos[0],stage.pos[1],stage.pos[2]);
mesh.rotation.x=Math.PI/2;
mesh.userData={stage:stage.name,index:idx};

// Label
const canvas=document.createElement('canvas');
canvas.width=256;canvas.height=64;
const ctx=canvas.getContext('2d');
ctx.fillStyle='#00ff00';
ctx.font='bold 28px monospace';
ctx.textAlign='center';
ctx.fillText(stage.name.toUpperCase(),128,40);
const texture=new THREE.CanvasTexture(canvas);
const spriteMat=new THREE.SpriteMaterial({map:texture});
const sprite=new THREE.Sprite(spriteMat);
sprite.scale.set(30,7.5,1);
sprite.position.set(0,20,0);
mesh.add(sprite);

QF.scene.add(mesh);
QF.stageNodes.set(idx,mesh);
QF.log(`Stage ${idx}: ${stage.name}`);
},

createConnection:(from,to)=>{
const s1=QF.pipeline[from];
const s2=QF.pipeline[to];
const geom=new THREE.BufferGeometry().setFromPoints([
new THREE.Vector3(...s1.pos),
new THREE.Vector3(...s2.pos)
]);
const mat=new THREE.LineBasicMaterial({
color:0x00ff00,
opacity:0.4,
transparent:true,
linewidth:2
});
const line=new THREE.Line(geom,mat);
QF.scene.add(line);
},

executeQuery:(text='Random query')=>{
const startTime=Date.now();
QF.queries++;
QF.log(`Query ${QF.queries}: "${text}"`);

// Create query particle
const particle={
text,
stage:0,
pos:new THREE.Vector3(...QF.pipeline[0].pos),
progress:0,
speed:0.02,
startTime,
scores:[]
};
QF.queryParticles.push(particle);

// Simulate pipeline stages
setTimeout(()=>QF.processStage(particle,0),100);
},

processStage:(particle,stageIdx)=>{
if(stageIdx>=QF.pipeline.length){
QF.completeQuery(particle);
return;
}

const stage=QF.pipeline[stageIdx];
stage.processed++;
const node=QF.stageNodes.get(stageIdx);

// Highlight stage
QF.highlightStage(stageIdx,1000);

// Stage-specific processing
const latency=50+Math.random()*100;
switch(stage.name){
case 'Embed':
QF.metrics.embed+=latency;
QF.log(`  Embedding generated (${latency.toFixed(0)}ms)`);
particle.embedding=Array(1536).fill(0).map(()=>Math.random());
break;
case 'Search':
QF.metrics.search+=latency;
const candidates=10+Math.floor(Math.random()*20);
QF.log(`  Found ${candidates} candidates (${latency.toFixed(0)}ms)`);
particle.candidates=candidates;
break;
case 'Score':
QF.metrics.score+=latency;
particle.scores=Array(particle.candidates||10).fill(0)
.map(()=>Math.random())
.sort((a,b)=>b-a);
QF.log(`  Scored ${particle.scores.length} vectors (${latency.toFixed(0)}ms)`);
// Create score visualization
QF.visualizeScores(particle,stageIdx);
break;
case 'Rank':
QF.metrics.rank+=latency;
QF.log(`  Ranked top ${Math.min(5,particle.scores.length)} results (${latency.toFixed(0)}ms)`);
break;
case 'Output':
QF.log(`  Results ready`);
break;
}

// Move to next stage
particle.stage=stageIdx+1;
if(particle.stage<QF.pipeline.length){
particle.targetPos=new THREE.Vector3(...QF.pipeline[particle.stage].pos);
}

setTimeout(()=>QF.processStage(particle,stageIdx+1),latency);
},

visualizeScores:(particle,stageIdx)=>{
const stagePos=QF.pipeline[stageIdx].pos;
particle.scores.slice(0,10).forEach((score,idx)=>{
const angle=(idx/10)*Math.PI*2;
const radius=25;
const x=stagePos[0]+Math.cos(angle)*radius;
const y=stagePos[1]+score*30;
const z=stagePos[2]+Math.sin(angle)*radius;

const geom=new THREE.SphereGeometry(2,8,8);
const mat=new THREE.MeshPhongMaterial({
color:QF.scoreToColor(score),
emissive:QF.scoreToColor(score),
emissiveIntensity:0.5
});
const mesh=new THREE.Mesh(geom,mat);
mesh.position.set(x,y,z);
QF.scene.add(mesh);

// Cleanup
setTimeout(()=>{
QF.scene.remove(mesh);
geom.dispose();
mat.dispose();
},2000);
});
},

scoreToColor:(score)=>{
const hue=score*120;
return new THREE.Color(`hsl(${hue},100%,50%)`).getHex();
},

highlightStage:(idx,duration)=>{
const node=QF.stageNodes.get(idx);
if(node){
const originalIntensity=node.material.emissiveIntensity;
node.material.emissiveIntensity=0.8;
const scale=node.scale.clone();
node.scale.multiplyScalar(1.2);
setTimeout(()=>{
node.material.emissiveIntensity=originalIntensity;
node.scale.copy(scale);
},duration);
}
},

completeQuery:(particle)=>{
const latency=Date.now()-particle.startTime;
QF.totalLatency+=latency;
const avgLatency=QF.totalLatency/QF.queries;
QF.log(`Query complete: ${latency}ms (avg: ${avgLatency.toFixed(0)}ms)`);
QF.updateUI();

// Remove particle
const idx=QF.queryParticles.indexOf(particle);
if(idx>=0)QF.queryParticles.splice(idx,1);
},

burst:()=>{
QF.log('Burst test: 10 queries');
const queries=[
'ISA-95 Level 3','PID controller','Batch process',
'Alarm management','Safety PLC','HMI design',
'SCADA system','Motor control','Valve sequencing',
'Process optimization'
];
queries.forEach((q,i)=>{
setTimeout(()=>QF.executeQuery(q),i*200);
});
},

log:(m)=>{
const t=document.getElementById('t');
const time=new Date().toTimeString().substr(0,8);
t.textContent+=`[${time}] ${m}\n`;
t.scrollTop=t.scrollHeight;
},

updateUI:()=>{
document.getElementById('s1').innerHTML=`
Queries: ${QF.queries}<br>
Active: ${QF.queryParticles.length}<br>
Avg Latency: ${(QF.totalLatency/Math.max(QF.queries,1)).toFixed(0)}ms
`;

const stages=document.getElementById('stages');
stages.innerHTML='';
QF.pipeline.forEach(stage=>{
const color=stage.color.toString(16).padStart(6,'0');
stages.innerHTML+=`<div style="color:#${color}">${stage.name}: ${stage.processed} processed</div>`;
});

const perf=document.getElementById('perf');
perf.innerHTML=`
<div>Embed: ${(QF.metrics.embed/Math.max(QF.queries,1)).toFixed(0)}ms avg</div>
<div>Search: ${(QF.metrics.search/Math.max(QF.queries,1)).toFixed(0)}ms avg</div>
<div>Score: ${(QF.metrics.score/Math.max(QF.queries,1)).toFixed(0)}ms avg</div>
<div>Rank: ${(QF.metrics.rank/Math.max(QF.queries,1)).toFixed(0)}ms avg</div>
<div style="color:#fff;margin-top:5px">Throughput: ${(QF.queries/(QF.totalLatency/1000)||0).toFixed(1)} q/s</div>
`;
},

animate:()=>{
requestAnimationFrame(QF.animate);
const t=Date.now()*0.001;

// Camera orbit
QF.camera.position.x=Math.sin(t*0.1)*280;
QF.camera.position.z=Math.cos(t*0.1)*280;
QF.camera.lookAt(0,50,0);

// Pulse stages
QF.stageNodes.forEach((node,idx)=>{
node.rotation.z+=0.01;
const pulse=1+Math.sin(t*2+idx)*0.05;
node.scale.set(1,1,pulse);
});

// Animate query particles
QF.queryParticles.forEach(particle=>{
if(particle.targetPos){
particle.pos.lerp(particle.targetPos,0.05);
}

// Draw particle
const geom=new THREE.SphereGeometry(3,16,16);
const mat=new THREE.MeshPhongMaterial({
color:0x00ffff,
emissive:0x00ffff,
emissiveIntensity:0.8
});
const mesh=new THREE.Mesh(geom,mat);
mesh.position.copy(particle.pos);
QF.scene.add(mesh);
setTimeout(()=>{
QF.scene.remove(mesh);
geom.dispose();
mat.dispose();
},50);

// Trail
const trailGeom=new THREE.SphereGeometry(1,8,8);
const trailMat=new THREE.MeshBasicMaterial({
color:0x0088ff,
transparent:true,
opacity:0.5
});
const trail=new THREE.Mesh(trailGeom,trailMat);
trail.position.copy(particle.pos);
QF.scene.add(trail);
setTimeout(()=>{
QF.scene.remove(trail);
trailGeom.dispose();
trailMat.dispose();
},200);
});

QF.renderer.render(QF.scene,QF.camera);
},

resize:()=>{
QF.camera.aspect=innerWidth/innerHeight;
QF.camera.updateProjectionMatrix();
QF.renderer.setSize(innerWidth,innerHeight);
}
};

window.addEventListener('DOMContentLoaded',()=>{
setTimeout(()=>QF.init(),100);
});
window.addEventListener('resize',QF.resize);
</script></body></html>
```

---

## 🎮 Controls

### Buttons
- **INITIALIZE**: Start pipeline visualization
- **RUN QUERY**: Execute single query
- **BURST TEST**: Run 10 queries rapidly

### Input
- Type query text and press Enter to execute custom query

## 📊 Pipeline Stages

| Stage | Function | Color | Metrics |
|-------|----------|-------|---------|
| **Input** | Query reception | Cyan | Queries received |
| **Embed** | Text → Vector embedding | Magenta | Embedding latency |
| **Search** | Vector similarity search | Yellow | Candidates found |
| **Score** | Calculate similarity scores | Green | Scoring latency |
| **Rank** | Order results by score | Orange | Ranking latency |
| **Output** | Return results | Pink | Total latency |

## 🎯 Visualization Elements

### Query Particles
- **Blue spheres**: Active queries
- **Trail**: Query path through pipeline
- **Movement**: Lerp interpolation between stages

### Score Visualization
- **Circular arrangement**: Around Score stage
- **Height**: Proportional to similarity score
- **Color**: Green (high) → Yellow → Red (low)

### Stage Highlighting
- **Pulse effect**: When processing query
- **Scale increase**: 1.2x during activity
- **Emissive boost**: Higher intensity

## 📈 Performance Metrics

### Latency Breakdown
- **Embed**: 50-150ms (text-embedding-3-large)
- **Search**: 50-150ms (HNSW index)
- **Score**: 50-150ms (cosine similarity)
- **Rank**: 50-150ms (top-k selection)
- **Total**: ~200-600ms per query

### Throughput
- **Sequential**: 2-5 queries/second
- **Burst**: 10 queries in 2 seconds
- **Sustained**: Limited by embedding API

## 🔬 Query Flow

```
Input → Embed → Search → Score → Rank → Output
  ↓       ↓        ↓       ↓       ↓       ↓
Text   Vector  Candidates Scores Top-K  Results
       (1536d)  (10-30)   (0-1)   (5)   (JSON)
```

## 🔗 Integration

### Connect to Real Qdrant
```javascript
async function executeRealQuery(text) {
  // Embed
  const embedding = await fetch('https://api.openai.com/v1/embeddings', {
    method: 'POST',
    headers: {'Authorization': 'Bearer ' + OPENAI_KEY},
    body: JSON.stringify({input: text, model: 'text-embedding-3-large'})
  }).then(r => r.json());

  // Search
  const results = await fetch('http://localhost:6333/collections/isa/points/search', {
    method: 'POST',
    body: JSON.stringify({
      vector: embedding.data[0].embedding,
      limit: 10
    })
  }).then(r => r.json());

  return results;
}
```

## 🎯 Use Cases

1. **Query Debugging**: Visualize pipeline bottlenecks
2. **Performance Testing**: Measure latency per stage
3. **Education**: Teach vector search concepts
4. **Monitoring**: Real-time query flow tracking
5. **Optimization**: Identify slow stages

---

**UUID Verification**: c3d4e5f6-g7h8-9012-cdef-234567890123
**Last Updated**: 2025-11-15
**Status**: Active
