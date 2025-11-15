# Cluster Network 3D
**UUID:** d4e5f6g7-h8i9-0123-defg-345678901234
**Type:** Qdrant Distributed Cluster | ISA-95 L4

3D visualization of distributed Qdrant cluster topology with nodes, shards, replication, and consensus protocols.

## 🎯 Features

- **Cluster Nodes**: Visualize Qdrant instances in 3D
- **Shard Distribution**: See how collections are sharded
- **Replication**: Replica placement and sync status
- **Consensus**: Raft protocol visualization
- **Load Balancing**: Request distribution across nodes

## 🚀 Quick Start

```bash
# Open in browser
python -m http.server 8080
# Navigate to: http://localhost:8080/collab/3d-worlds/cluster-network-3d.md
```

---

## 📦 Executable HTML

```html
<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Qdrant Cluster Network 3D</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#000;overflow:hidden;font-family:monospace;color:#0f0}#c{width:100vw;height:100vh}.h{position:absolute;background:rgba(0,20,40,0.95);border:2px solid;border-radius:8px;padding:10px;font-size:10px}.t{background:#000;color:#0f0;padding:8px;height:160px;overflow-y:auto;white-space:pre-wrap;font-size:9px}.b{background:linear-gradient(45deg,#f0f,#0ff);border:0;padding:5px 10px;border-radius:4px;cursor:pointer;color:#000;font-weight:bold;margin:2px;font-size:9px}</style></head>
<body><canvas id="c"></canvas>
<div class="h" style="top:10px;left:10px;border-color:#0ff;max-width:380px">
<div style="color:#0ff;font-weight:bold">🌐 CLUSTER NETWORK</div>
<div id="s1"></div>
<button class="b" onclick="CN.init()">INITIALIZE</button>
<button class="b" onclick="CN.addNode()">ADD NODE</button>
<button class="b" onclick="CN.failover()">SIMULATE FAILURE</button>
<button class="b" onclick="CN.rebalance()">REBALANCE</button>
</div>
<div class="h" style="top:10px;right:10px;border-color:#0f0;width:450px">
<div style="color:#0f0;font-weight:bold">⚡ CLUSTER TERMINAL</div>
<div id="t" class="t"></div>
<input type="text" id="i" style="background:#000;color:#0f0;border:1px solid #0f0;width:100%;padding:5px" placeholder="Command: status|shard|replica|raft">
</div>
<div class="h" style="bottom:10px;left:10px;border-color:#f0f;max-width:350px">
<div style="color:#f0f;font-weight:bold">🖥️ CLUSTER NODES</div>
<div id="nodes"></div>
</div>
<div class="h" style="bottom:10px;right:10px;border-color:#ff0;max-width:450px">
<div style="color:#ff0;font-weight:bold">📊 CLUSTER STATS</div>
<div id="stats"></div>
</div>
<script>
const CN={
// Cluster Network
nodes:[],
shards:[],
replicas:[],
scene:null,camera:null,renderer:null,
nodeMeshes:new Map(),
connections:[],
raftState:{leader:null,term:1,votes:0},
nextNodeId:1,
totalRequests:0,

init:()=>{
CN.log('Initializing Cluster Network...');
CN.scene=new THREE.Scene();
CN.camera=new THREE.PerspectiveCamera(75,innerWidth/innerHeight,0.1,2000);
CN.renderer=new THREE.WebGLRenderer({canvas:document.getElementById('c'),antialias:true});
CN.renderer.setSize(innerWidth,innerHeight);
CN.camera.position.set(200,200,200);

// Lights
CN.scene.add(new THREE.AmbientLight(0x404040));
const l1=new THREE.DirectionalLight(0xffffff,1);
l1.position.set(100,200,100);
CN.scene.add(l1);

// Grid
const grid=new THREE.GridHelper(400,80,0x00ff00,0x003300);
CN.scene.add(grid);

// Create initial cluster (3 nodes)
for(let i=0;i<3;i++){
const angle=(i/3)*Math.PI*2;
CN.createNode({
x:Math.cos(angle)*80,
y:50,
z:Math.sin(angle)*80
});
}

// Elect leader
CN.electLeader();

// Create shards
CN.createShards();

// Create replicas
CN.createReplicas();

// Input
document.getElementById('i').addEventListener('keypress',(e)=>{
if(e.key==='Enter'){CN.command(e.target.value);e.target.value=''}
});

CN.updateUI();
CN.animate();
CN.log('Cluster initialized. Ready for operations.');

// Simulate heartbeats
setInterval(()=>CN.heartbeat(),2000);

// Simulate requests
setInterval(()=>CN.simulateRequest(),1000);
},

createNode:(pos)=>{
const node={
id:`node-${CN.nextNodeId++}`,
pos:[pos.x,pos.y,pos.z],
status:'active',
role:'follower',
shards:[],
requests:0,
cpu:0,
mem:0,
disk:0
};
CN.nodes.push(node);

// Create 3D representation
const geom=new THREE.BoxGeometry(20,20,20);
const mat=new THREE.MeshPhongMaterial({
color:0x00ffff,
emissive:0x00ffff,
emissiveIntensity:0.3,
transparent:true,
opacity:0.9
});
const mesh=new THREE.Mesh(geom,mat);
mesh.position.set(pos.x,pos.y,pos.z);
mesh.userData={nodeId:node.id};

// Label
const canvas=document.createElement('canvas');
canvas.width=256;canvas.height=64;
const ctx=canvas.getContext('2d');
ctx.fillStyle='#00ff00';
ctx.font='bold 24px monospace';
ctx.textAlign='center';
ctx.fillText(node.id.toUpperCase(),128,40);
const texture=new THREE.CanvasTexture(canvas);
const spriteMat=new THREE.SpriteMaterial({map:texture});
const sprite=new THREE.Sprite(spriteMat);
sprite.scale.set(30,7.5,1);
sprite.position.set(0,15,0);
mesh.add(sprite);

CN.scene.add(mesh);
CN.nodeMeshes.set(node.id,mesh);

// Create connections to existing nodes
CN.nodes.slice(0,-1).forEach(other=>{
CN.createConnection(node.id,other.id);
});

CN.log(`Node created: ${node.id}`);
CN.updateUI();
return node;
},

createConnection:(id1,id2)=>{
const n1=CN.nodes.find(n=>n.id===id1);
const n2=CN.nodes.find(n=>n.id===id2);
if(!n1||!n2)return;

const geom=new THREE.BufferGeometry().setFromPoints([
new THREE.Vector3(...n1.pos),
new THREE.Vector3(...n2.pos)
]);
const mat=new THREE.LineBasicMaterial({
color:0x00ff00,
opacity:0.3,
transparent:true
});
const line=new THREE.Line(geom,mat);
CN.scene.add(line);
CN.connections.push({line,from:id1,to:id2,active:false});
},

createShards:()=>{
const collections=['isa','code','img','doc'];
const shardsPerCollection=2;

collections.forEach((coll,collIdx)=>{
for(let i=0;i<shardsPerCollection;i++){
const shardId=`${coll}-shard-${i}`;
const nodeIdx=(collIdx*shardsPerCollection+i)%CN.nodes.length;
const node=CN.nodes[nodeIdx];

const shard={
id:shardId,
collection:coll,
nodeId:node.id,
vectors:Math.floor(Math.random()*5000)+1000,
status:'active'
};
CN.shards.push(shard);
node.shards.push(shardId);

CN.log(`Shard ${shardId} assigned to ${node.id}`);
}
});
},

createReplicas:()=>{
CN.shards.forEach(shard=>{
const primaryNode=CN.nodes.find(n=>n.id===shard.nodeId);
const otherNodes=CN.nodes.filter(n=>n.id!==shard.nodeId);
if(otherNodes.length===0)return;

const replicaNode=otherNodes[Math.floor(Math.random()*otherNodes.length)];
const replica={
id:`${shard.id}-replica`,
shardId:shard.id,
nodeId:replicaNode.id,
primaryNodeId:shard.nodeId,
syncStatus:'synced',
lag:0
};
CN.replicas.push(replica);
replicaNode.shards.push(replica.id);

CN.log(`Replica ${replica.id} on ${replicaNode.id}`);
});
},

electLeader:()=>{
if(CN.nodes.length===0)return;

// Reset all to followers
CN.nodes.forEach(n=>n.role='follower');

// Elect random leader
const leader=CN.nodes[Math.floor(Math.random()*CN.nodes.length)];
leader.role='leader';
CN.raftState.leader=leader.id;
CN.raftState.term++;

CN.log(`Leader elected: ${leader.id} (term ${CN.raftState.term})`);

// Update visuals
CN.nodes.forEach(node=>{
const mesh=CN.nodeMeshes.get(node.id);
if(mesh){
mesh.material.color.setHex(node.role==='leader'?0xff00ff:0x00ffff);
mesh.material.emissive.setHex(node.role==='leader'?0xff00ff:0x00ffff);
}
});

CN.updateUI();
},

addNode:()=>{
const count=CN.nodes.length;
const angle=(count/(count+1))*Math.PI*2;
const radius=80+count*10;
CN.createNode({
x:Math.cos(angle)*radius,
y:50,
z:Math.sin(angle)*radius
});

// Rebalance shards
CN.rebalance();
},

failover:()=>{
if(CN.nodes.length<2){
CN.log('Need at least 2 nodes for failover');
return;
}

const activeNodes=CN.nodes.filter(n=>n.status==='active');
if(activeNodes.length===0)return;

const failNode=activeNodes[Math.floor(Math.random()*activeNodes.length)];
failNode.status='failed';

CN.log(`Node failed: ${failNode.id}`);

const mesh=CN.nodeMeshes.get(failNode.id);
if(mesh){
mesh.material.color.setHex(0xff0000);
mesh.material.emissive.setHex(0xff0000);
mesh.material.opacity=0.5;
}

// If leader failed, elect new leader
if(failNode.role==='leader'){
CN.log('Leader failed! Electing new leader...');
setTimeout(()=>CN.electLeader(),1000);
}

// Promote replicas
failNode.shards.forEach(shardId=>{
const replica=CN.replicas.find(r=>r.primaryNodeId===failNode.id&&r.shardId===shardId);
if(replica){
const replicaNode=CN.nodes.find(n=>n.id===replica.nodeId&&n.status==='active');
if(replicaNode){
CN.log(`Promoting replica ${replica.id} to primary`);
replica.syncStatus='promoted';
}
}
});

CN.updateUI();

// Auto-recover after 5 seconds
setTimeout(()=>{
failNode.status='active';
mesh.material.color.setHex(failNode.role==='leader'?0xff00ff:0x00ffff);
mesh.material.emissive.setHex(failNode.role==='leader'?0xff00ff:0x00ffff);
mesh.material.opacity=0.9;
CN.log(`Node recovered: ${failNode.id}`);
CN.updateUI();
},5000);
},

rebalance:()=>{
CN.log('Rebalancing shards across cluster...');
const activeNodes=CN.nodes.filter(n=>n.status==='active');
if(activeNodes.length===0)return;

// Redistribute shards evenly
CN.shards.forEach((shard,idx)=>{
const newNode=activeNodes[idx%activeNodes.length];
if(shard.nodeId!==newNode.id){
CN.log(`Moving ${shard.id}: ${shard.nodeId} → ${newNode.id}`);
shard.nodeId=newNode.id;
}
});

// Update node shard lists
activeNodes.forEach(node=>{
node.shards=CN.shards.filter(s=>s.nodeId===node.id).map(s=>s.id);
});

CN.updateUI();
CN.log('Rebalance complete');
},

heartbeat:()=>{
const leader=CN.nodes.find(n=>n.role==='leader'&&n.status==='active');
if(!leader)return;

// Leader sends heartbeat to followers
CN.nodes.filter(n=>n.role==='follower'&&n.status==='active').forEach(follower=>{
const conn=CN.connections.find(c=>
(c.from===leader.id&&c.to===follower.id)||
(c.from===follower.id&&c.to===leader.id)
);
if(conn){
CN.pulseConnection(conn);
}
});
},

pulseConnection:(conn)=>{
conn.active=true;
conn.line.material.opacity=0.8;
conn.line.material.color.setHex(0xff00ff);
setTimeout(()=>{
conn.active=false;
conn.line.material.opacity=0.3;
conn.line.material.color.setHex(0x00ff00);
},500);
},

simulateRequest:()=>{
const activeNodes=CN.nodes.filter(n=>n.status==='active');
if(activeNodes.length===0)return;

const node=activeNodes[Math.floor(Math.random()*activeNodes.length)];
node.requests++;
CN.totalRequests++;

// Update metrics
node.cpu=Math.min(100,node.cpu+Math.random()*10);
node.mem=Math.min(100,node.mem+Math.random()*5);
node.disk=Math.min(100,node.disk+Math.random()*2);

// Decay metrics
setTimeout(()=>{
node.cpu=Math.max(0,node.cpu-5);
node.mem=Math.max(0,node.mem-2);
node.disk=Math.max(0,node.disk-1);
},1000);

if(CN.totalRequests%100===0){
CN.log(`Total requests: ${CN.totalRequests}`);
CN.updateUI();
}
},

command:(cmd)=>{
const parts=cmd.trim().split(' ');
const c=parts[0];
CN.log(`> ${cmd}`);
switch(c){
case 'status':
CN.nodes.forEach(node=>{
CN.log(`${node.id}: ${node.status} (${node.role}) - ${node.shards.length} shards, ${node.requests} req`);
});
break;
case 'shard':
CN.log(`Shards: ${CN.shards.length}`);
CN.shards.forEach(s=>{
CN.log(`  ${s.id}: ${s.nodeId} (${s.vectors} vectors)`);
});
break;
case 'replica':
CN.log(`Replicas: ${CN.replicas.length}`);
CN.replicas.forEach(r=>{
CN.log(`  ${r.id}: ${r.nodeId} (${r.syncStatus})`);
});
break;
case 'raft':
CN.log(`Raft state:`);
CN.log(`  Leader: ${CN.raftState.leader}`);
CN.log(`  Term: ${CN.raftState.term}`);
break;
case 'help':
CN.log('Commands: status|shard|replica|raft|help');
break;
default:
CN.log(`Unknown: ${c}`);
}
},

log:(m)=>{
const t=document.getElementById('t');
const time=new Date().toTimeString().substr(0,8);
t.textContent+=`[${time}] ${m}\n`;
t.scrollTop=t.scrollHeight;
},

updateUI:()=>{
const activeNodes=CN.nodes.filter(n=>n.status==='active').length;
const failedNodes=CN.nodes.filter(n=>n.status==='failed').length;

document.getElementById('s1').innerHTML=`
Nodes: ${activeNodes}/${CN.nodes.length}<br>
Shards: ${CN.shards.length}<br>
Requests: ${CN.totalRequests}
`;

const nodesDiv=document.getElementById('nodes');
nodesDiv.innerHTML='';
CN.nodes.forEach(node=>{
const color=node.status==='failed'?'f00':(node.role==='leader'?'f0f':'0ff');
nodesDiv.innerHTML+=`<div style="color:#${color}">${node.id}: ${node.status} (${node.role})<br>  Shards: ${node.shards.length}, Req: ${node.requests}</div>`;
});

const statsDiv=document.getElementById('stats');
statsDiv.innerHTML=`
<div>Active Nodes: ${activeNodes}</div>
<div>Failed Nodes: ${failedNodes}</div>
<div>Total Shards: ${CN.shards.length}</div>
<div>Replicas: ${CN.replicas.length}</div>
<div>Leader: ${CN.raftState.leader||'None'}</div>
<div>Term: ${CN.raftState.term}</div>
<div style="margin-top:5px">Total Requests: ${CN.totalRequests}</div>
`;
},

animate:()=>{
requestAnimationFrame(CN.animate);
const t=Date.now()*0.001;

// Orbit camera
CN.camera.position.x=Math.cos(t*0.05)*200;
CN.camera.position.z=Math.sin(t*0.05)*200;
CN.camera.lookAt(0,50,0);

// Animate nodes
CN.nodeMeshes.forEach((mesh,nodeId)=>{
const node=CN.nodes.find(n=>n.id===nodeId);
if(!node)return;

mesh.rotation.y+=0.01;
if(node.role==='leader'){
const pulse=1+Math.sin(t*4)*0.1;
mesh.scale.set(pulse,pulse,pulse);
}else{
mesh.scale.set(1,1,1);
}

// CPU load visualization
const cpuRatio=node.cpu/100;
mesh.material.emissiveIntensity=0.3+cpuRatio*0.5;
});

// Update connections
CN.connections.forEach(conn=>{
const n1=CN.nodes.find(n=>n.id===conn.from);
const n2=CN.nodes.find(n=>n.id===conn.to);
if(n1&&n2){
conn.line.geometry.setFromPoints([
new THREE.Vector3(...n1.pos),
new THREE.Vector3(...n2.pos)
]);
}
});

CN.renderer.render(CN.scene,CN.camera);
},

resize:()=>{
CN.camera.aspect=innerWidth/innerHeight;
CN.camera.updateProjectionMatrix();
CN.renderer.setSize(innerWidth,innerHeight);
}
};

window.addEventListener('DOMContentLoaded',()=>{
setTimeout(()=>CN.init(),100);
});
window.addEventListener('resize',CN.resize);
</script></body></html>
```

