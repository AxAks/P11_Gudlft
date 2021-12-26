"""
Main File
containing flask routing functions
"""

from config import app, db_path, gudlft_database, competitions, clubs
from utils import save_database

from flask import render_template, request, redirect, flash, url_for

from lib_request.lib_request import extract_club_email, extract_competition_name,\
    extract_club_name, extract_required_places
from lib_database.lib_database import get_club_by_email, get_competition_by_name, get_club_by_name


@app.route('/')
def index():
    """
    Displays to the website homepage
    """
    return render_template('index.html')


@app.route('/show_summary', methods=['POST'])
def show_summary():
    """
    Redirects the user to their account summary page if the entered email is correct
    or asks to retry with a valid address
    """
    email = extract_club_email(request)
    club = get_club_by_email(email)
    if club:
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        flash("The entered email could not be found, please enter a registered email")
        return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """
    leads the user to the ticket booking page for a given competition

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
    Enables the user to buy tickets for a given competition
    """
    competition_name = extract_competition_name(request)
    club_name = extract_club_name(request)
    places_required_as_int = extract_required_places(request)

    competition = get_competition_by_name(competition_name)
    club = get_club_by_name(club_name)
    total_places_as_int = int(competition['numberOfPlaces'])
    total_points_as_int = int(club['points'])

    if total_places_as_int - places_required_as_int < 0:
        flash('You cannot purchase this amount of place. There are not enough places left!')

    if total_points_as_int - places_required_as_int < 0:
        flash('You cannot purchase this amount of place. You do not have enough points!')

    if (total_places_as_int - places_required_as_int >= 0) and (total_points_as_int - places_required_as_int >= 0):
        competition['numberOfPlaces'] = total_places_as_int - places_required_as_int
        club['points'] = total_points_as_int - places_required_as_int

        for club_in_db in gudlft_database['clubs']:
            if club_in_db['name'] == club['name']:
                club_in_db['points'] = str(club['points'])

        for competition_in_db in gudlft_database['competitions']:
            if competition_in_db['name'] == competition['name']:
                competition_in_db['numberOfPlaces'] = str(competition['numberOfPlaces'])

        save_database(gudlft_database, db_path)
        flash('Great-booking complete!')

    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display (no need to be logged, on the homepage)
def display_points():
    """

    """
    pass


@app.route('/logout')
def logout():
    """
    Enables the user to logout and be redirected to the homepage
    """
    return redirect(url_for('index'))
