from handlers import BaseHandler


class Handler(BaseHandler):
    def __init__(self) -> None:
        with open('.currentgarden', 'w') as stream:
            stream.write(BaseHandler._args.get('garden-name', ''))
