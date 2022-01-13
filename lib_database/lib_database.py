"""
Lib for functions related to database queries
"""
from typing import Union, List

from models.clubs import Club
from models.competitions import Competition
from config import db


def get_all_clubs() -> List[Club]:
    return Club.query.all()


def get_all_competitions() -> List[Competition]:
    return Competition.query.all()


def get_club_by_email(email: str, clubs: List[Club]) -> Union[Club, None]:
    """
    Searches a club whose registered contact email matches the email given as parameter
    """
    for club in clubs:
        if email == club.email:
            return club


def get_club_by_name(name: str, clubs: List[Club]) -> Union[Club, None]:
    """
    Enables to get a club infos from its name
    """
    for club in clubs:
        if name == club.name:
            return club


def get_competition_by_name(competition_name: str, competitions: List[Competition]) -> Union[Competition, None]:
    """
    Enables to get a competition infos from its name
    """
    for competition in competitions:
        if competition_name == competition.name:
            return competition


def update_competition_places(competition: Competition, new_number_of_places) -> Competition: # rediger un test
    competition.number_of_places = new_number_of_places
    competition_in_db = Competition.query.filter_by(id=competition.id).first()
    competition_in_db.number_of_places = new_number_of_places
    db.session.commit()
    return competition


def update_club_points(club: Club, new_points) -> Club:  # rediger un test
    club.points = new_points
    club_in_db = Competition.query.filter_by(id=club.id).first()
    club_in_db.points = new_points
    db.session.commit()
    return club
