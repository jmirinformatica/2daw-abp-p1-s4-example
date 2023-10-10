from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "Valor aleatori molt llarg i super secret"

@app.route('/')
def init():
    return "Hola des de Flask!"

@app.route("/hola/<nom>")
def hola(nom):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return f"Hola {nom}. La data i hora d'ara mateix és: {formatted_now}"
