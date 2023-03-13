from argyaml import BaseHandler

class Handler(BaseHandler.meta('Default')):
    def __init__(self):
        print('Hello from default generate handler')
        # Generate files here!
