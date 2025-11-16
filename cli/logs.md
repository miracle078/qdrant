# View Logs
**UUID:** cli-logs-001
**ISA-95 L2: Supervisory Control** | Markdown Executable

View system logs for different areas.

## Areas

- `backend` - Backend API logs
- `http` - HTTP server logs
- `system` - OS system logs
- `all` - All logs (default, shows last 10 lines of each)

```bash
#!/bin/bash
# View Chazon system logs

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

AREA="${1:-all}"

echo "📋 Chazon Logs: $AREA"
echo "===================="
echo ""

case "$AREA" in
    backend)
        if [ -f "$ROOT_DIR/cli/logs/backend.log" ]; then
            echo "Backend API Logs (live):"
            echo "------------------------"
            tail -f "$ROOT_DIR/cli/logs/backend.log"
        else
            echo "No backend logs found"
        fi
        ;;

    http)
        if [ -f "$ROOT_DIR/cli/logs/httpserver.log" ]; then
            echo "HTTP Server Logs (live):"
            echo "------------------------"
            tail -f "$ROOT_DIR/cli/logs/httpserver.log"
        else
            echo "No HTTP server logs found"
        fi
        ;;

    system)
        if [ -d "$ROOT_DIR/os/logs/system" ]; then
            echo "System Logs:"
            echo "------------"
            find "$ROOT_DIR/os/logs/system" -name "*.log" -exec tail -n 10 {} \;
        else
            echo "No system logs found"
        fi
        ;;

    all|*)
        echo "Backend API Logs (last 10 lines):"
        echo "----------------------------------"
        if [ -f "$ROOT_DIR/cli/logs/backend.log" ]; then
            tail -n 10 "$ROOT_DIR/cli/logs/backend.log"
        else
            echo "No backend logs"
        fi
        echo ""

        echo "HTTP Server Logs (last 10 lines):"
        echo "----------------------------------"
        if [ -f "$ROOT_DIR/cli/logs/httpserver.log" ]; then
            tail -n 10 "$ROOT_DIR/cli/logs/httpserver.log"
        else
            echo "No HTTP server logs"
        fi
        echo ""

        echo "System Logs (last 10 lines each):"
        echo "----------------------------------"
        if [ -d "$ROOT_DIR/os/logs" ]; then
            find "$ROOT_DIR/os/logs" -name "*.log" -type f | while read -r logfile; do
                echo ""
                echo "📄 $(basename $logfile):"
                tail -n 10 "$logfile"
            done
        else
            echo "No system logs"
        fi
        ;;
esac
```

## Usage

```bash
# View all logs (summary)
./cli/logs.md

# Tail backend logs (live)
./cli/logs.md backend

# Tail HTTP server logs (live)
./cli/logs.md http

# View system logs
./cli/logs.md system
```

## Live Monitoring

For live log monitoring, the script runs `tail -f` for single areas:

```bash
# Follow backend logs
./cli/logs.md backend

# Follow HTTP logs
./cli/logs.md http
```

Press `Ctrl+C` to exit live monitoring.

## Log Locations

| Area | Path |
|------|------|
| Backend API | `cli/logs/backend.log` |
| HTTP Server | `cli/logs/httpserver.log` |
| System | `os/logs/system/*.log` |
| PLC | `os/logs/plc/*.log` |
| SCADA | `os/logs/scada/*.log` |
| Modules | `os/logs/modules/*.log` |
| API | `os/logs/api/*.log` |
| Errors | `os/logs/errors/*.log` |
| Audit | `os/logs/audit/*.log` |
| Debug | `os/logs/debug/*.log` |
| Boot | `os/logs/boot/*.log` |
| Database | `os/logs/database/*.log` |
| Security | `os/logs/security/*.log` |

## Advanced Usage

```bash
# Search logs for errors
grep -r "ERROR" cli/logs/
grep -r "ERROR" os/logs/

# Search for specific text
grep -r "Qdrant" cli/logs/

# View logs from last hour
find cli/logs/ -name "*.log" -mmin -60 -exec tail {} \;

# Count error lines
grep -c "ERROR" cli/logs/backend.log
```

## Log Formats

All logs use JSON format:

```json
{
  "timestamp": "2025-11-15T16:30:00.000Z",
  "level": "INFO|WARN|ERROR|DEBUG",
  "source": "module-name|plc-area|api-endpoint",
  "message": "Log message",
  "data": { "additional": "context" }
}
```

## Troubleshooting

### No Logs Appearing

```bash
# Check if services are running
./cli/health.md

# Check log file permissions
ls -la cli/logs/

# Manually create log directory
mkdir -p cli/logs
```

### Logs Too Large

```bash
# Rotate logs
mv cli/logs/backend.log cli/logs/backend.log.old
mv cli/logs/httpserver.log cli/logs/httpserver.log.old

# Restart services to create new logs
./cli/restart.md
```

## Related

- `health.md` - Check service status
- `/os/logs/README.md` - Logging system documentation
- `/os/logs/index.html` - Web-based log viewer
