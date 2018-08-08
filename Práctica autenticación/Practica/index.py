from flask import Flask, render_template, request
from sklearn.externals import joblib

from login import Login

app = Flask(__name__)


@app.route("/")
def index():
    # Login sin almacenar datos
    return render_template("ai_auth.html")


@app.route("/train")
def train():
    # Login almacenando datos para mejorar el modelo
    return render_template("ai_auth_train.html")


@app.route("/login", methods=['POST'])
def login():
    # Almacenamos los valores del tiempo de presionado y tiempo de vuelo
    login = Login()
    login.tiempo_presionado = float(request.form['presionado'])
    login.tiempo_vuelo = float(request.form['vuelo'])

    # Campo para el entrenamiento, indica si el que hace login es el usuario autorizado
    if request.form.get("nombre") is not None:
        login.usuario = True
    else:
        login.usuario = False

    # Si estamos en modo entramiento guardamos los datos en la BBDD
    if request.form.get("train") is not None:
        login.save()

    # Cargamos el modelo de ML
    algo = joblib.load('gradient_boosting.pkl')
    login.predict(algo)

    return render_template("ai_auth_result.html", login=login)


app.debug = True

if __name__ == "__main__":
    app.run()
