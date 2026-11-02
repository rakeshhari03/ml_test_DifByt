from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os

load_dotenv()

DB_URL=os.getenv("DATABASE_URL")

engine=create_engine(DB_URL)

sessionlocal=sessionmaker(bind=engine,autoflush=False, autocommit=False)

base=declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

