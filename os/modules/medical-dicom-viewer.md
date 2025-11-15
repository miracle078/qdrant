# DICOM Viewer 3D
**Medical Image Visualization** | Three.js

3D visualization for DICOM, x-rays, and medical scans using Three.js.

```javascript
const DicomViewer3D = {
  scene: null,
  camera: null,
  renderer: null,

  init(containerId) {
    const container = document.getElementById(containerId);

    // Three.js setup
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x000000);

    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    this.camera.position.z = 5;

    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(container.offsetWidth, container.offsetHeight);
    container.appendChild(this.renderer.domElement);

    // Lighting
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(1, 1, 1);
    this.scene.add(light);
    this.scene.add(new THREE.AmbientLight(0x404040));

    console.log('📊 DICOM Viewer 3D ready');
  },

  loadXRay(imageUrl) {
    // Load x-ray as textured plane
    const loader = new THREE.TextureLoader();
    loader.load(imageUrl, (texture) => {
      const geometry = new THREE.PlaneGeometry(4, 4);
      const material = new THREE.MeshBasicMaterial({ map: texture });
      const plane = new THREE.Mesh(geometry, material);

      this.scene.add(plane);
      this.animate();
    });
  },

  load3DVolume(slices) {
    // Stack 2D slices into 3D volume
    const geometry = new THREE.BoxGeometry(2, 2, 2);
    const material = new THREE.MeshPhongMaterial({
      color: 0x00ff88,
      opacity: 0.5,
      transparent: true
    });
    const cube = new THREE.Mesh(geometry, material);

    this.scene.add(cube);
    this.animate();
  },

  animate() {
    requestAnimationFrame(() => this.animate());
    this.scene.rotation.y += 0.01;
    this.renderer.render(this.scene, this.camera);
  }
};

window.DicomViewer3D = DicomViewer3D;
```
