from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/getcode", methods=["GET"])
def getcode():
    return "Hi my name is khris bharmmano"


@app.route("/plus/<num1>/<num2>", methods=["GET"])
def plus(num1, num2):
    with app.app_context():
        try:
            num1 = float(num1)
            num2 = float(num2)

            print("Hello World!")

            ans = num1 + num2

            if ans.is_integer():
                ans = int(ans)

            result = {"result": ans}
            return jsonify(result), 200

        except ValueError:
            result = {"error_msg": "Inputs must be valid numbers"}
            return jsonify(result), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
