from sqlalchemy.exc import IntegrityError
from database.models import Garden
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self, server=False):
        super().__init__(server)
        try:
            self.db.add(Garden(name=self.args['name']))
            self.db.commit()
        except IntegrityError:
            self.print(
                f"Failed to create: garden '{self.args['name']}' already exists")
            exit(1)
        garden = self.db.query(Garden.id).filter_by(
            name=self.args['name']).first()
        if not garden:
            raise RuntimeError('Unable to create garden')
        self.print(f"Created garden '{self.args['name']}'")
        if self.args['use']:
            with open('.currentgarden', 'w', encoding='UTF-8') as stream:
                stream.write(str(garden[0]))
            self.print(f"Now using garden '{self.args['name']}'")
