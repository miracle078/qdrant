# WebGPU Inference
**UUID:** a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d
**GPU Acceleration** | WebGPU for Client-Side AI

WebGPU-accelerated inference engine for browser-based AI.

```javascript
const WebGPUInference = {
  device: null,
  adapter: null,
  supported: false,

  async init() {
    if (!navigator.gpu) {
      console.warn('WebGPU not supported, falling back to WebGL/WASM');
      this.supported = false;
      return false;
    }

    try {
      this.adapter = await navigator.gpu.requestAdapter();
      if (!this.adapter) {
        this.supported = false;
        return false;
      }

      this.device = await this.adapter.requestDevice();
      this.supported = true;

      console.log('WebGPU initialized:', {
        vendor: this.adapter.info?.vendor,
        architecture: this.adapter.info?.architecture,
        limits: this.device.limits
      });

      return true;
    } catch (err) {
      console.error('WebGPU initialization failed:', err);
      this.supported = false;
      return false;
    }
  },

  getInfo() {
    if (!this.supported) {
      return { supported: false };
    }

    return {
      supported: true,
      vendor: this.adapter.info?.vendor || 'unknown',
      architecture: this.adapter.info?.architecture || 'unknown',
      maxBufferSize: this.device.limits.maxBufferSize,
      maxComputeWorkgroupsPerDimension: this.device.limits.maxComputeWorkgroupsPerDimension
    };
  },

  async matmul(a, b, m, n, k) {
    if (!this.supported) {
      throw new Error('WebGPU not supported');
    }

    // Create buffers
    const aBuffer = this.device.createBuffer({
      size: m * k * Float32Array.BYTES_PER_ELEMENT,
      usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_DST
    });

    const bBuffer = this.device.createBuffer({
      size: k * n * Float32Array.BYTES_PER_ELEMENT,
      usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_DST
    });

    const resultBuffer = this.device.createBuffer({
      size: m * n * Float32Array.BYTES_PER_ELEMENT,
      usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_SRC
    });

    // Write data
    this.device.queue.writeBuffer(aBuffer, 0, a);
    this.device.queue.writeBuffer(bBuffer, 0, b);

    // Create shader
    const shaderModule = this.device.createShaderModule({
      code: `
        @group(0) @binding(0) var<storage, read> a: array<f32>;
        @group(0) @binding(1) var<storage, read> b: array<f32>;
        @group(0) @binding(2) var<storage, read_write> result: array<f32>;

        @compute @workgroup_size(8, 8)
        fn main(@builtin(global_invocation_id) global_id: vec3<u32>) {
          let row = global_id.x;
          let col = global_id.y;

          if (row >= ${m}u || col >= ${n}u) {
            return;
          }

          var sum = 0.0;
          for (var i = 0u; i < ${k}u; i = i + 1u) {
            sum = sum + a[row * ${k}u + i] * b[i * ${n}u + col];
          }

          result[row * ${n}u + col] = sum;
        }
      `
    });

    // Create pipeline
    const pipeline = this.device.createComputePipeline({
      layout: 'auto',
      compute: {
        module: shaderModule,
        entryPoint: 'main'
      }
    });

    // Create bind group
    const bindGroup = this.device.createBindGroup({
      layout: pipeline.getBindGroupLayout(0),
      entries: [
        { binding: 0, resource: { buffer: aBuffer } },
        { binding: 1, resource: { buffer: bBuffer } },
        { binding: 2, resource: { buffer: resultBuffer } }
      ]
    });

    // Execute
    const commandEncoder = this.device.createCommandEncoder();
    const passEncoder = commandEncoder.beginComputePass();
    passEncoder.setPipeline(pipeline);
    passEncoder.setBindGroup(0, bindGroup);
    passEncoder.dispatchWorkgroups(Math.ceil(m / 8), Math.ceil(n / 8));
    passEncoder.end();

    // Read result
    const gpuReadBuffer = this.device.createBuffer({
      size: m * n * Float32Array.BYTES_PER_ELEMENT,
      usage: GPUBufferUsage.COPY_DST | GPUBufferUsage.MAP_READ
    });

    commandEncoder.copyBufferToBuffer(
      resultBuffer, 0,
      gpuReadBuffer, 0,
      m * n * Float32Array.BYTES_PER_ELEMENT
    );

    this.device.queue.submit([commandEncoder.finish()]);

    await gpuReadBuffer.mapAsync(GPUMapMode.READ);
    const result = new Float32Array(gpuReadBuffer.getMappedRange());
    const output = new Float32Array(result);
    gpuReadBuffer.unmap();

    // Cleanup
    aBuffer.destroy();
    bBuffer.destroy();
    resultBuffer.destroy();
    gpuReadBuffer.destroy();

    return output;
  },

  async benchmark() {
    if (!this.supported) {
      return { error: 'WebGPU not supported' };
    }

    const m = 256, n = 256, k = 256;
    const a = new Float32Array(m * k).fill(1.0);
    const b = new Float32Array(k * n).fill(1.0);

    const start = performance.now();
    await this.matmul(a, b, m, n, k);
    const end = performance.now();

    const gflops = (2 * m * n * k) / ((end - start) / 1000) / 1e9;

    return {
      time: end - start,
      gflops,
      matrixSize: `${m}×${k} × ${k}×${n}`
    };
  }
};

window.WebGPUInference = WebGPUInference;
```