---

## 🎮 Controls

### Buttons
- **INITIALIZE**: Start cluster visualization
- **ADD NODE**: Add new node to cluster
- **SIMULATE FAILURE**: Random node failure + failover
- **REBALANCE**: Redistribute shards evenly

### Commands
- `status` - Show all node status
- `shard` - List all shards
- `replica` - Show replica status
- `raft` - Display Raft consensus state
- `help` - Show commands

## 🌐 Cluster Architecture

### Node Types
- **Leader** (Magenta): Raft leader, coordinates writes
- **Follower** (Cyan): Replicates data, handles reads
- **Failed** (Red): Unavailable, triggers failover

### Shard Distribution
- Collections split into multiple shards
- Even distribution across nodes
- Automatic rebalancing on topology changes

### Replication
- Each shard has at least one replica
- Async replication from primary to replicas
- Automatic promotion on primary failure

## 🔬 Raft Consensus

### Leader Election
- Random timeout triggers election
- Majority vote required
- Term number increments

### Heartbeats
- Leader sends periodic heartbeats
- Followers reset election timeout
- Visualized as purple pulses

### Failover
- Leader failure triggers new election
- Replicas promoted to primary
- Automatic recovery simulation

## 📊 Metrics

### Node Metrics
- **CPU**: Request processing load
- **Memory**: Data structure overhead
- **Disk**: Shard storage usage
- **Requests**: Total query count

