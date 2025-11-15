# Logs Directory

Centralized logging system for the Chazon SCADA platform following ISA-95 standards.

## Directory Structure

```
logs/
├── system/        → System-level logs (startup, shutdown, health)
├── plc/           → PLC controller logs (scan cycles, tag updates)
├── scada/         → SCADA monitoring logs (alarms, events, trends)
├── modules/       → Module execution logs (114+ markdown modules)
├── api/           → Backend API request/response logs
├── errors/        → Error and exception logs
├── audit/         → Security audit trail (user actions, auth)
├── debug/         → Development and debugging logs
├── boot/          → Boot sequence logs (6 phases)
├── database/      → Database operation logs (SQLite, Qdrant)
└── security/      → Security events (auth failures, intrusions)
```

## Log Format

All logs follow a standardized JSON format:

```json
{
  "timestamp": "2025-11-15T16:30:00.000Z",
  "level": "INFO|WARN|ERROR|DEBUG",
  "source": "module-name|plc-area|api-endpoint",
  "message": "Log message",
  "data": { "additional": "context" },
  "session_id": "uuid",
  "user_id": "user-identifier"
}
```

## Log Levels

- **DEBUG**: Detailed diagnostic information
- **INFO**: General informational messages
- **WARN**: Warning messages (potential issues)
- **ERROR**: Error events (functionality affected)
- **CRITICAL**: Critical failures (system down)

## Retention Policy

- **System/PLC/SCADA**: 30 days
- **API**: 7 days
- **Errors**: 90 days
- **Audit/Security**: 365 days (compliance)
- **Debug**: 3 days

## Log Rotation

Logs are automatically rotated daily at midnight UTC:
- Format: `{type}-YYYY-MM-DD.log`
- Compressed after 7 days: `{type}-YYYY-MM-DD.log.gz`
- Deleted per retention policy

## Viewing Logs

### Via HMI
Navigate to `/os/logs/hmi.html` for real-time log viewer

### Via CLI
```bash
# Tail all system logs
tail -f os/logs/system/*.log

# Search for errors in last hour
grep "ERROR" os/logs/errors/*.log | tail -100

# View PLC logs for specific area
cat os/logs/plc/backend-$(date +%Y-%m-%d).log
```

### Via API
```bash
# Get recent logs
curl http://localhost:8000/api/logs?limit=100&level=ERROR

# Query specific time range
curl http://localhost:8000/api/logs?start=2025-11-15T00:00:00Z&end=2025-11-15T23:59:59Z
```

## Integration

### JavaScript Logging
```javascript
// From any module
window.Logger.log('INFO', 'Module loaded', { module: 'example.md' });
window.Logger.error('Failed to load', { error: err.message });
```

### Python Logging
```python
# Backend API
import logging
logger = logging.getLogger(__name__)
logger.info('API request received', extra={'endpoint': '/api/search'})
```

## Monitoring

- **Grafana Dashboard**: http://localhost:3000/logs
- **Log Aggregation**: Configured for ELK stack (optional)
- **Alerting**: Critical errors trigger notifications

## Compliance

Logs support regulatory compliance for:
- **21 CFR Part 11**: FDA electronic records
- **EU Annex 11**: Computerized systems validation
- **ISO 13485**: Medical device quality management

## Troubleshooting

### High log volume
Adjust log levels in `os/config/logging.yaml`

### Missing logs
Check write permissions and disk space

### Log corruption
Validate with: `python os/scripts/validate-logs.py`

---

**Last Updated**: 2025-11-15
**Maintained By**: Chazon System Administrators
