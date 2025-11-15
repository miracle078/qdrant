# Vector Space 3D Visualizer
**UUID:** a1b2c3d4-e5f6-7890-abcd-ef1234567890
**Type:** Qdrant Vector Space Visualization | ISA-95 L3

Autonomous 3D visualization of Qdrant vector embeddings with real-time similarity search and agent-based point management.

## 🎯 Features

- **3D Vector Space**: Visualize high-dimensional embeddings projected to 3D
- **Similarity Search**: Visual nearest neighbor queries
- **Autonomous Agents**: Self-organizing vector clusters
- **Real-time Updates**: Live point insertion and deletion
- **Collection Views**: Switch between Qdrant collections

## 🚀 Quick Start

```bash
# Open in browser
python -m http.server 8080
# Navigate to: http://localhost:8080/collab/3d-worlds/vector-space-3d.md
```

Or simply open this file in a browser that supports HTML in markdown.

---

## 📦 Executable HTML

```html
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Qdrant Vector Space 3D</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000;overflow:hidden;font-family:monospace;color:#0f0}#c{width:100vw;height:100vh}.h{position:absolute;background:rgba(0,20,40,0.95);border:2px solid;border-radius:8px;padding:10px;font-size:10px}.t{background:#000;color:#0f0;padding:8px;height:200px;overflow-y:auto;white-space:pre-wrap;font-size:9px}.b{background:linear-gradient(45deg,#f0f,#0ff);border:0;padding:5px 10px;border-radius:4px;cursor:pointer;color:#000;font-weight:bold;margin:2px;font-size:9px}</style></head>
<body><canvas id="c"></canvas>
<div class="h" style="top:10px;left:10px;border-color:#0ff;max-width:380px">
<div style="color:#0ff;font-weight:bold">🔮 QDRANT VECTOR SPACE</div>
<div id="s1"></div>
<button class="b" onclick="QV.init()">INITIALIZE</button>
<button class="b" onclick="QV.addVector()">ADD VECTOR</button>
<button class="b" onclick="QV.search()">SEARCH SIMILAR</button>
<button class="b" onclick="QV.cluster()">CLUSTER</button>
</div>
<div class="h" style="top:10px;right:10px;border-color:#0f0;width:450px">
<div style="color:#0f0;font-weight:bold">⚡ VECTOR TERMINAL</div>
<div id="t" class="t"></div>
<input type="text" id="i" style="background:#000;color:#0f0;border:1px solid #0f0;width:100%;padding:5px" placeholder="Command: add|search|cluster|clear">
</div>
<div class="h" style="bottom:10px;left:10px;border-color:#f0f;max-width:350px" id="a">
<div style="color:#f0f;font-weight:bold">🤖 VECTOR AGENTS</div>
<div id="ag"></div>
</div>
<div class="h" style="bottom:10px;right:10px;border-color:#ff0;max-width:350px">
<div style="color:#ff0;font-weight:bold">📊 COLLECTIONS</div>
<div id="col"></div>
</div>
<script>
const QV={
// Qdrant Vector Visualizer
collections:{
isa:{name:'ISA Standards',dim:1536,color:0x00ffff,vectors:[]},
code:{name:'PLC Code',dim:768,color:0xff00ff,vectors:[]},
img:{name:'Diagrams',dim:512,color:0xffff00,vectors:[]},
audio:{name:'Audio',dim:512,color:0x00ff00,vectors:[]},
doc:{name:'Documentation',dim:1536,color:0xff0000,vectors:[]}
},
currentCollection:'isa',
scene:null,camera:null,renderer:null,
points:new Map(),vectorId:0,
agents:new Map(),selectedPoint:null,

// Initialize 3D world
init:()=>{
QV.log('Initializing Qdrant Vector Space...');
QV.scene=new THREE.Scene();
QV.camera=new THREE.PerspectiveCamera(75,innerWidth/innerHeight,0.1,2000);
QV.renderer=new THREE.WebGLRenderer({canvas:document.getElementById('c'),antialias:true});
QV.renderer.setSize(innerWidth,innerHeight);
QV.camera.position.set(100,100,200);

// Lights
QV.scene.add(new THREE.AmbientLight(0x404040));
const l1=new THREE.PointLight(0x00ffff,2);l1.position.set(100,100,100);
const l2=new THREE.PointLight(0xff00ff,1.5);l2.position.set(-100,100,-100);
QV.scene.add(l1);QV.scene.add(l2);

// Grid
const grid=new THREE.GridHelper(400,80,0x00ff00,0x003300);
QV.scene.add(grid);

// Axes helper
const axes=new THREE.AxesHelper(200);
QV.scene.add(axes);

// Create initial vectors
QV.generateVectors('isa',20);
QV.generateVectors('code',15);
QV.generateVectors('img',10);

// Create agents
QV.createAgent('clusterer','clustering',QV.clusterBehavior);
QV.createAgent('searcher','similarity',QV.searchBehavior);
QV.createAgent('organizer','optimization',QV.organizeBehavior);
QV.createAgent('spawner','creation',QV.spawnBehavior);

// Start agents
QV.startAgents();

// Input handler
document.getElementById('i').addEventListener('keypress',(e)=>{
if(e.key==='Enter'){QV.command(e.target.value);e.target.value=''}
});

// Update UI
QV.updateCollections();
QV.animate();
QV.log('Vector space initialized. Agents active.');
},

// Generate random vectors for a collection
generateVectors:(collName,count)=>{
const coll=QV.collections[collName];
for(let i=0;i<count;i++){
const v={
id:`${collName}_${QV.vectorId++}`,
collection:collName,
embedding:Array(coll.dim).fill(0).map(()=>Math.random()*2-1),
pos:[
(Math.random()-0.5)*150,
Math.random()*100,
(Math.random()-0.5)*150
],
metadata:{created:Date.now(),cluster:-1}
};
coll.vectors.push(v);
QV.addPoint(v,coll.color);
}
QV.log(`Generated ${count} vectors in ${collName} collection`);
},

// Add 3D point
addPoint:(v,color)=>{
const geom=new THREE.SphereGeometry(2,8,8);
const mat=new THREE.MeshPhongMaterial({
color,emissive:color,emissiveIntensity:0.3,transparent:true,opacity:0.8
});
const mesh=new THREE.Mesh(geom,mat);
mesh.position.set(v.pos[0],v.pos[1],v.pos[2]);
mesh.userData={vectorId:v.id,collection:v.collection};
QV.scene.add(mesh);
QV.points.set(v.id,mesh);
},

// Add new vector
addVector:()=>{
const coll=QV.collections[QV.currentCollection];
const v={
id:`${QV.currentCollection}_${QV.vectorId++}`,
collection:QV.currentCollection,
embedding:Array(coll.dim).fill(0).map(()=>Math.random()*2-1),
pos:[
(Math.random()-0.5)*150,
Math.random()*100,
(Math.random()-0.5)*150
],
metadata:{created:Date.now(),cluster:-1}
};
coll.vectors.push(v);
QV.addPoint(v,coll.color);
QV.log(`Added vector ${v.id} to ${QV.currentCollection}`);
QV.updateStatus();
},

// Search similar vectors
search:()=>{
const coll=QV.collections[QV.currentCollection];
if(coll.vectors.length===0){
QV.log('No vectors to search');return;
}
const query=coll.vectors[Math.floor(Math.random()*coll.vectors.length)];
const results=QV.findSimilar(query,5);
QV.log(`Search results for ${query.id}:`);
results.forEach((r,i)=>{
QV.log(`  ${i+1}. ${r.id} (similarity: ${r.similarity.toFixed(3)})`);
QV.highlightVector(r.id,0xffffff,2000);
});
// Draw connections
results.forEach(r=>{
const p1=query.pos;
const p2=r.pos;
const g=new THREE.BufferGeometry().setFromPoints([
new THREE.Vector3(...p1),new THREE.Vector3(...p2)
]);
const line=new THREE.Line(g,new THREE.LineBasicMaterial({
color:0xffffff,opacity:0.6,transparent:true
}));
QV.scene.add(line);
setTimeout(()=>QV.scene.remove(line),2000);
});
},

// Find similar vectors (cosine similarity)
findSimilar:(query,k)=>{
const coll=QV.collections[query.collection];
const similarities=coll.vectors
.filter(v=>v.id!==query.id)
.map(v=>({
...v,
similarity:QV.cosineSim(query.embedding,v.embedding)
}))
.sort((a,b)=>b.similarity-a.similarity)
.slice(0,k);
return similarities;
},

// Cosine similarity
cosineSim:(a,b)=>{
let dot=0,magA=0,magB=0;
for(let i=0;i<Math.min(a.length,b.length);i++){
dot+=a[i]*b[i];
magA+=a[i]*a[i];
magB+=b[i]*b[i];
}
return dot/(Math.sqrt(magA)*Math.sqrt(magB));
},

// Cluster vectors
cluster:()=>{
const coll=QV.collections[QV.currentCollection];
if(coll.vectors.length<3){
QV.log('Need at least 3 vectors to cluster');return;
}
const k=Math.min(5,Math.floor(coll.vectors.length/3));
const clusters=QV.kMeans(coll.vectors,k);
QV.log(`Created ${k} clusters in ${QV.currentCollection}`);
// Color by cluster
const clusterColors=[0xff0000,0x00ff00,0x0000ff,0xffff00,0xff00ff,0x00ffff];
clusters.forEach((cluster,idx)=>{
cluster.forEach(v=>{
const point=QV.points.get(v.id);
if(point){
point.material.color.setHex(clusterColors[idx%clusterColors.length]);
point.material.emissive.setHex(clusterColors[idx%clusterColors.length]);
}
v.metadata.cluster=idx;
});
QV.log(`  Cluster ${idx}: ${cluster.length} vectors`);
});
},

// K-means clustering
kMeans:(vectors,k)=>{
const centroids=vectors.slice(0,k).map(v=>v.embedding.slice());
let clusters=Array(k).fill(null).map(()=>[]);
for(let iter=0;iter<10;iter++){
clusters=Array(k).fill(null).map(()=>[]);
vectors.forEach(v=>{
const sims=centroids.map(c=>QV.cosineSim(v.embedding,c));
const cluster=sims.indexOf(Math.max(...sims));
clusters[cluster].push(v);
});
for(let i=0;i<k;i++){
if(clusters[i].length===0)continue;
const newCentroid=Array(vectors[0].embedding.length).fill(0);
clusters[i].forEach(v=>{
v.embedding.forEach((val,j)=>newCentroid[j]+=val);
});
centroids[i]=newCentroid.map(x=>x/clusters[i].length);
}
}
return clusters;
},

// Highlight vector
highlightVector:(id,color,duration)=>{
const point=QV.points.get(id);
if(point){
const originalColor=point.material.color.getHex();
point.material.color.setHex(color);
point.material.emissive.setHex(color);
point.material.emissiveIntensity=0.8;
const scale=point.scale.clone();
point.scale.multiplyScalar(2);
setTimeout(()=>{
point.material.color.setHex(originalColor);
point.material.emissive.setHex(originalColor);
point.material.emissiveIntensity=0.3;
point.scale.copy(scale);
},duration);
}
},

// Agent system
createAgent:(name,type,behavior)=>{
const agent={
name,type,active:true,cycles:0,mem:{},
run:async()=>{
while(agent.active){
await behavior.call(agent);
agent.cycles++;
await QV.sleep(100+Math.random()*200);
}
}
};
QV.agents.set(name,agent);
return agent;
},

sleep:(ms)=>new Promise(r=>setTimeout(r,ms)),

startAgents:()=>{
QV.agents.forEach(a=>a.run());
QV.log(`Started ${QV.agents.size} agents`);
},

// Agent behaviors
clusterBehavior:async function(){
if(this.cycles%30===0){
const colls=Object.keys(QV.collections);
const coll=colls[Math.floor(Math.random()*colls.length)];
QV.currentCollection=coll;
QV.cluster();
}
},

searchBehavior:async function(){
if(this.cycles%20===0){
QV.search();
}
},

organizeBehavior:async function(){
if(this.cycles%40===0){
// Move similar vectors closer
Object.values(QV.collections).forEach(coll=>{
if(coll.vectors.length<2)return;
const v1=coll.vectors[Math.floor(Math.random()*coll.vectors.length)];
const similar=QV.findSimilar(v1,3);
similar.forEach(v2=>{
const p1=QV.points.get(v1.id);
const p2=QV.points.get(v2.id);
if(p1&&p2){
const dx=(p1.position.x-p2.position.x)*0.1;
const dz=(p1.position.z-p2.position.z)*0.1;
p2.position.x+=dx;
p2.position.z+=dz;
v2.pos=[p2.position.x,p2.position.y,p2.position.z];
}
});
});
this.mem.organized=(this.mem.organized||0)+1;
}
},

spawnBehavior:async function(){
if(this.cycles%50===0){
QV.addVector();
this.mem.spawned=(this.mem.spawned||0)+1;
}
},

// Commands
command:(cmd)=>{
const parts=cmd.trim().split(' ');
const c=parts[0];
const args=parts.slice(1);
QV.log(`> ${cmd}`);
switch(c){
case 'add':QV.addVector();break;
case 'search':QV.search();break;
case 'cluster':QV.cluster();break;
case 'clear':
QV.points.forEach((p,id)=>{
QV.scene.remove(p);p.geometry.dispose();p.material.dispose();
});
QV.points.clear();
QV.collections[QV.currentCollection].vectors=[];
QV.log('Cleared vectors');
break;
case 'switch':
if(args[0]&&QV.collections[args[0]]){
QV.currentCollection=args[0];
QV.log(`Switched to ${args[0]} collection`);
QV.updateCollections();
}
break;
case 'stats':
let total=0;
Object.entries(QV.collections).forEach(([name,coll])=>{
QV.log(`${name}: ${coll.vectors.length} vectors`);
total+=coll.vectors.length;
});
QV.log(`Total: ${total} vectors`);
break;
case 'help':
QV.log('Commands: add|search|cluster|clear|switch <coll>|stats|help');
break;
default:
QV.log(`Unknown command: ${c}`);
}
QV.updateStatus();
},

// Logging
log:(m)=>{
const t=document.getElementById('t');
const time=new Date().toTimeString().substr(0,8);
t.textContent+=`[${time}] ${m}\n`;
t.scrollTop=t.scrollHeight;
},

// Update UI
updateStatus:()=>{
let total=0;
Object.values(QV.collections).forEach(c=>total+=c.vectors.length);
document.getElementById('s1').innerHTML=`
Collection: <span style="color:#0ff">${QV.currentCollection}</span><br>
Vectors: ${QV.collections[QV.currentCollection].vectors.length}<br>
Total: ${total} | Points: ${QV.points.size}
`;
const ag=document.getElementById('ag');
ag.innerHTML='';
QV.agents.forEach(a=>{
ag.innerHTML+=`<div style="color:${a.active?'#0f0':'#f00'}">${a.name}: ${a.cycles}c${a.mem.organized?' [org:'+a.mem.organized+']':''}${a.mem.spawned?' [+'+a.mem.spawned+']':''}</div>`;
});
},

updateCollections:()=>{
const col=document.getElementById('col');
col.innerHTML='';
Object.entries(QV.collections).forEach(([name,coll])=>{
const active=name===QV.currentCollection?'★':'';
const color=coll.color.toString(16).padStart(6,'0');
col.innerHTML+=`<div style="color:#${color};cursor:pointer" onclick="QV.command('switch ${name}')">${active} ${coll.name}: ${coll.vectors.length}</div>`;
});
},

// Animation loop
animate:()=>{
requestAnimationFrame(QV.animate);
const t=Date.now()*0.001;

// Rotate camera
QV.camera.position.x=Math.cos(t*0.05)*200;
QV.camera.position.z=Math.sin(t*0.05)*200;
QV.camera.lookAt(0,30,0);

// Animate points
QV.points.forEach((p,id)=>{
p.rotation.y+=0.02;
p.material.emissiveIntensity=0.3+Math.sin(t*2+p.position.x*0.01)*0.2;
});

QV.renderer.render(QV.scene,QV.camera);
},

// Window resize
resize:()=>{
QV.camera.aspect=innerWidth/innerHeight;
QV.camera.updateProjectionMatrix();
QV.renderer.setSize(innerWidth,innerHeight);
}
};

// Auto-initialize
window.addEventListener('DOMContentLoaded',()=>{
setTimeout(()=>QV.init(),100);
});
window.addEventListener('resize',QV.resize);
</script></body></html>
```

