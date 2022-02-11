"""
Config file for app settings and environment variables
"""
from typing import Dict, List

from flask import Flask

from utils import load


def create_app():
    """
    Create the Flask app used by the program
    """
    app = Flask(__name__)
    app.secret_key = 'something_special'
    return app


def declare_db_path() -> str:
    """
    Set the path of the JSon DB file
    """
    return 'database.json'


def setup_db() -> Dict[str, List]:
    """
    Initiates the DB from the Json file located at the DB path
    """
    db_path = declare_db_path()
    database = load(db_path)
    return database


def setup_registry(clubs: List, competitions: List) -> Dict[str, List[Dict[str, int]]]:
    """
    initiates the purchased places per club for all competitions to 0.
    Places purchased by a club for a competition will be added to the registry
    to prevent them to book more places than the authorized limit
    """
    return {club['name']: [{competition['name']: 0} for competition in competitions] for club in clubs}
