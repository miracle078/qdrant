# CLI Logs Commands
**UUID:** 2a8f5e9c-3d7b-4e1f-9a6c-8d5f7e2b6a3c
**Logging** | logs, tail, grep, watch

Log viewing and monitoring commands for Chazon CLI.

```javascript
const CLILogs = {
  logBuffer: [],
  maxLogs: 1000,

  register(cli) {
    cli.commands.logs = (filter) => this.showLogs(cli, filter);
    cli.commands.tail = (lines) => this.tailLogs(cli, lines);
    cli.commands.grep = (pattern) => this.grepLogs(cli, pattern);
    cli.commands.watch = (cmd) => this.watchCommand(cli, cmd);
    cli.commands.history = () => this.showHistory(cli);

    // Intercept console.log to capture logs
    this.interceptConsole();

    return this;
  },

  interceptConsole() {
    const originalLog = console.log;
    const self = this;

    console.log = function(...args) {
      const message = args.map(a =>
        typeof a === 'object' ? JSON.stringify(a) : String(a)
      ).join(' ');

      self.logBuffer.push({
        timestamp: new Date().toISOString(),
        message,
        level: 'info'
      });

      if (self.logBuffer.length > self.maxLogs) {
        self.logBuffer.shift();
      }

      originalLog.apply(console, args);
    };
  },

  showLogs(cli, filter) {
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('  SYSTEM LOGS', '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');

    if (this.logBuffer.length === 0) {
      cli.print('No logs available', '#888');
      return;
    }

    const logs = filter
      ? this.logBuffer.filter(log => log.message.includes(filter))
      : this.logBuffer;

    logs.slice(-50).forEach(log => {
      const time = new Date(log.timestamp).toLocaleTimeString();
      cli.print(`[${time}] ${log.message}`, '#888');
    });

    cli.print('');
    cli.print(`Showing ${logs.length} log entries`, '#00ccff');
  },

  tailLogs(cli, lines) {
    lines = parseInt(lines) || 10;

    cli.print(`Last ${lines} log entries:`, '#00ccff');
    cli.print('');

    this.logBuffer.slice(-lines).forEach(log => {
      const time = new Date(log.timestamp).toLocaleTimeString();
      cli.print(`[${time}] ${log.message}`, '#888');
    });
  },

  grepLogs(cli, pattern) {
    if (!pattern) {
      cli.print('Usage: grep <pattern>', '#ff0000');
      return;
    }

    cli.print(`Searching logs for: ${pattern}`, '#00ccff');
    cli.print('');

    const matches = this.logBuffer.filter(log =>
      log.message.toLowerCase().includes(pattern.toLowerCase())
    );

    if (matches.length === 0) {
      cli.print('No matches found', '#888');
      return;
    }

    matches.forEach(log => {
      const time = new Date(log.timestamp).toLocaleTimeString();
      const highlighted = log.message.replace(
        new RegExp(pattern, 'gi'),
        `**${pattern}**`
      );
      cli.print(`[${time}] ${highlighted}`, '#00ff88');
    });

    cli.print('');
    cli.print(`Found ${matches.length} matches`, '#00ccff');
  },

  watchCommand(cli, cmd) {
    if (!cmd) {
      cli.print('Usage: watch <command>', '#ff0000');
      cli.print('Example: watch logs', '#888');
      return;
    }

    cli.print(`Watching: ${cmd}`, '#00ccff');
    cli.print('Press Ctrl+C to stop (not implemented yet)', '#888');
    cli.print('');

    // Mock implementation
    let count = 0;
    const interval = setInterval(() => {
      if (count >= 5) {
        clearInterval(interval);
        cli.print('Watch stopped', '#888');
        return;
      }

      cli.executeCommand(cmd);
      count++;
    }, 2000);
  },

  showHistory(cli) {
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('  COMMAND HISTORY', '#00ccff');
    cli.print('═══════════════════════════════════════', '#00ff88');
    cli.print('');

    if (!cli.history || cli.history.length === 0) {
      cli.print('No command history', '#888');
      return;
    }

    cli.history.slice(-20).forEach((cmd, idx) => {
      cli.print(`  ${idx + 1}  ${cmd}`, '#888');
    });

    cli.print('');
    cli.print(`Total commands: ${cli.history.length}`, '#00ccff');
  }
};

window.CLILogs = CLILogs;
```

## Commands

- **logs** - Show system logs
- **tail** - Show last N log entries
- **grep** - Search logs for pattern
- **watch** - Watch command output
- **history** - Show command history

## Features

- Captures console.log output
- Timestamps all logs
- Pattern matching/filtering
- Command history tracking
