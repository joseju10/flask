from flask import Flask, render_template
app = Flask(__name__)

import json

from operator import  eq
with open("books.json") as fichero:
    datos_json=json.load(fichero)

@app.route('/')
def inicio():
    libros=datos_json
    return render_template("inicio.html",libros=libros)

app.run("0.0.0.0",5000,debug=True)