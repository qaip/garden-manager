from database.models import Garden, GardenBed, Plant
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self, server=False):
        super().__init__(server)
        garden = self.db.query(Garden).filter_by(
            name=self.args['name']).first()
        if garden is None:
            self.print(f"Failed to delete: "
                       f"garden '{self.args['name']}' does not exist")
        else:
            if not self.args['force']:
                bed = self.db.query(GardenBed).filter_by(
                    garden_id=garden.id).first()
                if bed is not None:
                    self.print(f"Failed to delete: "
                               f"garden '{self.args['name']}' is not empty")
                    self.print(
                        "Use '--force' flag to delete garden with all its contents")
                    exit(1)
            else:
                beds = self.db.query(GardenBed).filter_by(
                    garden_id=garden.id)
                for bed in beds:
                    self.db.query(Plant).filter_by(bed_id=garden.id).delete()
                beds.delete()
            try:
                if self.safe_current_garden_id == garden.id:
                    with open('.currentgarden', 'w', encoding='UTF-8') as stream:
                        stream.write('')
            except FileNotFoundError:
                pass
            self.db.delete(garden)
            self.db.commit()
            if not self.args['force']:
                self.print(f"Deleted garden '{self.args['name']}'")
            else:
                self.print(
                    f"Deleted garden '{self.args['name']}' with all its contents")
