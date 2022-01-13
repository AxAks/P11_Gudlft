"""
Main File
containing flask routing functions
"""
from config import app

from flask import render_template, request, redirect, flash, url_for

from lib_general.lib_general import check_competition_places, check_club_points, check_booking_possible,\
    check_competition_date, is_email_blank, check_required_places_amount
from lib_request.lib_request import extract_club_email, extract_competition_name,\
    extract_club_name, extract_required_places
from lib_database.lib_database import get_club_by_email, get_all_clubs, get_all_competitions, get_club_by_name,\
    get_competition_by_name, update_club_points, update_competition_places


clubs = get_all_clubs()
competitions = get_all_competitions()


@app.route('/')
def index():
    """
    Displays to the website homepage
    """
    return render_template('index.html', clubs=clubs)


@app.route('/show_summary', methods=['POST'])
def show_summary():
    """
    Redirects the user to their account summary page if the entered email is correct
    or asks to retry with a valid address
    """
    email = extract_club_email(request)
    if is_email_blank(email):
        flash("Please enter a valid email")
        return redirect(url_for('index'))
    club = get_club_by_email(email, clubs)
    if not club:
        flash("The entered email could not be found, please enter a registered email")
        return redirect(url_for('index'))
    else:
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition_name>/<club_name>')
def book(competition_name, club_name):
    """
    leads the user to the ticket booking page for a given competition

    """
    club = get_club_by_name(club_name, clubs)
    competition = get_competition_by_name(competition_name, competitions)
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
    places_required = extract_required_places(request.form)

    competition = get_competition_by_name(competition_name, competitions)
    club = get_club_by_name(club_name, clubs)

    competition_date = competition.date
    total_places = competition.number_of_places
    total_points = club.points

    has_enough_places = check_competition_places(places_required, total_places)
    has_enough_points = check_club_points(places_required, total_points)
    competition_is_in_the_future = check_competition_date(competition_date)
    places_required_is_below_limit = check_required_places_amount(places_required)

    booking_is_possible = check_booking_possible(has_enough_places, has_enough_points,
                                                 competition_is_in_the_future, places_required_is_below_limit)

    if not places_required_is_below_limit:
        flash('You cannot purchase this amount of places. This is over the purchase limit per club for a competition!')

    if not has_enough_places:
        flash('You cannot purchase this amount of places. There are not enough places left!')

    if not has_enough_points:
        flash('You cannot purchase this amount of places. You do not have enough points!')

    if not competition_is_in_the_future:
        flash('You cannot purchase places for this competition. The competition is over!')

    if booking_is_possible:
        new_points = total_points - places_required
        new_number_of_places = total_places - places_required

        update_club_points(club, new_points)
        update_competition_places(competition, new_number_of_places)
        flash('Great-booking complete!')

    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/logout')
def logout():
    """
    Enables the user to logout and be redirected to the homepage
    """
    return redirect(url_for('index'))
