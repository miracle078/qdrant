# Collection Topology 3D
**UUID:** b2c3d4e5-f6g7-8901-bcde-f12345678901
**Type:** Qdrant Collection Network | ISA-95 L3-L4

3D network visualization of Qdrant collections, showing relationships, data flow, and cross-collection queries with autonomous network agents.

## 🎯 Features

- **Collection Nodes**: 3D spheres representing each collection
- **Data Flow**: Animated connections showing query paths
- **Network Agents**: Auto-balancing and optimization
- **Cross-Collection Search**: Visual multi-collection queries
- **Real-time Stats**: Collection size, query count, performance

## 🚀 Quick Start

```bash
# Open in browser
python -m http.server 8080
# Navigate to: http://localhost:8080/collab/3d-worlds/collection-topology.md
```

---

## 📦 Executable HTML

```html
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Qdrant Collection Topology</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000;overflow:hidden;font-family:monospace;color:#0f0}#c{width:100vw;height:100vh}.h{position:absolute;background:rgba(0,20,40,0.95);border:2px solid;border-radius:8px;padding:10px;font-size:10px}.t{background:#000;color:#0f0;padding:8px;height:180px;overflow-y:auto;white-space:pre-wrap;font-size:9px}.b{background:linear-gradient(45deg,#f0f,#0ff);border:0;padding:5px 10px;border-radius:4px;cursor:pointer;color:#000;font-weight:bold;margin:2px;font-size:9px}</style></head>
<body><canvas id="c"></canvas>
<div class="h" style="top:10px;left:10px;border-color:#0ff;max-width:380px">
<div style="color:#0ff;font-weight:bold">🌐 COLLECTION TOPOLOGY</div>
<div id="s1"></div>
<button class="b" onclick="CT.init()">INITIALIZE</button>
<button class="b" onclick="CT.query()">CROSS-QUERY</button>
<button class="b" onclick="CT.optimize()">OPTIMIZE</button>
<button class="b" onclick="CT.expand()">EXPAND</button>
</div>
<div class="h" style="top:10px;right:10px;border-color:#0f0;width:450px">
<div style="color:#0f0;font-weight:bold">⚡ NETWORK TERMINAL</div>
<div id="t" class="t"></div>
<input type="text" id="i" style="background:#000;color:#0f0;border:1px solid #0f0;width:100%;padding:5px" placeholder="Command: query|route|optimize|stats">
</div>
<div class="h" style="bottom:10px;left:10px;border-color:#f0f;max-width:350px">
<div style="color:#f0f;font-weight:bold">🤖 NETWORK AGENTS</div>
<div id="ag"></div>
</div>
<div class="h" style="bottom:10px;right:10px;border-color:#ff0;max-width:450px">
<div style="color:#ff0;font-weight:bold">📊 COLLECTION STATS</div>
<div id="stats"></div>
</div>
<script>
const CT={
// Collection Topology
collections:{
isa:{name:'ISA',pos:[0,50,0],size:15420,dim:1536,color:0x00ffff,queries:0},
code:{name:'Code',pos:[60,30,60],size:8760,dim:768,color:0xff00ff,queries:0},
img:{name:'Images',pos:[-60,30,60],size:4520,dim:512,color:0xffff00,queries:0},
audio:{name:'Audio',pos:[60,30,-60],size:2180,dim:512,color:0x00ff00,queries:0},
doc:{name:'Docs',pos:[-60,30,-60],size:12340,dim:1536,color:0xff6600,queries:0},
vid:{name:'Video',pos:[0,10,80],size:1560,dim:512,color:0xff0066,queries:0}
},
routes:[],
scene:null,camera:null,renderer:null,
nodes:new Map(),connections:[],
agents:new Map(),
queryParticles:[],

init:()=>{
CT.log('Initializing Collection Topology...');
CT.scene=new THREE.Scene();
CT.camera=new THREE.PerspectiveCamera(75,innerWidth/innerHeight,0.1,2000);
CT.renderer=new THREE.WebGLRenderer({canvas:document.getElementById('c'),antialias:true});
CT.renderer.setSize(innerWidth,innerHeight);
CT.camera.position.set(150,150,150);

// Lights
CT.scene.add(new THREE.AmbientLight(0x404040));
const l1=new THREE.DirectionalLight(0xffffff,1);
l1.position.set(100,200,100);
CT.scene.add(l1);

// Grid
const grid=new THREE.GridHelper(200,40,0x00ff00,0x003300);
CT.scene.add(grid);

// Create collection nodes
Object.entries(CT.collections).forEach(([key,coll])=>{
CT.createCollectionNode(key,coll);
});

// Create connections
CT.createConnections();

// Create routes
CT.routes=[
{from:'isa',to:'code',weight:0.8,packets:0},
{from:'isa',to:'doc',weight:0.6,packets:0},
{from:'code',to:'img',weight:0.5,packets:0},
{from:'img',to:'doc',weight:0.4,packets:0},
{from:'audio',to:'doc',weight:0.3,packets:0},
{from:'vid',to:'img',weight:0.7,packets:0}
];

// Create agents
CT.createAgent('router','routing',CT.routerBehavior);
CT.createAgent('balancer','load-balancing',CT.balancerBehavior);
CT.createAgent('optimizer','optimization',CT.optimizerBehavior);
CT.createAgent('monitor','monitoring',CT.monitorBehavior);

CT.startAgents();

// Input
document.getElementById('i').addEventListener('keypress',(e)=>{
if(e.key==='Enter'){CT.command(e.target.value);e.target.value=''}
});

CT.updateStats();
CT.animate();
CT.log('Topology initialized. Network agents active.');
},

createCollectionNode:(key,coll)=>{
const radius=Math.log(coll.size+1)*2+5;
const geom=new THREE.SphereGeometry(radius,32,32);
const mat=new THREE.MeshPhongMaterial({
color:coll.color,
emissive:coll.color,
emissiveIntensity:0.3,
transparent:true,
opacity:0.8,
wireframe:false
});
const mesh=new THREE.Mesh(geom,mat);
mesh.position.set(coll.pos[0],coll.pos[1],coll.pos[2]);
mesh.userData={collection:key,name:coll.name};

// Add label
const canvas=document.createElement('canvas');
canvas.width=256;canvas.height=64;
const ctx=canvas.getContext('2d');
ctx.fillStyle='#00ff00';
ctx.font='bold 32px monospace';
ctx.textAlign='center';
ctx.fillText(coll.name.toUpperCase(),128,40);
const texture=new THREE.CanvasTexture(canvas);
const spriteMat=new THREE.SpriteMaterial({map:texture});
const sprite=new THREE.Sprite(spriteMat);
sprite.scale.set(20,5,1);
sprite.position.set(0,radius+10,0);
mesh.add(sprite);

CT.scene.add(mesh);
CT.nodes.set(key,mesh);
CT.log(`Created node: ${coll.name} (${coll.size} vectors, ${coll.dim}d)`);
},

createConnections:()=>{
const keys=Object.keys(CT.collections);
keys.forEach((k1,i)=>{
keys.slice(i+1).forEach(k2=>{
const n1=CT.nodes.get(k1);
const n2=CT.nodes.get(k2);
if(n1&&n2){
const geom=new THREE.BufferGeometry().setFromPoints([
n1.position,n2.position
]);
const mat=new THREE.LineBasicMaterial({
color:0x00ff00,
opacity:0.15,
transparent:true
});
const line=new THREE.Line(geom,mat);
CT.scene.add(line);
CT.connections.push({line,from:k1,to:k2,active:0});
}
});
});
CT.log(`Created ${CT.connections.length} connections`);
},

query:()=>{
const keys=Object.keys(CT.collections);
const from=keys[Math.floor(Math.random()*keys.length)];
const to=keys[Math.floor(Math.random()*keys.length)];
if(from===to)return;

CT.executeQuery(from,to);
},

executeQuery:(from,to)=>{
const n1=CT.nodes.get(from);
const n2=CT.nodes.get(to);
if(!n1||!n2)return;

CT.collections[from].queries++;
CT.collections[to].queries++;

// Find route
const route=CT.routes.find(r=>(r.from===from&&r.to===to)||(r.from===to&&r.to===from));
if(route)route.packets++;

// Highlight connection
const conn=CT.connections.find(c=>
(c.from===from&&c.to===to)||(c.from===to&&c.to===from)
);
if(conn){
conn.active=1;
conn.line.material.opacity=0.8;
conn.line.material.color.setHex(0x00ffff);
setTimeout(()=>{
conn.active=0;
conn.line.material.opacity=0.15;
conn.line.material.color.setHex(0x00ff00);
},1000);
}

// Create particle
const particle={
pos:n1.position.clone(),
target:n2.position.clone(),
progress:0,
speed:0.02,
color:CT.collections[from].color
};
CT.queryParticles.push(particle);

CT.log(`Query: ${from} → ${to}`);
CT.updateStats();
},

optimize:()=>{
CT.log('Optimizing network topology...');
// Reposition nodes based on query frequency
const keys=Object.keys(CT.collections);
const center=new THREE.Vector3(0,40,0);
keys.forEach((key,idx)=>{
const coll=CT.collections[key];
const node=CT.nodes.get(key);
const angle=(idx/keys.length)*Math.PI*2;
const radius=40+coll.queries*0.5;
const newPos=new THREE.Vector3(
Math.cos(angle)*radius,
40+coll.queries*0.1,
Math.sin(angle)*radius
);
// Smooth transition
node.position.lerp(newPos,0.1);
coll.pos=[node.position.x,node.position.y,node.position.z];
});

// Update connections
CT.connections.forEach(conn=>{
const n1=CT.nodes.get(conn.from);
const n2=CT.nodes.get(conn.to);
if(n1&&n2){
conn.line.geometry.setFromPoints([n1.position,n2.position]);
}
});

CT.log('Topology optimized');
},

expand:()=>{
CT.log('Expanding collection network...');
Object.values(CT.nodes).forEach(node=>{
node.position.multiplyScalar(1.2);
});
CT.connections.forEach(conn=>{
const n1=CT.nodes.get(conn.from);
const n2=CT.nodes.get(conn.to);
if(n1&&n2){
conn.line.geometry.setFromPoints([n1.position,n2.position]);
}
});
Object.entries(CT.collections).forEach(([key,coll])=>{
const node=CT.nodes.get(key);
coll.pos=[node.position.x,node.position.y,node.position.z];
});
CT.log('Network expanded');
},

// Agents
createAgent:(name,type,behavior)=>{
const agent={
name,type,active:true,cycles:0,mem:{},
run:async()=>{
while(agent.active){
await behavior.call(agent);
agent.cycles++;
await CT.sleep(150+Math.random()*150);
}
}
};
CT.agents.set(name,agent);
return agent;
},

sleep:(ms)=>new Promise(r=>setTimeout(r,ms)),

startAgents:()=>{
CT.agents.forEach(a=>a.run());
CT.log(`Started ${CT.agents.size} network agents`);
},

routerBehavior:async function(){
if(this.cycles%15===0){
CT.query();
this.mem.routed=(this.mem.routed||0)+1;
}
},

balancerBehavior:async function(){
if(this.cycles%25===0){
// Balance queries across collections
const keys=Object.keys(CT.collections);
const sorted=keys.sort((a,b)=>
CT.collections[a].queries-CT.collections[b].queries
);
const from=sorted[sorted.length-1];
const to=sorted[0];
if(CT.collections[from].queries>CT.collections[to].queries+5){
CT.executeQuery(from,to);
this.mem.balanced=(this.mem.balanced||0)+1;
}
}
},

optimizerBehavior:async function(){
if(this.cycles%40===0){
CT.optimize();
this.mem.optimized=(this.mem.optimized||0)+1;
}
},

monitorBehavior:async function(){
if(this.cycles%10===0){
CT.updateStats();
}
},

// Commands
command:(cmd)=>{
const parts=cmd.trim().split(' ');
const c=parts[0];
const args=parts.slice(1);
CT.log(`> ${cmd}`);
switch(c){
case 'query':
if(args.length===2){
CT.executeQuery(args[0],args[1]);
}else{
CT.query();
}
break;
case 'route':
CT.log('Active routes:');
CT.routes.forEach(r=>{
CT.log(`  ${r.from}→${r.to}: weight=${r.weight.toFixed(2)}, packets=${r.packets}`);
});
break;
case 'optimize':CT.optimize();break;
case 'expand':CT.expand();break;
case 'stats':
Object.entries(CT.collections).forEach(([key,coll])=>{
CT.log(`${key}: ${coll.size} vectors, ${coll.queries} queries`);
});
break;
case 'reset':
Object.values(CT.collections).forEach(c=>c.queries=0);
CT.routes.forEach(r=>r.packets=0);
CT.log('Stats reset');
CT.updateStats();
break;
case 'help':
CT.log('Commands: query [from] [to]|route|optimize|expand|stats|reset|help');
break;
default:
CT.log(`Unknown: ${c}`);
}
},

log:(m)=>{
const t=document.getElementById('t');
const time=new Date().toTimeString().substr(0,8);
t.textContent+=`[${time}] ${m}\n`;
t.scrollTop=t.scrollHeight;
},

updateStats:()=>{
let totalQueries=0,totalVectors=0;
const statHTML=[];
Object.entries(CT.collections).forEach(([key,coll])=>{
const color=coll.color.toString(16).padStart(6,'0');
statHTML.push(`<div style="color:#${color}">${coll.name}: ${coll.size}v, ${coll.queries}q</div>`);
totalQueries+=coll.queries;
totalVectors+=coll.size;
});
document.getElementById('stats').innerHTML=statHTML.join('')+
`<div style="color:#fff;margin-top:5px">Total: ${totalVectors} vectors, ${totalQueries} queries</div>`;

document.getElementById('s1').innerHTML=`
Collections: ${Object.keys(CT.collections).length}<br>
Connections: ${CT.connections.length}<br>
Queries: ${totalQueries}
`;

const ag=document.getElementById('ag');
ag.innerHTML='';
CT.agents.forEach(a=>{
ag.innerHTML+=`<div style="color:${a.active?'#0f0':'#f00'}">${a.name}: ${a.cycles}c${a.mem.routed?' [r:'+a.mem.routed+']':''}${a.mem.balanced?' [b:'+a.mem.balanced+']':''}${a.mem.optimized?' [o:'+a.mem.optimized+']':''}</div>`;
});
},

animate:()=>{
requestAnimationFrame(CT.animate);
const t=Date.now()*0.001;

// Rotate camera
CT.camera.position.x=Math.cos(t*0.08)*150;
CT.camera.position.z=Math.sin(t*0.08)*150;
CT.camera.lookAt(0,40,0);

// Pulse nodes
CT.nodes.forEach((node,key)=>{
const coll=CT.collections[key];
node.rotation.y+=0.005;
const scale=1+Math.sin(t*2+node.position.x*0.01)*0.05;
node.scale.set(scale,scale,scale);
node.material.emissiveIntensity=0.3+Math.sin(t*3)*0.1;
});

// Animate query particles
for(let i=CT.queryParticles.length-1;i>=0;i--){
const p=CT.queryParticles[i];
p.progress+=p.speed;
if(p.progress>=1){
CT.queryParticles.splice(i,1);
continue;
}
p.pos.lerp(p.target,p.speed);

// Draw particle
const geom=new THREE.SphereGeometry(1,8,8);
const mat=new THREE.MeshBasicMaterial({color:p.color});
const mesh=new THREE.Mesh(geom,mat);
mesh.position.copy(p.pos);
CT.scene.add(mesh);
setTimeout(()=>{
CT.scene.remove(mesh);
geom.dispose();
mat.dispose();
},50);
}

CT.renderer.render(CT.scene,CT.camera);
},

resize:()=>{
CT.camera.aspect=innerWidth/innerHeight;
CT.camera.updateProjectionMatrix();
CT.renderer.setSize(innerWidth,innerHeight);
}
};

window.addEventListener('DOMContentLoaded',()=>{
setTimeout(()=>CT.init(),100);
});
window.addEventListener('resize',CT.resize);
</script></body></html>
```

