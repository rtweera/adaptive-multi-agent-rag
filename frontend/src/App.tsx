import { useEffect, useState } from "react"

const API = "http://localhost:8008"

function App() {
  const [health, setHealth] = useState("checking")
  const [postgres, setPostgres] = useState("checking")
  const [redis, setRedis] = useState("checking")
  const [message, setMessage] = useState("")
  const [response, setResponse] = useState("")

  useEffect(() => {
    fetch(`${API}/health`)
      .then((res) => { if (!res.ok) throw new Error(); return res.json() })
      .then(() => setHealth("online"))
      .catch(() => setHealth("offline"))

    fetch(`${API}/postgres-test`)
      .then((res) => { if (!res.ok) throw new Error(); return res.json() })
      .then((data) => setPostgres(data.postgres))
      .catch(() => setPostgres("failed"))

    fetch(`${API}/redis-test`)
      .then((res) => { if (!res.ok) throw new Error(); return res.json() })
      .then((data) => setRedis(data.redis))
      .catch(() => setRedis("failed"))
  }, [])

  async function sendMessage() {
    const controller = new AbortController()
    const timeout = setTimeout(() => controller.abort(), 10000) // 10 second timeout

    try {
      const res = await fetch(`${API}/demo-chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message }),
        signal: controller.signal
      })

      const data = await res.json()
      setResponse(data.response)
    } catch (err) {
      if (err instanceof Error && err.name === "AbortError") {
        setResponse("Service unavailable — request timed out.")
      } else {
        setResponse("Service unavailable.")
      }
    } finally {
      clearTimeout(timeout)
    }
  }


  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto space-y-6">
        <h1 className="text-4xl font-bold">
          Adaptive Multi-Agent RAG Platform
        </h1>

        <div className="grid grid-cols-3 gap-4">
          <div className="bg-white p-4 rounded-xl shadow">
            <h2 className="font-semibold">Backend</h2>
            <p>{health}</p>
          </div>

          <div className="bg-white p-4 rounded-xl shadow">
            <h2 className="font-semibold">PostgreSQL</h2>
            <p>{postgres}</p>
          </div>

          <div className="bg-white p-4 rounded-xl shadow">
            <h2 className="font-semibold">Redis</h2>
            <p>{redis}</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow space-y-4">
          <h2 className="text-2xl font-semibold">Demo Chat</h2>

          <input
            className="w-full border p-3 rounded-lg"
            placeholder="Type a message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <button
            onClick={sendMessage}
            className="bg-black text-white px-4 py-2 rounded-lg"
          >
            Send
          </button>

          <div className="border rounded-lg p-4 bg-gray-50">
            {response || "No response yet"}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App