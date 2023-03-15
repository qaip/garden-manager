from argyaml import BaseHandler


class Handler(BaseHandler):
    def __init__(self) -> None:
        with open('.currentgarden', 'w') as stream:
            stream.write(self.args.get('garden-name', ''))
