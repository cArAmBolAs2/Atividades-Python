from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return calcular()
    # Em GET, exibe a calculadora limpa
    return render_template("calculadora.html", etapas=None, resultados=None)

if __name__ == "__main__":
    app.run(debug=True)