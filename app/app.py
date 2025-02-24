from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/getcode", methods=["GET"])
def getcode():
    return "Hi my name is khris bharmmano"


@app.route("/is_prime/<num1>", methods=["GET"])
def is_prime(num1):
    with app.app_context():
        try:
            num = int(num1)
            if num < 2:
                result = {"result": False}
                return jsonify(result), 200
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    result = {"result": False}
                    return jsonify(result), 200

            result = {"result": True}
            return jsonify(result), 200

        except ValueError:
            result = {"error_msg": "Input must be a valid integer"}
            return jsonify(result), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
