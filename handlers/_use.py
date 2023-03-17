from database.models import Garden
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        garden = self.db.query(Garden.name).filter_by(name=self.args['name']).first()
        if garden is not None:
            with open('.currentgarden', 'w', encoding='UTF-8') as stream:
                stream.write(self.args['name'])
            print(f"Now using garden '{self.args['name']}'")
        else:
            print(f"Garden '{self.args['name']}' does not exist")
