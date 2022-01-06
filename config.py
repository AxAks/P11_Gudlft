"""
Config file for app settings and environment variables
"""
from utils import load

db_path = 'gudlft_db.json'

gudlft_database = load(db_path)

competitions = gudlft_database['competitions']
clubs = gudlft_database['clubs']
