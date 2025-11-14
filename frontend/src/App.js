import { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [mode, setMode] = useState('hybrid');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

  const search = async () => {
    if (!query.trim()) {
      alert('Please enter a query');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_URL}/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ q: query, mode: mode })
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }

      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      search();
    }
  };

  return (
    <div className="App">
      <header className="header">
        <h1 className="title">🏭 AUTOMATIONGPT [ISA∞]</h1>
        <div className="subtitle">Multimodal ISA Standards Search Engine</div>
      </header>

      <div className="legend">
        <div className="legend-title">LEGEND</div>
        🔍=Qdrant | 🧠=Femto | 🎵=Audio | 📸=Img | 💻=Code | 🏭=ISA-95 | 🧪=ISA-88 | 🚨=ISA-18.2 | 🎯=Agent | ⚡=CPU | 📡=API
      </div>

      <div className="search-container">
        <div className="mode-selector">
          <label htmlFor="mode">Search Mode:</label>
          <select
            id="mode"
            value={mode}
            onChange={(e) => setMode(e.target.value)}
          >
            <option value="hybrid">🔄 Hybrid (All Modalities)</option>
            <option value="t">📝 Text/Standards</option>
            <option value="c">💻 Code</option>
            <option value="i">📸 Images/Diagrams</option>
            <option value="a">🎵 Audio</option>
          </select>
        </div>

        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Query ISA standards, code, diagrams..."
        />

        <button onClick={search} disabled={loading}>
          {loading ? '⏳ Searching...' : '🔍 Search'}
        </button>
      </div>

      {error && (
        <div className="error">
          <strong>ERROR:</strong> {error}<br /><br />
          Make sure the AutomationGPT API is running at {API_URL}
        </div>
      )}

      {results && (
        <div className="results">
          <div className="result-header">RESULTS</div>

          <div className="answer">
            <strong>ANSWER:</strong><br /><br />
            {results.answer}
          </div>

          {results.sources && results.sources.length > 0 && (
            <div className="sources">
              <strong>SOURCES:</strong><br /><br />
              {results.sources.map((source, i) => {
                const p = source.payload;
                return (
                  <div key={i} className="source-item">
                    {p.std && (
                      <div>
                        <span className="source-tag">[{p.std}:{p.sec || '?'}]</span> {p.txt}
                      </div>
                    )}
                    {p.code && (
                      <div>
                        <span className="source-tag">[CODE:{p.lang}]</span> {p.fn}<br />
                        <pre>{p.code.substring(0, 200)}...</pre>
                      </div>
                    )}
                    {p.title && (
                      <div>
                        <span className="source-tag">[AUDIO:{p.title}]</span> {p.lyr}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          )}

          <div className="metadata">
            Mode: {results.mode} | Sources: {results.context_count} | Time: {(results.retrieval_time * 1000).toFixed(0)}ms
          </div>
        </div>
      )}

      <div className="features">
        <div className="feature">
          <div className="feature-icon">🏭</div>
          <div className="feature-title">ISA Standards</div>
          <div>Search ISA-95, ISA-88, ISA-18.2</div>
        </div>

        <div className="feature">
          <div className="feature-icon">💻</div>
          <div className="feature-title">PLC Code</div>
          <div>Ladder Logic, ST, SCL</div>
        </div>

        <div className="feature">
          <div className="feature-icon">📸</div>
          <div className="feature-title">Diagrams</div>
          <div>P&IDs, HMI, Control Loops</div>
        </div>

        <div className="feature">
          <div className="feature-icon">🎵</div>
          <div className="feature-title">Audio</div>
          <div>Educational Songs</div>
        </div>

        <div className="feature">
          <div className="feature-icon">🧠</div>
          <div className="feature-title">AI-Powered</div>
          <div>Claude AI with RAG</div>
        </div>

        <div className="feature">
          <div className="feature-icon">⚡</div>
          <div className="feature-title">CPU-Only</div>
          <div>No GPU Required</div>
        </div>
      </div>

      <footer className="footer">
        <div>Built with Qdrant + Claude AI</div>
        <div><a href="https://github.com/teslasolar/qdrant">GitHub</a></div>
      </footer>
    </div>
  );
}

export default App;
