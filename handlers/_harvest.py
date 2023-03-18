from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Query
from database.models import GardenBed, Plant
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        if bool(self.args['bed_id']) == bool(self.args['all']):
            print("Please specify either '--bed BED_ID' argument or '--all' flag")
            exit(1)
        if self.args['bed_id']:
            garden_bed = self.db.query(GardenBed).filter_by(
                id=self.args['bed_id']
            ).first()
            if garden_bed is None:
                print(f"Failed to harvest from bed: "
                      f"garden bed {self.args['bed_id']} does not exist")
                exit(1)
            query = self.db.query(Plant).filter_by(bed_id=self.args['bed_id'])
        else:
            query = self.db.query(Plant).join(GardenBed).filter_by(
                garden_id=self.current_garden_id)
        self.harvest(query)

    def harvest(self, query: Query):
        harvest = {}
        plants = query.all()
        for plant in plants:
            name = plant.name.strip()
            if name not in harvest:
                harvest[name] = 0
            harvest[name] += 1
        result = ", ".join([f"{count} {name + ('' if count == 1 else 's')}"
                            for name, count in harvest.items()])
        if result:
            if self.args['all']:
                print(f"Harvested {result} from the the whole garden")
            else:
                print(
                    f"Harvested {result} from garden bed {self.args['bed_id']}")
        else:
            if self.args['all']:
                print("Nothing to harvest from the garden")
            else:
                print(
                    f"Nothing to harvest from garden bed {self.args['bed_id']}")
