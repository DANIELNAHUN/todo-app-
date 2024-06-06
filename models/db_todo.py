import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

connection = f"mysql+pymysql://{os.getenv('USER_TODOAPP')}:{os.getenv('PASS_TODOAPP')}@{os.getenv('IP_TODOAPP')}:{os.getenv('PORT_TODOAPP')}/{os.getenv('NAME_TODOAPP')}"
engine = create_engine(connection)
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind=engine)
Base = declarative_base()
meta = MetaData()