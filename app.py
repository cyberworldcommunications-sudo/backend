from flask import Flask, jsonify
from flask_cors import CORS
import random
import os  # <-- Needed to get the PORT from the environment

app = Flask(__name__)
CORS(app)

quotes = [
    "Stay hungry, stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "MAN IS NOT A MACHINE"
]

@app.route('/api/quote')
def quote():
    return jsonify({'quote': random.choice(quotes)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # <-- Use Render-provided port
    app.run(host="0.0.0.0", port=port, debug=True)
