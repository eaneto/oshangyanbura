from flask import Blueprint, render_template
from flask_login import login_required, current_user

from werkzeug.exceptions import NotFound

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/home")
@login_required
def home():
    return render_template("home.html", customer_name=current_user.name)


@main_bp.route("/about")
def about():
    return render_template("about.html")


@main_bp.errorhandler(NotFound)
def handle_not_found(e):
    return render_template("notfound.html"), 404
