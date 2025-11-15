# Parser
**Type:** Compiler Phase | Syntax Analysis

Syntax analysis phase for SNT language - builds Abstract Syntax Tree (AST).

## Grammar

```
Program     := Statement*
Statement   := VarDecl | FuncDecl | ExprStmt | IfStmt | WhileStmt | ReturnStmt
VarDecl     := ('let' | 'const') IDENTIFIER '=' Expression ';'
FuncDecl    := 'function' IDENTIFIER '(' Params? ')' Block
ExprStmt    := Expression ';'
IfStmt      := 'if' '(' Expression ')' Block ('else' Block)?
WhileStmt   := 'while' '(' Expression ')' Block
ReturnStmt  := 'return' Expression? ';'
Expression  := Assignment
Assignment  := LogicalOr ('=' Assignment)?
LogicalOr   := LogicalAnd ('||' LogicalAnd)*
LogicalAnd  := Equality ('&&' Equality)*
Equality    := Comparison (('==' | '!=') Comparison)*
Comparison  := Term (('<' | '>' | '<=' | '>=') Term)*
Term        := Factor (('+' | '-') Factor)*
Factor      := Unary (('*' | '/') Unary)*
Unary       := ('!' | '-' | '~') Unary | Primary
Primary     := NUMBER | STRING | IDENTIFIER | '(' Expression ')' | ArrayLit | FuncCall
ArrayLit    := '[' (Expression (',' Expression)*)? ']'
FuncCall    := IDENTIFIER '(' (Expression (',' Expression)*)? ')'
Block       := '{' Statement* '}'
```

## AST Structure

```javascript
// Variable declaration
{
  type: 'VarDecl',
  kind: 'let',
  name: 'x',
  value: { type: 'Number', value: 42 }
}

// Function declaration
{
  type: 'FuncDecl',
  name: 'add',
  params: ['a', 'b'],
  body: [/* statements */]
}

// Binary expression
{
  type: 'BinaryExpr',
  operator: '+',
  left: { type: 'Identifier', name: 'a' },
  right: { type: 'Number', value: 1 }
}
```

## Parser Implementation

```javascript
const Parser = {
  parse(tokens) {
    let pos = 0;
    
    function parseProgram() {
      const statements = [];
      while (pos < tokens.length) {
        statements.push(parseStatement());
      }
      return { type: 'Program', body: statements };
    }
    
    function parseStatement() {
      const token = tokens[pos];
      
      if (token.value === 'let' || token.value === 'const') {
        return parseVarDecl();
      }
      if (token.value === 'function') {
        return parseFuncDecl();
      }
      if (token.value === 'if') {
        return parseIfStmt();
      }
      if (token.value === 'while') {
        return parseWhileStmt();
      }
      if (token.value === 'return') {
        return parseReturnStmt();
      }
      
      return parseExprStmt();
    }
    
    // ... more parsing functions
    
    return parseProgram();
  }
};
```

## See Also

- `lexer.md` - Tokenization
- `optimizer.md` - AST optimization
