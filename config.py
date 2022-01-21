"""
Config file for app settings and environment variables
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test=False):
    app = Flask(__name__)
    if test:
        database_path = 'sqlite:///databases/test_db.sqlite3'
    else:
        database_path = 'sqlite:///databases/gudlft_db.sqlite3'
    app.secret_key = 'something_special'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


app = create_app()
db = SQLAlchemy(app)
from models.clubs import Club
from models.competitions import Competition
db.create_all()
db.session.commit()
