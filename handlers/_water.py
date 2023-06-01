from sqlalchemy.exc import IntegrityError
from database.models import Plant
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self, server=False):
        super().__init__(server)
        increase = 20 if self.args['intensive'] else 10
        try:
            self.db.query(Plant).filter_by(
                bed_id=self.args['bed_id']
            ).update({"stage": Plant.stage + increase})
            self.db.commit()
        except IntegrityError:
            self.print(
                f"Failed to water: garden bed '{self.args['bed_id']}' does not exist")
            exit(1)
        self.print(
            f"Watered garden bed {self.args['bed_id']} (+{increase})")
