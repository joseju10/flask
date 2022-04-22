from flask import Flask, render_template, abort
app = Flask(__name__)

import json

from operator import  eq
with open("books.json") as fichero:
    datos_json=json.load(fichero)

@app.route('/')
def inicio():
    libros=datos_json
    return render_template("inicio.html",libros=libros)

@app.route('/libro/<isbn>')
def libro(isbn):
    dato="MEAP"
    for libro in datos_json:
        if libro["isbn"]==isbn:
            return render_template("libro.html",libro=libro,dato=dato)
    return abort(404)



app.run("0.0.0.0",5000,debug=True)