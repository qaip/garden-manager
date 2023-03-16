from database.models import Garden
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        garden = self.db.query(Garden).filter(Garden.name == self.args['name']).first()
        if garden is None:
            print(f"'Garden '{self.args['name']}' not found")
        else:
            self.db.delete(garden)
            self.db.commit()
            print(f"Removed garden '{self.args['name']}'")
