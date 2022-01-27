"""
Config file for app settings and environment variables
"""
from flask import Flask
from utils import load


def create_app():
    app = Flask(__name__)
    app.secret_key = 'something_special'
    return app


def declare_db_path():
    return 'gudlft_db.json'


def setup_db():
    db_path = declare_db_path()
    database = load(db_path)
    return database
