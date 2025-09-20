from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # <-- This enables CORS for all routes

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
    app.run(debug=True)
