# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

app = Flask(__name__)

TARGET_USER = "test_user"
CORRECT_PASS = "secret123"
FAILED_ATTEMPTS = 0

@app.route('/login', methods=['POST'])
def login():
    global FAILED_ATTEMPTS
    
    username = request.form.get('username')
    password = request.form.get('password')

    if FAILED_ATTEMPTS >= 5:
        return jsonify({"status": "blocked", "message": "Blocked IP!"}), 429

    if username == TARGET_USER and password == CORRECT_PASS:
        FAILED_ATTEMPTS = 0
        msg = "Correct password: " + str(password)
        return jsonify({"status": "success", "message": msg}), 200
    else:
        FAILED_ATTEMPTS += 1
        return jsonify({"status": "failed", "message": "Wrong password!"}), 401

if __name__ == '__main__':
    print("Server running on port 5000...")
    app.run(port=5000)
