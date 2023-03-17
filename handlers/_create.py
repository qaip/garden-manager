from database.models import Garden
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        self.db.add(Garden(name=self.args['name']))
        self.db.commit()
        print(f"Created garden '{self.args['name']}'")