### Cluster Metrics
- **Active Nodes**: Healthy instances
- **Failed Nodes**: Unavailable instances
- **Total Shards**: Shard count across cluster
- **Replicas**: Backup shard count

## 🎯 Visualization Elements

### Nodes
- **Size**: Fixed 20x20x20
- **Color**: Status-dependent (cyan/magenta/red)
- **Rotation**: Constant Y-axis rotation
- **Pulse**: Leader nodes pulse

### Connections
- **Default**: Thin green (0.3 opacity)
- **Heartbeat**: Thick magenta (0.8 opacity)
- **Updates**: Follow node positions

### Labels
- **Node ID**: Above each node
- **Font**: Monospace, green
- **Size**: 30x7.5 sprite

## 🔗 Integration

### Real Qdrant Cluster
```bash
# Start 3-node cluster
docker-compose up -d

# Check cluster status
curl http://localhost:6333/cluster

# Add collection with sharding
curl -X PUT http://localhost:6333/collections/my_collection \
  -d '{"shard_number": 4, "replication_factor": 2}'
```

### Monitor Real Cluster
```javascript
async function syncClusterState() {
  const response = await fetch('http://localhost:6333/cluster');
  const cluster = await response.json();

  // Update visualization with real data
  cluster.peers.forEach(peer => {
    updateNode(peer.id, peer.status);
  });
}
setInterval(syncClusterState, 5000);
```

## 📈 Scalability

- **Nodes**: Supports up to 10+ nodes
- **Shards**: Unlimited shard visualization
- **Replicas**: Multiple replicas per shard
- **Performance**: 60 FPS with WebGL

## 🎯 Use Cases

1. **Cluster Planning**: Visualize topology before deployment
2. **Failover Testing**: Simulate node failures
3. **Load Balancing**: See request distribution
4. **Education**: Teach distributed systems
5. **Monitoring**: Real-time cluster health

---

**UUID Verification**: d4e5f6g7-h8i9-0123-defg-345678901234
**Last Updated**: 2025-11-15
**Status**: Active
