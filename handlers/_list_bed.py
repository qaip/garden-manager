from database.models import Garden, GardenBed
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        beds = self.db.query(
            GardenBed.id,
            GardenBed.size,
            GardenBed.life_factor
        ).join(
            Garden, Garden.id == GardenBed.garden_id
        ).filter(Garden.name == self.current_garden)

        print(*beds, sep='\n')
