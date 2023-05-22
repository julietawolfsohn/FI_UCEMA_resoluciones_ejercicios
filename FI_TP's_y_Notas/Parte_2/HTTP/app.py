
from flask import Flask

app = Flask(__name__)  #app va a ser el nombre que le de a mi servidor 

@app.get("/")
def home():
    return "<p> Te damos la bienvenida </p>"    #<p> --> etiqueta de parrafo en HTML