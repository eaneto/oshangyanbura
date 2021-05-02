from flask import Blueprint, render_template

auth_bp = Blueprint("auth", __name__)

from . import views