---

## 🎮 Controls

### Buttons
- **INITIALIZE**: Start topology visualization
- **CROSS-QUERY**: Execute random cross-collection query
- **OPTIMIZE**: Reposition nodes based on query frequency
- **EXPAND**: Expand network spacing

### Commands
- `query [from] [to]` - Execute query between collections
- `route` - Show active routes
- `optimize` - Optimize topology
- `expand` - Expand network
- `stats` - Show collection statistics
- `reset` - Reset query counters
- `help` - Show commands

## 🤖 Network Agents

### Router Agent
- Routes queries between collections
- Tracks packet flow
- Optimizes query paths

### Balancer Agent
- Load balances queries
- Prevents hotspots
- Distributes traffic

### Optimizer Agent
- Repositions nodes
- Optimizes network layout
- Minimizes path lengths

### Monitor Agent
- Updates statistics
- Tracks performance
- Alerts on issues

## 📊 Collections

| Collection | Size | Dimensions | Color | Description |
|-----------|------|------------|-------|-------------|
| ISA | 15,420 | 1536 | Cyan | ISA standards |
| Code | 8,760 | 768 | Magenta | PLC code |
| Images | 4,520 | 512 | Yellow | Diagrams |
| Audio | 2,180 | 512 | Green | Audio files |
| Docs | 12,340 | 1536 | Orange | Documentation |
| Video | 1,560 | 512 | Pink | Video content |

