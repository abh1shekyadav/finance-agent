import { useState } from "react";

function App() {
  const [response, setResponse] = useState<{ observations: string[]; suggestions: string[] } | null>(null);
  const [loading, setLoading] = useState(false);

  const handleAskAI = async () => {
    setLoading(true);
    setResponse(null);

    try {
      const res = await fetch("http://localhost:8000/ask-ai");
      const data = await res.json();

      let raw = data.response;

      // Clean up code fences
      if (typeof raw === "string") {
        raw = raw.replace(/```json\n?/, "").replace(/\n?```$/, "");
      }

      const parsed = JSON.parse(raw);
      setResponse(parsed);
    } catch (err) {
      alert("Error connecting to backend.");
      console.error("Parsing or fetch error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-sky-50 to-indigo-100 p-6 text-gray-900">
      <div className="max-w-3xl mx-auto space-y-6">
        <h1 className="text-4xl font-bold text-indigo-800">📊 Finance AI Advisor</h1>

        <button
          onClick={handleAskAI}
          disabled={loading}
          className="bg-indigo-600 text-white px-6 py-3 rounded-xl shadow-md hover:bg-indigo-700 disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Analyze Portfolio"}
        </button>

        {response && (
          <div className="space-y-6">
            {/* Observations */}
            <section>
              <h2 className="text-2xl font-semibold text-indigo-700">🔍 Observations</h2>
              <div className="grid md:grid-cols-2 gap-4 mt-3">
                {response.observations.map((obs, idx) => (
                  <div key={idx} className="p-4 bg-white border-l-4 border-blue-400 rounded-md shadow-sm">
                    <p className="text-gray-800">{obs}</p>
                  </div>
                ))}
              </div>
            </section>

            {/* Suggestions */}
            <section>
              <h2 className="text-2xl font-semibold text-emerald-700">💡 Suggestions</h2>
              <div className="grid md:grid-cols-2 gap-4 mt-3">
                {response.suggestions.map((sugg, idx) => (
                  <div key={idx} className="p-4 bg-white border-l-4 border-green-400 rounded-md shadow-sm">
                    <p className="text-gray-800">{sugg}</p>
                  </div>
                ))}
              </div>
            </section>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
