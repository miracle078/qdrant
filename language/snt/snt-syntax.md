# SNT Syntax
**UUID:** 8b2f4e7a-3d6c-4f9e-9a1c-6d5f8e2b4a9c
**Space-Time Notation Language** | High-Level Syntax

SNT language syntax and semantics.

```javascript
const SNTSyntax = {
  // Timeline operators
  timeline: {
    '@past': -1,
    '@present': 0,
    '@future': 1
  },

  // Quantum operators
  quantum: {
    '|0⟩': 1,   // Ground state (positive)
    '|1⟩': -1,  // Excited state (negative)
    '|+⟩': 0    // Superposition (neutral)
  },

  // Trinary operators
  trinary: {
    'POS': 1,
    'ZERO': 0,
    'NEG': -1
  },

  // Keywords
  keywords: [
    'timeline', 'quantum', 'paradox', 'resolve',
    'encode', 'decode', 'compress', 'optimize',
    'past', 'present', 'future', 'cache', 'prefetch'
  ],

  // Statement types
  statements: {
    timeline: /^@(past|present|future)\s+(.+)$/,
    emoji: /🔮\.(\w+)\((.*?)\)/,
    quantum: /\|(.*?)⟩/,
    trinary: /\[([-01],?\s*)+\]/,
    paradox: /paradox\s+(\w+)\s*\{([^}]+)\}/
  },

  validate(code) {
    const errors = [];
    const lines = code.split('\n');

    lines.forEach((line, i) => {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('//')) return;

      let matched = false;
      for (const [type, pattern] of Object.entries(this.statements)) {
        if (pattern.test(trimmed)) {
          matched = true;
          break;
        }
      }

      if (!matched) {
        errors.push({ line: i + 1, message: 'Invalid syntax' });
      }
    });

    return { valid: errors.length === 0, errors };
  },

  highlight(code) {
    let html = code;

    // Timeline operators
    html = html.replace(/@(past|present|future)/g, '<span class="timeline">@$1</span>');

    // Quantum states
    html = html.replace(/\|([^⟩]+)⟩/g, '<span class="quantum">|$1⟩</span>');

    // Emoji operations
    html = html.replace(/🔮/g, '<span class="emoji">🔮</span>');

    // Keywords
    this.keywords.forEach(kw => {
      html = html.replace(new RegExp(`\\b${kw}\\b`, 'g'), `<span class="keyword">${kw}</span>`);
    });

    return html;
  }
};

window.SNTSyntax = SNTSyntax;
```

## Language Reference

### Timeline Declarations
```
@past load(x)      // Execute in past timeline
@present work(x)   // Execute in present
@future save(x)    // Execute in future
```

### Quantum Operations
```
|0⟩  // Ground state (1)
|1⟩  // Excited state (-1)
|+⟩  // Superposition (0)
```

### Emoji Encoding
```
🔮.encode(42)         // Encode to trits
🔮.decode([1,-1,0])   // Decode from trits
```
