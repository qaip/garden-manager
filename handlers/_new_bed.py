from argyaml import BaseHandler


class Handler(BaseHandler.meta()):
    def __init__(self):
        print('Successfully created a new bed')
