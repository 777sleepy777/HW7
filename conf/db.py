
import configparser
import  pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')
db_name  = config.get('DB', 'DB_NAME')
domain   = config.get('DB', 'DOMAIN')
port     = config.get('DB', 'PORT')

url = f'postgresql://{username}:{password}@{domain}:{port}/{db_name}'
engine = create_engine(url, pool_size=5, max_overflow=0, echo=True)
DBSessinn = sessionmaker(engine)
session = DBSessinn()

