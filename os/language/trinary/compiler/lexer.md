# Lexer
**Type:** Compiler Phase | Tokenization

Lexical analysis phase for SNT language.

## Tokens

### Keywords
- `let`, `const`, `var`
- `function`, `return`
- `if`, `else`, `while`, `for`
- `space`, `time`, `trinary`

### Operators
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Logical: `&&`, `||`, `!`
- Trinary: `~`, `?`, `:`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`

### Literals
- Numbers: `42`, `3.14`, `-1`
- Strings: `"hello"`, `'world'`
- Trinary: `-1`, `0`, `+1`
- Arrays: `[1, 0, -1]`

### Symbols
- Braces: `{`, `}`
- Parens: `(`, `)`
- Brackets: `[`, `]`
- Semicolon: `;`
- Comma: `,`

## Tokenization Process

```javascript
const Lexer = {
  tokenize(source) {
    const tokens = [];
    let pos = 0;
    
    while (pos < source.length) {
      // Skip whitespace
      if (/\s/.test(source[pos])) {
        pos++;
        continue;
      }
      
      // Match keyword/identifier
      if (/[a-zA-Z_]/.test(source[pos])) {
        const start = pos;
        while (/[a-zA-Z0-9_]/.test(source[pos])) pos++;
        const text = source.slice(start, pos);
        tokens.push({ type: 'IDENTIFIER', value: text });
        continue;
      }
      
      // Match number
      if (/[0-9]/.test(source[pos]) || source[pos] === '-') {
        const start = pos;
        if (source[pos] === '-') pos++;
        while (/[0-9.]/.test(source[pos])) pos++;
        const text = source.slice(start, pos);
        tokens.push({ type: 'NUMBER', value: parseFloat(text) });
        continue;
      }
      
      // Match operator
      const ops = ['==', '!=', '<=', '>=', '&&', '||'];
      const twoChar = source.slice(pos, pos + 2);
      if (ops.includes(twoChar)) {
        tokens.push({ type: 'OPERATOR', value: twoChar });
        pos += 2;
        continue;
      }
      
      // Single character
      tokens.push({ type: 'SYMBOL', value: source[pos] });
      pos++;
    }
    
    return tokens;
  }
};
```

## See Also

- `parser.md` - Syntax analysis
- `../spacetime-compiler.md` - Full compiler
