# BERT-Tiny

**Type:** Text Embedding Model
**Framework:** ONNX
**Size:** ~500 KB
**Input:** Token IDs (int64, shape: [batch, seq_len])
**Output:** Embeddings (float32, shape: [batch, seq_len, 128])

## Usage

```javascript
// Load model with ONNX Runtime
const session = await ort.InferenceSession.create('models/bert-tiny/bert-tiny.onnx');

// Prepare input
const inputIds = new ort.Tensor('int64', [101, 2003, 1037, 3231, 102], [1, 5]);

// Run inference
const outputs = await session.run({ input_ids: inputIds });
const embeddings = outputs.output.data;
```

## Pre-trained Alternatives

For production use, download pre-trained models:

```bash
# TinyBERT from Hugging Face
pip install transformers optimum[onnxruntime]
optimum-cli export onnx --model huawei-noah/TinyBERT_General_4L_312D bert-tiny-pretrained/
```

## Medical Use Cases

- Patient note embeddings
- Medical literature search
- Diagnosis code classification
- Clinical trial matching
