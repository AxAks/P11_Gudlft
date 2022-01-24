"""
Model file for competitions
"""
from database import db


# ex : {"name": "Spring Festival", "date": "2020-03-27 10:00:00", "number_of_places": "25"}
class Competition(db.Model):
    """
    Model for competition objects
    """
    __tablename__ = 'competitions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    number_of_places = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.name}: {self.date}'
