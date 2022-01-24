"""
Model file for clubs
"""
from database import db


# ex : {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
class Club(db.Model):
    """
    Model for club objects
    """
    __tablename__ = 'clubs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    points = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.name}'
