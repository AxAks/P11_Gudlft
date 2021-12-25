"""
Main File
containing flask routing functions
"""

from config import app, competitions, clubs
from flask import render_template, request, redirect, flash, url_for

from lib_request.lib_request import extract_club_email, extract_competition_name, \
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
    total_places_as_int = int(competition['numberOfPlaces'])
    club = get_club_by_name(club_name)

    competition['numberOfPlaces'] = total_places_as_int - places_required_as_int

    # TODO save into database file (json dump)

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
