from database.models import Garden, GardenBed, Plant
from handlers import GardenHandler
from tabulate import tabulate
import garden


class Handler(GardenHandler):
    def __init__(self):
        beds = self.db.query(
            GardenBed.id,
            GardenBed.size,
            GardenBed.life_factor
        ).filter_by(garden_id=self.current_garden_id).all()
        plants = []
        if not self.args['details']:
            plants_query = self.db.query(Plant.id)
            for bed in beds:
                plants.append((
                    plants_query.filter(Plant.bed_id == bed[0]).count(),
                    plants_query.filter(
                        Plant.bed_id == bed[0],
                        Plant.stage > garden.Plant.Stage.ADULT_PLANT.value
                    ).count()
                ))
            print(tabulate(
                [(*bed, *plants[index]) for index, bed in enumerate(beds)],
                headers=['Id', 'Size', 'Life Factor',
                         'Total Plants', 'Adult Plants'],
                numalign='center'
            ))
        else:
            plants_query = self.db.query(Plant.id, Plant.name, Plant.stage)
            for index, bed in enumerate(beds):
                if index:
                    print()
                print(
                    f"Bed: {bed[0]} | size: {bed[1]} | life factor: {bed[2]}")
                plants = (plants_query.filter(Plant.bed_id == bed[0]).all())
                print(tabulate(
                    plants,
                    headers=['Id', 'Name', 'Stage'],
                    numalign='center'
                ))
