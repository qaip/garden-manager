from handlers import BaseHandler
from arguments import args
from dotenv import load_dotenv


def main():
    BaseHandler(vars(args))
    print(vars(args))


if __name__ == '__main__':
    main()
