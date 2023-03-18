from database.models import Garden
from handlers import GardenHandler


class Handler(GardenHandler):
    def __init__(self):
        garden = self.db.query(Garden).filter_by(name=self.args['name']).first()
        if garden is None:
            print(f"Garden '{self.args['name']}' does not exist")
        else:
            try:
                if self.safe_current_garden_id == garden.id:
                    with open('.currentgarden', 'w', encoding='UTF-8') as stream:
                        stream.write('')
            except FileNotFoundError:
                pass
            self.db.delete(garden)
            self.db.commit()
            print(f"Removed garden '{self.args['name']}'")
