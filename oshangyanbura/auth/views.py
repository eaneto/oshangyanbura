from flask import render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from structlog import get_logger

from .forms import LoginForm, SignupForm
from . import auth_bp as auth
from ..models import Customer
from .. import db, login_manager

log = get_logger()

@login_manager.user_loader
def load_user(email):
    return email

@auth.route("/login")
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@auth.route("/signup", methods=("GET", "POST"))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        log.info("Registering customer")
        hashed_password = generate_password_hash(form.password.data)
        customer = Customer(name = form.name.data,
                 email = form.name.data,
                 password = hashed_password)
        db.session.add(customer)
        db.session.commit()
        log.info("Customer registered succesfulyy")
        return redirect(url_for("main.index"))
    return render_template("auth/signup.html", form=form)
