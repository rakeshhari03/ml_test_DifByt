from app.database import base
from sqlalchemy import Column,Integer, String

class Forms(base):
    __tablename__="Form_table"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    message = Column(String(1000), nullable=False)

