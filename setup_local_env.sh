#!/bin/sh

source .venv/bin/activate
export FLASK_ENV=development
export FLASK_APP=oshangyanbura
export DATABASE_URL="postgresql://user:user@localhost:5432/oshangyanbura"
flask run
