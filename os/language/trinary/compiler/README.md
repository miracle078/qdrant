# Spacetime Compiler
**Type:** Language | Trinary Computing

SNT (Space-Time Notation) compiler with trinary logic support.

## Components

1. **Lexer** - `lexer.md` - Tokenization
2. **Parser** - `parser.md` - Syntax analysis
3. **Optimizer** - `optimizer.md` - Code optimization
4. **Codegen** - `codegen.md` - Code generation
5. **Runtime** - `runtime.md` - Trinary runtime

## Architecture

```
Source Code (SNT)
     │
     ▼
  Lexer (Tokens)
     │
     ▼
  Parser (AST)
     │
     ▼
 Optimizer (Optimized AST)
     │
     ▼
 Codegen (Trinary Bytecode)
     │
     ▼
 Runtime (Execution)
```

## Trinary Logic

- **-1** - False/Negative
- **0** - Unknown/Neutral
- **+1** - True/Positive

## Compilation Phases

### Phase 1: Lexical Analysis
Tokenize source code into lexemes.

### Phase 2: Syntax Analysis
Parse tokens into Abstract Syntax Tree (AST).

### Phase 3: Semantic Analysis
Type checking and symbol resolution.

### Phase 4: Optimization
Dead code elimination, constant folding.

### Phase 5: Code Generation
Generate trinary bytecode.

### Phase 6: Execution
Run on trinary virtual machine.

## Quick Start

```javascript
// Compile SNT code
const source = 'let x = space(3, [1, 0, -1])';
const bytecode = Compiler.compile(source);

// Execute
const result = Runtime.execute(bytecode);
```

## See Also

- `../../../language/` - Language PLC area
- `../../../language/snt/` - SNT language specs
- `../../README.md` - Template system overview
