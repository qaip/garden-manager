from database.models import Garden
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        garden = self.db.query(Garden.id).filter_by(name=self.args['name']).first()
        if garden is not None:
            with open('.currentgarden', 'w', encoding='UTF-8') as stream:
                stream.write(str(garden[0]))
            print(f"Now using garden '{self.args['name']}'")
        else:
            print(f"Failed to use: garden '{self.args['name']}' does not exist")
