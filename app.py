from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Supported operations
OPERATIONS = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}


@app.route("/")
def home():
    """Render the calculator page"""
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Receives JSON: {"a": number, "b": number, "op": "add|sub|mul|div"}
    Returns JSON: {"result": value} or {"error": message}
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    try:
        a = float(data["a"])
        b = float(data["b"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Please enter valid numbers"}), 400

    op = data.get("op")
    if op not in OPERATIONS:
        return jsonify({"error": "Unsupported operator"}), 400

    # Division by zero check
    if op == "div" and b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400

    result = OPERATIONS[op](a, b)

    # Drop trailing .0 for integer results (e.g. 4.0 -> 4)
    if result == int(result):
        result = int(result)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)