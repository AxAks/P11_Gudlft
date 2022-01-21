"""
Lib for functions related to databases queries
"""
from typing import Union, List

from models.clubs import Club
from models.competitions import Competition
from config import db


def get_all_clubs() -> List[Club]:
    return Club.query.all()


def get_all_competitions() -> List[Competition]:
    return Competition.query.all()


def get_club_by_email(email: str) -> Union[Club, None]:
    """
    Searches a club whose registered contact email matches the email given as parameter
    """
    return Club.query.filter_by(email=email).first()


def get_club_by_name(name: str) -> Union[Club, None]:
    """
    Enables to get a club infos from its name
    """
    return Club.query.filter_by(name=name).first()


def get_competition_by_name(name: str) -> Union[Competition, None]:
    """
    Enables to get a competition infos from its name
    """
    return Competition.query.filter_by(name=name).first()


def update_competition_places(competition: Competition, new_number_of_places) -> Competition: # rediger un test
    competition.number_of_places = new_number_of_places
    db.session.commit()
    return competition


def update_club_points(club: Club, new_points) -> Club:  # rediger un test
    club.points = new_points
    db.session.commit()
    return club
