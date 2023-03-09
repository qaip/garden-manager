from handlers import BaseHandler


class Handler(BaseHandler):
    def __init__(self) -> None:
        print(BaseHandler.get_current_garden())
