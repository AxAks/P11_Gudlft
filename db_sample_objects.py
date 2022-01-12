from datetime import datetime

from models.clubs import Club
from models.competitions import Competition

club1 = Club(name="Simply Lift", email="john@simplylift.co", points=13)
club2 = Club(name="Iron Temple", email="admin@irontemple.com", points=4)
club3 = Club(name="She Lifts", email="kate@shelifts.co.uk", points=12)

competition1 = Competition(name="Spring Festival",
                           date=datetime.strptime("2020-03-27 10:00:00", '%Y-%m-%d %H:%M:%S'), number_of_places=25)
competition2 = Competition(name="Fall Classic",
                           date=datetime.strptime("2020-10-22 13:30:00", '%Y-%m-%d %H:%M:%S'), number_of_places=13)

# db.session.add(club1)
# db.session.add(club2)
# db.session.add(club3)
# db.session.add(competition1)
# db.session.add(competition2)
# db.session.commit()
