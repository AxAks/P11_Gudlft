"""
Model file for competitions
"""
from server import db


# ex : {"name": "Spring Festival", "date": "2020-03-27 10:00:00", "number_of_places": "25"}
class Competition(db.Model):
    """
    Model for competition objects
    """
    __tablename__ = 'Competitions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    number_of_places = db.Column(db.Integer)

    def __init__(self, name, date, number_of_places):
        self.name = name
        self.date = date
        self.number_of_places = number_of_places

    def __repr__(self):
        return f'{self.name}: {self.date}'
