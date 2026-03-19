from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to Tejas Web App 🚀"

# Add API
@app.route("/add", methods=["GET"])
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(debug=True)
