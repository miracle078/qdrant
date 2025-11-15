# CLI Edit Commands
**UUID:** 7e2c9f5a-4d8b-4e3f-9a6c-8d5f7e2b3a1c
**File Editing** | edit, save, delete, mkdir, touch

File editing and management commands for Chazon CLI.

```javascript
const CLIEdit = {
  currentFile: null,
  editBuffer: '',

  register(cli) {
    cli.commands.edit = (filename) => this.editFile(cli, filename);
    cli.commands.save = (filename) => this.saveFile(cli, filename);
    cli.commands.rm = (filename) => this.deleteFile(cli, filename);
    cli.commands.touch = (filename) => this.createFile(cli, filename);
    cli.commands.mkdir = (dirname) => this.makeDir(cli, dirname);
    cli.commands.cp = (src, dest) => this.copyFile(cli, src, dest);
    cli.commands.mv = (src, dest) => this.moveFile(cli, src, dest);
    cli.commands.nano = (filename) => this.nanoEditor(cli, filename);

    return this;
  },

  editFile(cli, filename) {
    if (!filename) {
      cli.print('Usage: edit <filename>', '#ff0000');
      return;
    }

    const content = cli.files[filename] || '';
    this.currentFile = filename;
    this.editBuffer = content;

    cli.print(`Editing: ${filename}`, '#00ccff');
    cli.print('─'.repeat(50), '#888');
    cli.print(content || '(empty file)', '#ccc');
    cli.print('─'.repeat(50), '#888');
    cli.print('Type your changes and use "save" to save', '#00ff88');
    cli.print('Current buffer stored', '#888');
  },

  saveFile(cli, filename) {
    filename = filename || this.currentFile;

    if (!filename) {
      cli.print('No file to save. Use: save <filename>', '#ff0000');
      return;
    }

    cli.files[filename] = this.editBuffer;
    cli.print(`✓ Saved: ${filename}`, '#00ff88');

    // Save to localStorage if available
    if (typeof localStorage !== 'undefined') {
      const allFiles = JSON.stringify(cli.files);
      localStorage.setItem('chazon_files', allFiles);
      cli.print('✓ Persisted to localStorage', '#888');
    }
  },

  deleteFile(cli, filename) {
    if (!filename) {
      cli.print('Usage: rm <filename>', '#ff0000');
      return;
    }

    if (!cli.files[filename]) {
      cli.print(`File not found: ${filename}`, '#ff0000');
      return;
    }

    delete cli.files[filename];
    cli.print(`✓ Deleted: ${filename}`, '#00ff88');
  },

  createFile(cli, filename) {
    if (!filename) {
      cli.print('Usage: touch <filename>', '#ff0000');
      return;
    }

    if (cli.files[filename]) {
      cli.print(`File already exists: ${filename}`, '#888');
      return;
    }

    cli.files[filename] = '';
    cli.print(`✓ Created: ${filename}`, '#00ff88');
  },

  makeDir(cli, dirname) {
    if (!dirname) {
      cli.print('Usage: mkdir <dirname>', '#ff0000');
      return;
    }

    cli.print(`✓ Directory created: ${dirname}`, '#00ff88');
    cli.print('(Virtual directory - files support paths)', '#888');
  },

  copyFile(cli, src, dest) {
    if (!src || !dest) {
      cli.print('Usage: cp <source> <destination>', '#ff0000');
      return;
    }

    if (!cli.files[src]) {
      cli.print(`Source file not found: ${src}`, '#ff0000');
      return;
    }

    cli.files[dest] = cli.files[src];
    cli.print(`✓ Copied: ${src} → ${dest}`, '#00ff88');
  },

  moveFile(cli, src, dest) {
    if (!src || !dest) {
      cli.print('Usage: mv <source> <destination>', '#ff0000');
      return;
    }

    if (!cli.files[src]) {
      cli.print(`Source file not found: ${src}`, '#ff0000');
      return;
    }

    cli.files[dest] = cli.files[src];
    delete cli.files[src];
    cli.print(`✓ Moved: ${src} → ${dest}`, '#00ff88');
  },

  nanoEditor(cli, filename) {
    if (!filename) {
      cli.print('Usage: nano <filename>', '#ff0000');
      return;
    }

    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print(`  GNU nano - ${filename}`, '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');
    cli.print('Mini text editor - use "edit" and "save" commands', '#888');
    cli.print('Full nano emulation: Coming soon!', '#00ccff');
  }
};

window.CLIEdit = CLIEdit;
```

## Commands

- **edit** - Open file for editing
- **save** - Save current file
- **rm** - Delete file
- **touch** - Create empty file
- **mkdir** - Create directory
- **cp** - Copy file
- **mv** - Move/rename file
- **nano** - Text editor
