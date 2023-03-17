from handlers import GardenHandler
from database.models import Garden


class Handler(GardenHandler):
    def __init__(self):
        garden_names = self.db.query(Garden.name).all()
        try:
            current_garden = self.current_garden
        except FileNotFoundError:
            current_garden = None
        for garden_name, in garden_names:
            prefix = '*' if current_garden == garden_name else ' '
            print(prefix, garden_name)
