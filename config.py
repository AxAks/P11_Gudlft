"""
Config file for app settings and environment variables
"""
import json
from typing import Dict
from flask import Flask


def load_database(db_file: str) -> Dict:
    """
    Loads all the objects instances from the database file needed by the program at once
    """
    with open(db_file) as db:
        database = json.load(db)
        return database


app = Flask(__name__)
app.secret_key = 'something_special'

gudlft_database = load_database('gudlft_db.json')


