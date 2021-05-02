from flask import Blueprint, render_template

from werkzeug.exceptions import NotFound

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/about")
def about():
    return render_template("about.html")


@main_bp.errorhandler(NotFound)
def handle_not_found(e):
    return render_template("notfound.html"), 404