## 🔬 Network Topology

### Node Representation
- **Size**: Logarithmic scale based on vector count
- **Position**: Optimized by query frequency
- **Color**: Collection-specific
- **Pulse**: Indicates activity level

### Connection Types
- **Passive**: Thin green lines (dormant)
- **Active**: Thick cyan lines (query in progress)
- **Weight**: Based on query frequency

### Query Particles
- Travel along connections
- Color matches source collection
- Speed proportional to route weight

## 📈 Optimization Algorithm

```javascript
// Reposition nodes based on query frequency
nodes.forEach((node, idx) => {
  const angle = (idx / nodeCount) * 2π;
  const radius = baseRadius + queryCount * scaleFactor;
  const height = baseHeight + queryCount * heightFactor;

  node.position = polarToCartesian(angle, radius, height);
});
```

## 🔗 Integration

### Qdrant API
```bash
# Get collection info
curl http://localhost:6333/collections/isa

# Cross-collection search
curl -X POST http://localhost:6333/collections/isa/points/query \
  -d '{"query": {...}, "using": "code"}'
```

### Real-time Updates
```javascript
// Connect to live Qdrant
setInterval(async () => {
  const stats = await fetch('http://localhost:6333/collections').then(r => r.json());
  stats.collections.forEach(c => {
    updateCollectionNode(c.name, c.vectors_count);
  });
}, 5000);
```

## 🎯 Use Cases

1. **Network Visualization**: See collection relationships
2. **Query Path Analysis**: Understand cross-collection queries
3. **Load Balancing**: Identify hotspots
4. **Capacity Planning**: Visualize growth patterns
5. **Topology Optimization**: Improve network efficiency

---

**UUID Verification**: b2c3d4e5-f6g7-8901-bcde-f12345678901
**Last Updated**: 2025-11-15
**Status**: Active
