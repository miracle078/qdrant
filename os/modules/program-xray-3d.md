# X-Ray 3D Viewer
**Three.js Visualization** | DICOM | ISA-95 L2

3D visualization of medical images using Three.js.

```javascript
console.log('📊 3D Medical Viewer Demo\n');

// 1. Check if Three.js is available
if (typeof THREE === 'undefined') {
  console.log('⚠️ Three.js not loaded. Include:');
  console.log('   <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>');
  return { error: 'Three.js required' };
}

// 2. Create container if not exists
let container = document.getElementById('dicom-viewer-3d');
if (!container) {
  container = document.createElement('div');
  container.id = 'dicom-viewer-3d';
  container.style.cssText = `
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 600px;
    height: 600px;
    background: #000;
    border: 2px solid #00ff88;
    z-index: 10000;
  `;
  document.body.appendChild(container);
}

// 3. Initialize viewer
console.log('Initializing 3D viewer...');
DicomViewer3D.init('dicom-viewer-3d');

// 4. Load sample x-ray
console.log('Loading x-ray as 3D plane...');
const sample = MedicalDataset.get('chest-001');
DicomViewer3D.loadXRay(sample.url);

// 5. Instructions
console.log('\n✅ 3D Viewer active!');
console.log('   • Viewer rotating automatically');
console.log('   • Close by removing #dicom-viewer-3d element');

// 6. Add close button
const closeBtn = document.createElement('button');
closeBtn.textContent = '✖ Close';
closeBtn.style.cssText = `
  position: absolute;
  top: 10px;
  right: 10px;
  background: #00ff88;
  color: #000;
  border: none;
  padding: 5px 15px;
  cursor: pointer;
  z-index: 10001;
`;
closeBtn.onclick = () => container.remove();
container.appendChild(closeBtn);

ChangeLog.record('3d_viewer_opened', { sample: sample.id });

return {
  success: true,
  viewer: 'active',
  sample: sample.id
};
```
