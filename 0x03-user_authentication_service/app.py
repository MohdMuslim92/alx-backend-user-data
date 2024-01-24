#!/usr/bin/env python3
"""
Basic Flask App for user authentication.
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome() -> str:
    """A simple GET route that returns a JSON payload."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """Endpoint to register a user."""
    try:
        email = request.form["email"]
        password = request.form["password"]
        AUTH.register_user(email, password)
        response = {"email": email, "message": "user created"}
        return jsonify(response), 200
    except ValueError:
        response = {"message": "email already registered"}
        return jsonify(response), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
