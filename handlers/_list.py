from handlers import GardenHandler
from database.models import Garden


class Handler(GardenHandler):
    def __init__(self, server=False):
        super().__init__(server)
        gardens = self.db.query(Garden.id, Garden.name).all()
        for garden_id, garden_name in gardens:
            prefix = '*' if self.safe_current_garden_id == garden_id else ' '
            self.print(prefix, garden_name)
