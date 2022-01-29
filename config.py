"""
Config file for app settings and environment variables
"""
from typing import Dict, List

from flask import Flask
from utils import load


def create_app():
    app = Flask(__name__)
    app.secret_key = 'something_special'
    return app


def declare_db_path() -> str:
    return 'database.json'


def setup_db() -> Dict[str, List]:
    db_path = declare_db_path()
    database = load(db_path)
    return database
