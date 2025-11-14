# Sync Engine
**Multi-Device Synchronization** | Conflict Resolution

Keep all instances in sync using UUID-based changelogs.

```javascript
const SyncEngine = {
  localId: null,
  peers: [],

  init() {
    this.localId = ChangeLog.uuid();
    console.log(`🔄 Sync initialized: ${this.localId.slice(0,8)}`);
  },

  // Export current state
  export() {
    return {
      id: this.localId,
      timestamp: Date.now(),
      changelog: ChangeLog.get(1000),
      states: PackML.machines,
      sqlite: SQLiteDB.export()
    };
  },

  // Import from another instance
  import(snapshot) {
    if (!snapshot || !snapshot.id) return { error: 'Invalid snapshot' };

    // Merge changelogs by UUID (no duplicates)
    const localChanges = ChangeLog.get(1000);
    const remoteChanges = snapshot.changelog || [];

    const merged = [...localChanges, ...remoteChanges].reduce((acc, record) => {
      if (!acc.find(r => r.id === record.id)) acc.push(record);
      return acc;
    }, []);

    // Merge states (most recent wins)
    Object.entries(snapshot.states || {}).forEach(([id, state]) => {
      if (!PackML.machines[id] || state.timestamp > PackML.machines[id].timestamp) {
        PackML.machines[id] = state;
      }
    });

    // Merge SQLite tables
    if (snapshot.sqlite) {
      SQLiteDB.import(snapshot.sqlite);
    }

    ChangeLog.record('sync_complete', {
      from: snapshot.id,
      merged: merged.length,
      conflicts: 0
    });

    return { success: true, merged: merged.length };
  },

  // Auto-sync via localStorage broadcast
  broadcast() {
    const snapshot = this.export();
    localStorage.setItem('chazon:sync:broadcast', JSON.stringify(snapshot));
  },

  listen() {
    window.addEventListener('storage', (e) => {
      if (e.key === 'chazon:sync:broadcast' && e.newValue) {
        const snapshot = JSON.parse(e.newValue);
        if (snapshot.id !== this.localId) {
          this.import(snapshot);
        }
      }
    });
  }
};

window.SyncEngine = SyncEngine;
```
