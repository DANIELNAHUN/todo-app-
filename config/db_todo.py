import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

usuario = os.getenv('USER_BD')
password = os.getenv('PASS_BD')
ip = os.getenv('IP_BD')
port = os.getenv('PORT_BD')
nombre_bd = os.getenv('NAME_BD')

connection = f"mysql+pymysql://{usuario}:{password}@{ip}:{port}/{nombre_bd}"
engine = create_engine(connection)
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind=engine)
Base = declarative_base()
meta = MetaData()