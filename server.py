from flask import Flask, request, jsonify
import os

from functions import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("index.html")

@app.route("/api/characters", methods=["GET"])
def get_characters():
    character_list = fetch_character_list()
    return jsonify(character_list)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="healthy")

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(received=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)