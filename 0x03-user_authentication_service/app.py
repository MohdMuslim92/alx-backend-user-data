#!/usr/bin/env python3
"""
Basic Flask App for user authentication.
"""
from flask import abort, Flask, jsonify, redirect, request
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


@app.route('/sessions', methods=['POST'])
def login():
    """
    Handle user login.

    Expects form data with "email" and "password" fields.
    If the login information is correct, creates a new session for the user,
    stores the session ID as a cookie, and returns a JSON payload.
    If the login information is incorrect, responds with a 401 HTTP status.
    """
    try:
        email = request.form['email']
        password = request.form['password']

        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(401, 'Unauthorized')
    except KeyError:
        abort(400, 'Bad Request')


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logout route to destroy the session."""
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """Profile route to get user information."""
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
