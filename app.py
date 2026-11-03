import os
import sqlite3
from datetime import datetime, timezone
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

DB_NAME = "opspilot.db"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>OpsPilot AI</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #101827;
            color: white;
            margin: 0;
            padding: 30px;
        }
        .container {
            max-width: 850px;
            margin: auto;
        }
        .card {
            background: #1e293b;
            padding: 22px;
            border-radius: 12px;
            margin-top: 20px;
        }
        input, textarea, select, button {
            width: 100%;
            box-sizing: border-box;
            padding: 12px;
            margin: 8px 0 16px;
            border-radius: 6px;
            border: 1px solid #475569;
        }
        button {
            background: #14b8a6;
            color: #06201d;
            font-weight: bold;
            cursor: pointer;
        }
        .status { color: #fbbf24; }
        .agent { color: #5eead4; }
    </style>
</head>
<body>
<div class="container">
    <h1>🚀 OpsPilot AI</h1>
    <p>Multi-Agent AI-Powered IT Incident Response Platform</p>

    <div class="card">
        <h2>Report a New Incident</h2>
        <form id="incidentForm">
            <label>Incident title</label>
            <input name="title" required
                   placeholder="Example: Company website is down">

            <label>Description</label>
            <textarea name="description" required
                      placeholder="Describe the issue..."></textarea>

            <label>Reported priority</label>
            <select name="priority">
                <option>High</option>
                <option>Critical</option>
                <option>Medium</option>
                <option>Low</option>
            </select>

            <button type="submit">Submit Incident</button>
        </form>
        <p id="result"></p>
    </div>

    <div class="card">
        <h2>Multi-Agent Workflow</h2>
        <p class="agent">1. Triage Agent — classifies severity</p>
        <p class="agent">2. Investigation Agent — identifies possible causes</p>
        <p class="agent">3. Resolution Agent — recommends a safe fix</p>
        <p class="agent">4. Verification Agent — checks recovery criteria</p>
        <p class="status">Incident remains OPEN until human approval
        and independent verification.</p>
    </div>

    <div class="card">
        <h2>Recent Incidents</h2>
        <div id="incidents">Loading...</div>
    </div>
</div>

<script>
async function loadIncidents() {
    const response = await fetch("/api/incidents");
    const incidents = await response.json();

    document.getElementById("incidents").innerHTML =
        incidents.length
        ? incidents.map(item => `
            <p><b>${item.id}</b> — ${item.title}
            <br>Priority: ${item.priority}
            | Status: ${item.status}</p>
        `).join("")
        : "No incidents reported yet.";
}

document.getElementById("incidentForm").onsubmit = async function(e) {
    e.preventDefault();

    const data = Object.fromEntries(new FormData(this));

    const response = await fetch("/api/incidents", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").textContent =
        result.message || result.error;

    if (response.ok) {
        this.reset();
        loadIncidents();
    }
};

loadIncidents();
</script>
</body>
</html>
"""


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS incidents (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/api/incidents", methods=["GET"])
def get_incidents():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM incidents ORDER BY created_at DESC"
        ).fetchall()
        return jsonify([dict(row) for row in rows])


@app.route("/api/incidents", methods=["POST"])
def create_incident():
    data = request.get_json(silent=True) or {}

    title = data.get("title", "").strip()
    description = data.get("description", "").strip()
    priority = data.get("priority", "Medium")

    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    if priority not in ["Critical", "High", "Medium", "Low"]:
        return jsonify({"error": "Invalid priority"}), 400

    with sqlite3.connect(DB_NAME) as conn:
        count = conn.execute(
            "SELECT COUNT(*) FROM incidents"
        ).fetchone()[0]

        incident_id = f"INC-{count + 1:03d}"

        conn.execute("""
            INSERT INTO incidents
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            incident_id,
            title,
            description,
            priority,
            "OPEN",
            datetime.now(timezone.utc).isoformat()
        ))

    return jsonify({
        "message": f"{incident_id} created successfully. Status: OPEN",
        "incident_id": incident_id
    }), 201


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "application": "OpsPilot AI"})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
