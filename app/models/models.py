from sqlalchemy import  Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    event = Column(String)
    creation_date = Column(DateTime)
    modified_date = Column(DateTime)