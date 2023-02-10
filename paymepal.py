from flask import Flask, render_template, request, session
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["SECRET_KEY"] = "very secret stuff"
engine = create_engine("sqlite:///paymepal.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["user"]
    password = request.form["password"]

    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "';"

    with engine.connect() as connection:
        # use fetchone()
        row = connection.execute(query)

        if row:
            session["username"] = username
            session["user_id"] = row[0]
            
            return "OK"

        return str(rows)


app.run(debug=True, port=8080)