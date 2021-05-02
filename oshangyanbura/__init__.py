import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_database_url():
    return os.environ['DATABASE_URL'].replace("postgres", "postgresql")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
    db.init_app(app)

    from .main import main_bp
    app.register_blueprint(main_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
