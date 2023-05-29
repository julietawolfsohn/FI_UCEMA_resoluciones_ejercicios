
from flask import Flask
prendas = [
    {"id":1, "tipo": "pantalon", "talle": 42}, 
    {"id":2, "tipo": "pantalon", "talle": 56},
]
app = Flask(__name__)  #app va a ser el nombre que le de a mi servidor 

@app.get("/")
def home():
    return "<p> Te damos la bienvenida </p>"    #<p> --> etiqueta de parrafo en HTML


#EJERCICIO: armar la ruta/prendas que muestre todos los items de prendas

