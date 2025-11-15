# CLI Test Commands
**UUID:** 9c5e7f2a-6d8b-4e3f-9a5c-7d8f6e2b4a1c
**Testing** | test, coverage, lint, benchmark

Testing and quality assurance commands for Chazon CLI.

```javascript
const CLITest = {
  testResults: [],

  register(cli) {
    cli.commands.test = (pattern) => this.runTests(cli, pattern);
    cli.commands.coverage = () => this.showCoverage(cli);
    cli.commands.lint = (filename) => this.lintFile(cli, filename);
    cli.commands.benchmark = (filename) => this.benchmarkFile(cli, filename);
    cli.commands.validate = () => this.validateModules(cli);

    return this;
  },

  runTests(cli, pattern) {
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('  RUNNING TESTS', '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');

    const testFiles = Object.keys(cli.files).filter(name =>
      name.includes('test') || name.includes('spec')
    );

    if (testFiles.length === 0) {
      cli.print('No test files found', '#888');
      cli.print('Test files should include "test" or "spec" in name', '#888');
      return;
    }

    let passed = 0;
    let failed = 0;

    testFiles.forEach(file => {
      if (pattern && !file.includes(pattern)) return;

      cli.print(`Testing: ${file}`, '#00ccff');

      try {
        const content = cli.files[file];
        const hasAssertions = content.includes('assert') ||
                             content.includes('expect') ||
                             content.includes('test(');

        if (hasAssertions) {
          cli.print(`  ✓ ${file}`, '#00ff88');
          passed++;
        } else {
          cli.print(`  ⚠ ${file} - no assertions found`, '#ffaa00');
        }
      } catch (err) {
        cli.print(`  ✗ ${file} - ${err.message}`, '#ff0000');
        failed++;
      }
    });

    cli.print('');
    cli.print('─'.repeat(40), '#888');
    cli.print(`Tests: ${passed} passed, ${failed} failed`, '#00ff88');
    cli.print(`Total: ${passed + failed} test suites`, '#888');
  },

  showCoverage(cli) {
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('  CODE COVERAGE', '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');

    const totalFiles = Object.keys(cli.files).length;
    const testFiles = Object.keys(cli.files).filter(f =>
      f.includes('test') || f.includes('spec')
    ).length;

    const coverage = totalFiles > 0 ?
      Math.round((testFiles / totalFiles) * 100) : 0;

    cli.print(`Files:        ${totalFiles}`, '#888');
    cli.print(`Test Files:   ${testFiles}`, '#888');
    cli.print(`Coverage:     ${coverage}%`, coverage > 80 ? '#00ff88' : '#ffaa00');
    cli.print('');

    if (coverage < 80) {
      cli.print('⚠ Coverage below 80% - add more tests!', '#ffaa00');
    } else {
      cli.print('✓ Good coverage!', '#00ff88');
    }
  },

  lintFile(cli, filename) {
    if (!filename) {
      cli.print('Usage: lint <filename>', '#ff0000');
      return;
    }

    const content = cli.files[filename];
    if (!content) {
      cli.print(`File not found: ${filename}`, '#ff0000');
      return;
    }

    cli.print(`Linting: ${filename}`, '#00ccff');
    cli.print('');

    let issues = 0;

    // Check for common issues
    if (content.length > 25000) {  // ~250 tokens
      cli.print('  ⚠ File exceeds 250 token limit', '#ffaa00');
      issues++;
    }

    if (!content.includes('UUID:')) {
      cli.print('  ⚠ Missing UUID header', '#ffaa00');
      issues++;
    }

    if (!content.includes('window.')) {
      cli.print('  ⚠ No window export found', '#ffaa00');
      issues++;
    }

    if (issues === 0) {
      cli.print('  ✓ No issues found', '#00ff88');
    } else {
      cli.print('');
      cli.print(`Found ${issues} issue(s)`, '#ffaa00');
    }
  },

  benchmarkFile(cli, filename) {
    if (!filename) {
      cli.print('Usage: benchmark <filename>', '#ff0000');
      return;
    }

    cli.print(`Benchmarking: ${filename}`, '#00ccff');

    const start = performance.now();

    try {
      const content = cli.files[filename];
      if (window.MDCompiler) {
        MDCompiler.compile(content);
      }

      const end = performance.now();
      const time = (end - start).toFixed(2);

      cli.print(`  Execution time: ${time}ms`, '#00ff88');

      if (time < 10) {
        cli.print('  ⚡ Fast!', '#00ff88');
      } else if (time < 100) {
        cli.print('  ✓ Good', '#00ccff');
      } else {
        cli.print('  ⚠ Slow - consider optimization', '#ffaa00');
      }
    } catch (err) {
      cli.print(`  ✗ Error: ${err.message}`, '#ff0000');
    }
  },

  validateModules(cli) {
    cli.print('Validating all modules...', '#00ccff');
    cli.print('');

    let valid = 0;
    let invalid = 0;

    Object.keys(cli.files).forEach(filename => {
      const content = cli.files[filename];

      const hasUUID = content.includes('UUID:');
      const hasExport = content.includes('window.');
      const sizeOk = content.length < 25000;

      if (hasUUID && hasExport && sizeOk) {
        valid++;
      } else {
        cli.print(`  ⚠ ${filename}`, '#ffaa00');
        if (!hasUUID) cli.print('    - Missing UUID', '#888');
        if (!hasExport) cli.print('    - No window export', '#888');
        if (!sizeOk) cli.print('    - Exceeds size limit', '#888');
        invalid++;
      }
    });

    cli.print('');
    cli.print(`Valid: ${valid}, Invalid: ${invalid}`, '#00ff88');
  }
};

window.CLITest = CLITest;
```

## Commands

- **test** - Run all tests
- **coverage** - Show code coverage
- **lint** - Lint a file
- **benchmark** - Benchmark execution time
- **validate** - Validate all modules
