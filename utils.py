"""

"""
import json
from typing import Dict


def load(db_path: str) -> Dict:
    """
    Loads all the objects instances from the database file needed by the program at once
    """
    with open(db_path) as db:
        database = json.load(db)
        return database


def save(database: Dict, db_path: str) -> None:
    """
    saves all the objects instances of the program database to the database file
    """
    with open(db_path, "w") as db:
        return json.dump(database, db)
