# Restart Services
**UUID:** cli-restart-001
**ISA-95 L3: MES Layer** | Markdown Executable

Convenience script that stops and starts all services.

```bash
#!/bin/bash
# Restart all Chazon services

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔄 Restarting Chazon Services"
echo "=============================="
echo ""

# Stop all services
echo "Stopping services..."
"$SCRIPT_DIR/stop.sh"

# Wait for graceful shutdown
echo ""
echo "Waiting for graceful shutdown..."
sleep 2

# Start all services
echo ""
echo "Starting services..."
"$SCRIPT_DIR/start.sh"
```

## Usage

```bash
# Restart all services
./cli/restart.md
```

## Equivalent To

```bash
./cli/stop.md && sleep 2 && ./cli/start.md
```

## When to Restart

- After configuration changes
- After updating code
- When services are unresponsive
- After system updates
- When troubleshooting issues

## What Gets Restarted

1. Backend API
2. HTTP Server
3. Qdrant vector database

## Wait Time

The script waits 2 seconds between stop and start to ensure:
- Ports are fully released
- Processes have terminated
- File locks are released
- Resources are cleaned up

## Troubleshooting

### Services Don't Start After Restart

```bash
# Check for port conflicts
lsof -i :6333  # Qdrant
lsof -i :8000  # Backend API
lsof -i :8080  # HTTP Server

# Check logs for errors
./cli/logs.md backend
./cli/logs.md http
```

### Restart Takes Too Long

```bash
# Force stop instead
kill -9 $(cat cli/logs/backend.pid)
kill -9 $(cat cli/logs/httpserver.pid)
docker rm -f qdrant

# Then start
./cli/start.md
```

## Related

- `start.md` - Start services
- `stop.md` - Stop services
- `health.md` - Check status after restart
