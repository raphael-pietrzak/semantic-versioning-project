from flask import Flask, jsonify

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
    return jsonify({"name": main.name, "version": main.version})


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    main = Main()
    result = main.add_numbers(a, b)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
