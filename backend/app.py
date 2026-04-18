from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Flask Backend Running!", "status": "healthy"})

@app.route('/api/all')
def all_stats():
    return jsonify({
        "users": {"count": 1200, "label": "Active Users"},
        "projects": {"count": 45, "label": "Ongoing Projects"},
        "revenue": {"amount": ",500", "label": "Total Revenue"},
        "performance": {"status": "Good", "uptime": "99.9%"}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
