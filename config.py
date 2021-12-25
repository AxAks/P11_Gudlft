"""
Config file for app settings and environment variables
"""
from utils import load_database
from flask import Flask


app = Flask(__name__)
app.secret_key = 'something_special'

gudlft_database = load_database('gudlft_db.json')

competitions = gudlft_database['competitions']
clubs = gudlft_database['clubs']

