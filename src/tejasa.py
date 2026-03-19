from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to Tejas Web App 🚀", 200


# Add API
@app.route("/add", methods=["GET"])
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b}), 200
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


# Health check (extra good practice)
@app.route("/health")
def health():
    return jsonify({"status": "OK"}), 200


# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
