"""
Config file for app settings and environment variables
"""
from flask import Flask
from utils import load

db_path = 'gudlft_db.json'
database = load(db_path)
competitions = database['competitions']
clubs = database['clubs']


def create_app():
    app = Flask(__name__)
    app.secret_key = 'something_special'
    return app
