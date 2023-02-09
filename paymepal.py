from flask import Flask, render_template, request
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine("sqlite:///paymepal.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    return render_template("unauthorized.html"), 403


app.run(debug=True, port=8080)