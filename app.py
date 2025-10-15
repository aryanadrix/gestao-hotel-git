from flask import Flask, render_template
from clientes import clientes
from quartos import quartos
from reservas import reservas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('interface.html', clientes=clientes, quartos=quartos, reservas=reservas)

if __name__ == "__main__":
    app.run(debug=True)
