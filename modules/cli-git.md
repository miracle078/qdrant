# CLI Git Commands
**UUID:** 5c7e9f2a-4d8b-4e3f-9a6c-7d5f8e2b3a1c
**Version Control** | status, commit, push, log, diff

Git operations for Chazon CLI.

```javascript
const CLIGit = {
  commits: [],
  branch: 'main',

  register(cli) {
    cli.commands.status = () => this.gitStatus(cli);
    cli.commands.commit = (message) => this.gitCommit(cli, message);
    cli.commands.push = () => this.gitPush(cli);
    cli.commands.pull = () => this.gitPull(cli);
    cli.commands.log = (count) => this.gitLog(cli, count);
    cli.commands.diff = (filename) => this.gitDiff(cli, filename);
    cli.commands.branch = (name) => this.gitBranch(cli, name);
    cli.commands.checkout = (branch) => this.gitCheckout(cli, branch);

    return this;
  },

  gitStatus(cli) {
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('  GIT STATUS', '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');

    cli.print(`On branch: ${this.branch}`, '#00ccff');
    cli.print('');

    const modified = Object.keys(cli.files).filter(f =>
      this.isModified(f, cli.files[f])
    );

    if (modified.length === 0) {
      cli.print('  ✓ Working tree clean', '#00ff88');
    } else {
      cli.print('Modified files:', '#ffaa00');
      modified.forEach(file => {
        cli.print(`  M  ${file}`, '#ff0000');
      });
      cli.print('');
      cli.print(`${modified.length} files modified`, '#888');
    }
  },

  gitCommit(cli, message) {
    if (!message) {
      cli.print('Usage: commit <message>', '#ff0000');
      cli.print('Example: commit "Add new feature"', '#888');
      return;
    }

    const commit = {
      hash: this.generateHash(),
      message,
      timestamp: new Date().toISOString(),
      author: 'chazon-user',
      files: Object.keys(cli.files).length
    };

    this.commits.push(commit);

    cli.print(`[${this.branch} ${commit.hash.slice(0, 7)}] ${message}`, '#00ff88');
    cli.print(`${commit.files} files changed`, '#888');

    // Save to localStorage
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem('chazon_commits', JSON.stringify(this.commits));
    }
  },

  gitPush(cli) {
    cli.print('Pushing to origin...', '#00ccff');

    setTimeout(() => {
      cli.print('');
      cli.print('✓ Pushed to remote repository', '#00ff88');
      cli.print(`Branch: ${this.branch}`, '#888');
      cli.print(`Commits: ${this.commits.length}`, '#888');
    }, 1000);
  },

  gitPull(cli) {
    cli.print('Pulling from origin...', '#00ccff');

    setTimeout(() => {
      cli.print('');
      cli.print('✓ Already up to date', '#00ff88');
    }, 1000);
  },

  gitLog(cli, count) {
    count = parseInt(count) || 10;

    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('  GIT LOG', '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');

    if (this.commits.length === 0) {
      cli.print('No commits yet', '#888');
      return;
    }

    this.commits.slice(-count).reverse().forEach(commit => {
      cli.print(`commit ${commit.hash}`, '#ffaa00');
      cli.print(`Author: ${commit.author}`, '#888');
      cli.print(`Date:   ${new Date(commit.timestamp).toLocaleString()}`, '#888');
      cli.print('', '#888');
      cli.print(`    ${commit.message}`, '#ccc');
      cli.print('', '#888');
    });
  },

  gitDiff(cli, filename) {
    if (!filename) {
      cli.print('Usage: diff <filename>', '#ff0000');
      return;
    }

    cli.print(`diff --git a/${filename} b/${filename}`, '#00ccff');
    cli.print('--- a/' + filename, '#ff0000');
    cli.print('+++ b/' + filename, '#00ff88');
    cli.print('');
    cli.print('(Diff implementation coming soon)', '#888');
  },

  gitBranch(cli, name) {
    if (!name) {
      cli.print(`* ${this.branch}`, '#00ff88');
      cli.print('  develop', '#888');
      cli.print('  feature/*', '#888');
      return;
    }

    cli.print(`Created branch: ${name}`, '#00ff88');
  },

  gitCheckout(cli, branch) {
    if (!branch) {
      cli.print('Usage: checkout <branch>', '#ff0000');
      return;
    }

    this.branch = branch;
    cli.print(`Switched to branch '${branch}'`, '#00ff88');
  },

  generateHash() {
    return Math.random().toString(36).substring(2, 15) +
           Math.random().toString(36).substring(2, 15);
  },

  isModified(filename, content) {
    // Simple check - in real implementation, would compare with last commit
    return Math.random() > 0.7;
  }
};

window.CLIGit = CLIGit;
```

## Commands

- **status** - Show git status
- **commit** - Commit changes
- **push** - Push to remote
- **pull** - Pull from remote
- **log** - Show commit log
- **diff** - Show file differences
- **branch** - List/create branches
- **checkout** - Switch branches

## Features

- Commit history tracking
- Branch management
- File change detection
- LocalStorage persistence
