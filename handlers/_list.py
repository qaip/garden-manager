from handlers import GardenHandler
from database.models import Garden


class Handler(GardenHandler):
    def __init__(self):
        garden_names = self.db.query(Garden.name).all()
        for garden_name, in garden_names:
            print(garden_name)
