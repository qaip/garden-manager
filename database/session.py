import os
import sqlalchemy as sql
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker


USER = os.environ['POSTGRES_USER']
PASSWORD = os.environ['POSTGRES_PASSWORD']
PORT = os.environ['POSTGRES_PORT']
DB = os.environ['POSTGRES_DB']

DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@localhost/{DB}'

engine = sql.create_engine(DATABASE_URI)

try:
    engine.connect()
except SQLAlchemyError as err:
    print('Connection refused.\nCheck connection')
    exit(1)

make_session = sessionmaker(bind=engine)
