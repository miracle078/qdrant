# Chazon CLI System
**Modular Command-Line Interface**

Complete CLI system with modular command sets for Chazon OS.

## Architecture

The CLI is split into multiple modules for better organization and maintainability:

```
chazon-cli.md          # Core CLI engine
├── cli-core.md        # Basic commands (ls, cat, help)
├── cli-edit.md        # File operations (edit, save, rm)
├── cli-test.md        # Testing (test, coverage, lint)
├── cli-logs.md        # Logging (logs, tail, grep)
└── cli-git.md         # Version control (status, commit, push)
```

## All Available Commands

### Core Commands (cli-core.md)
- **help** - Show all available commands
- **ls** - List all files
- **cat <file>** - Display file contents
- **run <file>** - Execute a program
- **pwd** - Print working directory
- **clear** - Clear terminal
- **whoami** - Show current user
- **version** - Show Chazon version

### File Operations (cli-edit.md)
- **edit <file>** - Open file for editing
- **save [file]** - Save current buffer to file
- **rm <file>** - Delete file
- **touch <file>** - Create empty file
- **mkdir <dir>** - Create directory
- **cp <src> <dest>** - Copy file
- **mv <src> <dest>** - Move/rename file
- **nano <file>** - Text editor (basic)

### Testing (cli-test.md)
- **test [pattern]** - Run all tests (optionally filter by pattern)
- **coverage** - Show code coverage statistics
- **lint <file>** - Lint a file for issues
- **benchmark <file>** - Benchmark execution time
- **validate** - Validate all modules

### Logging (cli-logs.md)
- **logs [filter]** - Show system logs (optionally filtered)
- **tail [lines]** - Show last N log entries
- **grep <pattern>** - Search logs for pattern
- **watch <cmd>** - Watch command output
- **history** - Show command history

### Version Control (cli-git.md)
- **status** - Show git status
- **commit <message>** - Commit changes
- **push** - Push to remote
- **pull** - Pull from remote
- **log [count]** - Show commit history
- **diff <file>** - Show file differences
- **branch [name]** - List/create branches
- **checkout <branch>** - Switch branches

## Usage Examples

### Basic File Operations
```bash
# List all files
ls

# View file contents
cat hello.md

# Run a program
run hello.md

# Create and edit a file
touch myprogram.md
edit myprogram.md
save

# Copy and rename
cp hello.md goodbye.md
mv goodbye.md farewell.md
```

### Testing Workflow
```bash
# Run all tests
test

# Run specific tests
test attractor

# Check coverage
coverage

# Lint a file
lint myprogram.md

# Validate all modules
validate

# Benchmark performance
benchmark myprogram.md
```

### Logging and Debugging
```bash
# View all logs
logs

# View last 10 logs
tail 10

# Search logs
grep error

# Show command history
history
```

### Version Control
```bash
# Check status
status

# Commit changes
commit "Add new feature"

# Push to remote
push

# View log
log

# Show diff
diff myfile.md

# Create branch
branch feature/new-stuff

# Switch branch
checkout feature/new-stuff
```

## Creating Custom Command Modules

Create a new file `cli-custom.md`:

```markdown
# CLI Custom Commands
**UUID:** your-uuid-here

\`\`\`javascript
const CLICustom = {
  register(cli) {
    cli.commands.mycmd = () => {
      cli.print('My custom command!', '#00ff88');
    };

    return this;
  }
};

window.CLICustom = CLICustom;
\`\`\`
```

Then load it in `chazon/index.html`:

```javascript
modules: [
  // ... other modules
  '../modules/cli-custom.md',
  '../modules/chazon-cli.md',  // Must load after command modules
  // ...
]
```

## Integration

The CLI automatically integrates with:

- **MDCompiler** - Executes markdown programs
- **ChazonOS** - OS module system
- **Terminal** - Terminal output display
- **LocalStorage** - Persistence for files and commits

## Features

### Command History
- All commands are tracked in `ChazonCLI.history`
- Use `history` command to view

### File Persistence
- Files saved to LocalStorage automatically
- Survives page reloads

### Colored Output
- Commands can print in different colors
- Format: `cli.print(message, '#color')`

### Error Handling
- Try/catch around all command execution
- User-friendly error messages

### Module System
- Easy to add new command sets
- Clean separation of concerns
- Each module is < 250 tokens

## Architecture Benefits

1. **Modular** - Easy to add/remove command sets
2. **Maintainable** - Each module < 250 tokens
3. **Extensible** - Simple registration pattern
4. **Testable** - Each module can be tested independently
5. **Documented** - Self-documenting code in markdown

## Command Module Template

```javascript
const CLIModuleName = {
  register(cli) {
    // Register commands
    cli.commands.cmd1 = (arg1, arg2) => {
      cli.print(`Executed: ${arg1} ${arg2}`, '#00ff88');
    };

    cli.commands.cmd2 = () => {
      cli.print('Command 2', '#00ccff');
    };

    return this;
  }
};

window.CLIModuleName = CLIModuleName;
```

## Loading Order

**IMPORTANT**: Command modules must load BEFORE `chazon-cli.md`:

```javascript
modules: [
  // 1. Load all CLI command modules first
  '../modules/cli-core.md',
  '../modules/cli-edit.md',
  '../modules/cli-test.md',
  '../modules/cli-logs.md',
  '../modules/cli-git.md',

  // 2. Load main CLI (will register all above)
  '../modules/chazon-cli.md',

  // 3. Continue with other modules
  // ...
]
```

## Terminal Integration

Initialize CLI with output element:

```javascript
const output = document.getElementById('output');
ChazonCLI.init(output);
```

Then execute commands:

```javascript
ChazonCLI.exec('help');
ChazonCLI.exec('ls');
ChazonCLI.exec('test');
```

## Future Enhancements

- **Tab completion** - Complete commands and filenames
- **Pipe support** - `cat file.md | grep pattern`
- **Aliases** - Custom command shortcuts
- **Scripting** - Run command scripts
- **Remote execution** - Execute commands on server
- **Plugins** - Dynamic module loading

---

**See individual module files for detailed command documentation**
