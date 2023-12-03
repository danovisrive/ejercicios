from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/")
def hodano():
    return "<center> <h1>hola desde falsk danobis </h1> <center> <hr>"
    
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=00,nota3=0):
    resultado = (nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1> el resultado es: {resultado} </h1>"



@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad =0):

    if edad < 18 and edad > 0:
        r = edad
        return f"es menor de edad tiene {r}"
    
    elif edad > 18 and edad < 60:
        r = edad
        return f"es mayor de edad tiene {r}"
    
    else:
        r = edad
        return f"la persona es adulto mayor tiene {r}"
    

import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores =0, columnas =0, filas = 0):
    if filas == 0:
        arreglos = np.random.randint(valores, size=columnas)
    else:
        arreglos = np.random.randint(valores, size=(filas, columnas))
    return f"<h1> arreglo aleatorio: {arreglos} </h1> <hr>"


    
if __name__== "__main__":
    app.run(debug=True)