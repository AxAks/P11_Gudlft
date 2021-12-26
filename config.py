"""
Config file for app settings and environment variables
"""
from utils import load_database
from flask import Flask


app = Flask(__name__)
app.secret_key = 'something_special'
db_path = 'gudlft_db.json'

gudlft_database = load_database(db_path)

competitions = gudlft_database['competitions']
clubs = gudlft_database['clubs']

