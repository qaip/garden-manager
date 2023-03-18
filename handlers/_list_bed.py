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
            plants_query = self.db.query(Plant.stage)
            for bed in beds:
                stages = plants_query.filter_by(bed_id=bed[0]).all()
                plants.append((
                    Handler.num_stages(stages, GardenHandler.PlantStage.SEED),
                    Handler.num_stages(stages, GardenHandler.PlantStage.SPROUT),
                    Handler.num_stages(stages, GardenHandler.PlantStage.SMALL_PLANT),
                    Handler.num_stages(stages, GardenHandler.PlantStage.ADULT_PLANT),
                ))
            print(tabulate(
                [(*bed, *plants[index]) for index, bed in enumerate(beds)],
                headers=['Id', 'Size', 'Life Factor', 'Seeds',
                         'Spouts', 'Small Plants', 'Adult Plants'],
                numalign='center'
            ))
        else:
            plants_query = self.db.query(Plant.id, Plant.name, Plant.stage)
            for index, bed in enumerate(beds):
                plants = (plants_query.filter(Plant.bed_id == bed[0]).all())
                if index:
                    print()
                print(
                    f"Bed: {bed[0]} | size: {bed[1]} "
                    f"| seeded: {len(plants)} | life factor: {bed[2]}")
                print(tabulate(
                    plants,
                    headers=['Id', 'Name', 'Stage'],
                    numalign='center'
                ))

    @staticmethod
    def num_stages(stages, target_stage: GardenHandler.PlantStage) -> int:
        return sum(GardenHandler.get_plant_stage(stage) == target_stage
                   for stage, in stages)
