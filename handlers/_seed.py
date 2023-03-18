from sqlalchemy.exc import IntegrityError
from database.models import Plant
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        plants = [Plant(name=self.args['name'], stage=0, bed_id=self.args['bed_id'])
                  for _ in range(self.args['count'])]
        try:
            self.db.bulk_save_objects(plants)
            self.db.commit()
        except IntegrityError:
            print(f"Failed to seed: garden bed '{self.args['bed_id']}' does not exist")
            exit(1)
        print(
            f"Seeded garden bed '{self.args['bed_id']}' with {self.args['count']} {self.args['name']}(s).")
