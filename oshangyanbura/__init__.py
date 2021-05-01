from flask import Flask, render_template
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(NotFound)
def handle_not_found(e):
    return render_template("notfound.html"), 404


if __name__ == "__main__":
    app.run()
