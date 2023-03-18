from database.models import Garden, GardenBed
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        self.db.add(GardenBed(size=self.args['size'], life_factor=100, garden_id=self.current_garden_id))
        self.db.commit()
        print(f"Created garden bed of size {self.args['size']}")
