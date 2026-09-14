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
        return jsonify({"status": "blocked", "message": "ئایپی هاتیە قفلکرن! زێدەتر ژ ٥ هەوڵدانان کرینە."}), 429

    if username == TARGET_USER and password == CORRECT_PASS:
        FAILED_ATTEMPTS = 0
        return jsonify({"status": "success", "message": f"پاسوردێ درست هاتە دیتن: {password}"}), 200
    else:
        FAILED_ATTEMPTS += 1
        return jsonify({"status": "failed", "message": "پاسورد شاشە!"}), 401

if __name__ == '__main__':
    print("سێرڤەرێ لۆکال دەستبکار بوو ل سەر: http://127.0.0.1:5000")
    app.run(port=5000)
