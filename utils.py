"""

"""
import json
from typing import Dict, Any


def load_database(db_file: str) -> Dict:
    """
    Loads all the objects instances from the database file needed by the program at once
    """
    with open(db_file) as db:
        database = json.load(db)
        return database


def save_database(database: Dict, db_file: str) -> None:
    """
    Loads all the objects instances from the database file needed by the program at once
    """
    with open(db_file, "w") as db:
        return json.dump(database, db)
