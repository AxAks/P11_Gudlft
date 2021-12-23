import json
from typing import Union, Dict

from flask import Flask, render_template, request, redirect, flash, url_for


def load_database(db_file):
    """
    Loads all the objects instances from the database file needed by the program at once
    """
    with open(db_file) as db:
        database = json.load(db)
        return database


app = Flask(__name__)
app.secret_key = 'something_special'

gudlft_database = load_database('gudlft_db.json')

competitions = gudlft_database['competitions']
clubs = gudlft_database['clubs']


@app.route('/')
def index():
    """

    """
    return render_template('index.html')


@app.route('/show_summary', methods=['POST'])
def show_summary():
    """
    Redirects the user to their account summary page if the entered email is correct
    """
    email = extract_email_from_request()
    club = find_club(email)
    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash("The entered Email could not be found, please retry")
        return redirect(url_for('index'))


def extract_email_from_request():
    """
    Enables to get the entered email from the request
    """
    email = request.form['email']
    return email


def find_club(email: str) -> Union[Dict, None]:
    """
    Searches a club whose registered contact email matches the email given as parameter
    """
    for club in clubs:
        if email == club['email']:
            return club


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """

    """
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchase_places', methods=['POST'])
def purchase_places():
    """

    """
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
def display_points():
    pass


@app.route('/logout')
def logout():
    """

    """
    return redirect(url_for('index'))
