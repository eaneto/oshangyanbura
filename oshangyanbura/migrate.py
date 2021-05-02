import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

def get_database_url():
    return os.environ['DATABASE_URL'].replace("postgres", "postgresql")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_database_url()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
