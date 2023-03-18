from database.models import Garden
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        self.db.add(Garden(name=self.args['name']))
        self.db.commit()
        garden = self.db.query(Garden.id).filter_by(name=self.args['name']).first()
        if not garden:
            raise RuntimeError('Unable to create garden')
        print(f"Created garden '{self.args['name']}'")
        if self.args['use']:
            with open('.currentgarden', 'w', encoding='UTF-8') as stream:
                stream.write(str(garden[0]))
            print(f"Now using garden '{self.args['name']}'")
