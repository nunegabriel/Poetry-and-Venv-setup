from pydantic import BaseModel
import datetime


class Event(BaseModel):
    id: int
    name: str
    event:str
    creation_date: datetime.datetime
    modified_date: datetime.datetime

    class Config:
        orm_mode = True

class CreateEvent(Event):
    pass