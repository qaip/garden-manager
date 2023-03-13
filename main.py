from handlers import BaseHandler
from arguments import args

def main():
    BaseHandler(['custom', '--argument'], config='./custom-config.yaml',
                path='my_custom_handlers', handlers=lambda c: c)
    print(vars(args))


class CustomHandler(BaseHandler):
    config = './custom-config.yaml'
    path ='my_custom_handlers'
    handlers = lambda c: c

if __name__ == '__main__':
    main()


class CustomHandler(BaseHandler.meta('garden')):
    difosidfjo:
