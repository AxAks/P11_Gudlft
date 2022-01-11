"""

"""
import json
from typing import Dict

from flask_sqlalchemy import SQLAlchemy


def load(db_file: str) -> Dict:
    """
    Loads all the objects instances from the database file needed by the program at once
    """
    with open(db_file) as db:
        database = json.load(db)
        return database


def save(database: SQLAlchemy, db_file: str) -> None:
    """
    saves all the objects instances of the program database to the database file
    """
    with open(db_file, "w") as db:
        return json.dump(database, db)
