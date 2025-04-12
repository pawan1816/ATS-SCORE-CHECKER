import React, { useState } from 'react';
import { checkATSScore } from './api'; // Import our API service

function App() {
  const [resume, setResume] = useState('');
  const [jobDesc, setJobDesc] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const data = await checkATSScore(resume, jobDesc); // Using our API function
    setResult(data);
    setLoading(false);
  };
  
  return (
    <div className="app">
      <h1>ATS Score Checker</h1>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Resume Text</label>
          <textarea 
            value={resume}
            onChange={(e) => setResume(e.target.value)}
            rows={10}
            required
          />
        </div>

        <div className="form-group">
          <label>Job Description</label>
          <textarea
            value={jobDesc}
            onChange={(e) => setJobDesc(e.target.value)}
            rows={10}
            required
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Analyzing...' : 'Check ATS Score'}
        </button>
      </form>

      {result && (
        <div className="results">
          <h2>Results</h2>
          {result.error ? (
            <p className="error">{result.error}</p>
          ) : (
            <>
              <p><strong>Score:</strong> {result.score}%</p>
              {result.analysis.missing_keywords.length > 0 && (
                <div>
                  <h3>Missing Keywords:</h3>
                  <ul>
                    {result.analysis.missing_keywords.map((word, i) => (
                      <li key={i}>{word}</li>
                    ))}
                  </ul>
                </div>
              )}
              {result.analysis.suggestions.length > 0 && (
                <div>
                  <h3>Suggestions:</h3>
                  <ul>
                    {result.analysis.suggestions.map((suggestion, i) => (
                      <li key={i}>{suggestion}</li>
                    ))}
                  </ul>
                </div>
              )}
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;

