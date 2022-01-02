"""
Main File
containing flask routing functions
"""

from config import app, db_path, gudlft_database, competitions, clubs
from utils import save

from flask import render_template, request, redirect, flash, url_for

from lib_general.lib_general import check_competition_places, check_club_points, check_booking_possible
from lib_request.lib_request import extract_club_email, extract_competition_name,\
    extract_club_name, extract_required_places
from lib_database.lib_database import get_club_by_email, get_competition_by_name, get_club_by_name, \
    update_club_points_for_db, update_competition_places_for_db


@app.route('/')
def index():
    """
    Displays to the website homepage
    """
    return render_template('index.html', clubs=clubs) # clubs : tests


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


@app.route('/book/<competition_name>/<club_name>')
def book(competition_name, club_name):
    """
    leads the user to the ticket booking page for a given competition

    """
    club = get_club_by_name(club_name)
    competition = get_competition_by_name(competition_name)
    if club and competition:
        return render_template('booking.html', club=club, competition=competition)
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
    total_places_as_int = int(competition['number_of_places'])
    total_points_as_int = int(club['points'])

    has_enough_places = check_competition_places(places_required_as_int, total_places_as_int)
    has_enough_points = check_club_points(places_required_as_int, total_points_as_int)
    booking_is_possible = check_booking_possible(has_enough_places, has_enough_points)

    if not has_enough_places:
        flash('You cannot purchase this amount of place. There are not enough places left!')

    if not has_enough_points:
        flash('You cannot purchase this amount of place. You do not have enough points!')

    if booking_is_possible:
        club['points'] = total_points_as_int - places_required_as_int
        competition['number_of_places'] = total_places_as_int - places_required_as_int

        update_club_points_for_db(club)
        update_competition_places_for_db(competition)
        save(gudlft_database, db_path)
        flash('Great-booking complete!')

    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display (no need to be logged, on the homepage)
@app.route('/display_points', methods=['GET'])
def display_points():
    """
    Displays a page with showing points for all registered clubs
    """
    return render_template('clubs_points.html', clubs=clubs)


@app.route('/logout')
def logout():
    """
    Enables the user to logout and be redirected to the homepage
    """
    return redirect(url_for('index'))
