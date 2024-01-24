"""
Basic Flask App for user authentication.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    """A simple GET route that returns a JSON payload."""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)