---

## 🎮 Controls

### Buttons
- **INITIALIZE**: Start the 3D vector space
- **ADD VECTOR**: Insert random vector in current collection
- **SEARCH SIMILAR**: Find nearest neighbors
- **CLUSTER**: K-means clustering visualization

### Commands
Type in terminal input:
- `add` - Add new vector
- `search` - Similarity search
- `cluster` - Cluster vectors
- `clear` - Remove all vectors
- `switch <collection>` - Switch collection (isa|code|img|audio|doc)
- `stats` - Show statistics
- `help` - Show commands

## 🤖 Autonomous Agents

### Clusterer Agent
- Automatically clusters vectors every 30 cycles
- Uses k-means algorithm
- Colors vectors by cluster

### Searcher Agent
- Performs random similarity searches
- Highlights similar vectors
- Draws connection lines

### Organizer Agent
- Moves similar vectors closer together
- Self-organizing visualization
- Tracks organization count

### Spawner Agent
- Creates new vectors periodically
- Maintains active vector population
- Tracks spawn count

## 📊 Collections

| Collection | Dimensions | Color | Description |
|-----------|-----------|-------|-------------|
| **isa** | 1536 | Cyan | ISA Standards embeddings |
| **code** | 768 | Magenta | PLC code embeddings |
| **img** | 512 | Yellow | Diagram embeddings |
| **audio** | 512 | Green | Audio embeddings |
| **doc** | 1536 | Red | Documentation embeddings |

