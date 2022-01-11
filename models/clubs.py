"""
Model file for clubs
"""
from server import db


# ex : {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
class Club:
    """
    Model for club objects
    """
    __tablename__ = 'Clubs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    points = db.Column(db.Integer)

    def __init__(self, name, email, points):
        self.name = name
        self.email = email
        self.points = points

    def __repr__(self):
        return f'{self.name}'
