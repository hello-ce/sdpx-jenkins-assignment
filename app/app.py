from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/getcode", methods=["GET"])
def getcode():
    return "qqq"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def plus(num1, num2):
    with app.app_context():
        try:
            num1 = float(num1)
            num2 = float(num2)

            ans = num1 + num2

            if ans.is_integer():
                ans = int(ans)

            result = {"result": ans}
            return jsonify(result), 200

        except ValueError:
            result = {"error_msg": "Inputs must be valid numbers"}
            return jsonify(result), 400


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


@app.route("/cir_sur/<radius>", methods=["GET"])
def cir_sur(radius):
    with app.app_context():
        try:
            r = float(radius)
            if r < 0:
                result = {"result": 0.00}
                return jsonify(result), 200
            
            pi = 3.14
            area = 4 * pi * r**2

            # Convert to integer if the result is a whole number
            if area.is_integer():
                area = int(area)

            result = {"result": area}
            return jsonify(result), 200

        except ValueError:
            result = {"error_msg": "Input must be a valid number"}
            return jsonify(result), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
