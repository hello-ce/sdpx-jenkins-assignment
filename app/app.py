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
            
            result = {'result': ans}
            return jsonify(result), 200

        except ValueError:
            result = {"error_msg": "Inputs must be valid numbers"}
            return jsonify(result), 400


@app.route("/is_prime/<num1>", methods=["GET"])
def is_prime(num1):
    with app.app_context():
        try:
            num1 = int(num1)
            if num1 <= 1:
                return jsonify({"error_msg": "Number must be greater than 1"}), 400

            for i in range(2, num1):
                if num1 % i == 0:
                    return jsonify({"result": False}), 200

            return jsonify({"result": True}), 200

        except ValueError:
            return jsonify({"error_msg": "Input must be a valid integer"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
