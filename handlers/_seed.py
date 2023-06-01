from sqlalchemy.exc import IntegrityError
from database.models import GardenBed, Plant
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self, server=False):
        super().__init__(server)
        garden_bed_size = self.db.query(GardenBed.size).filter_by(
            id=self.args['bed_id']).first()
        num_existing_plants = self.db.query(Plant).filter_by(
            bed_id=self.args['bed_id']).count()
        if garden_bed_size is None:
            self.print(f"Failed to seed: garden bed "
                       f"'{self.args['bed_id']}' does not exist")
            exit(1)
        available_size = garden_bed_size[0] - num_existing_plants
        if self.args['count'] > available_size:
            self.print(f"Failed to seed: garden bed has a maximum of "
                       f"{available_size} free places for plants")
            exit(1)
        plants = [Plant(
            name=self.args['name'],
            stage=0,
            bed_id=self.args['bed_id']
        ) for _ in range(self.args['count'])]
        self.db.bulk_save_objects(plants)
        self.db.commit()
        self.print(f"Seeded garden bed {self.args['bed_id']} with "
                   f"{self.args['count']} {self.args['name']}"
                   f"{'' if self.args['count'] == 1 else 's'}")
