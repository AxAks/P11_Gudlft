"""
Config file for app settings and environment variables
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_path = 'database/gudlft_db.sqlite3'


def create_app():
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database/gudlft_db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


app = create_app()
db = SQLAlchemy(app)
db.create_all()
