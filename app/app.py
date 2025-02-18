from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/getcode", methods=["GET"])
def getcode():
    return "Hi my name is Khris Bharmmano"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def plus(num1, num2):
    try:
        result = float(num1) + float(num2)
        return jsonify({"result": int(result) if result.is_integer() else result}), 200
    except ValueError:
        return jsonify({"error_msg": "Inputs must be valid numbers"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
