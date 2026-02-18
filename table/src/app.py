from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Create database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Create user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (data["name"], data["email"]))
    conn.commit()
    conn.close()
    return jsonify({"message": "User added"})

# Read users
@app.route("/users", methods=["GET"])
def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

# Update user
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (data["name"], data["email"], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated"})

# Delete user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)