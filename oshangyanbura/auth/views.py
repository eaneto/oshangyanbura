from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from structlog import get_logger
from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, SignupForm
from . import auth_bp as auth
from ..models import Customer
from .. import db, login_manager

log = get_logger()

@login_manager.user_loader
def load_user(customer_id):
    return Customer.query.get(int(customer_id))

@auth.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        log.info("Logging user")
        customer = Customer.query.filter_by(email=form.email.data).first()
        if not customer:
            flash("Email not registered.")
            return redirect(url_for("auth.login"))

        if not check_password_hash(customer.password, form.password.data):
            flash("Check your login details and try again.")
            return redirect(url_for("auth.login"))

        login_user(customer)
        return redirect(url_for("main.home"))
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route("/signup", methods=("GET", "POST"))
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        log.info("Registering customer")
        hashed_password = generate_password_hash(form.password.data)
        customer = Customer(name = form.name.data,
                 email = form.email.data,
                 password = hashed_password)
        db.session.add(customer)
        try:
            db.session.commit()
            log.info("Customer registered successfully")
            return redirect(url_for("main.index"))
        except IntegrityError:
            db.session.rollback()
            flash("Email already registered.")
            return redirect(url_for("auth.signup"))

    return render_template("auth/signup.html", form=form)