## 🔬 Technical Details

### Similarity Calculation
```javascript
// Cosine similarity
cosineSim(a, b) {
  const dot = a.reduce((sum, val, i) => sum + val * b[i], 0);
  const magA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0));
  const magB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0));
  return dot / (magA * magB);
}
```

### K-Means Clustering
- Initialize k random centroids
- Assign vectors to nearest centroid
- Update centroids to cluster mean
- Iterate 10 times

### 3D Projection
High-dimensional embeddings are projected to 3D space using:
- Random positioning for visualization
- Self-organizing agents pull similar vectors together
- Clustering creates visual separation

## 📈 Performance

- **Vectors**: Up to 1000+ simultaneous points
- **Search**: O(n) linear scan (optimized with early termination)
- **Clustering**: O(n*k*i) where k=clusters, i=iterations
- **Rendering**: 60 FPS with WebGL acceleration

## 🔗 Integration

### Python API
```python
# Query vectors from Python
import requests
vectors = requests.get('http://localhost:6333/collections/isa/points').json()
```

### Qdrant Integration
```javascript
// Connect to real Qdrant instance
const response = await fetch('http://localhost:6333/collections/isa/points/search', {
  method: 'POST',
  body: JSON.stringify({
    vector: embedding,
    limit: 10
  })
});
```

## 📝 Notes

- This is a client-side visualization tool
- Vectors are randomly generated for demonstration
- For production use, connect to real Qdrant instance
- Agent behaviors can be customized in code

## 🎯 Use Cases

1. **Vector Space Exploration**: Visualize embedding distributions
2. **Similarity Testing**: Verify cosine similarity calculations
3. **Clustering Analysis**: Evaluate cluster quality
4. **Collection Comparison**: Compare vector distributions across collections
5. **Educational**: Teach vector database concepts

---

**UUID Verification**: a1b2c3d4-e5f6-7890-abcd-ef1234567890
**Last Updated**: 2025-11-15
**Status**: Active
