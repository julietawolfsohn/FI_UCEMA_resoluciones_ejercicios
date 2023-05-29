
from flask import Flask, render_template
from markupsafe import escape

prendas = [
    {"id":1, "tipo": "pantalon", "talle": 42}, 
    {"id":2, "tipo": "pantalon", "talle": 56},
]
app = Flask(__name__)  #app va a ser el nombre que le de a mi servidor 

@app.get("/")
def home():
    return render_template("home.html")  # me va a tener que renderizar home.html

"""
"<p> Te damos la bienvenida </p>"    #<p> --> etiqueta de parrafo en HTML
"""


#EJERCICIO: armar la ruta/prendas que muestre todos los items de prendas

@app.get("/prendas")
def get_all_prendas(): #cuando le pegue a este get en paricular va a obtener todas las prendas
    return f"<p>Mostrando todas las prendas<p>"  #"f "" perimte meter algun texto o variable dentro del string"

#se printea y en lapag web se le agrega /prendas


@app.get("/prendas/<id>")  #<id> asume que se le puede pasar cualquier id-- se programa una sola vez para todas las prendas
def get_prenda(id):
    return f"<p>Mostrando la prenda{escape(id)}</p>" #{id} me va a decir cual es la prenda que quiero sin tener que indicarla - flask lo hace solo
                                                     # / --> es un espacio 
                                                     # {escape(id)} --> poner siempre el escape - es para que no te hakeen 
                                            
                                             
    