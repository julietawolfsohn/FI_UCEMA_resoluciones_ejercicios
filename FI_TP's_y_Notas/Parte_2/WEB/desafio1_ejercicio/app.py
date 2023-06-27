from flask import Flask, render_template
from markupsafe import escape

juli = Flask(__name__)

@juli.get("/")
def home():
    return render_template("home.html")

