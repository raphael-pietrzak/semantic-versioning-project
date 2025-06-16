from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


class Main:
    def __init__(self):
        self.name = "Main"
        self.version = "1.0.0"

    def add_numbers(self, a, b):
        """Ajoute deux nombres et retourne le résultat."""
        return a + b


@app.route("/")
def index():
    main = Main()
    return render_template("index.html", name=main.name, version=main.version)


@app.route("/add", methods=["POST"])
def add():
    main = Main()
    a = int(request.form["num1"])
    b = int(request.form["num2"])
    result = main.add_numbers(a, b)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
